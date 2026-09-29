---
layout: default
title: Vincristine
parent: Solo predicción del modelo (L5)
nav_order: 560
evidence_level: L5
indication_count: 3
---

# Vincristine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Vincristina: De Agente Antineoplásico Hematológico y Pediátrico a Ganglioneuroblastoma

## Resumen en Una Frase

La vincristina es un alcaloide de la vinca utilizado como antineoplásico en leucemias, linfomas y tumores sólidos pediátricos como el neuroblastoma y el tumor de Wilms. El modelo TxGNN predice que podría ser efectiva para **ganglioneuroblastoma**, con **4 ensayos clínicos** y **6 publicaciones** relacionados. Sin embargo, la evidencia es indirecta: los ensayos evalúan fármacos añadidos a un esquema de quimioterapia y las publicaciones son sobre todo casos clínicos.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Agente antineoplásico (leucemia, linfomas, rabdomiosarcoma, neuroblastoma, tumor de Wilms), según datos farmacológicos. El texto de indicación de la AEMPS no está disponible en las autorizaciones |
| Nueva Indicación Predicha | Ganglioneuroblastoma |
| Puntaje de Predicción TxGNN | 99,31% |
| Nivel de Evidencia | L2 (indirecta) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

La vincristina se une a la tubulina beta (TUBB, clase I) e impide el ensamblaje de los microtúbulos. Esto provoca una parada mitótica en las células que se dividen rápidamente. No disponemos de datos detallados de mecanismo de acción en DrugBank. La descripción anterior procede de la base farmacológica y del análisis de la predicción.

El ganglioneuroblastoma pertenece al espectro de los tumores neuroblásticos. En este grupo, la vincristina es un componente habitual de los esquemas de inducción con varios fármacos. Los casos clínicos recogidos la mencionan dentro de combinaciones como cisplatino, doxorrubicina, ciclofosfamida y vincristina. Por eso el puntaje alto del modelo (0,993) es coherente con la biología conocida.

**Salvedad importante:** los ensayos identificados evalúan agentes añadidos (dinutuximab, 131I-MIBG, inhibidores de ALK, busulfán/melfalán) sobre una base de quimioterapia. Los datos no confirman que la vincristina esté en cada esquema base. Su aportación individual no se puede separar del conjunto del régimen.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03786783](https://clinicaltrials.gov/study/NCT03786783) | Fase 2 | Completado | 42 | Dinutuximab y sargramostim combinados con quimioterapia de inducción en neuroblastoma de alto riesgo recién diagnosticado. Evidencia indirecta de viabilidad de la combinación. Relevancia B |
| [NCT03126916](https://clinicaltrials.gov/study/NCT03126916) | Fase 3 | Reclutando | 750 | 131I-MIBG o inhibidor de ALK (lorlatinib) añadidos al tratamiento intensivo en neuroblastoma o ganglioneuroblastoma de alto riesgo. La variable aleatorizada no es la vincristina. Sin resultados. Relevancia B |
| [NCT06172296](https://clinicaltrials.gov/study/NCT06172296) | Fase 3 | Reclutando | 478 | Dinutuximab añadido a la terapia multimodal intensiva en neuroblastoma de alto riesgo. La vincristina probablemente forma parte de la base de quimioterapia. Sin resultados. Relevancia B |
| [NCT01798004](https://clinicaltrials.gov/study/NCT01798004) | Fase 1 | Completado | 150 | Consolidación mieloablativa con busulfán/melfalán tras inducción. La vincristina sería, como mucho, parte de la inducción previa. Relevancia baja (C) |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31342649](https://pubmed.ncbi.nlm.nih.gov/31342649/) | 2019 | Ensayo clínico prospectivo | Pediatric Blood & Cancer | Estudio JN-L-10: uso de factores de riesgo definidos por imagen para decidir la cirugía en neuroblastoma de bajo riesgo. Se centra en la estrategia quirúrgica, no en la vincristina |
| [15701990](https://pubmed.ncbi.nlm.nih.gov/15701990/) | 2005 | Caso clínico | J Pediatr Hematol Oncol | Ganglioneuroblastoma con ictericia obstructiva como presentación inicial. Se trató con quimioterapia con cisplatino, pirarrubicina/doxorrubicina, ciclofosfamida y vincristina |
| [8255850](https://pubmed.ncbi.nlm.nih.gov/8255850/) | 1993 | Caso clínico | Postgrad Med J | Ganglioneuroblastoma espinal irresecable. Remisión completa histológica solo con quimioterapia combinada (doxorrubicina, vincristina, ciclofosfamida, etopósido, ifosfamida, cisplatino) |
| [7421294](https://pubmed.ncbi.nlm.nih.gov/7421294/) | 1980 | Serie de casos | J Thorac Cardiovasc Surg | 31 pacientes con ganglioneuroblastoma intratorácico tratados con resección, radioterapia o quimioterapia. Supervivencia de 27/31 |
| [3071124](https://pubmed.ncbi.nlm.nih.gov/3071124/) | 1988 | Caso clínico | Hinyokika Kiyo | Ganglioneuroblastoma suprarrenal en adulto con metástasis ganglionar regional, tratado de forma multimodal |
| [8888754](https://pubmed.ncbi.nlm.nih.gov/8888754/) | 1996 | Caso clínico | J Pediatr Hematol Oncol | Ganglioneuroblastoma multifocal en estadio 4 con afectación gástrica en una lactante |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 71117 | VINCRISTINA TEVA 1 mg/ml SOLUCIÓN INYECTABLE EFG | Solución inyectable | Teva Pharma S.L.U. |
| 62378 | VINCRISTINA PFIZER 1 mg/ml SOLUCIÓN INYECTABLE EFG | Solución inyectable | Pfizer S.L. |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (alcaloide de la vinca, antimicrotúbulo que actúa sobre la tubulina beta) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma, función hepática y renal. Confirmar los parámetros exactos en el prospecto |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La vincristina tiene una base biológica sólida y un uso conocido dentro de los esquemas multiagente para tumores neuroblásticos, y el puntaje de TxGNN es alto. Aun así, la evidencia es indirecta: ningún ensayo prueba la vincristina de forma aislada, los dos ensayos de Fase 3 siguen reclutando y la literatura es principalmente de casos clínicos.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS, que aporta las advertencias, contraindicaciones y la indicación aprobada, hoy no disponibles. Sin ellos no se puede completar el cribado de seguridad.
- Confirmar en los protocolos de los ensayos si la vincristina forma parte del esquema base de cada uno.
- Obtener los datos de mecanismo de acción de DrugBank.
- Esperar los resultados de los ensayos de Fase 3 (NCT03126916 y NCT06172296).
- Revisar los datos de mielosupresión, emetogenicidad y monitoreo en el prospecto.

Las otras dos predicciones del modelo, "anomalías vertebrales y disfunción endocrina y de células T variable" y "neoplasia retroperitoneal", tienen evidencia menor. La primera es solo predicción del modelo y la segunda solo una pregunta de investigación por histología.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

