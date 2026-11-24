"""AEMPS CIMA 成分欄（證據包 tfda.records 的 ingredients，取自 practiv）的成分切分與單方／複方判定（2026-11-24）。

原本 reviewer/drug_evidence_pack.py 用「;;」切成分，但本站成分欄的複方以「 + 」連接（例「piperacilina + tazobactam」），
另有少數以「, 」連接（例「deutivacaftor, tezacaftor, vanzacaftor」），事實層把複方也算成單方（single_total＝total）。
用戶 2026-11-24 決定：事實層依本站成分欄正確切分。scripts/sync_license_tables.py 快照的 single_real 也用這裡的規則。
"""
import re

_SEP = re.compile(r"\s\+\s|,\s")


def split_ingredients(s):
    return [x.strip() for x in _SEP.split(str(s or "")) if x.strip()]


def kind(s):
    """單方 single／複方 combo；成分欄空白時照舊算 single（跟原本「;;」切法空白時的結果相同）"""
    return "combo" if len(split_ingredients(s)) > 1 else "single"
