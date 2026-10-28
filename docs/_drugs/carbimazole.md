---
layout: default
title: Carbimazole
parent: Solo predicción del modelo (L5)
nav_order: 146
evidence_level: L5
indication_count: 2
monitor_inn: "Carbimazole"
predicted_indications: ["resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "hyperthyroxinemia"]
last_modified_at: 2026-10-27
description: "Carbimazole: nueva indicación predicha, Resistencia a la hormona tiroidea por mutación en el receptor beta de la hormona tiroidea (resistance to thyroid hormon… (nivel de evidencia L5). Indicación or…"
---

# Carbimazole
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

## Carbimazol: antitiroideo (profármaco del metimazol) → resistencia a la hormona tiroidea por mutación en el receptor beta de la hormona tiroidea (resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta)
{: .text-alpha }

## Resumen en Una Frase

Carbimazol es un antitiroideo que actúa como profármaco del metimazol y reduce la síntesis de hormonas tiroideas.
El modelo TxGNN predice que podría ser efectivo para **resistencia a la hormona tiroidea por mutación en el receptor beta de la hormona tiroidea (resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta)**,
pero actualmente solo existe **1 publicación** (un caso clínico) y **ningún ensayo clínico** registrado, y esa publicación no estudia directamente esta enfermedad con el fármaco como tratamiento.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Resistencia a la hormona tiroidea por mutación en el receptor beta de la hormona tiroidea (resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta) |
| Puntaje de Predicción TxGNN | 0,9971 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 1 de 1) |
| Número de Autorizaciones | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Carbimazol es un profármaco del metimazol: inhibe la peroxidasa tiroidea y reduce la síntesis de hormonas tiroideas. En la resistencia a la hormona tiroidea por mutación en THRB, el defecto principal es una menor sensibilidad de los tejidos a la hormona, con elevación compensatoria de T4/T3 y TSH no suprimida.

Reducir la producción hormonal con un antitiroideo podría, en teoría, bajar los niveles de hormona. Sin embargo, es esperable que eleve aún más la TSH, agrave el bocio y provoque hipotiroidismo en tejidos ya relativamente resistentes. En general, los antitiroideos no se recomiendan en esta condición.

Por tanto, el puntaje alto probablemente refleja la proximidad en la red a genes relacionados con la hormona tiroidea, y no una justificación terapéutica real.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [24165508](https://pubmed.ncbi.nlm.nih.gov/24165508/) | 2013 | Revisión / discusión de caso | BMJ Case Reports | Varón con T4 libre elevada y TSH no suprimida, tratado de forma intermitente con carbimazol durante años como hipertiroidismo; se discute el diagnóstico diferencial de esta combinación analítica |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 28996 | NEO-TOMIZOL 5 mg COMPRIMIDOS | Comprimido | No registrada en los datos locales |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de ensayos clínicos y de estudios que evalúen directamente el fármaco en esta enfermedad. Además, el razonamiento mecanístico sugiere que el tratamiento antitiroideo podría ser perjudicial (aumento de TSH, bocio, hipotiroidismo).

**Para avanzar se necesita:**
- Datos de mecanismo de acción y de seguridad del prospecto de la AEMPS
- Estudios clínicos o series de casos que evalúen específicamente el efecto de los antitiroideos en esta condición
- Revisión por especialistas en endocrinología que confirmen o descarten la plausibilidad clínica
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

