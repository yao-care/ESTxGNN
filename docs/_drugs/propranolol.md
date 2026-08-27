---
layout: default
title: Propranolol
parent: 僅模型預測 (L5)
nav_order: 231
evidence_level: L5
indication_count: 6
---

# Propranolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Propranolol: De Uso Cardiovascular Establecido a Miocardiopatia (Cardiomyopathy)

## Resumen en Una Frase

Propranolol es un beta-bloqueante no selectivo de uso cardiovascular consolidado (hipertension, angina, arritmias), aunque los datos regulatorios detallados sobre la indicacion original aprobada y el mecanismo de accion no estan disponibles en este paquete de evidencia (brechas DG001 y DG002).
El modelo TxGNN evaluo **6 indicaciones candidatas** de reposicionamiento para este farmaco; la de mayor respaldo es **Miocardiopatia (Cardiomyopathy)**,
con **3 ensayos clinicos** y **20 publicaciones** que actualmente respaldan esta direccion, alcanzando un nivel de evidencia **L2**.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | No disponible en este informe (brecha de datos DG001, bloqueante); propranolol es clinicamente conocido como beta-bloqueante de uso cardiovascular general |
| Nueva Indicacion Predicha | Miocardiopatia (Cardiomyopathy) |
| Puntaje de Prediccion TxGNN | 99.12% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Espana | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Proceed with Guardrails |

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion procedentes de este informe (brecha DG002, severidad Alta), ni de la indicacion original aprobada segun fuentes regulatorias (brecha DG001, severidad Bloqueante). Segun la informacion farmacologica ampliamente establecida, propranolol es un beta-bloqueante no selectivo (antagonista de los receptores adrenergicos beta-1 y beta-2) cuyo uso clinico clasico abarca hipertension arterial, angina de pecho y arritmias, y mecanisticamente podria ser aplicable a la miocardiopatia hipertrofica obstructiva (HOCM), donde el bloqueo beta reduce la contractilidad miocardica, la frecuencia cardiaca y el gradiente de presion en el tracto de salida del ventriculo izquierdo.

De hecho, la HOCM es una indicacion de uso clinico consolidado para propranolol desde hace decadas (efecto de clase de los beta-bloqueantes), lo que respalda razonablemente la prediccion de TxGNN para la categoria mas amplia de "cardiomyopathy". Sin embargo, este termino agrupa subtipos heterogeneos (hipertrofica obstructiva, dilatada, mitocondrial), y la evidencia disponible se concentra mayoritariamente en HOCM con estudios hemodinamicos antiguos (decadas 1970-1990), mientras que los ensayos de fase 3/4 mas recientes se orientan a la **desprescripcion** de beta-bloqueantes en HFpEF y amiloidosis cardiaca, no a validar una nueva indicacion.

---

## Evidencia de Ensayos Clinicos

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT05019027](https://clinicaltrials.gov/study/NCT05019027) | Fase 4 | Reclutando por invitacion | 20 | Ensayos N-of-1 de desprescripcion de beta-bloqueante en amiloidosis cardiaca por transtiretina (relevancia C: no evalua propranolol como tratamiento de novo) |
| [NCT05427474](https://clinicaltrials.gov/study/NCT05427474) | Fase 3 | Desconocido | 90 | Terapia combinada propranolol + gabapentina en hiperactividad simpatica paroxistica tras traumatismo craneoencefalico (relevancia C: no es miocardiopatia) |
| [NCT04767061](https://clinicaltrials.gov/study/NCT04767061) | Fase 4 | Completado | 9 | Ensayos N-of-1 de desprescripcion de beta-bloqueantes en insuficiencia cardiaca con fraccion de eyeccion preservada (HFpEF) (relevancia C: no valida nueva indicacion) |

*Nota: los tres ensayos disponibles evaluan la retirada de beta-bloqueantes o usos no relacionados, no la eficacia terapeutica de propranolol para miocardiopatia de novo.*

---

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [7200796](https://pubmed.ncbi.nlm.nih.gov/7200796/) | 1982 | ECA | British Heart Journal | Nifedipino + propranolol combinados superan a nifedipino solo en miocardiopatia hipertrofica obstructiva (HOCM) |
| [8989641](https://pubmed.ncbi.nlm.nih.gov/8989641/) | 1996 | Cohorte | Journal of Cardiac Failure | Predictores hemodinamicos de intolerancia temprana y efectos a largo plazo de propranolol en miocardiopatia dilatada |
| [36104228](https://pubmed.ncbi.nlm.nih.gov/36104228/) | 2022 | Reporte de Caso | International Heart Journal | Miocardiopatia mitocondrial infantil tratada con propranolol a baja dosis + cibenzolina por estenosis del tracto de salida del VI |
| [10460081](https://pubmed.ncbi.nlm.nih.gov/10460081/) | 1999 | Reporte de Caso | Pediatric Emergency Care | Miocardiopatia dilatada aguda y toxicidad del SNC tras intoxicacion por propranolol |
| [2019674](https://pubmed.ncbi.nlm.nih.gov/2019674/) | 1991 | Preclinico/Animal | Journal of Comparative Pathology | Cambios morfologicos en miocardiopatia inducida por furazolidona: efectos de digoxina y propranolol |
| [6686544](https://pubmed.ncbi.nlm.nih.gov/6686544/) | 1983 | No clasificado | European Heart Journal | Propranolol reduce la rigidez diastolica del ventriculo izquierdo en HCM, comparado con verapamilo |
| [7192151](https://pubmed.ncbi.nlm.nih.gov/7192151/) | 1980 | No clasificado | British Heart Journal | Efectos de propranolol sobre el consumo de oxigeno miocardico y hemodinamica en HOCM |
| [1611637](https://pubmed.ncbi.nlm.nih.gov/1611637/) | 1992 | No clasificado | Cardiology | Propranolol + disopiramida mejoran la funcion ventricular izquierda en reposo y ejercicio en HCM |
| [11300365](https://pubmed.ncbi.nlm.nih.gov/11300365/) | 2000 | No clasificado | Cardiovascular Drugs and Therapy | Comparacion de verapamilo y propranolol sobre vasomocion coronaria en HCM sintomatica |
| [3189143](https://pubmed.ncbi.nlm.nih.gov/3189143/) | 1988 | No clasificado | American Heart Journal | Efectos hemodinamicos agudos de pindolol vs. propranolol en miocardiopatia dilatada |

---

## Otros Candidatos Evaluados en Este Paquete

Este paquete de evidencia es multi-indicacion. Ademas de miocardiopatia (candidato principal arriba), TxGNN identifico 5 candidatos adicionales, con evidencia mucho mas limitada:

| Indicacion | Puntaje TxGNN | Nivel de Evidencia | Recomendacion | Nota |
|---|---|---|---|---|
| Miocardiopatia cirrotica | 99.12% | L3 | Proceed with Guardrails | 5 publicaciones observacionales; el beta-bloqueo puede corregir el QTc prolongado pero tambien empeorar la hemodinamica renal en ascitis refractaria |
| Miocardiopatia hipertrofica por entrenamiento deportivo intensivo | 99.17% | L4 | Research Question | Extrapolacion del efecto de clase en HCM; sin estudios especificos de este subtipo |
| Distrofia muscular distal tipo Tateyama | 99.40% | L5 | Hold | Sin conexion mecanistica conocida; probable artefacto de proximidad en el grafo de conocimiento |
| Miopatia congenita con exceso de filamentos finos | 99.30% | L5 | Hold | Sin conexion mecanistica ni evidencia clinica |
| Condroma | 99.14% | L5 | Hold | El mecanismo antiangiogenico util en hemangioma infantil no es aplicable a tumores de origen condrocitico |

---

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

---

## Conclusion y Proximos Pasos

**Decision: Proceed with Guardrails**

**Justificacion:**
El uso de beta-bloqueantes en el subtipo HOCM esta clinicamente bien establecido y respalda la senal de TxGNN para "cardiomyopathy" (L2), pero la evidencia disponible es heterogenea, mayormente antigua (1970-1990), y los ensayos de fase 3/4 actuales se centran en desprescripcion, no en nueva indicacion.

**Para avanzar se necesita:**
- Resolver la brecha DG001 (advertencias/contraindicaciones del prospecto) antes de cualquier evaluacion de seguridad S1
- Completar la brecha DG002 (mecanismo de accion detallado de DrugBank)
- Estratificar la evidencia por subtipo de miocardiopatia (HOCM vs. dilatada vs. mitocondrial) antes de una decision definitiva
- Evaluar miocardiopatia cirrotica (L3) como via secundaria si el subtipo HOCM se confirma como el mecanismo dominante
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

