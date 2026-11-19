---
layout: default
title: Ethosuximide
parent: Solo predicción del modelo (L5)
nav_order: 315
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
description: "Ethosuximide: nueva indicación predicha, Síndrome nefrogénico de antidiuresis inapropiada (nivel de evidencia L5). Indicación original: Epilepsia de ausencia"
monitor_inn: "ethosuximide"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
---

# Ethosuximide
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

## Etosuximida: De Epilepsia de Ausencia a Síndrome Nefrogénico de Antidiuresis Inapropiada
{: .text-alpha }

## Resumen en Una Frase

Etosuximida es un fármaco antiepiléptico utilizado originalmente para el tratamiento de la epilepsia de ausencia.
El modelo TxGNN predice que podría ser efectivo para el **síndrome nefrogénico de antidiuresis inapropiada (SNAI)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Epilepsia de ausencia |
| Nueva Indicación Predicha | Síndrome nefrogénico de antidiuresis inapropiada |
| Puntaje de Predicción TxGNN | 0.9991 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 2; revocadas o suspendidas: 1) |
| Número de Autorizaciones | 2 (comercializadas: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Ethosuximide (traducción no oficial): «La etosuximida suprime la actividad paroxística de punta-onda de tres ciclos por segundo asociada a lapsos de conciencia, que es frecuente en las crisis de ausencia (pequeño mal). La frecuencia de los ataques epileptiformes se reduce, aparentemente mediante la depresión de la corteza motora y la elevación del umbral del sistema nervioso central a los estímulos convulsivos.» Texto original en inglés: "Ethosuximide suppresses the paroxysmal three cycle per second spike and wave activity associated with lapses of consciousness which is common in absence (petit mal) seizures. The frequency of epileptiform attacks is reduced, apparently by depression of the motor cortex and elevation of the threshold of the central nervous system to convulsive stimuli." ([DailyMed: Zarontin (ethosuximide) prescribing information, Parke-Davis Div of Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0e008f33-70a1-4bc6-b3a0-d45214418ab6), versión del 2026-05-25; consultado el 2026-11-19). Según la información conocida, la etosuximida se describe generalmente como un bloqueador de los canales de calcio tipo T en las neuronas talámicas, y su eficacia en la epilepsia de ausencia está establecida. Esta descripción proviene de conocimiento general y no de los datos aportados.

El SNAI se asocia típicamente a variantes de ganancia de función del receptor V2 de la vasopresina (AVPR2), que provocan retención renal de agua independiente de la vasopresina. Con los datos disponibles, **no se puede establecer un vínculo mecanístico** entre el bloqueo de canales de calcio tipo T y la señalización de AVPR2 o el manejo renal del agua. Tampoco se ha evaluado la similitud entre la indicación original y la nueva (pendiente).

El puntaje de 0.9991 proviene del modelo TxGNN (aprendizaje profundo) y es solo una predicción computacional. No constituye evidencia clínica y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. La predicción debe interpretarse con mucha cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 42250 | ETOSUXIMIDA FAES 250 mg CÁPSULAS DURAS | Cápsula dura | No disponible en los datos compilados |
| 37828 | ZARONTIN 50 mg/ml SOLUCIÓN ORAL | Jarabe | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad, no texto del prospecto): trastorno de ansiedad, trastorno neurótico, trastorno distímico, enfermedad renal, piouréter, enfermedad hematológica, enfermedad hepática, enfermedad de la vesícula biliar, lupus eritematoso sistémico (incluido el pediátrico), neutropenia, agranulocitosis y porfiria aguda intermitente.
- **Interacciones farmacológicas**: se identificaron 92 interacciones en total. Entre las de nivel moderado se incluyen aprepitant, morfina (y morfina liposomal), opio, dronabinol, nabilona, metoclopramida, sibutramina, etanol, cobicistat, ácido fólico, levofolinato, folinato (leucovorina), deferasirox, prometazina, fostamatinib, cloroquina, mefloquina, hidroxicloroquina y clorfenamina.

Las advertencias principales y contraindicaciones del prospecto de la AEMPS no están disponibles; consultar el prospecto para completar la información de seguridad. Dado el perfil de contraindicaciones (enfermedad renal y hematológica), es especialmente relevante revisarlo antes de considerar un uso en un trastorno de origen renal.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible con los datos disponibles. Además, falta la información de seguridad del prospecto y el grafo señala contraindicaciones renales.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consulta a DrugBank) y análisis de su posible relación con la fisiopatología del SNAI (AVPR2)
- Descarga y análisis del prospecto de la AEMPS (advertencias y contraindicaciones) para el cribado de seguridad
- Revisión de literatura preclínica y de casos que apoye la hipótesis
- Evaluación de la compatibilidad de vías de administración y de la similitud con la indicación original
- Evaluar la seguridad en pacientes con compromiso renal, dadas las contraindicaciones señaladas

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Zarontin (ethosuximide) prescribing information, Parke-Davis Div of Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0e008f33-70a1-4bc6-b3a0-d45214418ab6) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

