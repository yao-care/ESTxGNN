---
layout: default
title: Vindesine
parent: Solo predicción del modelo (L5)
nav_order: 851
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Vindesine: nueva indicación predicha, Ganglioneuroblastoma (nivel de evidencia L5). Indicación original: Leucemia linfoblástica aguda (según el grafo de conocimiento"
monitor_inn: "Vindesine"
predicted_indications: ["ganglioneuroblastoma (disease)", "vertebral anomalies and variable endocrine and T-cell dysfunction", "neuroblastoma", "retroperitoneal neoplasm"]
---

# Vindesine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Vindesina: De Leucemia Linfoblástica Aguda a Ganglioneuroblastoma

## Resumen en Una Frase

Vindesina es un alcaloide de la vinca (inhibidor de la polimerización de la tubulina), utilizado originalmente en el tratamiento de la leucemia linfoblástica aguda y otras neoplasias hematológicas y sólidas.
El modelo TxGNN predice que podría ser efectiva para **ganglioneuroblastoma**, pero para esta indicación no hay ensayos clínicos ni publicaciones que la respalden.
La señal con más respaldo entre las predicciones es la de **neuroblastoma** (6 ensayos clínicos y 10 publicaciones, casi todos de protocolos multifármaco o estudios preclínicos), que se analiza en este informe como indicación relacionada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Leucemia linfoblástica aguda (según el grafo de conocimiento; el texto de indicación de la autorización de AEMPS no está disponible) |
| Nueva Indicación Predicha | Ganglioneuroblastoma |
| Puntaje de Predicción TxGNN | 99,89% |
| Nivel de Evidencia | L5 (ganglioneuroblastoma); L3 para neuroblastoma |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold (ganglioneuroblastoma); "pregunta de investigación" para neuroblastoma |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, la vindesina es un alcaloide de la vinca semisintético, derivado de la vinblastina, que inhibe la polimerización de la tubulina y provoca una detención mitótica. Su eficacia en leucemias agudas y en otras neoplasias ha sido descrita en la literatura.

El ganglioneuroblastoma pertenece al espectro de los tumores neuroblásticos y comparte biología con el neuroblastoma. Los alcaloides de la vinca (sobre todo la vincristina) son componentes establecidos de los regímenes de quimioterapia del neuroblastoma, por lo que es plausible que un agente antimitótico actúe sobre estos tumores. No obstante, se trata únicamente de una inferencia basada en el modelo: no hay estudios con vindesina en ganglioneuroblastoma.

Conviene ser cautos con el puntaje. La predicción de neuroblastoma (99,86%) cuenta con datos preclínicos in vitro que muestran citotoxicidad de la vindesina en líneas celulares de neuroblastoma, y con un estudio de fase II de 1982 en neoplasias infantiles. Sin embargo, los ensayos de fase 3 listados son protocolos multifármaco en los que no se puede confirmar ni aislar la contribución de la vindesina, y la vincristina es el alcaloide de la vinca habitual en los regímenes actuales.

---

## Evidencia de Ensayos Clínicos

Para ganglioneuroblastoma no hay ensayos clínicos relacionados registrados. A continuación se presentan los ensayos de la indicación relacionada, **neuroblastoma**. En ninguno se ha podido confirmar el uso de vindesina con los datos disponibles.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03042429](https://clinicaltrials.gov/study/NCT03042429) | Fase 3 | Completado | 360 | Quimioterapia combinada con trasplante de progenitores e isotretinoína en neuroblastoma de alto riesgo; añade dos ciclos con topotecán |
| [NCT04221035](https://clinicaltrials.gov/study/NCT04221035) | Fase 3 | Reclutando | 800 | HR-NBL2 de SIOPEN: tres aleatorizaciones de inducción, consolidación y radioterapia en neuroblastoma de alto riesgo |
| [NCT00410631](https://clinicaltrials.gov/study/NCT00410631) | Fase 3 | Desconocido | 642 | Protocolo NB2004 de tratamiento adaptado al riesgo en niños con neuroblastoma |
| [NCT00002802](https://clinicaltrials.gov/study/NCT00002802) | Fase 3 | Completado | 500 | Ensayo multicéntrico en niños y adolescentes con neuroblastoma (1990-2003) |
| [NCT00017225](https://clinicaltrials.gov/study/NCT00017225) | Fase 2 | Completado | No disponible | Diversas terapias (quimioterapia, radioterapia, trasplante de progenitores) en neuroblastoma |
| [NCT00526318](https://clinicaltrials.gov/study/NCT00526318) | No aplica | Desconocido | 360 | Protocolo NB2004-HR para neuroblastoma de alto riesgo; información específica del fármaco limitada |

---

## Evidencia de Literatura

Para ganglioneuroblastoma no hay literatura relacionada disponible. Se muestran las publicaciones más relevantes para **neuroblastoma**:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [7038420](https://pubmed.ncbi.nlm.nih.gov/7038420/) | 1982 | Estudio clínico fase II | Med Pediatr Oncol | Vindesina en 36 niños con neoplasias; neurotoxicidad y toxicidad digestiva graves con la pauta diaria, mejor tolerancia con infusión semanal de 4 mg/m² |
| [9340428](https://pubmed.ncbi.nlm.nih.gov/9340428/) | 1997 | Observacional | Klin Padiatr | Estudio NB90: regeneración mielopoyética en 14 niños tratados con ciclos que incluyen vindesina, etopósido y cisplatino |
| [3731152](https://pubmed.ncbi.nlm.nih.gov/3731152/) | 1986 | Preclínico in vitro | Cancer Treat Rep | Sensibilidad diferencial de seis líneas celulares de neuroblastoma a antimitóticos, incluida la vindesina |
| [6943380](https://pubmed.ncbi.nlm.nih.gov/6943380/) | 1981 | Preclínico in vitro | J Natl Cancer Inst | Citotoxicidad comparada de vincristina y vindesina; las células de neuroblastoma murino resultaron unas cinco veces menos sensibles a la vindesina |
| [2166461](https://pubmed.ncbi.nlm.nih.gov/2166461/) | 1990 | Preclínico in vitro | Anticancer Res | El ácido gamma-linolénico duplicó aproximadamente la citotoxicidad de los alcaloides de la vinca, incluida la vindesina |
| [21139829](https://pubmed.ncbi.nlm.nih.gov/21139829/) | 2010 | Reporte de caso | Rare Tumors | Neuroblastoma epidural en una mujer de 67 años tratada con un ciclo de vindesina, cisplatino y etopósido, entre otros tratamientos |
| [37444475](https://pubmed.ncbi.nlm.nih.gov/37444475/) | 2023 | Cohorte retrospectiva | Cancers | Dinutuximab beta con ciclos de quimioterapia N5/N6 en 25 pacientes con neuroblastoma recaído/refractario |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 55626 | ENISON 5 MG POLVO PARA SOLUCIÓN INYECTABLE (Laboratorio Stada S.L.) | Polvo para solución inyectable | Texto de indicación no disponible |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (alcaloide de la vinca, antimitótico) |
| Riesgo de Mielosupresión | Alto: según la literatura, la toxicidad limitante de la dosis es la mielosupresión (nadir hacia los días 7-8, recuperación hacia los días 11-13) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Ítems de Monitoreo | Hemograma con diferencial, función hepática y renal; vigilancia de neurotoxicidad periférica y autonómica y de toxicidad digestiva |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Neurotoxicidad y toxicidad digestiva**: en el estudio de fase II en niños (PMID 7038420), la pauta de 2 mg/m²/día durante cinco días produjo neurotoxicidad grave y toxicidad gastrointestinal potencialmente mortal; la pauta semanal de 4 mg/m² fue mejor tolerada.
- **Neuropatía periférica**: descrita con vindesina y, sobre todo, con vincristina (PMID 6297011).

No se dispone de datos de interacciones farmacológicas. Consultar el prospecto para el resto de la información de seguridad (advertencias y contraindicaciones).

---

## Conclusión y Próximos Pasos

**Decisión: Hold** (ganglioneuroblastoma)

**Justificación:**
Para ganglioneuroblastoma solo existe la predicción del modelo (L5), sin ensayos ni literatura. La indicación relacionada de neuroblastoma alcanza L3 y se considera una pregunta de investigación: la evidencia es indirecta (estudios preclínicos, un estudio de fase II antiguo y protocolos multifármaco en los que no se confirma la vindesina). Además, la leucemia mieloide, también predicha, solapa con una indicación ya existente (crisis blástica de LMC) y no constituye un reposicionamiento genuino.

**Para avanzar se necesita:**
- Verificar si la vindesina forma parte de los regímenes de los ensayos de neuroblastoma (NB2004, NB90, HR-NBL2) revisando los protocolos
- Revisar el prospecto de AEMPS (advertencias, contraindicaciones, texto de indicación aprobada), cuya ausencia bloquea el cribado de seguridad
- Obtener datos del mecanismo de acción desde DrugBank
- Comparar vindesina frente a vincristina en neuroblastoma/ganglioneuroblastoma, con revisión sistemática y datos específicos de ganglioneuroblastoma
- Plan de monitoreo de seguridad para población pediátrica (neurotoxicidad, mielosupresión)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

