---
layout: default
title: Hexetidine
parent: Solo predicción del modelo (L5)
nav_order: 394
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Hexetidine: nueva indicación predicha, Aneurisma del tabique interventricular (nivel de evidencia L5). Indicación original: No disponible en la autorización de la AEMPS (el texto de indicación…"
monitor_inn: "hexetidine"
predicted_indications: ["interventricular septum aneurysm", "pulmonary valve disease", "orofacial clefting syndrome", "Laubry-Pezzi syndrome", "genetic syndromic Pierre Robin syndrome", "disorder of fucoglycosan synthesis", "partial deletion of the long arm of chromosome 22", "Pierre Robin syndrome associated with a chromosomal anomaly", "partial deletion of the long arm of chromosome 7", "Jeune syndrome situs inversus"]
---

# Hexetidine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Hexetidina: De Antiséptico Local a Aneurisma del Tabique Interventricular
{: .text-alpha }

## Resumen en Una Frase

Hexetidina es un antiséptico de uso tópico (con actividad antibacteriana y antifúngica) que en España está autorizado en una crema rectal de un solo principio activo.
El modelo TxGNN predice que podría ser efectivo para el **aneurisma del tabique interventricular**,
pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en la autorización de la AEMPS (el texto de indicación está vacío) |
| Nueva Indicación Predicha | Aneurisma del tabique interventricular |
| Puntaje de Predicción TxGNN | 0,9916 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 1 de 1) |
| Número de Autorizaciones | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la hexetidina es un antiséptico tópico con actividad antibacteriana y antifúngica, utilizado sobre todo en el cuidado de la cavidad oral y, en este caso, autorizado en forma de crema rectal.

La relación entre su uso original y la nueva indicación es muy débil. Un aneurisma del tabique interventricular es una alteración estructural cardíaca, y la hexetidina no tiene ninguna acción conocida sobre las vías del desarrollo o la estructura cardíaca. Además, un antiséptico tópico tiene una exposición sistémica mínima.

Por ello, la puntuación alta proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica, sin respaldo clínico, mecanístico ni bibliográfico. No se identifica un vínculo mecanístico plausible.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 56385 | ABRASONE RECTAL, CREMA RECTAL | Crema rectal | No especificada |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en los datos compilados para este informe.

## Otras Predicciones del Modelo (Contexto)

Las siguientes predicciones de mayor rango tampoco cuentan con ensayos clínicos y todas tienen nivel de evidencia L5 y decisión Hold:

| Rango | Enfermedad Predicha | Puntaje TxGNN | Comentario |
|------|------|------|------|
| 2 | Enfermedad de la válvula pulmonar | 0,9909 | Sin mecanismo plausible; exposición sistémica insignificante |
| 3 | Síndrome de fisura orofacial | 0,9908 | Malformación del desarrollo; el antiséptico no puede corregirla |
| 4 | Síndrome de Laubry-Pezzi | 0,9906 | Cardiopatía estructural; sin mecanismo conocido |
| 5 | Síndrome de Pierre Robin sindrómico genético | 0,9905 | Origen del desarrollo; sin acción modificadora de la enfermedad |
| 6 | Trastorno de la síntesis de fucoglicanos | 0,9904 | Una revisión (PMID 12974527) sobre agentes antiplaca; relación indirecta, no es evidencia clínica |
| 7 | Deleción parcial del brazo largo del cromosoma 22 | 0,9903 | Causa genética; sin mecanismo |
| 8 | Síndrome de Pierre Robin asociado a anomalía cromosómica | 0,9903 | Causa genética; sin mecanismo |
| 9 | Deleción parcial del brazo largo del cromosoma 7 | 0,9903 | Causa genética; sin mecanismo |
| 10 | Síndrome de Jeune con situs inversus | 0,9902 | Ciliopatía; sin acción conocida |

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible entre un antiséptico tópico y una alteración estructural cardíaca. Además, no se dispone de datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS (advertencias y contraindicaciones) y la indicación autorizada del producto
- Datos del mecanismo de acción desde DrugBank
- Una hipótesis mecanística biológicamente plausible y estudios preclínicos que la respalden
- Evaluar la compatibilidad de la vía de administración (actualmente solo crema rectal) con la nueva indicación
- Considerar la priorización de otras indicaciones más afines a su perfil antiséptico (por ejemplo, de uso oral o local)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

