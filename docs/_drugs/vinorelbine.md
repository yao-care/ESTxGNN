---
layout: default
title: Vinorelbine
parent: Solo predicción del modelo (L5)
nav_order: 562
evidence_level: L5
indication_count: 10
---

# Vinorelbine
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

# Vinorelbina: De Cáncer de Pulmón No Microcítico a Sarcoma de Ewing

## Resumen en Una Frase

Vinorelbina es un alcaloide de la vinca (antimitótico citotóxico) cuyo uso establecido, según la literatura recuperada, es el cáncer de pulmón no microcítico y el cáncer de mama.
El modelo TxGNN predice que podría ser efectivo para **Sarcoma de Ewing**, con **4 ensayos clínicos** relacionados (ninguno confirmado como específico de Ewing) y **ninguna publicación** que respalde esta dirección por ahora.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en las fichas de AEMPS recuperadas; según la literatura, cáncer de pulmón no microcítico y cáncer de mama |
| Nueva Indicación Predicha | Sarcoma de Ewing |
| Puntaje de Predicción TxGNN | 99.999% |
| Nivel de Evidencia | L2 (provisional: el ensayo de Fase 2 completado no está confirmado como específico de Ewing) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 16 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente de datos. Según la farmacología general, vinorelbina es un alcaloide de la vinca que inhibe el ensamblaje de los microtúbulos y provoca detención mitótica. Su eficacia en cáncer de pulmón no microcítico y de mama está comprobada, y mecanísticamente podría ser aplicable al sarcoma de Ewing.

El sarcoma de Ewing es un tumor de proliferación rápida, y un fármaco que bloquea la división celular es un mecanismo citotóxico plausible. Además, uno de los ensayos identificados combina vinorelbina con ciclofosfamida en tumores pediátricos refractarios o en recaída, entre ellos tumores de Ewing.

El puntaje TxGNN es muy alto (0.99999), pero es solo una predicción del modelo. No sustituye a la evidencia clínica específica en Ewing, que por ahora no está confirmada.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00003234](https://clinicaltrials.gov/study/NCT00003234) | Fase 2 | Completado | 50 | Vinorelbina en niños con neoplasias recurrentes o refractarias; no se confirma una cohorte específica de Ewing |
| [NCT00180947](https://clinicaltrials.gov/study/NCT00180947) | Fase 2 | Desconocido | 210 | Vinorelbina + ciclofosfamida en tumores refractarios o en recaída (rabdomiosarcoma, tumores de Ewing, osteosarcoma, neuroblastoma, meduloblastoma); resultados específicos de Ewing no verificables |
| [NCT05999994](https://clinicaltrials.gov/study/NCT05999994) | Fase 2 | Reclutando | 105 | CAMPFIRE: protocolo maestro pediátrico; no se confirma un brazo con vinorelbina |
| [NCT06451302](https://clinicaltrials.gov/study/NCT06451302) | N/A | Activo, sin reclutar | 100 | Cohorte prospectiva sobre tratamiento estratificado por riesgo en sarcoma de Ewing pediátrico en China; observacional, sin confirmar que incluya vinorelbina |

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 84245 | VINORELBINA GLENMARK 20 MG CÁPSULAS BLANDAS EFG | Cápsula blanda |
| 88631 | VINORELBINA ACCORD 80 MG CÁPSULA BLANDA EFG | Cápsula blanda |
| 65978 | NAVELBINE 20 mg CÁPSULAS BLANDAS | Cápsula blanda |
| 72511 | VINORELBINA IPS 10 mg/ml CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN EFG | Concentrado para solución para perfusión |
| 87420 | VINORELBINA MEDAC 80 MG CÁPSULAS BLANDAS EFG | Cápsula blanda |

Se muestran 5 de las 16 autorizaciones. Existen presentaciones oral e intravenosa. Los datos recuperados no incluyen el texto de indicación aprobada.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (alcaloide de la vinca, antimitótico) |
| Riesgo de Mielosupresión | Alto: la literatura recuperada describe la mielosupresión como toxicidad limitante de la dosis |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con fórmula leucocitaria; función hepática y renal |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto; aplicar la normativa de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un mecanismo citotóxico plausible y ensayos de Fase 2 en tumores pediátricos, incluidos tumores de Ewing. Sin embargo, la evidencia específica en Ewing no está confirmada y no hay literatura de respaldo, por lo que el nivel L2 es provisional.

**Para avanzar se necesita:**
- Confirmar si NCT00003234 y NCT00180947 incluyen cohortes de Ewing con resultados publicados, y si CAMPFIRE tiene un brazo con vinorelbina
- Buscar literatura específica de vinorelbina en sarcoma de Ewing
- Descargar y analizar el prospecto de AEMPS (advertencias, contraindicaciones, emetogenicidad y manejo)
- Obtener los datos del mecanismo de acción desde DrugBank
- Otras predicciones del modelo (por ejemplo, carcinoma de pulmón de células pequeñas) tienen evidencia indirecta o mezclada con cáncer de pulmón no microcítico, y no deben priorizarse
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

