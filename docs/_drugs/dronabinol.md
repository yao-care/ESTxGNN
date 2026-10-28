---
layout: default
title: Dronabinol
parent: Evidencia moderada (L3-L4)
nav_order: 267
evidence_level: L3
indication_count: 9
last_modified_at: 2026-10-28
description: "Dronabinol: nueva indicación predicha, Migraña (migraine disorder) (nivel de evidencia L3). Indicación original: No disponible en los datos de la autorización de AEMPS"
monitor_inn: "dronabinol"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "headache disorder", "trigeminal autonomic cephalalgia", "pulmonary hypertension", "hypertrichosis (disease)", "kyphoscoliotic heart disease", "Ambras type hypertrichosis universalis congenita", "atrophoderma vermiculata"]
---

# Dronabinol
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **9** 
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

## Dronabinol: De Indicación No Especificada en la Autorización a Migraña
{: .text-alpha }

## Resumen en Una Frase

Dronabinol (delta-9-tetrahidrocannabinol sintético) está autorizado en España en el producto Sativex, solución para pulverización bucal, aunque los datos compilados no incluyen el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **migraña (trastorno de migraña)**,
con **1 ensayo clínico** de Fase 2 completado (sin resultados confirmados) y **1 publicación** de baja relevancia (una encuesta) que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de la autorización de AEMPS |
| Nueva Indicación Predicha | Migraña (migraine disorder) |
| Puntaje de Predicción TxGNN | 0,9992 |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | Comercializado (registros vigentes: 1 de 1) |
| Número de Autorizaciones | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

No se dispone actualmente de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, dronabinol es el delta-9-THC sintético y actúa como agonista de los receptores cannabinoides CB1 y CB2.

El sistema endocannabinoide modula la señalización nociceptiva, la activación trigeminovascular, la transmisión serotoninérgica y la neuroinflamación, procesos que podrían contribuir a la fisiopatología de la migraña. Esto es coherente con la predicción del modelo, pero el puntaje es una predicción computacional y no constituye evidencia clínica.

La relación con la indicación original no puede establecerse con los datos disponibles, porque la autorización de AEMPS no incluye texto de indicación. Existen además reportes de apoyo para cefaleas primarias (un caso de cefalea en racimos con respuesta a cannabis y dronabinol), pero son anecdóticos y no controlados.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00123201](https://clinicaltrials.gov/study/NCT00123201) | Fase 2 | Completado | No disponible | Estudio multicéntrico, aleatorizado, doble ciego y controlado con placebo de dronabinol en inhalador de dosis medida (MDI) para el tratamiento agudo de la migraña moderada a grave (2005-2007). No hay resultados publicados ni inscripción confirmada, por lo que su relevancia queda pendiente de verificación (grado B). |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10575286](https://pubmed.ncbi.nlm.nih.gov/10575286/) | 1999 | Encuesta | Forschende Komplementärmedizin | Encuesta estandarizada sobre el uso médico de productos de cannabis en países de habla alemana; apoyo indirecto y de baja calidad. |

Para indicaciones relacionadas (cefalea en general y cefalea en racimos) existen además una revisión narrativa ([28281107](https://pubmed.ncbi.nlm.nih.gov/28281107/), 2017, *Current Pain and Headache Reports*, sobre cannabis para dolor y cefaleas) y un reporte de caso ([19220500](https://pubmed.ncbi.nlm.nih.gov/19220500/), 2009, *Headache*, cefalea en racimos refractaria con alivio mediante cannabis y dronabinol).

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 72544 | SATIVEX 2,7 MG/2,5 MG SOLUCIÓN PARA PULVERIZACIÓN BUCAL | Solución para pulverización bucal | No especificada en los datos |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad, no texto del prospecto): hipertensión, trastorno hipotensivo, epilepsia, trastorno de ansiedad, trastorno neurótico, trastorno distímico, trastorno bipolar, trastorno afectivo mayor, esquizofrenia, abuso/dependencia de sustancias y trastornos relacionados con sustancias.
- **Interacciones farmacológicas**: se identificaron 357 interacciones. Entre las listadas destaca una de nivel **mayor** con **tramadol**. Otras de nivel moderado incluyen fentanilo, codeína, dihidrocodeína, alfentanilo, etanol, butalbital, gabapentina, fluvoxamina, fosfenitoína, nifedipino, furosemida, fosinopril, clorfeniramina y aldesleukina. En general, conviene vigilar el efecto aditivo sobre el sistema nervioso central con opioides, sedantes y alcohol.
- Los efectos cardiovasculares de los cannabinoides (taquicardia, hipotensión) requieren atención especial.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única evidencia directa es un ensayo de Fase 2 completado, sin resultados ni inscripción verificados, además de literatura indirecta (encuesta, revisión y reporte de caso). El nivel de evidencia es L3 y la propuesta se mantiene como pregunta de investigación. Además, faltan los datos de seguridad oficiales del prospecto, lo que impide avanzar al cribado de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias, contraindicaciones e indicación aprobada).
- Completar los datos del mecanismo de acción desde DrugBank.
- Localizar los resultados y la inscripción del ensayo NCT00123201 y confirmar sus criterios de valoración en migraña.
- Evaluar la compatibilidad de la vía de administración (bucal frente a inhalada) para la nueva indicación.
- Valorar el perfil de riesgo en pacientes con hipertensión, trastornos psiquiátricos, epilepsia o antecedentes de abuso de sustancias.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

