"""ES（AEMPS CIMA）許可證下載與狀態對應，給 tools/txgnn/.claude/license_refresh_20261029.py 用（2026-10-29）。

來源：https://cima.aemps.es/cima/rest/medicamentos（公開 REST，免金鑰，每頁 200 筆，約 130 頁）。
狀態規則沿用 2026-10-21 es_cima_status（pm 第 7 點）：estado 有 rev＝Revocada、有 susp＝Suspendida、
否則 comerc＝true 為 Autorizada，false 為 Autorizada (no comercializada)。
2026-11-17（用戶要求確認新資料查不到的許可證）：CIMA 清單本身就是完整登錄（含已撤銷、暫停的），但撤銷約 5 年後
會從 CIMA 移除（/medicamentos 清單與 /medicamento?nregistro= 單筆查詢都查不到）。2026-11-17 查不到的 232 張，
在 2026-03 的 CIMA 清單全部是 Revocada（撤銷日 2021-03-30～2021-11-15），證據包也早已標 Revocada。
fetch() 把清單上所有 nregistro 存進 LISTED；preprocess 對清單沒有的號標 license_status＝cancelled 與
cima_not_listed（第一次發現日），status 原文不動；之後又出現在清單就取消標記。清單不完整（筆數少於 MIN_LISTED）時不判定。
"""
import time

import requests

RAW_FILE = "raw/cima_medicamentos_raw.json"
URL = "https://cima.aemps.es/cima/rest/medicamentos"
LISTED: set = set()   # fetch() 填：CIMA 清單上的全部 nregistro（含撤銷、暫停）；空的就不做「不在清單」判定
MIN_LISTED = 20000    # 少於這個數＝下載或格式有問題，不判定


def fetch():
    out, page, total = [], 1, None
    while True:
        for attempt in range(4):
            try:
                r = requests.get(URL, params={"pagina": page}, timeout=60)
                r.raise_for_status()
                d = r.json()
                break
            except Exception:
                if attempt == 3:
                    raise
                time.sleep(5 * (attempt + 1))
        rows = d.get("resultados") or []
        total = d.get("totalFilas", total)
        out += rows
        if not rows or len(out) >= (total or 0):
            break
        page += 1
        time.sleep(0.2)
    if total is None or len(out) < total:
        raise RuntimeError(f"只拿到 {len(out)}／{total} 筆")
    LISTED.clear()
    ids = {str(r.get("nregistro")).strip() for r in out if r.get("nregistro")}
    if len(ids) >= MIN_LISTED:
        LISTED.update(ids)
    return out


def confirmed_absent(lid):
    """給 license_refresh：CIMA 完整清單（含撤銷）有成功下載而且沒有這個號＝已不在 CIMA 登錄（撤銷逾約 5 年）"""
    lid = str(lid or "").strip()
    return bool(LISTED) and bool(lid) and lid not in LISTED


def preprocess(bundle):
    """CIMA 清單沒有的許可號標 license_status＝cancelled、cima_not_listed＝第一次發現日（status 原文不動）；
    又出現在清單的取消標記。有改回 True"""
    if not LISTED:
        return False
    today = time.strftime("%Y-%m-%d")
    ch = False
    for r in (bundle.get("tfda") or {}).get("records") or []:
        lid = str(r.get("license_id") or "").strip()
        if not lid:
            continue
        if lid in LISTED:
            if r.get("cima_not_listed"):
                r.pop("cima_not_listed", None)
                r.pop("license_status", None)
                ch = True
        elif not r.get("cima_not_listed"):
            r["cima_not_listed"] = today
            r["license_status"] = "cancelled"
            ch = True
    return ch


def validate(new, old):
    p = []
    if not new:
        return ["下載 0 筆"]
    miss = sum(1 for r in new if not r.get("nregistro") or not isinstance(r.get("estado"), dict) or "comerc" not in r)
    if miss / len(new) > 0.01:
        p.append(f"{miss} 筆缺 nregistro／estado／comerc 欄位")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


def _status(r):
    e = r.get("estado") or {}
    return ("Revocada" if "rev" in e else "Suspendida" if "susp" in e
            else "Autorizada" if r.get("comerc") else "Autorizada (no comercializada)"), r.get("comerc")


def status_index(new):
    return {str(r.get("nregistro")): _status(r) for r in new if r.get("nregistro")}


def record_id(rec):
    return str(rec.get("license_id") or "")


def update(rec, new):
    st, comerc = new
    if rec.get("status") == st and rec.get("comercializado") == comerc:
        return False
    rec["status"], rec["comercializado"] = st, comerc
    return True


# 2026-11-24（用戶決定）：市場段落的許可證表改由程式產生（scripts/sync_license_tables.py）。每週排程（母目錄
# license_refresh_20261029.py 的 sync_tables 掛鉤）對狀態有變的證據包重排程式表；3b 自我檢查另允許改的非表格行＝PAGE_NOTE
# （表下程式說明句、NONE_LINE、程式區塊標記、known_use_pages 的舊部分紀錄提示）。
PAGE_NOTE = (r"^(Se muestran? (la única|las \d+|\d+ de (al menos )?\d+) autorizaci(ón|ones) con este principio activo (recogidas )?en los "
             r"datos de CIMA \(AEMPS\).*|No se encontraron autorizaciones con este principio activo en los datos de CIMA \(AEMPS\).*|"
             r"Los datos solo contienen parte de los registros; la lista puede estar incompleta\.|<!-- licenses:(begin|end) -->)$")


def sync_tables(site_root, bundles):
    """狀態有變的藥：「Información de Mercado en España」的程式許可證表依證據包重排（comercializadas 在前），狀態照 CIMA 現行狀態；
    SHOW 句跟著改（規則見 scripts/sync_license_tables.py）。回傳 [(頁, 欄位, 前值, 後值)]"""
    import importlib.util
    from pathlib import Path
    p = Path(site_root) / "scripts/sync_license_tables.py"
    s = importlib.util.spec_from_file_location("es_sync_license_tables", p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    if not bundles:
        return []
    return m.run(only=set(bundles))
