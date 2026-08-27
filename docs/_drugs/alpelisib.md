---
layout: default
title: Alpelisib
parent: 僅模型預測 (L5)
nav_order: 19
evidence_level: L5
indication_count: 1
---

# Alpelisib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Alpelisib: De Indicación Oncológica No Especificada a Hipertensión Pulmonar

## Resumen en Una Frase

El Evidence Pack no registra la indicación original aprobada de Alpelisib (0 autorizaciones en España, mecanismo de acción marcado como Data Gap), aunque la evidencia adjunta sugiere un contexto de uso oncológico (cáncer de mama avanzado/metastásico HR+/HER2-). El modelo TxGNN predice que Alpelisib podría ser efectivo para **Hipertensión Pulmonar**, con una puntuación de **99.03%**, pero la evidencia real disponible (1 ensayo clínico y 2 publicaciones) **no respalda** esta dirección — de hecho, apunta en sentido contrario.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin datos registrados en el Evidence Pack (no hay autorizaciones en España; ver nota abajo) |
| Nueva Indicación Predicha | Hipertensión Pulmonar |
| Puntaje de Predicción TxGNN | 99.03% (rank interno #12,533) |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

> **Nota sobre la indicación original:** el campo `original_indications` está vacío y `original_moa` está marcado como Data Gap (DG002, severidad Alta). El único indicio disponible en el Evidence Pack proviene de un ensayo excluido por irrelevancia (REASSURE, NCT06705504), cuya descripción menciona el uso real-world de Alpelisib en cáncer de mama HR+/HER2- avanzado o metastásico junto con ribociclib. Este dato es contextual, no una indicación aprobada verificada, y no debe tratarse como tal.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de Alpelisib en este Evidence Pack (Data Gap DG002, severidad Alta). Tampoco hay indicaciones aprobadas registradas para España (0 autorizaciones, estado "No comercializado"), por lo que no es posible confirmar con esta fuente cuál es su indicación original documentada en este mercado.

El único indicio contextual disponible proviene de un ensayo (REASSURE, NCT06705504) que describe el uso de Alpelisib en combinación con ribociclib para cáncer de mama HR+/HER2- avanzado o metastásico — aunque este ensayo fue calificado por el propio pipeline como **no relevante** para la indicación predicha (coincidencia solo por nombre de fármaco, sin relación con hipertensión pulmonar).

La justificación mecanística teórica que vincula un inhibidor de PI3Kα con la hipertensión pulmonar (HP) se basa en que la vía PI3Kα/AKT/mTOR participa en la proliferación de células musculares lisas de la arteria pulmonar (PASMC) y en el remodelado vascular, un mecanismo patológico conocido en la HP. Sin embargo, la evidencia real adjunta a esta predicción **no respalda esta dirección**: ambas publicaciones disponibles describen toxicidad pulmonar y cardiaca inducida por Alpelisib/inhibición de PI3Kα (enfermedad pulmonar intersticial, atrofia biventricular con disfunción del ventrículo derecho), no un efecto terapéutico sobre la HP. De hecho, la enfermedad pulmonar intersticial es una causa reconocida de hipertensión pulmonar secundaria, lo que sugiere que la señal observada podría ir en sentido **opuesto** al predicho por TxGNN.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06705504](https://clinicaltrials.gov/study/NCT06705504) | N/A | Completado | 435 | Estudio retrospectivo real-world (REASSURE) sobre Ribociclib o Alpelisib en cáncer de mama HR+/HER2- avanzado/metastásico. **No relacionado con hipertensión pulmonar** — incluido solo por coincidencia de nombre de fármaco; calificado como grado C (dato no válido como evidencia de soporte). |

**No existe actualmente ningún ensayo clínico genuinamente relacionado con Alpelisib para hipertensión pulmonar.**

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | Reporte de Caso | J Oncol Pharm Pract | Describe un caso de enfermedad pulmonar intersticial **inducida por Alpelisib** en una paciente con cáncer de mama avanzado — evidencia de toxicidad pulmonar, no de eficacia terapéutica en HP. |
| [31039672](https://pubmed.ncbi.nlm.nih.gov/31039672/) | 2019 | Preclínico/Mecanístico | J Am Heart Assoc | La inhibición de la vía PI3Kα produce atrofia biventricular y disfunción del ventrículo derecho en modelos animales — señal de toxicidad cardiopulmonar, no de beneficio en HP. |

Ambas publicaciones describen **efectos adversos** asociados a la inhibición de PI3Kα, no evidencia de eficacia para hipertensión pulmonar.

---

## Información de Mercado en España

Alpelisib no cuenta actualmente con ninguna autorización de comercialización registrada en España (0 licencias, estado "No comercializado").

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de PI3Kα) |
| Riesgo de Mielosupresión | Consultar el prospecto (sin datos específicos en este Evidence Pack) |
| Clasificación de Emetogenicidad | Consultar el prospecto (sin datos específicos en este Evidence Pack) |
| Items de Monitoreo | Función pulmonar (riesgo de enfermedad pulmonar intersticial descrito en la literatura), función cardiaca (riesgo de disfunción ventricular descrito en la literatura) |
| Protección en Manejo | Consultar el prospecto y las normativas locales de manejo de terapias dirigidas oncológicas |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> **Aviso importante:** las advertencias/contraindicaciones del prospecto (TFDA/AEMPS) constituyen un Data Gap de severidad **Bloqueante** (DG001) — su ausencia impide actualmente completar la evaluación de seguridad inicial (etapa S1) de este candidato.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- El nivel de evidencia es L4 (solo estudios preclínicos/mecanísticos), sin ningún ensayo clínico genuino ni publicación que respalde eficacia en hipertensión pulmonar.
- La evidencia disponible describe toxicidad pulmonar y cardiaca asociada a Alpelisib, una señal que contradice —en lugar de respaldar— la dirección predicha por TxGNN.
- Faltan datos críticos de seguridad (prospecto TFDA/AEMPS, Data Gap Bloqueante DG001) que impiden avanzar a la etapa de evaluación de seguridad inicial (S1).

**Para avanzar se necesita:**
- Obtener el prospecto oficial (TFDA/AEMPS) con advertencias y contraindicaciones (resolver DG001, Bloqueante)
- Obtener datos del mecanismo de acción (MOA) verificados vía DrugBank (resolver DG002)
- Confirmar la(s) indicación(es) aprobada(s) original(es) de Alpelisib, actualmente no registrada(s) en este Evidence Pack
- Identificar evidencia clínica genuinamente específica para hipertensión pulmonar (actualmente ausente)
- Evaluar y descartar explícitamente el riesgo de que la vía mecanística propuesta sea contraproducente (toxicidad pulmonar/cardiaca) antes de cualquier consideración de reposicionamiento
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

