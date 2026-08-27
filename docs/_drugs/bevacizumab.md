---
layout: default
title: Bevacizumab
parent: 僅模型預測 (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
---

# Bevacizumab
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

# Bevacizumab: Hacia Neoplasia Quística (Cáncer de Ovario) como Nueva Indicación

## Resumen en Una Frase

Bevacizumab es un anticuerpo monoclonal anti-VEGF de uso oncológico establecido, actualmente **no comercializado en España** y sin indicación original registrada en esta base de datos. El modelo TxGNN predice que podría ser efectivo para **Neoplasia Quística** (mayoritariamente representada por cáncer de ovario en la evidencia disponible), con **8 ensayos clínicos** y **20 publicaciones** que respaldan esta dirección, incluyendo un ensayo de Fase 3 con 1.052 pacientes.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos regulatorios (fármaco no comercializado en España; sin licencias registradas) |
| Nueva Indicación Predicha | Neoplasia Quística (Cystic Neoplasm) |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en esta base de datos. Según la evidencia clínica recopilada, bevacizumab es un anticuerpo monoclonal que actúa como inhibidor del factor de crecimiento endotelial vascular (VEGF-A), un mecanismo antiangiogénico documentado de forma consistente en los ensayos incluidos en este informe (cáncer de ovario, mama, colorrectal, renal, tumores estromales gastrointestinales, entre otros).

Las "neoplasias quísticas" son, en la práctica clínica, con frecuencia manifestaciones de cáncer de ovario (especialmente el subtipo seroso de bajo grado y el mucinoso), un tumor altamente vascularizado donde el bloqueo de VEGF ya es una estrategia terapéutica consolidada. Esto explica por qué la mayor parte de la evidencia recuperada para esta predicción corresponde en realidad a estudios sobre cáncer de ovario y no a "neoplasia quística" como categoría amplia.

Mecanísticamente, la aplicabilidad es razonable: la angiogénesis tumoral es un rasgo compartido entre tumores quísticos ováricos y otras neoplasias donde bevacizumab ya demuestra actividad. Sin embargo, debe señalarse una salvedad importante: la etiqueta "neoplasia quística" agrupa entidades muy heterogéneas (benignas y malignas, de múltiples órganos), y la evidencia real disponible es específica de cáncer de ovario, por lo que la extrapolación a neoplasias quísticas benignas o de otros órganos no está respaldada.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00565851](https://clinicaltrials.gov/study/NCT00565851) | Fase 3 | Activo, no reclutando | 1.052 | Carboplatino + paclitaxel (o gemcitabina) ± bevacizumab, seguido de bevacizumab de mantenimiento, en cáncer de ovario/peritoneal/trompa de Falopio recidivante sensible a platino |
| [NCT03074513](https://clinicaltrials.gov/study/NCT03074513) | Fase 2 | Activo, no reclutando | 133 | Atezolizumab + bevacizumab en tumores sólidos raros, estudio abierto de un solo brazo |
| [NCT00381797](https://clinicaltrials.gov/study/NCT00381797) | Fase 2 | Completado | 97 | Bevacizumab + irinotecán en niños con glioma, meduloblastoma o ependimoma recurrente/refractario |
| [NCT00023959](https://clinicaltrials.gov/study/NCT00023959) | Fase 1 | Completado | 39 | Bevacizumab + 5-FU + hidroxiurea con radioterapia concomitante en cáncer de cabeza y cuello de mal pronóstico |
| [NCT01096381](https://clinicaltrials.gov/study/NCT01096381) | N/A | Terminado | 8 | Biomarcadores de hipertensión inducida por bevacizumab en tumores sólidos malignos |
| [NCT00492089](https://clinicaltrials.gov/study/NCT00492089) | Fase 2 | Completado | 11 | Bevacizumab para reducir el daño por radiación cerebral tras radioterapia en tumor cerebral, meningioma o cáncer de cabeza y cuello |
| [NCT00101348](https://clinicaltrials.gov/study/NCT00101348) | Fase 1/2 | Completado | 66 | Erlotinib + cetuximab ± bevacizumab en carcinoma renal metastásico y otros tumores sólidos |
| [NCT00324987](https://clinicaltrials.gov/study/NCT00324987) | Fase 3 | Terminado (prematuramente) | 12 | Imatinib ± bevacizumab en tumor estromal gastrointestinal (GIST) metastásico/irresecable |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37754507](https://pubmed.ncbi.nlm.nih.gov/37754507/) | 2023 | Revisión Sistemática | Current Oncology | Confirma actividad de bevacizumab en cáncer de ovario seroso de bajo grado, subtipo quimiorresistente sin tratamiento estándar definido |
| [38328890](https://pubmed.ncbi.nlm.nih.gov/38328890/) | 2024 | Cohorte | Future Oncology | En 51 pacientes con cáncer de ovario seroso de bajo grado recurrente, tasa de respuesta objetiva del 54,1% con bevacizumab + quimioterapia |
| [24978709](https://pubmed.ncbi.nlm.nih.gov/24978709/) | 2014 | Estudio de cohorte | Int J Gynecol Cancer | Bevacizumab muestra actividad significativa en cáncer de ovario seroso de bajo grado y peritoneal primario recurrente |
| [18165643](https://pubmed.ncbi.nlm.nih.gov/18165643/) | 2008 | Ensayo Fase II | J Clin Oncol | Bevacizumab + ciclofosfamida oral metronómica evaluado en cáncer de ovario recurrente (consorcio California/Chicago/Princess Margaret) |
| [27412268](https://pubmed.ncbi.nlm.nih.gov/27412268/) | 2016 | ECA Fase II | Cancer | Paclitaxel + capecitabina + bevacizumab de primera línea en cáncer de mama triple negativo metastásico/localmente avanzado (estudio GINECO A-TaXel) |
| [40513287](https://pubmed.ncbi.nlm.nih.gov/40513287/) | 2025 | Sub-estudio Fase III | Eur J Cancer | Estudio ancilar de PAOLA-1/ENGOT-ov25: bevacizumab + olaparib de mantenimiento en cáncer de ovario seroso de alto grado con deficiencia de recombinación homóloga |
| [37657955](https://pubmed.ncbi.nlm.nih.gov/37657955/) | 2023 | Cohorte | Clin Colorectal Cancer | Mitomicina-C + capecitabina metronómica + bevacizumab en pseudomixoma peritoneal irresecable/recidivante de origen apendicular |
| [18796376](https://pubmed.ncbi.nlm.nih.gov/18796376/) | 2008 | Cohorte | Clin Transl Oncol | Ciclofosfamida oral + bevacizumab en cáncer de ovario pesadamente pretratado |
| [32494876](https://pubmed.ncbi.nlm.nih.gov/32494876/) | 2020 | Revisión | Curr Oncol Rep | Manejo de primera línea del cáncer de ovario seroso de alto grado avanzado; describe el papel de la vía VEGF |
| [27141073](https://pubmed.ncbi.nlm.nih.gov/27141073/) | 2016 | Revisión | Ann Oncol | Carcinoma ovárico mucinoso: diferenciación diagnóstica entre tumores primarios y metastásicos |

---

## Información de Mercado en España

Actualmente no hay autorizaciones de comercialización registradas para bevacizumab en esta base de datos (estado: **no comercializado**, 0 licencias).

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (anticuerpo monoclonal antiangiogénico anti-VEGF; no es quimioterapia citotóxica convencional) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La evidencia alcanza nivel L1, con un ensayo Fase 3 de gran tamaño (n=1.052) y una revisión sistemática dedicada que respaldan la actividad de bevacizumab en cáncer de ovario, la entidad clínica que mejor representa "neoplasia quística" en los datos disponibles. No obstante, esta evidencia es específica de cáncer de ovario (particularmente el subtipo seroso de bajo grado) y no de neoplasias quísticas benignas u otros órganos, por lo que el avance debe limitarse a esa subpoblación y con las debidas salvaguardas.

**Para avanzar se necesita:**
- Mecanismo de acción (MOA), advertencias, contraindicaciones e interacciones farmacológicas (actualmente data gap bloqueante para evaluación de seguridad)
- Delimitación clínica precisa de la subpoblación diana (cáncer de ovario seroso de bajo grado / mucinoso) en lugar de "neoplasia quística" como categoría genérica
- Confirmación del estatus regulatorio y vía de acceso en España, dado que el fármaco no está actualmente comercializado en este mercado
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

