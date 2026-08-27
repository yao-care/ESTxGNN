---
layout: default
title: Plerixafor
parent: 僅模型預測 (L5)
nav_order: 226
evidence_level: L5
indication_count: 7
---

# Plerixafor
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Plerixafor: De Movilización de Células Madre a Leucemia Mieloide

## Resumen en Una Frase

Plerixafor es un antagonista de CXCR4 utilizado establecidamente para la movilización de células madre hematopoyéticas antes de trasplante, según confirman múltiples ensayos incluidos en este informe.
El modelo TxGNN predice que podría ser efectivo como agente sensibilizador en **Leucemia Mieloide (principalmente LMA)**,
con **30 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección — con diferencia, la indicación con más evidencia real entre las 7 candidatas evaluadas para este fármaco.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Movilización de células madre hematopoyéticas periféricas para trasplante (autólogo/alogénico), uso confirmado en los propios ensayos del evidence pack (p. ej. NCT01696461, NCT00241358) |
| Nueva Indicación Predicha | Leucemia Mieloide (Myeloid Leukemia) |
| Puntaje de Predicción TxGNN | 99.02% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold (Pregunta de Investigación) |

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados del mecanismo de acción en DrugBank para este análisis (data gap señalado en el propio evidence pack). Según la información conocida a partir de los propios ensayos clínicos recopilados, Plerixafor es un antagonista del receptor CXCR4 que bloquea el eje CXCR4/CXCL12(SDF-1α), utilizado clínicamente para movilizar células madre hematopoyéticas desde el nicho de la médula ósea hacia la sangre periférica.

Ese mismo eje CXCR4/CXCL12 ancla a las células madre leucémicas dentro del nicho protector de la médula ósea en la leucemia mieloide aguda (LMA), donde quedan protegidas de la quimioterapia. La hipótesis mecanicista, respaldada por más de una decena de ensayos Fase 1/2 en el evidence pack, es que bloquear CXCR4 con plerixafor moviliza también a las células leucémicas hacia la sangre periférica, aumentando su sensibilidad a agentes citotóxicos (quimiosensibilización) — un uso conceptualmente derivado de su mecanismo de movilización ya aprobado, no una indicación terapéutica nueva desde cero.

Cabe señalar que, de las 7 indicaciones predichas por TxGNN para este fármaco, las otras 6 (mieloma indolente, CMM7, melanoma leptomeníngeo pediátrico, melanoma uveal, bronquitis, melanoma vulvar) no cuentan con ningún ensayo ni literatura de respaldo (nivel L5, Hold) — la leucemia mieloide es la única con evidencia clínica sustancial.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01435343](https://clinicaltrials.gov/study/NCT01435343) | Fase 1/2 | Completado | 55 | Terapia de inducción con fludarabina, idarubicina, citarabina, G-CSF y plerixafor en LMA en recaída/refractaria en pacientes jóvenes |
| [NCT00906945](https://clinicaltrials.gov/study/NCT00906945) | Fase 1/2 | Completado | 39 | Plerixafor + G-CSF como quimiosensibilizador en LMA en recaída/refractaria |
| [NCT01455025](https://clinicaltrials.gov/study/NCT01455025) | Fase 1 | Terminado | 11 | Escalada de dosis de plerixafor combinado con inducción/consolidación en LMA en recaída |
| [NCT00822770](https://clinicaltrials.gov/study/NCT00822770) | Fase 1/2 | Completado | 47 | G-CSF + plerixafor con busulfán/fludarabina en trasplante alogénico para LMA/SMD/LMC |
| [NCT00943943](https://clinicaltrials.gov/study/NCT00943943) | Fase 1 | Completado | 33 | G-CSF + plerixafor + sorafenib en LMA con mutación FLT3 |
| [NCT02605460](https://clinicaltrials.gov/study/NCT02605460) | Fase 2 | Desconocido | 20 | Quimiosensibilización con antagonista de CXCR4 antes de trasplante en leucemia aguda en remisión |
| [NCT06141304](https://clinicaltrials.gov/study/NCT06141304) | Fase 2 | Desconocido | 28 | Plerixafor + infusión de linfocitos del donante en leucemia aguda en recaída post-trasplante alogénico |
| [NCT00241358](https://clinicaltrials.gov/study/NCT00241358) | Fase 1/2 | Completado | 92 | Movilización y trasplante de células madre de donante HLA-compatible con AMD3100 (plerixafor) en neoplasias hematológicas avanzadas |
| [NCT04762875](https://clinicaltrials.gov/study/NCT04762875) | Fase 2 | Terminado | 7 | MGTA-145 combinado con plerixafor para movilización/trasplante en neoplasias hematológicas |
| [NCT01413568](https://clinicaltrials.gov/study/NCT01413568) | Fase 1/2 | Completado | 38 | Seguridad de POL6326 (otro antagonista de CXCR4) como agente único de movilización — referencia mecanicista |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29392425](https://pubmed.ncbi.nlm.nih.gov/29392425/) | 2018 | Ensayo Fase 1/2 | Annals of Hematology | Régimen PLERIFLAG (plerixafor + FLAG-Ida) en LMA en primera recaída temprana o refractaria |
| [32697348](https://pubmed.ncbi.nlm.nih.gov/32697348/) | 2020 | Ensayo Fase 1 | American Journal of Hematology | Sorafenib + G-CSF + plerixafor en LMA con mutación FLT3-ITD en recaída/refractaria |
| [22308295](https://pubmed.ncbi.nlm.nih.gov/22308295/) | 2012 | Ensayo Fase 1/2 | Blood | Quimiosensibilización con el antagonista de CXCR4 plerixafor en 52 pacientes con LMA en recaída/refractaria |
| [29724902](https://pubmed.ncbi.nlm.nih.gov/29724902/) | 2018 | Ensayo Fase 1 | Haematologica | Plerixafor combinado con decitabina en pacientes mayores con LMA de nuevo diagnóstico |
| [32877869](https://pubmed.ncbi.nlm.nih.gov/32877869/) | 2020 | Revisión Sistemática/Metanálisis | Leukemia Research | Plerixafor combinado con quimioterapia y/o trasplante en leucemia aguda: revisión de estudios preclínicos y clínicos |
| [39261603](https://pubmed.ncbi.nlm.nih.gov/39261603/) | 2024 | Revisión | Leukemia | CXCR4 como diana terapéutica en leucemia mieloide aguda |
| [32079173](https://pubmed.ncbi.nlm.nih.gov/32079173/) | 2020 | Revisión | Biology | Antagonistas de CXCR4 como movilizadores y sensibilizadores en LMA y glioblastoma |
| [30654137](https://pubmed.ncbi.nlm.nih.gov/30654137/) | 2019 | Estudio de Cohorte | Biology of Blood and Marrow Transplantation | Seguridad y tolerabilidad de plerixafor en régimen mieloablativo previo a trasplante alogénico en LMA |
| [33080779](https://pubmed.ncbi.nlm.nih.gov/33080779/) | 2020 | Revisión | Cells | Hiperleucocitosis y leucostasis en LMA: fisiopatología molecular subyacente |
| [27822339](https://pubmed.ncbi.nlm.nih.gov/27822339/) | 2016 | Revisión | World Journal of Stem Cells | Actualización sobre células madre leucémicas en LMA: descubrimientos y oportunidades terapéuticas |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold (Pregunta de Investigación)**

**Justificación:**
La evidencia acumulada (30 ensayos, mayoritariamente Fase 1/2, varios completados pero varios también terminados o de estado desconocido, sin ningún ECA de Fase 3 confirmatorio) respalda una hipótesis mecanicista sólida de quimiosensibilización vía CXCR4 en leucemia mieloide, pero no alcanza el umbral de un ECA Fase 2/3 concluyente que justifique avanzar directamente a "Go" o "Proceed with Guardrails".

**Para avanzar se necesita:**
- Datos de advertencias/contraindicaciones del prospecto TFDA/AEMPS (actualmente bloqueante — DG001, impide la evaluación de seguridad S1)
- Datos del mecanismo de acción (MOA) desde DrugBank para consolidar el análisis de plausibilidad mecanística (DG002)
- Un ensayo Fase 2/3 controlado y confirmatorio específico para quimiosensibilización en LMA, dado que los estudios actuales son mayoritariamente de dosis-escalada o piloto de un solo brazo
- Evaluación de vías de administración disponibles y compatibilidad de formulación para esta nueva indicación
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

