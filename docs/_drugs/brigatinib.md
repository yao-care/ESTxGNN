---
layout: default
title: Brigatinib
parent: 僅模型預測 (L5)
nav_order: 44
evidence_level: L5
indication_count: 10
---

# Brigatinib
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

# Brigatinib: De Cáncer de Pulmón No Microcítico ALK-Positivo a Fibromatosis Gingival

## Resumen en Una Frase

Brigatinib es un inhibidor de tirosina quinasa ALK/ROS1, cuyo uso conocido en cáncer de pulmón no microcítico (NSCLC) ALK-positivo se confirma únicamente a través de la literatura incluida en este paquete de evidencia (no hay ficha de indicación original ni MOA en las fuentes regulatorias consultadas). El modelo TxGNN predice que podría ser efectivo para **Fibromatosis Gingival**, pero actualmente **no existe ningún ensayo clínico ni publicación** que respalde esta dirección — se trata exclusivamente de una puntuación del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de pulmón no microcítico (NSCLC) ALK-positivo *(inferido de la evidencia bibliográfica del paquete; no confirmado por ficha TFDA/DrugBank — ver brecha DG002)* |
| Nueva Indicación Predicha | Fibromatosis Gingival |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en las fuentes consultadas (DrugBank, TFDA). Según la literatura incluida en este paquete, brigatinib es un inhibidor de ALK/ROS1 de segunda generación cuya eficacia está bien establecida en NSCLC ALK-positivo (ensayos ALTA-1L, ALTA-3, entre otros).

Para la indicación de mayor puntaje del modelo, **fibromatosis gingival**, no existe ninguna relación mecanística conocida entre la vía ALK y esta condición periodontal benigna, y no se recuperó ningún ensayo clínico ni artículo que la vincule con brigatinib. El propio análisis de razonamiento del paquete concluye que no es posible evaluar esta hipótesis con la evidencia disponible.

**Nota de contexto:** este paquete evaluó 10 indicaciones predichas por TxGNN para brigatinib; todas recibieron nivel de evidencia L4-L5 y recomendación "Hold". Las dos con mayor cantidad de literatura (rango 5, "lung benign neoplasm", y rango 8, "lung germ cell tumor") muestran 20 y 5 publicaciones respectivamente, pero el propio análisis las señala como probables desajustes de palabra clave del modelo (confusión benigno/maligno o superposición del término "lung", sin evidencia directa sobre la indicación predicha).

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Brigatinib no está comercializado en España y no cuenta con autorizaciones registradas en las fuentes consultadas (0 licencias).

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa ALK/ROS1), según la literatura incluida en el paquete |
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
La indicación predicha con mayor puntaje (fibromatosis gingival) carece por completo de evidencia clínica, bibliográfica y de plausibilidad mecanística. Además, faltan datos regulatorios básicos (ficha técnica TFDA, MOA de DrugBank) que impiden siquiera iniciar la evaluación de seguridad (brecha bloqueante DG001), y el fármaco no está comercializado en España.

**Para avanzar se necesita:**
- Ficha técnica/prospecto de TFDA (advertencias, contraindicaciones) — brecha bloqueante DG001
- Mecanismo de acción confirmado vía DrugBank — brecha DG002
- Si se desea explorar otras indicaciones del mismo lote (p. ej. rango 5 u 8), una revisión manual que confirme si la superposición terminológica con "lung"/ALK refleja una hipótesis real o un artefacto del modelo, antes de asignar recursos de evaluación
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

