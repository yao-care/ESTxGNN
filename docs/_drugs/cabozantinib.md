---
layout: default
title: Cabozantinib
parent: 僅模型預測 (L5)
nav_order: 51
evidence_level: L5
indication_count: 10
---

# Cabozantinib
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

# Cabozantinib: De Carcinoma de Células Renales a Liposarcoma

## Resumen en Una Frase

Cabozantinib es un inhibidor multiquinasa (MET/VEGFR1-3/RET/AXL/KIT/TIE2) cuya indicación consolidada a nivel internacional es el carcinoma de células renales avanzado (respaldada por ensayos pivotales como METEOR y CheckMate 9ER), aunque en el registro de este mercado no consta actualmente como comercializado. El modelo TxGNN predice que podría ser efectivo para **Liposarcoma**, con **1 ensayo clínico** y **1 publicación** que actualmente respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Carcinoma de células renales (indicación consolidada a nivel internacional; sin licencias ni texto de indicación registrados en este mercado) |
| Nueva Indicación Predicha | Liposarcoma |
| Puntaje de Predicción TxGNN | 99.83% |
| Nivel de Evidencia | L2 |
| Estado de Mercado | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Research Question |

## ¿Por qué es Razonable esta Predicción?

Cabozantinib es un inhibidor de múltiples tirosina quinasas, con actividad principal sobre MET, VEGFR1-3, RET, AXL, KIT y TIE2. Esta información de mecanismo de acción no proviene del registro estructurado de DrugBank (marcado como dato pendiente en este informe), sino que se ha reconstruido a partir de la caracterización farmacológica conocida del fármaco.

El liposarcoma, como otros sarcomas de tejido blando, presenta con frecuencia dependencia de la angiogénesis y activación de las vías MET/VEGFR, un mecanismo ya explotado terapéuticamente en sarcomas mediante otros inhibidores antiangiogénicos (p. ej., pazopanib). Esta base mecanística ofrece una justificación razonable para explorar cabozantinib en sarcomas, incluido el liposarcoma, aunque de forma no específica: el ensayo disponible incluye sarcoma de tejido blando en general, sin diseño dirigido exclusivamente a liposarcoma.

En conjunto, la señal de TxGNN es mecanísticamente plausible pero todavía preliminar: se apoya en un ensayo de fase 2 en curso (sin lectura de resultados) y un estudio de fase 1 sobre una subpoblación relacionada (sarcomas de extremidades), por lo que se recomienda tratarla como pregunta de investigación más que como candidata lista para avanzar.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT05836571](https://clinicaltrials.gov/study/NCT05836571) | Fase 2 | En curso (no reclutando) | 66 | Ensayo randomizado que compara ipilimumab+nivolumab solos vs. en combinación con cabozantinib en sarcoma de tejido blando avanzado; sin lectura de resultados aún (finalización estimada 2026-05) |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41770651](https://pubmed.ncbi.nlm.nih.gov/41770651/) | 2026 | Ensayo Fase 1 (neoadyuvante + radioterapia) | American Journal of Clinical Oncology | Evalúa la seguridad de cabozantinib concurrente con radioterapia como terapia neoadyuvante en sarcoma de tejido blando de extremidades; el uso combinado con RT se había limitado por riesgo de fístula/perforación |

## Información de Mercado

Actualmente no hay autorizaciones registradas para cabozantinib en este mercado (fármaco no comercializado, 0 licencias).

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor multiquinasa: MET/VEGFR1-3/RET/AXL/KIT/TIE2), no citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Research Question**

**Justificación:**
La evidencia actual para liposarcoma es mecanísticamente razonable pero clínicamente preliminar: un único ensayo de fase 2 aún sin resultados leídos y un estudio de fase 1 en una población de sarcomas relacionada, no específica de liposarcoma. No es suficiente para avanzar a evaluación de guardrails, pero justifica seguimiento activo.

**Para avanzar se necesita:**
- Resultados del ensayo NCT05836571 (finalización estimada mayo 2026)
- Obtener el texto de advertencias/contraindicaciones (仿單) vía TFDA/AEMPS — actualmente bloqueante para la evaluación de seguridad S1 (DG001)
- Confirmar el mecanismo de acción mediante consulta directa a la API de DrugBank (DG002)
- Nota: dentro de este mismo candidato, TxGNN identificó señales con evidencia considerablemente más sólida — carcinoma de células renales no clasificado (L2, S2, Proceed with Guardrails) y carcinoma renal en general (L1, S3, Proceed with Guardrails, respaldado por múltiples ECAs de fase 3 como CheckMate 9ER y METEOR) — que podrían priorizarse como vía de avance más inmediata
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

