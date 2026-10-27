---
layout: default
title: Pentostatin
parent: Solo predicción del modelo (L5)
nav_order: 624
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Pentostatin: nueva indicación predicha, Rabdomiosarcoma embrionario botrioide de vagina (nivel de evidencia L5). Indicación original: Leucemia de células peludas (según el grafo de conocimiento"
monitor_inn: "pentostatin"
predicted_indications: ["botryoid-type embryonal rhabdomyosarcoma of the vagina", "parameningeal embryonal rhabdomyosarcoma", "rhabdomyosarcoma (disease)", "embryonal extrahepatic bile duct rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma", "liver sarcoma"]
---

# Pentostatin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

## Pentostatina: De Leucemia de Células Peludas a Rabdomiosarcoma Embrionario Botrioide de Vagina
{: .text-alpha }

## Resumen en Una Frase

Pentostatina es un inhibidor de la adenosina desaminasa (ADA), utilizado originalmente para el tratamiento de la leucemia de células peludas y su variante.
El modelo TxGNN predice que podría ser efectivo para **rabdomiosarcoma embrionario botrioide de vagina**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Leucemia de células peludas (según el grafo de conocimiento; el texto de indicación de la autorización de AEMPS está vacío) |
| Nueva Indicación Predicha | Rabdomiosarcoma embrionario botrioide de vagina |
| Puntaje de Predicción TxGNN | 99.54% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, la pentostatina inhibe la adenosina desaminasa (ADA), lo que provoca la depleción de linfocitos y la alteración del metabolismo de las purinas. Su eficacia en la leucemia de células peludas, una neoplasia linfoide, está establecida.

La relación con la nueva indicación es débil. El rabdomiosarcoma embrionario botrioide de vagina es un tumor sólido pediátrico, biológicamente distinto de las neoplasias linfoides. Los datos compilados no respaldan un vínculo mecanístico entre la inhibición de ADA y la biología de este tumor. Una hipótesis general es que la alteración del metabolismo de purinas podría afectar a células tumorales de proliferación rápida, pero no está validada.

El puntaje elevado (0.995) es una predicción basada en grafos y probablemente refleja la cercanía en la ontología de enfermedades, no biología específica del fármaco. Las otras seis predicciones principales (rabdomiosarcoma parameníngeo, rabdomiosarcoma en general, rabdomiosarcoma de vías biliares extrahepáticas en dos variantes, rabdomiosarcoma embrionario de próstata y sarcoma hepático) tampoco cuentan con ensayos ni literatura.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 59993 | NIPENT 10 mg polvo para solución inyectable y para perfusión (Pfizer S.L.) | Polvo para solución inyectable y para perfusión | No disponible en los datos compilados |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (análogo de purinas, inhibidor de ADA) |
| Riesgo de Mielosupresión | Alto, de acuerdo con la lista de enfermedades contraindicadas del grafo de conocimiento (neutropenia, trombocitopenia, leucopenia, anemia, agranulocitosis); consultar el prospecto para detalles |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal; vigilancia de infecciones |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

- **Contraindicaciones / condiciones de riesgo (grafo de conocimiento, no texto del prospecto)**: enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, neutropenia, agranulocitosis, leucopenia, anemia (incluida la macrocítica), enfermedades infecciosas, trastornos hipotensivos, edema pulmonar y piouréter.
- **Interacciones Farmacológicas**: se identificaron 138 interacciones en total. Entre las de nivel **Mayor** figuran deferiprona, samario (153Sm) lexidronam, adalimumab y baricitinib. Entre las de nivel **Moderado**: palifermina, cloruro de estroncio Sr-89, mercaptopurina, roflumilast, cloranfenicol, zidovudina, aldesleukina, alefacept, alemtuzumab, anakinra, azatioprina y algunas vacunas (toxoide tetánico, ántrax). Entre las de nivel **Menor**: levofloxacino y alopurinol.

Las advertencias y contraindicaciones del prospecto de AEMPS no estaban disponibles; consultar el prospecto para información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico respaldado entre la inhibición de ADA y el rabdomiosarcoma. Además, el perfil de seguridad (mielosupresión, inmunosupresión y numerosas interacciones) exige cautela.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consultar DrugBank) y análisis del vínculo mecanístico con el rabdomiosarcoma
- Revisión de la literatura y de registros de ensayos sobre pentostatina en sarcomas
- Estudios preclínicos en modelos de rabdomiosarcoma
- Descarga y análisis del prospecto de AEMPS (advertencias y contraindicaciones)
- Evaluación de la compatibilidad de vía de administración y de la similitud con la indicación original
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

