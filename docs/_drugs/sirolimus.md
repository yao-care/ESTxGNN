---
layout: default
title: Sirolimus
parent: 僅模型預測 (L5)
nav_order: 260
evidence_level: L5
indication_count: 10
---

# Sirolimus
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Sirolimus: De Prevención del Rechazo de Trasplante Renal a Liposarcoma

## Resumen en Una Frase

Sirolimus (rapamicina) es un inhibidor de mTOR utilizado clásicamente como inmunosupresor para prevenir el rechazo en trasplante renal. El modelo TxGNN predice que podría ser efectivo para **Liposarcoma**, con **5 ensayos clínicos** y **12 publicaciones** que actualmente respaldan esta dirección (aunque gran parte de la evidencia usa análogos de sirolimus como temsirolimus, everolimus y ridaforolimus).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Prevención del rechazo de trasplante renal (inmunosupresión) — según información farmacológica conocida; no hay ficha técnica española que lo confirme, ya que el fármaco no está comercializado en España |
| Nueva Indicación Predicha | Liposarcoma |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Research Question (profundizar antes de decidir) |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha técnica española. Según la información farmacológica conocida, sirolimus se une a la proteína FKBP12 e inhibe mTOR (mammalian target of rapamycin), bloqueando la proliferación de linfocitos T dependiente de IL-2; este mecanismo es la base de su uso histórico como inmunosupresor en trasplante renal.

La vía mTOR es también un regulador central del crecimiento celular y está frecuentemente hiperactivada en tumores sólidos. En liposarcoma desdiferenciado se ha demostrado activación directa de las vías Akt-mTOR y MAPK (PMID 26518767), lo que da una base mecanística concreta para el uso de inhibidores de mTOR en este tumor. De hecho, la literatura incluida en este paquete de evidencia ya documenta que sirolimus reduce el riesgo de cáncer en receptores de trasplante renal (PMID 16434506), reforzando la plausibilidad de su efecto antitumoral independiente de su acción inmunosupresora.

Es importante matizar que la mayoría de los ensayos clínicos relevantes (AP23573/ridaforolimus, temsirolimus, everolimus) prueban análogos de sirolimus y no la molécula original; solo un ensayo (NCT02821507) evalúa sirolimus per se, en combinación con ciclofosfamida, específicamente en liposarcoma mixoide. Esto sugiere un efecto de clase plausible, pero con evidencia directa aún limitada para sirolimus como monofármaco.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Fase 2 | Completado | 70 | Combinación de sirolimus y ciclofosfamida en liposarcoma mixoide/condrosarcoma metastásico o irresecable |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Fase 2 | Completado | 216 | AP23573 (ridaforolimus, inhibidor de mTOR) en sarcoma avanzado, incluyendo liposarcoma |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Fase 2 | Completado | 46 | Cixutumumab + temsirolimus en tumores sólidos pediátricos recurrentes/refractarios (incl. sarcoma) |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Fase 2 | Activo, no reclutando | 48 | Ribociclib + everolimus en liposarcoma desdiferenciado y leiomiosarcoma avanzados |
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Fase 1/2 | Completado | 24 | Torisel (temsirolimus) + doxorrubicina liposomal en sarcomas de tejido blando y óseo avanzados |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | ECA (Fase 2) | Clin Cancer Res | Ribociclib + everolimus en liposarcoma desdiferenciado y leiomiosarcoma avanzados (SAR-096) |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Revisión | Cancers | Panorama de nuevas terapias dirigidas en sarcoma de tejido blando |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Mecanístico/traslacional | Tumour Biology | Activación de las vías Akt-mTOR y MAPK en liposarcoma desdiferenciado |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Revisión | Curr Opin Oncol | Nuevos tratamientos dirigidos para sarcomas avanzados |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Revisión | Bull Cancer | Tratamiento dirigido de tumores raros de tejido conectivo y sarcomas |
| [37400145](https://pubmed.ncbi.nlm.nih.gov/37400145/) | 2023 | Preclínico (PDX) | Cancer Genomics Proteomics | Cloroquina + rapamicina como tratamiento sinérgico para liposarcoma bien diferenciado |
| [36309387](https://pubmed.ncbi.nlm.nih.gov/36309387/) | 2022 | Preclínico (PDOX) | In Vivo | Cloroquina + rapamicina detiene el crecimiento tumoral en modelo PDOX de liposarcoma desdiferenciado |
| [25519700](https://pubmed.ncbi.nlm.nih.gov/25519700/) | 2015 | Preclínico | Mol Cancer Ther | MLN0128, inhibidor de mTOR quinasa, con actividad antitumoral en sarcoma óseo y de tejido blando |
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | Cohorte (RCT) | J Am Soc Nephrol | Sirolimus tras retirada precoz de ciclosporina reduce el riesgo de cáncer en trasplante renal |
| [20534289](https://pubmed.ncbi.nlm.nih.gov/20534289/) | 2010 | Serie de casos | Transplant Proc | Conversión a rapamicina como inmunosupresión tras aparición de neoplasia en trasplante renal |

*Nota: se excluyeron 2 referencias del conjunto original de 12 por menor relevancia directa con liposarcoma (una sobre cribado oncológico general en trasplantados y otra sobre una anomalía vascular no tumoral, FAVA).*

## Información de Mercado en España

Sirolimus no está actualmente comercializado en España (`market_status: 未上市`) y no existen autorizaciones registradas en la base consultada (0 licencias). No es posible presentar una tabla de autorizaciones/marcas comerciales con los datos disponibles.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se dispone de datos verificados de advertencias, contraindicaciones ni interacciones farmacológicas (DDI) en esta evaluación.

## Conclusión y Próximos Pasos

**Decisión: Research Question (profundizar antes de decidir)**

**Justificación:**
Existe una base mecanística sólida (activación de Akt-mTOR/MAPK en liposarcoma) y múltiples ensayos de Fase 2 con inhibidores de mTOR, pero la mayoría emplea análogos de sirolimus (temsirolimus, everolimus, ridaforolimus) en combinación con otros fármacos, y solo un ensayo evalúa sirolimus per se. La evidencia es prometedora pero insuficiente para una recomendación firme de avance directo.

**Para avanzar se necesita:**
- Datos formales de MOA desde DrugBank (actualmente bloqueado por Data Gap)
- Ficha técnica/advertencias de la AEMPS (el fármaco no está comercializado en España, por lo que habría que evaluar vías de acceso: uso compasivo, importación, medicamento extranjero)
- Evidencia clínica que use sirolimus como monofármaco (no solo análogos) específicamente en subtipos de liposarcoma
- Perfil de seguridad e interacciones farmacológicas completo antes de cualquier uso off-label
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

