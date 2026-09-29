---
layout: default
title: Sulfasalazine
parent: Solo predicción del modelo (L5)
nav_order: 505
evidence_level: L5
indication_count: 10
---

# Sulfasalazine
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

# Sulfasalazina: De Artritis Reumatoide y Enfermedad Inflamatoria Intestinal a Síndrome de Braquidactilia-Sindactilia

## Resumen en Una Frase

La sulfasalazina es un fármaco antiinflamatorio utilizado en artritis reumatoide y enfermedad inflamatoria intestinal (según la fuente farmacológica del paquete de evidencia; el registro de la AEMPS no incluye el texto de indicación).
El modelo TxGNN predice que podría ser efectivo para **síndrome de braquidactilia-sindactilia**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Artritis reumatoide y enfermedad inflamatoria intestinal (fuente farmacológica; el registro AEMPS no trae texto de indicación) |
| Nueva Indicación Predicha | Síndrome de braquidactilia-sindactilia |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la sulfasalazina es un fármaco antiinflamatorio cuyo mecanismo principal no ha podido confirmarse. Se le atribuyen la inhibición de NF-kB, la inhibición del transportador xCT (antiportador cistina/glutamato) y, en bacterias, la inhibición de la enzima dihidropteroato sintasa. Su eficacia está reconocida en enfermedades inflamatorias, y figura en la Lista de Medicamentos Esenciales de la OMS.

**Esta predicción no resulta razonable desde el punto de vista mecanístico.** El síndrome de braquidactilia-sindactilia es una malformación congénita rara de las extremidades, de origen genético del desarrollo. No tiene un componente inflamatorio que la sulfasalazina pueda modular. La evaluación del paquete de evidencia concluye que no existe un vínculo plausible y que el puntaje alto de TxGNN probablemente sea un artefacto del grafo de conocimiento.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Otras Predicciones con Más Respaldo

Aunque la primera predicción carece de evidencia, otras dos predicciones del mismo modelo sí cuentan con algún respaldo:

| Indicación Predicha | Puntaje TxGNN | Nivel | Decisión | Evidencia disponible |
|------|------|------|------|------|
| Osteoartritis | 99.64% | L4 | Pregunta de investigación | Estudios preclínicos e in vitro (PMID 19690126, 26466556, 29548914); ningún dato de eficacia en humanos. Los 2 ensayos clínicos asociados no evalúan sulfasalazina en osteoartritis. |
| Espondiloartropatía (susceptibilidad) | 99.53% | L4 | Pregunta de investigación | Solo revisiones y un estudio de asociación genética (PMID 25413361). Verificar el estado actual en ficha técnica y guías. |

El resto de las predicciones (por ejemplo, síndrome WHIM, displasia acromesomélica tipo Hunter-Thompson, miosclerosis) carecen de evidencia y de vínculo mecanístico (L5, Hold).

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 39681 | SALAZOPYRINA 500 MG COMPRIMIDOS (Pfizer S.L.) | Comprimido | No consta en el registro |

## Consideraciones de Seguridad

- **Interacciones farmacológicas / dianas registradas**: la consulta devolvió un solo registro, el transportador de folato acoplado a protones (SLC46A1). Es una diana farmacológica, no una interacción con otro medicamento, y no tiene nivel de gravedad asignado.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal (nivel L5) carece por completo de ensayos, literatura y vínculo mecanístico plausible. Los puntajes de TxGNN cercanos al 99% no bastan por sí solos para avanzar.

**Para avanzar se necesita:**
- Descartar esta indicación como candidata, o justificar un mecanismo específico antes de cualquier estudio.
- Priorizar las predicciones con respaldo preclínico (osteoartritis, espondiloartropatía) como preguntas de investigación. Para osteoartritis se necesitarían datos de eficacia en humanos. Para espondiloartropatía, confirmar el estado actual en ficha técnica y guías clínicas.
- Obtener el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones autorizadas), pues el cribado de seguridad no puede avanzar sin ellos.
- Completar los datos del mecanismo de acción (consulta a la API de DrugBank).

*Este informe es solo para fines de investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

