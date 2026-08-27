---
layout: default
title: Fosinopril
parent: 僅模型預測 (L5)
nav_order: 126
evidence_level: L5
indication_count: 5
---

# Fosinopril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Fosinopril: De Hipertensión Arterial a Nefropatía Hipertensiva Maligna

## Resumen en Una Frase

Fosinopril es un inhibidor de la enzima convertidora de angiotensina (IECA), una clase farmacológica cuyo uso establecido es el tratamiento de la hipertensión arterial. El modelo TxGNN predice que podría ser efectivo para la **Nefropatía Hipertensiva Maligna** (malignant hypertensive renal disease), con una puntuación de predicción del **99.87%**, pero actualmente **no hay ningún ensayo clínico ni publicación** que respalde directamente esta indicación específica: la hipótesis se apoya únicamente en la extrapolación del mecanismo farmacológico de la clase IECA.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en las fuentes consultadas (Fosinopril no está comercializado en España, sin autorizaciones registradas). Como referencia de clase, los IECA se indican habitualmente para hipertensión arterial. |
| Nueva Indicación Predicha | Nefropatía Hipertensiva Maligna (malignant hypertensive renal disease) |
| Puntaje de Predicción TxGNN | 99.87% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

No se dispone de datos estructurados sobre el mecanismo de acción de Fosinopril en la ficha del fármaco (campo marcado como no disponible). Sin embargo, la propia justificación mecanística del candidato indica que Fosinopril es un inhibidor de la ECA que actúa suprimiendo el sistema renina-angiotensina-aldosterona (RAAS), reduciendo tanto la presión arterial sistémica como la presión intraglomerular renal.

Esta acción sobre el RAAS tiene una relación teórica directa con la nefropatía hipertensiva maligna, ya que el daño renal en esta condición está mediado precisamente por presiones sistémicas e intraglomerulares elevadas. La reducción farmacológica de estas presiones es un mecanismo de protección renal ya reconocido para la clase IECA en otras nefropatías hipertensivas.

Dicho esto, esta relación es una extrapolación del efecto de clase de los IECA, no una evidencia específica para Fosinopril en esta indicación: no existen ensayos clínicos, estudios preclínicos dirigidos ni literatura que evalúen este fármaco en este contexto concreto. Por ello el nivel de evidencia se mantiene bajo (L4), correspondiente a un razonamiento mecanístico sin respaldo experimental directo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

*Nota: existe una brecha de datos de severidad "Blocking" (DG001) sobre el prospecto/advertencias de la agencia reguladora, lo que impide actualmente completar la evaluación de seguridad inicial (S1) de este candidato.*

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se sustenta únicamente en la extrapolación del mecanismo de clase de los IECA (nivel de evidencia L4), sin ningún ensayo clínico ni publicación específica sobre Fosinopril en nefropatía hipertensiva maligna. Además, el fármaco no está comercializado en España y existe una brecha de datos de seguridad de severidad bloqueante que impide completar la evaluación inicial de seguridad.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha técnica oficial (advertencias y contraindicaciones) para completar la evaluación de seguridad S1
- Confirmar el mecanismo de acción (MOA) mediante DrugBank u otra fuente estructurada
- Buscar o generar evidencia preclínica dirigida (modelos animales de nefropatía hipertensiva maligna) antes de considerar estudios clínicos
- Evaluar la viabilidad regulatoria dado que el fármaco actualmente no tiene autorizaciones en España
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

