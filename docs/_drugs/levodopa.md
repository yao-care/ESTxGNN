---
layout: default
title: Levodopa
parent: Solo predicción del modelo (L5)
nav_order: 466
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
monitor_inn: "LEVODOPA"
predicted_indications: ["Rasmussen subacute encephalitis"]
description: "Levodopa: nueva indicación predicha, Encefalitis subaguda de Rasmussen (Rasmussen subacute encephalitis) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 1 (comercializadas: 1)"
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

## Levodopa: Encefalitis subaguda de Rasmussen (Rasmussen subacute encephalitis)
{: .text-alpha }

## Resumen en Una Frase

Levodopa es un precursor de la dopamina, utilizado originalmente para el tratamiento de la enfermedad de Parkinson y de otros síndromes parkinsonianos.
El modelo TxGNN predice que podría ser efectivo para la **encefalitis subaguda de Rasmussen**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: la predicción se basa únicamente en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Encefalitis subaguda de Rasmussen (Rasmussen subacute encephalitis) |
| Puntaje de Predicción TxGNN | 0.9906 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Levodopa (traducción no oficial): «La levodopa, el precursor metabólico de la dopamina, atraviesa la barrera hematoencefálica y presumiblemente se convierte en dopamina en el cerebro. Se cree que este es el mecanismo por el cual la levodopa alivia los síntomas de la enfermedad de Parkinson.» Texto original en inglés: "Levodopa, the metabolic precursor of dopamine, crosses the blood-brain barrier and presumably is converted to dopamine in the brain. This is thought to be the mechanism whereby levodopa relieves symptoms of Parkinson's disease." ([DailyMed: Inbrija (levodopa) prescribing information, Merz Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=077c0f39-a3a2-4b2b-a184-09131889dcfb), versión del 2026-07-20; consultado el 2026-11-19). Según la información conocida, levodopa es un precursor de la dopamina que actúa sobre la neurotransmisión dopaminérgica, y su eficacia en la enfermedad de Parkinson y en síndromes parkinsonianos relacionados está bien establecida.

La encefalitis de Rasmussen es una enfermedad inflamatoria cerebral rara, crónica y unilateral, mediada por linfocitos T, con atrofia hemisférica progresiva y epilepsia focal refractaria. No se ha establecido un vínculo mecanístico directo con levodopa. Una conexión meramente especulativa podría estar en rasgos compartidos de los ganglios basales o de los trastornos del movimiento, ya que algunos pacientes desarrollan hemiparesia o distonía.

Sin embargo, la reposición de dopamina no actúa sobre la patología inmunomediada ni sobre las crisis epilépticas. Es probable que el puntaje elevado provenga del modelo TxGNN (aprendizaje profundo) y refleje similitudes que el modelo aprendió entre enfermedades relacionadas, como el síndrome de hemiparkinsonismo-hemiatrofia y otros trastornos parkinsonianos, y no evidencia biológica.

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
La predicción se apoya solo en el puntaje del modelo TxGNN (aprendizaje profundo, nivel L5), que puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica; no hay ensayos clínicos ni literatura, ni un vínculo mecanístico plausible, y la epilepsia figura como contraindicación.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), pues su ausencia impide el cribado de seguridad.
- Completar los datos del mecanismo de acción de levodopa (por ejemplo, desde DrugBank).
- Realizar una revisión de literatura y de registros de ensayos sobre dopaminérgicos en encefalitis de Rasmussen.
- Evaluar la compatibilidad de la vía de administración: la única presentación autorizada es inhalatoria (Inbrija) y no se ha determinado su idoneidad para esta indicación.
- Generar evidencia preclínica o mecanística que justifique un vínculo biológico antes de reconsiderar la decisión.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Inbrija (levodopa) prescribing information, Merz Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=077c0f39-a3a2-4b2b-a184-09131889dcfb) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

