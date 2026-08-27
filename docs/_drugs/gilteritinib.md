---
layout: default
title: Gilteritinib
parent: 僅模型預測 (L5)
nav_order: 134
evidence_level: L5
indication_count: 1
---

# Gilteritinib
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

# Gilteritinib: De Leucemia Mieloide Aguda a Poliomielitis Bulbar

## Resumen en Una Frase

Gilteritinib es un inhibidor de las tirosina quinasas FLT3 (incluyendo mutaciones ITD/TKD) y AXL, utilizado originalmente en el tratamiento de la leucemia mieloide aguda (LMA) recidivante o refractaria con mutación FLT3. El modelo TxGNN predice una posible asociación con la **Poliomielitis Bulbar**, con un puntaje de **99.10%**, pero actualmente **no existe ningún ensayo clínico ni publicación** que respalde esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Leucemia mieloide aguda (LMA) recidivante/refractaria con mutación FLT3 |
| Nueva Indicación Predicha | Poliomielitis Bulbar |
| Puntaje de Predicción TxGNN | 99.10% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Gilteritinib actúa inhibiendo las tirosina quinasas FLT3 (incluidas las formas mutadas ITD/TKD) y AXL, un mecanismo dirigido y validado en el contexto de la leucemia mieloide aguda con mutación FLT3.

La Poliomielitis Bulbar es una enfermedad neurodegenerativa de origen viral, causada por la infección del poliovirus en las neuronas motoras del tronco encefálico, cuyo mecanismo patológico central es la replicación viral, la lisis neuronal y la inflamación local. No existe una relación mecanística conocida ni directa entre la vía de señalización FLT3/AXL y la fisiopatología de esta enfermedad.

El puntaje elevado del modelo TxGNN (99.10%) refleja únicamente una **similitud topológica** dentro del grafo de conocimiento (posiblemente a través de nodos intermedios relacionados con "inhibidores de quinasa" y procesos neuroinflamatorios), y no constituye evidencia a nivel mecanístico. Además, el propio expediente presenta vacíos de datos relevantes (mecanismo de acción detallado marcado como pendiente, ausencia de advertencias de ficha técnica), lo que reduce aún más la confiabilidad de esta señal en su estado actual.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa FLT3/AXL) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Ítems de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La señal se sustenta únicamente en una puntuación de similitud del modelo TxGNN (nivel de evidencia L5), sin ningún ensayo clínico, publicación científica ni vínculo mecanístico plausible entre el fármaco y la nueva indicación. Adicionalmente, el propio expediente del fármaco presenta vacíos de datos críticos (mecanismo de acción y advertencias de seguridad), lo que impide avanzar a una etapa de evaluación de seguridad (S1).

**Para avanzar se necesita:**
- Datos confirmados del mecanismo de acción (MOA) vía DrugBank
- Advertencias y contraindicaciones del prospecto (TFDA/AEMPS) — actualmente bloqueante
- Búsqueda ampliada de literatura y ensayos clínicos que puedan validar o refutar la señal
- Revisión experta de la plausibilidad mecanística entre la inhibición de FLT3/AXL y la poliomielitis bulbar antes de continuar la evaluación
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

