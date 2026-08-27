---
layout: default
title: Panobinostat
parent: 僅模型預測 (L5)
nav_order: 211
evidence_level: L5
indication_count: 1
---

# Panobinostat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Usando el Evidence Pack proporcionado, genero el informe siguiendo el formato v5. Aviso breve: `original_indications` y `original_moa` vienen vacíos/`[Data Gap]` en el pack (DG002), y no hay licencias en España (`taiwan_regulatory.licenses` vacío), así que ajusto el título y omito los campos sin dato en vez de inventarlos.

---

# Panobinostat: Hacia una Nueva Indicacion en Leucemia Mieloide

## Resumen en Una Frase

Panobinostat es un inhibidor pan-HDAC (histona deacetilasa) actualmente sin comercializacion registrada en Espana y sin datos de indicacion original disponibles en esta evaluacion.
El modelo TxGNN predice que podria ser efectivo para **Leucemia Mieloide**,
con **19 ensayos clinicos** y **20 publicaciones** que actualmente respaldan esta direccion.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Sin datos disponibles en este Evidence Pack (dato pendiente, ver DG002) |
| Nueva Indicacion Predicha | Leucemia Mieloide (myeloid leukemia) |
| Puntaje de Prediccion TxGNN | 99.70% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Espana | Sin comercializar |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion en las fuentes consultadas (DrugBank no devolvio el campo de MOA en esta consulta). Segun la informacion recogida de los propios ensayos clinicos del pack, panobinostat es descrito repetidamente como un "inhibidor de histona deacetilasa (HDAC)" que bloquea enzimas necesarias para el crecimiento celular, deteniendo la division de celulas cancerosas e induciendolas a morir.

La evidencia clinica disponible se concentra casi en su totalidad en neoplasias mieloides: leucemia mieloide aguda (LMA), sindromes mielodisplasicos (SMD) y leucemia mieloide cronica (LMC), tanto en monoterapia como en combinacion con azacitidina, decitabina, citarabina, idarubicina o mitoxantrona. Esto sugiere que la actividad antileucemica de panobinostat en neoplasias mieloides ya esta ampliamente explorada en la practica clinica, mas alla de ser una prediccion puramente computacional.

Mecanisticamente, la inhibicion de HDAC modula la expresion genica relacionada con apoptosis y diferenciacion celular en progenitores mieloides malignos, lo cual es coherente con el uso extendido del farmaco en combinacion con hipometilantes (azacitidina, decitabina) en SMD/LMA, reforzando la plausibilidad biologica de la prediccion de TxGNN.

---

## Evidencia de Ensayos Clinicos

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04326764](https://clinicaltrials.gov/study/NCT04326764) | Fase 3 | Terminado | 52 | Panobinostat de mantenimiento vs. estandar de cuidado tras trasplante alogenico en LMA/SMD de alto riesgo (ETAL-4/HOVON-145) |
| [NCT00621244](https://clinicaltrials.gov/study/NCT00621244) | Fase 1/2 | Completado | 175 | Escalada de dosis oral en malignidades hematologicas avanzadas; seguridad, farmacocinetica y actividad antileucemica preliminar |
| [NCT00946647](https://clinicaltrials.gov/study/NCT00946647) | Fase 1b/2b | Completado | 113 | Ensayo aleatorizado: panobinostat + azacitidina vs. azacitidina sola en SMD/LMMC/LMA |
| [NCT02386800](https://clinicaltrials.gov/study/NCT02386800) | Fase 4 | En curso (no reclutando) | 279 | Estudio de seguridad a largo plazo en pacientes tratados con ruxolitinib +/- panobinostat |
| [NCT00691938](https://clinicaltrials.gov/study/NCT00691938) | Fase 1/2 | Completado | 52 | Combinacion con decitabina en pacientes ≥60 anos con SMD/LMA de alto riesgo |
| [NCT01451268](https://clinicaltrials.gov/study/NCT01451268) | Fase 1/2 | Desconocido | 62 | Terapia de mantenimiento oral post-trasplante alogenico en SMD/LMA de alto riesgo (PANOBEST) |
| [NCT01055483](https://clinicaltrials.gov/study/NCT01055483) | Fase 1 | Completado | 59 | Combinacion con Ara-C y mitoxantrona como terapia de rescate en LMA refractaria/recidivante |
| [NCT00880269](https://clinicaltrials.gov/study/NCT00880269) | Fase 2 | Completado | 59 | Monoterapia oral en LMA refractaria de novo o secundaria |
| [NCT00840346](https://clinicaltrials.gov/study/NCT00840346) | Fase 1/2 | Completado | 46 | Combinacion con idarubicina y citarabina en LMA de nuevo diagnostico ≥65 anos |
| [NCT01242774](https://clinicaltrials.gov/study/NCT01242774) | Fase 1 | Completado | 46 | Combinacion con idarubicina/citarabina en induccion y citarabina en dosis alta en consolidacion, LMA ≤65 anos |

---

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29051280](https://pubmed.ncbi.nlm.nih.gov/29051280/) | 2018 | Estudio clinico | Haematologica | Resultados de dos ensayos clinicos con panobinostat en monoterapia y combinacion en LMA |
| [26160880](https://pubmed.ncbi.nlm.nih.gov/26160880/) | 2015 | Estudio clinico (Fase Ib/II) | Haematologica | Panobinostat en induccion y mantenimiento en LMA de nuevo diagnostico en pacientes de edad avanzada |
| [31541945](https://pubmed.ncbi.nlm.nih.gov/31541945/) | 2019 | Estudio clinico | Leukemia research | Seguridad y eficacia de panobinostat oral + quimioterapia en LMA de alto riesgo ≤65 anos |
| [32809242](https://pubmed.ncbi.nlm.nih.gov/32809242/) | 2020 | Estudio clinico | Cancer | Seguridad, farmacocinetica y farmacodinamia en ninos/adolescentes/adultos jovenes con LMA recidivante |
| [24297862](https://pubmed.ncbi.nlm.nih.gov/24297862/) | 2014 | Estudio clinico/traslacional | Clinical Cancer Research | Azacitidina + panobinostat reduce Tregs TNFR2+ con beneficio clinico en LMA |
| [38965693](https://pubmed.ncbi.nlm.nih.gov/38965693/) | 2024 | Guia clinica | Pediatric Blood & Cancer | Guia de tratamiento de leucemia mieloide recidivante/refractaria en Sindrome de Down (incluye AZA +/- panobinostat) |
| [23826641](https://pubmed.ncbi.nlm.nih.gov/23826641/) | 2013 | Revision | Expert Opinion on Investigational Drugs | Revision de panobinostat en malignidades linfoides y mieloides |
| [31739588](https://pubmed.ncbi.nlm.nih.gov/31739588/) | 2019 | Revision | Cancers | Revision de inhibidores de HDAC en LMA |
| [27485472](https://pubmed.ncbi.nlm.nih.gov/27485472/) | 2016 | Revision | Expert Opinion on Investigational Drugs | Revision del uso de panobinostat en el tratamiento de LMA |
| [35311997](https://pubmed.ncbi.nlm.nih.gov/35311997/) | 2022 | Preclinico/mecanistico | Cancer Discovery | Activacion epigenetica de celulas dendriticas plasmocitoides mediada por panobinostat, dependiente de IFNAR, en LMA |

---

## Citotoxicidad

*Panobinostat se clasifica como antineoplasico: pertenece a la clase de los inhibidores de histona deacetilasa (HDAC), descritos explicitamente como agentes antineoplasicos en la evidencia de literatura del pack (PMID 23826641), y toda su evidencia clinica es en neoplasias hematologicas malignas.*

| Item | Contenido |
|------|------|
| Clasificacion de Citotoxicidad | Terapia dirigida (inhibidor pan-HDAC) |
| Riesgo de Mielosupresion | Consultar las advertencias y precauciones del prospecto |
| Clasificacion de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Proteccion en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad. (No se dispone de advertencias, contraindicaciones ni interacciones farmacologicas confirmadas en las fuentes consultadas; la busqueda de DDI no arrojo resultados.)

---

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
Existe evidencia clinica sustancial en neoplasias mieloides (19 ensayos, incluyendo un ensayo aleatorizado Fase 1b/2b completado y un Fase 3 terminado), pero falta informacion critica de seguridad (advertencias y contraindicaciones del TFDA — brecha bloqueante DG001), lo que impide completar la evaluacion inicial de seguridad (S1). El farmaco tampoco esta comercializado actualmente en Espana.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha tecnica oficial con advertencias y contraindicaciones (DG001, bloqueante)
- Completar el mecanismo de accion (MOA) desde DrugBank (DG002)
- Confirmar indicacion(es) original(es) aprobada(s) del farmaco
- Revisar por que el ensayo Fase 3 (NCT04326764) fue terminado antes de avanzar la decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

