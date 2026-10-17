---
layout: default
title: Levodopa
parent: Solo predicción del modelo (L5)
nav_order: 466
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Levodopa: nueva indicación predicha, Encefalitis subaguda de Rasmussen (nivel de evidencia L5). Indicación original: Enfermedad de Parkinson y síndromes parkinsonianos relacionados (segú…"
monitor_inn: "LEVODOPA"
predicted_indications: ["Rasmussen subacute encephalitis"]
---

# Levodopa
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Levodopa: De Enfermedad de Parkinson a Encefalitis Subaguda de Rasmussen

## Resumen en Una Frase

Levodopa es un precursor de la dopamina, utilizado originalmente para el tratamiento de la enfermedad de Parkinson y de otros síndromes parkinsonianos.
El modelo TxGNN predice que podría ser efectivo para la **encefalitis subaguda de Rasmussen**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: la predicción se basa únicamente en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Parkinson y síndromes parkinsonianos relacionados (según el grafo de conocimiento; el texto de indicación de la autorización no está disponible) |
| Nueva Indicación Predicha | Encefalitis subaguda de Rasmussen |
| Puntaje de Predicción TxGNN | 99,06% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Según la información conocida, levodopa es un precursor de la dopamina que actúa sobre la neurotransmisión dopaminérgica, y su eficacia en la enfermedad de Parkinson y en síndromes parkinsonianos relacionados está bien establecida.

La encefalitis de Rasmussen es una enfermedad inflamatoria cerebral rara, crónica y unilateral, mediada por linfocitos T, con atrofia hemisférica progresiva y epilepsia focal refractaria. No se ha establecido un vínculo mecanístico directo con levodopa. Una conexión meramente especulativa podría estar en rasgos compartidos de los ganglios basales o de los trastornos del movimiento, ya que algunos pacientes desarrollan hemiparesia o distonía.

Sin embargo, la reposición de dopamina no actúa sobre la patología inmunomediada ni sobre las crisis epilépticas. Es probable que el puntaje elevado se deba a la cercanía en el grafo de conocimiento con el síndrome de hemiparkinsonismo-hemiatrofia y otros trastornos parkinsonianos, y no a evidencia biológica.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1191390002 | INBRIJA 33 MG POLVO PARA INHALACIÓN CÁPSULAS DURAS | Polvo para inhalación (cápsula dura) | Texto de indicación no disponible |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): atrofia multisistémica, síndrome de taquicardia postural ortostática, hipotensión ortostática, discinesia inducida por fármacos, epilepsia, úlcera gástrica y péptica, trastornos de ansiedad, neuróticos y distímicos, enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, glaucoma de ángulo abierto y de ángulo cerrado, trastornos psicóticos (incluidos esquizofreniforme y esquizoafectivo), trastorno mental, diabetes mellitus, cetoacidosis diabética, melanoma, infarto de miocardio, trombosis coronaria, hemoglobinopatía, enfermedad diarreica, paro cardíaco súbito y enfermedad de la conducción cardíaca.
  - Cabe destacar la **epilepsia**, relevante porque la encefalitis de Rasmussen cursa con epilepsia focal refractaria.
- **Interacciones farmacológicas** (se identificaron 100 en total; se muestran las principales):
  - Moderadas: epinefrina, efedrina, bupropión, metronidazol, piridoxina, metoclopramida y anticolinérgicos (atropina, hiosciamina, metescopolamina, glicopirronio, clidinio, diciclomina, mepenzolato).
  - Menores: antiácidos con aluminio, calcio o magnesio (hidróxido de aluminio, carbonato de calcio, magaldrato, carbonato, hidróxido y óxido de magnesio).
  - Moderada: hierro.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura, sin vínculo mecanístico plausible y con la epilepsia señalada como contraindicación en el grafo de conocimiento.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), pues su ausencia impide el cribado de seguridad.
- Completar los datos del mecanismo de acción de levodopa (por ejemplo, desde DrugBank).
- Realizar una revisión de literatura y de registros de ensayos sobre dopaminérgicos en encefalitis de Rasmussen.
- Evaluar la compatibilidad de la vía de administración: la única presentación autorizada es inhalatoria (Inbrija) y no se ha determinado su idoneidad para esta indicación.
- Generar evidencia preclínica o mecanística que justifique un vínculo biológico antes de reconsiderar la decisión.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

