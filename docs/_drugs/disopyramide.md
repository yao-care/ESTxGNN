---
layout: default
title: Disopyramide
parent: Solo predicción del modelo (L5)
nav_order: 257
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-05
monitor_inn: "disopyramide"
predicted_indications: ["Tourette syndrome", "attention deficit-hyperactivity disorder", "trichotillomania", "attention deficit hyperactivity disorder, inattentive type", "faciodigitogenital syndrome", "specific developmental disorder", "idiopathic neonatal atrial flutter", "chondromyxoid fibroma", "multifocal atrial tachycardia (disease)", "trigeminal nerve neoplasm"]
description: "Disopyramide: nueva indicación predicha, Síndrome de Tourette (Tourette syndrome) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 1 (comercializadas: 1)"
---

# Disopyramide
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

## Disopyramide: Síndrome de Tourette (Tourette syndrome)
{: .text-alpha }

## Resumen en Una Frase

Disopiramida es un antiarrítmico de clase Ia comercializado en España (DICORYNAN 100 mg cápsulas duras); en los datos compilados no figura el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de Tourette**, pero **no existe ningún ensayo clínico ni publicación** que respalde esta dirección: es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Síndrome de Tourette (Tourette syndrome) |
| Puntaje de Predicción TxGNN | 0.9986 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Disopyramide (traducción no oficial): «Norpace (fosfato de disopiramida) es un fármaco antiarrítmico de tipo 1 (es decir, similar a la procainamida y la quinidina). En estudios en animales, Norpace disminuye la velocidad de despolarización diastólica (fase 4) en células con automatismo aumentado, disminuye la velocidad de ascenso (fase 0) y aumenta la duración del potencial de acción de las células cardíacas normales, disminuye la disparidad en la refractariedad entre el miocardio infartado y el miocardio adyacente con perfusión normal, y no tiene efecto sobre los receptores alfa- ni beta-adrenérgicos.» Texto original en inglés: "Norpace (disopyramide phosphate) is a Type 1 antiarrhythmic drug (i.e., similar to procainamide and quinidine). In animal studies Norpace decreases the rate of diastolic depolarization (phase 4) in cells with augmented automaticity, decreases the upstroke velocity (phase 0) and increases the action potential duration of normal cardiac cells, decreases the disparity in refractoriness between infarcted and adjacent normally perfused myocardium, and has no effect on alpha- or beta-adrenergic receptors." ([DailyMed: Norpace (disopyramide phosphate) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e2aa1642-d262-4520-bc6a-9fd3ad795677), versión del 2026-08-24; consultado el 2026-11-19). Según la información conocida, disopiramida es un antiarrítmico de clase Ia: bloquea los canales de sodio y posee actividad anticolinérgica.

El síndrome de Tourette implica una disfunción de la dopamina y de los circuitos córtico-estriado-tálamo-corticales. No se ha identificado un vínculo mecanístico establecido entre ambos. El puntaje elevado procede del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica; carece de respaldo clínico o bibliográfico, por lo que debe interpretarse con mucha cautela.

Otras predicciones del modelo siguen el mismo patrón. Trastorno por déficit de atención e hiperactividad (TDAH, 0.9982), tricotilomanía (0.9981) y otros trastornos del neurodesarrollo carecen de mecanismo plausible. Las únicas con cierta plausibilidad farmacológica indirecta, por el efecto de clase antiarrítmica, son el flutter auricular neonatal idiopático y la taquicardia auricular multifocal (nivel L4). Ninguna cuenta con evidencia directa con disopiramida.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para el síndrome de Tourette.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 52549 | DICORYNAN 100 mg CAPSULAS DURAS (Cheplapharm Arzneimittel GmbH) | Cápsula dura | No especificada en los datos disponibles |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proviene del prospecto)**: síndrome de QT largo (incluido el familiar), bloqueo auriculoventricular, miocardiopatías (incluida la hipertrófica), miocarditis, fibrilación y flutter auricular, trastornos hipotensivos, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, deficiencia de potasio, hipoglucemia, hiperplasia prostática benigna, glaucoma de ángulo cerrado, miastenia gravis y enfermedades de la unión neuromuscular.
- **Interacciones Farmacológicas**: se registraron 258 interacciones. Entre las de gravedad **mayor** figuran claritromicina, citrato de potasio y ácido picosulfúrico. Hay numerosas de gravedad moderada, entre ellas corticoesteroides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida), anticolinérgicos (atropina, hioscina, glicopirronio, clidinio), anfotericina B, loperamida, aprepitant, bisacodilo, famotidina y clorpropamida. La cimetidina figura como interacción menor.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para el síndrome de Tourette se basa solo en el modelo (L5), sin ensayos ni publicaciones y sin mecanismo plausible. Además, el perfil de seguridad de la disopiramida (efectos proarrítmicos y anticolinérgicos) y su amplio número de interacciones hacen poco favorable explorar esta indicación sin un fundamento adicional.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS (advertencias y contraindicaciones oficiales) y la indicación aprobada.
- Completar los datos del mecanismo de acción.
- Realizar estudios preclínicos o una revisión sistemática que justifique un vínculo con la fisiopatología del síndrome de Tourette.
- Si se desea explorar una vía con mayor plausibilidad, priorizar las arritmias auriculares (flutter auricular neonatal idiopático, taquicardia auricular multifocal), que pueden considerarse preguntas de investigación (L4), valorando antes seguridad y dosificación en la población objetivo.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Norpace (disopyramide phosphate) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e2aa1642-d262-4520-bc6a-9fd3ad795677) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

