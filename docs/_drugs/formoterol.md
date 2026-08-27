---
layout: default
title: Formoterol
parent: 僅模型預測 (L5)
nav_order: 122
evidence_level: L5
indication_count: 6
---

# Formoterol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Formoterol: De Farmaco No Comercializado en España a Candidato en Enfermedad Pulmonar Obstructiva

## Resumen en Una Frase

Formoterol es un agonista beta-2 adrenergico de accion prolongada (LABA) que actualmente **no consta comercializado en España** (0 autorizaciones registradas en esta evidence pack). Entre las 6 indicaciones predichas por TxGNN, **Enfermedad Pulmonar Obstructiva** es la que presenta el respaldo mas solido, con **50 ensayos clinicos** y **20 publicaciones** asociadas, incluyendo el ensayo pivotal ETHOS (reduccion de mortalidad por todas las causas). La prediccion mejor puntuada por el modelo (respiratory malformation) carece de toda evidencia real y ha sido senalada por el propio sistema como un probable artefacto de mapeo del grafo de conocimiento.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Nueva Indicacion Predicha | Enfermedad Pulmonar Obstructiva |
| Puntaje de Prediccion TxGNN | 99.90% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Proceed with Guardrails |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion en esta evidence pack (campo `original_moa` sin informacion). Segun la informacion clinica conocida de la sustancia, formoterol es un **agonista beta-2 adrenergico de accion prolongada (LABA)**: activa los receptores beta-2 del musculo liso bronquial, aumenta el AMPc intracelular y produce relajacion del musculo liso de la via aerea, con inicio de accion rapido (minutos) y duracion de hasta 12 horas.

Este mecanismo es directamente aplicable a cualquier enfermedad caracterizada por obstruccion funcional del flujo aereo — precisamente el nucleo de las tres indicaciones mejor respaldadas por evidencia en este analisis: **Enfermedad Pulmonar Obstructiva**, **bronquitis** y **asma**. En estas tres, formoterol se usa habitualmente en combinacion con corticosteroides inhalados (ICS) y/o antimuscarinicos de accion prolongada (LAMA), configuracion que sustenta ensayos de referencia como ETHOS, KRONOS y FULFIL.

Por el contrario, el mecanismo broncodilatador **no tiene fundamento farmacologico** para actuar sobre anomalias estructurales congenitas (respiratory malformation), sindromes de tejido conectivo mediados por la via TGF-beta (Rienhoff syndrome), ni sobre rasgos de susceptibilidad genetica no tratables clinicamente (asthma-related traits, susceptibility to).

## Panorama de las 6 Indicaciones Predichas por TxGNN

El modelo genero 6 predicciones para formoterol. Se presentan ordenadas por puntaje para transparencia, ya que la de mayor puntaje **no es la de mayor plausibilidad clinica**:

| Rank | Indicacion | Puntaje TxGNN | Nivel Evidencia | Recomendacion | Observacion |
|------|-----------|---------------|------------------|----------------|-------------|
| 1 | Respiratory malformation | 99.92% | L4 | Hold | Probable artefacto de mapeo del grafo de conocimiento; sin base mecanistica ni ensayos reales relevantes |
| 2 | Bronquitis | 99.92% | L1 | Proceed with Guardrails | Fenotipo de EPOC; multiples ensayos Fase 3 (ej. NCT01437397, 1692 pacientes) |
| 3 | Rienhoff syndrome | 99.90% | L5 | Hold | Sindrome de tejido conectivo (via TGF-beta); sin relacion mecanistica ni evidencia |
| 4 | **Enfermedad Pulmonar Obstructiva** | 99.90% | L1 | Proceed with Guardrails | Indicacion nuclear de LABA; ensayo pivotal ETHOS con reduccion de mortalidad |
| 5 | Asma | 99.74% | L1 | Proceed with Guardrails | Indicacion nuclear de LABA; multiples ECA en NEJM (O'Byrne 2018) |
| 6 | Susceptibilidad genetica a rasgos de asma | 99.50% | L5 | Hold | Rasgo de susceptibilidad genetica, no una enfermedad tratable; sin evidencia |

Dado que bronquitis, EPOC y asma comparten gran parte de los mismos ensayos y representan el mismo espectro de enfermedad obstructiva de la via aerea, este informe profundiza en **Enfermedad Pulmonar Obstructiva** por contar con el ensayo de mayor impacto clinico (ETHOS).

## Evidencia de Ensayos Clinicos (Enfermedad Pulmonar Obstructiva)

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02766608](https://clinicaltrials.gov/study/NCT02766608) | Fase 3 | Completado | 2389 | BFF MDI vs FF, budesonida y Symbicort Turbuhaler abierto en EPOC moderada a muy severa durante 24 semanas |
| [NCT01047553](https://clinicaltrials.gov/study/NCT01047553) | Fase 3 | Completado | 251 | Formoterol 18 mcg/dia vs tratamiento estandar en pacientes japoneses con EPOC, 52 semanas |
| [NCT01854658](https://clinicaltrials.gov/study/NCT01854658) | Fase 3 | Completado | 1615 | Glicopirrolato/formoterol (PT003) vs placebo en EPOC moderada a muy severa, 24 semanas |
| [NCT06712563](https://clinicaltrials.gov/study/NCT06712563) | N/A | Reclutando | 2000 | Analisis conjunto multipais de resultados en vida real de budesonida/glicopirronio/formoterol (BGF) |
| [NCT00604500](https://clinicaltrials.gov/study/NCT00604500) | Fase 3 | Completado | 272 | Estudio de manejo del dispositivo MF/F MDI con contador de dosis en asma persistente y EPOC |
| [NCT03590379](https://clinicaltrials.gov/study/NCT03590379) | Fase 2 | Completado | 366 | Triple combinacion CHF5993 (beclometasona/formoterol/glicopirronio) via DPI vs pMDI en EPOC |
| [NCT06480890](https://clinicaltrials.gov/study/NCT06480890) | N/A | Completado | 362 | Efectividad en vida real de triple terapia BDP/FF/GB (Trimbow pMDI) en EPOC, 12 semanas |
| [NCT05097014](https://clinicaltrials.gov/study/NCT05097014) | Fase 4 | Completado | 106 | Triple terapia CHF5993 vs dual CHF1535 sobre hiperinflacion pulmonar y resistencia al ejercicio en EPOC |
| [NCT03276078](https://clinicaltrials.gov/study/NCT03276078) | Fase 2 | Completado | 20 | Farmacocinetica y seguridad de aclidinio/formoterol en pacientes chinos con EPOC moderada a severa |
| [NCT01471340](https://clinicaltrials.gov/study/NCT01471340) | Fase 4 | Completado | 11744 | Estudio de seguridad a gran escala de mometasona/formoterol vs mometasona en asma persistente |

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33252985](https://pubmed.ncbi.nlm.nih.gov/33252985/) | 2021 | ECA | Am J Respir Crit Care Med | Ensayo ETHOS: triple terapia BGF reduce mortalidad por todas las causas vs GFF en EPOC |
| [39213002](https://pubmed.ncbi.nlm.nih.gov/39213002/) | 2025 | ECA | Am J Respir Crit Care Med | Analisis post-hoc de ETHOS: efecto de triple terapia sobre eventos cardiovasculares y cardiopulmonares graves |
| [28375647](https://pubmed.ncbi.nlm.nih.gov/28375647/) | 2017 | ECA | Am J Respir Crit Care Med | Ensayo FULFIL: triple terapia una vez al dia en EPOC |
| [30232048](https://pubmed.ncbi.nlm.nih.gov/30232048/) | 2018 | Revision | Lancet Respir Med | Ensayo KRONOS: BGF vs terapias duales en EPOC moderada a muy severa |
| [40619503](https://pubmed.ncbi.nlm.nih.gov/40619503/) | 2025 | Cohorte | Adv Ther | Efectividad comparativa de FF/UMEC/VI vs BUD/GLY/FORM en pacientes que escalan desde terapia dual |
| [35512458](https://pubmed.ncbi.nlm.nih.gov/35512458/) | 2022 | Cohorte | Respir Med | Relacion entre uso previo de ICS y beneficios de BGF sobre exacerbaciones y funcion pulmonar (ETHOS) |
| [39103901](https://pubmed.ncbi.nlm.nih.gov/39103901/) | 2024 | — | Respir Res | Analisis post-hoc de KRONOS por nivel de eosinofilos e historia de exacerbaciones |
| [33273813](https://pubmed.ncbi.nlm.nih.gov/33273813/) | 2020 | — | Int J Chron Obstruct Pulmon Dis | Revision del uso de formoterol en el tratamiento de EPOC |
| [26049917](https://pubmed.ncbi.nlm.nih.gov/26049917/) | 2015 | — | Eur J Intern Med | Revision extensa sobre broncodilatadores de accion prolongada: formoterol y salmeterol |
| [31951778](https://pubmed.ncbi.nlm.nih.gov/31951778/) | 2020 | — | Expert Rev Clin Pharmacol | Aclidinio/formoterol para el tratamiento de mantenimiento de la EPOC |

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad. La evidence pack no contiene advertencias, contraindicaciones ni interacciones farmacologicas documentadas para formoterol en esta version.

## Conclusion y Proximos Pasos

**Decision: Proceed with Guardrails**

**Justificacion:**
La evidencia clinica para el espectro asma/EPOC/bronquitis es de nivel L1, con multiples ensayos Fase 3 completados y al menos un ensayo pivotal (ETHOS) con impacto en mortalidad — esto corresponde al uso ya establecido y bien caracterizado de los LABA. Sin embargo, el farmaco **no tiene ninguna autorizacion registrada en España** y existe un **data gap de severidad Blocking (DG001)**: falta el prospecto/ficha tecnica de la AEMPS, lo que impide completar la evaluacion de seguridad inicial (S1) independientemente de la solidez de la evidencia de eficacia.

**Para avanzar se necesita:**
- Obtener el prospecto oficial (advertencias, contraindicaciones, interacciones) de la AEMPS — bloqueante para la etapa S1
- Confirmar el mecanismo de accion (MOA) detallado via DrugBank
- Aclarar si "respiratory malformation" y "Rienhoff syndrome" son entidades correctamente mapeadas en el grafo de conocimiento antes de considerarlas en futuras iteraciones
- Descartar "asthma-related traits, susceptibility to" como objetivo de reposicionamiento, al tratarse de un rasgo genetico y no de una enfermedad tratable
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

