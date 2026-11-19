# ESTxGNN - Claude CLI 使用指引

本站（西班牙，AEMPS CIMA）的維運規則。站群共用流程見母 repo yao-care/txgnn 的 CLAUDE.md；本檔只記本站自己的機制。

- 本專案結果僅供研究參考，不構成醫療建議
- 老藥新用候選需經過臨床驗證才能應用
- 所有網站頁面需包含 YMYL 免責聲明

---

## 藥物頁查核機制（2026-11-12 起）

用戶 2026-11-12 決定：30 站各有自己的查核機制，核心流程比照 TwTxGNN（Tw 的 CLAUDE.md「藥物頁人工查核紀錄」「藥物頁許可證表與張數」兩節；
做法同 UsTxGNN，見 UsTxGNN/CLAUDE.md 同名一節）。規則與程式都在本 repo；頁面文字用西班牙文，依據是AEMPS CIMA（已上市／授權未上市／撤銷或暫停分開寫）。本站的在地設定集中在 `src/estxgnn/regulatory/site.py`。

| 環節 | 本站檔案 | 說明 |
|------|----------|------|
| 查核紀錄 | `docs/_data/drug_reviews.json` | 單一真實來源，欄位同 Tw（correct／annotate／rereview／rereview_result／header_level／description_level、history、status） |
| 套用 | `scripts/apply_drug_reviews.py` | 套到 `docs/_drugs/*.md`：查核框 `<!-- review:begin id -->`、每頁查核紀錄表；可重複執行；`--check` 只檢查、`--touch` 連 last_modified_at 一起改 |
| 頁首等級 | `src/estxgnn/regulatory/page_format.py`（規則在 site.py 的 HEADER_RULE） | 頁首＝Resumen rápido「Nivel de Evidencia」格的**第一個**等級（主預測）。2026-11-12 實測 830 頁有總覽等級，全部符合；整格取最高會有 7 頁不同 |
| 撤回預測 | `src/estxgnn/regulatory/withdrawn.py` | verdict=withdraw 的預測不進證據監測（`scripts/extract_drug_list.py`）、搜尋索引與 FHIR（母目錄 `.claude/rebuild_search_index.py`、`.claude/sync_fhir_levels.py` 會讀本站這支） |
| 許可證 | `snapshots/es_licenses.json.gz`、`scripts/build_license_snapshot.py`、`src/estxgnn/regulatory/licenses.py` | 快照存本藥號碼與事實層；gate 依快照驗市場段落表格的號碼歸屬、狀態列與張數列、表格列狀態（本站沒有程式產生的許可證表，所以沒有程式區塊標記） |
| 刪改轉紀錄 | `scripts/reviews_from_edits.py` | 依成分重建刪句後（`scripts/license_rebuild_run.py` 有的話會自動跑）或依 git 前後版本，把正文刪改轉成 correct 紀錄 |
| 待查清單 | `docs/_data/drug_reviews_uncertain.json`、`scripts/check_original_indications.py` | 原適應症交叉驗證；本站證據包的 CIMA 紀錄沒有適應症文字，可比對 0 頁（程式照實回報） |
| gate | `scripts/check_seo_docs.py` 第 17–20 項 | 紀錄都已套用、許可證＝快照、頁首＝本站規則算出的等級、撤回預測沒有對外發布 |

原則（同 Tw）：基本事實照主管機關資料更正；模型預測原文不刪不改寫，只加註；證據等級與決策只經重審（rereview → rereview_result）變更。

改頁之後要跑：

```bash
python3 scripts/apply_drug_reviews.py          # 重套查核紀錄（sync_notes_to_docs.py、license_rebuild_run.py、每週排程結尾都會自動跑）
python3 scripts/build_license_snapshot.py --ws <工作目錄>   # 證據包或事實層變了才要（排程與重建會自動跑）
python3 scripts/check_seo_docs.py              # 必須 exit 0
```

2026-10-31～11-06 依成分重建後直接刪掉的矛盾子句，2026-11-12 已用 `scripts/reviews_from_edits.py --git` 轉成 247 筆紀錄（241 頁；沒有因 AI 重產而原句已不在頁面的；f64d05ef 的部分還原併進 8c11d4af 的整句刪除，成為子句級更正）。另 2026-11-12 人工更正 indacaterol（11-09 Release 事實層：12 張中已上市 2、授權未上市 6、撤銷 4）：概覽狀態列與張數列用 `tools/txgnn/.claude/license_table_sync_20261029.py` 的 sync_market_rows 程式同步，正文「12 autorizaciones vigentes」記成一筆 correct 紀錄。
`scripts/sync_notes_to_docs.py` 依 notes 重寫整頁時，會重套紀錄（有程式許可證表的站也保留舊頁的程式區塊），notes 裡的舊錯句會被紀錄再更正一次。
2026-11-12 正文許可證張數對事實層的掃描：codeine（第六張 20709 寫有效，CIMA 為 Revocada）、phenytoin（第六張 65303 寫有效、六張全有效，實為 4 張有效、65340 與 65303 撤銷）以 `es-lic-20261112-*` 更正；錨在 codeine 那句的 es-lic-20261105-codeine-1 改錨，前版存 history。

## 新資料查不到的許可證（2026-11-17）

每週排程把「CIMA 新資料查不到」的許可號保留原狀態，2026-11-17 列出 232 張（超過 2% 開 issue）。用戶要求確認實際狀態：
CIMA REST 清單（/medicamentos）本身就是完整登錄，含已撤銷（rev）與暫停（susp）的；這 232 張在清單與單筆查詢
（/medicamento?nregistro=…）都查不到，在 2026-03 的 CIMA 清單（Release data-20261029-handoff 的 data/raw/cima_medicamentos_raw.json）
則全部是 Revocada，撤銷日 2021-03-30～2021-11-15；同一份 3 月清單裡 2021-11-15 以前撤銷的 777 張 11 月都已不在 CIMA、
2021-11-18 以後撤銷的仍在——CIMA 撤銷約 5 年後移除紀錄。證據包本來就標 Revocada，事實層與頁面都不用改（0 頁）。
另找 AEMPS Nomenclátor de prescripción（listadomedicamentos.aemps.gob.es/prescripcion.zip）比對，雲端主機下載回 403，沒有用到。
- `scripts/license_adapter.py`：fetch() 把清單上的全部 nregistro 存進 LISTED（少於 MIN_LISTED＝20000 不判定）；preprocess 對清單沒有的號
  標 `license_status: cancelled`＋`cima_not_listed`（第一次發現日），status 原文不動，又出現在清單就取消；`confirmed_absent()` 讓排程把這些列成
  「主管機關現行清單確認已不列」，不算「查不到」、不開 issue（母目錄 license_refresh 的掛鉤）。之後每週會有撤銷滿 5 年的號陸續移除，照同樣處理。
- 這 232 張（證據包裡 328 筆、223 個藥）另記 `cima_revocada_fecha`（3 月清單的撤銷日）。沒有有效許可的 15 個證據包（8 個有藥物頁）依 CIMA practiv1 查成分確認沒有其他現行產品
  （catumaxomab 的 KORJUNY、interferon alfa-2b 的授權未上市品項與事實層一致）。

## 說明頁與證據等級頁的在地資料（2026-11-19）

用戶 2026-11-19 決定的第一批改版（母目錄 `.claude/gen_local_pages_20261119.py` 產生，不逐站手改）：說明頁（about／guide／sources／downloads／methodology，自有結構站只有證據等級頁與隱私頁）加本站資料區塊（`<!-- local-facts -->`）、證據等級頁的事實段與藥名表（`<!-- tier-facts -->`、`<!-- tier-table -->`）、隱私頁的適用法律／權利／著作權與資料來源段（`<!-- privacy-law -->`）；en／es／de 樣板站的共用長段落縮成一段（`<!-- local-condensed -->`）。
資料檔 `docs/_data/local_facts.json`、`docs/_data/evidence_tier_facts.json` 由 `scripts/local_facts.py`（＝母目錄 `.claude/local_facts_lib.py`）依藥物頁、許可證快照、查核紀錄、FHIR 算；`apply_drug_reviews.py`、許可證快照程式結尾會自動 `--write`，`check_seo_docs.py` 跑 `--check` 擋過期。跨站欄位（cross：本站獨有預測、30 站中位數）與頁面區塊只由母目錄產生器更新；藥物頁改等級、noindex 或預測後要在母目錄重跑。
