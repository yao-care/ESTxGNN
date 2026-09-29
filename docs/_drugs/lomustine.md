---
layout: default
title: Lomustine
parent: Solo predicción del modelo (L5)
nav_order: 326
evidence_level: L5
indication_count: 10
---

# Lomustine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Lomustina: De Agente Alquilante Antineoplásico a Linfosarcoma

## Resumen en Una Frase

Lomustina es una nitrosourea alquilante y liposoluble, utilizada en oncología, con una autorización comercializada en España (BELUSTINE cápsulas). Su indicación original no figura en los datos de AEMPS disponibles.
El modelo TxGNN predice que podría ser efectiva para **linfosarcoma** (linfoma no Hodgkin). La respaldan **17 ensayos clínicos** y **20 publicaciones**, aunque casi todos evalúan regímenes con varios fármacos y con muestras pequeñas.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Linfosarcoma |
| Puntaje de Predicción TxGNN | 99,90 % |
| Nivel de Evidencia | L2 (varios ensayos de Fase 2 completados, pero pequeños y con combinaciones) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos de origen. Según la justificación mecanística del análisis, lomustina es una nitrosourea alquilante lipofílica que atraviesa la barrera hematoencefálica y forma enlaces cruzados en el ADN. Este tipo de acción encaja con las neoplasias linfoides sensibles a agentes alquilantes.

Los datos no recogen la indicación original de la autorización española. Aun así, la evidencia muestra que lomustina ya forma parte de regímenes contra linfomas, incluido el linfoma de Hodgkin. También se emplea en combinaciones para el linfoma primario del sistema nervioso central (SNC), donde su capacidad de penetrar en el SNC es una ventaja. Un estudio aleatorizado clásico de 1978 comparó CCNU (lomustina) con metil-CCNU en linfomas avanzados, incluido el linfosarcoma.

Hay una limitación importante: casi toda la evidencia procede de combinaciones (por ejemplo, R-MCP, LEMP, CEAC, LACE). No es posible aislar la contribución de lomustina por sí sola. Por eso la predicción es biológicamente plausible, pero la eficacia propia del fármaco no está demostrada.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00049439](https://clinicaltrials.gov/study/NCT00049439) | Fase 2 | Completado | 54 | Lomustina, etopósido, ciclofosfamida y procarbazina orales con dosis modificadas en linfoma no Hodgkin asociado al SIDA (EE. UU. y África) |
| [NCT01775475](https://clinicaltrials.gov/study/NCT01775475) | Fase 2 | Completado | 7 | Aleatorizado: CHOP frente a quimioterapia oral (incluye lomustina) en linfoma asociado al VIH en África subsahariana |
| [NCT00003114](https://clinicaltrials.gov/study/NCT00003114) | Fase 2 | Completado | 5 | Régimen oral con lomustina en enfermedad de Hodgkin asociada al SIDA (estadios IIB a IV) |
| [NCT00074191](https://clinicaltrials.gov/study/NCT00074191) | Fase 2 | Completado | 1 | Metotrexato, procarbazina y CCNU en linfoma primario del SNC. Lomustina es componente explícito, pero solo se inscribió 1 paciente |
| [NCT00989352](https://clinicaltrials.gov/study/NCT00989352) | Fase 2 | Desconocido | 56 | Rituximab con metotrexato a dosis altas, lomustina y procarbazina, seguido de mantenimiento, en linfoma primario del SNC en mayores de 65 años |
| [NCT00003113](https://clinicaltrials.gov/study/NCT00003113) | Fase 2 | Terminado | 6 | Quimioterapia oral combinada con G-CSF en linfoma no Hodgkin de grado intermedio/alto en ancianos. Muestra muy pequeña |
| [NCT00003929](https://clinicaltrials.gov/study/NCT00003929) | Fase 2 | Retirado | 0 | Lomustina, procarbazina, filgrastim y radioterapia en linfoma primario del SNC. No se generaron datos |
| [NCT03678883](https://clinicaltrials.gov/study/NCT03678883) | Fase 1/2 | Activo, sin reclutar | 350 | Inhibidor de GSK-3β (9-ING-41) solo o con quimioterapia en cánceres refractarios. Lomustina es, como mucho, un fármaco acompañante, con relevancia baja |

**Nota:** los ensayos con lomustina explícita son pequeños o terminaron pronto. El de mayor tamaño (NCT00049439, n=54) es el que aporta más información.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21303800](https://pubmed.ncbi.nlm.nih.gov/21303800/) | 2011 | Ensayo Fase 2 (piloto) | Ann Oncol | Inmunoquimioterapia R-MCP (rituximab, metotrexato, procarbazina, lomustina) en linfoma primario del SNC en ancianos |
| [348294](https://pubmed.ncbi.nlm.nih.gov/348294/) | 1978 | Estudio aleatorizado | Cancer | CCNU frente a metil-CCNU (dosis única oral cada 6 semanas) en linfomas avanzados: Hodgkin, linfosarcoma y sarcoma de células reticulares |
| [8436213](https://pubmed.ncbi.nlm.nih.gov/8436213/) | 1993 | Ensayo clínico | Eur J Haematol | Régimen LEMP (lomustina, etopósido, metotrexato, prednisona) en 22 pacientes con linfoma no Hodgkin recidivante o refractario |
| [10711848](https://pubmed.ncbi.nlm.nih.gov/10711848/) | 1999 | Estudio clínico/revisión | Drugs | Régimen oral con lomustina, etopósido, ciclofosfamida y procarbazina en 38 pacientes con linfoma asociado al SIDA. Aprovecha la vía oral y el paso de la barrera hematoencefálica |
| [15803492](https://pubmed.ncbi.nlm.nih.gov/15803492/) | 2005 | Estudio clínico | Cancer | Régimen CIBO-P (lomustina, ifosfamida, bleomicina, vincristina, cisplatino) en linfoma no Hodgkin agresivo refractario o recidivante |
| [33336792](https://pubmed.ncbi.nlm.nih.gov/33336792/) | 2021 | Estudio clínico | Br J Haematol | Régimen oral DECC (dexametasona, etopósido, clorambucilo, lomustina) en linfoma difuso de células B grandes recidivante o refractario (según el título; sin resumen disponible) |
| [30197327](https://pubmed.ncbi.nlm.nih.gov/30197327/) | 2018 | Cohorte retrospectiva | J Cancer Res Ther | Acondicionamiento LACE (lomustina, citarabina, ciclofosfamida, etopósido) en trasplante autólogo por linfoma refractario o recidivante: toxicidad y resultados a largo plazo |
| [35999255](https://pubmed.ncbi.nlm.nih.gov/35999255/) | 2022 | Cohorte retrospectiva | Sci Rep | Comparación de acondicionamientos CEAC (con lomustina), BEAM e IEAC antes de trasplante autólogo en 52 pacientes con linfoma T periférico |
| [17134114](https://pubmed.ncbi.nlm.nih.gov/17134114/) | 2006 | Revisión | Neurosurg Focus | Quimioterapia del linfoma primario del SNC: el metotrexato a dosis altas es el fármaco más eficaz y se combina con otros, entre ellos lomustina |
| [22888657](https://pubmed.ncbi.nlm.nih.gov/22888657/) | 2012 | Preclínico (ratón) | Vopr Onkol | En ratones con linfosarcoma LIO-1 intracraneal, lomustina oral aumentó la supervivencia 1,6 veces y, combinada con gemcitabina, 3,3 veces |

**Nota:** el conjunto de literatura incluye además varios estudios veterinarios (perros y gatos) con protocolos con lomustina. Se han excluido de la tabla por su menor aplicabilidad humana.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Laboratorio |
|---------|------|------|-----------|
| 58474 | BELUSTINE CÁPSULAS | Cápsula dura | Bellon |

**Nota:** los datos disponibles de AEMPS no incluyen el texto de la indicación aprobada para esta autorización.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (agente alquilante, clase nitrosourea) |
| Riesgo de Mielosupresión | Alto. Es una toxicidad limitante de dosis, típicamente tardía y acumulativa (leucopenia y trombocitopenia). Además, un caso veterinario describe aplasia medular por sobredosis (PMID 31062418) |
| Clasificación de Emetogenicidad | Moderada a alta, según la dosis |
| Items de Monitoreo | Hemograma completo con diferencial y plaquetas (seguimiento prolongado tras cada dosis), función hepática y renal, y función pulmonar (la literatura describe toxicidad pulmonar por nitrosoureas: PMID 1470749) |
| Protección en Manejo | Sí. Debe seguir las normas de manejo de medicamentos citotóxicos |

Estos datos proceden de la clase farmacológica y de la literatura recopilada. Deben confirmarse con la ficha técnica de AEMPS.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay varios ensayos de Fase 2 completados y estudios clínicos con regímenes que incluyen lomustina en linfomas (nivel L2), y su mecanismo alquilante con penetración en el SNC es coherente. Sin embargo, la evidencia procede de combinaciones con muestras pequeñas. Además, no se dispone de datos de seguridad de la ficha técnica en España, así que solo debe avanzarse con condiciones.

**Para avanzar se necesita:**
- Descargar y analizar la ficha técnica de AEMPS (advertencias y contraindicaciones), lo que actualmente bloquea el cribado de seguridad
- Confirmar la indicación aprobada de BELUSTINE en España
- Completar los datos del mecanismo de acción desde DrugBank
- Buscar estudios que permitan aislar la contribución de lomustina, o que comparen regímenes con y sin ella
- Definir un plan de monitorización hematológica, hepática y pulmonar, y confirmar la exposición acumulada permitida
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

