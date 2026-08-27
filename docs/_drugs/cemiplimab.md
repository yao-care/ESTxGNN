---
layout: default
title: Cemiplimab
parent: 僅模型預測 (L5)
nav_order: 65
evidence_level: L5
indication_count: 10
---

# Cemiplimab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Cemiplimab: De Carcinoma Cutáneo de Células Escamosas a Carcinoma Adenoescamoso de Vesícula Biliar

## Resumen en Una Frase

Cemiplimab es un inhibidor del punto de control inmunitario anti-PD-1, originalmente aprobado para el carcinoma cutáneo de células escamosas (CSCC) avanzado. El modelo TxGNN predice que podría ser efectivo para **carcinoma adenoescamoso de vesícula biliar**, con una puntuación de predicción del **99.99%**, pero actualmente **sin ningún ensayo clínico ni publicación** que respalde esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Carcinoma Cutáneo de Células Escamosas (CSCC)* |
| Nueva Indicación Predicha | Carcinoma Adenoescamoso de Vesícula Biliar |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

*El paquete de evidencia no incluye licencias en `taiwan_regulatory.licenses` (campo vacío); la indicación original citada se basa en la aprobación conocida del fármaco (FDA), no en un dato del propio paquete.

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia (brecha de datos DG002, severidad Alta). Según la información conocida —y tal como referencian los propios razonamientos de reposicionamiento del modelo para otras indicaciones de este mismo candidato (rangos 2 y 4)—, cemiplimab es un inhibidor del punto de control inmunitario anti-PD-1, con eficacia comprobada en carcinoma cutáneo de células escamosas avanzado, carcinoma basocelular y cáncer de pulmón no microcítico.

Sin embargo, para la indicación de mayor puntuación de este candidato —el carcinoma adenoescamoso de vesícula biliar— el propio paquete de evidencia señala que se trata de una neoplasia rara, con escasa caracterización de su microambiente inmunitario tumoral. La predicción se basa únicamente en la puntuación alta del modelo TxGNN, sin ningún respaldo mecanístico directo, ensayo clínico o publicación disponible en este momento. La plausibilidad biológica es, por tanto, especulativa y requiere validación adicional antes de avanzar.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida / Inmunoterapia (inhibidor de punto de control PD-1) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación de mayor puntuación TxGNN para este candidato (carcinoma adenoescamoso de vesícula biliar) carece por completo de evidencia real —ni ensayos clínicos ni literatura— y corresponde a nivel de evidencia L5 (solo predicción del modelo). No es razonable avanzar sin al menos evidencia mecanística o preclínica de respaldo.

**Para avanzar se necesita:**
- Resolver la brecha bloqueante DG001 (advertencias/contraindicaciones del prospecto TFDA), indispensable para cualquier evaluación de seguridad S1
- Datos de mecanismo de acción (MOA) estructurados (DG002)
- Búsqueda dirigida de literatura preclínica o de mecanismo sobre PD-1 en neoplasias biliares/vesícula biliar
- Confirmación de vías de administración y compatibilidad de formulación

**Nota adicional:** Este candidato agrupa 10 indicaciones predichas por TxGNN para cemiplimab. De ellas, la de rango 4 (carcinoma basocelular de oído externo) presenta evidencia sustancialmente más sólida —nivel L4, con un caso publicado (PMID 34157152) y extensión plausible de la indicación de carcinoma basocelular ya aprobada— y está clasificada como **Proceed with Guardrails**. Se recomienda priorizar esa indicación para evaluación separada en lugar de la de mayor puntuación aquí reportada.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

