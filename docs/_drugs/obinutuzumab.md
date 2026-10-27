---
layout: default
title: Obinutuzumab
parent: Solo predicción del modelo (L5)
nav_order: 579
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Obinutuzumab: nueva indicación predicha, LLC/LLCP de centro pregerminal (nivel de evidencia L5). Indicación original: Leucemia linfoblástica aguda y síndrome de Richter (según el grafo de…"
---

# Obinutuzumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Obinutuzumab: De Leucemia Linfoblástica Aguda a Leucemia Linfocítica Crónica/Linfoma Linfocítico de Células Pequeñas de Centro Pregerminal
{: .text-alpha }

## Resumen en Una Frase

Obinutuzumab es un anticuerpo monoclonal anti-CD20. Según los datos compilados, sus indicaciones originales de partida son la leucemia linfoblástica aguda y el síndrome de Richter.
El modelo TxGNN predice que podría ser efectivo para la **leucemia linfocítica crónica/linfoma linfocítico de células pequeñas (LLC/LLCP) de centro pregerminal**, con un puntaje de 99,21 %.
Para esta indicación concreta hay **0 ensayos clínicos** y **0 publicaciones** registrados, por lo que el único respaldo es la predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Leucemia linfoblástica aguda y síndrome de Richter (según el grafo de conocimiento; el texto de indicación de las autorizaciones españolas está vacío) |
| Nueva Indicación Predicha | LLC/LLCP de centro pregerminal |
| Puntaje de Predicción TxGNN | 99,21 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Obinutuzumab es un anticuerpo anti-CD20 de tipo II, glicoingeniería, que potencia la muerte celular directa y la citotoxicidad celular dependiente de anticuerpos. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro del fármaco. La descripción anterior procede del análisis mecanístico de los datos compilados.

La indicación predicha es un subtipo molecular de LLC/LLCP (IGHV no mutado). Las células de la LLC expresan CD20, por lo que existe una base mecanística plausible para la actividad anti-CD20. Las indicaciones originales (leucemia linfoblástica aguda y síndrome de Richter) también son neoplasias hematológicas de linaje linfoide.

Hay una salvedad importante. Obinutuzumab ya está aprobado en la práctica para la LLC en general, así que esta predicción es un subtipo de una indicación existente y no una oportunidad real de reposicionamiento. Además, el único respaldo disponible para esta entrada es la predicción de TxGNN.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

## Otras Indicaciones Predichas

- **LLC/LLCP con hipermutación somática de IGHV (mutado)**: puntaje TxGNN de 99,21 %, nivel L5, decisión Hold. Es otro subtipo molecular de LLC/LLCP, sin ensayos ni literatura. Tampoco constituye una señal de reposicionamiento distinta.
- **Linfoma folicular**: puntaje TxGNN de 99,18 %, nivel L1, decisión Proceed with Guardrails. Es la predicción con más respaldo y se resume a continuación. El propio análisis señala que el fármaco ya está aprobado para esta enfermedad en la práctica real. Por tanto, debe leerse como confirmación de un uso establecido y no como un hallazgo nuevo. Conviene verificar el estado de la indicación en cada jurisdicción.

**Ensayos clínicos destacados en linfoma folicular:**

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT05100862](https://clinicaltrials.gov/study/NCT05100862) | Fase 3 | Activo, sin reclutar | 799 | Zanubrutinib + obinutuzumab frente a lenalidomida + rituximab en linfoma folicular o de la zona marginal en recaída/refractario |
| [NCT03817853](https://clinicaltrials.gov/study/NCT03817853) | Fase 4 | Completado | 114 | Infusión corta de obinutuzumab en linfoma folicular avanzado sin tratamiento previo |
| [NCT02871219](https://clinicaltrials.gov/study/NCT02871219) | Fase 2 | Completado | 96 | Obinutuzumab + lenalidomida en linfoma folicular sin tratamiento previo |
| [NCT00825149](https://clinicaltrials.gov/study/NCT00825149) | Fase 1 | Completado | 137 | Seguridad y eficacia de obinutuzumab con CHOP, FC o bendamustina |
| [NCT05929222](https://clinicaltrials.gov/study/NCT05929222) | Fase 3 | Reclutando | 190 | Radioterapia sola frente a radioterapia + obinutuzumab en linfoma folicular en estadio temprano |

**Literatura destacada en linfoma folicular:**

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29856692](https://pubmed.ncbi.nlm.nih.gov/29856692/) | 2018 | ECA | J Clin Oncol | GALLIUM: influencia de la quimioterapia asociada en la eficacia y seguridad de obinutuzumab frente a rituximab en linfoma folicular sin tratamiento previo |
| [37404773](https://pubmed.ncbi.nlm.nih.gov/37404773/) | 2023 | ECA | HemaSphere | Resultados finales de GALLIUM: obinutuzumab frente a rituximab con inmunoquimioterapia en linfoma indolente |
| [37506346](https://pubmed.ncbi.nlm.nih.gov/37506346/) | 2023 | ECA | J Clin Oncol | ROSEWOOD: zanubrutinib + obinutuzumab frente a obinutuzumab solo en linfoma folicular en recaída/refractario |
| [31296423](https://pubmed.ncbi.nlm.nih.gov/31296423/) | 2019 | Fase 2 de brazo único | Lancet Haematol | GALEN: obinutuzumab + lenalidomida en linfoma folicular en recaída/refractario |
| [28976863](https://pubmed.ncbi.nlm.nih.gov/28976863/) | 2017 | Estudio clínico (clasificado como revisión en los datos) | N Engl J Med | Obinutuzumab en el tratamiento de primera línea del linfoma folicular |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 114937001 | GAZYVARO 1000 MG concentrado para solución para perfusión | Concentrado para solución para perfusión | No especificada en los datos |
| 114937001IP | GAZYVARO 1000 mg concentrado para solución para perfusión | Concentrado para solución para perfusión | No especificada en los datos |

Ambas autorizaciones están vigentes, son de monofármaco y su titular es Roche Registration GmbH.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (anticuerpo monoclonal anti-CD20) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se consultaron 81 interacciones, de las cuales se muestra una selección de 20.
  - **Gravedad mayor**: deferiprona, samario (153Sm) lexidronam, adalimumab, baricitinib, certolizumab pegol, cladribina y clozapina.
  - **Gravedad moderada**: estroncio-89 cloruro, roflumilast, cloranfenicol (incluida la vía oftálmica), zidovudina, alefacept, alemtuzumab, anakinra, azatioprina, canakinumab y varias vacunas (toxoide tetánico, ántrax, cólera vivo).
  - Muchas de las interacciones listadas afectan al sistema inmunitario o a la médula ósea, lo que sugiere un riesgo aditivo de inmunosupresión o mielosupresión.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para la LLC/LLCP de centro pregerminal solo existe la predicción del modelo (nivel L5), sin ensayos ni literatura específicos. Además, se trata de un subtipo de una indicación ya aprobada y no de un reposicionamiento genuino.

**Para avanzar se necesita:**
- Confirmar el estado de la indicación de LLC en el prospecto de AEMPS, ya que el texto de indicación de las autorizaciones está vacío.
- Obtener el texto de advertencias y contraindicaciones del prospecto, un vacío de datos bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción (MOA) desde DrugBank.
- Buscar evidencia específica por subtipo molecular (IGHV mutado/no mutado), por ejemplo análisis de subgrupos de ensayos de LLC con obinutuzumab.
- Para el linfoma folicular, verificar el estado de la etiqueta en cada jurisdicción y tratarlo como confirmación de un uso establecido.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

