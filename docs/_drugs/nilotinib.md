---
layout: default
title: Nilotinib
parent: 僅模型預測 (L5)
nav_order: 196
evidence_level: L5
indication_count: 1
---

# Nilotinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Nilotinib: De Leucemia Mieloide Crónica a Dermatofibrosarcoma Protuberante

## Resumen en Una Frase

Nilotinib es un inhibidor de tirosina quinasa de segunda generación (BCR-ABL/PDGFR/KIT), utilizado originalmente en la leucemia mieloide crónica con cromosoma Filadelfia positivo. El modelo TxGNN predice que podría ser efectivo para **Dermatofibrosarcoma Protuberante**, con **0 ensayos clínicos** y **1 publicación** que actualmente respaldan esta dirección — la evidencia se encuentra todavía en fase de hipótesis mecanística.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Leucemia mieloide crónica Filadelfia positivo (no consta indicación aprobada en España — fármaco no comercializado) |
| Nueva Indicación Predicha | Dermatofibrosarcoma Protuberante |
| Puntaje de Predicción TxGNN | 99.31% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos estructurados detallados sobre el mecanismo de acción de nilotinib. Según la información conocida, nilotinib es un inhibidor de tirosina quinasa de segunda generación dirigido principalmente a BCR-ABL, con actividad adicional sobre PDGFR-α/β y KIT; su eficacia en la leucemia mieloide crónica Filadelfia-positiva ha sido ampliamente comprobada, y mecanísticamente podría ser aplicable al dermatofibrosarcoma protuberante (DFSP).

La mayoría de los casos de DFSP presentan la fusión génica COL1A1-PDGFB, que provoca la activación constitutiva de PDGFRB e impulsa el crecimiento tumoral. Imatinib —un inhibidor de la misma familia estructural (2-fenilaminopirimidina) que también bloquea PDGFR— ya está aprobado para el tratamiento de DFSP. Nilotinib comparte este mecanismo de inhibición multiquinasa, lo que otorga plausibilidad mecanística a la predicción de TxGNN.

No obstante, la afinidad de nilotinib por PDGFRB difiere de la de imatinib, por lo que la extrapolación de eficacia entre ambos fármacos no puede asumirse como un efecto de clase directo: la predicción requiere validación individual antes de considerarse clínicamente accionable.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Revisión | Pharmacological Research | Revisión del papel de los inhibidores de molécula pequeña del receptor PDGFR en neoplasias dependientes de la vía PDGF; proporciona el contexto mecanístico (PDGFR-α/β) relevante para la aplicabilidad de nilotinib en tumores impulsados por PDGFR, como el DFSP. |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa BCR-ABL/PDGFR/KIT) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia actual corresponde a nivel L4 (racional mecanístico por analogía con imatinib, sin ensayos clínicos ni estudios preclínicos específicos de nilotinib en DFSP). Además, la falta de datos de advertencias y contraindicaciones (TFDA/AEMPS) es una brecha bloqueante que impide completar la evaluación inicial de seguridad (S1), y el fármaco no está comercializado en España.

**Para avanzar se necesita:**
- Datos de advertencias, contraindicaciones e interacciones (brecha bloqueante DG001)
- Datos estructurados del mecanismo de acción y categorías DrugBank (DG002)
- Estudios preclínicos o series de casos que evalúen nilotinib específicamente en DFSP, dado que la evidencia actual es indirecta (por analogía con imatinib)
- Comparación de afinidad de nilotinib vs. imatinib por PDGFRB para validar la extrapolación del efecto de clase
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

