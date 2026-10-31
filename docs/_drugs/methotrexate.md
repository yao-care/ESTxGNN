---
layout: default
title: Methotrexate
parent: Solo predicción del modelo (L5)
nav_order: 512
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-31
monitor_inn: "Methotrexate"
predicted_indications: ["pulmonary blastoma", "primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "Hodgkins lymphoma", "rhabdomyosarcoma (disease)", "parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
description: "Methotrexate: nueva indicación predicha, Pulmonary blastoma (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Methotrexate
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Methotrexate: Pulmonary blastoma
{: .text-alpha }

## Resumen en Una Frase

El metotrexato es un antimetabolito (antifolato) utilizado originalmente para la leucemia linfoblástica aguda, la artritis reumatoide, la psoriasis, la micosis fungoide y los linfomas no Hodgkin.
El modelo TxGNN predice que podría ser efectivo para el **Linfoma de Hodgkin**, con **44 ensayos clínicos** y **20 publicaciones** relacionados. Sin embargo, la mayoría son estudios de linfoma no Hodgkin o de trasplante, en los que el metotrexato es solo un componente, de modo que la evidencia específica para Hodgkin es limitada.

> **Nota sobre la selección de la indicación:** la predicción con mayor puntaje TxGNN es el blastoma pulmonar (0,9945), pero no tiene ningún ensayo ni publicación asociados (nivel L5). Se presenta el linfoma de Hodgkin (puntaje 0,9932) porque es la indicación predicha con mayor respaldo de evidencia (nivel L3, etapa S1). Al final se resumen las demás predicciones.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Pulmonary blastoma |
| Puntaje de Predicción TxGNN | 0.9945 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 14) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold (con la pregunta de investigación abierta; ver Conclusión) |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según la información conocida, el metotrexato es un antifolato que inhibe la dihidrofolato reductasa (DHFR) y, con ello, la síntesis de timidilato y de purinas, lo que frena la proliferación de células que se dividen rápidamente. Los datos farmacológicos compilados confirman como dianas la DHFR, el transportador de folato reducido 1 (SLC19A1) y HMGB1.

La eficacia del metotrexato está bien establecida en neoplasias linfoides: leucemia linfoblástica aguda, linfoma no Hodgkin y linfoma cutáneo de células T. Esa cercanía biológica con el linfoma de Hodgkin hace plausible la predicción. Además, el metotrexato ha formado parte del esquema VBM (vinblastina, bleomicina y metotrexato) combinado con radioterapia en Hodgkin de estadio temprano, con tasas de remisión completa del 94-100 % en pequeños ensayos, aunque con toxicidad pulmonar considerable en los primeros estudios.

Como contrapeso, gran parte de los ensayos aportados son protocolos multifármaco de linfoma no Hodgkin o estudios de trasplante donde el metotrexato se emplea como profilaxis de la enfermedad injerto contra huésped (EICH), lo cual no demuestra actividad antilinfoma. Varias publicaciones describen además trastornos linfoproliferativos asociados a metotrexato, que son una señal de seguridad y no de eficacia.

---

## Evidencia de Ensayos Clínicos

Se listan los ensayos más relevantes (de 44 aportados). Ninguno es específico de linfoma de Hodgkin con metotrexato como agente evaluado.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03206671](https://clinicaltrials.gov/study/NCT03206671) | Fase 3 | Activo, no recluta | 650 | Protocolo B-NHL 2013 (NHL-BFM/NOPHO): papel del rituximab en linfoma B agresivo pediátrico; el metotrexato probablemente forma parte del esquema. Indirecto (no Hodgkin) |
| [NCT00002471](https://clinicaltrials.gov/study/NCT00002471) | Fase 2 | Completado | N/D | Quimioterapia intensiva de ciclo corto en linfoma no linfoblástico de mal pronóstico y NHL recurrente |
| [NCT00005977](https://clinicaltrials.gov/study/NCT00005977) | Fase 3 | Completado | 83 | Intensificación de dosis de metotrexato en linfoma no Hodgkin de células pequeñas no hendidas y LLA-B avanzados |
| [NCT00003217](https://clinicaltrials.gov/study/NCT00003217) | Fase 1 | Completado | 20 | Intensificación de metotrexato y ciclofosfamida en NHL/LLA pediátricos en estadio III/IV |
| [NCT00290498](https://clinicaltrials.gov/study/NCT00290498) | Fase 2 | Completado | 67 | Rituximab-HCVAD alternado con rituximab-metotrexato-citarabina frente a R-CHOP en NHL B agresivo |
| [NCT02912676](https://clinicaltrials.gov/study/NCT02912676) | Fase 1/2 | Completado | 30 | 6-tioguanina con metotrexato y 6-mercaptopurina en mantenimiento de linfoma linfoblástico y LLA |
| [NCT00045539](https://clinicaltrials.gov/study/NCT00045539) | Fase 2 | Completado | N/D | Metotrexato y tiotepa en linfoma primario del SNC de reciente diagnóstico |
| [NCT01399372](https://clinicaltrials.gov/study/NCT01399372) | Fase 2 | Completado | 91 | Rituximab, metotrexato, procarbazina, vincristina y citarabina con o sin radioterapia cerebral en linfoma primario del SNC |
| [NCT00928018](https://clinicaltrials.gov/study/NCT00928018) | Fase 3 | Completado | 139 | Profilaxis de EICH (tacrolimus/sirolimus/metotrexato) tras trasplante en linfoma; cuidado de soporte, no actividad antilinfoma |
| [NCT00574496](https://clinicaltrials.gov/study/NCT00574496) | Fase 2 | Completado | 25 | Quimioterapia de rescate seguida de trasplante alogénico en linfoma de Hodgkin de alto riesgo o recidivante; el metotrexato probablemente es de soporte |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21592816](https://pubmed.ncbi.nlm.nih.gov/21592816/) | 2012 | Revisión | Crit Rev Oncol Hematol | Régimen VBM más radioterapia en Hodgkin temprano: remisión completa 94-100 % y supervivencia libre de progresión a 5 años de 75-95 % en nueve ensayos pequeños; toxicidad pulmonar inicial |
| [14635074](https://pubmed.ncbi.nlm.nih.gov/14635074/) | 2003 | Estudio clínico | Cancer | Experiencia del Gruppo Italiano Studio Linfomi con VBM más radioterapia en Hodgkin temprano favorable |
| [15659500](https://pubmed.ncbi.nlm.nih.gov/15659500/) | 2005 | Ensayo fase 3 | J Clin Oncol | Linfoma de células grandes pediátrico avanzado: metotrexato a dosis intermedia y citarabina en el régimen APO |
| [3525767](https://pubmed.ncbi.nlm.nih.gov/3525767/) | 1986 | Estudio clínico | J Clin Oncol | Mejor supervivencia en niños con NHL B en estadio III/IV con quimioterapia multifármaco basada en metotrexato a dosis altas |
| [8635099](https://pubmed.ncbi.nlm.nih.gov/8635099/) | 1996 | Estudio clínico | Cancer | Esquema IVAM (con metotrexato) como rescate en NHL agresivo recidivante o refractario |
| [10559573](https://pubmed.ncbi.nlm.nih.gov/10559573/) | 1999 | Revisión | Dermatology | Tratamiento del linfoma cutáneo de células T; el metotrexato a dosis bajas es útil en micosis fungoide resistente |
| [35848760](https://pubmed.ncbi.nlm.nih.gov/35848760/) | 2022 | Cohorte/molecular | Am J Surg Pathol | Linfoma de Hodgkin asociado a metotrexato: alteración 9p24.1 y expresión de PD-L1 (señal de seguridad) |
| [7653488](https://pubmed.ncbi.nlm.nih.gov/7653488/) | 1995 | Retrospectivo | Am J Med | Relación entre metotrexato en artritis reumatoide y neoplasias hematológicas |
| [24246254](https://pubmed.ncbi.nlm.nih.gov/24246254/) | 2014 | Reporte de caso | J Oral Maxillofac Surg | Úlcera oral VEB positiva que simula linfoma de Hodgkin en paciente tratado con metotrexato |
| [16467107](https://pubmed.ncbi.nlm.nih.gov/16467107/) | 2006 | Preclínico | Clin Cancer Res | Pralatrexato/gemcitabina superan a metotrexato/citarabina en modelos de NHL |

---

## Información de Mercado en España

Hay 20 autorizaciones vigentes (todas de medicamento con un único principio activo, ninguna cancelada). El texto de indicación aprobada no figura en los datos compilados. Se muestran las 5 principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 40698 | Metotrexato Wyeth 2,5 mg comprimidos | Comprimido | No disponible en los datos compilados |
| 57241 | Metotrexato Wyeth 25 mg/ml solución inyectable | Solución inyectable | No disponible en los datos compilados |
| 71107 | Metoject 7,5 mg/0,15 ml | Solución inyectable en jeringa precargada | No disponible en los datos compilados |
| 78631 | Metoject Pen 30 mg | Solución inyectable en pluma precargada | No disponible en los datos compilados |
| 80860 | Methofill 7,5 mg/0,15 ml EFG | Solución inyectable en jeringa precargada | No disponible en los datos compilados |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antimetabolito, clase antifolato) |
| Riesgo de Mielosupresión | Alto: los datos de contraindicación del grafo de conocimiento incluyen leucopenia, trombocitopenia y anemia |
| Clasificación de Emetogenicidad | Baja a moderada (depende de la dosis; mayor con dosis altas) |
| Ítems de Monitoreo | Hemograma con diferencial, función hepática y renal, y función pulmonar si hay síntomas respiratorios. Consultar el prospecto para el detalle |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Contraindicaciones o enfermedades de riesgo (según el grafo de conocimiento, no texto de prospecto):** insuficiencia hepática, hepatopatía, enfermedad renal, enfermedad de la vesícula biliar, úlcera gástrica y enfermedad ulcerosa péptica, trombocitopenia, leucopenia, anemia y anemia macrocítica, enfermedad pulmonar intersticial, fibrosis pulmonar (incluida la posinflamatoria), colitis ulcerosa, enfermedad inflamatoria intestinal, estomatitis, enfermedad del sistema inmunitario, abuso o dependencia de sustancias y piouréter.
- **Señales de la literatura:** trastornos linfoproliferativos asociados a metotrexato (incluidos casos que simulan o constituyen linfoma de Hodgkin) y toxicidad pulmonar con el régimen VBM.
- **Interacciones farmacológicas:** los datos compilados describen interacciones de tipo farmacológico con dianas (transportador de folato reducido 1, DHFR y HMGB1), no con otros fármacos. Consultar el prospecto para las interacciones medicamentosas clínicas.

Las advertencias y contraindicaciones del prospecto de la AEMPS no estaban disponibles en los datos compilados; consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold** (la etapa S1 lo clasifica como pregunta de investigación; no se recomienda avanzar clínicamente todavía)

**Justificación:**
El metotrexato tiene alta plausibilidad mecanística y uso histórico en linfomas (incluido el régimen VBM en Hodgkin), pero la evidencia específica para Hodgkin es antigua y limitada, y la mayoría de los ensayos aportados no evalúan el metotrexato como agente antilinfoma en esta enfermedad. Además, el tratamiento actual del Hodgkin se basa en otros esquemas, y el propio metotrexato se asocia a trastornos linfoproliferativos.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank.
- Prospecto de la AEMPS con advertencias, contraindicaciones e indicaciones aprobadas (bloqueante para el cribado de seguridad).
- Revisión sistemática de regímenes con metotrexato en Hodgkin (VBM) frente a los estándares actuales.
- Evaluación de compatibilidad de vías de administración y del perfil de toxicidad (pulmonar, hematológica) en la población objetivo.

---

### Otras Predicciones del Modelo (referencia)

| Indicación predicha | Puntaje TxGNN | Nivel de evidencia | Recomendación |
|------|------|------|------|
| Blastoma pulmonar | 0,9945 | L5 | Hold |
| Linfoma pulmonar primario | 0,9945 | L5 | Hold |
| Adenocarcinoma fetal bien diferenciado de pulmón | 0,9942 | L5 | Hold |
| Rabdomiosarcoma | 0,9925 | L2 | Pregunta de investigación (S1) |
| Rabdomiosarcoma embrionario parameníngeo | 0,9921 | L5 | Hold |
| Rabdomiosarcoma embrionario botrioide de vagina | 0,9921 | L5 | Hold |
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

