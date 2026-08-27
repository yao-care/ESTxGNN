---
layout: default
title: Lanadelumab
parent: 僅模型預測 (L5)
nav_order: 156
evidence_level: L5
indication_count: 10
---

# Lanadelumab
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

# Lanadelumab: De Indicación No Registrada en España a Déficit del Inhibidor de C1 (Angioedema Hereditario)

## Resumen en Una Frase

No existen datos de indicación original ni de comercialización de lanadelumab en España (0 autorizaciones registradas). El modelo TxGNN predice que sería efectivo para **déficit del inhibidor de C1 (angioedema hereditario, AHE)**, con **22 ensayos clínicos** y **20 publicaciones** que respaldan actualmente esta dirección — de hecho, varios de estos ensayos indican que lanadelumab (Takhzyro®) ya está aprobado para esta misma indicación en China, Japón y Corea del Sur, por lo que el vacío principal es de registro en España, no de evidencia científica.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (sin registro de licencias ni indicación aprobada en España) |
| Nueva Indicación Predicha | Déficit del inhibidor de C1 (Angioedema Hereditario) |
| Puntaje de Predicción TxGNN | 99.9955% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos estructurados sobre el mecanismo de acción de lanadelumab (campo `original_moa` marcado como vacío, brecha de datos de severidad Alta). Sin embargo, la literatura recogida en este paquete de evidencia sí describe el mecanismo: lanadelumab es un anticuerpo monoclonal totalmente humano que inhibe la calicreína plasmática (plasma kallikrein), bloqueando así la producción excesiva de bradicinina — el mediador vasodilatador responsable de los ataques de angioedema en pacientes con deficiencia o disfunción de C1 esterasa inhibidor (mutaciones del gen SERPING1).

Esta relación mecanística es directa: el déficit del inhibidor de C1 es precisamente la vía fisiopatológica sobre la que actúa el fármaco (sistema calicreína-cinina), lo cual explica por qué TxGNN asigna un puntaje casi máximo (99.9955%) a esta indicación.

Cabe destacar que, según las descripciones de los propios ensayos incluidos en este paquete, lanadelumab ya cuenta con aprobación regulatoria para esta indicación en varios países (China, Japón, Corea del Sur), bajo el nombre comercial Takhzyro®. Esto sugiere que, más que un "reposicionamiento" experimental, se trata de una indicación ya validada clínica y regulatoriamente a nivel global, cuyo principal vacío en este análisis es la ausencia de registro y comercialización en España.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02586805](https://clinicaltrials.gov/study/NCT02586805) | Fase 3 | Completado | 125 | Estudio HELP: ECA doble ciego controlado con placebo para prevención de ataques agudos de AHE tipo I/II con DX-2930 (lanadelumab) |
| [NCT02741596](https://clinicaltrials.gov/study/NCT02741596) | Fase 3 | Completado | 212 | HELP Study Extension: seguridad y eficacia a largo plazo de DX-2930 en prevención de ataques de AHE |
| [NCT04180163](https://clinicaltrials.gov/study/NCT04180163) | Fase 3 | Completado | 12 | Eficacia y seguridad de lanadelumab en pacientes japoneses con AHE tipo I o II |
| [NCT05460325](https://clinicaltrials.gov/study/NCT05460325) | Fase 3 | Completado | 20 | Seguridad, farmacocinética y eficacia de lanadelumab en pacientes chinos con AHE, tratamiento durante 26 semanas |
| [NCT04070326](https://clinicaltrials.gov/study/NCT04070326) | Fase 3 | Completado | 21 | SPRING Study: seguridad, PK/PD y eficacia de lanadelumab en pacientes pediátricos de 2 a <12 años con AHE |
| [NCT04687137](https://clinicaltrials.gov/study/NCT04687137) | Fase 3 | Completado | 12 | Programa de acceso ampliado en Japón para pacientes con AHE tipo I/II con lanadelumab (TAK-743) |
| [NCT02093923](https://clinicaltrials.gov/study/NCT02093923) | Fase 1 | Completado | 38 | Estudio de dosis ascendente múltiple: seguridad, tolerabilidad y PK de DX-2930 en sujetos con AHE |
| [NCT01923207](https://clinicaltrials.gov/study/NCT01923207) | Fase 1 | Completado | 32 | Estudio de dosis única ascendente en sujetos sanos: seguridad, tolerabilidad y PK de DX-2930 |
| [NCT03845400](https://clinicaltrials.gov/study/NCT03845400) | N/A | Completado | 168 | EMPOWER Study: estudio observacional en EE.UU. y Canadá comparando tasa de ataques antes/después de iniciar lanadelumab |
| [NCT04130191](https://clinicaltrials.gov/study/NCT04130191) | N/A | Completado | 140 | ENABLE Study: efectividad a largo plazo de lanadelumab en práctica clínica real, seguimiento de 24-36 meses |

*(Se identificaron 22 ensayos en total; se listan los 10 más relevantes por fase, diseño y relevancia directa)*

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30480729](https://pubmed.ncbi.nlm.nih.gov/30480729/) | 2018 | ECA | JAMA | Efecto de lanadelumab vs. placebo en la prevención de ataques de angioedema hereditario |
| [30267321](https://pubmed.ncbi.nlm.nih.gov/30267321/) | 2018 | Revisión | Drugs | Lanadelumab: primera aprobación global; anticuerpo monoclonal inhibidor de calicreína plasmática |
| [34287942](https://pubmed.ncbi.nlm.nih.gov/34287942/) | 2022 | ECA (extensión abierta) | Allergy | HELP OLE Study: prevención a largo plazo de ataques de AHE con lanadelumab |
| [30539362](https://pubmed.ncbi.nlm.nih.gov/30539362/) | 2019 | Revisión | BioDrugs | Revisión de estudios preclínicos y de Fase I de lanadelumab para tratamiento profiláctico de AHE |
| [32187470](https://pubmed.ncbi.nlm.nih.gov/32187470/) | 2020 | Revisión | New England Journal of Medicine | Revisión clínica de angioedema hereditario |
| [39508959](https://pubmed.ncbi.nlm.nih.gov/39508959/) | 2024 | Revisión sistemática | Clinical Reviews in Allergy & Immunology | Ataques de AHE en pacientes bajo profilaxis a largo plazo |
| [39701274](https://pubmed.ncbi.nlm.nih.gov/39701274/) | 2025 | Estudio observacional | JACI In Practice | Estudio INTEGRATED multinacional: efectividad real de lanadelumab en AHE |
| [40434599](https://pubmed.ncbi.nlm.nih.gov/40434599/) | 2025 | Metaanálisis en red | Drugs in R&D | Comparación de terapias farmacológicas para profilaxis a largo plazo de AHE |
| [37898409](https://pubmed.ncbi.nlm.nih.gov/37898409/) | 2024 | Revisión | Journal of Allergy and Clinical Immunology | Carga de la enfermedad de AHE por déficit de C1-INH en la región Asia-Pacífico |
| [39836016](https://pubmed.ncbi.nlm.nih.gov/39836016/) | 2025 | Comparación indirecta | Journal of Comparative Effectiveness Research | Comparación de lanadelumab vs. inhibidor de C1-esterasa en pacientes pediátricos con AHE |

*(Se identificaron 20 publicaciones en total; se listan las 10 más relevantes priorizando ECA y revisiones sistemáticas)*

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se dispone de advertencias, contraindicaciones ni interacciones farmacológicas estructuradas en este paquete de evidencia — la obtención del prospecto de la TFDA/AEMPS (brecha DG001, severidad Bloqueante) es un requisito previo indispensable antes de cualquier evaluación de seguridad (S1).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia clínica es sólida y consistente (1 ECA pivotal de Fase 3 completado —HELP Study— más una amplia base de estudios de extensión, pediátricos y observacionales en múltiples países, con aprobación regulatoria ya vigente para esta misma indicación fuera de España). Sin embargo, la ausencia total de datos de seguridad estructurados (advertencias, contraindicaciones, interacciones) constituye una brecha bloqueante que impide avanzar a la evaluación de seguridad inicial (S1), y el fármaco no está registrado ni comercializado en España.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto/ficha técnica (TFDA/AEMPS) con advertencias y contraindicaciones formales
- Confirmar el mecanismo de acción mediante consulta directa a DrugBank (brecha DG002)
- Evaluar la vía regulatoria para el registro y comercialización del fármaco en España, dado que ya cuenta con aprobaciones en otros mercados para esta indicación
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

