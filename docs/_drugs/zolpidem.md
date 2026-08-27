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

# ZOLPIDEM: Indicación Original No Documentada → Trastorno de Inicio y Mantenimiento del Sueño (Insomnio)

## Resumen en Una Frase

La indicación original de ZOLPIDEM no está documentada en este Evidence Pack (data gap regulatorio, ver DG001/DG002). El modelo TxGNN predice que podría ser efectivo para el **Trastorno de Inicio y Mantenimiento del Sueño (Insomnio)**, con una puntuación de predicción del **99.87%**. Actualmente no hay ensayos clínicos registrados específicamente vinculados a esta predicción, pero **20 publicaciones científicas** —incluyendo varios ensayos clínicos aleatorizados (ECA) y metaanálisis en red— respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No documentada en el paquete de evidencia (ver data gap DG001/DG002) |
| Nueva Indicación Predicha | Trastorno de Inicio y Mantenimiento del Sueño (Insomnio) |
| Puntaje de Predicción TxGNN | 99.87% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

No se dispone de datos formales de mecanismo de acción a nivel de ficha del fármaco (campo `original_moa` marcado como data gap, DG002, severidad High). Sin embargo, el análisis de justificación mecanística asociado a esta predicción sí describe la farmacología de ZOLPIDEM: se une selectivamente a la subunidad α1 del receptor GABA-A, potenciando la frecuencia de apertura del canal de cloruro y produciendo un efecto sedante-hipnótico.

Esta acción farmacológica corresponde directamente a la fisiopatología del insomnio (dificultad para iniciar y/o mantener el sueño). De hecho, la propia justificación del modelo señala que esta indicación es, mecanísticamente, la **indicación primaria/central** del fármaco más que un reposicionamiento especulativo — lo cual es coherente con el hecho de que ZOLPIDEM es clínicamente conocido como un hipnótico no benzodiazepínico ("fármaco Z") de uso establecido para el insomnio.

Dado que la ficha de indicaciones originales y la de advertencias del prospecto están vacías en este paquete de evidencia, no es posible en este momento contrastar formalmente "indicación original" vs. "indicación predicha" — el hallazgo relevante aquí es más bien una **validación del modelo** (el TxGNN recupera correctamente el perfil terapéutico conocido del fármaco) que un descubrimiento de una nueva indicación no relacionada.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31880796](https://pubmed.ncbi.nlm.nih.gov/31880796/) | 2019 | ECA (Fase 3) | JAMA Network Open | Comparación de lemborexant vs. placebo vs. zolpidem tartrato ER en adultos mayores con insomnio |
| [39879708](https://pubmed.ncbi.nlm.nih.gov/39879708/) | 2025 | ECA | Sleep Medicine | Análisis post-hoc del efecto de lemborexant sobre la arquitectura del sueño en insomnio con apnea obstructiva leve comórbida |
| [39374004](https://pubmed.ncbi.nlm.nih.gov/39374004/) | 2024 | ECA | JAMA Internal Medicine | Ensayo de reducción gradual enmascarada combinada con terapia conductual para discontinuar agonistas del receptor de benzodiazepinas (incluye fármacos Z) |
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | Metaanálisis/NMA | Lancet | Revisión sistemática y metaanálisis en red de intervenciones farmacológicas para el manejo agudo y a largo plazo del insomnio |
| [34121443](https://pubmed.ncbi.nlm.nih.gov/34121443/) | 2021 | Metaanálisis/NMA | J Manag Care Spec Pharm | Eficacia comparativa de lemborexant frente a otros tratamientos del insomnio mediante metaanálisis en red |
| [22424586](https://pubmed.ncbi.nlm.nih.gov/22424586/) | 2012 | Revisión/Cochrane | Expert Opin Pharmacother | Revisión específica de zolpidem como agonista del receptor benzodiazepínico, el hipnótico más prescrito en EE.UU. |
| [37549414](https://pubmed.ncbi.nlm.nih.gov/37549414/) | 2023 | Revisión | J Fam Pract | Actualización sobre manejo del insomnio en atención primaria |
| [29487083](https://pubmed.ncbi.nlm.nih.gov/29487083/) | 2018 | Revisión | Pharmacol Rev | Fármacos para el insomnio más allá de las benzodiazepinas, incluyendo perfil de efectos adversos de los fármacos Z (zolpidem, zopiclona, zaleplón) |
| [31953863](https://pubmed.ncbi.nlm.nih.gov/31953863/) | 2020 | Revisión | Annals of Neurology | Relación dosis-respuesta de daridorexant, nuevo antagonista dual del receptor de orexina, en el trastorno de insomnio |
| [28845958](https://pubmed.ncbi.nlm.nih.gov/28845958/) | 2017 | Revisión | FP Essentials | Panorama general de los trastornos del sueño e insomnio en medicina familiar |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La predicción está respaldada por un nivel de evidencia L1, con múltiples ECA y metaanálisis en red que confirman el papel establecido de ZOLPIDEM (y su clase de fármacos Z) en el tratamiento del insomnio. Sin embargo, la ausencia de datos regulatorios sobre advertencias/contraindicaciones del prospecto (DG001, severidad *Blocking*) impide avanzar a la evaluación de seguridad inicial (S1) sin antes remediar este vacío.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto (ficha técnica) de TFDA/AEMPS con advertencias y contraindicaciones (DG001 — bloqueante)
- Consultar la API de DrugBank para obtener el mecanismo de acción formal a nivel de fármaco (DG002)
- Confirmar el estado real de comercialización en España, dado que el paquete de evidencia indica "no comercializado" con 0 autorizaciones
- Evaluar interacciones farmacológicas (DDI), actualmente sin datos ("not_found")
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

