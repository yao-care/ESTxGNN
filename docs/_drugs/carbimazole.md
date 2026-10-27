---
layout: default
title: Carbimazole
parent: Solo predicción del modelo (L5)
nav_order: 146
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Carbimazole: nueva indicación predicha, Resistencia a la hormona tiroidea por mutación en el receptor beta de… (nivel de evidencia L5). Indicación original: Hipertiroidismo…"
monitor_inn: "Carbimazole"
predicted_indications: ["resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "neonatal thyrotoxicosis", "hyperthyroxinemia"]
---

# Carbimazole
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Carbimazol: De Hipertiroidismo a Resistencia a la Hormona Tiroidea por Mutación del Receptor Beta
{: .text-alpha }

## Resumen en Una Frase

Carbimazol es un fármaco antitiroideo (profármaco del metimazol), originalmente utilizado para el tratamiento del hipertiroidismo, la enfermedad de Graves y la tiroTOXicosis.
El modelo TxGNN predice que podría ser efectivo para la **resistencia a la hormona tiroidea por mutación del receptor beta (RTH-beta)**, pero **sin ensayos clínicos** y con **una sola publicación** (un caso clínico de diagnóstico diferencial), por lo que la evidencia es únicamente predictiva y, además, el razonamiento mecanístico apunta en contra de su uso.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertiroidismo, enfermedad de Graves y tirotoxicosis (según el grafo de conocimiento; el texto de indicación de la autorización en España no está disponible) |
| Nueva Indicación Predicha | Resistencia a la hormona tiroidea por mutación en el receptor beta de la hormona tiroidea |
| Puntaje de Predicción TxGNN | 99.71% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento farmacológico general, el carbimazol es un profármaco del metimazol que inhibe la tiroperoxidasa y reduce la síntesis de hormonas tiroideas. Su eficacia en el hipertiroidismo está bien establecida.

En la RTH-beta, el defecto primario no es un exceso de producción hormonal, sino una menor sensibilidad tisular a la hormona tiroidea por mutaciones en el gen THRB, con elevación compensatoria de T4/T3 y TSH no suprimida. En teoría, reducir la producción hormonal bajaría los niveles circulantes, pero se esperaría que aumentara aún más la TSH, agravara el bocio y pudiera inducir hipotiroidismo en tejidos ya relativamente resistentes a la hormona.

Por tanto, el puntaje elevado del modelo probablemente refleja la proximidad en la red a genes relacionados con la hormona tiroidea y no un fundamento terapéutico real. En general, los antitiroideos no se recomiendan en la RTH.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [24165508](https://pubmed.ncbi.nlm.nih.gov/24165508/) | 2013 | Caso clínico / discusión diagnóstica | BMJ Case Reports | Varón joven tratado de forma intermitente con carbimazol durante 10 años por T4 libre elevada y TSH no suprimida; el caso se discute como diagnóstico diferencial de esta combinación analítica, no como evidencia de beneficio terapéutico |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 28996 | NEO-TOMIZOL 5 mg COMPRIMIDOS | Comprimido | Texto de indicación no disponible en los datos compilados |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (L5), sin ensayos clínicos y con una única publicación que no demuestra beneficio. Además, el mecanismo sugiere que reducir la síntesis hormonal podría elevar la TSH, empeorar el bocio y provocar hipotiroidismo, por lo que no se recomienda avanzar.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y del prospecto de la AEMPS (advertencias y contraindicaciones), actualmente ausentes.
- Evidencia preclínica o clínica que demuestre un beneficio real en RTH-beta, que hoy no existe.
- Valorar, como líneas más viables, las otras predicciones: la tirotoxicosis neonatal (nivel L3, con series y casos clínicos, aunque es más una extensión de población que un reposicionamiento, y con señales de seguridad como atresia de coanas) y la hipertiroxinemia (L4, no es una entidad tratable coherente).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

