---
layout: default
title: Galantamine
parent: Solo predicción del modelo (L5)
nav_order: 368
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-31
description: "Galantamine: nueva indicación predicha, Trastornos psicógenos del movimiento (nivel de evidencia L5). Indicación original: Enfermedad de Alzheimer"
monitor_inn: "Galantamine"
predicted_indications: ["psychogenic movement disorders", "chronic tic disorder", "primary orthostatic tremor", "benign shuddering attacks", "extrapyramidal and movement disease", "tremor-nystagmus-duodenal ulcer syndrome", "lingual-facial-buccal dyskinesia", "benign paroxysmal tonic upgaze of childhood with ataxia", "acute intermittent porphyria"]
---

# Galantamine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Galantamina: De Enfermedad de Alzheimer a Trastornos Psicógenos del Movimiento
{: .text-alpha }

## Resumen en Una Frase

Galantamina es un inhibidor de la acetilcolinesterasa y modulador alostérico de los receptores nicotínicos, utilizado originalmente para el tratamiento de la enfermedad de Alzheimer.
El modelo TxGNN predice que podría ser efectivo para **trastornos psicógenos del movimiento**, aunque **no existen ensayos clínicos ni publicaciones** que respalden directamente esta predicción.
Entre las demás predicciones del modelo, la mejor respaldada indirectamente es la discinesia lingual-facial-bucal (discinesia tardía), con literatura de nivel L4.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Alzheimer (según las indicaciones originales registradas en el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Trastornos psicógenos del movimiento |
| Puntaje de Predicción TxGNN | 0.9990 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 16) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Según la información conocida, galantamina inhibe la acetilcolinesterasa (diana ACHE) y actúa además como modulador del receptor nicotínico de acetilcolina α7. Su eficacia en la enfermedad de Alzheimer leve a moderada ha sido comprobada, con un rendimiento comparable al de otros inhibidores de colinesterasa.

La relación con la nueva indicación es débil. Una posible vía sería la modulación colinérgica y nicotínica de los circuitos motores, pero no hay evidencia directa que la respalde. Los trastornos psicógenos del movimiento son afecciones funcionales sin una diana farmacológica establecida, por lo que la predicción se basa únicamente en el modelo TxGNN (aprendizaje profundo).

Cabe destacar que, entre las nueve predicciones evaluadas, la de **discinesia lingual-facial-bucal** (correspondiente a la discinesia tardía) es la que cuenta con más literatura indirecta: revisiones Cochrane sobre fármacos colinérgicos, estudios preclínicos y un ensayo cruzado aleatorizado de galantamina en discinesia tardía (PMID 17388711). Sin embargo, las revisiones Cochrane evalúan los fármacos colinérgicos en conjunto y no demuestran eficacia específica de galantamina. Esta línea merece una revisión focalizada de la literatura antes de diseñar cualquier ensayo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para trastornos psicógenos del movimiento.

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones vigentes, todas de principio activo único. Los textos de indicación aprobada no figuran en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 74331 | GALNORA 24 mg cápsulas duras de liberación prolongada EFG | Cápsula dura de liberación prolongada | No disponible |
| 66652 | REMINYL 24 mg cápsulas duras de liberación prolongada | Cápsula dura de liberación prolongada | No disponible |
| 74688 | GALANTAMINA VIATRIS 24 mg cápsulas duras de liberación prolongada EFG | Cápsula dura de liberación prolongada | No disponible |
| 63388 | REMINYL 4 mg/ml solución oral | Solución oral | No disponible |
| 77472 | GALANTAMINA TEVA-RATIO 16 mg cápsulas duras de liberación prolongada EFG | Cápsula dura de liberación prolongada | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no proceden del texto del prospecto): síndrome de QT largo familiar, insuficiencia hepática, enfermedad hepática, epilepsia, enfermedad pulmonar obstructiva crónica (incluida la de inicio precoz grave), enfermedad renal, piouréter, enfermedad de la vesícula biliar, úlcera péptica, úlcera duodenal, asma (intrínseca y alérgica), obstrucción del cuello vesical y bloqueo auriculoventricular.
- **Interacciones farmacológicas**: la consulta se completó y devolvió un único registro, correspondiente a la diana farmacológica principal (acetilcolinesterasa), sin interacciones medicamentosas específicas con otros fármacos.
- **Señal de seguridad relevante para la nueva indicación**: una revisión sistemática de 2025 (PMID 40224553) y un estudio de farmacovigilancia (PMID 24127392) señalan que los inhibidores de colinesterasa pueden inducir o empeorar trastornos del movimiento, incluido el síndrome de Pisa. Esto es especialmente importante al considerar su uso en trastornos del movimiento.
- Las advertencias y contraindicaciones del prospecto no se han podido consultar; se recomienda revisar el prospecto oficial.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal (trastornos psicógenos del movimiento) es solo computacional (L5), sin ensayos ni literatura, y existe una señal de seguridad de que los inhibidores de colinesterasa pueden empeorar los trastornos del movimiento. La dirección del efecto es incierta.

**Para avanzar se necesita:**
- Revisión focalizada de la literatura sobre galantamina en discinesia tardía, incluido el ensayo cruzado PMID 17388711, como candidata alternativa mejor respaldada (L4)
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), dado que es un vacío de datos bloqueante para el cribado de seguridad
- Datos detallados del mecanismo de acción (MOA) y análisis de similitud con la indicación original
- Evaluación de compatibilidad de vías de administración
- Evaluación del equilibrio riesgo-beneficio frente a la señal de trastornos del movimiento inducidos por inhibidores de colinesterasa
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

