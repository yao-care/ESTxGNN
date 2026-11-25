"""依原收集規則補收 CIMA 現行清單有、證據包沒收的本藥許可（2026-11-25 第五輪，用戶決定；全程不用 AI）。

問題：證據包的許可是 collectors/esfda.py 依 data/processed/drug_mapping.csv（2026-03 CIMA 清單的 principiosActivos → DrugBank ID）
收的：藥名 → DrugBank ID → drug_mapping 裡同一個 ID 的 nregistro → data/raw/es_fda_drugs.json（2026-03 CIMA 清單）的那一列；
最多存 20 筆（單方在前），total_matches 是全部筆數。2026-03 之後核准的許可（含平行輸入 IP 號）不在 drug_mapping、
也不在 es_fda_drugs.json，永遠收不進來。

證據包收集的時間不同，用到的 drug_mapping 也不同：2026-10-12 rescue_mapping 補救（複方拆成分等）之前收的證據包照
drug_mapping.csv.bak_20261012，之後收的照現行 drug_mapping.csv。每個證據包第一次跑時，照兩份對照分別在 es_fda_drugs.json
重算一次原收集器的結果，**張數正好等於 total_matches、而且證據包現有紀錄都在裡面**的那份就是它的收集規則（兩份都對就用現行），
記在 tfda.collection_rule；當時算進 total_matches 卻因 20 筆上限沒存的號碼回填到 tfda.records_not_stored（避免重複計數）。
重算不出來的證據包（張數對不上）整個不補、列進報告（停損，不推定）。

補收（只加不刪、可重複執行）：CIMA 現行清單（license_adapter.fetch() 的 /medicamentos 全量，含撤銷、暫停、平行輸入）的每一筆，
- nregistro 在該證據包收集規則那份 drug_mapping 裡、對到本藥 DrugBank ID 的 → 原規則的號碼對照；
- nregistro 不在那份 drug_mapping（2026-03 之後的新許可）→ 成分（vtm，與 2026-03 清單的 principiosActivos 寫法相同，2026-11-25 量測
  99.7% 一致）照同一份 drug_mapping 已有的「原始成分字串 → DrugBank ID」對照；那份對照沒見過的字串用本站 Phase 1 的
  mapping/drugbank_mapper（map_fda_drugs_to_drugbank 同一套）對；現行對照另照 rescue 的做法把「a + b」拆成分、每個成分都要對得到。
對到本藥、證據包還沒有（records、records_not_stored、excluded_records）的就補：records 未滿 20 筆存進 records（單方在前），
滿了只記號碼在 records_not_stored；兩者都算進 total_matches。每筆記 source（清單與日期、規則）與 added（補收日）。
狀態照 license_adapter（Revocada／Suspendida／Autorizada／Autorizada (no comercializada)）。

不改的：rescue 之前收的證據包，用現行對照會多對到的 2026-03 舊許可（多是複方）不是新許可，這支不補（數字見 2026-11-25 CLAUDE.md）。

用法（repo 根目錄）：python3 scripts/add_current_licenses.py [--download] [--dry-run] [--report out.tsv]
每週排程（.github/workflows/license-refresh.yml）在 license_refresh 前以 --download 跑。
"""
import csv
import datetime
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "src"))
import license_adapter as A  # noqa: E402

BUNDLES = ROOT / "data/bundles"
RAW = ROOT / "data" / A.RAW_FILE
BASE_LIST = ROOT / "data/raw/es_fda_drugs.json"
MAPS = {"drug_mapping.csv": ROOT / "data/processed/drug_mapping.csv",
        "drug_mapping.csv.bak_20261012": ROOT / "data/processed/drug_mapping.csv.bak_20261012"}
CUR = "drug_mapping.csv"
VOCAB = ROOT / "data/external/drugbank_vocab.csv"
CAP = 20
csv.field_size_limit(10**9)


def norm(t):
    t = unicodedata.normalize("NFKD", str(t or "")).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()


def key(t):
    return re.sub(r"\s+", " ", str(t or "")).strip().lower()


def load_map(p):
    """同 esfda.LocalFDACollector：成分 → ID、ID → 許可證；另存原始成分字串 → ID（給新許可用）、對照裡的全部號碼"""
    ing, lic, oi, ids_all = {}, {}, {}, set()
    with open(p, encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            lid = str(row.get("license_id") or "").strip()
            ids_all.add(lid)
            o = norm(row.get("original_ingredient"))
            oi.setdefault(o, set())
            db = str(row.get("drugbank_id") or "").strip().upper()
            if not db or str(row.get("mapping_success")).strip().lower() not in ("true", "1", "yes"):
                continue
            oi[o].add(db)
            for k in {norm(row.get("normalized_ingredient")), key(row.get("normalized_ingredient"))}:
                if k:
                    ing.setdefault(k, set()).add(db)
            if lid:
                lic.setdefault(db, set()).add(lid)
    return {"ing": ing, "lic": lic, "oi": oi, "ids": ids_all}


def vtm(r):
    return str(((r.get("vtm") or {}).get("nombre")) or "").strip()


class Phase1:
    """本站 Phase 1 的成分 → DrugBank 對照（mapping/drugbank_mapper.map_fda_drugs_to_drugbank 同一套），只在對照沒見過的字串用"""
    def __init__(self):
        from estxgnn.mapping import drugbank_mapper as M
        from estxgnn.mapping.normalizer import get_all_synonyms
        self.M, self.syn = M, get_all_synonyms
        self.idx = M.build_name_index(M.load_drugbank_vocab())
        self.cache = {}

    def ids(self, s):
        if s not in self.cache:
            out = set()
            for main, syns in self.syn(s):
                db = self.M.map_ingredient_to_drugbank(main, self.idx)
                for sy in ([] if db else syns):
                    db = self.M.map_ingredient_to_drugbank(sy, self.idx)
                    if db:
                        break
                if db:
                    out.add(db)
            self.cache[s] = out
        return self.cache[s]


def new_ids(r, mp, rule, p1):
    """不在該份 drug_mapping 的許可：成分字串 → DrugBank ID"""
    v = vtm(r)
    if not v:
        return set()
    n = norm(v)
    if mp["oi"].get(n):
        return mp["oi"][n]
    comps = [c for c in re.split(r"\s*\+\s*", v) if c.strip()]
    if rule == CUR and len(comps) > 1:  # rescue_20261012 的複方規則：拆開逐一對，每個成分都要對得到
        got = [mp["oi"].get(norm(c)) or p1.ids(c) for c in comps]
        return set().union(*got) if all(got) else set()
    if n in mp["oi"]:  # 對照見過、當時就對不到（failed）
        return set()
    return p1.ids(v) if len(comps) == 1 or rule != CUR else set()


def drug_ids(b, mp, vocab):
    drug = (b.get("drug") or {}).get("inn") or ""
    s = set(str(x).upper() for x in (b.get("tfda") or {}).get("drugbank_ids") or [])
    for k in (norm(drug), key(drug)):
        s |= mp["ing"].get(k, set()) | vocab.get(k, set())
    return s


def ncomp(r):
    return len(re.split(r"[,;+/&]|&&| and | y ", vtm(r) or "x"))


def main(argv):
    dry = "--dry-run" in argv
    rep = argv[argv.index("--report") + 1] if "--report" in argv else None
    today = datetime.date.today().isoformat()
    if "--download" in argv:
        cur = A.fetch()
        RAW.write_text(json.dumps(cur, ensure_ascii=False), encoding="utf-8")
    else:
        try:
            cur = json.loads(RAW.read_text(encoding="utf-8"))
        except Exception as e:
            raise SystemExit(f"讀不到現行清單 {RAW}：{e}")
    if len(cur) < A.MIN_LISTED:
        raise SystemExit(f"現行清單只有 {len(cur)} 筆，疑似下載或格式有問題，不補收")
    ldate = datetime.date.fromtimestamp(RAW.stat().st_mtime).isoformat()
    curd = {str(r.get("nregistro") or "").strip(): r for r in cur if r.get("nregistro")}
    try:
        maps = {k: load_map(p) for k, p in MAPS.items() if p.exists()}
        base = {str(r["nregistro"]) for r in json.loads(BASE_LIST.read_text(encoding="utf-8"))} if BASE_LIST.exists() else None
        vocab = {}
        with open(VOCAB, encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f):
                vocab.setdefault(norm(row.get("drug_name")), set()).add(str(row.get("drugbank_id", "")).upper())
    except Exception as e:
        raise SystemExit(f"讀不到對照資料：{e}")
    if CUR not in maps:
        raise SystemExit("沒有 data/processed/drug_mapping.csv，不補收")
    p1 = Phase1()
    # 每份對照：現行清單每筆許可 → 對到的 DrugBank ID（原號碼對照，或新許可的成分對照）
    cand = {}
    for rule, mp in maps.items():
        by_db = {}
        lic_db = {}
        for db, ls in mp["lic"].items():
            for lid in ls:
                lic_db.setdefault(lid, set()).add(db)
        for lid, r in curd.items():
            dbs = lic_db.get(lid, set()) if lid in mp["ids"] else new_ids(r, mp, rule, p1)
            for db in dbs:
                by_db.setdefault(db, []).append(lid)
        cand[rule] = by_db
    rows, nb, nrec, nfill, gaps, nrule = [], 0, 0, 0, [], 0
    for f in sorted(BUNDLES.glob("*/drug_bundle.json")):
        page = f.parent.name
        try:
            b = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            raise SystemExit(f"讀不到證據包 {f}：{e}")  # 讀不到資料就停，不當成沒有紀錄
        t = b.get("tfda") or {}
        if not t:
            continue
        recs = list(t.get("records") or [])
        not_stored = [str(x) for x in t.get("records_not_stored") or []]
        have = {str(r.get("license_id") or "") for k in ("records", "excluded_records") for r in (t.get(k) or [])} | set(not_stored)
        total = int(t.get("total_matches") or len(recs))
        rule = t.get("collection_rule")
        changed = False
        if not rule:  # 第一次：找出收集規則、回填當時沒存的號碼
            if base is None:
                rows.append(f"{page}\t-\t(沒有 es_fda_drugs.json，判斷不了收集規則)\tskipped_rule\t")
                gaps.append(page)
                continue
            filled = {str(r.get("license_id")) for r in recs if r.get("source")}  # es_fill_by_cima 依成分補入的（total_matches 已含）
            plain = {str(r.get("license_id")) for r in recs} - filled
            for rn in (CUR, "drug_mapping.csv.bak_20261012"):
                if rn not in maps:
                    continue
                mp = maps[rn]
                ids = drug_ids(b, mp, vocab)
                m = {lid for db in ids for lid in mp["lic"].get(db, ()) if lid in base}
                if len(m) + len(filled) == total and plain <= m:
                    rule = rn
                    hid = sorted(m - have)
                    if hid:
                        not_stored += hid
                        have |= set(hid)
                        nfill += 1
                        rows.append(f"{page}\t-\t({len(hid)} hidden IDs)\tbackfill_not_stored\t{rn}")
                    break
            if not rule:
                gaps.append(page)
                rows.append(f"{page}\t-\t(兩份對照都重算不出 total_matches {total})\tskipped_rule\t")
                continue
            nrule += 1
            changed = True
        if total - len(recs) - len(not_stored) > 0:
            gaps.append(page)
            rows.append(f"{page}\t-\t(total_matches 比已知號碼多 {total - len(recs) - len(not_stored)} 張)\tskipped_gap\t")
            continue
        if rule not in maps:
            gaps.append(page)
            rows.append(f"{page}\t-\t(沒有 {rule})\tskipped_rule\t")
            continue
        ids = drug_ids(b, maps[rule], vocab)
        want = {lid for db in ids for lid in cand[rule].get(db, ())} - have
        src = (f"CIMA /medicamentos ({ldate}); matched by the original collector rule ({rule}"
               f"{'' if rule == CUR else ', pre-2026-10-12 mapping used when this bundle was collected'})")
        added = []
        for lid in sorted(want, key=lambda x: (ncomp(curd[x]) > 1, x)):
            r = curd[lid]
            st, comerc = A._status(r)
            rec = {"license_id": lid, "brand_name_zh": r.get("nombre", ""), "brand_name_en": vtm(r), "ingredients": vtm(r), "indication": "",
                   "dosage_form": ((r.get("formaFarmaceutica") or {}).get("nombre") or ""), "manufacturer": r.get("labtitular", ""),
                   "license_holder": r.get("labtitular", ""), "approval_date": "", "expiry_date": "", "status": st,
                   "comercializado": comerc, "source": src, "added": today}
            total += 1
            if len(recs) < CAP:
                recs.append(rec)
                where = "records"
            else:
                not_stored.append(lid)
                where = "not_stored"
            added.append(lid)
            rows.append(f"{page}\t{lid}\t{r.get('nombre', '')}\t{where}\t{vtm(r)}\t{st}")
        if not added and not changed:
            continue
        nb += bool(added)
        nrec += len(added)
        t2 = dict(t, records=recs, total_matches=total, found=bool(recs), collection_rule=rule)
        if not_stored:
            t2["records_not_stored"] = not_stored
        if not dry:
            b["tfda"] = t2
            f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    if rep:
        Path(rep).write_text("page\tlicense_id\tproduct\twhere\tingredients\tstatus\n" + "\n".join(rows) + "\n", encoding="utf-8")
    if nrule:
        print(f"記下收集規則：{nrule} 個證據包（回填 records_not_stored {nfill} 個）")
    if gaps:
        print(f"⚠ 判斷不了收集規則或已算進總數卻不知道號碼、這次不補的證據包 {len(gaps)} 個：{', '.join(gaps[:20])}")
    print(f"{'（試跑）' if dry else ''}依原收集規則補收：{nb} 個證據包、{nrec} 筆（現行清單 {len(curd)} 筆，{ldate}）")


if __name__ == "__main__":
    main(sys.argv[1:])
