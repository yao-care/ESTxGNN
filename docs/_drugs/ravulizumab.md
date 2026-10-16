---
layout: default
title: Ravulizumab
parent: Solo predicción del modelo (L5)
nav_order: 686
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ravulizumab: nueva indicación predicha, Neutropenia congénita grave autosómica recesiva por deficiencia de G6… (nivel de evidencia L5). Indicación original: Hemoglobinuria paroxística nocturna (según…"
---

# Ravulizumab
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

# Ravulizumab: De Hemoglobinuria Paroxística Nocturna a Neutropenia Congénita Grave Autosómica Recesiva por Deficiencia de G6PC3

## Resumen en Una Frase

Ravulizumab es un inhibidor del componente C5 del complemento, originalmente utilizado para el tratamiento de la hemoglobinuria paroxística nocturna (HPN).
El modelo TxGNN predice que podría ser efectivo para **neutropenia congénita grave autosómica recesiva por deficiencia de G6PC3**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hemoglobinuria paroxística nocturna (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Neutropenia congénita grave autosómica recesiva por deficiencia de G6PC3 |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Ravulizumab es un anticuerpo monoclonal que inhibe el componente C5 del complemento terminal. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Por su clase farmacológica, su eficacia en la HPN, una enfermedad de hemólisis intravascular mediada por complemento, es conocida.

La relación entre la indicación original y la nueva es débil. La deficiencia de G6PC3 es un defecto metabólico y de maduración mieloide sin patología conocida dirigida por el complemento. El vínculo mecanístico proviene únicamente del grafo de conocimiento y no cuenta con respaldo mecanístico ni clínico.

Por ello, la alta puntuación del modelo (99.96%) debe interpretarse con cautela: no hay una justificación biológica establecida para que la inhibición de C5 sea aplicable a esta enfermedad. Otras predicciones del mismo análisis (neutropenia cíclica, hiperoxaluria primaria, neutropenia congénita grave, entre otras) presentan igualmente evidencia de nivel L5 y recomendación Hold.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1191371003 | ULTOMIRIS 1100 mg/11 ml concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos compilados |
| 1191371002 | ULTOMIRIS 300 mg/3 ml concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones (grafo de conocimiento)**: infección meningocócica. Este dato procede de las relaciones fármaco-enfermedad del grafo de conocimiento, no del texto del prospecto.
- **Interacciones Farmacológicas**: se identificaron 4 interacciones de nivel menor, todas con inmunoglobulina G humana (intravenosa, subcutánea, intramuscular e intravenosa/subcutánea).

Para el resto de la información de seguridad, consultar el prospecto. Cabe señalar que la inhibición del complemento terminal conlleva un riesgo de infección meningocócica, que sería especialmente relevante en poblaciones con inmunodeficiencia o neutropenia.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa exclusivamente en el modelo (nivel L5), sin ensayos clínicos, literatura ni racional mecanístico que vincule la inhibición de C5 con la deficiencia de G6PC3. Además, el riesgo de infecciones graves por inhibición del complemento sería preocupante en pacientes neutropénicos.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y evidencia preclínica que relacione el complemento con la fisiopatología de la deficiencia de G6PC3
- Texto de las advertencias y contraindicaciones del prospecto de AEMPS
- Texto de las indicaciones aprobadas en las autorizaciones españolas
- Evaluación de la compatibilidad de vía de administración y de la similitud con la indicación original
- Un plan de seguridad que contemple el riesgo de infección meningocócica y de infecciones en pacientes neutropénicos
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

