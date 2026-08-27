---
layout: default
title: Idelalisib
parent: 僅模型預測 (L5)
nav_order: 139
evidence_level: L5
indication_count: 10
---

# Idelalisib
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

# Idelalisib: De Leucemia Linfocitica Cronica a Linfoma de Celulas del Manto

## Resumen en Una Frase

Idelalisib es un inhibidor oral de PI3Kδ, aprobado originalmente para leucemia linfocítica crónica (LLC) y linfoma folicular refractarios.
El modelo TxGNN predice que también podría ser efectivo para **Linfoma de Células del Manto (MCL)**,
con **9 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección, aunque con señales mixtas de resistencia.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Leucemia linfocítica crónica (LLC) y linfoma folicular (conocido por literatura; sin registro formal en este Evidence Pack) |
| Nueva Indicacion Predicha | Linfoma de Células del Manto (Mantle Cell Lymphoma) |
| Puntaje de Prediccion TxGNN | 99.84% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

---

## Por que es Razonable esta Prediccion?

No hay datos estructurados de DrugBank sobre el mecanismo de acción (dato pendiente de completar). Sin embargo, la literatura incluida en este informe describe de forma consistente a idelalisib como un inhibidor selectivo, de primera clase, de la isoforma delta de la fosfatidilinositol 3-quinasa (PI3Kδ), enzima que actúa como nodo central de la vía de señalización del receptor de células B (BCR) y que se expresa de forma restringida en células hematopoyéticas.

La LLC y el linfoma folicular (indicaciones conocidas de idelalisib) y el linfoma de células del manto comparten un origen común: son neoplasias de células B maduras que dependen, en distinto grado, de la señalización constitutiva del BCR para su supervivencia y proliferación. Esta dependencia mecanística es la base racional de la predicción del modelo TxGNN.

No obstante, la evidencia disponible es ambivalente: existen ensayos clínicos que demuestran actividad directa de idelalisib en MCL recidivante/refractario, pero también hay literatura preclínica que documenta **resistencia intrínseca** de las células de MCL a idelalisib, con estrategias de reversión mediante inhibición de p300/CBP o mediante pérdida de CBX5. Esto sugiere que el mecanismo es plausible, pero que la eficacia clínica depende de subgrupos moleculares aún no bien caracterizados.

---

## Evidencia de Ensayos Clinicos

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01838434](https://clinicaltrials.gov/study/NCT01838434) | Fase 1/2 (aleatorizado) | Completado | 106 | Idelalisib + lenalidomida en MCL recidivante/refractario; ensayo con población directamente correspondiente |
| [NCT01088048](https://clinicaltrials.gov/study/NCT01088048) | Fase 1 | Completado | 241 | Idelalisib en combinación con anti-CD20, quimioterapia, inhibidor mTOR, etc., en NHL indolente, MCL y LLC recidivante/refractaria |
| [NCT02603445](https://clinicaltrials.gov/study/NCT02603445) | Fase 1b | Completado | 20 | BCL201 + idelalisib en linfoma folicular y MCL |
| [NCT03740529](https://clinicaltrials.gov/study/NCT03740529) | Fase 1/2 | Completado | 803 | Pirtobrutinib oral en LLC/SLL/NHL previamente tratados; idelalisib figura como tratamiento previo, no como fármaco en estudio |
| [NCT02824159](https://clinicaltrials.gov/study/NCT02824159) | N/A | Completado | 121 | Estudio de vida real sobre relación entre efectos secundarios y concentración plasmática de ibrutinib e idelalisib |
| [NCT01796470](https://clinicaltrials.gov/study/NCT01796470) | Fase 2 | Terminado | 66 | Entospletinib + idelalisib en neoplasias hematológicas recidivantes/refractarias (LLC, MCL, DLBCL, NHL indolente) |
| [NCT02457598](https://clinicaltrials.gov/study/NCT02457598) | Fase 1b | Terminado | 203 | Tirabrutinib en combinación con otras terapias dirigidas, incluido idelalisib, en neoplasias de células B |
| [NCT03151057](https://clinicaltrials.gov/study/NCT03151057) | Fase 1 | Terminado | 16 | Idelalisib como mantenimiento post-trasplante alogénico en neoplasias de células B, muestra pequeña |
| [NCT04985214](https://clinicaltrials.gov/study/NCT04985214) | N/A | Desconocido | 464 | Estudio observacional de calidad de vida en pacientes con linfoma tratados con terapia oral (incluye idelalisib) |

---

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [24615778](https://pubmed.ncbi.nlm.nih.gov/24615778/) | 2014 | Ensayo clínico Fase 1 | Blood | Estudio Fase 1 del inhibidor PI3Kδ idelalisib en 40 pacientes con MCL recidivante/refractario; evalúa seguridad, DLT, ORR, PFS |
| [24795031](https://pubmed.ncbi.nlm.nih.gov/24795031/) | 2014 | Cohorte/Clínico | Cancer Discovery | Idelalisib mostró actividad clínica en pacientes con MCL muy pretratados |
| [33850273](https://pubmed.ncbi.nlm.nih.gov/33850273/) | 2022 | Preclínico | Acta Pharmacologica Sinica | Inhibición de p300/CBP revierte la resistencia intrínseca de MCL a idelalisib |
| [40466505](https://pubmed.ncbi.nlm.nih.gov/40466505/) | 2025 | Preclínico | Phytomedicine | Pérdida de CBX5 induce resistencia a idelalisib en MCL; propóleos restaura sensibilidad vía ferroptosis |
| [27342398](https://pubmed.ncbi.nlm.nih.gov/27342398/) | 2017 | Preclínico | Clin Cancer Res | Idelalisib afecta el crecimiento celular en MCL mediante mecanismos de regulación traduccional |
| [38815797](https://pubmed.ncbi.nlm.nih.gov/38815797/) | 2024 | Preclínico | Cancer Letters | Idelalisib potencia el efecto antitumoral de palbociclib vía PLK1 en linfoma de células B (incluye MCL) |
| [24974852](https://pubmed.ncbi.nlm.nih.gov/24974852/) | 2014 | Revisión | Br J Haematol | Regímenes actuales y agentes novedosos para MCL |
| [26360791](https://pubmed.ncbi.nlm.nih.gov/26360791/) | 2015 | Revisión | Expert Opin Pharmacother | Opciones de tratamiento para MCL |
| [23512567](https://pubmed.ncbi.nlm.nih.gov/23512567/) | 2013 | Revisión | Curr Treat Options Oncol | Terapias actuales y emergentes en MCL |
| [25023849](https://pubmed.ncbi.nlm.nih.gov/25023849/) | 2015 | Revisión | Medicina Clínica | Hacia una estrategia terapéutica personalizada en MCL |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificacion de Citotoxicidad | Terapia dirigida (inhibidor selectivo de PI3Kδ) |
| Riesgo de Mielosupresion | Consultar las advertencias y precauciones del prospecto |
| Clasificacion de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma completo con diferencial, función hepática (transaminasas), vigilancia de síntomas respiratorios y de infecciones oportunistas |
| Proteccion en Manejo | Debe seguir la normativa de manejo de fármacos antineoplásicos vigente en el centro |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. La ficha técnica de TFDA/AEMPS (advertencias, contraindicaciones) y el perfil de interacciones farmacológicas no fueron recuperados en este ciclo de datos y constituyen un vacío bloqueante para la evaluación de seguridad inicial (S1).

---

## Conclusion y Proximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia de nivel L2 se apoya en un único ensayo Fase 1/2 aleatorizado directamente relevante (NCT01838434, n=106) y en un estudio Fase 1 publicado (PMID 24615778), pero la literatura preclínica reciente documenta resistencia intrínseca de MCL a idelalisib, lo que introduce incertidumbre sobre la magnitud del beneficio clínico y sugiere que la respuesta podría limitarse a subgrupos moleculares específicos.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha técnica de TFDA/AEMPS con advertencias, contraindicaciones e interacciones (vacío bloqueante, DG001)
- Completar los datos estructurados de mecanismo de acción vía DrugBank (DG002)
- Aclarar los mecanismos de resistencia intrínseca (p300/CBP, CBX5) y su relevancia para la selección de pacientes
- Dado que idelalisib no está comercializado en España, evaluar la vía regulatoria disponible (uso compasivo, importación) antes de cualquier desarrollo clínico local
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

