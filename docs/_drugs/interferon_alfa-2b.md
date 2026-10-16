---
layout: default
title: Interferon Alfa-2B
parent: Solo predicción del modelo (L5)
nav_order: 423
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Interferon Alfa-2B: nueva indicación predicha, Esclerosis múltiple remitente-recurrente (nivel de evidencia L5). Indicación original: Infección anogenital por virus del papiloma humano"
monitor_inn: "INTERFERON ALFA-2B"
predicted_indications: ["relapsing-remitting multiple sclerosis"]
---

# Interferon Alfa-2B
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

# Interferón alfa-2b: De Infección Anogenital por Virus del Papiloma Humano a Esclerosis Múltiple Remitente-Recurrente

## Resumen en Una Frase

Interferón alfa-2b es un interferón de tipo I con actividad inmunomoduladora y antiviral, utilizado originalmente en la infección anogenital por virus del papiloma humano, la leucemia de células pilosas, el melanoma, el linfoma folicular, el sarcoma de Kaposi y las hepatitis crónicas B y C.
El modelo TxGNN predice que podría ser efectivo para la **esclerosis múltiple remitente-recurrente**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección anogenital por virus del papiloma humano (primera indicación original registrada en el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Esclerosis múltiple remitente-recurrente |
| Puntaje de Predicción TxGNN | 99.81% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Espana | ✓ Comercializado |
| Numero de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, el interferón alfa-2b es un interferón de tipo I con actividad inmunomoduladora y antiviral, y su eficacia en varias indicaciones oncológicas y virales ha sido establecida. Mecanísticamente podría ser aplicable a la esclerosis múltiple, aunque esto es una inferencia a partir de conocimiento general y no de los datos compilados para este informe.

Otros interferones de tipo I (interferón beta-1a e interferón beta-1b) son terapias modificadoras de la enfermedad establecidas para la esclerosis múltiple remitente-recurrente. Se cree que actúan a través del receptor compartido IFNAR, lo que podría reducir la activación de los linfocitos T, modificar el equilibrio de citocinas y limitar el paso de células inmunes a través de la barrera hematoencefálica. Esta plausibilidad a nivel de clase probablemente explica el puntaje tan alto de la predicción (0.998).

Sin embargo, es una predicción computacional. No existe evidencia clínica específica del interferón alfa-2b en esta enfermedad, y la farmacología de los subtipos alfa y beta no es intercambiable. Además, el interferón alfa se ha asociado con reportes de inducción o agravamiento de enfermedades autoinmunes y neurológicas, incluidos eventos desmielinizantes, por lo que el balance beneficio-riesgo es incierto.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 99127034 | INTRONA 30 millones de UI solución inyectable, pluma multidosis | Solución inyectable en pluma precargada | No disponible en los datos compilados |
| 99127031 | INTRONA 18 millones de UI solución inyectable, pluma multidosis | Solución inyectable en pluma precargada | No disponible en los datos compilados |
| 99127020 | INTRONA 10 millones de UI/ml solución inyectable o para perfusión | Solución inyectable y para perfusión | No disponible en los datos compilados |
| 99127037 | INTRONA 60 millones de UI solución inyectable, pluma multidosis | Solución inyectable en pluma precargada | No disponible en los datos compilados |

Las cuatro autorizaciones son de medicamento monofármaco, están vigentes y pertenecen a Merck Sharp & Dohme B.V.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (citocina; uso antineoplásico en leucemia de células pilosas, melanoma, linfoma folicular y sarcoma de Kaposi) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto (en general, hemograma y funciones hepática y renal) |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; a continuación se resumen las clasificadas como mayores entre las listadas:
  - **Mayores**: bupropión, deferiprona, iohexol, iopamidol, lexidronam de samario (153Sm) y eltrombopag.
  - **Moderadas** (selección): metronidazol, tinidazol, naltrexona, rosuvastatina, simvastatina, warfarina, dicumarol, cloroquina, disulfiram, palifermina, cloruro de estroncio Sr-89, ácido picosulfúrico, polietilenglicol (3350 con electrolitos) y sulfato de sodio.
- **Nota general**: el interferón alfa se ha asociado con reportes de inducción o agravamiento de enfermedades autoinmunes y neurológicas, incluidos eventos desmielinizantes. Esto es especialmente relevante para esta nueva indicación.

Para advertencias y contraindicaciones detalladas, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje TxGNN muy alto (99.81%), pero no hay ningún ensayo clínico ni publicación que la respalde (nivel L5). Además, el interferón alfa se asocia con posibles efectos autoinmunes y desmielinizantes, y los interferones beta ya cubren esta necesidad terapéutica, por lo que el balance beneficio-riesgo es incierto.

**Para avanzar se necesita:**
- Revisión sistemática de la literatura sobre interferón alfa en esclerosis múltiple, incluidos los reportes de eventos desmielinizantes
- Datos del mecanismo de acción (MOA) del interferón alfa-2b, para analizar el vínculo mecanístico
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), requisito previo para cualquier evaluación de seguridad
- Comparación farmacológica entre interferón alfa-2b e interferones beta (receptor, señalización, perfil de seguridad)
- Evidencia preclínica o clínica específica del interferón alfa-2b en esclerosis múltiple remitente-recurrente
- Evaluación de compatibilidad de vías de administración y de la similitud con las indicaciones originales
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

