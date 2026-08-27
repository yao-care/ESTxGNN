---
layout: default
title: Saquinavir
parent: 僅模型預測 (L5)
nav_order: 253
evidence_level: L5
indication_count: 6
---

# Saquinavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Usando el Evidence Pack proporcionado (candidato multi-indicación `TW-DB01232-multi`), genero el informe. Como el pack contiene 5 indicaciones predichas con calidad de evidencia muy dispar, adapto la plantilla de una sola indicación a un panel de candidatos, manteniendo cada sección exigida.

# Saquinavir: Panel Multi-Indicación — De VIH-1 a Nuevas Señales de Reposicionamiento

## Resumen en Una Frase

Saquinavir es un inhibidor de la proteasa del VIH-1, originalmente desarrollado para el tratamiento antirretroviral de la infección por VIH.
El modelo TxGNN generó 5 señales de reposicionamiento para este fármaco, pero **ninguna representa una indicación terapéutica nueva y bien respaldada**: las dos únicas señales con evidencia clínica sólida (**infección congénita por VIH** y **AIDS related complex**) son en realidad extensiones de su indicación ya conocida, mientras que las 3 señales restantes carecen de cualquier respaldo clínico o de literatura.

---

## Resumen Rápido (Panel de Candidatos)

| Rango | Indicación Predicha | Puntaje TxGNN | Nivel de Evidencia | Etapa de Decisión | Recomendación |
|------|------|------|------|------|------|
| 1 | Feline acquired immunodeficiency syndrome (enfermedad veterinaria) | 99.97% | L5 | S0 | Hold |
| 2 | Simian immunodeficiency virus infection (modelo animal, no humano) | 99.97% | L3 | S1 | Hold |
| 3 | Trastorno neurodesarrollo raro (ataxia, ausencia de habla) | 99.97% | L5 | S0 | Hold |
| 4 | Hiperlipidemia combinada familiar (obsoleta; dirección mecanística contraria) | 99.59% | L5 | S0 | Hold |
| 5 | Infección congénita por VIH (pediatría/perinatal) | 99.47% | L1 | S3 | Proceed with Guardrails |
| 6 | AIDS related complex (estadio sintomático histórico del VIH) | 99.47% | L1 | S3 | Proceed with Guardrails |

| Item | Contenido |
|------|------|
| Indicación Original | Infección por VIH-1 (terapia antirretroviral) — no consta ficha técnica en España |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada (global) | **Hold** — no se identifica una indicación nueva genuina con evidencia suficiente |

---

## Por qué son Razonables (o no) estas Predicciones?

El campo `original_moa` del fármaco está marcado como dato faltante, pero la evidencia asociada a los propios candidatos describe el mecanismo: saquinavir es un **inhibidor de la proteasa del VIH-1**, que bloquea la escisión de la poliproteína gag-pol e impide la maduración de nuevas partículas virales infecciosas.

De las 6 señales generadas, solo dos (rangos 5 y 6) son mecanísticamente coherentes y están respaldadas por ensayos clínicos reales — pero ambas corresponden al **mismo mecanismo ya aprobado** (inhibición de proteasa del VIH) aplicado a subpoblaciones o nomenclaturas históricas de la misma enfermedad (VIH pediátrico/congénito, y "AIDS related complex", la denominación CDC de los años 90 para la enfermedad sintomática por VIH). No constituyen una hipótesis de reposicionamiento nueva.

Las otras 4 señales (rangos 1–4) no tienen justificación mecanística sólida: la proteasa del virus de inmunodeficiencia felina (FIV) difiere estructuralmente de la del VIH-1; la infección por SIV es un modelo en primates no humanos sin población clínica humana; el trastorno neurodesarrollo raro no tiene vínculo fisiopatológico conocido con la inhibición de proteasa viral; y la hiperlipidemia representa una **relación mecanística inversa** (los inhibidores de proteasa del VIH son causantes conocidos de dislipidemia, no tratamiento).

---

## Análisis por Candidato

### Rango 5 — Infección Congénita por VIH (L1, Proceed with Guardrails)

**Racional:** Extensión del mecanismo ya aprobado (inhibición de proteasa del VIH-1) a la validación de dosis/seguridad en lactantes y prevención de transmisión vertical madre-hijo. No es una hipótesis de reposicionamiento nueva.

**Evidencia de Ensayos Clínicos**

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00623597](https://clinicaltrials.gov/study/NCT00623597) | Fase 1/2 | Completado | 18 | Farmacocinética y seguridad de saquinavir + ritonavir en lactantes/niños VIH+ (4 meses–6 años) |
| [NCT00035932](https://clinicaltrials.gov/study/NCT00035932) | Fase 3 | Completado | 571 | Atazanavir + ritonavir o saquinavir + tenofovir en VIH (saquinavir como comparador) |
| [NCT02951052](https://clinicaltrials.gov/study/NCT02951052) | Fase 3 | Activo, no reclutando | 618 | Cambio a cabotegravir/rilpivirina LA desde régimen basado en IP (incluye saquinavir como régimen previo) |
| [NCT00197145](https://clinicaltrials.gov/study/NCT00197145) | Fase 3 | Terminado | 24 | Antagonista CCR5 + ritonavir vs. placebo en pacientes con experiencia en tratamiento |
| [NCT02429791](https://clinicaltrials.gov/study/NCT02429791) | Fase 3 | Completado | 510 | Cambio a dolutegravir + rilpivirina desde régimen basado en IP/INI/NNRTI |
| [NCT03299049](https://clinicaltrials.gov/study/NCT03299049) | Fase 3b | Activo, no reclutando | 1049 | Cabotegravir + rilpivirina LA cada 8 vs. 4 semanas |
| [NCT02938520](https://clinicaltrials.gov/study/NCT02938520) | Fase 3 | Activo, no reclutando | 631 | Cabotegravir + rilpivirina LA de mantenimiento tras régimen de comprimido único |
| [NCT02422797](https://clinicaltrials.gov/study/NCT02422797) | Fase 3 | Completado | 518 | Cambio a dolutegravir + rilpivirina desde régimen basado en IP/INI/NNRTI |
| [NCT01641809](https://clinicaltrials.gov/study/NCT01641809) | Fase 2b | Completado | 244 | GSK1265744 (cabotegravir) en inducción de supresión virológica, naive a tratamiento |

**Evidencia de Literatura**

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27242802](https://pubmed.ncbi.nlm.nih.gov/27242802/) | 2016 | Cohorte | Frontiers in Immunology | Estudio SMARTT/PHACS: seguridad de exposición in utero a antirretrovirales en >3,500 niños |
| [22938775](https://pubmed.ncbi.nlm.nih.gov/22938775/) | 2012 | Cohorte | Médecine et Maladies Infectieuses | Eficacia y seguridad de saquinavir/ritonavir en embarazadas VIH+ (cohorte INEMA) |

### Rango 6 — AIDS Related Complex (L1, Proceed with Guardrails)

**Racional:** "AIDS related complex" es la denominación histórica CDC (años 90) para la enfermedad sintomática por VIH; los ensayos pivotales originales de saquinavir (entonces Ro 31-8959) usaron esta nomenclatura. Es la indicación ya aprobada bajo un nombre antiguo, no una hipótesis nueva.

**Evidencia de Ensayos Clínicos**

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00002111](https://clinicaltrials.gov/study/NCT00002111) | Fase 1 | Completado | 32 | Escalada de dosis de Ro 31-8959 (saquinavir) en enfermedad por VIH |
| [NCT00001040](https://clinicaltrials.gov/study/NCT00001040) | Fase 2 | Completado | 300 | Ro 31-8959 + AZT vs. AZT + ddC vs. triple combinación |
| [NCT00000848](https://clinicaltrials.gov/study/NCT00000848) | Fase 2 | Completado | 144 | Cambio de cápsula dura a cápsula blanda de saquinavir vs. indinavir |
| [NCT00002333](https://clinicaltrials.gov/study/NCT00002333) | Fase 2 | Completado | 900 | Ro 31-8959 solo, ddC solo, y combinación, en VIH avanzado |
| [NCT00002334](https://clinicaltrials.gov/study/NCT00002334) | Fase 3 | Completado | 3000 | AZT solo vs. AZT+ddC vs. AZT+saquinavir vs. triple combinación |
| [NCT00002162](https://clinicaltrials.gov/study/NCT00002162) | Fase 2 | Completado | 140 | Dos formulaciones de saquinavir combinadas con otros antirretrovirales |
| [NCT00035932](https://clinicaltrials.gov/study/NCT00035932) | Fase 3 | Completado | 571 | Atazanavir + ritonavir o saquinavir + tenofovir en VIH |
| [NCT00002347](https://clinicaltrials.gov/study/NCT00002347) | Fase 2 | Completado | 225 | AZT/ddC + nevirapina o saquinavir (Invirase) en combinación |

**Evidencia de Literatura**

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [26944096](https://pubmed.ncbi.nlm.nih.gov/26944096/) | 2016 | Revisión | Advanced Drug Delivery Reviews | Nanotecnología para superar la barrera hematoencefálica en NeuroAIDS |
| [19290032](https://pubmed.ncbi.nlm.nih.gov/19290032/) | 2009 | Cohorte | AIDS Reviews | Factores de riesgo de eventos adversos gastrointestinales en pacientes VIH tratados |
| [32694416](https://pubmed.ncbi.nlm.nih.gov/32694416/) | 2020 | Estudio PK | AIDS (London) | Concentraciones de zidovudina/lamivudina en LCR ventricular vs. lumbar |
| [18256206](https://pubmed.ncbi.nlm.nih.gov/18256206/) | 2008 | Mecanístico/PK | Drug Metab Dispos | Rol de P-gp, MRP2 y CYP3A en la absorción oral de saquinavir (rata) |
| [15925431](https://pubmed.ncbi.nlm.nih.gov/15925431/) | 2005 | Reporte de caso | Rev Med Interne | Trombosis de vena porta en pacientes VIH+ (4 casos) |

### Rango 2 — Simian Immunodeficiency Virus Infection (L3, Hold)

Existe cierta base experimental: la proteasa del SIV comparte alta homología estructural con la del VIH-1, y saquinavir muestra actividad inhibitoria in vitro contra cepas de SIV. Sin embargo, esta es una **enfermedad de modelo animal (primates no humanos)**, no una indicación clínica humana, por lo que no tiene vía de desarrollo clínico. Sin ensayos clínicos registrados.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | In vitro | Antimicrob Agents Chemother | Saquinavir inhibe SIVmac239 (EC50 55±3 nM), comparable a inhibición de VIH-1 |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro | Antiviral Therapy | Susceptibilidad de HIV-2, SIV y SHIV a 16 antirretrovirales aprobados |
| [20497048](https://pubmed.ncbi.nlm.nih.gov/20497048/) | 2010 | Modelo animal | J Infect Dis | HAART reduce replicación viral e inflamación en SNC en macacos con SIV |
| [16809296](https://pubmed.ncbi.nlm.nih.gov/16809296/) | 2006 | Estructural | J Virol | Rol del residuo Thr80 invariante en la estructura/función de la proteasa del VIH-1 |

### Rangos 1, 3 y 4 — Señales Descartadas (L5, Hold)

Estas tres señales no cuentan con ningún ensayo clínico ni publicación de respaldo (búsquedas en ClinicalTrials.gov, ICTRP y PubMed con resultado cero), y se consideran ruido de similitud del embedding de TxGNN:

- **Feline acquired immunodeficiency syndrome**: la proteasa del FIV difiere estructuralmente de la del VIH-1; la literatura muestra pobre inhibición de la proteasa de FIV por inhibidores de proteasa del VIH.
- **Trastorno del neurodesarrollo raro** (ataxia, ausencia de habla, sustancia blanca reducida): enfermedad genética sin vínculo fisiopatológico conocido con la vía viral.
- **Hiperlipidemia combinada familiar (obsoleta)**: dirección mecanística contraria — los inhibidores de proteasa del VIH son causa conocida de dislipidemia, no tratamiento; además la categoría diagnóstica está marcada como obsoleta.

---

## Información de Mercado en España

Saquinavir **no está comercializado en España** (`market_status: 未上市`, 0 autorizaciones registradas). No hay ficha técnica local disponible para confirmar indicación aprobada, posología ni advertencias específicas del mercado español.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

*(No hay datos de advertencias, contraindicaciones ni interacciones farmacológicas disponibles en las fuentes consultadas; TFDA marca esta brecha como bloqueante para la evaluación de seguridad — ver Conclusión.)*

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ninguna de las 6 señales generadas por TxGNN constituye una oportunidad de reposicionamiento nueva y accionable. Las dos señales con evidencia de Nivel 1 (infección congénita por VIH, AIDS related complex) son extensiones o nomenclatura histórica de la indicación ya conocida del fármaco (inhibición de proteasa del VIH-1), no una hipótesis nueva. Las cuatro señales restantes carecen de evidencia clínica/de literatura suficiente o presentan una relación mecanística contradictoria. Además, el fármaco no está comercializado en España, y falta información de seguridad crítica (TFDA) para siquiera iniciar una evaluación S1.

**Para avanzar se necesitaría:**
- Resolver DG001 (bloqueante): obtener el prospecto/ficha técnica de TFDA con advertencias y contraindicaciones
- Resolver DG002: confirmar el mecanismo de acción vía API de DrugBank
- Si se desea explorar el candidato SIV (rango 2) con fines de investigación básica, definir explícitamente que es un modelo preclínico en primates, no una vía de desarrollo clínico humano
- Reevaluar el pipeline TxGNN para este fármaco: las 3 señales de Nivel 5 sugieren ruido en el espacio de embeddings más que verdaderas hipótesis de reposicionamiento
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

