---
layout: default
title: Givosiran
parent: 僅模型預測 (L5)
nav_order: 135
evidence_level: L5
indication_count: 10
---

# Givosiran
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

# Givosiran: De Porfiria Hepática Aguda a Porfiria por Deficiencia de ALA-Deshidratasa (ADP)

> **Nota sobre la candidata seleccionada:** TxGNN generó 10 predicciones para givosiran. Nueve de ellas —incluida la de mayor puntaje bruto ("hepatopulmonary syndrome", 99.99%)— no cuentan con ningún ensayo clínico ni publicación de respaldo y su racional mecanístico se describe como "sin relación conocida" (Nivel L5, Hold). La única candidata con evidencia real es **porfiria por deficiencia de ALA-deshidratasa (ADP)**, con 8 publicaciones asociadas. Este informe se centra en ella por ser la única evaluable de forma sustantiva.

## Resumen en Una Frase

Givosiran es un fármaco de ARN de interferencia (siRNA) utilizado originalmente para el tratamiento de la porfiria hepática aguda (PHA), un grupo de trastornos hereditarios del metabolismo del hemo. El modelo TxGNN predice que también podría ser eficaz en la **porfiria por deficiencia de ALA-deshidratasa (ADP)**, una variante ultra-rara del mismo grupo de enfermedades, con **8 publicaciones** que actualmente respaldan esta dirección, aunque **sin ningún ensayo clínico dedicado específicamente a la ADP**.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Porfiria Hepática Aguda (PHA), predominantemente Porfiria Intermitente Aguda |
| Nueva Indicación Predicha | Porfiria por Deficiencia de ALA-Deshidratasa (ADP) |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

No hay un registro específico del mecanismo de acción en el campo de MOA del expediente (dato pendiente), pero la evidencia recopilada permite reconstruirlo con claridad: givosiran es un siRNA conjugado con GalNAc que se dirige al ARNm de la enzima hepática ALAS1 (delta-aminolevulinato sintasa 1), la enzima limitante del primer paso de la biosíntesis del hemo. Al reducir la expresión de ALAS1, disminuye la producción de los metabolitos neurotóxicos ácido delta-aminolevulínico (ALA) y porfobilinógeno (PBG), que son los responsables de las crisis agudas neuroviscerales características de las porfirias hepáticas agudas.

La ADP (deficiencia de ALA-deshidratasa) pertenece al mismo grupo de porfirias hepáticas agudas que la indicación original de givosiran (junto con la porfiria intermitente aguda, la coproporfiria hereditaria y la porfiria variegata), y comparte la misma vía fisiopatológica río arriba: la inducción de ALAS1 hepática. Por eso, mecanísticamente, reducir ALAS1 debería beneficiar también a los pacientes con ADP, y de hecho el fármaco ya cuenta con aprobación regulatoria general para "prevención de ataques de porfirias hepáticas agudas", categoría que en principio incluye la ADP.

Sin embargo, hay un matiz importante: la ADP es extremadamente rara (se han descrito muy pocos casos en el mundo) y el defecto enzimático (ALAD/PBGS, que convierte ALA en PBG) es distinto al de la porfiria intermitente aguda (deficiencia de PBG-deaminasa), por lo que la equivalencia terapéutica no está probada. De hecho, la evidencia de literatura incluye un caso documentado de **falta de respuesta a givosiran en un paciente con ADP** (ver sección de literatura), lo que introduce incertidumbre real sobre la generalización del mecanismo a este subtipo específico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados específicamente para porfiria por deficiencia de ALA-deshidratasa (búsquedas en ClinicalTrials.gov e ICTRP sin resultados).

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35067977](https://pubmed.ncbi.nlm.nih.gov/35067977/) | 2022 | ECA / análisis post-hoc (predominio AIP) | Journal of Internal Medicine | La terapia con givosiran reduce significativamente la tasa de ataques en porfiria intermitente aguda |
| [36028858](https://pubmed.ncbi.nlm.nih.gov/36028858/) | 2022 | ECA (análisis secundario Fase 3 ENVISION) | Orphanet Journal of Rare Diseases | Evalúa la carga de enfermedad en pacientes con PHA en el ensayo Fase 3 ENVISION de givosiran |
| [39313028](https://pubmed.ncbi.nlm.nih.gov/39313028/) | 2024 | Revisión | Revista Clínica Española | Abordaje terapéutico de las crisis agudas de porfirias hepáticas; describe la inducción de ALAS1 como desencadenante común |
| [35734365](https://pubmed.ncbi.nlm.nih.gov/35734365/) | 2022 | Revisión | Drug Design, Development and Therapy | Revisión del diseño, desarrollo y lugar terapéutico de givosiran en adultos con PHA |
| [40312531](https://pubmed.ncbi.nlm.nih.gov/40312531/) | 2025 | Cohorte | Scientific Reports | Eficacia y seguridad de givosiran en pacientes japoneses con PHA (estudio de acceso expandido, n=10) |
| [37027823](https://pubmed.ncbi.nlm.nih.gov/37027823/) | 2023 | Revisión | Blood | Revisión de la terapia de interferencia de ARN en porfirias hepáticas agudas, centrada en ALAS1 |
| [36883675](https://pubmed.ncbi.nlm.nih.gov/36883675/) | 2023 | Estudio de modelado PK/PD | CPT: Pharmacometrics & Systems Pharmacology | Modelo PK/PD de la reducción de ALA urinario tras tratamiento con givosiran |
| [35991568](https://pubmed.ncbi.nlm.nih.gov/35991568/) | 2022 | Reporte de caso | Frontiers in Genetics | **Falta de respuesta a givosiran en un caso de porfiria por deficiencia de ALA-deshidratasa (ADP)**, pese a que el fármaco está aprobado para prevención de ataques en PHA incluyendo ADP |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El mecanismo de acción (inhibición de ALAS1) es coherente con la fisiopatología de la ADP y el fármaco ya tiene aprobación general para porfirias hepáticas agudas, que en teoría incluye este subtipo. Sin embargo, la ADP es ultra-rara y el único dato clínico específico disponible es un reporte de caso que documenta **falta de respuesta**, sin ningún ensayo clínico dedicado que confirme eficacia en esta población concreta. La evidencia de apoyo (ENVISION Fase 3, estudio japonés de acceso expandido) corresponde a PHA en general, no a ADP específicamente.

**Para avanzar se necesita:**
- Confirmación de la indicación aprobada y advertencias/contraindicaciones vía ficha técnica de la AEMPS o EMA (dato actualmente ausente)
- Caracterización adicional de casos de ADP tratados con givosiran para contrastar el reporte de falta de respuesta
- Datos de interacciones farmacológicas (DDI), actualmente sin registro
- Evaluación de si la extrema rareza de la ADP justifica un desarrollo clínico dedicado o si basta con vigilancia post-comercialización dentro de la indicación ya aprobada de PHA
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

