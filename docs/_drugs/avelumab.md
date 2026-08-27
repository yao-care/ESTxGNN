---
layout: default
title: Avelumab
parent: 僅模型預測 (L5)
nav_order: 31
evidence_level: L5
indication_count: 10
---

# Avelumab
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

# Avelumab: De Carcinoma Urotelial a Tumor Asociado al Herpesvirus Humano 8

## Resumen en Una Frase

Avelumab es un inhibidor de PD-L1 (anti-PD-L1) cuya indicación de referencia dentro de este Evidence Pack es el carcinoma urotelial localmente avanzado o metastásico. El modelo TxGNN predice que podría ser efectivo para **tumores asociados al herpesvirus humano 8 (VHH-8)**, con un score de predicción del **99.97%**, pero actualmente **sin ningún ensayo clínico ni publicación** que respalde esta dirección — la evidencia proviene únicamente de la inferencia del modelo (nivel L5).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Carcinoma urotelial localmente avanzado/metastásico *(no consta en licencias TFDA — mencionado como indicación ya aprobada dentro del análisis de racionalidad mecanística del propio Evidence Pack)* |
| Nueva Indicación Predicha | Tumor asociado al herpesvirus humano 8 (VHH-8) |
| Puntaje de Predicción TxGNN | 99.97% (rank 975) |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Taiwán | No comercializado (未上市) |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos estructurados sobre el mecanismo de acción de avelumab (campo `original_moa` marcado como Data Gap, DG002). Sin embargo, el propio análisis de racionalidad del Evidence Pack identifica a avelumab como un **inhibidor de PD-L1 (anti-PD-L1)**, cuya indicación ya aprobada es el carcinoma urotelial.

La hipótesis para los tumores asociados a VHH-8 (como el sarcoma de Kaposi o el linfoma efusión primario) se basa en que estos tumores suelen presentar sobreexpresión de PD-L1 en el microambiente tumoral, generando evasión inmunitaria; en teoría, un anti-PD-L1 podría restaurar la actividad antitumoral de los linfocitos T.

No obstante, esta relación es puramente de inferencia mecanística: no existe ningún dato de expresión de PD-L1 específico en tumores VHH-8, ni evidencia clínica directa de avelumab en esta población. El propio Evidence Pack califica este vínculo como "推論，無直接臨床資料佐證" (inferencia sin datos clínicos directos que la respalden).

> **Nota:** dentro del mismo lote de 10 predicciones, las de rango 9 y 10 (carcinoma urotelial de uretra prostática y carcinoma urotelial sarcomatoide de pelvis renal) presentan una racionalidad mecanística más sólida, al pertenecer al mismo tejido que la indicación ya aprobada de avelumab (carcinoma urotelial). Estas podrían justificar seguimiento prioritario por separado.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para "tumor asociado al herpesvirus humano 8".

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

---

## Citotoxicidad

Avelumab actúa sobre una diana oncoinmunológica (indicación de referencia: carcinoma urotelial), por lo que se incluye esta sección.

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (inhibidor de punto de control inmunitario anti-PD-L1) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El score de TxGNN es muy alto, pero no existe ninguna evidencia clínica ni de literatura que lo respalde (0 ensayos, 0 publicaciones), y la enfermedad predicha es extremadamente rara sin datos conocidos de expresión de PD-L1. Esta predicción no alcanza el nivel mínimo para avanzar a la evaluación de seguridad S1.

**Para avanzar se necesita:**
- Datos de expresión de PD-L1 en tumores asociados a VHH-8
- Al menos un estudio preclínico o serie de casos que respalde el mecanismo propuesto
- Resolución del Data Gap bloqueante DG001 (仿單警語/禁忌 de TFDA) antes de cualquier evaluación de seguridad S1
- Confirmación del mecanismo de acción detallado de avelumab (DG002)
- Evaluación independiente de las predicciones de rango 9-10 (subtipos de carcinoma urotelial), que muestran mayor plausibilidad mecanística por su relación directa con la indicación ya aprobada
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

