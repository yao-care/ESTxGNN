---
layout: default
title: Diltiazem
parent: 僅模型預測 (L5)
nav_order: 93
evidence_level: L5
indication_count: 1
---

# Diltiazem
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Diltiazem: De Hipertensión y Angina a Susceptibilidad a Ictus Isquémico

## Resumen en Una Frase

Diltiazem es un bloqueador de los canales de calcio no-dihidropiridínico, utilizado clásicamente para el control de la hipertensión, la angina de pecho y las arritmias. El modelo TxGNN predice que podría estar asociado con **"obsolete susceptibility to ischemic stroke"**, pero esta dirección no cuenta actualmente con ningún ensayo clínico ni publicación que la respalde — se trata de una predicción computacional aislada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión, angina de pecho y arritmias (según clase farmacológica) |
| Nueva Indicación Predicha | Susceptibilidad a Ictus Isquémico ("obsolete susceptibility to ischemic stroke") |
| Puntaje de Predicción TxGNN | 99.08% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción específico para esta indicación. Según la información conocida, diltiazem es un bloqueador de los canales de calcio no-dihidropiridínico (CCB), cuya eficacia en el control de la hipertensión, la angina de pecho y las arritmias está bien establecida. Mecanísticamente, el control de la presión arterial es un factor de riesgo modificable relevante para el ictus isquémico, lo que ofrece una base teórica indirecta para esta dirección — pero se trata de un razonamiento a nivel de clase farmacológica, no de evidencia mecanística específica para esta indicación.

**Advertencia importante:** el nombre de la indicación predicha, "obsolete susceptibility to ischemic stroke", contiene el término "obsolete", lo que sugiere una posible anomalía en la etiqueta de la ontología o el grafo de conocimiento utilizado por el modelo. Antes de avanzar con esta candidatura es necesario confirmar que se trata de un concepto clínico válido y no de ruido en los datos de origen.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia disponible se limita a la predicción del modelo TxGNN (L5), sin ningún ensayo clínico ni publicación que la respalde, y el propio nombre de la indicación presenta una anomalía ("obsolete") que debe aclararse antes de invertir más recursos. Además, faltan datos de seguridad regulatoria de carácter bloqueante.

**Para avanzar se necesita:**
- Confirmar si "obsolete susceptibility to ischemic stroke" es un concepto clínico válido o un artefacto del grafo de conocimiento
- Obtener las advertencias, contraindicaciones y ficha técnica oficial (AEMPS/TFDA) del diltiazem — actualmente bloqueante para la evaluación de seguridad (S1)
- Confirmar el mecanismo de acción detallado vía DrugBank u otra fuente farmacológica
- Buscar estudios preclínicos o mecanísticos que vinculen específicamente los CCB con la reducción del riesgo de ictus isquémico
- Verificar el estado de comercialización real en España, dado que actualmente consta como no comercializado
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

