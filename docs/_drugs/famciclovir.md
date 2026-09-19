---
layout: default
title: Famciclovir
parent: Evidencia alta (L1-L2)
nav_order: 117
evidence_level: L2
indication_count: 9
---

# Famciclovir
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **9** 
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

# Famciclovir: Del Herpes Zóster (Herpes Zoster) a la Varicela (Chickenpox)

## Resumen de una frase

Famciclovir es un profármaco de penciclovir, y los datos bibliográficos muestran que está establecido para el tratamiento antiviral sistémico del herpes zóster (Herpes Zoster) e herpes genital (Genital Herpes). El modelo TxGNN predice que también podría ser efectivo para **varicela (Chickenpox)**, actualmente apoyado por **5 ensayos clínicos** (de los cuales 2 son ensayos de Fase 3 completados, incluyendo 1 que prueba directamente la eficacia comparativa de famciclovir) y **20 artículos bibliográficos**, alcanzando un nivel de evidencia L2, siendo la candidata con la evidencia más sólida en este grupo de evaluación.

> **Explicación de selección de candidatos**: Este Evidence Pack predice 9 indicaciones, siendo la puntuación TxGNN más alta para post-infectious neuralgia (rank 1), pero su evidencia consiste solo en 2 ensayos sin relación directa con famciclovir (los fármacos de intervención fueron oxicodona y bloqueo nervioso respectivamente, calificación de relevancia C), y la exposición del mecanismo aclara "este conjunto de datos no proporciona ensayos que prueben directamente famciclovir para PHN". En comparación, varicela (rank 7), aunque con una puntuación TxGNN ligeramente menor, es la única candidata con ensayos de comparación directa con famciclovir (calificación A) y el apoyo bibliográfico más extenso, por lo que este informe la toma como el objetivo principal de evaluación. La evidencia para las otras 8 candidatas se resume en una tabla adjunta al final.

## Resumen rápido

| Elemento | Contenido |
|----------|-----------|
| Indicación original | Herpes zóster (Herpes Zoster) / Herpes genital (Genital Herpes) — según literatura PMID 16595111, 9675639 |
| Nueva indicación predicha | Varicela (Chickenpox) |
| Puntuación de predicción TxGNN | 99.11% (rank 11741) |
| Nivel de evidencia | L2 |
| Estado del mercado | Not marketed |
| Número de licencias aprobadas | 0 |
| Recomendación de decisión | Proceed with Guardrails |

## ¿Por qué esta predicción es razonable?

La base de datos actual no proporciona una descripción completa del mecanismo de acción de famciclovir ([Data Gap], ver DG002). Pero basándose en información ya conocida de la literatura del grupo de evaluación (PMID 19273678, 9675639): famciclovir es un profármaco de penciclovir que, tras fosforilación, inhibe la DNA polimerasa del virus varicela-zóster (VZV), bloqueando la replicación viral. Este mecanismo ha obtenido eficacia terapéutica confirmada en el tratamiento del herpes zóster (reactivación de VZV) e herpes genital (HSV).

La varicela y el herpes zóster son diferentes manifestaciones clínicas del mismo agente patógeno (VZV) — la varicela es la infección primaria, el herpes zóster es la reactivación del virus latente. Como el agente patógeno es exactamente el mismo y el blanco del fármaco (DNA polimerasa de VZV) no cambia, la transferibilidad del mecanismo es directa e inequívoca. Actualmente, las licencias farmacéuticas y el uso clínico se concentran en indicaciones de herpes zóster / PHN, mientras que la varicela (especialmente en la población pediátrica) representa una extensión de etiqueta con el mismo agente patógeno, lo que también se refleja en la discusión de la literatura como PMID 10375341 sobre tratamiento de infecciones por VZV en niños.

## Evidencia de ensayos clínicos

| Número de ensayo | Fase | Estado | Número de participantes | Hallazgos principales |
|------------------|------|--------|----------------------|----------------------|
| [NCT01327144](https://clinicaltrials.gov/study/NCT01327144) | Phase 3 | Completado | 177 | Ensayo de comparación directa de Famciclovir 500mg versus Aciclovir 400mg para herpes zóster (relevancia A: prueba directa de famciclovir) |
| [NCT00098046](https://clinicaltrials.gov/study/NCT00098046) | Phase 3 | Completado | 76 | Ensayo de farmacocinética y seguridad de formulación oral pediátrica de Famciclovir en niños de 1-12 años con infección por VZV (relevancia A: correspondencia directa con población de riesgo de varicela) |
| [NCT07099157](https://clinicaltrials.gov/study/NCT07099157) | Phase 4 | Reclutando | 140 | Ensayo multicéntrico aleatorizado controlado de Brivudina versus Famciclovir para herpes zóster agudo (relevancia C: estudio de fármaco de comparación, no evidencia directa de famciclovir) |
| [NCT03120962](https://clinicaltrials.gov/study/NCT03120962) | NA | Estado desconocido | 140 | Intervención temprana con Oxicodona para prevenir neuralgia posherpética aguda (relevancia C: fármaco de intervención no es famciclovir) |
| [NCT06798662](https://clinicaltrials.gov/study/NCT06798662) | NA | Sin reclutar aún | 120 | Bloqueo nervioso multimodal y tratamiento de radiofrecuencia pulsada para dolor de herpes zóster agudo (relevancia C: intervención no farmacológica) |

## Evidencia bibliográfica

| PMID | Año | Tipo | Revista | Hallazgos principales |
|------|-----|------|---------|----------------------|
| [19273678](https://pubmed.ncbi.nlm.nih.gov/19273678/) | 2009 | Estudio de cohorte/PK (Nivel 1) | Antimicrob Agents Chemother | Análisis comprehensivo de farmacocinética y seguridad de formulación oral pediátrica de famciclovir en infecciones por HSV/VZV |
| [29431387](https://pubmed.ncbi.nlm.nih.gov/29431387/) | 2017 | Revisión (Nivel 2) | Am Fam Physician | Prevención y manejo de herpes zóster y PHN, incluyendo el papel de fármacos antivirales |
| [33672709](https://pubmed.ncbi.nlm.nih.gov/33672709/) | 2021 | Revisión (Nivel 2) | Molecules | Avances en manejo de infecciones por VZV, discutiendo el lugar del tratamiento con fármacos antivirales como famciclovir |
| [8809466](https://pubmed.ncbi.nlm.nih.gov/8809466/) | 1996 | Revisión (Nivel 2) | Clin Microbiol Rev | Revisión clásica sobre patogenia de VZV, latencia y reactivación |
| [36851652](https://pubmed.ncbi.nlm.nih.gov/36851652/) | 2023 | Revisión (Nivel 2) | Viruses | Manejo de infecciones por HSV y VZV en pacientes con cáncer |
| [9675639](https://pubmed.ncbi.nlm.nih.gov/9675639/) | 1997 | Revisión | Intervirology | Eficacia de ensayos clínicos amplios de Famciclovir y Valaciclovir en herpes genital e herpes zóster agudo ya establecida |
| [11487454](https://pubmed.ncbi.nlm.nih.gov/11487454/) | 2001 | Revisión | Curr Treat Options Neurol | Herpes zóster que surge de latencia de VZV posterior a varicela en la infancia, famciclovir/valaciclovir/aciclovir de alta dosis efectivos dentro de 3 días del inicio del sarpullido |
| [16595111](https://pubmed.ncbi.nlm.nih.gov/16595111/) | 2006 | Revisión | Actas Dermosifiliogr | Fármacos aprobados en Europa para tratamiento sistémico de herpes zóster incluyendo aciclovir, valaciclovir, famciclovir |
| [12182687](https://pubmed.ncbi.nlm.nih.gov/12182687/) | 2002 | Revisión | Drugs Aging | Infecciones virales dermatológicas en pacientes ancianos: famciclovir y valaciclovir como antivirales de nueva generación con frecuencia de dosificación más baja |
| [8845591](https://pubmed.ncbi.nlm.nih.gov/8845591/) | 1996 | Revisión | Drugs Aging | Tratamiento antiviral de herpes zóster agudo en pacientes ancianos, famciclovir como uno de los tres fármacos antivirales efectivos y bien tolerados |

## Información del mercado

Este fármaco actualmente **Not marketed** en el mercado de evaluación, sin datos de licencia aprobada disponibles para mostrar.

## Consideraciones de seguridad

Consulte el prospecto del fármaco para obtener información de seguridad.

## Conclusiones y pasos siguientes

**Decisión: Proceed with Guardrails**

**Razón:**
La candidata Varicela tiene 1 ensayo clínico de Fase 3 completado de comparación directa con famciclovir (NCT01327144) más 1 ensayo de Fase 3 de PK/seguridad en población pediátrica (NCT00098046), además de 20 artículos que respaldan la consistencia del mecanismo patogénico de VZV, alcanzando un nivel de evidencia L2, siendo la dirección candidata con mayor base de evidencia en este grupo, pero aún sin ensayos de control dedicados específicamente a la indicación de "varicela" en sí, requiriendo avance cauteloso bajo mecanismos de salvaguardia.

**Requerido para progreso:**
- Datos de advertencias y contraindicaciones de prospecto TFDA / mercado objetivo (DG001, Bloqueante, actualmente imposible realizar evaluación inicial de seguridad S1)
- Datos completos de mecanismo de acción (MOA) de DrugBank (DG002, Alto, Limita profundidad de análisis de vínculo mecanístico)
- Resultados de consulta de base de datos de interacciones farmacológicas (DDI) (actualmente not_found)
- Planificación de ensayo de control especializado de eficacia/dosificación para población pediátrica de varicela

---

### Apéndice: Resumen de nivel de evidencia para otras indicaciones predichas

| Rango | Indicación | Puntuación TxGNN | Nivel de evidencia | Etapa de decisión | Recomendación |
|-------|-----------|-----------------|-------------------|-----------------|--------------|
| 1 | Post-infectious neuralgia | 99.75% | L3 | S2 | Proceed with Guardrails |
| 2 | Sequela of COVID-19 | 99.73% | L5 | S0 | Hold |
| 3 | Hepatitis C induced liver cirrhosis | 99.73% | L5 | S0 | Hold |
| 4 | Malignant pleural mesothelioma | 99.46% | L5 | S0 | Hold |
| 5 | AIDS-related disorder | 99.30% | L3 | S2 | Proceed with Guardrails |
| 6 | Malignant epithelioid mesothelioma | 99.14% | L5 | S0 | Hold |
| **7** | **Varicela (Tema principal de este informe)** | **99.11%** | **L2** | **S3** | **Proceed with Guardrails** |
| 8 | Sarcomatoid mesothelioma | 99.09% | L5 | S0 | Hold |
| 9 | Malignant visceral pleura tumor | 99.04% | L5 | S0 | Hold |

*Los 4 candidatos relacionados con mesotelioma (rank 4, 6, 8, 9) carecen de cualquier ensayo o apoyo bibliográfico, y mecanísticamente no hay intersección entre la fisiopatología de fármacos antivirales contra virus del herpes y tumores malignos relacionados con amianto. Se juzga que son ruido de predicción del modelo y no se recomienda inversión adicional de recursos.*

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

