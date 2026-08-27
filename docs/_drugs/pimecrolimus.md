---
layout: default
title: Pimecrolimus
parent: 僅模型預測 (L5)
nav_order: 222
evidence_level: L5
indication_count: 4
---

# Pimecrolimus
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Pimecrolimus: De Dermatitis Atópica a Dermatitis Seborreica

## Resumen en Una Frase

Pimecrolimus es un inhibidor tópico de la calcineurina, originalmente indicado como tratamiento de segunda línea para la dermatitis atópica leve a moderada. El modelo TxGNN predice que podría ser efectivo para **Dermatitis Seborreica**, con **1 ensayo clínico** y **18 publicaciones** que actualmente respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dermatitis atópica leve a moderada (uso de segunda línea) |
| Nueva Indicación Predicha | Dermatitis Seborreica |
| Puntaje de Predicción TxGNN | 99.73% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos estructurados sobre el mecanismo de acción de pimecrolimus en la ficha del fármaco. Según la evidencia recopilada, pimecrolimus es una macrolactama derivada de ascomicina que actúa como inhibidor selectivo de la calcineurina: inhibe la activación y proliferación de linfocitos T, reduce la producción y liberación de citocinas inflamatorias (IL-2, IL-4, interferón-gamma, TNF-alfa) e inhibe la degranulación de mastocitos. Su eficacia en dermatitis atópica leve a moderada está ampliamente comprobada.

La dermatitis seborreica comparte con la dermatitis atópica un componente fisiopatológico común: una respuesta inflamatoria cutánea mediada por queratinocitos y linfocitos T, en este caso desencadenada por la colonización de *Malassezia* spp. Dado que el efecto antiinflamatorio de pimecrolimus no depende de un mecanismo antifúngico específico sino de la modulación de la vía inflamatoria T-celular, su extrapolación mecanística a la dermatitis seborreica es razonable.

Esta hipótesis ya cuenta con respaldo clínico consolidado: existe un ensayo clínico de Fase 2 dirigido específicamente a esta indicación, junto con múltiples revisiones sistemáticas (incluyendo revisiones sistemáticas de ensayos aleatorizados) que documentan su uso off-label en dermatitis seborreica facial y de cuero cabelludo desde hace más de una década.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00403559](https://clinicaltrials.gov/study/NCT00403559) | Fase 2 | Completado | 113 | Estudio exploratorio aleatorizado, doble ciego, de grupos paralelos con comparador activo (Elidel) de 4 semanas de duración para evaluar la eficacia de pimecrolimus en el tratamiento de la dermatitis seborreica |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34910320](https://pubmed.ncbi.nlm.nih.gov/34910320/) | 2022 | ECA | Clinical and Experimental Dermatology | Ensayo aleatorizado ciego que compara crema de pimecrolimus 1% frente a sertaconazol 2% en dermatitis seborreica facial |
| [22142161](https://pubmed.ncbi.nlm.nih.gov/22142161/) | 2012 | Revisión Sistemática de ECA | Expert Review of Clinical Pharmacology | Pimecrolimus 1% resulta bien tolerado y eficaz frente a corticosteroides, antimicóticos o placebo en dermatitis seborreica |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Revisión Sistemática | American Journal of Clinical Dermatology | Revisión sistemática del tratamiento tópico de la dermatitis seborreica facial, incluyendo inhibidores de calcineurina |
| [36072203](https://pubmed.ncbi.nlm.nih.gov/36072203/) | 2022 | Revisión Sistemática | Cureus | Revisión sistemática de ECA sobre eficacia y seguridad de pimecrolimus en dermatitis seborreica facial |
| [18677657](https://pubmed.ncbi.nlm.nih.gov/18677657/) | 2009 | Estudio comparativo abierto | Journal of Dermatological Treatment | Estudio prospectivo aleatorizado que compara pimecrolimus 1% con ketoconazol 2% en dermatitis seborreica |
| [23715821](https://pubmed.ncbi.nlm.nih.gov/23715821/) | 2013 | Estudio comparativo | Irish Journal of Medical Science | Comparación de sertaconazol 2% frente a pimecrolimus 1% en el tratamiento de dermatitis seborreica |
| [15700745](https://pubmed.ncbi.nlm.nih.gov/15700745/) | 2004 | Estudio clínico | Drugs Under Experimental and Clinical Research | Pimecrolimus crema 1% como tratamiento eficaz para dermatitis seborreica de cara y tronco |
| [20000875](https://pubmed.ncbi.nlm.nih.gov/20000875/) | 2010 | Estudio abierto | American Journal of Clinical Dermatology | Pimecrolimus 1% en dermatitis seborreica facial resistente a otros tratamientos |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Revisión | Journal of Drugs in Dermatology | Estado actual y horizontes terapéuticos de la dermatitis seborreica facial, incluyendo inhibidores de calcineurina |
| [16033622](https://pubmed.ncbi.nlm.nih.gov/16033622/) | 2005 | Revisión | International Journal of Clinical Practice | Revisión del uso de pimecrolimus en dermatología más allá de la dermatitis atópica |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ensayo clínico de Fase 2 completado dirigido específicamente a dermatitis seborreica, respaldado por al menos un ECA adicional y múltiples revisiones sistemáticas que confirman consistentemente la eficacia de pimecrolimus frente a comparadores activos (ketoconazol, sertaconazol). La evidencia corresponde a nivel L2, suficiente para avanzar con condiciones, pero no para una recomendación Go sin reservas.

**Para avanzar se necesita:**
- Advertencias y contraindicaciones del prospecto (TFDA/AEMPS) — actualmente bloqueante para la evaluación de seguridad S1 (DG001)
- Datos detallados del mecanismo de acción (MOA) desde DrugBank (DG002)
- Confirmación de vías de administración disponibles y compatibilidad con formulación tópica ya existente
- Dado que el fármaco no está comercializado en España, evaluar viabilidad regulatoria de importación o solicitud de autorización antes de cualquier desarrollo clínico local
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

