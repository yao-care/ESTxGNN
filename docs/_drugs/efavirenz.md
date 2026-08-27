---
layout: default
title: Efavirenz
parent: 僅模型預測 (L5)
nav_order: 100
evidence_level: L5
indication_count: 3
---

# Efavirenz
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

# Efavirenz: De Infección por VIH-1 a Infección por Virus de Inmunodeficiencia de Simios

## Resumen en Una Frase

Efavirenz es un inhibidor no nucleosídico de la transcriptasa reversa (NNRTI), utilizado originalmente en el tratamiento de la infección por VIH-1.
El modelo TxGNN predice que podría ser relevante para la **infección por virus de inmunodeficiencia de simios (SIV)**,
con **1 ensayo clínico** y **16 publicaciones** identificadas, aunque de relevancia clínica limitada (ver más abajo).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección por VIH-1 (terapia antirretroviral) |
| Nueva Indicación Predicha | Infección por virus de inmunodeficiencia de simios (SIV) |
| Puntaje de Predicción TxGNN | 99.80% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

No se dispone de una ficha estructurada del mecanismo de acción (MOA) de efavirenz en esta base. Sin embargo, la evidencia clínica revisada confirma que efavirenz es un **NNRTI** que inhibe directamente la transcriptasa reversa del VIH-1; su eficacia en la infección por VIH-1 está firmemente establecida (el ensayo NCT01263015 lo sitúa como componente del régimen de referencia Atripla®, en combinación con emtricitabina/tenofovir).

La "infección por SIV" **no es una enfermedad humana**, sino un modelo animal (virus de inmunodeficiencia de simios en macacos) empleado por investigadores para estudiar fármacos anti-VIH. El vínculo mecanístico identificado es que los investigadores han desarrollado quimeras virales SIV/SHIV (en las que la transcriptasa reversa nativa de SIV se sustituye por la del VIH-1, dando lugar al llamado "RT-SHIV"), precisamente para poder ensayar NNRTIs como efavirenz —que de otro modo no tienen actividad frente a la transcriptasa reversa nativa de SIV—.

En consecuencia, aunque el puntaje de TxGNN es muy alto (99.80%), la señal refleja el uso de efavirenz como **herramienta de investigación** en un modelo animal (misma diana enzimática), y no una indicación clínica nueva y viable en humanos.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | No aplica | Retirado | 0 | Estudio sobre cinética de decaimiento del VIH con el inhibidor de integrasa **raltegravir** (no efavirenz); retirado sin inscripción, sin evidencia utilizable. |

**Nota:** este ensayo fue calificado con relevancia grado C ("el fármaco del estudio es raltegravir, no efavirenz; estado RETIRADO, inscripción=0, sin evidencia disponible") — no aporta soporte real a la predicción.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15328115](https://pubmed.ncbi.nlm.nih.gov/15328115/) | 2004 | Estudio en animales | Antimicrob Agents Chemother | Evaluó la actividad de efavirenz en macacos infectados con la quimera RT-SHIV, validando su uso en este modelo animal. |
| [19889213](https://pubmed.ncbi.nlm.nih.gov/19889213/) | 2009 | Estudio en animales | Retrovirology | Macacos RT-SHIV tratados con monoterapia corta de efavirenz seguida de terapia combinada; análisis de dinámica de subpoblaciones virales resistentes. |
| [15919889](https://pubmed.ncbi.nlm.nih.gov/15919889/) | 2005 | Estudio en animales | J Virol | Siete macacos RT-SHIV tratados con efavirenz (200 mg/día) + lamivudina + tenofovir mostraron supresión significativa de la carga viral. |
| [21084490](https://pubmed.ncbi.nlm.nih.gov/21084490/) | 2011 | Estudio en animales | J Virol | Analiza la diversidad genética viral tras terapia antirretroviral (incluida monoterapia inicial con efavirenz) en macacos RT-SHIV. |
| [22933296](https://pubmed.ncbi.nlm.nih.gov/22933296/) | 2012 | Estudio en animales/in vitro | J Virol | Detección de variantes de resistencia preexistentes mediante PCR ultrasensible en macacos infectados con RT-SHIV. |
| [15564466](https://pubmed.ncbi.nlm.nih.gov/15564466/) | 2004 | Estudio in vitro | J Virol | Caracteriza la quimera SHIV-VIH, desarrollada específicamente para permitir el estudio de resistencia a NNRTIs (como efavirenz) en macacos. |
| [24777106](https://pubmed.ncbi.nlm.nih.gov/24777106/) | 2014 | Estudio en animales | Antimicrob Agents Chemother | Evalúa regímenes antirretrovirales potenciados (4-5 fármacos) sobre la cinética de decaimiento viral en el modelo RT-SHIV. |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | Estudio in vitro | Antivir Ther | Evalúa la actividad antiviral de 16 fármacos aprobados frente a cepas de VIH-2, SIV y SHIV. |
| [20668516](https://pubmed.ncbi.nlm.nih.gov/20668516/) | 2010 | Estudio en animales | PLoS One | Caracteriza la cinética de decaimiento viral bajo HAART en el modelo de macacos RT-SHIV. |
| [26559632](https://pubmed.ncbi.nlm.nih.gov/26559632/) | 2015 | Estudio en animales | Retrovirology | Analiza poblaciones virales en plasma y tejido de macacos RT-SHIV bajo terapia antirretroviral. |

**Nota:** las 16 publicaciones identificadas son, sin excepción, estudios preclínicos (animales o in vitro); no existe ningún ECA ni estudio observacional en humanos.

## Información de Mercado en España

Efavirenz no cuenta actualmente con autorizaciones de comercialización registradas en España (0 licencias; estado: No comercializado).

## Consideraciones de Seguridad

Consulte el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia disponible es de nivel L4: no existe ningún ensayo clínico en humanos relevante para efavirenz en esta indicación, solo estudios preclínicos donde el fármaco se emplea como herramienta de investigación en un modelo animal (RT-SHIV), no como tratamiento dirigido a una enfermedad humana. Además, la "infección por SIV" no es una enfermedad humana, por lo que no constituye un objetivo de reposicionamiento clínicamente viable en su forma actual.

**Para avanzar se necesita:**
- Ficha técnica completa con mecanismo de acción (MOA) verificado (brecha de datos DG002)
- Advertencias, contraindicaciones y prospecto oficial (brecha de datos bloqueante DG001, impide evaluación de seguridad S1)
- Reevaluar si el modelo TxGNN debe filtrar indicaciones no humanas antes de puntuar: las otras dos indicaciones predichas para este fármaco en esta ficha son un síndrome veterinario (inmunodeficiencia felina) y un síndrome pediátrico raro sin ningún vínculo mecanístico ni evidencia (0 ensayos, 0 literatura) — ninguna es candidata viable
- Datos de autorización de comercialización en España, actualmente inexistentes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

