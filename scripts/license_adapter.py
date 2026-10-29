"""ES（AEMPS CIMA）許可證下載與狀態對應，給 tools/txgnn/.claude/license_refresh_20261029.py 用（2026-10-29）。

來源：https://cima.aemps.es/cima/rest/medicamentos（公開 REST，免金鑰，每頁 200 筆，約 130 頁）。
狀態規則沿用 2026-10-21 es_cima_status（pm 第 7 點）：estado 有 rev＝Revocada、有 susp＝Suspendida、
否則 comerc＝true 為 Autorizada，false 為 Autorizada (no comercializada)。
"""
import time

import requests

RAW_FILE = "raw/cima_medicamentos_raw.json"
URL = "https://cima.aemps.es/cima/rest/medicamentos"


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
    return out


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
