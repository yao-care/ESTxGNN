---
layout: default
title: Tegafur
parent: 僅模型預測 (L5)
nav_order: 270
evidence_level: L5
indication_count: 10
---

# Tegafur
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

# Tegafur: De Cáncer Gástrico a Neoplasia de Colon

## Resumen en Una Frase

Tegafur es un profármaco oral de 5-fluorouracilo (5-FU), utilizado clásicamente —como componente de combinaciones como UFT (tegafur+uracilo) y S-1 (tegafur+gimeracil+oteracil)— en el tratamiento del cáncer gástrico y otros tumores sólidos.
El modelo TxGNN predice que podría ser efectivo para **Neoplasia de Colon**,
con **30 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer gástrico (indicación clásica de tegafur/UFT/S-1; ver justificación abajo) |
| Nueva Indicación Predicha | Neoplasia de Colon |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco (dato marcado como pendiente en DrugBank). Según la información conocida en la literatura, tegafur es un profármaco de 5-fluorouracilo (5-FU) y forma parte de combinaciones orales como UFT (tegafur + uracilo) y S-1 (tegafur + gimeracil + oteracil); tras su conversión hepática vía CYP2A6, el 5-FU liberado inhibe la enzima timidilato sintasa, bloqueando la síntesis de ADN y ejerciendo citotoxicidad directa sobre células de rápida proliferación.

El cáncer gástrico y la neoplasia de colon son ambos tumores del tracto gastrointestinal con perfil de sensibilidad farmacológica similar. De hecho, una revisión de referencia (PMID 17952521) documenta que UFT ya se emplea como quimioterapia adyuvante postoperatoria establecida en carcinomas de pulmón, estómago, colon/recto y mama, lo que respalda mecanísticamente la extensión de uso hacia la neoplasia de colon.

Esta plausibilidad mecanística está además fuertemente respaldada por evidencia clínica directa: múltiples ensayos de Fase 3 completados y de gran tamaño muestral (UFT+LV, S-1, TS-1) ya han evaluado regímenes basados en tegafur específicamente en cáncer de colon/colorrectal como quimioterapia adyuvante, lo que sitúa esta predicción del modelo TxGNN muy cerca de una práctica clínica ya validada en poblaciones asiáticas.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00378716](https://clinicaltrials.gov/study/NCT00378716) | Fase 3 | Completado | 1608 | UFT + leucovorina vs. 5-FU + leucovorina en cáncer de colon resecado Estadio II/III |
| [NCT00392899](https://clinicaltrials.gov/study/NCT00392899) | Fase 3 | Completado | 2025 | Quimioterapia adyuvante con UFT vs. observación en cáncer de colon Estadio II resecado curativamente |
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Fase 3 | Completado | 1535 | UFT + leucovorina vs. S-1 (TS-1) como tratamiento adyuvante en cáncer de colon Estadio III |
| [NCT00152230](https://clinicaltrials.gov/study/NCT00152230) | Fase 3 | Completado | 900 | UFT adyuvante vs. cirugía sola en cáncer colorrectal Dukes C (NSAS-CC) |
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Fase 3 | Completado | 161 | S-1 vs. capecitabina en primera línea de cáncer colorrectal metastásico (estudio SALTO) |
| [NCT00905047](https://clinicaltrials.gov/study/NCT00905047) | Fase 3 | Completado | 89 | Xeloda (capecitabina) vs. UFT + ácido folínico en cáncer colorrectal avanzado/metastásico, diseño cruzado |
| [NCT00385970](https://clinicaltrials.gov/study/NCT00385970) | Fase 3 | Desconocido | 380 | UFT + PSK vs. UFT + leucovorina como adyuvante en cáncer colorrectal Estadio IIB/III |
| [NCT02887365](https://clinicaltrials.gov/study/NCT02887365) | Fase 4 (título indica Fase 2) | Desconocido | 300 | Tegafur-uracilo como quimioterapia de mantenimiento en cáncer de colon Estadio II MSI-L/MSS |
| [NCT01225744](https://clinicaltrials.gov/study/NCT01225744) | Fase 2 | Completado | 47 | Cetuximab + irinotecán + oxaliplatino + UFT en primera línea de cáncer colorrectal metastásico |
| [NCT00439517](https://clinicaltrials.gov/study/NCT00439517) | Fase 2 | Completado | 302 | FOLFOX-4 + cetuximab vs. UFOX (UFT+oxaliplatino) + cetuximab en cáncer colorrectal metastásico |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | ECA | Clinical Colorectal Cancer | Ensayo ACTS-CC 02: S-1+oxaliplatino (SOX) vs. UFT/LV como adyuvante en cáncer de colon Estadio III de alto riesgo |
| [33714860](https://pubmed.ncbi.nlm.nih.gov/33714860/) | 2021 | ECA | ESMO Open | Actualización a 5 años de supervivencia global del ensayo ACTS-CC 02 (SOX vs. UFT/LV) |
| [33950962](https://pubmed.ncbi.nlm.nih.gov/33950962/) | 2021 | ECA/Cohorte nacional | Medicine | Uracilo-tegafur vs. 5-FU como adyuvante en cáncer de colon Estadio II/III: cohorte nacional taiwanesa y metaanálisis |
| [16648506](https://pubmed.ncbi.nlm.nih.gov/16648506/) | 2006 | ECA | Journal of Clinical Oncology | Ensayo NSABP C-06: UFT+leucovorina oral vs. 5-FU+leucovorina IV en cáncer de colon Estadio II/III |
| [26347106](https://pubmed.ncbi.nlm.nih.gov/26347106/) | 2015 | ECA (Fase 3) | Annals of Oncology | Ensayo JFMC33-0502: duración óptima de UFT/leucovorina adyuvante en cáncer de colon Estadio IIB/III |
| [35168560](https://pubmed.ncbi.nlm.nih.gov/35168560/) | 2022 | Observacional prospectivo | BMC Cancer | JFMC46-1201: eficacia de UFT/LV en cáncer de colon Estadio II de alto riesgo (pareamiento por puntaje de propensión) |
| [38833114](https://pubmed.ncbi.nlm.nih.gov/38833114/) | 2024 | Observacional prospectivo (análisis final) | International Journal of Clinical Oncology | Resultados finales a 5 años del estudio JFMC46-1201 (UFT/LV en cáncer de colon Estadio II de alto riesgo) |
| [15108041](https://pubmed.ncbi.nlm.nih.gov/15108041/) | 2004 | ECA | International Journal of Clinical Oncology | Inmunoquimioterapia adyuvante con OK-432 combinado con HCFU y UFT en cáncer colorrectal |
| [25209093](https://pubmed.ncbi.nlm.nih.gov/25209093/) | 2014 | Revisión | Clinical Colorectal Cancer | Guías de consenso asiático para cáncer colorrectal metastásico, con recomendaciones sobre fluoropirimidinas orales |
| [17952521](https://pubmed.ncbi.nlm.nih.gov/17952521/) | 2007 | Revisión | Surgery Today | UFT como quimioterapia adyuvante postoperatoria en tumores sólidos (pulmón, estómago, colon/recto, mama): evidencia clínica y mecanismo de acción |

---

## Información de Mercado en España

Tegafur actualmente **no está comercializado en España**; no hay autorizaciones de comercialización registradas en los datos disponibles (0 licencias).

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (clase fluoropirimidina, profármaco de 5-FU) |
| Riesgo de Mielosupresión | Moderado (neutropenia y trombocitopenia descritas con frecuencia en regímenes UFT/S-1) |
| Clasificación de Emetogenicidad | Baja a moderada |
| Ítems de Monitoreo | Hemograma completo (con diferencial), función hepática y renal, electrolitos |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos (equipo de protección, preparación en cabina de bioseguridad) |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El nivel de evidencia clínica es L1, respaldado por múltiples ensayos de Fase 3 completados y de gran tamaño muestral que ya validan regímenes basados en tegafur (UFT, S-1/TS-1) en cáncer de colon adyuvante y metastásico. Sin embargo, persisten brechas de datos bloqueantes sobre seguridad local (advertencias/contraindicaciones del prospecto en España) que impiden completar la evaluación inicial de seguridad (S1).

**Para avanzar se necesita:**
- Advertencias y contraindicaciones del prospecto oficial (fuente: AEMPS) — brecha bloqueante (DG001)
- Datos detallados del mecanismo de acción (MOA) desde DrugBank — brecha de alta prioridad (DG002)
- Datos de interacciones farmacológicas (DDI), actualmente no encontrados
- Evaluación de vías de administración disponibles/requeridas, pendiente
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

