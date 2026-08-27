---
layout: default
title: Neratinib
parent: 僅模型預測 (L5)
nav_order: 194
evidence_level: L5
indication_count: 4
---

# Neratinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Neratinib: De Cáncer de Mama HER2-Positivo a Cáncer de Mama con Receptor de Progesterona Positivo

## Resumen en Una Frase

Neratinib es un inhibidor irreversible de tirosina-quinasa (HER1/HER2/HER4), con uso clínico establecido en cáncer de mama HER2-positivo (terapia adyuvante extendida tras trastuzumab, según el ensayo ExteNET). El modelo TxGNN predice que también podría ser efectivo en **cáncer de mama con receptor de progesterona positivo**, con **5 ensayos clínicos** y **10 publicaciones** que actualmente respaldan esta dirección, aunque la mayoría son de Fase 2 con resultados mixtos (uno en reclutamiento, uno retirado, uno terminado prematuramente).

> **Nota de datos**: No se dispone de indicación original estructurada (`original_indications` y las licencias de referencia están vacías — brecha DG001/DG002). La indicación original citada arriba se reconstruye a partir del contexto de los ensayos y literatura incluidos en este mismo Evidence Pack (p. ej. PMID 26874901), no de un registro regulatorio verificado.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de mama HER2-positivo en estadio temprano, terapia adyuvante extendida tras trastuzumab (inferido de la literatura del Evidence Pack; sin confirmación regulatoria) |
| Nueva Indicación Predicha | Cáncer de mama con receptor de progesterona positivo |
| Puntaje de Predicción TxGNN | 99.68% |
| Nivel de Evidencia | L2 |
| Estado de Mercado | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

## Por qué es Razonable esta Predicción?

No se dispone de datos estructurados de mecanismo de acción (`original_moa` = brecha DG002). Según la información contenida en la literatura de este Evidence Pack, Neratinib es un inhibidor irreversible de tirosina-quinasa de HER1, HER2 y HER4 (PMID 26874901), utilizado clínicamente en el tratamiento del cáncer de mama HER2-positivo.

Los tumores HER2-positivos frecuentemente coexisten con positividad de receptores hormonales (subtipo HR+/HER2+), por lo que el bloqueo de la señalización HER2 por neratinib puede actuar en sinergia con la vía hormonal en tumores con receptor de progesterona positivo. Varios ensayos de este paquete de evidencia combinan directamente neratinib con terapia endocrina (p. ej. NCT04886531: neratinib + inhibidor de aromatasa + trastuzumab en cáncer ER-positivo/HER2-positivo).

Sin embargo, la evidencia específica para la población PR-positiva es todavía limitada: el ensayo con calificación de relevancia más alta (grado A, NCT04886531) está en fase de reclutamiento sin resultados maduros, y dos estudios relacionados fueron retirados o terminados prematuramente por reclutamiento insuficiente. La solidez mecanística se apoya, en gran medida, en la extrapolación desde la población HER2+ ya validada en el ensayo Fase 3 ExteNET.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04886531](https://clinicaltrials.gov/study/NCT04886531) | Fase 2 | Reclutando | 30 | Neratinib + inhibidor de aromatasa + trastuzumab preoperatorio en cáncer ER-positivo/HER2-positivo; sin resultados maduros aún |
| [NCT04460430](https://clinicaltrials.gov/study/NCT04460430) | Fase 2 | Terminado | 12 | Neratinib en cáncer HR-positivo/HER2-negativo HER2-enriquecido; terminado prematuramente por reclutamiento insuficiente |
| [NCT06131424](https://clinicaltrials.gov/study/NCT06131424) | N/A | Completado | 1151 | Estudio retrospectivo de prevalencia de HER2-low en cáncer de mama metastásico HER2-negativo; no evalúa eficacia de neratinib |
| [NCT05599334](https://clinicaltrials.gov/study/NCT05599334) | N/A | Completado | 111 | Estudio observacional (Programa de Acceso Temprano europeo) describiendo perfiles clínicos de pacientes HER2+ con neratinib adyuvante extendido |
| [NCT04901299](https://clinicaltrials.gov/study/NCT04901299) | Fase 2 | Retirado | 0 | Diseñado para evaluar neratinib + fulvestrant en cáncer HR-positivo/HER2-negativo metastásico; retirado sin inscripción |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [26874901](https://pubmed.ncbi.nlm.nih.gov/26874901/) | 2016 | ECA (Fase 3) | Lancet Oncol | ExteNET: neratinib 12 meses tras terapia adyuvante con trastuzumab en cáncer de mama HER2+ temprano; subgrupo HR+ mostró mayor beneficio |
| [27406346](https://pubmed.ncbi.nlm.nih.gov/27406346/) | 2016 | ECA | N Engl J Med | I-SPY2: ensayo adaptativo Fase 2 de neratinib neoadyuvante en cáncer de mama de alto riesgo |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Revisión/Guía | J Clin Oncol | Actualización de la guía ASCO sobre terapia sistémica en cáncer de mama HER2+ avanzado |
| [29784737](https://pubmed.ncbi.nlm.nih.gov/29784737/) | 2018 | Revisión/Guía | J Natl Compr Canc Netw | Actualización de las guías NCCN de cáncer de mama |
| [39153126](https://pubmed.ncbi.nlm.nih.gov/39153126/) | 2024 | Cohorte | Breast Cancer Res Treat | Patrones de uso y tolerancia de neratinib adyuvante en cáncer HR+/HER2+ temprano; toxicidad GI limita continuidad |
| [33726508](https://pubmed.ncbi.nlm.nih.gov/33726508/) | 2021 | Revisión | Future Oncol | Tendencias actuales en el tratamiento del cáncer HR+/HER2+ |
| [32139271](https://pubmed.ncbi.nlm.nih.gov/32139271/) | 2020 | Revisión | Clin Breast Cancer | Mesa redonda de expertos (BCTEG) sobre desarrollo clínico en cáncer HER2+ |
| [35251981](https://pubmed.ncbi.nlm.nih.gov/35251981/) | 2022 | Reporte de caso | Front Oncol | Caso de enfermedad leptomeníngea en cáncer HER2+ (RE-/RP-) tratado con pirotinib/vinorelbina; relevancia indirecta |
| [32782013](https://pubmed.ncbi.nlm.nih.gov/32782013/) | 2020 | Cohorte/Genómico | Breast Cancer Res | Mutaciones de ERBB2 como marcador pronóstico adverso en carcinoma lobulillar RE-positivo |
| [24892840](https://pubmed.ncbi.nlm.nih.gov/24892840/) | 2013 | Revisión | Clin Adv Hematol Oncol | Panorama del tratamiento del cáncer de mama metastásico por subtipo inmunohistoquímico |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina-quinasa HER1/HER2/HER4) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto (sin datos estructurados; la literatura documenta toxicidad gastrointestinal significativa —diarrea— como efecto adverso limitante, no mielosupresión) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe respaldo mecanístico sólido (HER2 y receptores hormonales frecuentemente coexisten) y evidencia Fase 3 robusta en la población HER2+ relacionada (ExteNET), pero la evidencia específica para PR-positivo depende de un único ensayo Fase 2 aún en reclutamiento (NCT04886531), con otros estudios relacionados retirados o terminados prematuramente — de ahí el nivel L2 y la recomendación de avanzar con salvaguardas en lugar de "Go" directo.

**Para avanzar se necesita:**
- Resolver la brecha bloqueante DG001 (advertencias/contraindicaciones del prospecto TFDA/AEMPS)
- Datos estructurados de MOA (DG002) confirmados vía DrugBank/ficha técnica oficial
- Resultados maduros del ensayo NCT04886531 (reclutando) estratificados por estado de receptor de progesterona
- Datos de interacciones farmacológicas (DDI) y perfil de toxicidad (actualmente "not_found")
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

