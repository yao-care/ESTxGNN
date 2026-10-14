---
layout: default
title: Amantadine
parent: Solo predicción del modelo (L5)
nav_order: 46
evidence_level: L5
indication_count: 4
---

# Amantadine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Amantadina: De Enfermedad de Parkinson a Encefalitis Subaguda de Rasmussen

## Resumen en Una Frase

La amantadina es un fármaco utilizado originalmente para el tratamiento de la enfermedad de Parkinson y otros trastornos extrapiramidales.
El modelo TxGNN predice que podría ser efectiva para la **encefalitis subaguda de Rasmussen**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Parkinson (según el grafo de conocimiento; el texto de indicación de la autorización española no está disponible) |
| Nueva Indicación Predicha | Encefalitis subaguda de Rasmussen |
| Puntaje de Predicción TxGNN | 99.48% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Según la información farmacológica conocida, la amantadina actúa como antagonista de los receptores NMDA (con interacción descrita con las subunidades GluN2A, GluN2B, GluN2C y GluN2D) y modula la transmisión dopaminérgica. Su eficacia en la enfermedad de Parkinson y en la discinesia asociada a levodopa está documentada.

La encefalitis de Rasmussen es una enfermedad inflamatoria cerebral de base inmunomediada, con lesión neuronal excitotóxica relacionada con el glutamato y crisis focales intratables. Desde un punto de vista teórico, el antagonismo NMDA podría tener relevancia en ese componente excitotóxico.

No obstante, este vínculo es solo hipotético. No hay ensayos ni literatura que lo respalden, y la similitud con la indicación original no ha podido evaluarse. La predicción debe considerarse no verificada.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 44541 | AMANTADINE LEVEL 100 mg CÁPSULAS DURAS (Laboratorios Ern S.A.) | Cápsula dura | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad, no texto del prospecto): atrofia multisistémica, síndrome de taquicardia postural ortostática, hipotensión ortostática, epilepsia, enfermedad renal, piouréter, insuficiencia cardíaca congestiva, trastorno psicótico, trastorno esquizofreniforme, trastorno mental, trastorno esquizoafectivo, melanoma, glaucoma de ángulo cerrado, trastornos relacionados con sustancias y abuso/dependencia, eccema atópico y dermatitis.
- **Interacciones farmacológicas**: la consulta se completó con 4 registros, todos de farmacología de dianas (no interacciones con otros fármacos): la amantadina actúa sobre las subunidades de receptor NMDA GluN2A, GluN2B, GluN2C y GluN2D.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (puntaje alto, pero sin ensayos clínicos ni literatura), el mecanismo de acción original no está documentado y la información del prospecto no está disponible. Además, la epilepsia figura entre las contraindicaciones del grafo de conocimiento, lo que es relevante para una enfermedad caracterizada por crisis focales.

**Para avanzar se necesita:**
- Obtener el prospecto oficial de la AEMPS (advertencias, contraindicaciones e indicación aprobada).
- Completar los datos de mecanismo de acción desde DrugBank.
- Realizar una revisión de literatura específica sobre antagonistas NMDA en encefalitis de Rasmussen y estudios preclínicos.
- Evaluar la contraindicación en epilepsia frente al contexto de crisis intratables.
- Si se desea explorar otras predicciones, la mielitis (síndrome pospolio, con un ensayo doble ciego de 1995 sobre fatiga, evidencia indirecta, nivel L4) y la neurodegeneración asociada a PLA2G6 (un reporte de caso en PKAN, evidencia indirecta, nivel L4) cuentan con algo más de respaldo bibliográfico, aunque ambas siguen siendo preguntas de investigación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

