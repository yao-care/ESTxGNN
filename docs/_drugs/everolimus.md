---
layout: default
title: Everolimus
parent: 僅模型預測 (L5)
nav_order: 115
evidence_level: L5
indication_count: 10
---

# Everolimus
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

Using el prompt de informe de reposicionamiento (no requiere skill adicional — es una tarea de generación de documento estructurado a partir de datos ya proporcionados).

Notas sobre el manejo de datos antes del informe: `original_indications` y `taiwan_regulatory.licenses` vienen vacíos y `original_moa` es un vacío de datos explícito, así que no invento la indicación original ni el MOA — uso únicamente lo que aparece en el Evidence Pack (incluyendo el hecho, mencionado en el propio JSON, de que Everolimus es citado como "inhibidor de mTOR" en la justificación mecanística de otras indicaciones predichas). El campo `scoring` de la indicación #1 (liposarcoma) viene `"pending"`, así que determino el nivel de evidencia yo mismo según las reglas del prompt.

---

# Everolimus: Potencial Reposicionamiento hacia Liposarcoma

## Resumen en Una Frase

No se dispone en este informe de datos sobre la indicación original aprobada de Everolimus (el fármaco figura como no comercializado, con 0 autorizaciones registradas, y el mecanismo de acción es un vacío de datos pendiente). El modelo TxGNN predice que Everolimus podría ser efectivo para **Liposarcoma**, con **1 ensayo clínico** y **5 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Liposarcoma |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L2 (ver justificación abajo) |
| Estado de Mercado | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

*(La fila "Indicación Original" se omite: no hay ningún `approved_indication_text` ni `original_indications` disponible en los datos de entrada.)*

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de Everolimus en el campo dedicado (`original_moa`). Sin embargo, el propio Evidence Pack identifica a Everolimus como un **inhibidor de mTOR** en varias justificaciones mecanísticas de otras indicaciones predichas para este fármaco (p. ej., "mTOR 抑制劑 everolimus 具明確機轉基礎" en la indicación de rabdomiosarcoma), lo cual es consistente con la literatura recogida para liposarcoma.

En concreto, la publicación PMID 26518767 documenta activación de las vías **Akt-mTOR y MAPK** en liposarcoma desdiferenciado (99 muestras analizadas), con efecto antitumoral demostrado de un inhibidor de mTOR in vitro. Esto proporciona un fundamento mecanístico directo: si la vía mTOR está activada en este subtipo tumoral, un inhibidor de mTOR como Everolimus tiene una base biológica razonable para ser evaluado.

El ensayo clínico más relevante (NCT03114527 / publicación PMID 37967116) combina Everolimus con ribociclib (inhibidor de CDK4/6), explotando precisamente esta doble vulnerabilidad — CDK4 en liposarcoma desdiferenciado y mTOR en leiomiosarcoma — lo que refuerza la coherencia mecanística de incluir Everolimus en esta indicación.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Fase 2 | Activo, no reclutando | 48 | Estudio de combinación Ribociclib (inhibidor CDK4/6) + Everolimus (inhibidor mTOR) en liposarcoma desdiferenciado (DDL) y leiomiosarcoma (LMS) avanzados con progresión tras ≥1 línea previa; evalúa la actividad antitumoral de la combinación por cohortes histológicas. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Ensayo clínico Fase II (publicación de resultados) | Clinical Cancer Research | Reporta el ensayo SAR-096 (mismo NCT03114527); ribociclib + everolimus muestran inhibición sinérgica del crecimiento en múltiples modelos tumorales, fundamento biológico de la combinación en DDL/LMS. |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Revisión | Frontiers in Oncology | Revisión de modelos PDOX de sarcoma que identifican combinaciones eficaces con el inhibidor de CDK palbociclib, como estrategia traducible a la clínica. |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Estudio mecanístico | Tumour Biology | Activación de las vías Akt-mTOR y MAPK en 99 muestras de liposarcoma desdiferenciado; efecto antitumoral de un inhibidor de mTOR demostrado in vitro. |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Estudio preclínico | Anticancer Research | Evalúa eribulina (ya usada en liposarcoma) en combinación con agentes de mecanismo diferente, explorando actividad antitumoral de amplio espectro. |
| [41991999](https://pubmed.ncbi.nlm.nih.gov/41991999/) | 2026 | Estudio preclínico/mecanístico | Oncogene | El inhibidor de XPO1 selinexor altera la maquinaria transcripcional central del liposarcoma desdiferenciado (DDLPS), identificando nuevas vulnerabilidades terapéuticas. |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de mTOR) — según se identifica en la evidencia recopilada para este fármaco |
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
Existe evidencia clínica moderada para liposarcoma (un ensayo Fase 2 activo con publicación de resultados y fundamento mecanístico coherente), pero la brecha de datos bloqueante sobre el prospecto TFDA impide iniciar la evaluación de seguridad S1, y no hay ningún dato de advertencias, contraindicaciones o interacciones disponible.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha técnica oficial para completar advertencias y contraindicaciones (resuelve DG001, bloqueante)
- Obtener datos de mecanismo de acción vía DrugBank API (DG002)
- Confirmar el estado real de finalización y resultados definitivos del ensayo NCT03114527
- Obtener datos de interacciones farmacológicas (DDI) mediante una fuente alternativa, dado que la consulta actual no arrojó resultados
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

