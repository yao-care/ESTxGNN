---
layout: default
title: Carvedilol
parent: 僅模型預測 (L5)
nav_order: 61
evidence_level: L5
indication_count: 5
---

# Carvedilol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Carvedilol: De Hipertensión Arterial a Hipertensión Renovascular Maligna

## Resumen en Una Frase

Carvedilol es un betabloqueante no selectivo con actividad bloqueante alfa-1, de uso clínico habitual en hipertensión arterial e insuficiencia cardíaca (no consta una indicación aprobada específica en el registro disponible). El modelo TxGNN predice que podría ser efectivo para **Hipertensión Renovascular Maligna**, pero esta dirección no cuenta actualmente con **ningún ensayo clínico** ni **publicación** que la respalde directamente.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Hipertensión arterial (uso clínico habitual; sin indicación aprobada registrada en la fuente disponible) |
| Nueva Indicacion Predicha | Hipertensión Renovascular Maligna |
| Puntaje de Prediccion TxGNN | 99.55% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Espana | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción (MOA) de carvedilol en esta fuente. Según la información conocida, carvedilol es un betabloqueante no selectivo β1/β2 con actividad adicional bloqueante alfa-1, cuyo mecanismo antihipertensivo combina reducción del gasto cardíaco, vasodilatación periférica e inhibición de la liberación de renina.

La hipertensión renovascular maligna suele asociarse a una activación excesiva del sistema renina-angiotensina. En teoría, el bloqueo combinado alfa/beta de carvedilol podría contribuir al control tensional en este contexto, pero se trata de una extrapolación indirecta a partir de su mecanismo antihipertensivo general, sin evidencia dirigida a este subtipo específico (renovascular, maligno).

El alto puntaje de TxGNN probablemente refleja la asociación del fármaco con la categoría amplia de "hipertensión" más que una especificidad real para esta presentación clínica grave y poco frecuente, que habitualmente requiere manejo hipotensor intravenoso urgente.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Informacion de Mercado en Espana

Carvedilol no está comercializado en España según los datos disponibles (0 autorizaciones registradas).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La predicción para hipertensión renovascular maligna se apoya únicamente en la inferencia del modelo TxGNN (L5), sin ningún ensayo clínico ni publicación de respaldo, y el fármaco no está comercializado en España. No existe base suficiente para avanzar a una evaluación de seguridad o clínica.

**Para avanzar se necesita:**
- Datos verificados del mecanismo de acción (MOA) vía DrugBank
- Advertencias y contraindicaciones desde el prospecto oficial (actualmente bloqueante para la evaluación de seguridad S1)
- Búsqueda de literatura dirigida específicamente a carvedilol en hipertensión renovascular/maligna, no solo en hipertensión general
- Revisión de las otras 4 indicaciones candidatas del mismo evidence pack (hipertensión pulmonar por enfermedad pulmonar/hipoxia, con nivel L4 pero literatura de baja relevancia directa; síndrome de Braddock, entre otras) antes de priorizar recursos de validación
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

