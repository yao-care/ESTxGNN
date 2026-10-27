---
layout: default
title: Vincristine
parent: Evidencia moderada (L3-L4)
nav_order: 850
evidence_level: L3
indication_count: 3
last_modified_at: 2026-10-14
description: "Vincristine: nueva indicación predicha, Ganglioneuroblastoma (nivel de evidencia L3). Indicación original: Leucemia linfoblástica aguda y linfomas (según las indicaciones origi…"
monitor_inn: "Vincristine"
predicted_indications: ["ganglioneuroblastoma (disease)", "vertebral anomalies and variable endocrine and T-cell dysfunction", "retroperitoneal neoplasm"]
---

# Vincristine
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **3** 
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

## Vincristina: De Leucemia Linfoblástica Aguda a Ganglioneuroblastoma
{: .text-alpha }

## Resumen en Una Frase

Vincristina es un alcaloide de la vinca, utilizado originalmente en el tratamiento de la leucemia linfoblástica aguda, linfomas (Hodgkin y no Hodgkin) y otras neoplasias hematológicas.
El modelo TxGNN predice que podría ser efectiva para **ganglioneuroblastoma**,
con **0 ensayos clínicos** y **6 publicaciones** (en su mayoría informes de casos) que actualmente respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Leucemia linfoblástica aguda y linfomas (según las indicaciones originales del grafo de conocimiento; los textos de indicación de las autorizaciones españolas están vacíos) |
| Nueva Indicación Predicha | Ganglioneuroblastoma |
| Puntaje de Predicción TxGNN | 99.31% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Espana | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según la información conocida, la vincristina es un alcaloide de la vinca que se une a la tubulina (diana registrada: tubulina beta clase I, TUBB) e impide la polimerización de los microtúbulos, lo que provoca la detención de la mitosis en células de división rápida. Su eficacia en leucemia linfoblástica aguda y linfomas está bien establecida.

El ganglioneuroblastoma pertenece a la familia de los tumores neuroblásticos (neuroblastoma, ganglioneuroblastoma, ganglioneuroma). La vincristina es desde hace tiempo un componente de los regímenes de quimioterapia combinada para estos tumores (junto con ciclofosfamida, doxorrubicina, cisplatino y etopósido). Esto es coherente con el alto puntaje del modelo.

Conviene hacer una salvedad: los subtipos intermedios, ricos en estroma schwanniano, suelen ser menos quimiosensibles y con frecuencia se manejan con cirugía u observación. Además, la evidencia disponible proviene de informes de casos y no hay ensayos clínicos que evalúen la vincristina de forma específica en esta indicación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31342649](https://pubmed.ncbi.nlm.nih.gov/31342649/) | 2019 | Ensayo clínico prospectivo no aleatorizado | Pediatric Blood & Cancer | Estrategia quirúrgica guiada por factores de riesgo definidos por imagen en neuroblastoma de bajo riesgo; no evalúa la vincristina de forma específica |
| [8255850](https://pubmed.ncbi.nlm.nih.gov/8255850/) | 1993 | Reporte de caso | Postgraduate Medical Journal | Ganglioneuroblastoma espinal irresecable con remisión completa histológica tras quimioterapia combinada que incluía vincristina |
| [15701990](https://pubmed.ncbi.nlm.nih.gov/15701990/) | 2005 | Reporte de caso | J Pediatr Hematol Oncol | Ganglioneuroblastoma con ictericia obstructiva, tratado con cisplatino, pirarrubicina/doxorrubicina, ciclofosfamida y vincristina |
| [7421294](https://pubmed.ncbi.nlm.nih.gov/7421294/) | 1980 | Serie de casos | J Thorac Cardiovasc Surg | 31 pacientes con ganglioneuroblastoma intratorácico tratados con resección, radioterapia o quimioterapia; supervivencia de 27/31 |
| [3071124](https://pubmed.ncbi.nlm.nih.gov/3071124/) | 1988 | Reporte de caso | Hinyokika Kiyo | Ganglioneuroblastoma suprarrenal del adulto con tratamiento multimodal |
| [8888754](https://pubmed.ncbi.nlm.nih.gov/8888754/) | 1996 | Reporte de caso | J Pediatr Hematol Oncol | Ganglioneuroblastoma multifocal en estadio 4 con afectación gástrica en una lactante |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 71117 | Vincristina Teva 1 mg/ml solución inyectable EFG | Solución inyectable | No disponible en los datos compilados |
| 62378 | Vincristina Pfizer 1 mg/ml solución inyectable EFG | Solución inyectable | No disponible en los datos compilados |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (alcaloide de la vinca, antimitótico que actúa sobre la tubulina) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto (la leucopenia figura entre las contraindicaciones del grafo de conocimiento) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función hepática (incluida bilirrubina) y estado neurológico |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

- **Contraindicaciones asociadas en el grafo de conocimiento** (no proceden del texto del prospecto): insuficiencia hepática, colestasis (incluida la colestasis intrahepática familiar y recurrente benigna), hiperbilirrubinemia (incluidos el síndrome de Gilbert y las formas hereditarias), leucopenia, neuropatía periférica (incluida la motora), enfermedad de Charcot-Marie-Tooth, enfermedades neuromusculares, neuritis, infecciones (incluidas las fúngicas y la dermatofitosis) y nefropatía aguda por uratos.
- **Interacciones farmacológicas**: solo se registra la interacción farmacológica con su diana, la tubulina beta clase I (TUBB). No se dispone de datos de interacciones con otros fármacos.

Las advertencias y contraindicaciones del prospecto de la AEMPS no estaban disponibles; consultar el prospecto para la información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje del modelo es alto y el mecanismo es biológicamente coherente con el uso establecido de la vincristina en regímenes multiagente para tumores neuroblásticos. Sin embargo, la evidencia (L3) se limita a informes y series de casos sin ensayos clínicos, y falta la información de seguridad del prospecto, que es un dato bloqueante.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), requisito previo para el cribado de seguridad.
- Completar los datos del mecanismo de acción (consulta a la API de DrugBank).
- Revisar sistemáticamente la literatura sobre regímenes con vincristina en neuroblastoma y ganglioneuroblastoma, y definir el subtipo histológico y el contexto de riesgo (los subtipos ricos en estroma suelen manejarse con cirugía u observación).
- Considerar las contraindicaciones asociadas en el grafo (hepáticas, neurológicas y leucopenia) al seleccionar la población.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

