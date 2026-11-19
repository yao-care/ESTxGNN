---
layout: default
title: Clobazam
parent: Evidencia moderada (L3-L4)
nav_order: 191
evidence_level: L4
indication_count: 10
last_modified_at: 2026-11-20
monitor_inn: "CLOBAZAM"
predicted_indications: ["febrile infection-related epilepsy syndrome", "perioral myoclonia with absences", "atypical childhood epilepsy with centrotemporal spikes", "photosensitive occipital lobe epilepsy", "cryptogenic late-onset epileptic spasms", "childhood onset epileptic encephalopathy", "benign occipital epilepsy", "early-onset epileptic encephalopathy and intellectual disability due to GRIN2A mutation", "restless legs syndrome", "polymicrogyria with optic nerve hypoplasia"]
description: "Clobazam: nueva indicación predicha, Febrile infection-related epilepsy syndrome (nivel de evidencia L4). En España, autorizaciones de la AEMPS: 4 (comercializadas: 4)"
---

# Clobazam
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

## Clobazam: Febrile infection-related epilepsy syndrome
{: .text-alpha }

## Resumen en Una Frase

Clobazam es una benzodiazepina (1,5-benzodiazepina) utilizada originalmente para el tratamiento del síndrome de Lennox-Gastaut.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de epilepsia relacionada con infección febril (FIRES)**,
aunque actualmente solo hay **2 publicaciones** (series y reportes de casos, ninguna con clobazam) y **ningún ensayo clínico** que respalde esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Febrile infection-related epilepsy syndrome |
| Puntaje de Predicción TxGNN | 0.9982 |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 4 de 4) |
| Número de Autorizaciones | 4 (comercializadas: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Clobazam (traducción no oficial): «El mecanismo de acción exacto del clobazam, una 1,5-benzodiazepina, no se conoce por completo, pero se cree que implica la potenciación de la neurotransmisión GABAérgica derivada de la unión al sitio de las benzodiazepinas del receptor GABA A.» Texto original en inglés: "The exact mechanism of action for clobazam, a 1,5-benzodiazepine, is not fully understood but is thought to involve potentiation of GABAergic neurotransmission resulting from binding at the benzodiazepine site of the GABA A receptor." ([DailyMed: Onfi (clobazam) prescribing information, Lundbeck Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=de03bd69-2dca-459c-93b4-541fd3e9571c), versión del 2026-10-16; consultado el 2026-11-19). Según la información conocida, clobazam es un modulador alostérico positivo del receptor GABA-A, igual que las benzodiazepinas (midazolam, lorazepam) empleadas en el manejo de FIRES. Esto ofrece una justificación plausible a nivel de clase farmacológica.

FIRES es un tipo de estado epiléptico refractorio de inicio reciente (NORSE) que aparece en niños previamente sanos, y las crisis suelen ser resistentes a los antiepilépticos convencionales. Clobazam ya se usa en una encefalopatía epiléptica grave de la infancia (Lennox-Gastaut), por lo que existe cierta afinidad clínica entre ambas condiciones.

Sin embargo, la literatura recuperada trata sobre lorazepam enteral y perampanel, no sobre clobazam. La evidencia es por tanto **indirecta**, y no demuestra eficacia de clobazam en FIRES.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35770765](https://pubmed.ncbi.nlm.nih.gov/35770765/) | 2022 | Serie de casos | Epileptic Disorders | El lorazepam enteral resultó una estrategia prometedora de retirada gradual en pacientes con FIRES dependientes de midazolam |
| [39958143](https://pubmed.ncbi.nlm.nih.gov/39958143/) | 2025 | Reporte de caso | Cureus | Posible papel de perampanel para reducir la dependencia de barbitúricos en un niño de 13 años con FIRES |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 54862 | NOIAFREN 10 mg COMPRIMIDOS | Comprimido | No disponible |
| 56993 | NOIAFREN 20 mg COMPRIMIDOS | Comprimido | No disponible |
| 81523 | SILOCALM 2 MG/ML SUSPENSIÓN ORAL | Suspensión oral | No disponible |
| 81524 | SILOCALM 1 MG/ML SUSPENSIÓN ORAL | Suspensión oral | No disponible |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (se identificaron 100 interacciones; se muestran las principales):
  - **Mayores**: morfina (incluida la liposomal) y eliglustat.
  - **Moderadas**: bupropión, aprepitant, omeprazol, esomeprazol, lansoprazol, cimetidina, claritromicina, dexfenfluramina, fenfluramina, dronabinol y metoclopramida.
  - **Menores**: antiácidos como óxido, carbonato e hidróxido de magnesio, hidróxido de aluminio, carbonato de calcio y magaldrato.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje de TxGNN es alto, pero la evidencia se limita a una serie de casos y un reporte de caso con otras benzodiazepinas y perampanel, sin ensayos clínicos ni datos específicos de clobazam en FIRES (nivel L4).

**Para avanzar se necesita:**
- Datos específicos de clobazam en FIRES/NORSE (series de casos o estudios retrospectivos)
- Datos detallados del mecanismo de acción (MOA)
- Texto de las indicaciones autorizadas y advertencias/contraindicaciones del prospecto de la AEMPS, necesarios para el cribado de seguridad
- Evaluación de la compatibilidad de vías de administración (formas orales disponibles frente a las necesidades en pacientes críticos)
- Plan de monitoreo de seguridad que contemple las interacciones de nivel mayor (opioides, eliglustat)

**Nota sobre otras indicaciones predichas:** entre las otras nueve candidatas, la **encefalopatía epiléptica de inicio en la infancia** (puntaje 0.9959) es la que cuenta con mayor respaldo bibliográfico (nivel L3, 20 publicaciones, principalmente revisiones y guías sobre Lennox-Gastaut y otros síndromes). Dado que clobazam ya está indicado en Lennox-Gastaut, se trata en gran medida de una extensión de un uso conocido, y merece evaluarse como pregunta de investigación. El resto de candidatas tienen nivel L4 o L5 y se mantienen en Hold.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Onfi (clobazam) prescribing information, Lundbeck Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=de03bd69-2dca-459c-93b4-541fd3e9571c) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

