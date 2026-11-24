"""正文許可證張數的程式改寫（2026-11-24 建，用戶決定把 KrTxGNN／MyTxGNN 的做法移植到本站；結構照 COTxGNN 的同名檔（同為西班牙文），
規則是本站 AEMPS CIMA 的西班牙文句型）。

正文裡「N autorizaciones (comercializadas／vigentes／revocadas…)」這類 CIMA 許可證張數敘述，由程式依許可證快照
（snapshots/es_licenses.json.gz 的 facts）改寫，每週資料更新後跟著改，不逐筆寫查核紀錄（同 Tw／Kr／My／CO：程式改寫的張數敘述是程式產生的正文）。

本站事實層：valid＝comercializada（Autorizada＋comercializado）、not_marketed＝autorizada no comercializada、
cancelled＝revocada或suspendida（含 cima_not_listed）；快照另存 susp（證據包裡 Suspendida 的筆數）。
只改「句型明確、數字確定是本藥許可證張數」的地方，其餘一律不動：
  - 句子要有許可證名詞（autorización(es)、registro(s)、AEMPS、CIMA；在市場段落「Información de Mercado en España」裡
    「N presentaciones／N productos／N medicamentos」也算），而且數字右邊緊接許可證名詞或狀態字；沒有交互作用、試驗、文獻等字樣。
  - 跳過：查核框（<!-- review -->）、程式許可證區塊（<!-- licenses -->）、表格列、標題、引言框、front matter；
    查核紀錄 replacement／anchor 所在的句子（改了紀錄會對不上）。
  - 整句不動（列在 skipped）：有保留（al menos、parcial、incomplet、puede haber más）、講證據包或查詢結果（datos compilados、consulta、
    devolvió、se encontraron、Evidence Pack）、相對數（otros、más、además de、restantes、adicionales）、劑型或廠商子集
    （comprimido、cápsula、inyectable、crema、oftálmic…、laboratorio、S.A.、pertenecen、titular）；事實層 partial 的頁整頁不動。
  - 數字不動：顯示筆數（se muestran／se listan／la tabla／listados、「N de M」的 N）、劑量與年份；文字數詞（dos、tres、ambas…）不認。
角色看數字右側：revocad／suspendid／cancelad／anulad→註銷（只寫 revocad 而有暫停的，讀法另含 註銷−暫停）；
autorizad… no comercializad／no comercializad→授權未上市；comercializad→上市（＝事實層 valid）；
vigente／válid／activ／en vigor→有效（本站「vigente」可讀成上市數或上市＋授權未上市數，兩種讀法都算對）；
de un solo principio activo／monofármaco／monocomponente→單方；en combinación／combinad→複方；其餘→總數。
同一行只要有一句含許可證數字而被略過，整行都不動（免得前後句數字對不上）。
同一句另有明確的有效／註銷數字時，沒有限定詞的數字確定是總數。
數字已等於該角色的任一合理讀法就不動；不等於時各讀法相同才改，不同就列為 ambiguous。
原數字是 0 的句子（建立在 0 張前提上）不改、列為 zero-premise；改寫會跨過 1（名詞與形容詞單複數要跟著變）的不改、列為 plural；要改請寫查核紀錄。
前提檢查：句子說「todas (están) vigentes／comercializadas、ninguna revocada」而事實不符、說全部是單方或全部是複方而事實不符時整句不動、列出（premise）。
"""
from __future__ import annotations

import re

from . import site as C

SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÑ¿¡*\[(>-])")
NUM = re.compile(r"(?<![\w.,/-])(\d{1,3}(?:\.\d{3})+|\d+)(?![\w.,/%-]|[.,]\d)")
NOUN = r"(?:autorizaci(?:ón|ones|on)(?:\s+de\s+comercializaci[oó]n)?|registros?(?:\s+sanitarios?)?|licencias?|presentaciones?|productos?|medicamentos?)"
LICENSE = re.compile(r"\bautorizaci(ón|ones|on)\b|\blicencias?\b|\bAEMPS\b|\bCIMA\b|"
                     r"\d+\s+registros?\b(?!\s+de\s+(ensayos?|estudios?|pacientes?|casos?))", re.I)
MKT_NOUN = re.compile(r"\d+\s+(registros?|productos?|presentaciones?|medicamentos?)\b", re.I)
NOT_LICENSE = re.compile(r"interacci|ensayo|estudio|art[ií]culo|PMID|NCT|pacientes?|casos?\b|efectos? adversos?|\bmg\b|\bml\b|%|"
                         r"\baños?\b|\bmeses\b|semanas?|d[ií]as?\b|candidat|predicci|predich|puntuaci|score|rank|farmacolog|blancos?\b|"
                         r"receptor|DrugBank|ChEMBL|PubMed|ClinicalTrials|publicaci|referencias?\b", re.I)
HEDGED = re.compile(r"al menos|parcial|incomplet|puede haber m[aá]s|pueden existir|podr[ií]a|posiblemente|datos compilados|compilad|"
                    r"Evidence Pack|paquete de evidencia|consulta|devolvi|se (encontraron|identificaron|registraron)|identificad|"
                    r"\botr[oa]s\b|\bm[aá]s\b|adem[aá]s de|restantes?|adicional|resto|incluid|entre ellas?|entre ellos|"
                    r"veterinari|exportaci|importaci|paralel|laboratori|\bS\.?\s?A\.?(U\.?)?\b|\bS\.?L\.?(U\.?)?\b|\bGmbH\b|\bB\.V\.|Ltd|"
                    r"pertenec|fabricant|titular|"
                    r"comprimid|c[aá]psula|inyectable|soluci[oó]n|crema|jarabe|suspensi[oó]n|oft[aá]lmic|t[oó]pic|oral\b|gel\b|"
                    r"pomada|ung[uü]ento|polvo|ampolla|vial|parche|aerosol|inhalad|inhalaci|gotas|colirio|supositori|forma farmac|"
                    r"presentaciones? (de|en)\b|\bdosis\b|concentraci", re.I)
DISPLAY = re.compile(r"(se muestran?|se listan?|se recogen|la tabla|listad[oa]s|anteriores|siguientes|arriba|abajo|mostrad[oa]s|principales)", re.I)
BLOCK = re.compile(r"<!-- (review|licenses):begin.*?<!-- \1:end[^>]*-->", re.S)
VIG = r"(?:vigentes?|en vigor|activ[oa]s?|v[aá]lid[oa]s?)"
CANC = r"(?:revocad[oa]s?|suspendid[oa]s?|cancelad[oa]s?|anulad[oa]s?)"
NOCOM = r"(?:(?:autorizad[oa]s?\s+)?(?:pero\s+|aunque\s+)?(?:actualmente\s+)?no\s+(?:est[aá]n?\s+)?comercializad[oa]s?|sin comercializar)"
COM = r"(?:comercializad[oa]s?|en el mercado)"


def _role(s, a, b):
    left, right = s[max(0, a - 30):a].lower(), s[b:b + 60].lower()
    if re.match(r"\s*de\s+(los\s+|las\s+)?\d", right):
        return "display"
    # 「N de M」「las N principales de M」的 M 是總數（或有效數），不是顯示筆數：照右側判斷
    if DISPLAY.search(left) and not re.search(r"\bde\s+(los\s+|las\s+)?$", left):
        return "display"
    if DISPLAY.search(right[:30]) and not re.match(rf"\s*{NOUN}", right):
        return "display"
    near = right[:60]
    pre = rf"\s*(?:{NOUN}\s+)?(?:\w+\s+){{0,2}}(?:est[aá]n\s+|figuran\s+(?:como\s+)?|constan\s+como\s+|son\s+|siguen\s+)?(?:actualmente\s+)?"
    if re.match(pre + CANC, near):
        return "cancelled"
    if re.match(pre + NOCOM, near):
        return "nm"
    if re.match(pre + COM, near):
        return "comerc"
    if re.match(rf"\s*(?:{NOUN}\s+)?(?:\w+\s+){{0,3}}(?:de\s+)?(?:un solo principio activo|un [uú]nico principio activo|un solo componente|"
                r"monocomponentes?|monof[aá]rmacos?|ingrediente [uú]nico|principio activo [uú]nico)", near):
        return "single"
    if re.match(rf"\s*(?:{NOUN}\s+)?(?:\w+\s+){{0,2}}(?:son\s+|en\s+|de\s+)?(?:combinaci[oó]n|combinad[oa]s|asociaci[oó]n)", near):
        return "combo"
    if re.match(pre + VIG + r"\b", near) or re.match(rf"\s*(?:{NOUN}\s+)?(?:est[aá]n\s+)?autorizad[oa]s\b(?!\s+(pero\s+|aunque\s+)?no\b)", near):
        return "valid"
    if re.match(rf"\s*{NOUN}\b", right):
        return "total"
    return None


def _readings(role, f, sent, explicit=False):
    t, v, c, nm = f.get("total"), f.get("valid"), f.get("cancelled"), f.get("not_marketed") or 0
    st, vs = f.get("single_total"), f.get("valid_single")
    sp = f.get("susp")
    vlegal = None if v is None else v + nm
    lo = sent.lower()
    if role == "cancelled":
        if re.search(r"revocad", lo) and not re.search(r"suspendid|cancelad|anulad", lo):
            if sp is None:
                return {c}, None
            return {c, c - sp}, c if not sp else None
        return {c}, c
    if role == "nm":
        return {nm}, nm
    if role == "comerc":
        return {v}, v
    if role == "valid":
        return {v, vlegal}, v if v == vlegal else None
    if role == "single" and explicit:  # 同一句另有上市／註銷數字：單方的數字是單方總數
        return {st}, st
    if role == "combo" and explicit:
        ct = None if t is None or st is None else t - st
        return {ct}, ct
    if role == "single":
        validctx = bool(re.search(r"\bvigentes?\b|\bv[aá]lid[oa]s?\b|\bcomercializad", sent, re.I))
        if validctx:
            return {vs}, None  # 單方有效數：vigente 的兩種讀法事實層只存上市單方數，判斷不了要怎麼改
        return {st, vs}, st if st == vs else None
    if role == "combo":
        ct = None if t is None or st is None else t - st
        cv = None if v is None or vs is None else v - vs
        if re.search(r"\bvigentes?\b|\bv[aá]lid[oa]s?\b|\bcomercializad", sent, re.I):
            return {cv}, None
        return {ct, cv}, ct if ct == cv else None
    if explicit:  # 同一句另有明確的上市／授權未上市／註銷數字：沒有限定詞的那個就是總數
        return {t}, t
    return {t, v, vlegal}, t if t == v == vlegal else None


def _premise_ok(sent, f):
    lo = sent.lower()
    v, nm, c, t = f.get("valid") or 0, f.get("not_marketed") or 0, f.get("cancelled") or 0, f.get("total")
    if re.search(r"\b(tod[oa]s|ambos|ambas)\b[^.;]{0,60}\b(vigentes?|v[aá]lid|autorizad[oa]s\b(?!\s+(pero\s+)?no))|"
                 r"ning[uú]n[oa]? (\w+ ){0,3}(est[aá] )?(revocad|suspendid|cancelad)|sin (\w+ ){0,2}(revocad|cancelad|suspendid)", lo) \
            and (v + nm != t or c):
        return False
    if re.search(r"\b(tod[oa]s|ambos|ambas)\b[^.;]{0,60}\bcomercializad", lo) and not re.search(r"no comercializad", lo) and v != t:
        return False
    if re.search(r"\b(tod[oa]s|ambos|ambas)\b[^.;]{0,60}(un solo principio activo|un [uú]nico principio activo|monocomponente|"
                 r"monof[aá]rmaco|ingrediente [uú]nico)", lo):
        if f.get("single_total") != t:
            return False
    if re.search(r"\b(tod[oa]s|ambos|ambas)\b[^.;]{0,60}(combinaci[oó]n|combinad)", lo):
        if f.get("single_total"):
            return False
    return True


def rewrite_sentence(sent, f, market=False):
    """回傳 (新句子, 跳過理由或 None)。"""
    if not NUM.search(sent) or not (LICENSE.search(sent) or (market and MKT_NOUN.search(sent))):
        return sent, None
    if NOT_LICENSE.search(sent):
        return sent, None
    found = [(m, _role(sent, m.start(), m.end())) for m in NUM.finditer(sent)]
    if not any(r not in (None, "display") for _, r in found):
        return sent, None
    if HEDGED.search(sent):
        return sent, "hedged/subset"
    explicit = any(r in ("valid", "comerc", "cancelled", "nm") for _, r in found)
    subs = []
    for m, role in found:
        if role in (None, "display"):
            continue
        old = int(m.group(1).replace(".", ""))
        ok, v = _readings(role, f, sent, explicit)
        if old in ok:
            continue
        if v is None:
            return sent, "ambiguous"
        if old == 0:
            return sent, "zero-premise"
        if (old == 1) != (v == 1) or v == 0:  # 跨過 1（單複數）或改成 0：不改，列待查
            return sent, "plural"
        subs.append((m, v))
    if not subs:
        return sent, None
    if not _premise_ok(sent, f):
        return sent, "premise"
    out, pos = [], 0
    for m, v in subs:
        out.append(sent[pos:m.start(1)])
        out.append(f"{v:,}".replace(",", ".") if v >= 1000 else str(v))
        pos = m.end(1)
    out.append(sent[pos:])
    new = "".join(out)
    return new, None


def _line(ln, f, protect, skipped, market=False):
    if ln.startswith(("|", "#", ">")) or not ln.strip():
        return ln
    parts = SENT_SPLIT.split(ln)
    seps = SENT_SPLIT.findall(ln)
    new, held = [], False
    for s in parts:
        if any(p and (p in s or s in p) for p in protect):
            new.append(s)
            continue
        ns, why = rewrite_sentence(s, f, market)
        if why:
            skipped.append((why, s.strip()))
            held = True
        new.append(ns)
    if held:  # 同一行有句子判斷不了：整行不動，免得改了一句、旁邊的句子對不上
        return ln
    out = new[0]
    for sep, s in zip(seps, new[1:]):
        out += sep + s
    return out


def rewrite(text, facts, protect=()):
    """text：整頁 markdown。facts：快照的 facts。回傳 (新內容, skipped)。front matter、查核框、程式區塊、表格不動。"""
    skipped = []
    if not facts or facts.get("partial") or facts.get("total") is None:
        return text, skipped
    protect = [p.strip() for p in protect if p and len(p.strip()) >= 6]
    fm_end = 0
    if text.startswith("---"):
        j = text.find("\n---", 3)
        fm_end = j + 4 if j > 0 else 0
    body = text[fm_end:]
    keep = []

    def hold(m):
        keep.append(m.group(0))
        return f"\x00{len(keep) - 1}\x00"
    body = BLOCK.sub(hold, body)
    lines, market = [], False
    for ln in body.split("\n"):
        if ln.startswith("## "):
            market = bool(C.MARKET_SEC.match(ln))
        lines.append(ln if "\x00" in ln else _line(ln, facts, protect, skipped, market))
    body = re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], "\n".join(lines))
    return text[:fm_end] + body, skipped
