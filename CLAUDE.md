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
| 許可證 | `scripts/sync_license_tables.py`（程式表前後有 `<!-- licenses:begin/end -->` 標記，2026-11-24 起）、`snapshots/es_licenses.json.gz`、`scripts/build_license_snapshot.py`、`src/estxgnn/regulatory/licenses.py` | 快照存本藥號碼、事實層與程式表列；gate 依快照驗程式區塊、市場段落表格的號碼歸屬、狀態列與張數列、表格列狀態 |
| 刪改轉紀錄 | `scripts/reviews_from_edits.py` | 依成分重建刪句後（`scripts/license_rebuild_run.py` 有的話會自動跑）或依 git 前後版本，把正文刪改轉成 correct 紀錄 |
| 待查清單 | `docs/_data/drug_reviews_uncertain.json`、`scripts/check_original_indications.py` | 原適應症交叉驗證；本站證據包的 CIMA 紀錄沒有適應症文字，可比對 0 頁（程式照實回報） |
| gate | `scripts/check_seo_docs.py` 第 17–20、22 項 | 紀錄都已套用、許可證＝快照（含程式表）、頁首＝本站規則算出的等級、撤回預測沒有對外發布、正文張數＝程式改寫結果 |

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


## 市場段落許可證表與正文張數改由程式維護（2026-11-24）

用戶 2026-11-24 決定（30 站逐站做，本站第二波、A＋B 都做；照 COTxGNN 同日的同名程式，同為西班牙文）：每週許可證排程只改概覽表狀態列／張數列，AI 寫的自由格式許可證表
（多數只有號碼、品名、劑型與一欄寫「No disponible」的「Indicación Aprobada」，少數另寫 Vigente／Cancelado）與正文寫死的張數會跟每週變的 CIMA 矛盾，checker 擋頁、要人處理。
- A. `scripts/sync_license_tables.py`：市場段落（Información de Mercado en España）的第一張表換成程式依證據包產生的表
  「| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |」（欄位全取 CIMA 原文：nregistro、nombre、forma farmacéutica、titular，不翻譯；
  原表第四欄「Indicación Aprobada」CIMA 資料沒有內容，改放持有人）。狀態照 CIMA：Autorizada＋comercializado→Comercializada、Autorizada (no comercializada)→
  Autorizada, no comercializada、Revocada、Suspendida（cima_not_listed 的號碼證據包原本就是 Revocada，照寫）；排序上市→授權未上市→暫停→撤銷。
  列數＝原表列數與 min(10, 總數) 取大（上限 20；CO 是 5，本站 AI 正文常在表下補講第 6、7 張）；段落裡有 AI 寫的「表上列了幾筆」說明句（se muestran／se listan／
  la tabla／la lista muestra／las N principales／no listadas…）時照原表列數。表下程式句「Se muestran N de M autorizaciones con este principio activo en los datos de CIMA (AEMPS)…」
  （部分紀錄寫「de al menos K」，列滿時「las K … recogidas … para este informe」）；沒有紀錄時寫 NONE_LINE；段落沒有表的頁在標題下補程式區塊；known_use_pages 的舊部分紀錄提示句拿掉。
  gate 由 `site.program_block_problems` 依快照（rows、total、partial、listed）重算比對。快照另存 susp（Suspendida 筆數）與 single_real／valid_single_real
  （依證據包成分欄「 + 」重算的單方張數：事實層 single_total 把複方也算成單方，2026-11-24 實測 104 頁不符；只給正文改寫用，事實層不改）。
  接進：每週排程（`scripts/license_adapter.py` 的 sync_tables＋PAGE_NOTE）、`build_license_snapshot.py` 結尾（全站重排＋B；`--no-rewrite` 不跑）、`sync_notes_to_docs.py` 的 carry_block。
- B. `scripts/rewrite_license_counts.py`＋`src/estxgnn/regulatory/count_prose.py`（照 CO 的版本，句型改 CIMA 寫法）：comercializad→上市數；no comercializad→授權未上市數；
  revocad／suspendid／cancelad→非有效數（只寫 revocad 而有暫停的，讀法另含 非有效−暫停）；vigente／válid→上市數或上市＋授權未上市數都算對、要改時兩者相同才改；
  有保留、相對數、劑型或廠商子集、顯示筆數、部分紀錄頁不改，同一行有判斷不了的整行不動；改成 0 或跨過 1 張（單複數）列 plural、不改。
  `apply_drug_reviews.py`（非 --check）結尾、`build_license_snapshot.py` 結尾都會跑；gate 第 22 項擋「再跑一次會變」。
- 2026-11-24 套用（Release data-20261123-143851）：公開藥物頁 859 頁中 855 頁有市場段落，849 頁的 AI 表換掉、6 頁補程式區塊（連 noindex 共 856 頁有變，last_modified_at 改 2026-11-24）；
  沒有錨在舊表列上的查核紀錄（superseded 0 筆）。B 評估 76 句（非部分紀錄頁）：56 句已等於事實、17 句有保留或子集、3 句判斷不了，改寫 0 句（11-12 起的紀錄已把張數改對）。
  換表後跟新表或事實對不上的 17 句以 17 筆 `es-lic-20261124-*` 更正：舊表「沒列第六張／límite de cinco」「la sexta es…」「las otras dos…」（maraviroc、palbociclib、urofollitropin、
  fosaprepitant、golimumab、olopatadine、methionine、norepinephrine、rifampicin）、單方說法依成分欄是複方（ephedrine、hexetidine、insulin_degludec、oxytetracycline、phenylbutazone）、
  「ambas／todas vigentes」而有撤銷或暫停（gadobenic_acid、remdesivir、methylphenidate、urofollitropin）。
  查核紀錄更正文字裡寫死的張數（用戶同日追加決定）：147 筆刪句紀錄 note 的「El medicamento tiene N autorizaciones (comercializadas: M)」拿掉、只留「las cifras actuales están en el Resumen rápido…」，
  codeine、indacaterol、phenytoin、salmeterol、norfloxacin 5 筆的張數／舊表筆數改成號碼或「見表」寫法，共 152 筆同 id 重發（前版存 history）。
  部分紀錄頁寫死的張數跟已收錄紀錄不符的 4 句（adalimumab、amlodipine、azithromycin、pseudoephedrine）列進待查清單（程式不改 partial 頁）。
- 2026-11-24 第二輪（用戶決定：舊錯句逐句寫紀錄、劑型說法、張數樣板）：待查清單 4 句部分紀錄頁張數（adalimumab、amlodipine、azithromycin、pseudoephedrine）依 CIMA 全量清單（Release data-20261123 的
  data/raw/cima_medicamentos_raw.json，依 vtm）確認實際張數比證據包多，以 `es-lic-20261124b-*` 改成不寫數字的寫法（實際張數記在紀錄 finding），待查標 resolved；同類（部分紀錄頁把收錄的 20 張寫成總數、沒有保留語）
  另 18 句（ceftriaxone、diazepam、docetaxel、filgrastim×2、fluconazole、paliperidone、sacubitril、tolvaptan、clotrimazole、denosumab×2、lamotrigine、loperamide、nintedanib、perampanel、safinamide、vortioxetine）一併更正。
  舊 AI 表外的品項說法（la sexta／las restantes／las demás／el resto／otras N／no listada）與「Se muestran 5 de las N…」這類舊表說明句（含總張數，跟程式表下方說明句重複、張數不會跟著更新）：
  全站逐句處理；第二輪合計新紀錄 73 筆（含上面的部分紀錄頁 22 句與下面劑型 3 句）、既有紀錄更正文字同 id 重發 22 筆（前版存 history；piroxicam 1 筆改錨），92 頁，改成「Entre las autorizaciones figuran…」或刪掉；順帶更正的事實：desogestrel 的 NACREZ、DESOGESTREL STADA 已撤銷，
  epinephrine 的 EMERADE、ketoprofen 的 ORUDIS RETARD、melphalan 的 Melfalan Medac、triflusal 的 Triflusal Aristo、orlistat 的 Orlistat Aristo、oxcarbazepine 的 Teva、imidapril 的 Asibilan 已撤銷，guanfacine Paxneury 有 1～7 mg。
  說明句拿掉後 42 頁程式表依規則改列 min(10, 總數) 列。沒有張數、跟程式表一致的引導句（「Principales autorizaciones:」「Se muestran las 5 principales:」、部分紀錄頁「5 de al menos 20」約 80 句）不動。
  劑型說法全站 51 句逐句對照證據包與 CIMA 全量：azathioprine（注射劑已撤銷）、cabozantinib（Cometriq 未上市）、midazolam（另有 DORMICUM 錠劑；併在既有紀錄重發）、ebastine（另有口溶凍晶、口服液）更正，其餘成立。
  `site._fig`（reviews_from_edits 寫紀錄說明的張數樣板）改成不寫數字。checker 0→0、gate exit 0。
- 2026-11-24 第三輪（用戶決定）：
  B. 公開頁（非 noindex）整頁沒有市場段落、但證據包有紀錄的（比照 JpTxGNN 第二輪 add_section）：`scripts/sync_license_tables.py` 的 `add_section` 在「## Consideraciones de Seguridad」之前
  （沒有就「## Conclusión y Próximos Pasos」、再沒有就「## Descargo de responsabilidad」之前）補「## Información de Mercado en España」與程式區塊；`carry_block` 遇到整頁重寫後沒有市場段落的頁也照同一位置補回舊區塊。
  全量量測：公開頁 859 頁中 4 頁沒有「Información de Mercado」段落：acarbose、artemether、carboplatin 補段落（12、1、6 張），carbenoxolone 的報告用「## Informe de Mercado en España」標題、
  下面是 AI 表——`SEC_RE`／`site.MARKET_SEC` 改成也認這個標題，AI 表換成程式表（標題不改）。gate 第 18 項加「公開頁有證據包紀錄卻沒有市場段落」就擋（licenses.page_problems）；
  `scripts/license_adapter.py` 的 PAGE_NOTE 放行新標題行。carbenoxolone 結論裡「la formulación disponible en España (pomada bucal)」（唯一一張 44352 已撤銷）以 `es-lic-20261124c-carbenoxolone-1` 更正。
  C. 部分紀錄頁帶保留語（según los datos compilados／puede ser parcial／al menos）、數字等於證據包收錄筆數（或其中的上市／撤銷張數）而 CIMA 全量（data/raw/cima_medicamentos_raw.json，依 vtm；
  另加證據包裡已不在 CIMA 的撤銷號）較多的張數句：全量掃部分紀錄頁 177 頁，24 句依全量改成不寫數字的寫法（`es-lic-20261124c-*`，note 指向概覽表與程式表，實際張數記在 finding）；
  apixaban 另更正「solo una figura como vigente y comercializada (Eliquis)」（CIMA 有多張上市的學名藥）。agomelatine 的「hay 20 autorizaciones registradas」照 CIMA 全量（19＋1 張，全在證據包）成立，不改。
  「Se muestran las 5 principales:」「Se muestran 5 de al menos 20」「se muestran solo 5」這類只講表上列數的句子照第二輪決定不動（程式表照原表列數）。checker 0→0、gate exit 0。
- 母目錄 `.claude/license_labels/ESTxGNN.json` 還沒有程式表的狀態字（Comercializada、Autorizada, no comercializada、Revocada、Suspendida）；lts.apply 認不得就跳過、不會列 unsynced，
  程式表由 sync_tables 重排，但要讓 checker 的表格列狀態檢查也驗程式表，需在母目錄加這 4 個字。

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

## 作用機轉段的資料來源與查核機制（2026-11-19）

用戶 2026-11-19 決定把 NZTxGNN 同日的作法推到各站（seo-ops 轉交：搜「<藥名> mechanism of action」落在藥物頁排名 30–99，因為頁面寫「作用機轉資料不可得」）。
2026-11-19 量測：本站公開藥物頁（排除 noindex、轉址頁）有 705 頁在正文章節寫這種句子（證據包 drugbank.source＝vocab_only、沒有作用機轉文字，AI 照實寫「沒有資料」；本站最常見的寫法：「Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe.」）。
作用機轉是藥物本身的基本藥理事實、不是模型預測，所以照查核機制補：每段都節錄官方仿單或資料庫原文、附可點的出處與取用日期，不自己寫。

- 來源（理由同 NZTxGNN/CLAUDE.md 同名一節）：美國 FDA 核准仿單（openFDA drug label，連結到 NLM DailyMed 同一份 SPL setid；FDA 仿單是美國政府公開資料），美國沒有仿單時用 ChEMBL drug mechanism 表（CC BY-SA 3.0）；證據包的 DrugBank 欄位只有 vocab，DrugBank 文字授權也不允許轉載，不用。
  2026-11-19 這次用 openFDA 的 drug label 全量下載檔（download.open.fda.gov，同一批資料，只留 human prescription 仿單；`--fda-bulk <目錄>`），不吃 API 每日 1,000 次配額；之後少量重跑可直接用 API（不給 `--fda-bulk`）。快取目錄各站共用。
- `scripts/build_mechanism_reviews.py --cache <目錄> [--fda-bulk <目錄>]`：掃公開頁正文章節（排除結論／下一步的待辦、安全性、摘要、總覽表、查核紀錄、免責聲明等）裡同時有「作用機轉」「資料」「沒有」字樣的短句（本站語言的字樣在檔內 L 的 KW／DATA／NEG／EXCL）→ 依 front matter monitor_inn（INN 另對 USAN，表在 US_NAME）查 openFDA，選仿單規則同 NZ：只用單一成分、主成分名（去鹽類；酯類要相同）跟本頁相同的處方藥仿單；排序全身給藥→節錄夠長→有 12.1→有品牌名→版本新；美國只有複方仿單的只節錄 12.1 裡講本藥成分的句子並寫明是複方；節錄照原文 2～4 句、不改寫。
  紀錄寫進 `docs/_data/drug_reviews.json`（action＝mechanism，id `es-moa-<日期>-<藥>-1`，sources 附 url、accessed、excerpt、label_version、section、set_id 或 chembl_id）；仿單與 ChEMBL 都沒有的，列進 `docs/_data/drug_reviews_uncertain.json`（source＝mechanism of action，附原因）。已有紀錄或已列待查的頁不重抓。`--list` 只列仍寫「不可得」的頁。
- 替換句格式：本站語言（español）的出處句＋節錄的忠實翻譯（標明「非官方翻譯」）＋英文原文（照引、為準）＋DailyMed 連結、仿單版本、取用日期（用戶 2026-11-19 決定「當地語言摘要＋英文原文」）。只換「不可得」那一句（英文站句首子句後接 so／but 的後半句是 AI 推論，保留），不加框；查核紀錄表列原句與出處。模型預測與其他正文不動。
- 翻譯：節錄的翻譯是 AI 輔助的忠實翻譯（不增不減，藥名、基因與受體符號、數字、「[…]」照原文），2026-11-19 批次產生，存在紀錄 sources 的 translation（translation_lang、translation_note 註明非官方、英文原文為準）；頁面上同時列英文原文。`--translations <檔>` 讀翻譯、`--need <檔>` 列出還沒翻的節錄（這些頁那次不寫紀錄，gate 會擋，翻好再跑）。
- 2026-11-19 結果：604 頁寫入紀錄（美國仿單 519、ChEMBL 85），101 頁列待查（美國沒有單一成分處方藥仿單、仿單段落不是作用機轉，且 ChEMBL 沒有已核准分子的機轉紀錄；多是胺基酸、維生素、礦物質、賦形劑、生物製劑或只在別國上市的藥）。
- `scripts/apply_drug_reviews.py` 支援 mechanism；gate 第 21 項（`scripts/check_seo_docs.py`，函式在 build_mechanism_reviews.gate_errors）：公開頁仍寫「不可得」、既沒有 mechanism 紀錄也沒列待查的，擋下；有紀錄沒套上的由查核紀錄那一項擋。
- 注意：節錄的是美國仿單，劑型與適應症可能跟本站市場的產品不同（例如取到外用仿單）；文字上已寫明是美國 FDA 核准仿單。`sync_notes_to_docs.py` 整頁重寫後會重套紀錄（claim 是頁面原句）；報告重產、原句改寫後要再跑 build_mechanism_reviews.py。
- 2026-11-20 補做：程式更新：同頁不只一句「不可得」時每句各一筆紀錄（-1、-2…）；同頁別筆紀錄的更正文字、錨點與已套上的節錄不再當成「不可得」句；gate 改成公開頁仍寫「不可得」、又沒列待查就擋（不再只看該頁有沒有紀錄）；ChEMBL 譯文（詞組清單）後補句號 85 筆；同 id 重發，前版 replacement 存 history。
- 2026-11-20 試跑母目錄「交付前驗證」規則時補做：偵測改成原條件不動、另加新增寫法（L2，比中的再用 NOT 排除以缺資料為前提的模型推論），字樣用獨立、更寬的偵測全量掃出的候選句逐句標註校準（A 沒有漏、B 沒有誤中）；偵測漏抓的「不可得」句補 5 筆紀錄、1 頁列待查；節錄後面接著 AI 說明「上面描述依據」的句子（會讀成美國仿單的出處）1 筆改成那句在節錄前（原文不改，只換順序）；以上同 id 重發，前版存 history。程式另加 reorder_src_tail、同頁已引用同一段節錄時改指向上方（產生器 txgnn/.claude/moa_rollout_20261119/fix_20261120/）。

## 說明頁與證據等級頁的在地資料（2026-11-19）

用戶 2026-11-19 決定的第一批改版（母目錄 `.claude/gen_local_pages_20261119.py` 產生，不逐站手改）：說明頁（about／guide／sources／downloads／methodology，自有結構站只有證據等級頁與隱私頁）加本站資料區塊（`<!-- local-facts -->`）、證據等級頁的事實段與藥名表（`<!-- tier-facts -->`、`<!-- tier-table -->`）、隱私頁的適用法律／權利／著作權與資料來源段（`<!-- privacy-law -->`）；en／es／de 樣板站的共用長段落縮成一段（`<!-- local-condensed -->`）。
資料檔 `docs/_data/local_facts.json`、`docs/_data/evidence_tier_facts.json` 由 `scripts/local_facts.py`（＝母目錄 `.claude/local_facts_lib.py`）依藥物頁、許可證快照、查核紀錄、FHIR 算；`apply_drug_reviews.py`、許可證快照程式結尾會自動 `--write`，`check_seo_docs.py` 跑 `--check` 擋過期。跨站欄位（cross：本站獨有預測、30 站中位數）與頁面區塊只由母目錄產生器更新；藥物頁改等級、noindex 或預測後要在母目錄重跑。

## 藥物頁 description 句尾在地化（2026-11-19）

用戶 2026-11-19 決定（「藥物頁簡述在地化」，SEO 工具判定 30 站藥物頁近似重複，原因之一是 description 句尾都是同一句「原適應症：本地資料未記載」）：公開藥物頁（排除 noindex、轉址頁）front matter description 句尾的「Indicación original: No consta en los datos locales」換成本站許可證快照事實層（`snapshots/*_licenses.json.gz`，經 `src/*/regulatory/licenses.py` 的 snapshot()）的品項數句子，資料名稱照本站口徑：AEMPS 許可（comercializadas／autorizadas no comercializadas）。藥名、預測新適應症、等級字樣不動（母目錄 sync_description_levels.py 照舊對得到）；已有原適應症原文的頁不動。
例：abatacept「Indicación original: No consta en los datos locales」→「En España, autorizaciones de la AEMPS: 3 (comercializadas: 3)」；2026-11-19 改了 537 頁。
由母目錄 `.claude/drug_meta_description.py --apply --site ESTxGNN` 產生（站上複本 `tools/txgnn/.claude/drug_meta_description.py --apply --root .`），改動記在 `docs/_data/description_local_log.json`（pages＝目前句尾與原字樣、entries＝每次改動前後整行，可還原）。快照數字變了重跑會換新數字；`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾會自動 --apply，`check_seo_docs.py` 跑 --check 擋「還是未記載句尾」或「數字跟快照不符」。只改 front matter，lastmod_fix 不算正文改動、last_modified_at 不動。
同日修：`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾重算 local_facts 的 atexit 掛鉤在結束時取不到 `__file__`（NameError，之前其實沒跑成），改成先算好路徑。

## 事實層單方／複方依本站成分欄切分（2026-11-24）

用戶 2026-11-24 決定：事實層依各站成分欄正確切分。reviewer/drug_evidence_pack.py 原本用「;;」切成分，本站 CIMA practiv 的複方以「 + 」（少數「, 」）連接，都算成單方；改用 `src/estxgnn/regulatory/ingredients.py`，scripts/sync_license_tables.py 快照的 single_real 也改用同一規則（tezacaftor「deutivacaftor, tezacaftor, vanzacaftor」原本漏判）。
事實層 1534 藥中 102 藥 single_total 改變；證據包 100 個重算（data-overlay）。寬偵測掃事實有變的頁，跟成分欄矛盾 1 句（alanine 待辦「autorización monocomponente según el registro」，TEBETANE COMPUESTO 實為複方），以 `es-lic-20261124d-alanine-1` 更正。B 改寫 0 句；checker 0→0。
