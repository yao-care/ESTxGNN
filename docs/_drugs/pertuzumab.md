---
layout: default
title: Pertuzumab
parent: 僅模型預測 (L5)
nav_order: 221
evidence_level: L5
indication_count: 10
---

# Pertuzumab
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

# Pertuzumab: De Cáncer de Mama HER2-Positivo al Subtipo "Normal-like" de Carcinoma de Mama

## Resumen en Una Frase

Pertuzumab es un anticuerpo monoclonal ya establecido en el tratamiento del cáncer de mama HER2-positivo (en combinación con trastuzumab, con o sin docetaxel). El modelo TxGNN predice que también podría ser relevante para el subtipo **"normal-like" de carcinoma de mama**, pero esta dirección cuenta actualmente solo con **6 ensayos clínicos indirectos** (ninguno estratificado específicamente por este subtipo molecular) y **0 publicaciones** que la respalden directamente.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de mama HER2-positivo (referencia derivada del contexto clínico del fármaco; no hay registro estructurado de indicación original ni de licencias locales en los datos disponibles) |
| Nueva Indicación Predicha | Subtipo "Normal-like" de Carcinoma de Mama |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L3 |
| Estado de Mercado (local) | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold — Pregunta de Investigación (Research Question) |

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de una ficha estructurada de mecanismo de acción (MOA) procedente de DrugBank (brecha de datos pendiente, DG002). Según la información recogida en el propio análisis de evidencia, pertuzumab actúa bloqueando la dimerización del receptor HER2 con HER3, mecanismo ya validado clínicamente en el tratamiento del cáncer de mama HER2-positivo.

El subtipo "normal-like" es una de las categorías moleculares del sistema PAM50, caracterizada por un perfil de expresión génica similar al del tejido mamario normal y que, por definición, generalmente **no** está impulsado por la sobreexpresión de HER2. Por ello, la relación mecanística entre este subtipo y el bloqueo HER2/HER3 de pertuzumab es, según el propio análisis, **débil**.

Los 6 ensayos clínicos identificados corresponden todos a poblaciones HER2-positivas tratadas con terapia neoadyuvante, sin estratificación específica por el subtipo "normal-like"; se trata por tanto de evidencia indirecta y extrapolada. Al no existir literatura publicada que respalde directamente esta dirección, la clasificación actual es la de una **pregunta de investigación** más que la de un candidato listo para avanzar clínicamente.

---

## Evidencia de Ensayos Clinicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT05582499](https://clinicaltrials.gov/study/NCT05582499) | Fase 2 | Reclutando | 716 | Plataforma de precisión para terapia neoadyuvante en cáncer de mama operable, estratificada por subtipos clínicos/moleculares |
| [NCT06348134](https://clinicaltrials.gov/study/NCT06348134) | Fase 2 | Reclutando | 74 | Eficacia y seguridad de terapia anti-HER2 neo/adyuvante óptima en mujeres nigerianas con cáncer de mama HER2+ |
| [NCT01796197](https://clinicaltrials.gov/study/NCT01796197) | Fase 2 | Completado | 23 | Paclitaxel + trastuzumab + pertuzumab como terapia preoperatoria en cáncer de mama inflamatorio HER2+ (población HER2+ localmente avanzada, no estratificada por PAM50) |
| [NCT04329065](https://clinicaltrials.gov/study/NCT04329065) | Fase 2 | Reclutando | 25 | Vacuna WOKVAC combinada con quimioterapia neoadyuvante y terapia anti-HER2 |
| [NCT04750122](https://clinicaltrials.gov/study/NCT04750122) | Fase 1/2 | Reclutando | 46 | Terapia neoadyuvante guiada por cribado de fármacos in vitro en cáncer de mama temprano HER2+ |
| [NCT05900206](https://clinicaltrials.gov/study/NCT05900206) | Fase 2 | Reclutando | 370 | Trastuzumab deruxtecán vs. tratamiento preoperatorio estándar, con biomarcadores predictivos de respuesta, en cáncer de mama HER2+ no metastásico |

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Informacion de Mercado (local)

Pertuzumab actualmente **no está comercializado** en este mercado: no hay autorizaciones ni licencias registradas (0 de 0), por lo que no se dispone de información de producto, forma farmacéutica ni indicación aprobada localmente.

---

## Citotoxicidad

**Esta sección aplica porque pertuzumab es un fármaco antineoplásico** (anticuerpo monoclonal dirigido a HER2, utilizado en el tratamiento oncológico del cáncer de mama).

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (anticuerpo monoclonal anti-HER2, bloqueo de la dimerización HER2/HER3) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Función cardíaca (FEVI) — el riesgo de cardiotoxicidad de los agentes anti-HER2 se menciona explícitamente como objetivo de seguimiento en ensayos combinados (p. ej., NCT03329378); además, hemograma y función hepática/renal según protocolo clínico |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusion y Proximos Pasos

**Decisión: Hold — Pregunta de Investigación (Research Question)**

**Justificación:**
La relación mecanística entre pertuzumab y el subtipo "normal-like" de carcinoma de mama es débil (este subtipo no suele estar impulsado por HER2), y la evidencia clínica disponible es completamente indirecta (ensayos en población HER2+ general, sin estratificación por este subtipo) y sin ningún respaldo en literatura publicada.

**Para avanzar se necesita:**
- Datos de mecanismo de acción (MOA) verificados desde DrugBank (brecha DG002)
- Advertencias, contraindicaciones e interacciones farmacológicas desde el prospecto oficial (brecha DG001, bloqueante para evaluación de seguridad S1)
- Un ensayo o estudio traslacional que estratifique específicamente por el subtipo molecular "normal-like" (PAM50), en lugar de por estatus HER2 general
- Nota: dentro del mismo evidence pack, las indicaciones relacionadas **"progesterone-receptor positive breast cancer"** y **"progesterone-receptor negative breast cancer"** (rangos 2 y 3, mismo score TxGNN) presentan evidencia sustancialmente más sólida (L1, múltiples ensayos Fase 3 completados, recomendación "Proceed with Guardrails") y podrían priorizarse como vía de avance más inmediata para este fármaco
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

