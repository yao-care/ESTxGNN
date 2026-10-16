---
layout: default
title: Parecoxib
parent: Evidencia moderada (L3-L4)
nav_order: 611
evidence_level: L3
indication_count: 4
last_modified_at: 2026-10-14
description: "Parecoxib: nueva indicación predicha, Trastorno de migraña (nivel de evidencia L3). Indicación original: No disponible en los datos compilados (los textos de indicación de la…"
---

# Parecoxib
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **4** 
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

# Parecoxib: De Indicación Original No Especificada a Trastorno de Migraña

## Resumen en Una Frase

Parecoxib es un inhibidor selectivo de la COX-2 (profármaco del valdecoxib) comercializado en España en forma inyectable; los datos compilados no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **trastorno de migraña**,
con **0 ensayos clínicos** registrados y **1 publicación clínica** (un estudio piloto comparativo) que respaldan por ahora esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Trastorno de migraña |
| Puntaje de Predicción TxGNN | 99,55% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados no incluyen una descripción detallada del mecanismo de acción registrada para este fármaco. Según la información conocida, parecoxib es un profármaco del valdecoxib, un inhibidor selectivo de la COX-2. La COX-2 impulsa la síntesis de prostaglandinas (PGE2), que contribuyen a la inflamación neurógena, la sensibilización trigeminovascular y la liberación de CGRP durante las crisis de migraña.

Por ello, inhibir la COX-2 es un mecanismo plausible para el alivio agudo de la migraña. Los estudios preclínicos en ganglios trigeminales de rata y en modelos de activación trigeminovascular (PMID 21394197 y 16492237) son coherentes con este razonamiento.

Conviene ser prudente: la similitud con la indicación original no pudo evaluarse porque no hay texto de indicación disponible. El único estudio clínico identificado compara parecoxib con sumatriptán y rizatriptán, pero su diseño y la solidez de sus resultados no se han confirmado. Por eso el nivel de evidencia se fija de forma conservadora en L3.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21996647](https://pubmed.ncbi.nlm.nih.gov/21996647/) | 2011 | Estudio piloto clínico comparativo (diseño no confirmado) | Clinical Neuropharmacology | Compara 40 mg de parecoxib intravenoso con rizatriptán oral (10 mg) y sumatriptán subcutáneo en crisis agudas de migraña |

Para subtipos relacionados se identificó además evidencia preclínica (rata): [21394197](https://pubmed.ncbi.nlm.nih.gov/21394197/) (2011, PLoS One; la IL-1β estimula la síntesis de PGE2 dependiente de COX-2 y la liberación de CGRP en ganglios trigeminales) y [16492237](https://pubmed.ncbi.nlm.nih.gov/16492237/) (2006, Headache; efectos de parecoxib sobre la extravasación de proteínas plasmáticas y la expresión de c-fos).

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 02209005 | DYNASTAT 40 mg polvo para solución inyectable | Polvo para solución inyectable | No disponible |
| 02209008 | DYNASTAT 40 mg polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable | No disponible |

Ambas autorizaciones pertenecen a Pfizer Europe MA EEIG y están vigentes.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como aspecto de cautela general, los inhibidores selectivos de la COX-2 pueden plantear preocupaciones cardiovasculares, especialmente relevantes si se consideran poblaciones con enfermedad vascular.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción del modelo es muy alta (99,55%) y existe un mecanismo plausible (COX-2/PGE2/CGRP), pero la evidencia clínica se limita a un estudio piloto de diseño no confirmado y no hay ensayos registrados. Tampoco se dispone de datos de seguridad de la ficha técnica, lo que impide avanzar.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto/ficha técnica de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas)
- Confirmar el diseño y los resultados del estudio PMID 21996647 (¿ECA o abierto?) y buscar ensayos controlados adicionales
- Completar los datos del mecanismo de acción en DrugBank
- Evaluar la compatibilidad de la vía de administración (parecoxib es solo inyectable; la migraña aguda suele requerir opciones de uso rápido)
- Consolidar los subtipos de migraña (con aura de tronco encefálico, susceptibilidad genética) dentro de la evaluación de trastorno de migraña, ya que carecen de evidencia propia
- Descartar la hipertensión pulmonar como línea prioritaria: la única evidencia es un estudio animal con resultado neutro y existe una preocupación de seguridad cardiovascular
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

