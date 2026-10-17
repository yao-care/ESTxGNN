---
layout: default
title: Emedastine
parent: Evidencia alta (L1-L2)
nav_order: 285
evidence_level: L2
indication_count: 2
last_modified_at: 2026-10-14
description: "Emedastine: nueva indicación predicha, Urticaria alérgica (nivel de evidencia L2). Indicación original: Conjuntivitis atópica (según la base de conocimiento"
---

# Emedastine
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **2** 
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

# Emedastina: De Conjuntivitis Atópica a Urticaria Alérgica

## Resumen en Una Frase

Emedastina es un antihistamínico antagonista selectivo de los receptores H1, utilizado originalmente en forma de colirio para la conjuntivitis alérgica (atópica, papilar y primaveral), y con indicaciones de urticaria y angioedema según la base de conocimiento del modelo.
El modelo TxGNN predice que podría ser efectiva para la **urticaria alérgica**,
con **0 ensayos clínicos registrados** y **4 publicaciones** (de las cuales una es un ensayo aleatorizado directamente relevante) que actualmente respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Conjuntivitis atópica (según la base de conocimiento; el texto de indicación de las autorizaciones españolas no está disponible) |
| Nueva Indicación Predicha | Urticaria alérgica |
| Puntaje de Predicción TxGNN | 99,96% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold (línea de investigación; se requiere completar datos de seguridad antes de avanzar) |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción. Según la información conocida, la emedastina es un antagonista selectivo de los receptores H1 de histamina. Su eficacia en la conjuntivitis alérgica se ha comprobado, y mecanísticamente podría ser aplicable a la urticaria.

En la urticaria, la histamina liberada por los mastocitos es el principal mediador de la roncha y el eritema, por lo que el bloqueo H1 ofrece una justificación mecanística directa y plausible. Además, la urticaria y el angioedema ya figuran entre las indicaciones originales de la base de conocimiento, lo que respalda el puntaje tan alto del modelo (99,96%).

La literatura describe además una formulación oral (difumarato de emedastina) empleada en urticaria y enfermedades alérgicas, con posibles efectos adicionales sobre la remodelación tisular y la inflamación asociada a eosinófilos. Cabe señalar que la formulación comercializada en España es un colirio, por lo que la compatibilidad de vía de administración con la nueva indicación (oral) aún no está evaluada.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [17229605](https://pubmed.ncbi.nlm.nih.gov/17229605/) | 2006 | ECA | Eur J Dermatol | Difumarato de emedastina (2 mg dos veces al día) vs. loratadina (10 mg al día) durante 4 semanas en 192 pacientes con urticaria crónica idiopática. A la semana, la afectación cutánea se redujo a 0-10% en el 57,1% con emedastina frente al 38,2% con loratadina (p = 0,0019), y el 83,3% logró una puntuación total de síntomas de 0-1 frente al 64,5% (p = 0,0134) |
| [19558341](https://pubmed.ncbi.nlm.nih.gov/19558341/) | 2009 | Revisión | Expert Opin Pharmacother | Revisión del difumarato de emedastina como antagonista H1 selectivo con eficacia en rinitis alérgica, conjuntivitis alérgica, urticaria, dermatitis alérgica y prurito; sin efectos cardiovasculares adversos y con actividad anticolinérgica mínima; posible efecto sobre la remodelación tisular |
| [24720119](https://pubmed.ncbi.nlm.nih.gov/24720119/) | 2013 | Revisión | Przegl Lek | Análisis de las discrepancias entre guías de expertos, fichas técnicas y evidencia de eficacia de fármacos en urticaria (evidencia indirecta) |
| [14499249](https://pubmed.ncbi.nlm.nih.gov/14499249/) | 2003 | Preclínico | Clin Immunol | Estudio en ratón sobre hipersensibilidad de contacto con suplatast tosilato y otros antialérgicos; evidencia indirecta, no centrada en la emedastina |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 98095001IP | EMADINE 0,5 mg/ml colirio en solución (Alcon Laboratories Ltd, Reino Unido) | Colirio en solución | No disponible en los datos compilados |
| 98095001 | EMADINE 0,5 mg/ml colirio en solución (Immedica Pharma AB) | Colirio en solución | No disponible en los datos compilados |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en las consultas realizadas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Existe un ECA de fase comparativa frente a loratadina en urticaria crónica idiopática que respalda la eficacia de la forma oral (nivel L2), y el mecanismo H1 es coherente. Sin embargo, no hay ensayos registrados, no se dispone de información de seguridad del prospecto y la presentación comercializada en España (colirio) no corresponde a la vía necesaria para urticaria, por lo que conviene mantenerla como pregunta de investigación.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), un requisito bloqueante para el cribado de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Evaluar la compatibilidad de vía y formulación (colirio frente a formulación oral, no comercializada en España según los datos disponibles)
- Confirmar los hallazgos del ECA de 2006 con evidencia adicional o ensayos más recientes
- Nota sobre otra predicción: la **urticaria por frío** (puntaje 99,82%) tiene nivel de evidencia L5, sin estudios específicos, por lo que se mantiene en Hold.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

