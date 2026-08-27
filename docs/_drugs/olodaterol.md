---
layout: default
title: Olodaterol
parent: 僅模型預測 (L5)
nav_order: 203
evidence_level: L5
indication_count: 2
---

# Olodaterol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

Usando el Evidence Pack proporcionado (sin skills de proceso aplicables — es una tarea de redacción directa siguiendo la plantilla ya especificada), genero el informe:

---

# OLODATEROL: De EPOC a Bronquitis

## Resumen en Una Frase

Olodaterol es un agonista β2 de acción ultra-larga (LABA) inhalado, comercializado internacionalmente como monoterapia (Striverdi® Respimat®) o en combinación fija con tiotropio (Spiolto® Respimat®) para el tratamiento de mantenimiento de la EPOC.
El modelo TxGNN predice que podría ser efectivo para **Bronquitis**,
con **3 ensayos clínicos** respaldando actualmente esta dirección, aunque sin literatura específica identificada.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | EPOC (Enfermedad Pulmonar Obstructiva Crónica) — indicación aprobada a nivel internacional; sin registro de comercialización en el mercado evaluado |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L3 |
| Estado de Mercado | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en las fuentes consultadas. Según la información conocida por la literatura incluida en este paquete de evidencia, Olodaterol pertenece a la clase de los agonistas β2-adrenérgicos de acción ultra-larga (LABA); su eficacia como broncodilatador de mantenimiento en la EPOC ha sido ampliamente comprobada mediante múltiples ensayos de Fase 3, y mecanísticamente (relajación del músculo liso bronquial vía activación del receptor β2) podría ser aplicable a la bronquitis crónica, un fenotipo clínico incluido dentro del espectro de la EPOC.

Sin embargo, el término "bronquitis" utilizado en la predicción es ambiguo: engloba tanto la bronquitis aguda (mayoritariamente vírica, autolimitada y sin componente obstructivo) como la bronquitis crónica (fenotipo de EPOC). La plausibilidad mecanística es sólida para esta última, pero débil para la primera. Los tres ensayos disponibles como evidencia son todos estudios post-comercialización de utilización de fármacos o de seguridad a largo plazo en pacientes con EPOC —no ensayos diseñados específicamente para evaluar eficacia en "bronquitis" como entidad independiente—, por lo que la evidencia actual no permite sustentar una indicación diferenciada, sino que refuerza indirectamente el uso ya conocido en EPOC/bronquitis crónica.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT05127304](https://clinicaltrials.gov/study/NCT05127304) | N/A | Completado | 11.316 | Estudio de utilización de recursos sanitarios, costes y desenlaces en pacientes con EPOC que inician tiotropio/olodaterol frente a fluticasona furoato/umeclidinio/vilanterol; datos de mundo real, no ensayo de eficacia directa sobre bronquitis. |
| [NCT02850978](https://clinicaltrials.gov/study/NCT02850978) | N/A | Completado | 1.335 | Vigilancia post-comercialización (PMS) de seguridad y efectividad a largo plazo de la combinación fija tiotropio+olodaterol en pacientes japoneses con EPOC (bronquitis crónica, enfisema); confirma perfil de seguridad, no diseñado para bronquitis como indicación independiente. |
| [NCT03333018](https://clinicaltrials.gov/study/NCT03333018) | N/A | Completado | 22.155 | Estudio de utilización post-autorización de aclidinio (LAMA), no de olodaterol; incluido por asociación de clase terapéutica (broncodilatadores para EPOC), relevancia directa baja por posible desajuste de fármaco. |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia disponible (nivel L3) proviene exclusivamente de estudios post-comercialización de utilización y seguridad en EPOC, no de ensayos diseñados para bronquitis como indicación propia, y uno de los tres estudios corresponde a un fármaco distinto (aclidinio). Además, el candidato no cuenta con registro de comercialización en el mercado evaluado, lo que bloquea la evaluación de seguridad regulatoria (S1).

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank (brecha DG002)
- Prospecto/ficha técnica oficial con advertencias y contraindicaciones (brecha DG001, bloqueante)
- Delimitar si la predicción "bronquitis" se refiere a bronquitis crónica (subtipo de EPOC) o bronquitis aguda, dado que esto determina la validez mecanística
- Ensayos clínicos diseñados específicamente para bronquitis (no solo estudios de utilización en EPOC)
- Confirmación del estado regulatorio/de comercialización en el mercado objetivo
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

