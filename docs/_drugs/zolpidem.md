---
layout: default
title: Zolpidem
parent: 僅模型預測 (L5)
nav_order: 299
evidence_level: L5
indication_count: 3
---

# Zolpidem
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

# Zolpidem: De Insomnio a Trastorno del Sueño de Conciliación y Mantenimiento

## Resumen en Una Frase

Zolpidem es un hipnótico agonista del receptor GABA-A (clase "Z-drug"), utilizado internacionalmente para el tratamiento del insomnio. El modelo TxGNN predice que sería efectivo para **trastorno del sueño de conciliación y mantenimiento**, con **20 publicaciones** que respaldan esta dirección, aunque **no hay ensayos clínicos registrados en esta evidence pack** y, como se detalla más abajo, esta "nueva" indicación coincide en realidad con el uso ya establecido del fármaco.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Insomnio (uso hipnótico internacionalmente establecido; no confirmado por ficha técnica española, ver nota de mercado) |
| Nueva Indicación Predicha | Trastorno del sueño de conciliación y mantenimiento |
| Puntaje de Predicción TxGNN | 99.87% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Zolpidem es un agonista selectivo del receptor GABA-A, específico de la subunidad α1 (clase imidazopiridina), con un mecanismo sedante-hipnótico bien caracterizado y ampliamente descrito en la literatura clínica.

Aquí conviene una aclaración importante: la indicación predicha por TxGNN ("trastorno del sueño de conciliación y mantenimiento") **no es un mecanismo nuevo**, sino la indicación clínica original y ya consolidada de zolpidem. El propio análisis de razonamiento del modelo lo confirma explícitamente: se trata de la indicación aprobada históricamente, no de una hipótesis farmacológica novedosa. Por tanto, la alta puntuación de predicción (99.87%) refleja que el modelo reconoce correctamente la relación fármaco-enfermedad conocida, más que un hallazgo de reposicionamiento genuino.

Lo que sí representa una pregunta abierta y relevante es el **acceso a mercado**: zolpidem no está comercializado en España según los datos disponibles (0 autorizaciones registradas), por lo que el foco práctico de este candidato no es la investigación de una nueva indicación, sino una eventual evaluación regulatoria/comercial de introducción del producto ya validado en otros mercados.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados en esta evidence pack para la indicación predicha.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31880796](https://pubmed.ncbi.nlm.nih.gov/31880796/) | 2019 | ECA (Fase 3) | JAMA Network Open | En adultos mayores con insomnio, lemborexant fue superior a placebo y a zolpidem tartrato de liberación prolongada. |
| [22424586](https://pubmed.ncbi.nlm.nih.gov/22424586/) | 2012 | Revisión | Expert Opin Pharmacother | Revisión de zolpidem como agonista del receptor benzodiazepínico más prescrito para insomnio en EE. UU. |
| [31859791](https://pubmed.ncbi.nlm.nih.gov/31859791/) | 2020 | ECA | Rev Bras Psiquiatr | Ensayo de 3 meses comparando zolpidem sublingual (5 mg) vs oral (10 mg): eficacia y seguridad comparables. |
| [39374004](https://pubmed.ncbi.nlm.nih.gov/39374004/) | 2024 | ECA | JAMA Intern Med | Ensayo de reducción gradual enmascarada de agonistas BZ (incluye zolpidem) combinada con terapia cognitivo-conductual. |
| [37477771](https://pubmed.ncbi.nlm.nih.gov/37477771/) | 2023 | Análisis post-hoc | CNS Drugs | Comparación del efecto de daridorexant y zolpidem sobre número, duración y distribución de despertares nocturnos. |
| [36472134](https://pubmed.ncbi.nlm.nih.gov/36472134/) | 2023 | Estudio comparativo | J Clin Sleep Med | Comparación de eficacia entre lemborexant y zolpidem ER según subtipos de insomnio definidos por polisomnografía. |
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | Meta-análisis/NMA | Lancet | Metaanálisis en red de intervenciones farmacológicas para insomnio agudo y crónico, incluyendo zolpidem. |
| [34121443](https://pubmed.ncbi.nlm.nih.gov/34121443/) | 2021 | Meta-análisis/NMA | J Manag Care Spec Pharm | Comparación de eficacia de lemborexant frente a otros tratamientos de insomnio, incluyendo zolpidem. |
| [16696581](https://pubmed.ncbi.nlm.nih.gov/16696581/) | 2006 | Revisión | CNS Drugs | Revisión de zolpidem de liberación prolongada (formulación bicapa) para inicio y mantenimiento del sueño. |
| [29487083](https://pubmed.ncbi.nlm.nih.gov/29487083/) | 2018 | Revisión | Pharmacol Rev | Revisión de fármacos para insomnio más allá de las benzodiazepinas, incluyendo las "Z-drugs" (zolpidem, zopiclona, zaleplón). |

---

## Información de Mercado en España

Zolpidem no está comercializado en España según los datos disponibles (0 autorizaciones registradas en esta evidence pack).

---

## Consideraciones de Seguridad

No se dispone de ficha técnica española, dado que el producto no está comercializado en España; no se identificaron advertencias, contraindicaciones ni interacciones documentadas en esta evaluación. Se recomienda consultar la ficha técnica de referencia vigente en otros mercados (p. ej. FDA/EMA) o del país de origen antes de cualquier evaluación de seguridad formal.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La evidencia de literatura es sólida (L1, 20 publicaciones incluyendo ECAs y metaanálisis en red) para el uso de zolpidem en el insomnio, pero se trata de su indicación ya establecida y no de un mecanismo de reposicionamiento novedoso. El principal obstáculo no es la evidencia clínica, sino la ausencia de comercialización y de datos regulatorios en España.

**Para avanzar se necesita:**
- Ficha técnica / información de seguridad oficial del producto, dado que actualmente no está comercializado en España (brecha de datos bloqueante)
- Datos de mecanismo de acción (MOA) desde DrugBank, actualmente no disponibles (brecha de datos de alta prioridad)
- Evaluación de viabilidad regulatoria/comercial para introducción en el mercado español, en lugar de un programa de investigación de reposicionamiento

**Nota adicional:** el modelo también generó dos predicciones adicionales de menor confianza para zolpidem —espasmo torsional benigno del lactante y agorafobia— ambas sin ensayos clínicos ni literatura de respaldo (Nivel L5, decisión **Hold**), por lo que no se incluyen como candidatos activos en este informe.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

