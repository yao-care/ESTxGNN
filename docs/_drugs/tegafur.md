---
layout: default
title: Tegafur
parent: Evidencia alta (L1-L2)
nav_order: 513
evidence_level: L1
indication_count: 10
---

# Tegafur
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **10** 
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

# Tegafur: De Indicación Original No Registrada a Neoplasia de Colon

## Resumen en Una Frase

Tegafur es un profármaco oral del 5-fluorouracilo (5-FU) que se utiliza en quimioterapia, habitualmente combinado con uracilo (UFT). En los datos de la AEMPS disponibles no consta el texto de su indicación original.
El modelo TxGNN predice que podría ser efectivo para **neoplasia de colon**, con **30 ensayos clínicos** y **20 publicaciones** que respaldan esta dirección, entre ellos varios ensayos de Fase 3 completados.
Esta predicción se parece más a un uso ya establecido en otras regiones que a un reposicionamiento novedoso.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (el texto de indicación de la autorización está vacío) |
| Nueva Indicación Predicha | Neoplasia de colon |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, tegafur es un profármaco oral del 5-FU. Su combinación con uracilo (UFT) es una fluoropirimidina dirigida a la timidilato sintasa, la misma clase mecanística que la quimioterapia estándar del cáncer colorrectal. Mecanísticamente es aplicable a la neoplasia de colon.

La relación con la indicación original no puede verificarse, porque el registro español no incluye el texto de indicación. Aun así, la literatura y los ensayos muestran que UFT/leucovorina se usa como quimioterapia adyuvante en cáncer de colon estadio II y III, sobre todo en Japón y otras zonas de Asia. Por eso la propuesta se entiende mejor como un uso ya establecido regionalmente que como un reposicionamiento verdadero. Se recomienda añadir esta indicación a las indicaciones originales del fármaco en lugar de tratarla como novedosa.

Conviene tener en cuenta que el estado regulatorio varía por región (aprobado en Japón y partes de Asia, no aprobado por la FDA). Por eso la evidencia clínica asiática debe contrastarse con la práctica y la autorización europeas.

---

## Evidencia de Ensayos Clínicos

Se listan 10 de los 30 ensayos registrados, priorizando Fase 3 y los que evalúan tegafur de forma directa.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00378716](https://clinicaltrials.gov/study/NCT00378716) | Fase 3 | Completado | 1608 | UFT/leucovorina vs 5-FU/leucovorina en cáncer de colon resecado estadio II y III |
| [NCT00392899](https://clinicaltrials.gov/study/NCT00392899) | Fase 3 | Completado | 2025 | Quimioterapia adyuvante con UFT vs observación en cáncer de colon estadio II resecado |
| [NCT00152230](https://clinicaltrials.gov/study/NCT00152230) | Fase 3 | Completado | 900 | UFT adyuvante vs cirugía sola en cáncer colorrectal Dukes C (NSAS-CC) |
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Fase 3 | Completado | 1535 | UFT+leucovorina vs TS-1 (S-1) como adyuvancia en cáncer de colon estadio III |
| [NCT00905047](https://clinicaltrials.gov/study/NCT00905047) | Fase 3 | Completado | 89 | Cruzado según preferencia del paciente entre Xeloda y UFT con ácido folínico en cáncer colorrectal avanzado o metastásico |
| [NCT00209742](https://clinicaltrials.gov/study/NCT00209742) | Fase 3 | Desconocido | 340 | UFT+LV, UFT+LV/UFT y UFT+LV+PSK/UFT+PSK como adyuvancia en cáncer colorrectal estadio III |
| [NCT00385970](https://clinicaltrials.gov/study/NCT00385970) | Fase 3 | Desconocido | 380 | UFT+PSK vs UFT+LV en cáncer colorrectal estadio IIB/III; UFT es la base de ambos brazos |
| [NCT00497107](https://clinicaltrials.gov/study/NCT00497107) | Fase 3 | Desconocido | 300 | UFT/LV vs UFT/LV+PSK como adyuvancia en cáncer colorrectal estadio IIIa/IIIb |
| [NCT02887365](https://clinicaltrials.gov/study/NCT02887365) | Fase 4 | Desconocido | 300 | Tegafur-uracilo como quimioterapia de mantenimiento en cáncer de colon estadio II MSS/MSI-L |
| [NCT00439517](https://clinicaltrials.gov/study/NCT00439517) | Fase 2 | Completado | 302 | FOLFOX-4 + cetuximab vs UFOX (UFT + oxaliplatino + ácido folínico) + cetuximab en cáncer colorrectal metastásico |

---

## Evidencia de Literatura

Se listan 10 de las 20 publicaciones recuperadas, priorizando ensayos aleatorizados y revisiones.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33714860](https://pubmed.ncbi.nlm.nih.gov/33714860/) | 2021 | ECA | ESMO Open | Supervivencia global a 5 años y análisis por subgrupos del ensayo ACTS-CC 02: S-1 + oxaliplatino (SOX) no fue superior a UFT/LV en supervivencia libre de enfermedad en cáncer de colon estadio III de alto riesgo |
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | ECA | Clin Colorectal Cancer | Ensayo de Fase 3 de superioridad que compara SOX con UFT/LV como adyuvancia en cáncer de colon estadio III de alto riesgo |
| [16648506](https://pubmed.ncbi.nlm.nih.gov/16648506/) | 2006 | ECA | J Clin Oncol | Protocolo NSABP C-06: UFT oral + leucovorina vs 5-FU intravenoso + leucovorina en cáncer de colon estadio II y III |
| [26347106](https://pubmed.ncbi.nlm.nih.gov/26347106/) | 2015 | ECA | Ann Oncol | Ensayo de Fase 3 JFMC33-0502 sobre la duración óptima de UFT/LV adyuvante en cáncer de colon estadio IIB/III |
| [15108041](https://pubmed.ncbi.nlm.nih.gov/15108041/) | 2004 | ECA | Int J Clin Oncol | Inmunoquimioterapia adyuvante (OK-432) y quimioterapia con pirimidinas orales (HCFU y UFT) en cáncer colorrectal |
| [33950962](https://pubmed.ncbi.nlm.nih.gov/33950962/) | 2021 | Cohorte y metaanálisis | Medicine | UFT vs 5-FU como adyuvancia en cáncer de colon estadio II y III, con datos del seguro de salud nacional de Taiwán (2000-2015) |
| [38833114](https://pubmed.ncbi.nlm.nih.gov/38833114/) | 2024 | Estudio prospectivo controlado | Int J Clin Oncol | Resultados finales de JFMC46-1201: UFT/LV adyuvante en cáncer de colon estadio II con factores de riesgo; en el análisis previo la supervivencia libre de enfermedad a 3 años fue mayor que con cirugía sola |
| [35168560](https://pubmed.ncbi.nlm.nih.gov/35168560/) | 2022 | Estudio observacional prospectivo | BMC Cancer | UFT/LV frente a cirugía sola en cáncer de colon estadio II de alto riesgo, con emparejamiento por puntaje de propensión |
| [17952521](https://pubmed.ncbi.nlm.nih.gov/17952521/) | 2007 | Revisión | Surg Today | UFT como quimioterapia adyuvante en tumores sólidos: evidencia clínica y mecanismo de acción; su toxicidad leve lo hace adecuado tras la resección completa |
| [6402917](https://pubmed.ncbi.nlm.nih.gov/6402917/) | 1983 | Estudio clínico comparativo aleatorizado | Am J Clin Oncol | Tegafur oral vs 5-FU intravenoso en cáncer colorrectal metastásico |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 54192 | UTEFOS 400 mg cápsulas duras | Cápsula dura | No especificada en los datos disponibles |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (fluoropirimidina, profármaco del 5-FU) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Cribado de deficiencia de DPD (genotipado DPYD); demás parámetros según el prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto; seguir la normativa de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

No hay datos de seguridad extraídos del prospecto de la AEMPS ni interacciones registradas. Los siguientes puntos de atención proceden del análisis de reposicionamiento:

- **Toxicidad relacionada con DPD**: se necesita cribado previo, ya que la deficiencia de DPD aumenta el riesgo de toxicidad grave por fluoropirimidinas.
- **Interacciones farmacológicas a verificar**: warfarina y otras fluoropirimidinas.

Consultar el prospecto para el resto de la información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay varios ensayos de Fase 3 completados (NCT00378716, NCT00392899, NCT00152230, NCT00660894) y ensayos aleatorizados publicados con UFT en cáncer de colon adyuvante, lo que sitúa la evidencia en nivel L1. Los puntos débiles son la falta de indicación registrada en España y la ausencia de datos de seguridad del prospecto.

Las otras nueve predicciones (adenoma velloso de ciego, tumor neuroendocrino G1, lipoma, leiomioma, linfangioma, hemangioma cavernoso, etc.) tienen evidencia L4-L5 y carecen de justificación clínica. Las de enfermedad cecal y neoplasia de la unión rectosigmoidea se solapan con el cáncer colorrectal. Ninguna se recomienda como línea independiente.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), que es el vacío bloqueante para el cribado de seguridad
- Confirmar la indicación autorizada de UTEFOS 400 mg y si incluye cáncer colorrectal
- Obtener datos detallados del mecanismo de acción desde DrugBank
- Definir un plan de cribado de DPD y de revisión de interacciones (warfarina y otras fluoropirimidinas)
- Contrastar los resultados de los ensayos, en su mayoría asiáticos, con la práctica y la población europeas

*Los resultados de este informe son solo para investigación y no constituyen consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

