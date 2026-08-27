---
layout: default
title: Sorafenib
parent: 僅模型預測 (L5)
nav_order: 263
evidence_level: L5
indication_count: 10
---

# Sorafenib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# SORAFENIB: De Carcinoma Hepatocelular/Renal a Liposarcoma

## Resumen en Una Frase

Sorafenib es un inhibidor multiquinasa oral ya establecido para el tratamiento del carcinoma hepatocelular y el carcinoma de células renales avanzado. El modelo TxGNN predice que también podría ser efectivo para el **Liposarcoma**, con **2 ensayos clínicos** (1 realizado directamente con sorafenib, Fase II) y **8 publicaciones** que respaldan actualmente esta dirección, en su mayoría de carácter preclínico y mecanístico.

> Nota: este Evidence Pack corresponde a un candidato **multi-indicación** (10 enfermedades predichas). El presente informe desarrolla en detalle la indicación de mayor puntuación TxGNN (Liposarcoma, rank 1) según el formato estándar, e incluye un anexo comparativo con las otras 9 indicaciones evaluadas.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Carcinoma hepatocelular y carcinoma de células renales avanzado (mencionado de forma consistente en la literatura de referencia recopilada; el campo estructurado de indicación original no fue registrado en este Evidence Pack) |
| Nueva Indicacion Predicha | Liposarcoma |
| Puntaje de Prediccion TxGNN | 99.82% (rank 3756) |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Research Question (requiere más investigación) |

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos estructurados sobre el mecanismo de acción (MOA) de sorafenib en este Evidence Pack (data gap de alta severidad, DG002). Sin embargo, según la literatura recopilada, sorafenib es un inhibidor multiquinasa oral que actúa sobre CRAF/BRAF, VEGFR-1/2/3, PDGFR-β, KIT y RET, combinando actividad antiangiogénica y antiproliferativa (Wilhelm et al., 2004, PMID 15466206). Este mecanismo sustenta su uso ya establecido en el carcinoma hepatocelular y el carcinoma de células renales avanzado.

El liposarcoma, especialmente su subtipo desdiferenciado, se asocia a alteraciones de las vías PDGFR y PTEN. Dado que sorafenib inhibe PDGFR y la señalización RAF/MEK/ERK, existe una base mecanística razonable para su actividad en sarcomas de tejido blando (STS) en general, aunque el liposarcoma no es su indicación principal aprobada.

Esta hipótesis cuenta con respaldo clínico parcial: el ensayo intergrupo Fase II SWOG S0505 (PMID 21751200) evaluó sorafenib en sarcomas de tejido blando avanzados, y el estudio BAY 43-9006 (NCT00217620, Fase II, completado, n=51) usó sorafenib directamente en sarcomas de tejido blando avanzados. No obstante, la mayoría de la evidencia específica de liposarcoma es aún preclínica (líneas celulares y modelos de xenoinjerto), por lo que la extrapolación al liposarcoma como entidad específica —y no solo a los STS en general— sigue siendo una hipótesis de investigación.

---

## Evidencia de Ensayos Clinicos

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Fase 2 | Completado | 51 | BAY 43-9006 (sorafenib) evaluado directamente en sarcomas de tejido blando avanzados; sorafenib bloquea enzimas de crecimiento tumoral y el flujo sanguíneo al tumor. Evidencia directa del mismo fármaco (grado de relevancia A). |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Fase 2 | Completado | 131 | Estudio SARC024 sobre regorafenib oral (análogo estructural de sorafenib, no el mismo compuesto) en subtipos seleccionados de sarcoma; aporta evidencia de clase, no evidencia directa (grado de relevancia C). |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21751200](https://pubmed.ncbi.nlm.nih.gov/21751200/) | 2012 | Ensayo Fase 2 (SWOG S0505, intergrupo) | Cancer | Sorafenib (BAY 43-9006), inhibidor multiquinasa de RAF/VEGFR1-3/PDGFR-β/FLT3/KIT, evaluado en sarcomas de tejido blando avanzados con opciones terapéuticas limitadas. |
| [24554062](https://pubmed.ncbi.nlm.nih.gov/24554062/) | 2014 | Ensayo Fase 1 | Annals of Surgical Oncology | Radioterapia conformal neoadyuvante combinada con sorafenib en sarcoma de tejido blando de extremidad localmente avanzado; sinergia preclínica entre antiangiogénicos y radioterapia. |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Revisión | Annals of Oncology | Tratamiento de sarcomas de tejido blando dirigido por histología; trabectedina muestra actividad especialmente alta en liposarcoma mixoide. |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Revisión | Magyar Onkologia | Tratamiento médico de sarcomas de tejido blando según subtipo histológico; contextualiza el uso de terapias dirigidas junto a citotóxicos clásicos. |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Revisión | Frontiers in Oncology | Modelos PDOX (xenoinjerto ortotópico derivado de paciente) de sarcoma identifican combinaciones novedosas con el inhibidor de CDK palbociclib. |
| [18413802](https://pubmed.ncbi.nlm.nih.gov/18413802/) | 2008 | Preclínico | Molecular Cancer Therapeutics | Sorafenib inhibe el crecimiento y la señalización MAPK en células de tumor de la vaina nerviosa periférica maligno (MPNST) y en líneas celulares de liposarcoma desdiferenciado (LS141, DDLS). |
| [23416162](https://pubmed.ncbi.nlm.nih.gov/23416162/) | 2013 | Preclínico (xenoinjerto) | The American Journal of Pathology | Modelos de xenoinjerto de liposarcoma desdiferenciado revelan la disminución de PTEN como firma maligna y respuesta a la inhibición de la vía PI3K. |
| [25075796](https://pubmed.ncbi.nlm.nih.gov/25075796/) | 2014 | Reporte de caso (fármaco distinto) | Anti-Cancer Drugs | Respuesta a trabectedina (no sorafenib) en sarcoma sinovial avanzado con metástasis pulmonares; se incluye como contexto de la clase terapéutica en STS. |

---

## Informacion de Mercado en España

Sorafenib no está actualmente comercializado en España según este Evidence Pack: **0 autorizaciones** registradas y `market_status = "no comercializado"`. No se dispone de datos de licencias AEMPS para este análisis.

---

## Citotoxicidad

Sorafenib es un fármaco antineoplásico (inhibidor multiquinasa oral utilizado en oncología), por lo que aplica esta sección.

| Item | Contenido |
|------|------|
| Clasificacion de Citotoxicidad | Terapia dirigida (inhibidor multiquinasa oral de CRAF/BRAF, VEGFR-1/2/3, PDGFR-β, KIT, RET) — no es un citotóxico convencional |
| Riesgo de Mielosupresion | Consultar las advertencias y precauciones del prospecto |
| Clasificacion de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Proteccion en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Cabe destacar que la falta de datos de advertencias/contraindicaciones de TFDA/AEMPS está marcada en este Evidence Pack como una **brecha de datos bloqueante (DG001)**, lo que impide actualmente completar la evaluación de seguridad inicial (S1).

---

## Conclusion y Proximos Pasos

**Decisión: Research Question**

**Justificación:**
Existe una base mecanística razonable (inhibición de PDGFR y RAF/MEK/ERK) y un ensayo Fase II completado con sorafenib directamente en sarcomas de tejido blando avanzados, pero la evidencia específica para liposarcoma es mayormente preclínica. Además, el fármaco no está comercializado en España y falta información de seguridad bloqueante, por lo que no es posible avanzar más allá de una pregunta de investigación en este momento.

**Para avanzar se necesita:**
- Ficha técnica/prospecto con advertencias y contraindicaciones (brecha bloqueante, DG001)
- Confirmación estructurada del mecanismo de acción (DG002)
- Datos clínicos específicos de liposarcoma (no solo sarcoma de tejido blando en general)
- Evaluación de la vía regulatoria en España, dado que el fármaco no está comercializado

---

## Anexo: Otras Indicaciones Predichas Evaluadas

Este candidato incluye 10 indicaciones predichas por TxGNN. A continuación se resumen las 9 restantes para contexto comparativo:

| Rank | Enfermedad | Puntaje TxGNN | Nivel de Evidencia | Etapa de Decisión | Recomendación |
|------|-----------|--------------|--------------------|--------------------|----------------|
| 2 | Liposarcoma mixoide ovárico | 99.76% | L5 | S0 | Hold |
| 3 | Carcinoma de células renales asociado a neuroblastoma | 99.65% | L5 | S0 | Hold |
| 4 | Carcinoma de células renales no clasificado | 99.65% | **L1** | **S3** | **Proceed with Guardrails** |
| 5 | Carcinoma renal asociado a translocaciones Xp11.2/fusiones TFE3 | 99.65% | L5 | S0 | Hold |
| 6 | Carcinoma de células renales infantil | 99.57% | L3 | S1 | Research Question |
| 7 | Carcinoma de mama femenino | 99.53% | L2 | S2 | Hold |
| 8 | Carcinoma de pelvis renal | 99.40% | L2 | S2 | Research Question |
| 9 | Sarcoma de vulva | 99.37% | L5 | S0 | Hold |
| 10 | Dermatofibrosarcoma protuberans | 99.35% | L4 | S1 | Research Question |

**Observación relevante:** aunque el liposarcoma (rank 1) tiene el puntaje TxGNN más alto, el candidato con **mayor solidez de evidencia real** es el **carcinoma de células renales no clasificado** (rank 4): cuenta con un ensayo Fase III aleatorizado y completado (NCT01613846, n=544) que evalúa sorafenib en carcinoma renal avanzado/metastásico, además de literatura de cohorte de apoyo. Este candidato alcanza el nivel de evidencia L1 y la etapa de decisión S3 ("Proceed with Guardrails"), por lo que se recomienda priorizarlo para la siguiente fase de evaluación, en paralelo al seguimiento del liposarcoma como hipótesis de investigación.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

