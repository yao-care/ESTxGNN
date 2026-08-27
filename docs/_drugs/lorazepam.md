---
layout: default
title: Lorazepam
parent: 僅模型預測 (L5)
nav_order: 171
evidence_level: L5
indication_count: 10
---

# Lorazepam
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

# Lorazepam: De Ansiedad/Sedación a Insomnio

> **Nota metodológica:** El Evidence Pack incluye 10 indicaciones predichas por TxGNN. La de mayor puntaje (*trigeminal nerve neoplasm*, 99.87%) está marcada explícitamente en los datos como probable falso positivo del modelo (sin ensayos, sin literatura, sin plausibilidad mecanística) y su propia ficha recomienda **Hold**. Por eso este informe se centra en la indicación con mejor respaldo real de evidencia: **Insomnio** (rango 2, 99.80%, nivel L2). Las demás indicaciones predichas (crisis epilépticas reflejas de diversos subtipos, etc.) quedan en fase de investigación exploratoria (L3-L5, Hold/Research Question) y no se desarrollan en detalle aquí.

---

## Resumen en Una Frase

Lorazepam es una benzodiazepina de uso clásico como ansiolítico y sedante de acción corta-intermedia. El modelo TxGNN predice que podría ser efectivo para **Insomnio**, con **23 ensayos clínicos** y **18 publicaciones** que actualmente respaldan esta dirección — en realidad, más que una hipótesis novedosa, esto refleja un uso ya establecido en la práctica clínica.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ansiedad / sedación de corto plazo (uso reconocido internacionalmente de la clase benzodiazepina; sin ficha técnica registrada en España — ver nota abajo) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.80% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción (MOA) en el Evidence Pack, ni de la ficha técnica aprobada en España (el fármaco figura como no comercializado, 0 autorizaciones). Según el conocimiento farmacológico establecido, lorazepam es un modulador alostérico positivo del receptor GABA-A, lo que produce un efecto sedante-hipnótico central bien caracterizado.

La relación entre la indicación clásica (ansiedad/sedación) y la nueva indicación predicha (insomnio) es mecanísticamente directa y no representa una hipótesis de reposicionamiento novedosa: el mismo efecto GABAérgico que reduce la ansiedad induce sueño, y las benzodiazepinas —incluido lorazepam— llevan décadas usándose en la práctica clínica real para el tratamiento del insomnio transitorio, tanto en monoterapia como en combinación (p. ej. el producto en investigación SM-1, que combina difenhidramina, zolpidem y lorazepam).

Por tanto, la predicción de TxGNN aquí confirma un patrón de uso ya validado clínicamente más que descubrir una asociación nueva, lo cual eleva la confianza en la señal pero también reduce su valor como "descubrimiento".

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03331042](https://clinicaltrials.gov/study/NCT03331042) | Fase 3 | Completado | 85 | SM-1 (difenhidramina + zolpidem + lorazepam 0.5 mg de liberación retardada) vs comparadores y placebo en modelo de avance de fase de 5 horas para insomnio transitorio |
| [NCT02671760](https://clinicaltrials.gov/study/NCT02671760) | Fase 2 | Completado | 39 | Efectos farmacodinámicos de SM-1 (incluye lorazepam) sobre tiempo total de sueño en insomnio de corto plazo |
| [NCT04396327](https://clinicaltrials.gov/study/NCT04396327) | Fase 2 | No reclutando aún | 14 | Estudio cruzado de SM-1 (con lorazepam) vs comparador activo en modelo de avance de fase de 3 horas |
| [NCT03338764](https://clinicaltrials.gov/study/NCT03338764) | Fase 3 | Retirado | 0 | SM-1 (combinación con lorazepam) para insomnio transitorio; retirado antes de reclutar |
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | Desconocido | 1400 | Cohorte prospectiva en Taiwán sobre riesgo-beneficio de hipnóticos (incluye benzodiazepinas) en adultos mayores con trastornos del sueño |
| [NCT00826553](https://clinicaltrials.gov/study/NCT00826553) | Fase 1 | Terminado | 6 | Comparación polisomnográfica de sedación con agonistas α2 vs agonistas GABA (clase de lorazepam) en pacientes ventilados mecánicamente |
| [NCT06584513](https://clinicaltrials.gov/study/NCT06584513) | N/A | Reclutando | 470 | Intervención BE-SAFE para reducir el uso de benzodiazepinas/sedantes-hipnóticos en adultos mayores, con foco en seguridad |
| [NCT03405298](https://clinicaltrials.gov/study/NCT03405298) | N/A | Completado | 44 | Programa de reducción de uso inapropiado de benzodiazepinas (incluye lorazepam) en adultos mayores |
| [NCT04572750](https://clinicaltrials.gov/study/NCT04572750) | N/A | Completado | 170 | Intervención de autogestión para promover el cese de benzodiazepinas (ansiedad/insomnio) en veteranos |
| [NCT04109118](https://clinicaltrials.gov/study/NCT04109118) | Fase 2 | Completado | 4 | Intervención piloto de tolerancia a la angustia para discontinuación de benzodiazepinas en terapia con agonistas opioides |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [3280615](https://pubmed.ncbi.nlm.nih.gov/3280615/) | 1988 | ECA | Journal of Clinical Pharmacology | Ensayo cruzado doble ciego: lorazepam 2 mg superó a flurazepam 30 mg en la mayoría de parámetros de sueño en insomnio crónico |
| [10220122](https://pubmed.ncbi.nlm.nih.gov/10220122/) | 1999 | Cohorte/Abierto | International Clinical Psychopharmacology | Lorazepam 0.5 mg TID (pauta de 24h) evaluado frente a dosis nocturna única en insomnio primario |
| [30625122](https://pubmed.ncbi.nlm.nih.gov/30625122/) | 2018 | Revisión | The Medical Letter on Drugs and Therapeutics | Revisión de fármacos para insomnio crónico, incluyendo benzodiazepinas |
| [35087274](https://pubmed.ncbi.nlm.nih.gov/35087274/) | 2022 | Revisión | Journal of Multidisciplinary Healthcare | Eficacia, seguridad e interacciones farmacológicas del tratamiento del insomnio en pacientes con COVID-19 |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Cohorte/Metaanálisis | Acta Pharmaceutica | Metaanálisis de terapias tranquilizantes en adultos mayores con enfermedades crónicas: dosis, eficacia y efectos adversos |
| [39315391](https://pubmed.ncbi.nlm.nih.gov/39315391/) | 2024 | Cohorte | BMJ Neurology Open | Prescripción de benzodiazepinas en adultos con crisis psicógenas no epilépticas en EE. UU. |
| [15341891](https://pubmed.ncbi.nlm.nih.gov/15341891/) | 2004 | Cohorte/Base de datos | Sleep Medicine | Patrones de prescripción de "hipnóticos" en una gran población de atención gestionada |
| [36340306](https://pubmed.ncbi.nlm.nih.gov/36340306/) | 2022 | Revisión | Journal of Clinical and Experimental Hepatology | Manejo del síndrome de abstinencia alcohólica (insomnio como síntoma) en enfermedad hepática alcohólica |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Revisión | Expert Opinion on Drug Metabolism & Toxicology | Farmacocinética de los fármacos ansiolíticos |
| [25453732](https://pubmed.ncbi.nlm.nih.gov/25453732/) | 2014 | Cohorte | Clinical Therapeutics | Uso de benzodiazepinas/sedantes-hipnóticos en veteranos mayores gravemente enfermos: relación riesgo-beneficio |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen múltiples ensayos clínicos (incluyendo Fase 3) que evalúan directamente formulaciones con lorazepam para insomnio transitorio, además de literatura de nivel L2 (estudios abiertos/cohortes y un ensayo controlado histórico) que documenta su eficacia hipnótica. Esto no es una hipótesis especulativa: refleja un uso clínico ya extendido de la clase benzodiazepina, por lo que puede avanzar, pero con salvaguardas dado el perfil de dependencia/uso inapropiado bien documentado en la propia evidencia (varios ensayos tratan justamente sobre reducir o discontinuar el uso crónico de benzodiazepinas).

**Para avanzar se necesita:**
- Obtener el prospecto/ficha técnica oficial de TFDA o AEMPS (gap bloqueante DG001) — sin esto no se puede completar la evaluación de seguridad inicial (S1)
- Datos formales del mecanismo de acción (MOA) desde DrugBank (gap DG002)
- Confirmar interacciones farmacológicas (la consulta DDI actual retornó "not_found")
- Definir estrategia regulatoria en España, dado que el fármaco no está actualmente comercializado (0 autorizaciones)
- Diseñar plan de monitoreo de riesgo de dependencia/uso prolongado, dado que buena parte de la evidencia disponible trata sobre discontinuación y uso inapropiado de benzodiazepinas en poblaciones vulnerables (adultos mayores, veteranos)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

