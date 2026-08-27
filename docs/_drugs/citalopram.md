---
layout: default
title: Citalopram
parent: 僅模型預測 (L5)
nav_order: 72
evidence_level: L5
indication_count: 5
---

# Citalopram
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

Usando el Evidence Pack proporcionado, genero el informe centrado en la indicación predicha de mayor rango (TOC, la única con evidencia y decisión distinta de "Hold").

# Citalopram: De Depresión (Trastorno Depresivo Mayor) a Trastorno Obsesivo-Compulsivo (TOC)

## Resumen en Una Frase

Citalopram es un inhibidor selectivo de la recaptación de serotonina (ISRS), utilizado clásicamente para el tratamiento de la depresión.
El modelo TxGNN predice que podría ser efectivo para el **Trastorno Obsesivo-Compulsivo (TOC)**,
con **30 ensayos clínicos** y **16 publicaciones** que actualmente respaldan esta dirección, aunque la mayor parte de la evidencia clínica directa proviene de escitalopram, su enantiómero activo (mecanismo farmacológico idéntico).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Depresión (Trastorno Depresivo Mayor) — no hay registro regulatorio local que lo confirme (0 autorizaciones) |
| Nueva Indicación Predicha | Trastorno Obsesivo-Compulsivo (TOC) |
| Puntaje de Predicción TxGNN | 99.74% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción específico en esta base de evidencia. Según la información farmacológica conocida, citalopram pertenece a la clase de los inhibidores selectivos de la recaptación de serotonina (ISRS), cuya eficacia en el tratamiento de la depresión está ampliamente comprobada, y mecanísticamente podría ser aplicable al TOC.

La desregulación del sistema serotoninérgico es el mecanismo patológico central reconocido en el TOC, y los ISRS/clomipramina son el tratamiento de primera línea según las guías clínicas de esta patología. Citalopram comparte esta clase de mecanismo, y su enantiómero activo, escitalopram (mecanismo farmacológico idéntico), ya cuenta con múltiples ensayos controlados aleatorizados de Fase 4 que validan su eficacia en TOC — lo que refuerza indirectamente la plausibilidad de la predicción de TxGNN para citalopram.

Como advertencia relevante: la prolongación del intervalo QTc a dosis altas es un riesgo de seguridad ya conocido para citalopram, por lo que cualquier avance hacia esta indicación debe incorporar límites de dosis como medida de protección (guardrail).

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00116532](https://clinicaltrials.gov/study/NCT00116532) | Fase 4 | Completado | 30 | Evaluación de escitalopram (enantiómero activo de citalopram) en TOC y determinación de dosis óptima |
| [NCT05210140](https://clinicaltrials.gov/study/NCT05210140) | N/A | Desconocido | 148 | Monitorización de niveles plasmáticos y genotipado CYP2C19 para personalizar dosis de escitalopram; misma vía metabólica que citalopram |
| [NCT00564564](https://clinicaltrials.gov/study/NCT00564564) | Fase 4 | Completado | 21 | Aumento con quetiapina vs. clomipramina en pacientes con TOC refractarios a ISRS |
| [NCT00456937](https://clinicaltrials.gov/study/NCT00456937) | Fase 4 | Completado | 15 | Estudio abierto de escitalopram (hasta 20 mg/día) en esquizofrenia con TOC comórbido |
| [NCT03068429](https://clinicaltrials.gov/study/NCT03068429) | Fase 4 | Completado | 69 | Neuroimagen (fMRI) de condicionamiento/extinción del miedo en TOC, pre y post tratamiento con sertralina |
| [NCT02431845](https://clinicaltrials.gov/study/NCT02431845) | N/A | Reclutando | 200 | Estudio farmacogenético/proteómico/microbiómico en TOC para predecir respuesta a ISRS |
| [NCT00723060](https://clinicaltrials.gov/study/NCT00723060) | Fase 4 | Completado | 176 | ECA doble ciego multicéntrico: dosis convencional (20mg) vs. alta dosis (40mg) de escitalopram en TOC |
| [NCT00305500](https://clinicaltrials.gov/study/NCT00305500) | Fase 3 | Completado | 100 | Estudio abierto: escitalopram en dosis altas (20-50mg/día) en TOC del adulto |
| [NCT00215137](https://clinicaltrials.gov/study/NCT00215137) | Fase 2 | Completado | 14 | Estudio piloto de seguridad y eficacia de escitalopram en TOC |
| [NCT02022709](https://clinicaltrials.gov/study/NCT02022709) | Fase 4 | Completado | 78 | Comparación de eficacia entre ERP, ISRS y combinación de ambos en TOC |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10471169](https://pubmed.ncbi.nlm.nih.gov/10471169/) | 1999 | Cohorte/Abierto | Int Clin Psychopharmacol | Evidencia histórica de la eficacia de **citalopram específicamente** en TOC, más allá de la depresión |
| [10572334](https://pubmed.ncbi.nlm.nih.gov/10572334/) | 1999 | Cohorte/Abierto | Eur Psychiatry | Ensayo abierto de 90 días: citalopram solo vs. citalopram + clomipramina en TOC resistente al tratamiento (n=16) |
| [38703743](https://pubmed.ncbi.nlm.nih.gov/38703743/) | 2024 | Revisión | Compr Psychiatry | Seguridad y tolerabilidad a largo plazo de dosis altas off-label de ISRS en TOC |
| [35121274](https://pubmed.ncbi.nlm.nih.gov/35121274/) | 2022 | Meta-análisis en red | J Psychiatr Res | Comparación de tratamiento farmacológico y psicológico en TOC pediátrico/adolescente |
| [35818708](https://pubmed.ncbi.nlm.nih.gov/35818708/) | 2022 | Revisión sistemática | Expert Opin Pharmacother | ECAs de farmacoterapia en trastorno de personalidad obsesivo-compulsiva |
| [32242450](https://pubmed.ncbi.nlm.nih.gov/32242450/) | 2020 | Revisión sistemática | Nord J Psychiatry | Eficacia y tolerabilidad de fluoxetina en TOC infantojuvenil |
| [34313207](https://pubmed.ncbi.nlm.nih.gov/34313207/) | 2022 | Estudio farmacogenético | CNS Spectr | Impacto del polimorfismo BDNF Val66Met en la respuesta a escitalopram/paroxetina en TOC |
| [30973183](https://pubmed.ncbi.nlm.nih.gov/30973183/) | 2019 | Estudio de neuroimagen | Psychiatry Clin Neurosci | Cambios neuroquímicos (1H-MRS) tras 12 semanas de escitalopram en TOC |
| [41286906](https://pubmed.ncbi.nlm.nih.gov/41286906/) | 2025 | Protocolo ECA | BMC Psychiatry | Protocolo de ECA doble ciego con placebo: vortioxetina como terapia adyuvante en TOC |
| [22305974](https://pubmed.ncbi.nlm.nih.gov/22305974/) | 2012 | Revisión | BMJ Clin Evid | Panorama general de epidemiología y tratamiento del TOC |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No hay datos de advertencias, contraindicaciones ni interacciones farmacológicas disponibles en las fuentes consultadas (búsqueda DDI: sin resultados).

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen múltiples ECAs de Fase 2-4 que respaldan la eficacia de escitalopram (enantiómero activo, mecanismo idéntico a citalopram) en TOC, y dos estudios de cohorte/abiertos históricos evalúan citalopram directamente en esta indicación. La evidencia es razonable pero no suficientemente robusta para un "Go" directo, y el riesgo conocido de prolongación de QTc a dosis altas exige medidas de protección específicas.

**Para avanzar se necesita:**
- Datos de advertencias/contraindicaciones del prospecto TFDA (gap bloqueante DG001)
- Datos detallados del mecanismo de acción (MOA) de citalopram (gap DG002)
- Confirmación del estado regulatorio, dado que el fármaco figura como no comercializado (0 autorizaciones)
- Evidencia clínica directa con citalopram (no solo escitalopram) específicamente en TOC
- Plan de monitoreo de QTc y protocolo de límite de dosis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

