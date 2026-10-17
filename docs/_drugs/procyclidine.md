---
layout: default
title: Procyclidine
parent: Solo predicción del modelo (L5)
nav_order: 666
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Procyclidine: nueva indicación predicha, Encefalitis subaguda de Rasmussen (nivel de evidencia L5). Indicación original: Enfermedad de Parkinson y trastornos parkinsonianos (según el grafo d…"
monitor_inn: "procyclidine"
predicted_indications: ["Rasmussen subacute encephalitis", "myelitis", "PLA2G6-associated neurodegeneration", "attention deficit-hyperactivity disorder", "faciodigitogenital syndrome", "transaldolase deficiency", "progressive supranuclear palsy-corticobasal syndrome", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "fructose-1,6-bisphosphatase deficiency"]
---

# Procyclidine
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

# Procyclidina: De Enfermedad de Parkinson a Encefalitis Subaguda de Rasmussen

## Resumen en Una Frase

Procyclidina (procyclidina) es un anticolinérgico (antagonista muscarínico) comercializado en España como Kemadren 5 mg comprimidos, utilizado originalmente en la enfermedad de Parkinson y trastornos extrapiramidales afines.
El modelo TxGNN predice que podría ser efectivo para **encefalitis subaguda de Rasmussen**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Parkinson y trastornos parkinsonianos (según el grafo de conocimiento; el texto de indicación de la autorización de AEMPS no está disponible) |
| Nueva Indicación Predicha | Encefalitis subaguda de Rasmussen |
| Puntaje de Predicción TxGNN | 99,74% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, procyclidina es un antagonista de los receptores muscarínicos (anticolinérgico), cuya eficacia sintomática en parkinsonismo y distonías (incluidos distonía focal de la mano y blefaroespasmo) está reconocida.

La encefalitis de Rasmussen es una encefalitis crónica inmunomediada, dirigida por linfocitos T, con crisis focales. No se ha establecido un vínculo claro entre el bloqueo muscarínico y su fisiopatología. El puntaje elevado probablemente refleja la proximidad en la red del grafo a nodos de enfermedades neurológicas, más que una señal mecanística real.

Es una predicción puramente computacional, sin respaldo clínico ni bibliográfico, por lo que debe interpretarse con mucha cautela.

### Otras predicciones del modelo (todas L5, Hold)

| Rango | Enfermedad | Puntaje TxGNN | Comentario |
|---|---|---|---|
| 2 | Mielitis | 99,65% | Sin justificación mecanística; solo señal computacional |
| 3 | Neurodegeneración asociada a PLA2G6 | 99,63% | Posible relevancia sintomática (distonía-parkinsonismo); no modifica la enfermedad |
| 4 | Trastorno por déficit de atención e hiperactividad | 99,63% | Sin vínculo; los anticolinérgicos pueden empeorar la atención (riesgo) |
| 5 | Síndrome faciodigitogenital | 99,45% | Sin vínculo mecanístico plausible |
| 6 | Déficit de transaldolasa | 99,42% | Sin justificación mecanística |
| 7 | Síndrome de parálisis supranuclear progresiva-corticobasal | 99,42% | Solapamiento clínico; mala tolerabilidad de anticolinérgicos en esta población |
| 8 | Parálisis agitante juvenil de Hunt | 99,37% | Probablemente ya cubierta por la indicación original; baja novedad |
| 9 | Polimicrogiria perisilviana con hipoplasia cerebelosa y artrogriposis | 99,34% | Sin base mecanística |
| 10 | Déficit de fructosa-1,6-bisfosfatasa | 99,34% | Sin justificación mecanística |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 38206 | KEMADREN 5 mg COMPRIMIDOS (Aspen Pharma Trading Limited) | Comprimido | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no según el prospecto)**: hipertensión, úlcera gástrica, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, hiperplasia prostática benigna, enfermedad coronaria, glaucoma de ángulo cerrado, miastenia gravis y enfermedades de la unión neuromuscular, colitis ulcerosa y enfermedad inflamatoria intestinal, acalasia y megaesófago, estenosis pilórica, hipertiroidismo (enfermedad de Graves, tirotoxicosis), hernia de hiato, íleo paralítico y obstrucción intestinal, obstrucción del cuello vesical, megacolon tóxico, entre otras.
- **Interacciones farmacológicas**: se identificaron 70 interacciones. Las de mayor gravedad (**Mayor**) son con **cloruro de potasio** y **citrato de potasio**. Las de gravedad moderada incluyen otros anticolinérgicos/antimuscarínicos (hiosciamina, atropina, glicopirronio, diciclomina, trospio, metescopolamina, clidinio, mepenzolato), opioides (morfina, opio, loperamida, eluxadolina), cannabinoides (dronabinol, nabilona), metoclopramida y pramlintida. Predomina el riesgo de efecto anticolinérgico aditivo.
- Las advertencias y contraindicaciones del prospecto de AEMPS no estaban disponibles. Consultar el prospecto para la información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para encefalitis de Rasmussen se basa solo en el puntaje del modelo (nivel L5), sin ensayos, literatura ni vínculo mecanístico plausible. Además, el perfil anticolinérgico y las numerosas contraindicaciones aconsejan no avanzar sin respaldo adicional.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias, contraindicaciones e indicación aprobada), requisito bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión sistemática de literatura y de registros de ensayos sobre procyclidina/anticolinérgicos en encefalitis de Rasmussen.
- Evaluar si, entre las predicciones, la neurodegeneración asociada a PLA2G6 (uso sintomático en distonía-parkinsonismo) merece priorización como alternativa más plausible biológicamente.
- Evaluar la viabilidad de vía de administración y la compatibilidad de la población diana.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

