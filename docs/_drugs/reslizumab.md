---
layout: default
title: Reslizumab
parent: 僅模型預測 (L5)
nav_order: 242
evidence_level: L5
indication_count: 2
---

# Reslizumab
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

# Reslizumab: Indicación Original No Disponible → Trombocitopenia por Destrucción Inmune

*Candidato: TW-DB06602-multi · Versión v4 · Corte de datos: 2026-07-14*

---

## Resumen en Una Frase

No fue posible determinar la indicación original ni el mecanismo de acción de Reslizumab a partir de las fuentes consultadas (DrugBank, PubMed) — ambos campos figuran como brecha de datos en este Evidence Pack.
El modelo TxGNN predice dos posibles direcciones de reposicionamiento: **Trombocitopenia por Destrucción Inmune** (puntaje 99.53%) y **Trastorno Primario de Liberación Plaquetaria** (puntaje 99.25%).
Actualmente **no existe ningún ensayo clínico** que respalde ninguna de las dos indicaciones, y solo se dispone de **1 publicación indirecta** (una revisión sobre síndrome hipereosinofílico) relacionada con la segunda hipótesis.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en las fuentes consultadas (DrugBank/PubMed no reportaron indicación registrada) |
| Nueva Indicación Predicha | Trombocitopenia por Destrucción Inmune |
| Puntaje de Predicción TxGNN | 99.53% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Taiwán | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de Reslizumab, ni de su indicación original registrada en las fuentes consultadas (DrugBank, PubMed). Esto impide realizar un análisis de correlación mecanística riguroso y limita la interpretación de ambas hipótesis a lo que el propio paquete de evidencia documenta como racional de reposicionamiento.

**Candidato 1 — Trombocitopenia por Destrucción Inmune (rank 1):** el racional documentado en el Evidence Pack señala que la fisiopatología de esta enfermedad (autoanticuerpos contra glucoproteínas plaquetarias como GPIIb/IIIa, aclaramiento mediado por receptores Fc en el bazo, eje de linfocitos B/autoanticuerpos) **no tiene relación mecanística conocida** con el eje IL-5/eosinófilos. El propio análisis incluido en el paquete concluye que esta predicción es, con alta probabilidad, **ruido derivado de similitud de embeddings en el modelo TxGNN**, y no una señal biológica real. Esta predicción debe interpretarse con cautela reforzada.

**Candidato 2 — Trastorno Primario de Liberación Plaquetaria (rank 2):** la única literatura disponible discute el síndrome hipereosinofílico (SHE) y su tratamiento con mepolizumab (un anti-IL-5 distinto de reslizumab). El vínculo es, por tanto, una inferencia indirecta de "efecto de clase" (fármacos anti-IL-5 podrían mejorar anomalías hematológicas asociadas al SHE), no evidencia específica de reslizumab ni de este trastorno plaquetario en particular.

En ambos casos, la ausencia de datos sobre el mecanismo de acción original impide confirmar o descartar plausibilidad biológica con solidez.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para ninguna de las dos indicaciones predichas (Trombocitopenia por Destrucción Inmune ni Trastorno Primario de Liberación Plaquetaria).

---

## Evidencia de Literatura

**Candidato 1 — Trombocitopenia por Destrucción Inmune:** actualmente no hay literatura relacionada disponible.

**Candidato 2 — Trastorno Primario de Liberación Plaquetaria:**

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [20565230](https://pubmed.ncbi.nlm.nih.gov/20565230/) | 2010 | Revisión | Current Medical Research and Opinion | Estrategias de manejo del síndrome hipereosinofílico, incluyendo mepolizumab, orientadas a reducir la eosinofilia y prevenir el daño a órganos por infiltración eosinofílica; no evalúa reslizumab ni el trastorno plaquetario de forma directa |

---

## Información de Mercado en Taiwán

Reslizumab no está comercializado en Taiwán (0 autorizaciones registradas), por lo que no existe información de producto, forma farmacéutica ni indicación aprobada localmente disponible en este momento.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. (No se localizó el prospecto/ficha técnica de TFDA ni datos de interacciones farmacológicas en las fuentes consultadas; esta brecha está clasificada como bloqueante para la evaluación de seguridad S1.)

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ninguna de las dos indicaciones predichas cuenta con ensayos clínicos de respaldo, y la evidencia de literatura se limita a una única revisión indirecta (efecto de clase, no específica de reslizumab). El propio racional de reposicionamiento identifica el candidato de mayor puntaje como probable ruido del modelo. Con un nivel de evidencia L5/L4 y ausencia de datos de MOA e indicación original, no existe base suficiente para avanzar a etapas de evaluación posteriores.

**Para avanzar se necesita:**
- Obtener el mecanismo de acción (MOA) de Reslizumab vía API de DrugBank (DG002)
- Obtener el prospecto/ficha técnica de TFDA con advertencias y contraindicaciones (DG001, bloqueante para S1)
- Confirmar la(s) indicación(es) original(es) aprobada(s) del fármaco
- Búsqueda dirigida de literatura y ensayos clínicos específicos de reslizumab para ambas indicaciones candidatas, para distinguir señal biológica real de artefacto del modelo
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

