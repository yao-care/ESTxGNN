---
layout: default
title: Interferon Gamma-1B
parent: Solo predicción del modelo (L5)
nav_order: 425
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-05
monitor_inn: "INTERFERON GAMMA-1B"
predicted_indications: ["heart disease", "Jeune syndrome situs inversus", "orofacial clefting syndrome", "Pierre Robin syndrome associated with a chromosomal anomaly", "disorder of fucoglycosan synthesis", "partial deletion of the long arm of chromosome 7", "genetic syndromic Pierre Robin syndrome", "Laubry-Pezzi syndrome", "partial deletion of the long arm of chromosome 22", "interventricular septum aneurysm"]
description: "Interferon Gamma-1B: nueva indicación predicha, Heart disease (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 1 (comercializadas: 1)"
---

# Interferon Gamma-1B
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Interferon Gamma-1B: Heart disease
{: .text-alpha }

## Resumen en Una Frase

Interferón gamma-1b es una citocina recombinante inmunomoduladora autorizada en España (IMUKIN), cuya indicación original no figura en los datos compilados para este informe.
El modelo TxGNN predice que podría ser efectivo para **enfermedad cardíaca**, con un puntaje muy alto (0.9999), pero **sin ensayos clínicos** y con solo **3 publicaciones tangenciales** que no respaldan directamente esta indicación.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Heart disease |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Interferon Gamma-1B (traducción no oficial): «Los interferones se unen a receptores específicos de la superficie celular e inician una secuencia de eventos intracelulares que conducen a la transcripción de genes estimulados por interferón. Los tres grupos principales de interferones (alfa, beta, gamma) tienen actividades biológicas parcialmente superpuestas que incluyen la inmunorregulación, como el aumento de la resistencia a los patógenos microbianos y la inhibición de la proliferación celular.» Texto original en inglés: "Interferons bind to specific cell surface receptors and initiate a sequence of intracellular events that lead to the transcription of interferon-stimulated genes. The three major groups of interferons (alpha, beta, gamma) have partially overlapping biological activities that include immunoregulation such as increased resistance to microbial pathogens and inhibition of cell proliferation." ([DailyMed: Actimmune (interferon gamma-1b) prescribing information, Horizon Therapeutics USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5d0b1256-1981-4519-94f4-a4a2f98bd8a3), versión del 2026-03-30; consultado el 2026-11-19). Según la información conocida, el interferón gamma-1b es un inmunomodulador que activa macrófagos y las respuestas Th1.

No se ha establecido un vínculo mecanístico directo con la enfermedad cardíaca. El puntaje es muy alto, pero proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica, para una categoría amplia e inespecífica. Cualquier relevancia cardíaca sería indirecta (relacionada con infección o inflamación). Además, la señalización de IFN-gamma se ha implicado en la inflamación y el remodelado miocárdico, por lo que no puede descartarse un posible daño.

Las tres publicaciones recuperadas son tangenciales: una revisión sistemática sobre ataxia de Friedreich (que tiene un componente de miocardiopatía y en la que se ha probado este fármaco), un estudio de validación de la prueba de marcha de 6 minutos en fibrosis pulmonar idiopática y un caso clínico de endocarditis protésica por *Mycobacterium chimaera*. Ninguna demuestra que el fármaco trate la enfermedad cardíaca.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37180421](https://pubmed.ncbi.nlm.nih.gov/37180421/) | 2022 | Revisión sistemática | Therapeutic Advances in Rare Disease | Resume la eficacia y seguridad de las intervenciones en ataxia de Friedreich; relación solo indirecta con el corazón |
| [21131468](https://pubmed.ncbi.nlm.nih.gov/21131468/) | 2011 | Estudio de validación | Am J Respir Crit Care Med | Validación de la prueba de marcha de 6 minutos en fibrosis pulmonar idiopática; fuera del tema |
| [31020218](https://pubmed.ncbi.nlm.nih.gov/31020218/) | 2018 | Caso clínico | Eur Heart J Case Reports | Tratamiento exitoso de endocarditis protésica por *M. chimaera* asociada a la atención sanitaria; primer caso español |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 60113 | IMUKIN 100 microgramos SOLUCIÓN INYECTABLE | Solución inyectable | No especificada en los datos disponibles |

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: se identificaron 57 interacciones en total. Entre las listadas, las de nivel **mayor** son:
  - Bupropión
  - Deferiprona
  - Iohexol
  - Iopamidol
  - Samario (153Sm) lexidronam

  Entre las de nivel **moderado** figuran warfarina, dicumarol, teofilina, aminofilina, oxtrifilina, roflumilast, naltrexona, cloranfenicol, palifermina, avatrombopag, lindano, cloruro de estroncio Sr-89, ácido picosulfúrico, polietilenglicol con electrolitos y sulfato de sodio.
- Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de ensayos clínicos y de literatura directamente relevante. No existe un vínculo mecanístico demostrado con la enfermedad cardíaca, y la señalización de IFN-gamma podría ser perjudicial en la inflamación miocárdica. El puntaje alto del modelo, por sí solo, no basta para avanzar.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de la AEMPS (advertencias, contraindicaciones e indicación autorizada)
- Completar los datos del mecanismo de acción
- Definir un subtipo concreto de enfermedad cardíaca (por ejemplo, miocardiopatía inflamatoria o relacionada con infección) y realizar estudios preclínicos o de mecanismo
- Evaluar el riesgo cardiovascular de la señalización de IFN-gamma antes de cualquier estudio clínico
- Revisar las interacciones mayores para la población cardiológica

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Actimmune (interferon gamma-1b) prescribing information, Horizon Therapeutics USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5d0b1256-1981-4519-94f4-a4a2f98bd8a3) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

