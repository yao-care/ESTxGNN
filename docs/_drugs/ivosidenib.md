---
layout: default
title: Ivosidenib
parent: 僅模型預測 (L5)
nav_order: 154
evidence_level: L5
indication_count: 3
---

# Ivosidenib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Ivosidenib: De Leucemia Mieloide Aguda con Mutación IDH1 a LMA/SMD Relacionados con Tratamiento Oncológico Previo

## Resumen en Una Frase

Ivosidenib (DrugBank DB14568) es conocido públicamente como inhibidor de la enzima IDH1 mutada, usado en leucemia mieloide aguda (LMA) con esta mutación; sin embargo, esta información **no consta en el Evidence Pack analizado** y debe verificarse contra fuentes primarias antes de usarse. El modelo TxGNN predice que podría ser efectivo para **LMA/SMD relacionados con tratamiento oncológico previo** (radioterapia o agentes alquilantes), pero esta dirección no cuenta actualmente con **ningún ensayo clínico ni publicación** que la respalde — es una predicción puramente computacional (Nivel de Evidencia **L5**).

> Nota: la predicción mejor puntuada por TxGNN para este fármaco fue "bulbar polio" (99.3%, rank 9697). Se excluye de este informe porque el propio Evidence Pack la señala como carente de plausibilidad biológica y probable artefacto de embedding del grafo de conocimiento — no un candidato de reposicionamiento razonable.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en el Evidence Pack (dato de dominio público sin verificar en esta fuente: LMA con mutación IDH1) |
| Nueva Indicación Predicha | LMA / SMD relacionados con tratamiento oncológico previo (radioterapia o agentes alquilantes) |
| Puntaje de Predicción TxGNN | 99.26% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

El Evidence Pack no contiene datos del mecanismo de acción (MOA) de ivosidenib — este campo está marcado como brecha de datos de severidad **Alta**, lo que limita cualquier análisis mecanístico riguroso. Por conocimiento general del fármaco (no confirmado en esta fuente), ivosidenib es un inhibidor selectivo de la forma mutada de la enzima IDH1, relevante en neoplasias hematológicas donde esta mutación está presente.

La relación entre la indicación original conocida (LMA con mutación IDH1) y la nueva indicación predicha (LMA/SMD relacionados con tratamiento oncológico previo) es mecanísticamente coherente: las neoplasias mieloides secundarias a agentes alquilantes o a radioterapia presentan, en una proporción documentada en la literatura general, mutaciones en IDH1/IDH2 junto con TP53. Si el tumor del paciente porta la mutación IDH1, el fundamento biológico para extender el uso del fármaco es razonable.

Dicho esto, esta hipótesis mecanística **no está respaldada por ningún ensayo clínico ni publicación** en el Evidence Pack, y el propio informe de origen la clasifica como "Research Question" en fase de decisión S0 (etapa más temprana, previa a cualquier evaluación de seguridad). No debe interpretarse como una señal con evidencia real, sino como una hipótesis a investigar.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> El Evidence Pack señala una brecha de datos **Bloqueante**: no se dispone del prospecto/ficha técnica de la agencia reguladora con las advertencias y contraindicaciones oficiales. Esto impide, por sí solo, avanzar el candidato a la fase de evaluación inicial de seguridad (S1).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- Las tres indicaciones predichas están en fase S0 (etapa más temprana), sin ningún ensayo clínico ni publicación que las respalde — la única evidencia disponible es el puntaje de un modelo predictivo (L5).
- La predicción con mayor puntaje ("bulbar polio") fue descartada como artefacto sin plausibilidad biológica, lo que reduce la confianza en el resto del ranking.
- Existe una brecha de datos bloqueante (ficha técnica/warnings de la agencia reguladora) que impide iniciar siquiera la evaluación de seguridad.

**Para avanzar se necesita:**
- Obtener el prospecto oficial y sus advertencias/contraindicaciones (brecha bloqueante DG001).
- Confirmar el mecanismo de acción vía DrugBank/literatura primaria (brecha DG002).
- Verificar la indicación original y el estado regulatorio real del fármaco (los campos correspondientes están vacíos en esta fuente).
- Buscar literatura específica sobre prevalencia de mutación IDH1 en LMA/SMD secundarias a tratamiento, para sustentar o descartar la hipótesis mecanística antes de cualquier decisión de avance.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

