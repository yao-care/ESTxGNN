---
layout: default
title: Anakinra
parent: Solo predicción del modelo (L5)
nav_order: 57
evidence_level: L5
indication_count: 9
monitor_inn: "ANAKINRA"
predicted_indications: ["extracutaneous mastocytoma", "hepatic infarction", "aggressive systemic mastocytosis", "hepatic veno-occlusive disease", "peliosis hepatis", "oligoarticular juvenile idiopathic arthritis without anti-nuclear antibodies", "oligoarticular juvenile idiopathic arthritis with anti-nuclear antibodies", "pyogenic autoinflammatory syndrome", "unclassified autoinflammatory syndrome"]
last_modified_at: 2026-11-20
description: "Anakinra: nueva indicación predicha, mastocitoma extracutáneo (extracutaneous mastocytoma) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 1 (comercializadas: 1)"
---

# Anakinra
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

## Anakinra: antagonista del receptor de IL-1 → mastocitoma extracutáneo (extracutaneous mastocytoma)
{: .text-alpha }

## Resumen en Una Frase

Anakinra es un antagonista del receptor de la interleucina-1 (IL-1) que se comercializa en España.
El modelo TxGNN predice que podría ser efectivo para **mastocitoma extracutáneo (extracutaneous mastocytoma)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | mastocitoma extracutáneo (extracutaneous mastocytoma) |
| Puntaje de Predicción TxGNN | 0.9993 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Anakinra (traducción no oficial): «KINERET bloquea la actividad biológica de la IL-1 alfa y beta mediante la inhibición competitiva de la unión de la IL-1 al receptor de interleucina-1 de tipo I (IL-1RI), que se expresa en una amplia variedad de tejidos y órganos. La producción de IL-1 se induce en respuesta a estímulos inflamatorios y media diversas respuestas fisiológicas, incluidas las respuestas inflamatorias e inmunitarias.» Texto original en inglés: "KINERET blocks the biologic activity of IL-1 alpha and beta by competitively inhibiting IL-1 binding to the interleukin-1 type I receptor (IL-1RI), which is expressed in a wide variety of tissues and organs. IL-1 production is induced in response to inflammatory stimuli and mediates various physiologic responses including inflammatory and immunological responses." ([DailyMed: Kineret (anakinra) prescribing information, Swedish Orphan Biovitrum AB (publ)](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d9d74915-6606-4570-9c52-c4001d3177de), versión del 2026-04-03; consultado el 2026-11-19). Por su clase, anakinra bloquea el receptor de la IL-1, una citocina central en la inflamación local y sistémica, y se usa en enfermedades autoinflamatorias mediadas por IL-1.

La señalización de IL-1 podría tener un papel teórico en la inflamación dependiente de mastocitos. Sin embargo, los datos compilados para este informe no documentan un vínculo directo entre anakinra y el mastocitoma extracutáneo.

Por ello, la predicción debe considerarse una hipótesis de trabajo: la puntuación es alta, pero no existe ningún estudio real que la sustente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 102203006 | KINERET 100 mg/0,67 ml solución inyectable en jeringa precargada | Solución inyectable | No registrada en los datos locales |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (100 interacciones identificadas; se muestran las principales):
  - **Mayor**: deferiprona.
  - **Moderada**: corticoides (hidrocortisona, betametasona, budesonida, dexametasona, prednisolona, prednisona, triamcinolona), simvastatina, apixabán, dicumarol, rivaroxabán, ibritumomab tiuxetán, iobenguano (I-131), tositumomab y tositumomab (I-131).
  - **Menor**: sales de zinc (acetato, gluconato, sulfato).

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para mastocitoma extracutáneo carece de ensayos clínicos y de literatura, por lo que se queda en el nivel L5 y no justifica avanzar por ahora.

**Para avanzar se necesita:**
- Estudios preclínicos o series de casos que evalúen el bloqueo de IL-1 en mastocitoma extracutáneo
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones)
- Revisión de la plausibilidad biológica por parte de especialistas antes de cualquier estudio clínico

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Kineret (anakinra) prescribing information, Swedish Orphan Biovitrum AB (publ)](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d9d74915-6606-4570-9c52-c4001d3177de) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

