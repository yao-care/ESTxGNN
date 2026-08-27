---
layout: default
title: Guselkumab
parent: 僅模型預測 (L5)
nav_order: 137
evidence_level: L5
indication_count: 10
---

# Guselkumab
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

# Guselkumab: De Psoriasis a Osteoporosis Inducida por Fármacos

## Resumen en Una Frase

Guselkumab es un anticuerpo monoclonal anti-IL-23 (p19), cuya indicación aprobada en otros mercados es la **psoriasis en placas** de moderada a grave. El modelo TxGNN predice que también podría ser efectivo para la **Osteoporosis Inducida por Fármacos**, la indicación con la puntuación de predicción más alta de todo el panel (10 candidatas), pero actualmente **sin ningún ensayo clínico ni publicación** que la respalde.

> Nota: en este mismo panel de predicciones, otras dos indicaciones (psoriasis y colitis ulcerosa) sí cuentan con evidencia clínica sólida — ver "Próximos Pasos".

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Psoriasis en placas (referencia cruzada de este mismo paquete de evidencia; no hay texto de indicación oficial de TFDA/AEMPS porque el fármaco aún no está comercializado en Taiwán) |
| Nueva Indicación Predicha | Osteoporosis Inducida por Fármacos |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L5 |
| Estado de Mercado (Taiwán) | ✗ No comercializado |
| Número de Autorizaciones (Taiwán) | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

No se dispone de un resumen oficial del mecanismo de acción (MOA) para guselkumab en este paquete de evidencia. Sin embargo, según información recogida en otras entradas de este mismo panel de predicciones, guselkumab es un anticuerpo monoclonal humano que inhibe selectivamente la subunidad p19 de la interleucina-23 (IL-23), bloqueando el eje IL-23/Th17. Este mecanismo ya cuenta con validación clínica sólida en otras indicaciones del mismo panel (psoriasis y colitis ulcerosa, ambas con evidencia de Nivel L1).

Para la indicación de mayor puntuación evaluada en este informe — Osteoporosis Inducida por Fármacos —, la propia evaluación del modelo señala que **no existe una hipótesis clínica directa** que vincule el eje IL-23/Th17 con el eje RANKL de remodelación ósea, y que esta predicción carece por completo de respaldo en ensayos clínicos o literatura publicada. Es decir, la puntuación alta de TxGNN refleja una señal de similitud dentro de la red de conocimiento del modelo, pero no una relación mecanística validada hasta la fecha.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Taiwán

Guselkumab actualmente **no está comercializado en Taiwán** (0 autorizaciones registradas en TFDA), por lo que no hay licencias ni formas farmacéuticas que mostrar.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación con mayor puntuación TxGNN (Osteoporosis Inducida por Fármacos) no cuenta con ningún ensayo clínico ni literatura de respaldo, y ni siquiera existe una hipótesis mecanística directa entre el eje IL-23/Th17 y esta condición. Además, faltan datos de seguridad bloqueantes (advertencias TFDA) que impiden completar la evaluación inicial de seguridad (S1).

**Para avanzar se necesita:**
- Obtener el prospecto/etiquetado oficial de TFDA (advertencias y contraindicaciones) — brecha bloqueante identificada en este paquete de evidencia
- Datos detallados del mecanismo de acción (MOA) de guselkumab
- Estudios preclínicos o de mecanismo que vinculen el eje IL-23/Th17 con la osteoporosis inducida por fármacos, antes de justificar cualquier inversión adicional en esta indicación específica
- Confirmar estado de comercialización de guselkumab en Taiwán (actualmente 0 autorizaciones)
- **Recomendación adicional:** dado que este mismo panel contiene dos indicaciones con evidencia de Nivel L1 y recomendación "Proceed with Guardrails" (psoriasis, ya aprobada como Tremfya en otros mercados, y colitis ulcerosa, con el ensayo Fase 3 QUASAR), se sugiere priorizar la evaluación de esas indicaciones por separado en lugar de la osteoporosis inducida por fármacos
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

