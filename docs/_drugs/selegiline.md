---
layout: default
title: Selegiline
parent: Solo predicción del modelo (L5)
nav_order: 728
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-20
monitor_inn: "Selegiline"
predicted_indications: ["polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "schizophrenia", "congenital disorder of glycosylation with defective fucosylation", "retinal dystrophy with or without extraocular anomalies"]
description: "Selegiline: nueva indicación predicha, Polimicrogiria perisilviana con hipoplasia cerebelosa y artrogriposis (polymicrogyria, perisylvian… (nivel de evidencia L5). Indicación original: No consta en l…"
---

# Selegiline
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Selegiline: Polimicrogiria perisilviana con hipoplasia cerebelosa y artrogriposis (polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis)
{: .text-alpha }

## Resumen en Una Frase

Selegilina es un inhibidor de la monoaminooxidasa B (MAO-B), utilizado originalmente para la **enfermedad de Parkinson** y también asociado a depresión y trastornos de ansiedad.
El modelo TxGNN predice que podría ser efectivo para **polimicrogiria perisilviana con hipoplasia cerebelosa y artrogriposis**, un síndrome raro del neurodesarrollo,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Polimicrogiria perisilviana con hipoplasia cerebelosa y artrogriposis (polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis) |
| Puntaje de Predicción TxGNN | 0.9915 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Selegiline (traducción no oficial): «La selegilina es un inhibidor irreversible de la monoaminooxidasa (MAO), que regula la degradación metabólica de las catecolaminas y de la serotonina en el sistema nervioso central y en los tejidos periféricos. A las dosis recomendadas, la selegilina es selectiva para la MAO de tipo B (MAO-B), la forma principal en el cerebro.» Texto original en inglés: "Selegiline is an irreversible inhibitor of monoamine oxidase (MAO), which regulates the metabolic degradation of catecholamines and serotonin in the central nervous system and peripheral tissues. At recommended doses, selegiline is selective for MAO type B (MAO-B), the major form in the brain." ([DailyMed: Zelapar (selegiline hydrochloride) prescribing information, Bausch Health US, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=380d7717-2a79-42f3-a712-efe5e7696ba0), versión del 2021-06-01; consultado el 2026-11-19). Según la información conocida, selegilina es un inhibidor selectivo e irreversible de la MAO-B, y los datos farmacológicos disponibles también la vinculan con MAO-A (dosis más altas). Su eficacia en la enfermedad de Parkinson, como monoterapia en etapas tempranas o combinada con levodopa en etapas avanzadas, está comprobada, y originalmente se desarrolló para el trastorno depresivo mayor.

Con los datos disponibles **no se identifica una relación mecanística plausible** entre la inhibición de MAO-B y este síndrome de malformación del neurodesarrollo. La polimicrogiria con hipoplasia cerebelosa y artrogriposis es un trastorno estructural del desarrollo cerebral, muy distinto de la enfermedad de Parkinson, que es degenerativa y dopaminérgica.

El puntaje de 0.9915 es una predicción computacional del modelo, sin respaldo clínico ni bibliográfico. No debe interpretarse como evidencia de eficacia.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 58113 | PLURIMEN 5 mg COMPRIMIDOS (Orion Corporation) | Comprimido | No especificada en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo según el grafo de conocimiento** (no provienen del texto del prospecto): atrofia multisistémica, síndrome de taquicardia postural ortostática, hipotensión ortostática, enfermedad renal, piouréter, trastorno bipolar, trastorno afectivo mayor, enfermedad hepática, enfermedad de la vesícula biliar, trastornos psicóticos (incluidos esquizofreniforme y esquizoafectivo), trastorno mental, melanoma, paro cardíaco súbito, enfermedad de la conducción cardíaca, feocromocitoma, paraganglioma simpático, cáncer de duodeno, de intestino delgado, cardíaco y de glándula suprarrenal, discinesia tardía y discinesia lingual-facial-bucal.
- **Dianas farmacológicas registradas**: MAO-A y MAO-B. Esto implica un riesgo potencial de interacciones con otros fármacos serotoninérgicos o simpaticomiméticos, que debe verificarse en el prospecto.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de ensayos clínicos, literatura y vínculo mecanístico plausible (nivel L5). Con los datos actuales no hay base para avanzar en esta indicación.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA) de selegilina
- Una hipótesis biológica que conecte la inhibición de MAO-B con la fisiopatología de la polimicrogiria
- Estudios preclínicos o de mecanismo que respalden la plausibilidad
- Las advertencias y contraindicaciones oficiales del prospecto de la AEMPS
- Evaluación de la compatibilidad de la vía de administración y del similitud con la indicación original

**Nota complementaria:** entre las otras indicaciones predichas, la **esquizofrenia** (puntaje 0.9914) tiene mucho más respaldo: un ensayo clínico completado (NCT00456976, fase temprana 1, n=70) y literatura sobre selegilina como terapia adyuvante para síntomas negativos, incluidos ensayos aleatorizados y una revisión sistemática. Su nivel de evidencia es L3 y podría ser una candidata más prometedora para una evaluación independiente.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Zelapar (selegiline hydrochloride) prescribing information, Bausch Health US, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=380d7717-2a79-42f3-a712-efe5e7696ba0) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

