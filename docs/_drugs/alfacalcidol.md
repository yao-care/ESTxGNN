---
layout: default
title: Alfacalcidol
parent: Evidencia moderada (L3-L4)
nav_order: 32
evidence_level: L4
indication_count: 5
last_modified_at: 2026-10-14
description: "Alfacalcidol: nueva indicación predicha, Hipoparatiroidismo aislado familiar por alteración de la secreción de… (nivel de evidencia L4). Indicación original: Hiperparatiroidismo, osteítis fibrosa…"
monitor_inn: "ALFACALCIDOL"
predicted_indications: ["familial isolated hypoparathyroidism due to impaired PTH secretion", "Dahlberg-Borer-Newcomer syndrome", "craniofacial conodysplasia", "acromesomelic dysplasia, Campailla Martinelli type", "renal tubular acidosis"]
---

# Alfacalcidol
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **5** 
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

## Alfacalcidol: De Hiperparatiroidismo a Hipoparatiroidismo Aislado Familiar por Alteración de la Secreción de PTH
{: .text-alpha }

## Resumen en Una Frase

Alfacalcidol es un análogo de la vitamina D (vitamina D 1-alfa-hidroxilada), utilizado originalmente en el hiperparatiroidismo, la osteítis fibrosa, el hipoparatiroidismo y la osteodistrofia renal.
El modelo TxGNN predice que podría ser efectivo para **hipoparatiroidismo aislado familiar por alteración de la secreción de PTH**,
pero actualmente **no hay ensayos clínicos ni publicaciones** específicas que respalden esta predicción; se trata de una extrapolación a partir de una indicación ya existente.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hiperparatiroidismo, osteítis fibrosa, hipoparatiroidismo y osteodistrofia renal (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Hipoparatiroidismo aislado familiar por alteración de la secreción de PTH |
| Puntaje de Predicción TxGNN | 99.61% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado. Según la información conocida, alfacalcidol es un derivado de la vitamina D ya hidroxilado en posición 1-alfa; solo requiere la 25-hidroxilación hepática para convertirse en la forma activa (calcitriol). Por ello evita el paso de la 1-alfa-hidroxilasa renal, que depende de la PTH.

El hipoparatiroidismo aislado familiar es un subtipo genético de una enfermedad que ya figura entre las indicaciones originales del fármaco. En esta condición la secreción de PTH está alterada, la activación renal de la vitamina D disminuye y la calcemia baja. Un análogo que no depende de la PTH puede elevar el calcio sérico, lo que hace plausible el mecanismo.

El puntaje alto de TxGNN probablemente refleja este solapamiento con la indicación ya existente. Conviene interpretarlo con cautela: no hay estudios específicos en este subtipo, de modo que la evidencia es indirecta y extrapolada de la indicación general.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación específica.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 61022 | ETALPHA 1 microgramo solución inyectable | Solución inyectable | No disponible en los datos compilados |
| 55906 | ETALPHA 2 microgramos/ml gotas orales en solución | Gotas orales en solución | No disponible en los datos compilados |
| 61023 | ETALPHA 2 microgramos solución inyectable | Solución inyectable | No disponible en los datos compilados |

Las tres autorizaciones están vigentes y corresponden a monofármacos del titular Cheplapharm Arzneimittel GmbH.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se identificaron interacciones farmacológicas en los datos compilados para este informe.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo y en su cercanía con una indicación ya existente (hipoparatiroidismo), sin ensayos ni publicaciones específicas del subtipo familiar. El nivel de evidencia es bajo (L4) y faltan los datos de seguridad de la ficha técnica.

**Para avanzar se necesita:**
- Obtener y revisar las advertencias y contraindicaciones del prospecto de la AEMPS, así como los textos de indicación aprobados.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una búsqueda bibliográfica dirigida a hipoparatiroidismo familiar aislado y al uso de análogos de vitamina D.
- Valorar series de casos o registros que documenten la respuesta de la calcemia en este subtipo genético.

---

### Nota sobre otras predicciones evaluadas

Los datos compilados incluyen otras cuatro predicciones de menor prioridad. Ninguna cuenta con ensayos clínicos:

- **Síndrome de Dahlberg-Borer-Newcomer** (99.60%, L5, Hold): no se estableció un vínculo mecanístico claro. La literatura recuperada es mayormente general o ajena al tema, y el único artículo directamente relacionado trata de empagliflozina, no de alfacalcidol.
- **Conodisplasia craneofacial** (99.55%, L5, Hold): sin fundamento mecanístico, solo predicción del modelo.
- **Displasia acromesomélica tipo Campailla-Martinelli** (99.53%, L5, Hold): sin fundamento mecanístico, solo predicción del modelo.
- **Acidosis tubular renal** (99.27%, L4, pregunta de investigación): cinco casos clínicos describen mejoría de la osteomalacia con vitamina D activa, incluido alfacalcidol, pero apuntan a la complicación ósea y no a la acidosis, y están confundidos por tratamientos concurrentes con álcalis.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

