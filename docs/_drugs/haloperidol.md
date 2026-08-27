---
layout: default
title: Haloperidol
parent: 僅模型預測 (L5)
nav_order: 138
evidence_level: L5
indication_count: 10
---

# Haloperidol
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

# Haloperidol: De Esquizofrenia/Psicosis a Trastorno Bipolar (Episodio Maníaco)

## Resumen en Una Frase

Haloperidol es un antipsicótico típico (butirofenona), utilizado originalmente para la esquizofrenia y otros trastornos psicóticos.
El modelo TxGNN predice que también podría ser efectivo para el **Trastorno Bipolar Afectivo — episodio maníaco**,
con **9 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.

> Nota: TxGNN generó otras 9 indicaciones candidatas con score similar (>99.8%), pero ninguna cuenta con ensayos clínicos ni literatura de respaldo tras la búsqueda estructurada; todas permanecen en **Hold (S0)** por falta de evidencia. Este informe se centra en la única indicación con evidencia real: manía bipolar.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Esquizofrenia y otros trastornos psicóticos (antipsicótico típico; indicación específica autorizada y ficha técnica aún pendientes de verificación) |
| Nueva Indicación Predicha | Trastorno Bipolar Afectivo — episodio maníaco |
| Puntaje de Predicción TxGNN | 99.83% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

## Por qué es Razonable esta Predicción?

Haloperidol es un antipsicótico típico de primera generación, antagonista potente del receptor de dopamina D2. Los episodios maníacos del trastorno bipolar se asocian con hiperactividad dopaminérgica en la vía mesolímbica; el bloqueo D2 puede reducir directamente la agitación, el trastorno del pensamiento y los síntomas psicóticos que acompañan a la manía aguda. Esta relación mecanística es de consenso clásico en psicofarmacología, no una simple asociación estadística del modelo.

La cercanía entre la indicación original (trastornos psicóticos) y la nueva indicación predicha (manía bipolar) es consistente: ambas comparten la fisiopatología de hiperdopaminergia central, y haloperidol se ha utilizado históricamente como comparador activo de referencia en múltiples ensayos de Fase 3 frente a antipsicóticos de segunda generación (risperidona, olanzapina) en el tratamiento de la manía aguda, lo que refuerza que la predicción del modelo coincide con práctica clínica y evidencia ya existente.

Actualmente los datos estructurados de MOA (DrugBank) y la ficha técnica de TFDA/AEMPS están pendientes de verificación (ver brechas de datos abajo), por lo que la clasificación farmacológica aquí descrita se basa en el consenso de la literatura recuperada, no en una ficha técnica oficial confirmada.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00253149](https://clinicaltrials.gov/study/NCT00253149) | Fase 3 | Completado | 158 | Risperidona vs. placebo vs. haloperidol como terapia adyuvante a estabilizadores del ánimo en manía bipolar; haloperidol como brazo activo comparador directo |
| [NCT00253162](https://clinicaltrials.gov/study/NCT00253162) | Fase 3 | Completado | 439 | Risperidona en dosis flexible vs. placebo o haloperidol en episodios maníacos del trastorno bipolar I; haloperidol como comparador activo a 12 semanas |
| [NCT00129220](https://clinicaltrials.gov/study/NCT00129220) | Fase 3 | Completado | 224 | Olanzapina controlada con placebo y haloperidol en episodio maníaco o mixto del trastorno bipolar I; confirma a haloperidol como referencia de eficacia |
| [NCT00097266](https://clinicaltrials.gov/study/NCT00097266) | Fase 3 | Completado | 615 | Monoterapia con aripiprazol en manía aguda; rol de haloperidol como comparador no confirmado (relevancia B) |
| [NCT00126009](https://clinicaltrials.gov/study/NCT00126009) | Fase 2 | Completado | 120 | Valproato+amisulprida vs. valproato+haloperidol en manía bipolar I según DSM-IV-TR |
| [NCT00767715](https://clinicaltrials.gov/study/NCT00767715) | Fase 4 | Terminado | 11 | Olanzapina vs. antipsicóticos convencionales (incl. haloperidol) en manía aguda, Suecia; terminado prematuramente, muestra muy pequeña |
| [NCT04327843](https://clinicaltrials.gov/study/NCT04327843) | Fase 3 | Completado | 22 | Reducción de la carga de trastornos psicóticos crónicos en Tanzania; rol específico de haloperidol no detallado |
| [NCT06049953](https://clinicaltrials.gov/study/NCT06049953) | N/A | Reclutando | 200 | Estudio observacional de efectos del desarrollo tras exposición prenatal a antipsicóticos; no es evidencia directa de eficacia |
| [NCT03541031](https://clinicaltrials.gov/study/NCT03541031) | N/A | Desconocido | 120 | Micronutrientes como terapia adyuvante en trastorno bipolar; sin relación directa con haloperidol |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34642461](https://pubmed.ncbi.nlm.nih.gov/34642461/) | 2022 | Revisión/Metanálisis en red | Molecular Psychiatry | Metanálisis en red de ECAs doble ciego sobre tratamientos farmacológicos de la manía bipolar aguda, incluyendo haloperidol |
| [22134043](https://pubmed.ncbi.nlm.nih.gov/22134043/) | 2012 | ECA | Journal of Affective Disorders | Ensayo aleatorizado, doble ciego, controlado con placebo y haloperidol, en pacientes japoneses con episodio maníaco/mixto de trastorno bipolar I |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Revisión | Acta Psychiatrica Scandinavica | Revisión de opciones de tratamiento basadas en evidencia para la manía bipolar, con recomendaciones clínicas sobre elección de antipsicóticos |
| [36789916](https://pubmed.ncbi.nlm.nih.gov/36789916/) | 2023 | Revisión | BMJ Mental Health | Comparación de dosis equivalentes de antipsicóticos entre manía aguda y esquizofrenia |
| [10343182](https://pubmed.ncbi.nlm.nih.gov/10343182/) | 1999 | Estudio clínico | Neuropsychobiology | Efectos diferenciales del litio y haloperidol sobre proteínas Gαs en leucocitos mononucleares de pacientes con trastorno bipolar |
| [22070611](https://pubmed.ncbi.nlm.nih.gov/22070611/) | 2012 | Revisión | CNS Neuroscience & Therapeutics | Refractariedad en trastorno bipolar; sugiere añadir haloperidol u otros antipsicóticos en pacientes maníacos con respuesta parcial |
| [27151529](https://pubmed.ncbi.nlm.nih.gov/27151529/) | 2016 | Revisión sistemática/Metanálisis | Human Psychopharmacology | Tratamiento farmacológico de la agitación aguda asociada a trastornos psicóticos y bipolares |
| [18344731](https://pubmed.ncbi.nlm.nih.gov/18344731/) | 2008 | Revisión sistemática | Journal of Clinical Psychopharmacology | Efectos extrapiramidales inducidos por antipsicóticos en trastorno bipolar y esquizofrenia |
| [369472](https://pubmed.ncbi.nlm.nih.gov/369472/) | 1979 | ECA | Archives of General Psychiatry | Estudio controlado doble ciego de litio + haloperidol vs. placebo + haloperidol en trastorno esquizoafectivo excitado |
| [3312180](https://pubmed.ncbi.nlm.nih.gov/3312180/) | 1987 | Estudio controlado | Journal of Clinical Psychiatry | Comparación de clonazepam con litio y haloperidol en el tratamiento de manía aguda |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Múltiples ensayos de Fase 2/3 completados (varios con haloperidol como comparador activo directo) y una revisión sistemática en red de nivel 1 respaldan la eficacia de haloperidol en la manía aguda del trastorno bipolar. El nivel de evidencia L1 es sólido, pero persisten brechas críticas de seguridad (ficha técnica/DDI) que impiden avanzar sin restricciones.

**Para avanzar se necesita:**
- Ficha técnica/prospecto de TFDA con advertencias y contraindicaciones (DG001, bloqueante para evaluación S1)
- Datos estructurados de mecanismo de acción vía DrugBank (DG002)
- Confirmación del estatus regulatorio y autorizaciones de comercialización en España (actualmente sin registro)
- Aclaración del rol específico de haloperidol en los ensayos con relevancia B/C (títulos truncados, comparador no confirmado)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

