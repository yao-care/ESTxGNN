---
layout: default
title: Trastuzumab
parent: 僅模型預測 (L5)
nav_order: 283
evidence_level: L5
indication_count: 10
---

# Trastuzumab
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

# TRASTUZUMAB: De Cáncer de Mama HER2 Positivo a Subtipo "Normal-Like" de Carcinoma de Mama

## Resumen en Una Frase

Trastuzumab es un anticuerpo monoclonal anti-HER2/ERBB2, utilizado originalmente en el cáncer de mama con sobreexpresión/amplificación de HER2. El modelo TxGNN predice que podría ser efectivo para el subtipo molecular "normal-like" (normal breast-like) de carcinoma de mama, con **12 ensayos clínicos** y **1 publicación** que actualmente respaldan esta dirección, aunque la evidencia disponible es de carácter exploratorio y no concluyente.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de mama HER2 positivo (sobreexpresión/amplificación de HER2) |
| Nueva Indicación Predicha | Subtipo "Normal-like" de carcinoma de mama |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Los datos detallados del mecanismo de acción (MOA) de trastuzumab están marcados como brecha de información en este Evidence Pack (severidad "High", ítem DG002). Según la información disponible en el propio paquete de evidencia, trastuzumab es un anticuerpo monoclonal dirigido contra HER2/ERBB2, cuya indicación central son los tumores de mama con sobreexpresión o amplificación de HER2.

El subtipo "normal-like" es una categoría molecular intrínseca (clasificación PAM50) caracterizada típicamente por baja proliferación celular y expresión de HER2 generalmente baja o ausente. Esto plantea una **discordancia mecanística potencial** con el objetivo terapéutico de trastuzumab, que depende de la sobreexpresión de HER2 en la célula tumoral. Los ensayos clínicos identificados abordan mayormente poblaciones "HER2 no amplificado" o "PAM50 no-luminal", explorando si estos subgrupos podrían aun así beneficiarse de terapia anti-HER2, pero sin evidencia concluyente hasta la fecha.

Por lo tanto, la señal de TxGNN en este caso parece reflejar una asociación de red (proximidad en el grafo de conocimiento) más que un mecanismo biológico validado, lo que justifica un nivel de evidencia L3 y una recomendación de "pregunta de investigación" en esta etapa.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04759248](https://clinicaltrials.gov/study/NCT04759248) | Fase 2 | Activo, no reclutando | 55 | Atezolizumab + trastuzumab + vinorelbina en cáncer de mama HER2+ avanzado, ER-negativo o PAM50 no-luminal (grado B, relevancia parcial al subtipo) |
| [NCT01670877](https://clinicaltrials.gov/study/NCT01670877) | Fase 2 | Completado | 56 | Neratinib solo y combinado con fulvestrant en cáncer de mama HER2 no amplificado pero HER2 mutado (grado B) |
| [NCT01796197](https://clinicaltrials.gov/study/NCT01796197) | Fase 2 | Completado | 23 | Paclitaxel + trastuzumab + pertuzumab en cáncer de mama inflamatorio preoperatorio (grado C, población HER2+ general) |
| [NCT06328387](https://clinicaltrials.gov/study/NCT06328387) | Fase 1/2 | Desconocido | 120 | Hidroxicloroquina + ADC (T-DXd/SG) vs. ADC solo en cáncer de mama avanzado |
| [NCT05582499](https://clinicaltrials.gov/study/NCT05582499) | Fase 2 | Reclutando | 716 | Plataforma de terapia neoadyuvante de precisión según subtipo clínico/molecular (FASCINATE-N) |
| [NCT06348134](https://clinicaltrials.gov/study/NCT06348134) | Fase 2 | Reclutando | 74 | Terapia anti-HER2 neoadyuvante/adyuvante óptima en mujeres nigerianas con cáncer de mama HER2+ |
| [NCT03168880](https://clinicaltrials.gov/study/NCT03168880) | Fase 3 | Activo, no reclutando | 720 | Paclitaxel semanal ± carboplatino en cáncer de mama triple negativo (perfil molecular "basal-like", relacionado indirectamente) |
| [NCT04329065](https://clinicaltrials.gov/study/NCT04329065) | Fase 2 | Reclutando | 25 | Vacuna WOKVAC + quimioterapia neoadyuvante + trastuzumab en cáncer de mama |
| [NCT05659056](https://clinicaltrials.gov/study/NCT05659056) | Fase 2 | Reclutando | 65 | Pirotinib + trastuzumab + abraxane en cáncer de mama HER2-enriched temprano/localmente avanzado |
| [NCT04750122](https://clinicaltrials.gov/study/NCT04750122) | Fase 1/2 | Reclutando | 46 | Terapia neoadyuvante guiada por cribado de fármacos in vitro en pacientes HER2 positivo |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [19466513](https://pubmed.ncbi.nlm.nih.gov/19466513/) | 2009 | Estudio patológico (no terapéutico) | Breast Cancer (Tokyo, Japan) | Caracteriza rasgos morfológicos y citopatológicos del subtipo "basal-like" en comparación con otros subtipos moleculares (incluyendo "normal-like"); no evalúa eficacia terapéutica de trastuzumab |

---

## Información de Mercado en España

Actualmente no hay autorizaciones de comercialización registradas en España para este fármaco (estado de mercado: no comercializado).

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (anticuerpo monoclonal anti-HER2/ERBB2) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia para "normal-like" es de nivel L3 (estudios exploratorios/observacionales indirectos), con solo 1 publicación no terapéutica y ningún ensayo diseñado específicamente para este subtipo. El propio análisis mecanístico señala una discordancia potencial entre la biología del subtipo (HER2 típicamente bajo) y el mecanismo de acción de trastuzumab (dependiente de sobreexpresión de HER2).

**Para avanzar se necesita:**
- Confirmación del estado real de HER2 (IHC/FISH) en la población "normal-like" candidata a tratamiento
- Datos del prospecto/ficha técnica de la Agencia Española de Medicamentos (AEMPS), actualmente marcados como brecha bloqueante (DG001)
- Documentación completa del mecanismo de acción (DG002)
- Nota: dentro del mismo Evidence Pack, las indicaciones predichas de rango 2 y 3 ("cáncer de mama PR-positivo" y "PR-negativo", ambas dentro de la población HER2+) presentan evidencia de nivel L1 con recomendación "Proceed with Guardrails" y podrían justificar una evaluación separada y prioritaria
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

