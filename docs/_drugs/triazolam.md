---
layout: default
title: Triazolam
parent: Solo predicción del modelo (L5)
nav_order: 545
evidence_level: L5
indication_count: 1
---

# Triazolam
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Triazolam: De Indicación Original No Registrada a Trastorno del Sueño (Inicio y Mantenimiento)

## Resumen en Una Frase

Triazolam es una benzodiazepina hipnótica de acción corta. En los datos disponibles no consta una indicación original registrada, pero está comercializado en España como Halcion 0,125 mg comprimidos.
El modelo TxGNN predice que podría ser efectivo para **trastornos del sueño (inicio y mantenimiento del sueño)**, con **0 ensayos clínicos** y **20 publicaciones** que respaldan esta dirección. Se trata sobre todo de revisiones, guías y metaanálisis.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (el texto de indicación de la autorización está vacío) |
| Nueva Indicación Predicha | Trastorno del sueño (inicio y mantenimiento del sueño) |
| Puntaje de Predicción TxGNN | 99,72% |
| Nivel de Evidencia | L3 (revisiones sistemáticas y guías, mayormente a nivel de clase terapéutica; sin ensayos clínicos registrados) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Triazolam es una benzodiazepina hipnótica de acción corta. Actúa como modulador alostérico positivo de los receptores GABA-A, con lo que refuerza la neurotransmisión inhibitoria y favorece el inicio del sueño. Los datos de DrugBank no incluyen el mecanismo de acción detallado. Esta descripción proviene de la farmacología conocida de la clase.

La predicción del modelo (99,72%) es coherente con esta farmacología. El insomnio es el uso establecido de este tipo de fármacos, y la literatura recuperada lo confirma: revisiones históricas sobre hipnóticos de acción corta, una guía de la AASM y varios metaanálisis.

Por eso esta predicción parece más un **artefacto de integridad de datos** (indicaciones originales vacías y MOA sin completar) que un reposicionamiento genuino. Antes de cualquier acción conviene confirmar la indicación en la ficha técnica de la AEMPS y completar los datos de DrugBank.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27998379](https://pubmed.ncbi.nlm.nih.gov/27998379/) | 2017 | Guía de práctica clínica | J Clin Sleep Med | Guía de la AASM sobre tratamiento farmacológico del insomnio crónico en adultos. Evalúa fármacos individuales, incluidos los aprobados por la FDA para esta indicación |
| [33249496](https://pubmed.ncbi.nlm.nih.gov/33249496/) | 2021 | Revisión sistemática y metaanálisis en red | Sleep | Compara la eficacia y seguridad de hipnóticos para el insomnio en adultos mayores |
| [40110890](https://pubmed.ncbi.nlm.nih.gov/40110890/) | 2025 | Revisión sistemática y metaanálisis de ECA | Psychiatry Clin Neurosci | Evalúa la combinación de antidepresivos con hipnóticos, por clase (incluidas benzodiazepinas), en depresión mayor con insomnio |
| [30058034](https://pubmed.ncbi.nlm.nih.gov/30058034/) | 2018 | Revisión | Drugs & Aging | Recomendaciones de manejo farmacológico del insomnio en ancianos. Las terapias conductuales se consideran la intervención inicial |
| [27751669](https://pubmed.ncbi.nlm.nih.gov/27751669/) | 2016 | Revisión | Clin Ther | Seguridad y eficacia de los medicamentos para dormir en adultos mayores |
| [39932761](https://pubmed.ncbi.nlm.nih.gov/39932761/) | 2025 | Revisión | Minerva Med | Panorama actual del trastorno de insomnio: definición, epidemiología y riesgos asociados |
| [2567741](https://pubmed.ncbi.nlm.nih.gov/2567741/) | 1989 | Revisión crítica | J Clin Psychopharmacol | Analiza el insomnio de rebote tras suspender hipnóticos de vida media corta. Es una posibilidad real tras suspender triazolam |
| [19682231](https://pubmed.ncbi.nlm.nih.gov/19682231/) | 2010 | Estudio experimental en humanos | J Sleep Res | Compara triazolam y zolpidem en el aprendizaje motor dependiente del sueño. Aporta evidencia indirecta sobre cognición y seguridad |
| [9161660](https://pubmed.ncbi.nlm.nih.gov/9161660/) | 1997 | Revisión comparativa | Ann Pharmacother | Compara zolpidem con triazolam en eficacia y seguridad en humanos |
| [8573298](https://pubmed.ncbi.nlm.nih.gov/8573298/) | 1995 | Revisión | Drug Safety | Evaluación de los hipnóticos de acción corta |

Las publicaciones restantes son revisiones históricas y boletines terapéuticos con menor relevancia directa.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 58118 | HALCION 0,125 mg COMPRIMIDOS (Pfizer S.L.) | Comprimido | No especificada en los datos disponibles |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como cautelas generales tomadas de la literatura, los títulos y resúmenes recuperados apuntan a estas preocupaciones habituales de los hipnóticos benzodiazepínicos:
- Uso en adultos mayores.
- Efectos cognitivos y de memoria (véase PMID 19682231).
- Insomnio de rebote al suspender el tratamiento (véase PMID 2567741).
- Uso limitado a corto plazo.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El insomnio es coherente con la farmacología conocida de triazolam y con una literatura amplia sobre hipnóticos. Sin embargo, no hay ensayos clínicos registrados y la evidencia es mayormente a nivel de clase. Además, faltan la indicación original y los datos de seguridad de la ficha técnica, por lo que no es posible avanzar sin salvaguardas.

**Para avanzar se necesita:**
- Confirmar la indicación aprobada en la ficha técnica de la AEMPS (descargar y analizar el prospecto en PDF).
- Completar el mecanismo de acción y las indicaciones originales en DrugBank.
- Obtener advertencias y contraindicaciones del prospecto para el cribado de seguridad.
- Establecer restricciones de uso en adultos mayores, con duración limitada del tratamiento y plan de retirada gradual.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

