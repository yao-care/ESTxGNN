---
layout: default
title: Clobazam
parent: Evidencia moderada (L3-L4)
nav_order: 191
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Clobazam: nueva indicación predicha, Síndrome de epilepsia relacionada con infección febril (FIRES) (nivel de evidencia L4). Indicación original: Síndrome de Lennox-Gastaut (según el grafo de conocim…"
monitor_inn: "CLOBAZAM"
predicted_indications: ["febrile infection-related epilepsy syndrome", "perioral myoclonia with absences", "atypical childhood epilepsy with centrotemporal spikes", "photosensitive occipital lobe epilepsy", "cryptogenic late-onset epileptic spasms", "childhood onset epileptic encephalopathy", "benign occipital epilepsy", "early-onset epileptic encephalopathy and intellectual disability due to GRIN2A mutation", "restless legs syndrome", "polymicrogyria with optic nerve hypoplasia"]
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

## Clobazam: De Síndrome de Lennox-Gastaut a Síndrome de Epilepsia Relacionada con Infección Febril (FIRES)
{: .text-alpha }

## Resumen en Una Frase

Clobazam es una benzodiazepina (1,5-benzodiazepina) utilizada originalmente para el tratamiento del síndrome de Lennox-Gastaut.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de epilepsia relacionada con infección febril (FIRES)**,
aunque actualmente solo hay **2 publicaciones** (series y reportes de casos, ninguna con clobazam) y **ningún ensayo clínico** que respalde esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Síndrome de Lennox-Gastaut (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Síndrome de epilepsia relacionada con infección febril (FIRES) |
| Puntaje de Predicción TxGNN | 99.82% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, clobazam es un modulador alostérico positivo del receptor GABA-A, igual que las benzodiazepinas (midazolam, lorazepam) empleadas en el manejo de FIRES. Esto ofrece una justificación plausible a nivel de clase farmacológica.

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

**Nota sobre otras indicaciones predichas:** entre las otras nueve candidatas, la **encefalopatía epiléptica de inicio en la infancia** (puntaje 99.59%) es la que cuenta con mayor respaldo bibliográfico (nivel L3, 20 publicaciones, principalmente revisiones y guías sobre Lennox-Gastaut y otros síndromes). Dado que clobazam ya está indicado en Lennox-Gastaut, se trata en gran medida de una extensión de un uso conocido, y merece evaluarse como pregunta de investigación. El resto de candidatas tienen nivel L4 o L5 y se mantienen en Hold.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

