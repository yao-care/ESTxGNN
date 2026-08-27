---
layout: default
title: Gefitinib
parent: 僅模型預測 (L5)
nav_order: 133
evidence_level: L5
indication_count: 10
---

# Gefitinib
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

# Gefitinib: De Cáncer de Pulmón No Microcítico a Fibromatosis Gingival

## Resumen en Una Frase

Gefitinib es un inhibidor de la tirosina quinasa del receptor del factor de crecimiento epidérmico (EGFR-TKI), utilizado originalmente en el tratamiento del cáncer de pulmón no microcítico (CPNM) con mutación EGFR positiva. El modelo TxGNN predice que podría ser efectivo para **Fibromatosis Gingival**, pero actualmente **no existe ningún ensayo clínico ni publicación científica** que respalde esta dirección: se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de pulmón no microcítico (CPNM) con mutación EGFR positiva (información pública conocida; no confirmada en los campos estructurados del Evidence Pack) |
| Nueva Indicación Predicha | Fibromatosis Gingival |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en este Evidence Pack (dato marcado como brecha de alta severidad, DG002). Según información pública conocida, gefitinib es un inhibidor selectivo de la tirosina quinasa del EGFR, cuya eficacia en el cáncer de pulmón no microcítico con mutación EGFR positiva está ampliamente comprobada y constituye uno de los pilares de la terapia dirigida en oncología torácica.

Sin embargo, la fibromatosis gingival es una condición fibroproliferativa benigna de la encía, cuya patogénesis conocida no está impulsada por la vía de señalización EGFR. No existe, por tanto, un puente mecanístico establecido entre la indicación original (neoplasia maligna EGFR-dependiente) y la indicación predicha (proliferación fibrosa benigna no EGFR-dependiente).

En consecuencia, esta predicción se apoya únicamente en la puntuación de similitud del modelo TxGNN (99.89%, rango 2513), sin ningún ensayo clínico ni artículo de literatura que la respalde. Se trata de una asociación puramente computacional, sin base mecanística ni clínica verificable hasta la fecha.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Gefitinib no está actualmente comercializado en España (0 autorizaciones registradas en el Evidence Pack).

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa del EGFR) |
| Riesgo de Mielosupresión | Bajo (los EGFR-TKI presentan típicamente menor riesgo de mielosupresión que la quimioterapia citotóxica convencional; consultar el prospecto para datos específicos) |
| Clasificación de Emetogenicidad | Baja |
| Items de Monitoreo | Función hepática (transaminasas), función pulmonar (riesgo de enfermedad pulmonar intersticial), piel (erupción cutánea/acneiforme), intervalo QT |
| Protección en Manejo | Consultar el prospecto y las normativas vigentes de manejo de agentes antineoplásicos dirigidos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción "Fibromatosis Gingival" carece de todo respaldo clínico o bibliográfico y no presenta un vínculo mecanístico plausible con la vía EGFR; es una predicción de nivel L5 basada exclusivamente en el score del modelo. Adicionalmente, la ausencia del prospecto de la TFDA (brecha bloqueante, DG001) impide siquiera iniciar la evaluación de seguridad inicial (S1).

**Para avanzar se necesita:**
- Obtener el prospecto/ficha técnica oficial (advertencias y contraindicaciones) — brecha bloqueante actual
- Confirmar el mecanismo de acción detallado de gefitinib vía DrugBank
- Estudios preclínicos que exploren una relación biológica entre la vía EGFR y la fibromatosis gingival, hoy inexistente
- Nota complementaria: dentro de este mismo Evidence Pack, el candidato "lung hilum carcinoma" (rank 5, L3, Proceed with Guardrails) presenta una base mecanística mucho más sólida — al ser un subtipo anatómico de CPNM — y podría ser un candidato prioritario alternativo para esta molécula.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

