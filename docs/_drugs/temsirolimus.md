---
layout: default
title: Temsirolimus
parent: 僅模型預測 (L5)
nav_order: 271
evidence_level: L5
indication_count: 3
---

# Temsirolimus
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Temsirolimus: Hacia una Nueva Indicación en Liposarcoma

## Resumen en Una Frase

La indicación de aprobación original de Temsirolimus no está documentada en este Evidence Pack (dato pendiente de verificación regulatoria — ver vacíos de datos DG001/DG002). El modelo TxGNN predice que Temsirolimus podría ser efectivo para **Liposarcoma**, con **5 ensayos clínicos** y **1 publicación** que respaldan actualmente esta dirección, aunque la mayoría de los ensayos usan fármacos análogos (sirolimus, ridaforolimus) en lugar del propio temsirolimus.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Liposarcoma |
| Puntaje de Predicción TxGNN | 99.54% |
| Nivel de Evidencia | L3 |
| Estado de Mercado | No comercializado (未上市) |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

*(La fila "Indicación Original" se omite: no hay `approved_indication_text` ni `original_indications` disponibles en este Evidence Pack.)*

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción confirmados en este Evidence Pack (DG002, severidad Alta). Según la evidencia recopilada, Temsirolimus es un inhibidor de mTORC1 (relacionado estructuralmente con sirolimus, su metabolito activo), y todos los ensayos clínicos disponibles lo sitúan en un contexto oncológico, frecuentemente en combinación con agentes citotóxicos (doxorrubicina liposomal, ciclofosfamida) o biológicos (cixutumumab).

El liposarcoma desdiferenciado se caracteriza con frecuencia por amplificación de MDM2/CDK4, lo que activa la vía PI3K-AKT-mTOR — un fundamento mecanístico razonable para la inhibición de mTORC1. Sin embargo, la mayoría de la evidencia de ensayos disponible corresponde a fármacos de la misma clase (sirolimus, ridaforolimus) y no al propio temsirolimus, por lo que la relación mecanicista debe considerarse un "efecto de clase" más que evidencia directa del fármaco. Los sarcomas en general muestran tasas de respuesta modestas a la monoterapia con inhibidores de mTOR, por lo que suele requerirse combinación terapéutica.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Fase 1/2 | Completado | 24 | Torisel (temsirolimus) + doxorrubicina liposomal en sarcomas avanzados de tejidos blandos y óseos; uso directo del fármaco evaluado. |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Fase 2 | Completado | 46 | Cixutumumab + Temsirolimus en tumores sólidos pediátricos recurrentes/refractarios (incluye sarcoma); uso directo del fármaco, pero en población pediátrica. |
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Fase 2 | Completado | 70 | Sirolimus (análogo/metabolito activo, no temsirolimus) + ciclofosfamida en liposarcoma mixoide metastásico/irresecable y condrosarcoma; evidencia de clase. |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Fase 2 | Completado | 216 | AP23573 (ridaforolimus, otro inhibidor de mTOR, no temsirolimus) en sarcoma avanzado; evidencia de clase, mayor tamaño muestral. |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Fase 2 | En curso (no reclutando) | 48 | Ribociclib + Everolimus (no temsirolimus) en liposarcoma desdiferenciado y leiomiosarcoma avanzados; solo respalda indirectamente la vía mTOR. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Revisión | Bulletin du cancer | Revisión sobre tratamientos dirigidos en sarcomas y tumores raros del tejido conectivo; clasifica 6 subgrupos moleculares con terapias dirigidas correspondientes. Relevancia general para la vía, no específica de temsirolimus en liposarcoma. |

## Información de Mercado

Temsirolimus no está actualmente comercializado (未上市) y no existe ninguna autorización de comercialización registrada en este Evidence Pack (0 licencias).

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de mTORC1) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Ítems de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El fármaco no tiene ninguna autorización de comercialización (0 licencias, 未上市), el prospecto/advertencias de la TFDA constituyen un vacío de datos Bloqueante (DG001) que impide la evaluación de seguridad S1, y la evidencia clínica específica de temsirolimus en liposarcoma es limitada (dos ensayos con el fármaco propiamente dicho, n=24 y n=46; el resto son análogos de la misma clase).

**Para avanzar se necesita:**
- Prospecto/etiquetado de la TFDA (advertencias y contraindicaciones) — DG001
- Datos de mecanismo de acción (MOA) vía DrugBank — DG002
- Ensayos clínicos que evalúen temsirolimus directamente (no solo análogos) en población adulta con liposarcoma
- Datos de interacciones farmacológicas (DDI) actualmente no disponibles
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

