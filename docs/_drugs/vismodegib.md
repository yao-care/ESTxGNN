---
layout: default
title: Vismodegib
parent: Solo predicción del modelo (L5)
nav_order: 564
evidence_level: L5
indication_count: 10
---

# Vismodegib
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

# Vismodegib: De Carcinoma Basocelular Avanzado a Meduloblastoma con Nodularidad Extensa

## Resumen en Una Frase

Vismodegib es un inhibidor oral de la vía Hedgehog (bloquea Smoothened, SMO), comercializado como Erivedge para el carcinoma basocelular avanzado.
El modelo TxGNN predice que podría ser efectivo para **meduloblastoma con nodularidad extensa**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta indicación concreta: es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Carcinoma basocelular localmente avanzado o metastásico (según la literatura; la ficha de AEMPS no incluye texto de indicación) |
| Nueva Indicación Predicha | Meduloblastoma con nodularidad extensa |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Vismodegib inhibe Smoothened (SMO), una proteína clave de la vía Hedgehog. Esta vía está hiperactivada en la mayoría de los carcinomas basocelulares, y por eso el fármaco se usa en esa enfermedad. Actualmente no se dispone de datos detallados del mecanismo de acción en DrugBank para este paquete de evidencia.

El meduloblastoma con nodularidad extensa suele estar impulsado por la vía SHH (Sonic Hedgehog). Por eso, biológicamente, la predicción es plausible: el mismo mecanismo que sustenta el uso en carcinoma basocelular podría aplicarse a este tumor cerebral.

Hay dos limitaciones importantes:
- Los tumores con mutaciones por debajo de SMO en la vía (por ejemplo, *SUFU*) probablemente serían resistentes.
- En pacientes pediátricos habría que revisar la toxicidad sobre el cartílago de crecimiento (fusión epifisaria prematura).

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 113848001 | ERIVEDGE 150 MG CAPSULAS DURAS (Roche Registration GmbH) | Cápsula dura | — |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de SMO / vía Hedgehog) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Espasmos musculares, disgeusia y alopecia (efectos descritos para el uso en carcinoma basocelular); resto según el prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para meduloblastoma con nodularidad extensa solo existe la predicción del modelo (L5), sin ensayos ni literatura. Además, la seguridad en población pediátrica es una preocupación y la resistencia por mutaciones posteriores a SMO es posible.

Como referencia, la indicación de mayor evidencia entre las predichas es "cáncer de piel" (en la práctica, carcinoma basocelular), con nivel L2 y decisión "Proceed with Guardrails". Corresponde al uso ya comercializado del fármaco.

**Para avanzar se necesita:**
- Búsqueda de literatura y ensayos específicos de vismodegib en meduloblastoma SHH.
- Confirmar el subtipo molecular (SHH, ausencia de mutaciones en *SUFU*) que justificaría el uso.
- Evaluar la toxicidad en el crecimiento óseo si se considera población pediátrica.
- Obtener las advertencias y contraindicaciones del prospecto de AEMPS.
- Completar los datos del mecanismo de acción desde DrugBank.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

