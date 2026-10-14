---
layout: default
title: Larotrectinib
parent: Solo predicción del modelo (L5)
nav_order: 454
evidence_level: L5
indication_count: 2
---

# Larotrectinib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Larotrectinib: De Tumores Sólidos con Fusión NTRK a Neoplasia Endocrina Múltiple

## Resumen en Una Frase

Larotrectinib es un inhibidor selectivo de los receptores TRK (TRKA/B/C), comercializado en España como VITRAKVI para tumores sólidos con fusión del gen NTRK. El modelo TxGNN predice que podría ser efectivo para **neoplasia endocrina múltiple**, pero la evidencia es muy limitada: **1 ensayo clínico** de apoyo indirecto y **2 publicaciones** que no evalúan directamente esta indicación.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los textos de autorización compilados (el fármaco está autorizado como inhibidor de TRK para tumores sólidos con fusión NTRK) |
| Nueva Indicación Predicha | Neoplasia endocrina múltiple |
| Puntaje de Predicción TxGNN | 99,24% |
| Nivel de Evidencia | L3 (según la clasificación de los datos compilados; en la práctica, evidencia indirecta y débil) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados no incluyen el mecanismo de acción detallado. Según la información conocida, larotrectinib es un inhibidor pan-TRK altamente selectivo (TRKA, TRKB y TRKC), autorizado de forma agnóstica al tumor para cánceres sólidos con fusión NTRK.

La neoplasia endocrina múltiple (en particular la MEN2) está causada por mutaciones germinales activadoras de **RET**, una quinasa distinta de TRK. Larotrectinib no tiene actividad relevante sobre RET, por lo que no existe un vínculo mecanístico directo. Solo podría haberlo en los poco frecuentes tumores con fusión NTRK que aparecen en tejidos relacionados (por ejemplo, tiroides).

El puntaje alto de TxGNN (0,99) probablemente refleja la proximidad en la red de conocimiento con el cáncer de tiroides y otros inhibidores de quinasas, y no una relación validada entre fármaco y diana. La literatura disponible lo confirma: un trabajo trata la resistencia a inhibidores selectivos de RET y la otra es una revisión general sobre inhibidores de quinasas en cáncer de tiroides. Esta predicción debe considerarse una pregunta de investigación, no una hipótesis respaldada.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02465060](https://clinicaltrials.gov/study/NCT02465060) | Fase 2 | Activo, sin reclutamiento | 6452 | NCI-MATCH: ensayo "basket" de oncología de precisión con tratamiento dirigido por pruebas genéticas en tumores sólidos, linfomas y mieloma refractarios. No presenta datos de eficacia específicos para neoplasia endocrina múltiple; apoyo solo indirecto. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31322645](https://pubmed.ncbi.nlm.nih.gov/31322645/) | 2019 | Revisión | Endocrine Reviews | Terapia dirigida con inhibidores de quinasas en cáncer de tiroides avanzado; incluye indicaciones específicas por mutación, sin evidencia directa sobre larotrectinib en neoplasia endocrina múltiple. |
| [38438731](https://pubmed.ncbi.nlm.nih.gov/38438731/) | 2024 | Estudio preclínico/mecanístico | NPJ Precision Oncology | Mecanismos de resistencia a inhibidores selectivos de RET (selpercatinib) en un paciente con carcinoma medular de tiroides; no involucra larotrectinib. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1191385003 | VITRAKVI 20 mg/ml solución oral, 1 frasco de 100 ml | Solución oral | No disponible |
| 1191385004 | VITRAKVI 20 mg/ml solución oral, 2 frascos de 50 ml | Solución oral | No disponible |
| 1191385001 | VITRAKVI 25 mg cápsulas duras | Cápsula dura | No disponible |
| 1191385002 | VITRAKVI 100 mg cápsulas duras | Cápsula dura | No disponible |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de quinasas TRK) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto (en general, hemograma y función hepática y renal) |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; entre las 20 detalladas, la mayoría son de nivel moderado.
  - **Mayor**: claritromicina.
  - **Moderado**: hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida, pioglitazona, aprepitant, omeprazol, cimetidina, saxagliptina, dolasetrón, dronabinol, eliglustat, naldemedina, naltrexona, cisaprida y clotrimazol.
  - **Menor**: naloxegol.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay un vínculo mecanístico directo entre la inhibición de TRK y la neoplasia endocrina múltiple (impulsada por RET). El único ensayo es un estudio "basket" genérico y la literatura no evalúa larotrectinib en esta indicación. El puntaje alto de TxGNN parece reflejar proximidad en la red y no una relación biológica validada.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y de las indicaciones autorizadas por la AEMPS.
- Advertencias y contraindicaciones del prospecto de la AEMPS (bloqueante para el cribado de seguridad).
- Identificar si existen pacientes con neoplasias endocrinas y fusión NTRK confirmada, que sería el único escenario plausible.
- Evidencia clínica específica (series de casos o resultados por cohorte de NCI-MATCH) en tumores endocrinos con fusión NTRK.
- Revisión de las interacciones, en especial con inhibidores potentes de CYP3A4 como la claritromicina.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

