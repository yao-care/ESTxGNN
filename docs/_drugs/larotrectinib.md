---
layout: default
title: Larotrectinib
parent: 僅模型預測 (L5)
nav_order: 159
evidence_level: L5
indication_count: 2
---

# Larotrectinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Larotrectinib: Sin Indicación Original Registrada → Neoplasia Endocrina Múltiple

## Resumen en Una Frase

No hay indicación original registrada en este pack de evidencia para larotrectinib (sin licencias en Taiwán/España, sin MOA documentado). El modelo TxGNN predice que podría ser efectivo para **Neoplasia Endocrina Múltiple**, con **1 ensayo clínico** y **2 publicaciones** que actualmente respaldan esta dirección, aunque con vínculo mecanístico solo indirecto.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No registrada en este pack (sin licencias ni MOA disponibles) |
| Nueva Indicación Predicha | Neoplasia Endocrina Múltiple |
| Puntaje de Predicción TxGNN | 99.24% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos formales del mecanismo de acción de larotrectinib en este informe (dato pendiente, severidad Alta). Según la información de razonabilidad mecanística incluida en el pack, larotrectinib es un inhibidor selectivo pan-TRK, dirigido contra las proteínas de fusión NTRK1/2/3.

La neoplasia endocrina múltiple (MEN) está impulsada principalmente por mutaciones del gen MEN1 o por alteraciones de RET (en MEN2), no por fusiones de NTRK. La bibliografía aportada como respaldo se centra en inhibidores de RET (selpercatinib, pralsetinib) y en inhibidores multiquinasa para cáncer de tiroides avanzado, sin datos directos sobre larotrectinib ni sobre la vía TRK en MEN.

Por tanto, el vínculo mecanístico es indirecto: se apoya en la cercanía estructural dentro de la red de tirosina-quinasas relevantes en cáncer de tiroides, no en una superposición molecular directa entre el blanco del fármaco y la biología de MEN. El propio análisis de razonabilidad del pack califica esta conexión como una inferencia de red, no como evidencia directa.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02465060](https://clinicaltrials.gov/study/NCT02465060) | Fase 2 | Activo, no reclutando | 6452 | MATCH: ensayo tipo "cesta" guiado por biomarcadores en tumores sólidos, linfomas y mieloma refractarios; incluye un brazo con larotrectinib para fusiones NTRK, pero no está diseñado para MEN ni hay evidencia pública de pacientes con MEN incluidos en ese brazo. Relevancia clasificada como Grado C (asociación estructural, no directa). |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31322645](https://pubmed.ncbi.nlm.nih.gov/31322645/) | 2019 | Revisión | Endocrine Reviews | Panorama de inhibidores de quinasa en cáncer de tiroides avanzado; menciona inhibidores mutación-específicos (dabrafenib/trametinib) pero no se centra en larotrectinib ni en MEN. |
| [38438731](https://pubmed.ncbi.nlm.nih.gov/38438731/) | 2024 | Cohorte/Mecanístico | NPJ Precision Oncology | Mecanismos de resistencia adaptativa a inhibidores selectivos de RET (selpercatinib) en carcinoma medular de tiroides con mutación RET; no evalúa larotrectinib ni fusiones NTRK. |

## Candidato Adicional Identificado: HER2 Positive Breast Carcinoma

TxGNN también predice actividad para **cáncer de mama HER2 positivo** (puntaje 99.14%, rank 11413), pero con nivel de evidencia **L5** (solo predicción de modelo, sin ensayos clínicos registrados) y recomendación **Hold**.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38852701](https://pubmed.ncbi.nlm.nih.gov/38852701/) | 2024 | Preclínico/In-vitro | Cancer Letters | Inhibición dual de TrkA y JAK2 con entrectinib (no larotrectinib) + pacritinib suprime crecimiento/metástasis en cáncer de mama HER2+ y triple negativo; extrapolación entre fármacos, sin datos directos de larotrectinib. |

No hay ensayos clínicos registrados para esta indicación.

## Citotoxicidad

Larotrectinib actúa como inhibidor selectivo dirigido (pan-TRK) sobre neoplasias, por lo que aplica esta sección.

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor selectivo pan-TRK, NTRK1/2/3), no citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Ítems de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ambas indicaciones predichas (MEN: L4; cáncer de mama HER2+: L5) carecen de evidencia clínica directa sobre larotrectinib — la evidencia disponible es indirecta (asociación de red o extrapolación entre fármacos). Además, existe un vacío de datos bloqueante: no hay ficha técnica/advertencias de TFDA ni MOA confirmado, y el fármaco no está comercializado en España (0 autorizaciones), lo que impide el análisis preliminar de seguridad (S1).

**Para avanzar se necesita:**
- Ficha técnica y advertencias/contraindicaciones de TFDA (bloqueante para S1)
- Confirmación del mecanismo de acción vía DrugBank u otra fuente primaria
- Estudios preclínicos o clínicos que evalúen larotrectinib específicamente (no análogos como entrectinib/selpercatinib) en MEN o cáncer de mama HER2+
- Evaluación de disponibilidad de rutas de administración y compatibilidad posológica
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

