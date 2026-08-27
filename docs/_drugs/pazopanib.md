---
layout: default
title: Pazopanib
parent: 僅模型預測 (L5)
nav_order: 213
evidence_level: L5
indication_count: 10
---

# Pazopanib
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

評估包含 10 個候選適應症；除 Liposarcoma（脂肪肉瘤,L2/S3/Proceed with Guardrails）外，其餘證據等級多為 L4-L5（Hold），故以證據支持度最高的 Liposarcoma 作為本報告焦點。原始適應症欄位在 Evidence Pack 中為空值/Data Gap，下方以一般公開已知資訊（Pazopanib/Votrient 核准用於晚期腎細胞癌與軟組織肉瘤）補充並明確標註來源，非來自本 Evidence Pack。

```markdown
# Pazopanib: De Carcinoma de Células Renales Avanzado a Liposarcoma

## Resumen en Una Frase

Pazopanib es un inhibidor multi-diana de tirosina quinasa aprobado originalmente para el carcinoma de células renales avanzado y el sarcoma de tejidos blandos *(dato de contexto general, no incluido en el Evidence Pack — ver nota de origen abajo)*.
El modelo TxGNN predice que podría ser efectivo para **Liposarcoma**,
con **9 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección, incluyendo un ensayo Fase 2 dedicado específicamente a esta indicación.

> **Nota de origen:** El Evidence Pack no contiene datos de `original_indications` (campo vacío) ni de `original_moa` (Data Gap). El uso de pazopanib en carcinoma de células renales y sarcoma de tejidos blandos corresponde a conocimiento general de la molécula, no a datos verificados en este paquete.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Carcinoma de células renales avanzado / sarcoma de tejidos blandos (contexto general, no confirmado en Evidence Pack) |
| Nueva Indicacion Predicha | Liposarcoma |
| Puntaje de Prediccion TxGNN | 99.59% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Proceed with Guardrails |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos estructurados de mecanismo de acción (`original_moa` = Data Gap). Sin embargo, según la información recogida en el propio Evidence Pack (razonamiento de reposicionamiento asociado a esta indicación), pazopanib es un inhibidor de tirosina quinasa multi-diana que actúa sobre VEGFR-1/2/3, PDGFR-α/β, FGFR-1/3 y KIT, con actividad antiangiogénica y antitumoral.

El liposarcoma es un grupo heterogéneo de sarcomas de tejido adiposo con alta dependencia de la angiogénesis tumoral; el subtipo desdiferenciado (DDLPS), en particular, presenta con frecuencia activación de la señalización PDGFR. Esta superposición mecanística entre el perfil de pazopanib y la biología del liposarcoma sustenta la plausibilidad de la predicción de TxGNN, y ya existe un ensayo clínico Fase 2 dedicado (NCT01506596) que confirma actividad clínica en esta indicación, lo que refuerza la razonabilidad más allá de la mera predicción del modelo.

## Evidencia de Ensayos Clinicos

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01506596](https://clinicaltrials.gov/study/NCT01506596) | Fase 2 | Completado | 42 | Estudio pivotal de pazopanib en monoterapia para liposarcoma irresecable o metastásico; base de las publicaciones PMID 31010343 y 28832986 |
| [NCT01532687](https://clinicaltrials.gov/study/NCT01532687) | Fase 2 | Completado | 54 | ECA doble ciego: gemcitabina sola vs. + pazopanib en sarcoma de tejidos blandos refractario, incluye población con liposarcoma |
| [NCT02357810](https://clinicaltrials.gov/study/NCT02357810) | Fase 2 | Completado | 178 | Pazopanib combinado con topotecán oral en sarcomas de tejido blando y óseo metastásicos no resecables |
| [NCT02180867](https://clinicaltrials.gov/study/NCT02180867) | Fase 2/3 | Activo, no reclutando | 140 | Ensayo neoadyuvante (PAZNTIS) con/sin pazopanib más quimiorradioterapia en sarcomas de tejidos blandos no rabdomiosarcoma, incluye subtipos de liposarcoma |
| [NCT01692496](https://clinicaltrials.gov/study/NCT01692496) | Fase 2 | Completado | 52 | Actividad y tolerabilidad de pazopanib en liposarcoma avanzado/metastásico recidivante tras terapia estándar |
| [NCT01900743](https://clinicaltrials.gov/study/NCT01900743) | Fase 2 | Completado | 219 | Regorafenib vs. placebo en sarcoma de tejidos blandos metastásico tras fallo de antraciclinas; cohorte A específica de liposarcoma (comparador, no pazopanib) |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Fase 2 | Completado | 131 | SARC024: regorafenib oral en subtipos de sarcoma seleccionados; cita precedente de actividad de pazopanib en sarcomas de tejidos blandos |
| [NCT06239272](https://clinicaltrials.gov/study/NCT06239272) | Fase 1/2 | Reclutando | 139 | NRSTS2021: pazopanib de mantenimiento + radioterapia + selinexor en sarcoma pediátrico no rabdomiosarcoma; relevancia limitada por población pediátrica |
| [NCT06263231](https://clinicaltrials.gov/study/NCT06263231) | Fase 3 | Activo, no reclutando | 333 | INVINCIBLE-3: INT230-6 intratumoral vs. estándar de cuidado en liposarcoma/UPS/leiomiosarcoma; no evalúa pazopanib sistémico directamente |

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28832986](https://pubmed.ncbi.nlm.nih.gov/28832986/) | 2017 | Ensayo Fase 2 prospectivo | Cancer | Resultados del estudio Fase 2 prospectivo, multicéntrico, de pazopanib en monoterapia en liposarcoma irresecable/metastásico de grado intermedio-alto (NCT01506596) |
| [31010343](https://pubmed.ncbi.nlm.nih.gov/31010343/) | 2019 | Revisión de ensayo Fase 2 | Expert Opinion on Investigational Drugs | Análisis de pazopanib como TKI multi-diana en liposarcoma de grado intermedio-alto, resumiendo eficacia y perfil de seguridad |
| [28844815](https://pubmed.ncbi.nlm.nih.gov/28844815/) | 2017 | Comentario/Revisión | The Lancet Oncology | Comentario editorial sobre la actividad de pazopanib en liposarcoma avanzado |
| [33355646](https://pubmed.ncbi.nlm.nih.gov/33355646/) | 2021 | ECA Fase 2 (PAPAGEMO) | JAMA Oncology | Resultados finales del ECA Fase 2 de pazopanib con/sin gemcitabina en sarcoma de tejidos blandos refractario a antraciclina/ifosfamida |
| [25500074](https://pubmed.ncbi.nlm.nih.gov/25500074/) | 2014 | Preclínico | Translational Oncology | Pazopanib suprime el crecimiento tumoral vía inhibición de angiogénesis en modelos de xenoinjerto de liposarcoma desdiferenciado |
| [35609512](https://pubmed.ncbi.nlm.nih.gov/35609512/) | 2022 | Revisión | Oncology Research and Treatment | Revisión de opciones de tratamiento sistémico establecidas y experimentales para liposarcoma avanzado, incluyendo pazopanib |
| [32026050](https://pubmed.ncbi.nlm.nih.gov/32026050/) | 2020 | Revisión | Current Treatment Options in Oncology | Revisión de opciones de terapia sistémica para liposarcoma desdiferenciado |
| [37298520](https://pubmed.ncbi.nlm.nih.gov/37298520/) | 2023 | Revisión | International Journal of Molecular Sciences | Tratamiento del liposarcoma desdiferenciado en la era de la inmunoterapia |
| [34356494](https://pubmed.ncbi.nlm.nih.gov/34356494/) | 2021 | Estudio traslacional | Biology | Perfil molecular y patológico de muestras de sarcoma de tejidos blandos de alto riesgo antes/después de pazopanib neoadyuvante (estudio GISG-04/NOPASS) |
| [30060824](https://pubmed.ncbi.nlm.nih.gov/30060824/) | 2018 | Reporte de caso preclínico | Tissue & Cell | Liposarcoma pleomórfico resistente a doxorrubicina con amplificación de PDGFRA, tratado y regresionado con pazopanib en modelo PDOX |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificacion de Citotoxicidad | Terapia dirigida — inhibidor multi-diana de tirosina quinasa (VEGFR-1/2/3, PDGFR-α/β, FGFR-1/3, KIT) |
| Riesgo de Mielosupresion | Consultar las advertencias y precauciones del prospecto |
| Clasificacion de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Proteccion en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusion y Proximos Pasos

**Decision: Proceed with Guardrails**

**Justificacion:**
Existe un ensayo Fase 2 dedicado (NCT01506596) y evidencia de nivel L2 respaldando la actividad de pazopanib en liposarcoma, pero el fármaco no está comercializado en España (0 autorizaciones) y faltan datos críticos de seguridad (advertencias, contraindicaciones, interacciones) y de mecanismo de acción, lo que impide avanzar directamente a decisión "Go".

**Para avanzar se necesita:**
- Datos de advertencias y contraindicaciones del prospecto (TFDA/AEMPS) — actualmente bloqueante (DG001)
- Datos detallados del mecanismo de acción (MOA) vía DrugBank (DG002)
- Confirmación del estado regulatorio y de autorización de comercialización en España
- Datos de interacciones farmacológicas (DDI), actualmente no encontrados
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

