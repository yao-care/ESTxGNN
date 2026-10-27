---
layout: default
title: Insulin Lispro
parent: Solo predicción del modelo (L5)
nav_order: 422
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Insulin Lispro: nueva indicación predicha, Ooforitis autoinmune (nivel de evidencia L5). Indicación original: Diabetes mellitus tipo 2 (según el grafo de conocimiento"
monitor_inn: "Insulin lispro"
predicted_indications: ["autoimmune oophoritis", "thiamine-responsive dysfunction syndrome", "classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "pancreatic agenesis", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy"]
---

# Insulin Lispro
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Insulina lispro: De Diabetes Mellitus Tipo 2 a Ooforitis Autoinmune
{: .text-alpha }

## Resumen en Una Frase

Insulina lispro es un análogo de insulina de acción rápida, utilizado originalmente para el tratamiento de la diabetes mellitus (tipo 1 y tipo 2) y la cetoacidosis diabética.
El modelo TxGNN predice que podría ser efectivo para **ooforitis autoinmune**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.
Se trata de una predicción puramente computacional, con un nivel de evidencia L5.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Diabetes mellitus tipo 2 (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Ooforitis autoinmune |
| Puntaje de Predicción TxGNN | 99.78% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 9 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la insulina lispro es un análogo de insulina humana cuya eficacia en el control glucémico de la diabetes está comprobada. Reduce la glucosa sanguínea al sustituir la acción de la insulina endógena.

Un posible vínculo es la biología autoinmune compartida con la diabetes tipo 1 (por ejemplo, la autoinmunidad poliglandular). Sin embargo, la insulina lispro es un agente hipoglucemiante sin acción inmunomoduladora conocida sobre la autoinmunidad ovárica. La predicción probablemente se deba a la proximidad entre enfermedades en el grafo de conocimiento y no a un mecanismo terapéutico real.

Por tanto, la plausibilidad mecanística es baja y la predicción debe considerarse generadora de hipótesis, no una base para el uso clínico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para ooforitis autoinmune.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 96007004 | HUMALOG 100 U/ml, solución inyectable en cartucho | Solución inyectable en cartucho | No disponible |
| 96007031 | HUMALOG KWIKPEN 100 U/ml, solución inyectable | Solución inyectable en pluma precargada | No disponible |
| 1201422014 | LYUMJEV 200 unidades/ml KWIKPEN | Solución inyectable | No disponible |
| 1201422011 | LYUMJEV 100 unidades/ml JUNIOR KWIKPEN | Solución inyectable | No disponible |
| 196007044 | HUMALOG JUNIOR KWIKPEN 100 unidades/ml | Solución inyectable en pluma precargada | No disponible |

Se muestran 5 de las 9 autorizaciones vigentes, todas del titular Eli Lilly Nederland B.V.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones registradas; entre las principales (nivel moderado) figuran:
  - Agonistas adrenérgicos y simpaticomiméticos: fenilefrina, epinefrina, pseudoefedrina, salbutamol, formoterol.
  - Betabloqueantes: acebutolol.
  - Otros antidiabéticos: metformina, alogliptina, albiglutida.
  - Corticoides: hidrocortisona (y de forma menor, hidrocortisona tópica y alclometasona tópica).
  - Hormonas: estradiol, etinilestradiol, levonorgestrel.
  - Otros: acetazolamida, hidroclorotiazida, doxiciclina, alpelisib, etanol.

Consultar el prospecto para el resto de la información de seguridad (advertencias y contraindicaciones).

## Otras Indicaciones Predichas (Referencia)

| # | Indicación Predicha | Puntaje TxGNN | Evidencia | Comentario |
|---|------|------|------|------|
| 2 | Síndrome de disfunción sensible a tiamina | 99.37% | L5 | La insulina solo trata el componente diabético; el tratamiento principal es la tiamina |
| 3 | Síndrome de la persona rígida clásico | 99.36% | L5 | Asociación por autoinmunidad anti-GAD y diabetes concurrente |
| 4 | Síndrome de miembro rígido focal | 99.36% | L5 | Misma señal que la forma clásica |
| 5 | Opsismodisplasia | 99.34% | L5 | Vínculo especulativo vía INPPL1/SHIP2 en la señalización de insulina |
| 6 | Lipodistrofia localizada inducida por fármacos | 99.09% | L5 | Es un efecto adverso conocido de la insulina, no una indicación terapéutica |
| 7 | Agenesia pancreática | 99.09% | L4 | Reemplazo de insulina racional, pero es una extensión de la indicación existente; solo 1 revisión indirecta (PMID 12150359) |
| 8 | Lipodistrofia centrífuga | 99.04% | L5 | Sin evidencia; la insulina puede causar lipoatrofia |
| 9 | Lipoatrofia localizada inducida por presión | 99.03% | L5 | Sin evidencia; la insulina se asocia a lipoatrofia |

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para ooforitis autoinmune se basa únicamente en el grafo de conocimiento (L5), sin ensayos ni literatura, y la insulina lispro carece de acción inmunomoduladora que explique un beneficio. Ninguna de las otras indicaciones predichas presenta evidencia que justifique avanzar; varias reflejan comorbilidad diabética o efectos adversos de la insulina.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) de la insulina lispro.
- Advertencias y contraindicaciones del prospecto de la AEMPS.
- Textos de indicación aprobada de las autorizaciones españolas.
- Revisión sistemática de la literatura sobre autoinmunidad ovárica y diabetes tipo 1, y evidencia clínica o preclínica que respalde un efecto terapéutico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

