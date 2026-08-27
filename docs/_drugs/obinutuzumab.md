---
layout: default
title: Obinutuzumab
parent: 僅模型預測 (L5)
nav_order: 199
evidence_level: L5
indication_count: 3
---

# Obinutuzumab
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

# Obinutuzumab: De Leucemia Linfocitica Cronica a Linfoma Folicular

## Resumen en Una Frase

Obinutuzumab es un anticuerpo monoclonal anti-CD20, conocido principalmente por su uso en leucemia linfocitica cronica (LLC). El modelo TxGNN predice que podria ser efectivo para **Linfoma Folicular**, con **50 ensayos clinicos** y **20 publicaciones** que actualmente respaldan esta direccion, incluyendo multiples ensayos de Fase 3 ya completados.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Leucemia linfocitica cronica (segun informacion publica conocida; no consta en los datos de autorizacion de España proporcionados) |
| Nueva Indicacion Predicha | Linfoma Folicular |
| Puntaje de Prediccion TxGNN | 99.18% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Proceed with Guardrails |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion en este Evidence Pack. Segun la informacion conocida, obinutuzumab es un anticuerpo monoclonal anti-CD20 de segunda generacion, glicoingenierizado tipo II, cuya eficacia en leucemia linfocitica cronica ha sido comprobada, y mecanisticamente podria ser aplicable al linfoma folicular.

Tanto la LLC como el linfoma folicular son neoplasias de celulas B que expresan de forma consistente el antigeno CD20. El mecanismo de accion de obinutuzumab (citotoxicidad celular dependiente de anticuerpos, fagocitosis dependiente de anticuerpos y muerte celular directa) no depende del subtipo especifico de neoplasia B, sino de la expresion de CD20 en la superficie celular, lo que da soporte biologico razonable a esta prediccion.

Esta razonabilidad mecanistica se ve fuertemente reforzada por la evidencia clinica real: obinutuzumab ya cuenta con multiples ensayos de Fase 3 completados en linfoma folicular no tratado previamente (p. ej. GALLIUM), lo que confirma que la prediccion del modelo TxGNN coincide con una via de desarrollo clinico ya validada a nivel internacional, aunque aun no reflejada en el mercado local segun los datos de este Evidence Pack.

## Evidencia de Ensayos Clinicos

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06108232](https://clinicaltrials.gov/study/NCT06108232) | Fase 2 | Activo, no reclutando | 33 | Obinutuzumab + CC-99282 en linfoma folicular de alta carga tumoral no tratado previamente |
| [NCT02871219](https://clinicaltrials.gov/study/NCT02871219) | Fase 2 | Completado | 96 | Obinutuzumab + lenalidomida en linfoma folicular en estadio II-IV, grado 1-3a, no tratado previamente |
| [NCT01582776](https://clinicaltrials.gov/study/NCT01582776) | Fase 1b/2 | Completado | 317 | Obinutuzumab + lenalidomida en linfoma folicular no tratado y recaida/refractario, en 3 poblaciones distintas |
| [NCT06191744](https://clinicaltrials.gov/study/NCT06191744) | Fase 3 | Reclutando | 1095 | Epcoritamab + rituximab/lenalidomida vs quimioinmunoterapia (con esquemas de obinutuzumab) en LF no tratado; ensayo confirmatorio de gran tamano |
| [NCT05899621](https://clinicaltrials.gov/study/NCT05899621) | N/A | Reclutando | 332 | Estudio observacional del mundo real sobre eficacia y seguridad de terapia basada en obinutuzumab en LF no tratado |
| [NCT01691898](https://clinicaltrials.gov/study/NCT01691898) | Fase 1/2 | Completado | 231 | Polatuzumab vedotin/pinatuzumab + rituximab u obinutuzumab en linfoma B no Hodgkin recaido/refractario (incluye LF) |
| [NCT06806033](https://clinicaltrials.gov/study/NCT06806033) | Fase 2 | Reclutando | 100 | Optimizacion del perfil de sindrome de liberacion de citocinas para glofitamab + quimioterapia en linfoma B agresivo recaido/refractario |
| [NCT05169658](https://clinicaltrials.gov/study/NCT05169658) | Fase 2 | Completado | 42 | Mosunetuzumab subcutaneo con/sin polatuzumab vedotin y obinutuzumab en linfoma B indolente no tratado |
| [NCT06918015](https://clinicaltrials.gov/study/NCT06918015) | Fase 2 | Aun no reclutando | 58 | Zanubrutinib + esquema GCVP (incluye obinutuzumab) en linfoma folicular no tratado |
| [NCT04450173](https://clinicaltrials.gov/study/NCT04450173) | Fase 2 | Activo, no reclutando | 40 | Obinutuzumab + ibrutinib + venetoclax en LF no tratado; poblacion y relevancia menos definida (esquema tipico de LLC) |

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28976863](https://pubmed.ncbi.nlm.nih.gov/28976863/) | 2017 | ECA | The New England Journal of Medicine | Estudio GALLIUM: compara quimioterapia basada en rituximab vs obinutuzumab en LF avanzado no tratado previamente |
| [29856692](https://pubmed.ncbi.nlm.nih.gov/29856692/) | 2018 | ECA | Journal of Clinical Oncology | Analisis de GALLIUM sobre la influencia del esquema de quimioterapia en eficacia/seguridad de obinutuzumab vs rituximab en LF no tratado |
| [37506346](https://pubmed.ncbi.nlm.nih.gov/37506346/) | 2023 | ECA | Journal of Clinical Oncology | Estudio ROSEWOOD: zanubrutinib + obinutuzumab vs obinutuzumab en monoterapia en LF recaido/refractario |
| [31296423](https://pubmed.ncbi.nlm.nih.gov/31296423/) | 2019 | ECA | The Lancet Haematology | Estudio GALEN: obinutuzumab + lenalidomida en linfoma B folicular recaido/refractario |
| [31360086](https://pubmed.ncbi.nlm.nih.gov/31360086/) | 2017 | Cohorte | Blood and Lymphatic Cancer: Targets and Therapy | Revision del impacto de obinutuzumab solo y en combinacion en linfoma folicular |
| [37767550](https://pubmed.ncbi.nlm.nih.gov/37767550/) | 2024 | Cohorte | Haematologica | Estudio GO29365: polatuzumab vedotin + bendamustina y rituximab u obinutuzumab en LF recaido/refractario |
| [38660754](https://pubmed.ncbi.nlm.nih.gov/38660754/) | 2024 | Revision | Turkish Journal of Haematology | Revision integral del manejo actual del linfoma folicular |
| [39830356](https://pubmed.ncbi.nlm.nih.gov/39830356/) | 2024 | Revision | Frontiers in Pharmacology | Revision rapida de eficacia, seguridad y costo-efectividad de obinutuzumab en LF |
| [28276536](https://pubmed.ncbi.nlm.nih.gov/28276536/) | 2016 | Revision | Drugs of Today | Revision de obinutuzumab como anticuerpo anti-CD20 de nueva generacion en LF |
| [35180337](https://pubmed.ncbi.nlm.nih.gov/35180337/) | 2022 | Revision | Oncology (Williston Park) | Revision de terapias actuales y emergentes para linfoma folicular |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificacion de Citotoxicidad | Terapia dirigida / Inmunoterapia (anticuerpo monoclonal anti-CD20, no quimioterapia citotoxica convencional) |
| Riesgo de Mielosupresion | Consultar las advertencias y precauciones del prospecto (sin datos especificos en este Evidence Pack) |
| Clasificacion de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Proteccion en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

## Conclusion y Proximos Pasos

**Decision: Proceed with Guardrails**

**Justificacion:**
La evidencia internacional es solida (nivel L1): multiples ensayos de Fase 2/3 completados, incluyendo el ensayo pivotal GALLIUM y el confirmatorio ROSEWOOD, respaldan la eficacia de obinutuzumab en linfoma folicular. Sin embargo, el farmaco no esta actualmente comercializado en España (0 autorizaciones) y faltan datos criticos de seguridad local, por lo que no puede avanzar sin salvaguardas adicionales.

**Para avanzar se necesita:**
- Datos del prospecto/AEMPS sobre advertencias y contraindicaciones (brecha bloqueante, DG001)
- Confirmacion via DrugBank del mecanismo de accion detallado y perfil de toxicidad (DG002)
- Evaluacion de la via regulatoria para autorizacion de comercializacion en España, dado el estado actual de "no comercializado"
- Datos especificos de interacciones farmacologicas (DDI), actualmente no disponibles
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

