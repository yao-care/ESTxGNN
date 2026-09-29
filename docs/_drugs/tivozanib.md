---
layout: default
title: Tivozanib
parent: Solo predicción del modelo (L5)
nav_order: 531
evidence_level: L5
indication_count: 10
---

# Tivozanib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Tivozanib: De Indicación Original No Registrada a Carcinoma Endocervical

## Resumen en Una Frase

Tivozanib es un inhibidor de tirosina quinasas de los receptores VEGFR-1/2/3 y está comercializado en España como FOTIVDA. El registro recibido no incluye el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **carcinoma endocervical**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en el registro (las autorizaciones no incluyen texto de indicación) |
| Nueva Indicación Predicha | Carcinoma endocervical |
| Puntaje de Predicción TxGNN | 99,81 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción del fármaco en el registro. Según el análisis de la predicción, tivozanib es un inhibidor de VEGFR-1/2/3, es decir, actúa sobre la vía que impulsa la formación de nuevos vasos sanguíneos (angiogénesis) en los tumores.

En cáncer de cuello uterino la angiogénesis tumoral es una diana validada: la terapia anti-VEGF (bevacizumab) se usa en enfermedad avanzada. Por eso inhibir VEGFR es biológicamente plausible en el carcinoma endocervical.

Esta plausibilidad es solo **indirecta**. No hay datos mecanísticos específicos de tivozanib para esta enfermedad, la similitud con la indicación original no ha sido evaluada y el puntaje refleja cercanía en el grafo de conocimiento, no una señal clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1171215001 | FOTIVDA 890 microgramos cápsulas duras | Cápsula dura | No consta en el registro |
| 1171215002 | FOTIVDA 1340 microgramos cápsulas duras | Cápsula dura | No consta en el registro |

Titular de ambas autorizaciones: Recordati Netherlands B.V.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasas de VEGFR) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni publicaciones que apoyen tivozanib en carcinoma endocervical (nivel L5, etapa S0). Además, faltan los datos de seguridad del prospecto. Las otras nueve predicciones del modelo (adenocarcinomas de ligamento uterino y variantes raras de adenocarcinoma cervical) tienen el mismo nivel L5 y la misma recomendación Hold.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), un dato bloqueante para el cribado de seguridad.
- Obtener el mecanismo de acción detallado desde DrugBank.
- Confirmar la indicación aprobada de FOTIVDA en España.
- Buscar ensayos clínicos y literatura, incluidos estudios preclínicos, sobre inhibidores de VEGFR en cáncer de cuello uterino.
- Evaluar la compatibilidad de la vía de administración (actualmente solo hay cápsula oral) y la similitud con la indicación original.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

