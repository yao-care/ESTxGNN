---
layout: default
title: Tiagabine
parent: Evidencia moderada (L3-L4)
nav_order: 792
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-14
description: "Tiagabine: nueva indicación predicha, Epilepsia visual (nivel de evidencia L4). Indicación original: Epilepsia parcial (según el grafo de conocimiento"
---

# Tiagabine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **1** 
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

# Tiagabina: De Epilepsia Parcial a Epilepsia Visual

## Resumen en Una Frase

Tiagabina es un anticonvulsivante inhibidor selectivo de la recaptación de GABA (GAT-1), utilizado originalmente para el tratamiento de la epilepsia parcial.
El modelo TxGNN predice que podría ser efectivo para **Epilepsia Visual**,
pero actualmente no hay ensayos clínicos registrados y la literatura disponible (**16 publicaciones**) es general (revisiones y guías), sin estudios específicos de esta indicación.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Epilepsia parcial (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas están vacíos) |
| Nueva Indicación Predicha | Epilepsia visual |
| Puntaje de Predicción TxGNN | 99,25% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información farmacológica conocida y la literatura revisada, tiagabina inhibe selectivamente el transportador GAT-1 (gen *SLC6A1*), aumentando la concentración extracelular de GABA y reforzando la inhibición neuronal. Este mecanismo es único entre los fármacos antiepilépticos (PMID 10530690, 15094857).

La epilepsia visual es un trastorno focal, de origen típicamente occipital, muy próximo a la epilepsia parcial, indicación original del fármaco. El puntaje alto de TxGNN (0,99) probablemente refleja esta cercanía entre ambas enfermedades en el grafo de conocimiento, más que una señal terapéutica independiente.

Mecanísticamente, reforzar la inhibición GABAérgica podría ser aplicable a crisis focales de origen occipital, pero no se dispone de datos específicos en epilepsia visual. Además, la literatura señala precauciones: tiagabina se ha descrito en casos de estatus epiléptico inducido por fármacos (PMID 26210064) y existe una revisión sobre efectos en los campos visuales de fármacos GABAérgicos (PMID 12588906), relevante para una población con manifestaciones visuales.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Guía clínica | Neurology | Actualización de la guía AAN/AES sobre fármacos antiepilépticos nuevos en epilepsia de nueva aparición |
| [32120063](https://pubmed.ncbi.nlm.nih.gov/32120063/) | 2020 | Revisión | Neuropharmacology | Mecanismos de acción de los fármacos antiepilépticos actuales |
| [10530690](https://pubmed.ncbi.nlm.nih.gov/10530690/) | 1999 | Revisión | Epilepsia | Tiagabina inhibe la recaptación de GABA; eficaz como terapia añadida en crisis parciales; sin efectos relevantes sobre el metabolismo hepático ni los niveles de otros FAE |
| [12588906](https://pubmed.ncbi.nlm.nih.gov/12588906/) | 2003 | Revisión | J Neurol Neurosurg Psychiatry | Efectos de vigabatrina y tiagabina sobre los campos visuales (sin resumen disponible) |
| [26210064](https://pubmed.ncbi.nlm.nih.gov/26210064/) | 2015 | Revisión | Epilepsy & Behavior | Estatus epiléptico inducido por fármacos; los FAE GABAérgicos, incluida tiagabina, pueden exacerbar crisis en epilepsias generalizadas |
| [17560495](https://pubmed.ncbi.nlm.nih.gov/17560495/) | 2007 | Revisión | Pediatric Neurology | Antiepilépticos y función visual: alteraciones del campo visual y de la visión del color |
| [9097364](https://pubmed.ncbi.nlm.nih.gov/9097364/) | 1997 | Revisión | Seminars in Pediatric Neurology | Eficacia en crisis parciales en adultos y adolescentes; datos pediátricos preliminares alentadores |
| [8039477](https://pubmed.ncbi.nlm.nih.gov/8039477/) | 1994 | Revisión | Epilepsia | Efecto anticonvulsivante en modelos animales y en un ensayo controlado con placebo en crisis parciales complejas |
| [15094857](https://pubmed.ncbi.nlm.nih.gov/15094857/) | 1998 | Revisión | Drugs of Today | Mecanismo específico; sin evidencia de teratogenicidad, carcinogenicidad ni mutagenicidad en animales |
| [10030435](https://pubmed.ncbi.nlm.nih.gov/10030435/) | 1998 | Revisión | J Intellect Disabil Res | Opción terapéutica en epilepsia parcial con discapacidad intelectual; los inductores enzimáticos aumentan su aclaramiento un 50-65% |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 61606 | GABITRIL 5 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos |
| 61607 | GABITRIL 10 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos |
| 61608 | GABITRIL 15 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): trastorno de ansiedad, trastorno neurótico, trastorno distímico, enfermedad hepática y enfermedad de la vesícula biliar.
- **Interacciones farmacológicas**: la consulta no identificó interacciones con otros fármacos; solo consta la interacción farmacológica con su diana, el transportador GAT-1 (SLC6A1), que corresponde a su mecanismo de acción.
- **Alertas de la literatura**: posible exacerbación de crisis o estatus epiléptico en epilepsias generalizadas (PMID 26210064) y posibles efectos sobre el campo visual con fármacos GABAérgicos (PMID 12588906).

Para el resto de la información de seguridad, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo y en literatura general (nivel L4), sin ensayos clínicos ni estudios específicos en epilepsia visual. El puntaje alto probablemente refleja la proximidad con la epilepsia parcial, y existen alertas de seguridad relevantes para esta población.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), ya que su ausencia impide el cribado de seguridad.
- Completar los datos de mecanismo de acción desde DrugBank.
- Buscar estudios clínicos o series de casos específicos de tiagabina en epilepsia visual u occipital.
- Evaluar el riesgo sobre el campo visual y de exacerbación de crisis en esta población.
- Aclarar la relevancia de las contraindicaciones del grafo de conocimiento (ansiedad, hepatopatía, enfermedad biliar).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

