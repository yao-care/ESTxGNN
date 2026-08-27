---
layout: default
title: Tacrolimus
parent: 僅模型預測 (L5)
nav_order: 267
evidence_level: L5
indication_count: 3
---

# Tacrolimus
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

# Tacrolimus: De Trasplante de Órganos a Dermatitis Seborreica

## Resumen en Una Frase

Tacrolimus es un inhibidor de calcineurina utilizado originalmente para la prevención del rechazo en trasplante de órganos sólidos. El modelo TxGNN predice que podría ser efectivo para **Dermatitis Seborreica**, con **2 ensayos clínicos** (Fase 3 y Fase 4, ambos completados) y **20 publicaciones** que actualmente respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Prevención del rechazo de injerto en trasplante de órganos (indicación sistémica reconocida internacionalmente; sin registro de licencias en el mercado evaluado) |
| Nueva Indicación Predicha | Dermatitis Seborreica |
| Puntaje de Predicción TxGNN | 99.26% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción específico en esta ficha. Según la información conocida, tacrolimus pertenece a la clase de los inhibidores de calcineurina (inmunosupresores), su eficacia en la prevención del rechazo de trasplante de órganos ha sido ampliamente comprobada, y mecanísticamente podría ser aplicable a enfermedades inflamatorias cutáneas mediadas por linfocitos T, como la dermatitis seborreica.

En su formulación tópica, tacrolimus ya es ampliamente utilizado (incluyendo uso no autorizado en ficha técnica en varias regiones) para la dermatitis atópica, otra dermatosis inflamatoria mediada por células T. La dermatitis seborreica comparte con la dermatitis atópica un componente inflamatorio T-dependiente y una disfunción de la barrera cutánea, lo que hace mecanísticamente plausible la extrapolación entre ambas indicaciones.

La inhibición de calcineurina reduce la respuesta inflamatoria local mediada por linfocitos T, y existe literatura que sugiere una modulación indirecta sobre la disfunción de la barrera cutánea inflamatoria asociada a *Malassezia*, un factor etiológico relevante en la dermatitis seborreica. Esta convergencia mecanística con la dermatitis atópica —indicación ya validada para tacrolimus tópico— respalda la alta plausibilidad de la extrapolación entre indicaciones que sugiere el modelo TxGNN.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Fase 3 | Completado | 120 | Interés del ungüento de tacrolimus (Protopic®) en el tratamiento de mantenimiento de la dermatitis seborreica facial grave del adulto; busca reducir recaídas y el uso de esteroides tópicos |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Fase 4 | Completado | 104 | Tratamiento proactivo con ungüento de tacrolimus al 0.1% (1-2 veces/semana) para mantener la remisión y reducir exacerbaciones en dermatitis seborreica facial del adulto |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33010323](https://pubmed.ncbi.nlm.nih.gov/33010323/) | 2021 | ECA | J Am Acad Dermatol | Estudio multicéntrico, doble ciego, aleatorizado: tacrolimus 0.1% vs. ciclopiroxolamina 1% como terapia de mantenimiento en dermatitis seborreica facial grave |
| [22101215](https://pubmed.ncbi.nlm.nih.gov/22101215/) | 2012 | ECA | J Am Acad Dermatol | Ensayo aleatorizado simple ciego: hidrocortisona 1% vs. tacrolimus 0.1% en dermatitis seborreica facial en adultos |
| [24171300](https://pubmed.ncbi.nlm.nih.gov/24171300/) | 2013 | Ensayo clínico | Ann Parasitol | Comparación de eficacia entre sertaconazol 2% crema y tacrolimus 0.03% crema en 60 pacientes con dermatitis seborreica |
| [37067129](https://pubmed.ncbi.nlm.nih.gov/37067129/) | 2023 | Ensayo clínico | Indian J Dermatol Venereol Leprol | Itraconazol oral (2 días) + tacrolimus tópico vs. tacrolimus solo como tratamiento de mantenimiento en Vietnam |
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | Cohorte | Ann Dermatol | Terapia de mantenimiento de dermatitis seborreica facial con ungüento de tacrolimus 0.1%, extrapolando el régimen de uso intermitente validado en dermatitis atópica |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Revisión sistemática | Am J Clin Dermatol | Revisión sistemática del tratamiento tópico de la dermatitis seborreica facial: antifúngicos, queratolíticos y corticosteroides como primera línea |
| [19222250](https://pubmed.ncbi.nlm.nih.gov/19222250/) | 2009 | Revisión | Am J Clin Dermatol | Rol de los inhibidores tópicos de calcineurina en dermatitis seborreica: fisiopatología, seguridad y eficacia como alternativa a corticosteroides |
| [12833030](https://pubmed.ncbi.nlm.nih.gov/12833030/) | 2003 | Estudio piloto abierto | J Am Acad Dermatol | Estudio piloto abierto en 18 pacientes: 61% mostró aclaramiento completo de dermatitis seborreica con tacrolimus 0.1% en 28 días |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Revisión | J Drugs Dermatol | Estado actual y horizontes terapéuticos de la dermatitis seborreica facial, incluyendo el rol emergente de los inhibidores de calcineurina |
| [15461548](https://pubmed.ncbi.nlm.nih.gov/15461548/) | 2004 | Revisión | Expert Opin Pharmacother | Revisión del ungüento de tacrolimus en dermatitis atópica y otras enfermedades cutáneas inflamatorias, con mecanismo de inhibición de calcineurina aplicable a dermatosis relacionadas |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La evidencia de Nivel L1 —dos ensayos clínicos completados (Fase 3 y Fase 4) directamente en dermatitis seborreica facial, respaldados por un ECA multicéntrico doble ciego adicional (Joly 2021) y múltiples estudios comparativos— sustenta una plausibilidad clínica alta. Sin embargo, la ausencia de datos locales de seguridad (advertencias, contraindicaciones) y del mecanismo de acción detallado impide aún un cierre completo de la evaluación de seguridad inicial.

**Para avanzar se necesita:**
- Advertencias y contraindicaciones del prospecto TFDA/AEMPS (brecha bloqueante, DG001) — necesario para completar la evaluación de seguridad S1
- Datos detallados del mecanismo de acción vía DrugBank (DG002)
- Evaluación de interacciones farmacológicas (DDI), actualmente sin resultados ("not_found")
- Ruta de registro/autorización en el mercado evaluado, dado que actualmente no hay licencias activas (0 autorizaciones)
- Nota: el modelo también identificó candidatos adicionales de menor madurez de evidencia (parapsoriasis, L4/Hold; dermatitis atópica-relacionada, aún sin puntuar) que podrían explorarse en fases posteriores
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

