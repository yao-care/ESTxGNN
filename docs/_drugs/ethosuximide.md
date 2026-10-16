---
layout: default
title: Ethosuximide
parent: Solo predicción del modelo (L5)
nav_order: 315
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
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

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Etosuximida: De Epilepsia de Ausencia a Síndrome Nefrogénico de Antidiuresis Inapropiada

## Resumen en Una Frase

Etosuximida es un fármaco antiepiléptico utilizado originalmente para el tratamiento de la epilepsia de ausencia.
El modelo TxGNN predice que podría ser efectivo para el **síndrome nefrogénico de antidiuresis inapropiada (SNAI)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Epilepsia de ausencia |
| Nueva Indicación Predicha | Síndrome nefrogénico de antidiuresis inapropiada |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la etosuximida se describe generalmente como un bloqueador de los canales de calcio tipo T en las neuronas talámicas, y su eficacia en la epilepsia de ausencia está establecida. Esta descripción proviene de conocimiento general y no de los datos aportados.

El SNAI se asocia típicamente a variantes de ganancia de función del receptor V2 de la vasopresina (AVPR2), que provocan retención renal de agua independiente de la vasopresina. Con los datos disponibles, **no se puede establecer un vínculo mecanístico** entre el bloqueo de canales de calcio tipo T y la señalización de AVPR2 o el manejo renal del agua. Tampoco se ha evaluado la similitud entre la indicación original y la nueva (pendiente).

El puntaje de 0.9991 es solo una predicción computacional. No constituye evidencia clínica y puede reflejar la topología del grafo de conocimiento más que una relación biológica validada. La predicción debe interpretarse con mucha cautela.

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
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

