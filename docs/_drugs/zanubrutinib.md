---
layout: default
title: Zanubrutinib
parent: 僅模型預測 (L5)
nav_order: 298
evidence_level: L5
indication_count: 6
---

# Zanubrutinib
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

# Zanubrutinib: De Leucemia Linfocitica Cronica/Linfoma Linfocitico Pequeno a Leucemia Mieloide

## Resumen en Una Frase

Zanubrutinib es un inhibidor de BTK (Bruton tyrosine kinase) de nueva generacion, utilizado clinicamente en neoplasias malignas de celulas B como la leucemia linfocitica cronica/linfoma linfocitico pequeno (LLC/LLP) y la macroglobulinemia de Waldenstrom. El modelo TxGNN predice que podria ser efectivo para **Leucemia Mieloide**, pero la evidencia disponible (2 ensayos clinicos y 9 publicaciones) no respalda directamente esta nueva indicacion: ningun ensayo evalua zanubrutinib especificamente en leucemia mieloide, y toda la literatura recuperada trata sobre neoplasias de celulas B, no mieloides.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Leucemia linfocitica cronica/linfoma linfocitico pequeno (LLC/LLP) y otras neoplasias de celulas B, segun literatura clinica (no comercializado en España, sin ficha tecnica local disponible) |
| Nueva Indicacion Predicha | Leucemia Mieloide |
| Puntaje de Prediccion TxGNN | 99.65% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Espana | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion en el Evidence Pack (dato pendiente de DrugBank). Segun la informacion conocida por la literatura recuperada, zanubrutinib es un inhibidor selectivo de BTK de nueva generacion que bloquea la senalizacion del receptor de celulas B (BCR); su eficacia esta bien establecida en neoplasias linfoides de celulas B (LLC/LLP, macroglobulinemia de Waldenstrom, linfoma de celulas del manto, linfoma de zona marginal).

La leucemia mieloide, en cambio, se origina en el linaje mieloide de la medula osea y no depende de la via BCR/BTK como motor patogenico principal. Por ello, la relacion mecanistica entre la indicacion original de zanubrutinib y la nueva indicacion predicha es debil: no existe una via biologica conocida que conecte la inhibicion de BTK con la leucemogenesis mieloide.

Es probable que la alta puntuacion de TxGNN se deba a una confusion semantica del modelo por la proximidad del termino "leukemia" (compartido entre leucemias linfoides y mieloides en el grafo de conocimiento), mas que a una senal mecanistica real. Esto es consistente con que, pese a la puntuacion elevada, ningun ensayo clinico ni publicacion recuperada aborda realmente el uso de zanubrutinib en leucemia mieloide.

---

## Evidencia de Ensayos Clinicos

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04477291](https://clinicaltrials.gov/study/NCT04477291) | Fase 1 | Terminado | 45 | Estudio de CG-806 (luxeptinib), no de zanubrutinib, en LMA/SMD recidivante o refractaria. No aporta evidencia directa sobre zanubrutinib. |
| [NCT05665530](https://clinicaltrials.gov/study/NCT05665530) | Fase 1 | Completado | 86 | Estudio de PRT2527 (inhibidor de CDK9) como monoterapia y en combinacion con zanubrutinib o venetoclax en neoplasias hematologicas recidivantes/refractarias; no se centra en leucemia mieloide ni evalua zanubrutinib en monoterapia para esta indicacion. |

**Nota:** Ninguno de los dos ensayos constituye evidencia directa de eficacia de zanubrutinib en leucemia mieloide.

---

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39647999](https://pubmed.ncbi.nlm.nih.gov/39647999/) | 2025 | ECA | J Clin Oncol | Seguimiento a 5 anos del ensayo SEQUOIA (Fase 3): zanubrutinib vs. bendamustina-rituximab en LLC/LLP no tratada previamente. |
| [40334067](https://pubmed.ncbi.nlm.nih.gov/40334067/) | 2025 | Cohorte | Blood Advances | Zanubrutinib bien tolerado y eficaz en pacientes con LLC/LLP intolerantes a ibrutinib/acalabrutinib. |
| [40829104](https://pubmed.ncbi.nlm.nih.gov/40829104/) | 2026 | Cohorte | Blood Advances | Eficacia y seguridad de zanubrutinib en LLC/LLP con del(17p) y/o mutacion TP53, analisis conjunto de SEQUOIA y ALPINE. |
| [36400069](https://pubmed.ncbi.nlm.nih.gov/36400069/) | 2023 | Cohorte | Lancet Haematology | Estudio Fase 2 de zanubrutinib en neoplasias de celulas B previamente tratadas, en pacientes intolerantes a otros inhibidores de BTK. |
| [34959482](https://pubmed.ncbi.nlm.nih.gov/34959482/) | 2021 | Revision | Pharmaceutics | Revision sobre inhibidores de tirosina quinasa en leucemias cronicas (LMC y LLC). |
| [36402930](https://pubmed.ncbi.nlm.nih.gov/36402930/) | 2023 | Revision | Leukemia | Manejo de la macroglobulinemia de Waldenstrom con inhibidores de BTK. |
| [37150651](https://pubmed.ncbi.nlm.nih.gov/37150651/) | 2023 | Revision | Clin Lymphoma Myeloma Leuk | Reactivacion del virus de hepatitis B en pacientes tratados con inhibidores de BTK. |
| [36325357](https://pubmed.ncbi.nlm.nih.gov/36325357/) | 2022 | Reporte de Caso | Front Immunol | Caso de coexistencia de macroglobulinemia de Waldenstrom y leucemia linfoblastica aguda de celulas B. |
| [38288815](https://pubmed.ncbi.nlm.nih.gov/38288815/) | 2024 | Revision | Anticancer Agents Med Chem | Revision de metodos de sintesis de farmacos anticancerigenos aprobados por la FDA (2018-2021); no aborda eficacia clinica. |

**Nota:** Toda la literatura recuperada se refiere a neoplasias de celulas B (LLC/LLP, macroglobulinemia de Waldenstrom) o temas no relacionados con eficacia, no a leucemia mieloide.

---

## Informacion de Mercado en Espana

Zanubrutinib no cuenta actualmente con autorizaciones registradas en España (0 licencias, estado "no comercializado"). No hay informacion de producto, forma farmaceutica ni indicacion aprobada localmente disponible en el Evidence Pack.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificacion de Citotoxicidad | Terapia dirigida (inhibidor de BTK - Bruton tyrosine kinase) |
| Riesgo de Mielosupresion | Consultar las advertencias y precauciones del prospecto |
| Clasificacion de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Proteccion en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

---

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La puntuacion de TxGNN es alta, pero carece de respaldo real: ningun ensayo clinico ni publicacion aborda especificamente zanubrutinib en leucemia mieloide, y el mecanismo de accion conocido (inhibicion de BTK/via BCR) no tiene una relacion biologica establecida con la leucemogenesis mieloide. Es probable que la senal del modelo derive de una confusion semantica del termino "leukemia" mas que de una base mecanistica solida.

**Para avanzar se necesita:**
- Datos de mecanismo de accion (MOA) de DrugBank para confirmar o descartar cualquier via de accion relevante en celulas mieloides
- Advertencias, contraindicaciones y prospecto de la AEMPS (actualmente no disponibles)
- Estudios preclinicos que evaluen especificamente la actividad de zanubrutinib en lineas celulares o modelos de leucemia mieloide
- Ensayos clinicos dedicados a zanubrutinib (no en combinacion con otros farmacos) en poblaciones con leucemia mieloide, actualmente inexistentes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

