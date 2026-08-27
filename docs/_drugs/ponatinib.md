---
layout: default
title: Ponatinib
parent: 僅模型預測 (L5)
nav_order: 227
evidence_level: L5
indication_count: 2
---

# Ponatinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Ponatinib (DB08901): Evaluacion de Reposicionamiento hacia Fibromatosis Gingival y Liposarcoma

## Resumen en Una Frase

Ponatinib es un inhibidor de tirosina-quinasas actualmente **no comercializado en Espana**; el Evidence Pack no registra su indicacion original ni su mecanismo de accion (ambos marcados como Data Gap). El modelo TxGNN predice dos posibles nuevas indicaciones oncologicas: **Fibromatosis Gingival** (score 99.04%) y **Liposarcoma** (score 99.00%). La evidencia real que las respalda es minima: cero ensayos clinicos y cero publicaciones para fibromatosis gingival, y solo **1 estudio preclinico** (no especifico de ponatinib) para liposarcoma.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | No disponible en el Evidence Pack (drug.original_indications vacio; original_moa = Data Gap) |
| Nueva Indicacion Predicha (Principal) | Fibromatosis Gingival |
| Puntaje de Prediccion TxGNN (Principal) | 99.04% |
| Nueva Indicacion Predicha (Secundaria) | Liposarcoma |
| Puntaje de Prediccion TxGNN (Secundaria) | 99.00% |
| Nivel de Evidencia | L5 (Fibromatosis Gingival) / L4 (Liposarcoma) |
| Estado de Mercado en Espana | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold (ambas indicaciones) |

## Por que es Razonable esta Prediccion?

El Evidence Pack no contiene datos del mecanismo de accion (original_moa = Data Gap) ni de la indicacion original del farmaco. A modo de contexto general (informacion no incluida en este Evidence Pack), ponatinib es conocido publicamente como un inhibidor de tirosina-quinasas de tercera generacion con multiples dianas (incluyendo BCR-ABL, FGFR1-4, VEGFR2, PDGFRalfa, KIT, SRC, FLT3 y RET), segun se describe en la justificacion mecanistica asociada a la prediccion de liposarcoma.

Para **Fibromatosis Gingival**, el propio analisis del candidato concluye que no existe base mecanistica alguna: no hay ensayos clinicos ni literatura, y faltan tanto el MOA como la indicacion original del farmaco. La prediccion proviene unicamente de la puntuacion del modelo TxGNN, sin ningun soporte bibliografico que permita construir un argumento de plausibilidad biologica.

Para **Liposarcoma**, el fundamento es algo mas solido pero sigue siendo indirecto: dado que ponatinib inhibe multiples quinasas, y que un estudio preclinico de cribado de quinasas (RNAi y farmacos) en lineas celulares de liposarcoma identifico dianas quinasa potencialmente tratables, existe una hipotesis mecanistica de clase razonable. Sin embargo, ese estudio no evaluo ponatinib especificamente en modelos de liposarcoma, por lo que la relacion sigue siendo teorica y de bajo nivel de evidencia.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados, ni para Fibromatosis Gingival ni para Liposarcoma (busquedas en ClinicalTrials.gov e ICTRP con 0 resultados para ambas indicaciones).

## Evidencia de Literatura

**Fibromatosis Gingival:** Actualmente no hay literatura relacionada disponible.

**Liposarcoma:**

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29132397](https://pubmed.ncbi.nlm.nih.gov/29132397/) | 2017 | Preclinico (cribado in vitro RNAi/farmacos) | Journal of Hematology & Oncology | Cribado de quinasas mediante RNAi y farmacos en lineas celulares de liposarcoma identifico dianas quinasa potencialmente tratables; el estudio no evalua ponatinib de forma especifica. |

## Informacion de Mercado en Espana

Ponatinib no esta actualmente comercializado en Espana (0 autorizaciones registradas en el Evidence Pack).

## Citotoxicidad

Ponatinib es un inhibidor de tirosina-quinasas de uso oncologico (terapia dirigida), por lo que se incluye esta seccion. El Evidence Pack no aporta datos de toxicidad especificos:

| Item | Contenido |
|------|------|
| Clasificacion de Citotoxicidad | Terapia dirigida (inhibidor de tirosina-quinasas multi-diana) |
| Riesgo de Mielosupresion | Consultar las advertencias y precauciones del prospecto |
| Clasificacion de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Proteccion en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

El prospecto (ficha tecnica) de ponatinib fue localizado en TFDA pero aun no ha sido analizado de forma estructurada (advertencias, contraindicaciones e interacciones farmacologicas pendientes de extraccion). Consultar el prospecto para informacion de seguridad.

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
Ninguna de las dos indicaciones cuenta con evidencia clinica real (0 ensayos en ambas). Fibromatosis Gingival carece totalmente de literatura y de base mecanistica (L5); Liposarcoma solo dispone de 1 estudio preclinico no especifico de ponatinib (L4). Ademas, faltan datos criticos de seguridad y MOA (gap bloqueante segun el Evidence Pack), lo que impide avanzar a una evaluacion de seguridad S1.

**Para avanzar se necesita:**
- Ficha tecnica de TFDA/AEMPS con advertencias y contraindicaciones analizadas (gap bloqueante DG001)
- Datos de mecanismo de accion del farmaco (DG002)
- Estudios preclinicos o clinicos que evaluen ponatinib especificamente en liposarcoma
- Cualquier evidencia clinica o mecanistica minima para Fibromatosis Gingival antes de continuar la evaluacion
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

