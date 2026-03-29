#!/usr/bin/env python3
"""處理西班牙 AEMPS 藥品資料

從 CIMA REST API 下載藥品註冊資料並轉換為 JSON 格式。
分兩階段：先下載藥品清單，再逐筆取得活性成分詳情。

使用方法:
    uv run python scripts/process_fda_data.py

資料來源:
    清單: https://cima.aemps.es/cima/rest/medicamentos
    詳情: https://cima.aemps.es/cima/rest/medicamento?nregistro={nregistro}

產生檔案:
    data/raw/es_fda_drugs.json
"""

import json
import time
from pathlib import Path

import pandas as pd
import requests
import yaml


def load_config() -> dict:
    """載入欄位映射設定"""
    config_path = Path(__file__).parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def download_cima_list(output_path: Path) -> Path:
    """從 CIMA REST API 下載藥品清單（含分頁）

    清單端點 /medicamentos 不含 principiosActivos，僅含 vtm（虛擬
    治療成分）。需後續以 /medicamento?nregistro=... 取得完整成分。

    Args:
        output_path: JSON 輸出路徑

    Returns:
        下載的檔案路徑
    """
    config = load_config()
    base_url = config["data_source"]["url"]

    print("正在從 CIMA REST API 下載藥品清單...")
    print(f"Base URL: {base_url}")

    all_records = []
    page = 1
    page_size = 25  # CIMA default page size

    while True:
        params = {"pagina": page}
        print(f"  下載第 {page} 頁...", end=" ", flush=True)

        try:
            response = requests.get(base_url, params=params, timeout=60)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"\n第 {page} 頁下載失敗: {e}")
            if all_records:
                print(f"已收集 {len(all_records)} 筆資料，繼續處理...")
                break
            raise

        data = response.json()

        # CIMA API returns {"resultados": [...], "totalFilas": N, "pagina": N, ...}
        results = data.get("resultados", [])
        total_rows = data.get("totalFilas", 0)

        if not results:
            print("無更多資料")
            break

        all_records.extend(results)
        print(f"取得 {len(results)} 筆 (累計: {len(all_records)}/{total_rows})")

        if len(all_records) >= total_rows:
            break

        page += 1

    print(f"\n清單下載完成，共 {len(all_records)} 筆資料")

    # 確保輸出目錄存在
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_records, f, ensure_ascii=False, indent=2)

    print(f"已儲存至: {output_path}")
    return output_path


def enrich_with_ingredients(list_path: Path, enriched_path: Path) -> Path:
    """為每筆藥品從詳情端點取得 principiosActivos

    清單端點（/medicamentos）的 principiosActivos 為空，
    需逐筆呼叫 /medicamento?nregistro={nregistro} 取得完整資料。

    每 100 筆儲存一次進度，可中斷後繼續。

    Args:
        list_path: 藥品清單 JSON 路徑
        enriched_path: 含成分的輸出 JSON 路徑

    Returns:
        輸出檔案路徑
    """
    DETAIL_URL = "https://cima.aemps.es/cima/rest/medicamento"
    SAVE_INTERVAL = 100
    DELAY = 0.1  # 100ms between requests

    print("正在從 CIMA 詳情端點取得活性成分...")

    with open(list_path, "r", encoding="utf-8") as f:
        records = json.load(f)

    # 載入已有進度（若存在）
    already_done = {}
    if enriched_path.exists():
        with open(enriched_path, "r", encoding="utf-8") as f:
            existing = json.load(f)
        already_done = {r["nregistro"]: r for r in existing if "nregistro" in r}
        print(f"  已有 {len(already_done)} 筆進度，從斷點繼續")

    enriched = []
    errors = 0

    for i, item in enumerate(records):
        nregistro = item.get("nregistro", "")

        # 如果已有此筆的詳情資料（含 principiosActivos），直接使用
        if nregistro in already_done:
            enriched.append(already_done[nregistro])
            continue

        # 從 vtm 取得基本活性成分名稱（作為 fallback）
        vtm_name = ""
        vtm = item.get("vtm")
        if isinstance(vtm, dict):
            vtm_name = vtm.get("nombre", "")

        # 呼叫詳情端點
        try:
            resp = requests.get(
                DETAIL_URL,
                params={"nregistro": nregistro},
                timeout=30,
            )
            resp.raise_for_status()
            detail = resp.json()

            pas = detail.get("principiosActivos", [])
            if isinstance(pas, list) and pas:
                ingredients = "; ".join(
                    pa.get("nombre", "") if isinstance(pa, dict) else str(pa)
                    for pa in pas
                )
            else:
                # fallback 到 vtm
                ingredients = vtm_name
        except Exception as e:
            if errors < 5:
                print(f"\n  警告: nregistro={nregistro} 詳情取得失敗: {e}")
            errors += 1
            ingredients = vtm_name

        # 建立記錄（保留清單欄位 + 新的 principiosActivos）
        record = dict(item)
        record["principiosActivos_detail"] = ingredients
        enriched.append(record)

        # 進度回報
        done_count = i + 1
        if done_count % 500 == 0:
            print(f"  已處理 {done_count}/{len(records)} (錯誤: {errors})")

        # 儲存進度
        if done_count % SAVE_INTERVAL == 0:
            enriched_path.parent.mkdir(parents=True, exist_ok=True)
            with open(enriched_path, "w", encoding="utf-8") as f:
                json.dump(enriched, f, ensure_ascii=False, indent=2)

        time.sleep(DELAY)

    # 最終儲存
    enriched_path.parent.mkdir(parents=True, exist_ok=True)
    with open(enriched_path, "w", encoding="utf-8") as f:
        json.dump(enriched, f, ensure_ascii=False, indent=2)

    with_ingredients = sum(1 for r in enriched if r.get("principiosActivos_detail"))
    print(f"\n詳情取得完成，共 {len(enriched)} 筆")
    print(f"  有活性成分: {with_ingredients} ({with_ingredients/len(enriched)*100:.1f}%)")
    print(f"  錯誤數: {errors}")

    return enriched_path


def process_cima_data(input_path: Path, output_path: Path) -> Path:
    """處理 CIMA JSON 資料並正規化

    將巢狀 API 回應扁平化為表格式 JSON。

    Args:
        input_path: 含成分的 JSON 檔案路徑
        output_path: 處理後 JSON 輸出路徑

    Returns:
        輸出檔案路徑
    """
    config = load_config()

    print(f"讀取資料檔案: {input_path}")

    with open(input_path, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    print(f"原始資料筆數: {len(raw_data)}")

    # 扁平化巢狀結構
    records = []
    for item in raw_data:
        record = {
            "nregistro": item.get("nregistro", ""),
            "nombre": item.get("nombre", ""),
            "labtitular": item.get("labtitular", ""),
            "estado": item.get("estado", {}).get("nombre", "") if isinstance(item.get("estado"), dict) else str(item.get("estado", "")),
            "fechaAutorizacion": item.get("fechaAutorizacion", ""),
            "formaFarmaceutica": item.get("formaFarmaceutica", {}).get("nombre", "") if isinstance(item.get("formaFarmaceutica"), dict) else str(item.get("formaFarmaceutica", "")),
        }

        # 優先使用詳情端點取得的活性成分
        ingredients = item.get("principiosActivos_detail", "")

        # fallback: 嘗試清單中的 principiosActivos（通常為空）
        if not ingredients:
            pas = item.get("principiosActivos", [])
            if isinstance(pas, list) and pas:
                ingredients = ", ".join(
                    pa.get("nombre", "") if isinstance(pa, dict) else str(pa)
                    for pa in pas
                )
            elif pas:
                ingredients = str(pas)

        # 再 fallback: 嘗試 vtm
        if not ingredients:
            vtm = item.get("vtm")
            if isinstance(vtm, dict):
                ingredients = vtm.get("nombre", "")

        record["principiosActivos"] = ingredients or ""
        records.append(record)

    # 清理資料
    df = pd.DataFrame(records)
    df = df.fillna("")

    data = df.to_dict(orient="records")

    # 儲存 JSON
    output_path.parent.mkdir(parents=True, exist_ok=True)
    print(f"儲存至: {output_path}")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"完成！共 {len(data)} 筆藥品資料")

    # 顯示統計
    print_statistics(df, config)

    return output_path


def print_statistics(df: pd.DataFrame, config: dict):
    """印出資料統計"""
    fm = config["field_mapping"]
    status_field = fm["status"]
    ingredients_field = fm["ingredients"]

    print("\n" + "=" * 50)
    print("資料統計")
    print("=" * 50)

    if status_field in df.columns:
        print(f"\n註冊狀態分布:")
        status_counts = df[status_field].value_counts()
        for status, count in status_counts.items():
            print(f"  {status}: {count:,}")

    if ingredients_field in df.columns:
        with_ingredients = (df[ingredients_field] != "").sum()
        print(f"\n有活性成分: {with_ingredients:,} ({with_ingredients/len(df)*100:.1f}%)")


def main():
    print("=" * 60)
    print("處理西班牙 AEMPS/CIMA 藥品資料")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    raw_dir = base_dir / "data" / "raw"
    raw_json = raw_dir / "cima_medicamentos_raw.json"
    enriched_json = raw_dir / "cima_medicamentos_enriched.json"
    output_path = raw_dir / "es_fda_drugs.json"

    # 確保 raw 目錄存在
    raw_dir.mkdir(parents=True, exist_ok=True)

    # Phase 1: 下載清單（如果不存在）
    if not raw_json.exists():
        download_cima_list(raw_json)
    else:
        print(f"使用已存在的清單資料: {raw_json}")

    # Phase 2: 逐筆取得活性成分（可中斷後繼續）
    enrich_with_ingredients(raw_json, enriched_json)

    # Phase 3: 處理並輸出最終 JSON
    process_cima_data(enriched_json, output_path)

    print()
    print("下一步: 準備詞彙表資料")
    print("  uv run python scripts/prepare_external_data.py")


if __name__ == "__main__":
    main()
