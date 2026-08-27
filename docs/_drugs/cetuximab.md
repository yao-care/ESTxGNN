---
layout: default
title: Cetuximab
parent: 僅模型預測 (L5)
nav_order: 69
evidence_level: L5
indication_count: 10
---

# Cetuximab
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

# Cetuximab: De Carcinoma Escamoso de Cabeza y Cuello / Colorrectal a Neoplasia Quistica (Carcinoma Adenoide Quistico)

## Resumen en Una Frase

Cetuximab es un anticuerpo monoclonal anti-EGFR, cuyo uso conocido en los datos de ensayos clinicos incluidos corresponde a carcinoma escamoso de cabeza y cuello y a cancer colorrectal metastasico (tumores con sobreexpresion de EGFR). El modelo TxGNN predice, entre 10 indicaciones candidatas, que **Neoplasia Quistica** (particularmente carcinoma adenoide quistico de glandula salival) es la de mayor viabilidad, con **5 ensayos clinicos** y **20 publicaciones** relacionadas, incluyendo un ensayo Fase 1/2 especifico para carcinoma adenoide quistico y un estudio Fase II en carcinomas de glandula salival.

> **Nota sobre el alcance:** este Evidence Pack es un candidato "multi" que agrupa 10 indicaciones predichas por TxGNN para el mismo farmaco. Nueve de ellas no superan el nivel L4/L5 (sin evidencia real o solo mecanistica). Este informe se centra en la indicacion con mayor solidez de evidencia (**Neoplasia Quistica**, L2) y añade una tabla resumen del resto de candidatos para trazabilidad.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | No disponible en registro de licencias en España (0 licencias). Segun descripciones de los ensayos clinicos incluidos, cetuximab es conocido para carcinoma escamoso de cabeza y cuello y cancer colorrectal metastasico |
| Nueva Indicacion Predicha | Neoplasia Quistica (Cystic Neoplasm) — principalmente carcinoma adenoide quistico / carcinomas de glandula salival |
| Puntaje de Prediccion TxGNN | 99.95% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Espana | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Proceed with Guardrails |

### Vision General del Portafolio de Indicaciones Predichas (10 candidatos)

| Rango | Indicacion | Puntaje TxGNN | Nivel Evidencia | Recomendacion |
|------|------|------|------|------|
| 1 | Bronchial adenomas/carcinoids childhood | 99.95% | L5 | Hold |
| 2 | Chondroid hamartoma | 99.95% | L5 | Hold |
| 3 | Ductal or ductular proliferation | 99.95% | L5 | Hold |
| 4 | Non-seminomatous lesion | 99.95% | L5 | Hold |
| 5 | Tumor of testis and paratestis | 99.95% | L5 | Hold |
| 6 | Odontogenic cyst | 99.95% | L4 | Hold |
| 7 | Thyroglossal duct cyst | 99.95% | L5 | Hold |
| 8 | Epiglottis neoplasm | 99.95% | L4 | Hold |
| **9** | **Neoplasia Quistica (foco de este informe)** | **99.95%** | **L2** | **Research Question** |
| 10 | Pre-malignant neoplasm | 99.95% | L4 | Hold |

**Observacion:** todas las indicaciones comparten practicamente el mismo puntaje TxGNN (~99.95%), lo que indica que el puntaje bruto del modelo por si solo no discrimina viabilidad clinica en este lote — la diferenciacion real proviene exclusivamente de la evidencia externa (ensayos/literatura) encontrada para cada indicacion.

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de una ficha detallada del mecanismo de accion (MOA) en la base de datos consultada (data gap de severidad "High"). Segun la informacion recogida en los ensayos clinicos y la literatura del propio Evidence Pack, cetuximab es un **anticuerpo monoclonal quimerico anti-EGFR** que bloquea la senalizacion del receptor del factor de crecimiento epidermico, inhibiendo la proliferacion celular e induciendo apoptosis en tumores con sobreexpresion de EGFR.

Cetuximab ya es una clase de farmaco establecida para carcinoma escamoso de cabeza y cuello (HNSCC) y cancer colorrectal metastasico, ambos caracterizados por sobreexpresion de EGFR. La neoplasia quistica candidata en este informe corresponde principalmente a **carcinoma adenoide quistico (ACC) y otros carcinomas de glandula salival**, tumores del mismo territorio anatomico (cabeza y cuello) que tambien muestran sobreexpresion de EGFR documentada en la literatura (PMID 18804410). Esto proporciona una base farmacologica racional directa, no solo una extrapolacion del modelo.

En contraste, el resto de indicaciones del lote (adenomas bronquiales infantiles, hamartoma condroide, proliferacion ductular hepatica, lesiones no seminomatosas, quiste odontogenico, quiste tirogloso, neoplasias pre-malignas genericas) no presentan relacion mecanistica conocida con la via EGFR o carecen de evidencia clinica real que respalde la prediccion — el propio dataset las clasifica como L4-L5 con recomendacion "Hold".

## Evidencia de Ensayos Clinicos

*(Indicacion: Neoplasia Quistica)*

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01192087](https://clinicaltrials.gov/study/NCT01192087) | Fase 1/2 | Desconocido | 49 | Estudio ACCEPT: tratamiento combinado de carcinoma adenoide quistico con cetuximab + IMRT + refuerzo de iones de carbono (C12); ensayo especifico para el subtipo quistico, mayor especificidad de enfermedad, pero estado "Unknown" reduce certeza |
| [NCT00101348](https://clinicaltrials.gov/study/NCT00101348) | Fase 1/2 | Completado | 66 | Erlotinib + cetuximab +/- bevacizumab en carcinoma renal metastasico y otros tumores solidos; datos de seguridad de doble bloqueo EGFR |
| [NCT00397384](https://clinicaltrials.gov/study/NCT00397384) | Fase 1 | Completado | 43 | Erlotinib + cetuximab en cancer gastrointestinal avanzado, cabeza y cuello, CPNM y colorrectal; datos de dosis y seguridad |
| [NCT01637194](https://clinicaltrials.gov/study/NCT01637194) | Fase 1 | Completado | 12 | Cetuximab + everolimus (RAD001) en tumores solidos metastasicos/recurrentes de colon o cabeza y cuello |
| [NCT00896896](https://clinicaltrials.gov/study/NCT00896896) | N/A | Completado | 538 | Estudio observacional de inmunogenicidad/hipersensibilidad a cetuximab en pacientes con cancer de cabeza y cuello o colorrectal avanzado previamente tratados |

## Evidencia de Literatura

*(Indicacion: Neoplasia Quistica)*

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [18804410](https://pubmed.ncbi.nlm.nih.gov/18804410/) | 2009 | Fase II (brazo unico) | Oral Oncology | Cetuximab en carcinoma de glandula salival recurrente/metastasico (30 pacientes, 23 ACC); sobreexpresion de EGFR como fundamento del tratamiento anti-EGFR |
| [18366287](https://pubmed.ncbi.nlm.nih.gov/18366287/) | 2008 | Revision | Expert Rev Anticancer Ther | Revision de terapias sistemicas para cancer de glandula salival recurrente/metastasico, incluyendo anti-EGFR |
| [22144378](https://pubmed.ncbi.nlm.nih.gov/22144378/) | 2013 | Reporte de caso | Head & Neck | Carcinoma adenoide quistico metastasico de glandula salival con respuesta a cetuximab + paclitaxel semanal tras fallo de paclitaxel solo |
| [32518035](https://pubmed.ncbi.nlm.nih.gov/32518035/) | 2020 | Reporte de caso + revision | Oral Oncology | Monoterapia con cetuximab en carcinoma mucoepidermoide de alto grado en recaida |
| [36675234](https://pubmed.ncbi.nlm.nih.gov/36675234/) | 2023 | Investigacion basica | Int J Mol Sci | Establecimiento de lineas celulares de carcinoma mucoepidermoide (glandula salival) a partir de biopsias quirurgicas y de recurrencia |
| [21234529](https://pubmed.ncbi.nlm.nih.gov/21234529/) | 2011 | Estudio clinico retrospectivo | Strahlenther Onkol | Reirradiacion IMRT con cetuximab concurrente en cancer de cabeza y cuello recurrente |
| [39415301](https://pubmed.ncbi.nlm.nih.gov/39415301/) | 2024 | Reporte de caso | J Med Case Rep | Administracion exitosa de cetuximab mediante escalada de dosis para prevenir reacciones de infusion severas |
| [31983124](https://pubmed.ncbi.nlm.nih.gov/31983124/) | 2019 | Estudio clinico | J BUON | Cetuximab combinado con cisplatino mejora el pronostico en cancer gastrico; efecto sobre expresion de P38 MAPK |
| [30141310](https://pubmed.ncbi.nlm.nih.gov/30141310/) | 2018 | Cohorte retrospectiva | Asian Pac J Cancer Prev | Trastornos cutaneos y localizacion del tumor primario como factores pronosticos en cancer colorrectal metastasico tratado con cetuximab |
| [28320945](https://pubmed.ncbi.nlm.nih.gov/28320945/) | 2017 | Investigacion basica/traslacional | PNAS | Sistema de cultivo 3D identifica nuevo modo de resistencia a cetuximab; lineas celulares con morfologia quistica ("CC") en cancer colorrectal |

## Citotoxicidad

*(Cetuximab es una terapia antineoplasica dirigida — se incluye esta seccion)*

| Item | Contenido |
|------|------|
| Clasificacion de Citotoxicidad | Terapia dirigida (anticuerpo monoclonal anti-EGFR), no es un citotoxico convencional |
| Riesgo de Mielosupresion | Consultar las advertencias y precauciones del prospecto (sin datos de toxicidad hematologica en este Evidence Pack) |
| Clasificacion de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Proteccion en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad. No hay datos de advertencias, contraindicaciones ni interacciones farmacologicas disponibles en este Evidence Pack (incluye un data gap de severidad **Bloqueante**: ausencia del prospecto/ficha tecnica de la AEMPS, lo que impide actualmente la evaluacion de seguridad inicial S1).

## Conclusion y Proximos Pasos

**Decision: Proceed with Guardrails**

**Justificacion:**
La indicacion "Neoplasia Quistica" (carcinoma adenoide quistico / carcinomas de glandula salival) cuenta con una base mecanistica solida (sobreexpresion de EGFR compartida con las indicaciones ya validadas de cetuximab) y evidencia clinica real de nivel L2, incluyendo un estudio Fase II de brazo unico y un ensayo Fase 1/2 especifico para ACC. Sin embargo, el farmaco no esta comercializado en España (0 licencias) y falta el prospecto/ficha de seguridad de la AEMPS (data gap bloqueante), por lo que no puede avanzar sin resolver antes esa brecha regulatoria. Las otras 9 indicaciones predichas por TxGNN no superan L4-L5 y se mantienen en Hold por falta de evidencia real.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha tecnica de cetuximab desde la AEMPS para completar la evaluacion de seguridad S1 (data gap bloqueante DG001)
- Obtener datos formales de mecanismo de accion desde DrugBank (data gap DG002)
- Verificar el estado real de comercializacion de cetuximab en España (el registro de licencias muestra 0, lo cual contrasta con su uso conocido en oncologia a nivel internacional — posible brecha en la fuente de datos regulatorios)
- Clarificar si el termino generico "Neoplasia Quistica" del modelo TxGNN debe acotarse clinicamente a carcinoma adenoide quistico / carcinomas de glandula salival antes de cualquier diseno de estudio
- Dado el estado "Unknown" del ensayo NCT01192087 (el mas especifico para ACC), confirmar su estado actual de reclutamiento/resultados
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

