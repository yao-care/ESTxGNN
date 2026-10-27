---
layout: default
title: Chlorambucil
parent: Evidencia moderada (L3-L4)
nav_order: 169
evidence_level: L4
indication_count: 8
last_modified_at: 2026-10-14
description: "Chlorambucil: nueva indicación predicha, Leucemia linfocítica crónica/linfoma linfocítico pequeño de centro pr… (nivel de evidencia L4). Indicación original: Linfoma de Hodgkin, linfoma folicular, le…"
monitor_inn: "chlorambucil"
predicted_indications: ["pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma", "chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation", "ALK-positive large B-cell lymphoma", "primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "pulmonary blastoma", "small cell lung carcinoma"]
---

# Chlorambucil
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **8** 
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

## Clorambucilo: De Linfoma de Hodgkin a Leucemia Linfocítica Crónica/Linfoma Linfocítico Pequeño de Centro Pregerminal
{: .text-alpha }

## Resumen en Una Frase

Clorambucilo es un agente alquilante, originalmente utilizado en el tratamiento del linfoma de Hodgkin, el linfoma folicular, la leucemia linfoblástica aguda y otras neoplasias de células B maduras.
El modelo TxGNN predice que podría ser efectivo para **leucemia linfocítica crónica/linfoma linfocítico pequeño de centro pregerminal**, pero actualmente no hay ensayos clínicos registrados y solo **1 publicación** (una revisión general) respalda esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Linfoma de Hodgkin, linfoma folicular, leucemia linfoblástica aguda, neoplasias de células B maduras (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas están vacíos) |
| Nueva Indicación Predicha | Leucemia linfocítica crónica/linfoma linfocítico pequeño de centro pregerminal |
| Puntaje de Predicción TxGNN | 99.72% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, clorambucilo es un agente alquilante de la clase de las mostazas nitrogenadas, que daña el ADN de las células tumorales e impide su proliferación. Su eficacia en neoplasias linfoides de células B está establecida.

La leucemia linfocítica crónica (LLC) es una neoplasia de células B maduras muy cercana a las indicaciones originales del fármaco. El subtipo predicho, de centro pregerminal (con genes de inmunoglobulina no mutados), es una subclasificación molecular de la LLC/LLP. Por ello, la eficacia podría heredarse de la indicación principal, y el alto puntaje del modelo refleja esa proximidad en la red de conocimiento.

Conviene matizar que esto no es un reposicionamiento en sentido estricto, sino más bien un subtipo de una indicación ya existente. La única publicación recuperada es una revisión de 2003 que aboga por un tratamiento adaptado al riesgo en la LLC, y no constituye evidencia directa para este subtipo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [12577769](https://pubmed.ncbi.nlm.nih.gov/12577769/) | 2003 | Revisión | Nederlands tijdschrift voor geneeskunde | La LLC de células B es la leucemia más frecuente en Occidente y no es tan indolente como se supone; existen dos subtipos (centro pregerminal con genes no mutados y otro mutado), lo que justifica un enfoque adaptado al riesgo |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 33209 | LEUKERAN 2 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | No disponible en los datos compilados |
| 85506 | CLORAMBUCILO ASPEN 2 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | No disponible en los datos compilados |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (agente alquilante, mostaza nitrogenada) |
| Riesgo de Mielosupresión | Alto (el grafo de conocimiento registra contraindicación en neutropenia, trombocitopenia, leucopenia, anemia y linfopenia) |
| Clasificación de Emetogenicidad | Baja a moderada (según la categoría del fármaco) |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no proceden del texto del prospecto): epilepsia, trombocitopenia, síndrome nefrótico (incluidas las formas familiar y de lesiones mínimas), neutropenia, agranulocitosis, anemia (incluida la macrocítica), enfermedad pulmonar intersticial, fibrosis pulmonar, lesión hepática inducida por fármacos, leucopenia, linfopenia y leucemia aguda (incluidas las formas bifenotípica y de linaje ambiguo).
- **Interacciones farmacológicas**: se identificaron 167 interacciones en total. Entre las principales:
  - Gravedad **mayor**: deferiprona y lexidronam de samario (153Sm).
  - Gravedad **moderada**: anfotericina B (y sus formulaciones lipídicas), palifermina, cloruro de estroncio Sr-89, mercaptopurina, roflumilast y cloranfenicol.
  - Gravedad **menor**: levofloxacino.
- **Señal de seguridad adicional**: los estudios recuperados sobre neoplasias secundarias tras el tratamiento del linfoma de Hodgkin sugieren un riesgo relevante de segundas neoplasias con la exposición a alquilantes.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje del modelo es muy alto, pero no existen ensayos clínicos para este subtipo y la única publicación es una revisión general. La plausibilidad deriva de la indicación principal (LLC), no de datos específicos del subtipo.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), actualmente ausente
- Datos detallados del mecanismo de acción (MOA)
- Confirmar si el subtipo ya queda cubierto por la indicación de LLC de las autorizaciones españolas
- Evidencia clínica específica del subtipo (por ejemplo, datos de ensayos con clorambucilo en LLC según estado mutacional de IGHV)
- Plan de monitoreo hematológico y de segundas neoplasias
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

