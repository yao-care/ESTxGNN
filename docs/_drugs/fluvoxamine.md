---
layout: default
title: Fluvoxamine
parent: Solo predicción del modelo (L5)
nav_order: 353
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "Fluvoxamine"
predicted_indications: ["schizoid personality disorder", "histrionic personality disorder (disease)", "schizotypal personality disorder", "paranoid personality disorder", "anxiety disorder", "agoraphobia", "benign paroxysmal torticollis of infancy", "dependent personality disorder", "narcissistic personality disorder"]
description: "Fluvoxamine: nueva indicación predicha, Trastorno esquizoide de la personalidad (schizoid personality disorder) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 4 (comercializadas: 4)"
---

# Fluvoxamine
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

## Fluvoxamine: Trastorno esquizoide de la personalidad (schizoid personality disorder)
{: .text-alpha }

## Resumen en Una Frase

Fluvoxamina es un inhibidor selectivo de la recaptación de serotonina que actúa sobre el transportador SERT y el receptor sigma-1.
El modelo TxGNN predice que podría ser efectivo para el **trastorno esquizoide de la personalidad (schizoid personality disorder)**,
pero la evidencia es muy limitada: **ningún ensayo clínico** y **1 publicación** que no estudia directamente esta enfermedad.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Trastorno esquizoide de la personalidad (schizoid personality disorder) |
| Puntaje de Predicción TxGNN | 1.0000 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 4 de 4) |
| Número de Autorizaciones | 4 (comercializadas: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe indican que la fluvoxamina se une con alta afinidad al transportador de serotonina (SERT, gen SLC6A4) y al receptor sigma-1 (SIGMAR1), sobre el que parece actuar como agonista. Al bloquear SERT aumenta la serotonina disponible en la sinapsis. Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Fluvoxamine (traducción no oficial): «Se presume que el mecanismo de acción del maleato de fluvoxamina en el trastorno obsesivo-compulsivo está relacionado con su inhibición específica de la recaptación de serotonina en las neuronas cerebrales. Se ha demostrado en estudios preclínicos, tanto in vitro como in vivo, que la fluvoxamina es un potente inhibidor del transportador de recaptación de serotonina.» Texto original en inglés: "The mechanism of action of fluvoxamine maleate in obsessive compulsive disorder is presumed to be linked to its specific serotonin reuptake inhibition in brain neurons. Fluvoxamine has been shown to be a potent inhibitor of the serotonin reuptake transporter in preclinical studies, both in vitro and in vivo." ([DailyMed: fluvoxamine maleate prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9972efbb-46cd-45b7-b71c-35032311b70c), versión del 2026-10-26; consultado el 2026-11-20).

Sin embargo, no se ha establecido un vínculo mecanístico directo con el trastorno esquizoide de la personalidad. El puntaje alto del modelo parece reflejar la cercanía de esta enfermedad con otros trastornos psiquiátricos y dianas serotoninérgicas, no una prueba farmacológica específica. Por ello, esta predicción debe considerarse una hipótesis sin respaldo clínico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10929788](https://pubmed.ncbi.nlm.nih.gov/10929788/) | 2000 | Cohorte | Comprehensive Psychiatry | Estudio de 148 personas con trastorno dismórfico corporal, 26 de ellas en un estudio de tratamiento con fluvoxamina; describe rasgos y trastornos de la personalidad como comorbilidad. No evalúa fluvoxamina para el trastorno esquizoide de la personalidad. |

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 57233 | DUMIROX 50 mg COMPRIMIDOS RECUBIERTOS CON PELICULA | COMPRIMIDO RECUBIERTO CON PELÍCULA | Viatris Healthcare Limited | Comercializada |
| 58212 | DUMIROX 100 mg COMPRIMIDOS RECUBIERTOS CON PELICULA | COMPRIMIDO RECUBIERTO CON PELÍCULA | Viatris Healthcare Limited | Comercializada |
| 63277 | FLUVOXAMINA SANDOZ 100 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Sandoz Farmaceutica S.A. | Comercializada |
| 63276 | FLUVOXAMINA SANDOZ 50 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Sandoz Farmaceutica S.A. | Comercializada |

Se muestran las 4 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Interacciones farmacológicas / farmacología**: los datos compilados muestran unión a SERT y al receptor sigma-1 (SIGMAR1). No incluyen interacciones con otros medicamentos con nivel de gravedad asignado.

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ensayos clínicos y la única publicación vinculada no estudia fluvoxamina en el trastorno esquizoide de la personalidad; por ello el nivel de evidencia es L5.

**Para avanzar se necesita:**
- Estudios clínicos o preclínicos que evalúen directamente la fluvoxamina en el trastorno esquizoide de la personalidad
- Fundamento mecanístico que conecte la acción serotoninérgica o sigma-1 con esta enfermedad
- Revisión de las advertencias y contraindicaciones del prospecto en España antes de cualquier evaluación posterior

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-20 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: fluvoxamine maleate prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9972efbb-46cd-45b7-b71c-35032311b70c) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

