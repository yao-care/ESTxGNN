---
layout: default
title: Primidone
parent: Solo predicción del modelo (L5)
nav_order: 663
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-05
monitor_inn: "primidone"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
description: "Primidone: nueva indicación predicha, Neoplasia del nervio trigémino (trigeminal nerve neoplasm) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 1 (comercializadas: 1)"
---

# Primidone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Primidone: Neoplasia del nervio trigémino (trigeminal nerve neoplasm)
{: .text-alpha }

## Resumen en Una Frase

Primidona es un anticonvulsivo utilizado originalmente para el tratamiento de la epilepsia (crisis tónico-clónicas generalizadas, epilepsia parcial y síndrome de Lennox-Gastaut).
El modelo TxGNN predice que podría ser efectivo para **neoplasia del nervio trigémino**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Neoplasia del nervio trigémino (trigeminal nerve neoplasm) |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Primidone (traducción no oficial): «MYSOLINE eleva los umbrales convulsivos por electrochoque o por choque químico, o altera los patrones de las convulsiones, en animales de experimentación. Se desconoce el mecanismo o los mecanismos de la acción antiepiléptica de la primidona. La primidona per se tiene actividad anticonvulsiva, al igual que sus dos metabolitos, el fenobarbital y la feniletilmalonamida (PEMA).» Texto original en inglés: "MYSOLINE raises electro- or chemoshock seizure thresholds or alters seizure patterns in experimental animals. The mechanism(s) of primidone’s antiepileptic action is not known. Primidone per se has anticonvulsant activity as do its two metabolites, phenobarbital and phenylethylmalonamide (PEMA)." ([DailyMed: Mysoline (primidone) prescribing information, Bausch Health US, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=af593171-dabb-4ea3-b44c-89ed457b2c46), versión del 2026-09-10; consultado el 2026-11-19). Según la información conocida, primidona es un fármaco antiepiléptico cuya eficacia en epilepsia está bien establecida (es metabolizada en parte a fenobarbital), pero no hay datos que sustenten un mecanismo aplicable a una neoplasia.

La relación entre la indicación original y la nueva es débil. Primidona no tiene actividad antineoplásica conocida, y los datos compilados no respaldan un vínculo mecanístico. El puntaje tan alto (0.9999) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

Por ello, esta predicción debe interpretarse con cautela. Entre las demás predicciones del modelo, la **neuralgia del trigémino** (puntaje 0.9998, nivel L4) es la más plausible clínicamente, ya que se trata con anticonvulsivos moduladores de canales de sodio (la carbamazepina es de primera línea). Sin embargo, la evidencia disponible es indirecta y no hay ningún ensayo con primidona.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para neoplasia del nervio trigémino.

Como referencia, para otras indicaciones predichas se recuperó literatura indirecta, sin evidencia directa de eficacia de primidona:

| Indicación Predicha | Puntaje TxGNN | Nivel | Evidencia Recuperada |
|------|-----|------|---------|
| Neuralgia del trigémino | 0.9998 | L4 | Revisión de antiepilépticos en indicaciones distintas de la epilepsia ([15246950](https://pubmed.ncbi.nlm.nih.gov/15246950/), 2004); el resto trata de interacciones de carbamazepina o modelos preclínicos |
| Crisis epilépticas del pensamiento | 0.9999 | L4 | Estudio de cohorte sobre atención de epilepsia geriátrica ([19054416](https://pubmed.ncbi.nlm.nih.gov/19054416/), 2009), no específico |
| Epilepsia del sobresalto | 0.9999 | L4 | Un reporte de caso de 1995 ([8548670](https://pubmed.ncbi.nlm.nih.gov/8548670/)), anecdótico |
| Crisis epilépticas al comer | 0.9999 | L4 | Estudio en un perro, 1974 ([4525036](https://pubmed.ncbi.nlm.nih.gov/4525036/)) |
| Crisis epilépticas audiogénicas | 0.9999 | L4 | Estudios animales de 1964 y 1976 |
| Crisis epilépticas de lectura | 0.9999 | L4 | Reportes de caso y revisiones sobre otras epilepsias reflejas |
| Crisis inducidas por micción | 0.9999 | L4 | 15 publicaciones generales sobre epilepsia y seguridad de antiepilépticos, sin evidencia directa |
| Crisis inducidas por orgasmo; deficiencia de beta-cetotiolasa | 0.9999 / 0.9996 | L5 | Sin ensayos ni literatura |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 18498 | MYSOLINE 250 MG COMPRIMIDOS (Serb) | Comprimido | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): porfiria (incluida la hereditaria), enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, trastornos hematológicos (trombocitopenia, neutropenia, agranulocitosis, leucopenia, pancitopenia, anemia), abuso o dependencia de sustancias, síndromes de apnea del sueño e hipoventilación central, y trastornos de ansiedad, neuróticos y distímicos.
- **Interacciones Farmacológicas**: se identificaron 273 interacciones. Entre las principales, de gravedad **mayor**: morfina y eliglustat. De gravedad **moderada**: doxiciclina, hidrocortisona, dexametasona, betametasona, triamcinolona, colecalciferol, calcifediol, calcitriol, pioglitazona, bupropión, aprepitant, metronidazol, canagliflozina, saxagliptina, difenoxina, difenoxilato y dronabinol. De gravedad **menor**: cimetidina.

Para las advertencias y contraindicaciones del prospecto, consultar el prospecto de la AEMPS, ya que no se dispone de ellas en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para neoplasia del nervio trigémino se basa solo en el modelo (nivel L5), sin ensayos, sin literatura y sin vínculo mecanístico plausible con un fármaco sin actividad antineoplásica conocida. Entre las predicciones, solo la neuralgia del trigémino merece explorarse como pregunta de investigación.

**Para avanzar se necesita:**
- Obtener el mecanismo de acción de primidona (consulta a DrugBank).
- Obtener y analizar las advertencias y contraindicaciones del prospecto de la AEMPS, así como el texto de indicación autorizada.
- Revisión sistemática de la evidencia de primidona en neuralgia del trigémino y otros usos no epilépticos, frente a la carbamazepina.
- Evaluar la seguridad en poblaciones específicas (porfiria, insuficiencia hepática o renal, citopenias) y el riesgo de interacciones por inducción enzimática.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Mysoline (primidone) prescribing information, Bausch Health US, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=af593171-dabb-4ea3-b44c-89ed457b2c46) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

