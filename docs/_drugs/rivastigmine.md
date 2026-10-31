---
layout: default
title: Rivastigmine
parent: Solo predicción del modelo (L5)
nav_order: 709
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-31
monitor_inn: "Rivastigmine"
predicted_indications: ["glaucoma"]
description: "Rivastigmine: nueva indicación predicha, Glaucoma (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Rivastigmine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Rivastigmine: Glaucoma
{: .text-alpha }

## Resumen en Una Frase

Rivastigmina es un inhibidor de la colinesterasa, originalmente utilizado para el tratamiento de la enfermedad de Alzheimer.
El modelo TxGNN predice que podría ser efectivo para **glaucoma**, aunque por ahora solo cuenta con **3 publicaciones** (un estudio preclínico en conejos y dos revisiones) y **ningún ensayo clínico** que respalde esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Glaucoma |
| Puntaje de Predicción TxGNN | 0.9927 |
| Nivel de Evidencia | L5 (solo estudios preclínicos y de mecanismo) |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 9) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Rivastigmina inhibe dos enzimas: la acetilcolinesterasa y la butirilcolinesterasa. Al bloquearlas, aumenta la acetilcolina disponible y refuerza la señal colinérgica. No se dispone de datos curados sobre su mecanismo de acción original, por lo que esta descripción se infiere a partir de sus dianas farmacológicas y de su clase.

En el ojo, un mayor tono colinérgico puede favorecer la contracción del músculo ciliar y facilitar el drenaje del humor acuoso a través de la malla trabecular. Es el mismo principio de los agentes mióticos colinérgicos, como pilocarpina o fisostigmina, usados históricamente para reducir la presión intraocular (PIO). Un estudio preclínico en conejos (2000) observó que la rivastigmina tópica redujo la PIO, lo que apoya la plausibilidad biológica.

Hay que ser prudentes: la relación con la indicación original es sobre todo de clase farmacológica (inhibición de colinesterasas) y no se ha demostrado beneficio sobre el nervio óptico. El puntaje de TxGNN es una predicción computacional, no evidencia clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10673128](https://pubmed.ncbi.nlm.nih.gov/10673128/) | 2000 | Estudio preclínico (conejo) | J Ocul Pharmacol Ther | La rivastigmina tópica, inhibidor selectivo de la acetilcolinesterasa, redujo la presión intraocular en conejos normotensos |
| [39130374](https://pubmed.ncbi.nlm.nih.gov/39130374/) | 2024 | Revisión | Front Mol Biosci | Analiza los agentes colinérgicos para reducir la PIO (genética de sistemas, modelado molecular y perspectivas in vivo); señala que los agonistas M3 aprobados tienen efectos adversos colinérgicos sistémicos |
| [27967267](https://pubmed.ncbi.nlm.nih.gov/27967267/) | 2017 | Revisión (patentes) | Expert Opin Ther Pat | Repasa inhibidores y reactivadores de la acetilcolinesterasa; menciona que la inhibición leve tiene relevancia terapéutica en Alzheimer, miastenia gravis y glaucoma |

## Información de Mercado en España

Se registran 20 autorizaciones vigentes, todas de principio activo único. Las principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 98092005 | Prometax 3 mg cápsulas duras | Cápsula dura | No disponible |
| 98066025 | Exelon 9,5 mg/24 h parche transdérmico | Parche transdérmico | No disponible |
| 98066010 | Exelon 6 mg cápsulas duras | Cápsula dura | No disponible |
| 71781 | Rivastigmina Ortodrol 2 mg/ml solución oral EFG | Solución oral | No disponible |
| 109525010 | Nimvastid 3 mg cápsulas duras EFG | Cápsula dura | No disponible |

Las formas disponibles son cápsulas duras, parches transdérmicos y solución oral. No existe ninguna formulación oftálmica autorizada.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): epilepsia, enfermedades de los ganglios basales, distonía focal de la mano, blefaroespasmo, enfermedad pulmonar obstructiva crónica (EPOC), asma (incluidas las formas intrínseca y alérgica), enfermedad diarreica, parada cardíaca súbita, enfermedad de conducción cardíaca, síndrome del seno enfermo, bloqueo auriculoventricular, anorexia nerviosa, úlcera péptica activa, obstrucción del tracto urinario, trastornos parkinsonianos y enfermedad de Parkinson.
- **Interacciones farmacológicas**: no se identificaron interacciones entre fármacos; solo constan las dianas farmacológicas, acetilcolinesterasa y butirilcolinesterasa.
- **Seguridad ocular** (preocupaciones abiertas): miosis, irritación ocular y posibles efectos retinianos o en el cristalino con uso crónico.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia se limita a un estudio animal y a revisiones, sin ensayos en humanos (nivel L4). El puntaje alto de TxGNN no sustituye a los datos clínicos, y la seguridad ocular y la ausencia de formulación tópica son incógnitas importantes.

**Para avanzar se necesita:**
- Datos curados del mecanismo de acción
- Estudios preclínicos adicionales de eficacia y seguridad ocular, incluido el efecto sobre el nervio óptico
- Desarrollo y evaluación de una formulación oftálmica tópica
- Textos de indicación y advertencias de las fichas técnicas de la AEMPS
- Si los resultados preclínicos son favorables, un ensayo clínico exploratorio en humanos
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

