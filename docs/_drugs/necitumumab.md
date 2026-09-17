---
layout: default
title: Necitumumab
parent: Solo predicción del modelo (L5)
nav_order: 192
evidence_level: L5
indication_count: 10
---

# Necitumumab
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

# Necitumumab: De Carcinoma Escamoso de Pulmón a Fibromatosis Gingival

## Resumen en Una Frase

Necitumumab es un anticuerpo monoclonal humano anti-EGFR, aprobado originalmente (según literatura internacional) en combinación con gemcitabina y cisplatino para el carcinoma escamoso de pulmón no microcítico (NSCLC) metastásico. El modelo TxGNN predice que podría ser efectivo para **Fibromatosis Gingival**, pero actualmente **no existe ningún ensayo clínico ni publicación** que respalde esta dirección: se trata únicamente de una puntuación alta del modelo, sin base mecanística ni evidencia real.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Carcinoma escamoso de pulmón no microcítico (NSCLC) metastásico, en combinación con gemcitabina/cisplatino (según literatura asociada; no confirmado en registro regulatorio de España) |
| Nueva Indicación Predicha | Fibromatosis Gingival |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del candidato (dato marcado como brecha de alta prioridad). Según la literatura asociada a este expediente, necitumumab es un anticuerpo monoclonal IgG1 humano de segunda generación dirigido contra el receptor del factor de crecimiento epidérmico (EGFR), cuya eficacia en el carcinoma escamoso de pulmón no microcítico metastásico ha sido demostrada en el ensayo de fase 3 SQUIRE.

La fibromatosis gingival es una proliferación benigna del tejido conectivo fibroso de la encía, sin relación establecida con la vía de señalización EGFR ni con procesos de oncogénesis o proliferación tumoral. El propio análisis mecanístico del candidato señala que **no existe un vínculo conocido** entre el mecanismo antitumoral de necitumumab y esta condición, y no hay evidencia clínica ni de literatura que la respalde: la predicción se sostiene únicamente en la puntuación del modelo TxGNN.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (anticuerpo monoclonal anti-EGFR) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Ítems de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ningún ensayo clínico, publicación ni base mecanística conocida que respalde la relación entre necitumumab y la fibromatosis gingival; la puntuación TxGNN por sí sola no es suficiente para avanzar esta indicación.

**Para avanzar se necesita:**
- Ficha técnica/prospecto de TFDA con advertencias y contraindicaciones (brecha bloqueante, DG001)
- Datos de mecanismo de acción (MOA) verificados vía DrugBank (DG002)
- Estudio mecanístico o preclínico que justifique una relación biológica plausible con fibromatosis gingival antes de continuar

**Observación adicional:** dentro de este mismo paquete de evidencia, la entrada "lung benign neoplasm" (rango 7) presenta 20 publicaciones con nivel de evidencia L1, pero el análisis mecanístico indica que esa literatura describe en realidad el uso establecido de necitumumab en NSCLC escamoso, no la neoplasia benigna listada — un posible error de correspondencia de etiquetas del modelo. Se recomienda revisar ese registro por separado, ya que podría reflejar mejor la indicación con mayor solidez de evidencia real dentro de este candidato.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

