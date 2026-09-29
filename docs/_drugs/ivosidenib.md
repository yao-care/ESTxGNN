---
layout: default
title: Ivosidenib
parent: Solo predicción del modelo (L5)
nav_order: 297
evidence_level: L5
indication_count: 3
---

# Ivosidenib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Ivosidenib: De Enfermedad Mieloide con Mutación IDH1 a Poliomielitis Bulbar

## Resumen en Una Frase

Ivosidenib es un inhibidor de la enzima IDH1 mutada y está comercializado en España como TIBSOVO, aunque el registro no incluye el texto de su indicación aprobada. El modelo TxGNN predice que podría ser efectivo para **poliomielitis bulbar**, pero hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción, y no existe un vínculo mecanístico plausible.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en el registro de autorización (el texto de indicación está vacío) |
| Nueva Indicación Predicha | Poliomielitis bulbar |
| Puntaje de Predicción TxGNN | 99.31% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

**Esta predicción no es razonable desde el punto de vista biológico.** Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según el análisis mecanístico disponible, ivosidenib inhibe la enzima IDH1 mutada y reduce el oncometabolito 2-hidroxiglutarato. Este mecanismo es relevante en neoplasias mieloides con mutación IDH1.

La poliomielitis bulbar es una infección viral aguda de las neuronas motoras. La inhibición de IDH1 no tiene un papel conocido en la replicación del poliovirus ni en la respuesta del huésped. El puntaje alto (0.993) probablemente sea un artefacto del grafo de conocimiento, ya que no hay ensayos ni literatura que lo sustenten.

Las otras dos predicciones del modelo sí son biológicamente plausibles: **leucemia mieloide aguda y síndromes mielodisplásicos relacionados con radiación**, y los **relacionados con agentes alquilantes**. Ambas tienen un puntaje de 99.26%. Son subtipos secundarios a terapia que pueden portar mutaciones en IDH1, y el posible beneficio dependería del estado mutacional y no de la causa. Como ivosidenib ya se comercializa para enfermedad mieloide con IDH1 mutado, la pregunta abierta es si estos subgrupos necesitan evidencia propia. El modelo les asigna puntajes idénticos, lo que sugiere que los trata como nodos casi equivalentes y no como evidencia independiente. También en estos dos casos hay 0 ensayos y 0 publicaciones, por lo que son solo preguntas de investigación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1231728001 | TIBSOVO 250 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA (Les Laboratoires Servier) | Comprimido recubierto con película | No especificada en el registro |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de IDH1 mutada) |
| Riesgo de Mielosupresión, Emetogenicidad, Monitoreo y Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas en la consulta realizada.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal (poliomielitis bulbar) carece de ensayos, literatura y vínculo mecanístico, por lo que solo es una predicción del modelo (L5). No se recomienda avanzar con ella, y el puntaje alto probablemente refleja un artefacto del grafo de conocimiento.

**Para avanzar se necesita:**
- Descartar la poliomielitis bulbar como línea de investigación, salvo que aparezca evidencia independiente.
- Descargar y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicación aprobada), pendiente y bloqueante para cualquier cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Evaluar por separado las predicciones de leucemia mieloide aguda y síndromes mielodisplásicos relacionados con radiación y con agentes alquilantes, estratificadas por estado mutacional de IDH1.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

