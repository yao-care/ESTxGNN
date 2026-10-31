---
layout: default
title: Denosumab
parent: Solo predicción del modelo (L5)
nav_order: 233
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-31
monitor_inn: "DENOSUMAB"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy"]
description: "Denosumab: nueva indicación predicha, Retinopatía diabética no proliferativa grave (severe nonproliferative diabetic retinopathy) (nivel de evidencia L5). Indicación original: No consta en los datos …"
---

# Denosumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Denosumab: Retinopatía diabética no proliferativa grave (severe nonproliferative diabetic retinopathy)
{: .text-alpha }

## Resumen en Una Frase

Denosumab es un anticuerpo monoclonal utilizado originalmente para el tratamiento de la osteoporosis (incluida la posmenopáusica y la inducida por fármacos).
El modelo TxGNN predice que podría ser efectivo para la **retinopatía diabética no proliferativa grave**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden directamente esta indicación; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Retinopatía diabética no proliferativa grave (severe nonproliferative diabetic retinopathy) |
| Puntaje de Predicción TxGNN | 0.9963 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 18) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, denosumab inhibe RANKL (ligando del receptor activador del factor nuclear κB), y su eficacia en osteoporosis está comprobada. Mecanísticamente, la vía RANKL/RANK se ha vinculado en la literatura con inflamación, calcificación vascular y disfunción metabólica, procesos que podrían cruzarse con la patología microvascular diabética.

La relación entre la indicación original y la nueva es indirecta: la osteoporosis es un trastorno óseo, mientras que la retinopatía diabética es una complicación microvascular de la diabetes. Un posible puente sería que la inhibición de RANKL mejore el estado glucémico o metabólico y, con ello, reduzca complicaciones microvasculares. Esto es una inferencia especulativa y no está demostrada con la evidencia disponible.

El puntaje del modelo es muy alto (0,9963), pero por sí solo no sustituye a la evidencia clínica. No se pudo anclar el razonamiento a un mecanismo documentado.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Para la indicación principal (retinopatía diabética no proliferativa grave) no hay literatura disponible. Para la indicación predicha relacionada, **retinopatía diabética** (puntaje 0,9923), se recuperaron dos publicaciones de relevancia solo indirecta; ninguna evalúa denosumab en retinopatía. Las clasificaciones son tentativas, basadas en títulos y resúmenes, y requieren revisión del texto completo.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38899553](https://pubmed.ncbi.nlm.nih.gov/38899553/) | 2024 | Cohorte con revisión sistemática y metaanálisis | Diabetes, Obesity & Metabolism | Análisis de datos reales: denosumab frente a bisfosfonatos en osteoporosis se asoció con menor incidencia de diabetes tipo 2, menos úlceras del pie y menor mortalidad global. Evalúa complicaciones microvasculares (incluida retinopatía) como desenlace, pero es evidencia indirecta. |
| [36960265](https://pubmed.ncbi.nlm.nih.gov/36960265/) | 2023 | Observacional | Cureus | Evaluación del uso de la herramienta FRAX para riesgo de fractura en adultos con diabetes tipo 2; no guarda relación con desenlaces de retinopatía. |

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones vigentes (todas de medicamentos de un solo principio activo). El texto de la indicación aprobada no figura en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1241890001 | OBODENCE 60 mg | Solución inyectable en jeringa precargada | No disponible |
| 11703001IP | XGEVA 120 mg | Solución inyectable | No disponible |
| 1241904001 | OSENVELT 120 mg | Solución inyectable | No disponible |
| 1251997001 | OSQAY 60 mg | Solución inyectable en jeringa precargada | No disponible |
| 1251953004 | BOMYNTRA 120 mg | Solución inyectable | No disponible |

Las 15 autorizaciones restantes corresponden a otros biosimilares y presentaciones de 60 mg y 120 mg.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; las principales son de nivel **moderado** e incluyen:
  - Corticosteroides: hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida, prednisolona, prednisona, metilprednisolona.
  - Inmunosupresores y otros: tacrolimus, mercaptopurina, levamisol, trimetrexato, dupilumab.
  - Radiofármacos y anticuerpos: ibritumomab tiuxetán, iobenguano (I-131), tositumomab (con y sin I-131).
  - Hormonas: corticotropina, tetracosáctido.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto, pero carece de ensayos clínicos y de literatura directa (nivel L5 para la forma grave y L4 solo indirecto para retinopatía diabética en general). Además, no se han revisado advertencias ni contraindicaciones del prospecto, por lo que no es posible avanzar a una evaluación de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones).
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión sistemática de la literatura específica sobre RANKL/RANK y retinopatía diabética.
- Revisar el texto completo de PMID 38899553 para extraer los resultados de retinopatía.
- Evaluar la plausibilidad biológica en modelos preclínicos antes de plantear ensayos clínicos.
- Valorar la relevancia de las interacciones con corticosteroides en pacientes diabéticos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

