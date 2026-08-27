---
layout: default
title: Selpercatinib
parent: 僅模型預測 (L5)
nav_order: 255
evidence_level: L5
indication_count: 3
---

# Selpercatinib
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

# Selpercatinib: De Tumores RET-Positivos a Hipertensión Pulmonar

## Resumen en Una Frase

Selpercatinib es un inhibidor selectivo de la quinasa RET; según la nota mecanística del candidato, su uso conocido se limita a tumores sólidos con fusión/mutación de RET (CPNM, carcinoma medular de tiroides) — esta indicación original no consta como registro formal en esta Evidence Pack. El modelo TxGNN predice que podría ser efectivo para **hipertensión pulmonar**, con **0 ensayos clínicos** y **3 publicaciones** (ninguna centrada directamente en esta indicación) respaldando actualmente esta dirección. La propia nota de racionalidad advierte que esta predicción podría ser un **falso positivo** por confusión terminológica.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en registro formal (`original_indications` vacío); contexto mencionado en la nota mecanística: tumores RET fusión/mutación positivos (CPNM, carcinoma medular de tiroides) |
| Nueva Indicación Predicha | Hipertensión pulmonar |
| Puntaje de Predicción TxGNN | 99.18% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Taiwán | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

El campo formal de mecanismo de acción (MOA) no está disponible en esta Evidence Pack. Según la nota mecanística incluida en el análisis del candidato, selpercatinib es un inhibidor de la quinasa RET altamente selectivo, sin registro de comercialización en Taiwán, usado en otros mercados para tumores sólidos con fusión/mutación de RET.

La vía de señalización RET/GDNF tiene un papel teórico en la proliferación del músculo liso vascular, lo que ha motivado la exploración de inhibidores multi-diana de tirosina quinasa (p. ej. imatinib) en hipertensión arterial pulmonar. Sin embargo, la selectividad de selpercatinib por RET —a diferencia de esos fármacos multi-diana— hace que carezca de la actividad sobre remodelado vascular en la que se apoya esa hipótesis.

La propia nota de racionalidad señala una alerta relevante: la reacción adversa conocida de selpercatinib es **hipertensión sistémica**, una entidad clínica distinta de la **hipertensión pulmonar**, y sugiere que la puntuación alta de TxGNN podría reflejar una confusión de vía/terminología entre ambos conceptos — es decir, un posible falso positivo del modelo. Esto reduce sustancialmente la confianza mecanística en esta predicción.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

*Nota: las 3 publicaciones recuperadas tienen `relevance: pending` — ninguna aborda directamente selpercatinib en hipertensión pulmonar; se listan como contexto de seguridad/eficacia oncológica del fármaco.*

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39372206](https://pubmed.ncbi.nlm.nih.gov/39372206/) | 2024 | Real-world/Cohorte | Frontiers in Pharmacology | Comparación de eventos adversos entre pralsetinib y selpercatinib mediante datos del FDA FAERS; no aborda hipertensión pulmonar |
| [34178121](https://pubmed.ncbi.nlm.nih.gov/34178121/) | 2021 | Análisis retrospectivo | Ther Adv Med Oncol | Estudio SIREN: eficacia real-world de selpercatinib en CPNM con fusión RET |
| [41918669](https://pubmed.ncbi.nlm.nih.gov/41918669/) | 2026 | Reporte de caso | Cureus | Manejo a largo plazo de carcinoma medular de tiroides metastásico en MEN2B con mutación RET M918T |

---

## Otras Indicaciones Evaluadas (misma Evidence Pack)

| Indicación | Puntaje TxGNN | Nivel de Evidencia | Ensayos / Literatura | Decisión |
|---|---|---|---|---|
| Migraña | 99.17% | L5 | 0 / 0 | Hold |
| Migraña con aura de tronco encefálico | 99.05% | L5 | 0 / 0 | Hold |

Ambas carecen de vínculo mecanístico conocido con la inhibición de RET (la migraña se explica principalmente por la vía CGRP) y no cuentan con ningún ensayo clínico ni publicación de respaldo.

---

## Citotoxicidad

Selpercatinib actúa como terapia dirigida oncológica (inhibidor selectivo de quinasa RET), no como agente citotóxico convencional.

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de quinasa RET selectivo) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Ítems de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. (Advertencias clave, contraindicaciones e interacciones farmacológicas no constan en esta Evidence Pack; la búsqueda de DDI no arrojó resultados.)

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Las tres indicaciones predichas se encuentran en etapa S0 con nivel de evidencia L5 (solo predicción del modelo, sin ensayos clínicos de respaldo). La hipótesis principal (hipertensión pulmonar) tiene además una señal de alerta explícita de posible falso positivo por confusión con el efecto adverso conocido de hipertensión sistémica. Adicionalmente, existe una brecha de datos **Blocking** (DG001: ausencia de advertencias/contraindicaciones del prospecto TFDA), que por sí sola impide avanzar a la evaluación de seguridad S1 independientemente de la fuerza de la hipótesis de eficacia.

**Para avanzar se necesita:**
- Obtener el prospecto TFDA (advertencias y contraindicaciones) — DG001, severidad Blocking
- Obtener datos formales de mecanismo de acción vía API de DrugBank — DG002, severidad High
- Diseño de estudio o revisión mecanística que diferencie explícitamente hipertensión pulmonar de hipertensión sistémica antes de continuar con esta hipótesis
- No se requiere acción adicional sobre las indicaciones de migraña dado la ausencia total de evidencia y vínculo mecanístico
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

