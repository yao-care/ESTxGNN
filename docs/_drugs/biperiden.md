---
layout: default
title: Biperiden
parent: Solo predicción del modelo (L5)
nav_order: 107
evidence_level: L5
indication_count: 10
---

# Biperiden
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

# Biperideno: De Enfermedad de Parkinson a Encefalitis Subaguda de Rasmussen

## Resumen en Una Frase

Biperideno es un anticolinérgico muscarínico, utilizado originalmente para el tratamiento de la enfermedad de Parkinson y de los síndromes parkinsonianos.
El modelo TxGNN predice que podría ser efectivo para la **encefalitis subaguda de Rasmussen**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Parkinson y síndromes parkinsonianos (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Encefalitis subaguda de Rasmussen |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado. Según la información conocida, biperideno es un anticolinérgico antagonista de los receptores muscarínicos, con selectividad por M1. Los datos farmacológicos compilados lo vinculan con los receptores M1, M2, M3, M4 y M5. Su uso clínico consiste en aliviar la rigidez muscular, la sudoración y la salivación, y en mejorar la marcha y el temblor en el síndrome parkinsoniano.

La encefalitis de Rasmussen es una encefalitis crónica de origen inmunitario, mediada por linfocitos T, que cursa con crisis focales. No existe un vínculo establecido entre esta enfermedad y el antagonismo muscarínico. Cualquier justificación sería especulativa (por ejemplo, la modulación de circuitos colinérgicos implicados en las crisis).

Por tanto, la predicción parece reflejar sobre todo la proximidad en el grafo de conocimiento y no una base mecanística sólida. Incluso si hubiera algún efecto, sería a lo sumo sintomático y no modificador de la enfermedad.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 28994 | AKINETON 5 mg/ml solución inyectable | Solución inyectable | No disponible en los datos compilados |
| 26692 | AKINETON 2 mg comprimidos | Comprimido | No disponible en los datos compilados |
| 51224 | AKINETON RETARD 4 mg comprimidos de liberación prolongada | Comprimido de liberación prolongada | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento** (no proceden del texto del prospecto; deben verificarse con la ficha técnica): glaucoma de ángulo abierto y de ángulo cerrado, hiperplasia benigna de próstata, miastenia gravis y enfermedades de la unión neuromuscular, íleo paralítico, acalasia/megaesófago, hernia de hiato, colitis ulcerosa y enfermedad inflamatoria intestinal, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal, enfermedad pulmonar obstructiva crónica, hipertensión e hipotensión, enfermedad coronaria, parada cardíaca súbita y enfermedad de la conducción cardíaca, úlcera gástrica, y enfermedad renal, hepática o de la vesícula biliar.
- **Interacciones farmacológicas**: los datos compilados no incluyen interacciones fármaco-fármaco clínicas, solo la afinidad por los receptores muscarínicos M1 a M5.

Consultar el prospecto para la información de seguridad oficial (advertencias y contraindicaciones), ya que no se dispone del texto de AEMPS.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (99.94%), pero no cuenta con ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible entre el antagonismo muscarínico y una encefalitis inmunomediada. Por ello, el nivel de evidencia es L5.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), pendiente para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión de literatura dirigida y estudios preclínicos que evalúen la relación entre la señalización colinérgica muscarínica y las crisis o la neuroinflamación en la encefalitis de Rasmussen.
- Considerar candidatas alternativas con mayor plausibilidad clínica entre las otras predicciones. Por ejemplo, el parkinsonismo juvenil de Hunt, la neurodegeneración asociada a PLA2G6 y el síndrome de parálisis supranuclear progresiva-corticobasal son extensiones sintomáticas cercanas a la indicación original, aunque tampoco tienen ensayos ni literatura específica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

