---
layout: default
title: Trametinib
parent: 僅模型預測 (L5)
nav_order: 281
evidence_level: L5
indication_count: 10
---

# Trametinib
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

# Trametinib: De Melanoma Cutáneo BRAF-mutado a Melanoma No Cutáneo (y Otros Subtipos de Melanoma)

## Resumen en Una Frase

Trametinib es un inhibidor de MEK1/2 cuyo uso de referencia, según la evidencia de ensayos clínicos disponible en este paquete, es el melanoma cutáneo con mutación BRAF V600E/K (habitualmente en combinación con dabrafenib). El modelo TxGNN predice que el mecanismo podría extenderse a **melanoma no cutáneo** (independientemente del sitio anatómico de origen, siempre que exista mutación BRAF V600), con **50 ensayos clínicos** registrados y evidencia de nivel L1 respaldando esta dirección. Además, el modelo genera un clúster de 8 predicciones adicionales sobre subtipos histológicos/anatómicos de melanoma con niveles de evidencia muy dispares (de L2 a L5), y una predicción no relacionada (coroideremia) que carece de fundamento mecanístico plausible.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original (de referencia, según ensayos registracionales) | Melanoma cutáneo irresecable o metastásico con mutación BRAF V600E/K (no hay licencia local en España que confirmar; ver Mercado) |
| Nueva Indicación Predicha | Melanoma no cutáneo (non-cutaneous melanoma) |
| Puntaje de Predicción TxGNN | 99.30% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

El campo de mecanismo de acción a nivel de fármaco no está disponible en este informe (dato pendiente de completar vía DrugBank). Sin embargo, la propia evidencia de ensayos clínicos recogida permite reconstruir el mecanismo: trametinib es un **inhibidor selectivo de MEK1/2**, que en combinación con el inhibidor de BRAF dabrafenib bloquea de forma dual la vía MAPK/ERK. Esta combinación es el estándar de tratamiento establecido para el melanoma con mutación BRAF V600E/K, como demuestran los ensayos fundacionales fase III incluidos en este paquete (METRIC/NCT01245062, COMBI-d/NCT01584648, COMBI-v/NCT01597908).

La predicción de TxGNN para "melanoma no cutáneo" es razonable porque la elegibilidad para esta terapia depende del **estatus mutacional BRAF V600**, no del sitio anatómico de origen del tumor (piel, mucosa, conjuntiva, párpado, acral, etc.). Es decir, si un melanoma no cutáneo porta la misma mutación driver, el fundamento mecanístico para la inhibición dual MEK/BRAF se mantiene igual. Esto está respaldado por casos reportados de melanoma conjuntival y de párpado con mutación BRAF que respondieron a la combinación BRAF/MEK.

El resto del clúster de predicciones (subtipos histológicos como epitelioide, nodular, de extensión superficial, lentiginoso acral, amelanótico) comparte el mismo razonamiento pero con evidencia mucho más limitada, ya que la prevalencia de mutación BRAF varía por subtipo (por ejemplo, es menor en el subtipo acral, donde predominan mutaciones KIT). La predicción de coroideremia, en cambio, no tiene relación biológica conocida con la vía MAPK/MEK y se considera probable falso positivo del modelo.

---

## Evidencia de Ensayos Clínicos

*(Indicación principal: melanoma no cutáneo — 50 ensayos registrados; se listan los 10 más relevantes)*

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01245062](https://clinicaltrials.gov/study/NCT01245062) | Fase 3 | Completado | 322 | Ensayo registracional (METRIC): GSK1120212 (trametinib) monoterapia vs. quimioterapia en melanoma BRAF V600E/K+ avanzado |
| [NCT01584648](https://clinicaltrials.gov/study/NCT01584648) | Fase 3 | Completado | 423 | COMBI-d: dabrafenib+trametinib vs. dabrafenib+placebo como primera línea en melanoma BRAF V600E/K+ |
| [NCT01597908](https://clinicaltrials.gov/study/NCT01597908) | Fase 3 | Completado | 704 | COMBI-v: dabrafenib+trametinib vs. vemurafenib en melanoma BRAF V600E/K+ |
| [NCT03551626](https://clinicaltrials.gov/study/NCT03551626) | Fase 3b | Completado | 552 | COMBI-APlus: manejo de pirexia en adyuvancia con dabrafenib+trametinib tras resección completa (Grado A) |
| [NCT01072175](https://clinicaltrials.gov/study/NCT01072175) | Fase 1/2 | Completado | 430 | Escalada de dosis fundacional de dabrafenib+trametinib en melanoma metastásico BRAF-mutado (Grado A) |
| [NCT02645149](https://clinicaltrials.gov/study/NCT02645149) | Fase 2 | Completado | 216 | Perfilado molecular y terapia dirigida emparejada en melanoma avanzado irresecable (Grado B) |
| [NCT02910700](https://clinicaltrials.gov/study/NCT02910700) | Fase 2 | Activo, no reclutando | 52 | Triplete trametinib+dabrafenib+nivolumab (TRIDeNT) en melanoma metastásico BRAF-mutado (Grado B) |
| [NCT02039947](https://clinicaltrials.gov/study/NCT02039947) | Fase 2 | Completado | 127 | Dabrafenib+trametinib en melanoma BRAF-mutado con metástasis cerebrales |
| [NCT02130466](https://clinicaltrials.gov/study/NCT02130466) | Fase 1/2 | Completado | 184 | Pembrolizumab+dabrafenib+trametinib en melanoma avanzado |
| [NCT01941927](https://clinicaltrials.gov/study/NCT01941927) | Fase 2 | Completado | 20 | Trametinib+GSK2141795 (inhibidor de AKT) en melanoma BRAF wild-type |

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para "melanoma no cutáneo" como categoría específica.

---

## Otros Subtipos de Melanoma Predichos por TxGNN

El modelo generó un clúster adicional de 8 predicciones sobre subtipos histológicos/anatómicos de melanoma, además de una predicción sin relación mecanística plausible. Se resumen a continuación (no se repiten las tablas de ensayos/literatura ya detalladas):

| Subtipo Predicho | Score TxGNN | Nivel de Evidencia | Recomendación | Evidencia Clave |
|---|---|---|---|---|
| Coroideremia | 99.31% | L5 | Hold | Sin relación biológica conocida con la vía MAPK/MEK; probable falso positivo |
| Melanoma nodular maligno | 99.14% | L2 | Research Question | 1 ensayo fase 2 + 8 publicaciones (casos de paniculitis y metástasis cerebral bajo BRAF/MEK) |
| Melanoma de extensión superficial | 99.14% | L2 | Research Question | 1 ensayo fase 2 + 3 publicaciones (casos de metástasis cerebral/coroidea) |
| Melanoma lentiginoso acral | 99.14% | L2 | Research Question | 2 ensayos (1 fase 2 completado, 1 retrospectivo) + revisión; menor prevalencia de mutación BRAF en este subtipo |
| Melanoma epitelioide | 99.28% | L4 | Research Question | 2 reportes de caso (melanoma conjuntival BRAF-mutado) |
| Melanoma de párpado | 99.26% | L4 | Research Question | 2 reportes de caso (melanoma conjuntival/ocular BRAF-mutado) |
| Melanoma amelanótico cutáneo | 99.14% | L4 | Research Question | 1 revisión + 1 caso pediátrico de metástasis a SNC |
| Melanoma de escroto | 99.21% | L5 | Hold | Sin ensayos ni literatura; solo clasificación anatómica sin evidencia |
| Melanoma maligno de células en balón | 99.14% | L5 | Hold | Subtipo extremadamente raro; sin ensayos ni literatura |

---

## Información de Mercado en España

Trametinib no está actualmente comercializado en España según los datos regulatorios consultados (0 autorizaciones registradas). No hay licencias que listar.

---

## Citotoxicidad

**Esta sección aplica porque trametinib es un antineoplásico** (inhibidor de MEK usado en el tratamiento del melanoma, según la evidencia de ensayos clínicos de este paquete).

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de MEK1/2) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Baja a moderada (categoría habitual de los inhibidores de MEK) |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails** (limitada a melanoma BRAF V600E/K+ de origen no cutáneo; el resto de subtipos permanece en Hold / Research Question)

**Justificación:**
- La evidencia para melanoma no cutáneo alcanza nivel L1, con múltiples ensayos fase 3 completados que sustentan el uso de trametinib (solo o combinado con dabrafenib) en melanoma BRAF V600-mutado independientemente del sitio anatómico. El resto de subtipos predichos tiene evidencia insuficiente (L2–L5) y no debe avanzar sin confirmación adicional.

**Para avanzar se necesita:**
- Resolver DG001 (advertencias/contraindicaciones del prospecto AEMPS/TFDA) — actualmente bloqueante para la evaluación de seguridad S1.
- Resolver DG002 (mecanismo de acción formal vía DrugBank).
- Confirmar el estatus mutacional BRAF V600 como criterio de selección antes de extrapolar a subtipos no cutáneos específicos.
- Dado que el fármaco no está comercializado en España, definir la vía regulatoria (autorización AEMPS / uso de medicamento extranjero) antes de cualquier aplicación clínica local.
- Para los subtipos en Research Question (nodular, superficial, acral, epitelioide, párpado, amelanótico), generar series de casos o estudios observacionales dirigidos que confirmen prevalencia de mutación BRAF y respuesta clínica.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

