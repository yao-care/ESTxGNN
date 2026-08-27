---
layout: default
title: Ustekinumab
parent: 僅模型預測 (L5)
nav_order: 290
evidence_level: L5
indication_count: 10
---

# Ustekinumab
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

# Ustekinumab: De Psoriasis a Dermatitis

## Resumen en Una Frase

Ustekinumab es un anticuerpo monoclonal antagonista de interleucina-12/23, originalmente utilizado para el tratamiento de la psoriasis en placas de moderada a grave (y otras indicaciones inmunomediadas como artritis psoriásica, enfermedad de Crohn y colitis ulcerosa).
El modelo TxGNN predice que podria ser efectivo para **Dermatitis** (principalmente dermatitis atopica),
con **7 ensayos clinicos** y **20 publicaciones** que actualmente respaldan esta direccion.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Psoriasis en placas de moderada a grave (segun literatura de respaldo; artritis psoriasica, enfermedad de Crohn y colitis ulcerosa tambien descritas) |
| Nueva Indicacion Predicha | Dermatitis (principalmente dermatitis atopica) |
| Puntaje de Prediccion TxGNN | 99.99% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Espana | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Proceed with Guardrails |

---

## Por que es Razonable esta Prediccion?

Segun la informacion conocida y la literatura de respaldo, ustekinumab es un anticuerpo monoclonal IgG1 dirigido contra la subunidad p40 compartida por las interleucinas IL-12 e IL-23, lo que le permite suprimir la activacion de las vias Th1, Th17 y Th22. Esta accion inmunomoduladora es la base de su eficacia comprobada en psoriasis en placas, una enfermedad inflamatoria cutanea mediada en gran parte por estas mismas vias.

La dermatitis atopica comparte con la psoriasis un componente inflamatorio cutaneo cronico, con activacion superpuesta de las vias Th17 y Th22 (ademas de la via Th2 predominante en dermatitis atopica). Esta similitud mecanistica es la razon por la que multiples grupos de investigacion han evaluado directamente ustekinumab en dermatitis atopica moderada a grave, con resultados documentados en ensayos clinicos de fase 2 en poblaciones adultas y japonesas.

No obstante, la evidencia real-world muestra resultados mixtos: mientras algunos estudios controlados documentan reduccion de biomarcadores Th2/Th22, otras series de casos describen resultados anecdoticos con eficacia inconsistente frente a la dermatitis atopica, a diferencia de la solidez de la evidencia en psoriasis.

---

## Evidencia de Ensayos Clinicos

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02074982](https://clinicaltrials.gov/study/NCT02074982) | Fase 3 | Completado | 676 | Estudio CLEAR: secukinumab vs. ustekinumab en psoriasis en placas moderada a grave (evidencia de perfil comparativo, no de dermatitis atopica) |
| [NCT01945086](https://clinicaltrials.gov/study/NCT01945086) | Fase 2 | Completado | 79 | Ustekinumab vs. placebo en dermatitis atopica grave en poblacion japonesa adulta |
| [NCT01806662](https://clinicaltrials.gov/study/NCT01806662) | Fase 2 | Completado | 32 | Estudio piloto aleatorizado de ustekinumab en dermatitis atopica cronica con respuesta subóptima a terapia previa |
| [NCT05535738](https://clinicaltrials.gov/study/NCT05535738) | Fase 2/3 | En curso | 45 | Modelo de dermatitis de contacto con biologicos para estudiar inflamacion cutanea mediante ampollas por succion |
| [NCT01356758](https://clinicaltrials.gov/study/NCT01356758) | N/A | Completado | 126 | Evaluacion de riesgo cardiovascular en psoriasis grave tratada con agentes biologicos |
| [NCT07041112](https://clinicaltrials.gov/study/NCT07041112) | N/A | Completado | 1000 | Estudio observacional retrospectivo sobre supervivencia a 10 anos de terapias biologicas en psoriasis cutanea |
| [NCT07352566](https://clinicaltrials.gov/study/NCT07352566) | Fase 4 | Aun no reclutando | 10 | Microdispositivo cutaneo para testar farmacos aprobados en dermatitis atopica y psoriasis |

---

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27304428](https://pubmed.ncbi.nlm.nih.gov/27304428/) | 2017 | ECA | Experimental dermatology | Ensayo fase 2 doble ciego controlado con placebo: eficacia y seguridad de ustekinumab en dermatitis atopica moderada a grave |
| [28338223](https://pubmed.ncbi.nlm.nih.gov/28338223/) | 2017 | ECA | British Journal of Dermatology | Ensayo fase 2 aleatorizado en pacientes japoneses con dermatitis atopica grave |
| [33074565](https://pubmed.ncbi.nlm.nih.gov/33074565/) | 2021 | Revision sistematica | Allergy | Revision sistematica y metaanalisis de tratamientos sistemicos para dermatitis atopica (base de guia clinica EAACI) |
| [29164954](https://pubmed.ncbi.nlm.nih.gov/29164954/) | 2018 | Revision sistematica | J Dermatolog Treat | Revision sistematica de ustekinumab en el tratamiento de dermatitis atopica |
| [29098604](https://pubmed.ncbi.nlm.nih.gov/29098604/) | 2018 | Revision sistematica | Am J Clin Dermatol | Metaanalisis sobre eficacia de biologicos en dermatitis atopica |
| [36208443](https://pubmed.ncbi.nlm.nih.gov/36208443/) | 2022 | Revision | Dermatologic Therapy | Revision de usos off-label de ustekinumab, confirma indicaciones aprobadas (psoriasis, artritis psoriasica, Crohn, colitis ulcerosa) |
| [33849369](https://pubmed.ncbi.nlm.nih.gov/33849369/) | 2022 | Estudio observacional | J Dermatolog Treat | Efectividad real-world de ustekinumab en dermatitis atopica, con reportes anecdoticos de resultados conflictivos |
| [27745907](https://pubmed.ncbi.nlm.nih.gov/27745907/) | 2017 | Estudio de mecanismo | J Am Acad Dermatol | Ustekinumab reduce expresion de Th2/Th22 en dermatitis atopica grave |
| [39987634](https://pubmed.ncbi.nlm.nih.gov/39987634/) | 2025 | Estudio observacional | Int Immunopharmacol | Analisis de seguridad real-world de ustekinumab en psoriasis y artritis psoriasica (base FAERS) |
| [37929636](https://pubmed.ncbi.nlm.nih.gov/37929636/) | 2024 | Reporte de caso | Australas J Dermatol | Terapia dual con dupilumab y ustekinumab en dermatitis atopica grave y enfermedad de Crohn concurrentes |

---

## Informacion de Mercado en Espana

Ustekinumab actualmente figura como **no comercializado** en los registros consultados para este informe, con **0 autorizaciones** registradas. No hay datos de numero de autorizacion, nombre de producto o forma farmaceutica disponibles para listar.

---

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

---

## Conclusion y Proximos Pasos

**Decision: Proceed with Guardrails**

**Justificacion:**
Existen dos ensayos clinicos de fase 2 completados y multiples revisiones sistematicas que respaldan la aplicacion de ustekinumab en dermatitis atopica, alcanzando el nivel de evidencia L2. Sin embargo, la ausencia de ensayos de fase 3 confirmatorios para esta indicacion especifica, resultados real-world inconsistentes, y la falta critica de datos de seguridad (advertencias, contraindicaciones e interacciones) impiden una recomendacion de avance sin restricciones.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha tecnica oficial (advertencias, contraindicaciones, interacciones) — actualmente bloqueante para la evaluacion de seguridad S1
- Confirmar el mecanismo de accion mediante consulta directa a DrugBank
- Evaluar la viabilidad de un ensayo de fase 3 especifico para dermatitis atopica
- Monitorizar la evidencia real-world adicional dado el patron de resultados conflictivos reportado
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

