---
layout: default
title: Pitolisant
parent: 僅模型預測 (L5)
nav_order: 225
evidence_level: L5
indication_count: 3
---

# Pitolisant
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Pitolisant: De Narcolepsia a Insomnio

## Resumen en Una Frase

Pitolisant es un agonista inverso selectivo del receptor de histamina H3, aprobado en la Unión Europea y EE. UU. para narcolepsia (con o sin cataplejía) y para la somnolencia diurna excesiva asociada a apnea obstructiva del sueño (OSA). El modelo TxGNN predice que podría ser efectivo para **Insomnio**, pero esta dirección solo cuenta actualmente con **1 ensayo clínico retirado (0 participantes reclutados)** y **8 publicaciones**, ninguna de las cuales estudia pitolisant específicamente en insomnio. Al tratarse de un fármaco promotor de la vigilia, esta predicción presenta una contradicción mecanística relevante que debe señalarse explícitamente.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Narcolepsia (con o sin cataplejía) — según literatura incluida en este informe; no confirmada por ficha técnica local, ya que el fármaco no está comercializado |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.71% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos estructurados sobre el mecanismo de acción de pitolisant en la fuente DrugBank consultada. Según la literatura incluida en este informe, pitolisant es un agonista inverso selectivo del receptor de histamina H3 (H3R) que bloquea los autorreceptores H3 presinápticos, aumentando la liberación de histamina y de otros neurotransmisores promotores de la vigilia (noradrenalina, acetilcolina) en el cerebro. Este mecanismo lo convierte en un fármaco **promotor de la vigilia**, motivo por el cual está aprobado para narcolepsia con o sin cataplejía y se ha estudiado ampliamente para la somnolencia diurna excesiva (EDS) asociada a OSA.

La indicación predicha por TxGNN, insomnio, es fisiopatológicamente opuesta a la indicación original: el insomnio se caracteriza por dificultad para conciliar o mantener el sueño, mientras que pitolisant actúa incrementando la vigilia y el estado de alerta. No existe, por tanto, una relación mecanística de refuerzo entre ambas indicaciones, sino una contradicción direccional. El único ensayo localizado (NCT02800083) no estudiaba insomnio como variable primaria, sino el trastorno por consumo de alcohol, y fue retirado antes de reclutar ningún participante (enrollment = 0), por lo que no aporta evidencia real.

En conjunto, la ausencia de un fundamento mecanístico coherente, sumada a la falta de literatura que estudie pitolisant específicamente en insomnio, sugiere que esta predicción de TxGNN es probablemente un **falso positivo**, posiblemente originado por una confusión del modelo entre distintas categorías de trastornos del sueño en el espacio de embeddings de enfermedades.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02800083](https://clinicaltrials.gov/study/NCT02800083) | Fase 2 | Retirado | 0 | Diseñado para evaluar pitolisant en trastorno por consumo de alcohol (no insomnio); retirado antes de reclutar pacientes, sin datos generados |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36931805](https://pubmed.ncbi.nlm.nih.gov/36931805/) | 2023 | ECA | Lancet Neurol | Seguridad y eficacia de pitolisant en niños ≥6 años con narcolepsia con/sin cataplejía (fase 3) |
| [33121980](https://pubmed.ncbi.nlm.nih.gov/33121980/) | 2021 | ECA | Chest | Pitolisant redujo la somnolencia diurna residual en pacientes con OSA adherentes a CPAP |
| [31917607](https://pubmed.ncbi.nlm.nih.gov/31917607/) | 2020 | ECA | Am J Respir Crit Care Med | Pitolisant mejoró la somnolencia diurna en OSA moderada-grave que rechazaba CPAP |
| [36169322](https://pubmed.ncbi.nlm.nih.gov/36169322/) | 2022 | Cohorte (mundo real) | Rev Neurol | Estudio WAKE: efectividad y seguridad de pitolisant en narcolepsia tipo 1 refractaria |
| [34225942](https://pubmed.ncbi.nlm.nih.gov/34225942/) | 2021 | Revisión | Handb Clin Neurol | Panorama de receptores de histamina (H1-H4) en salud y enfermedad, incluido el sistema H3 en el SNC |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Revisión | Drug Des Devel Ther | Perfil de pitolisant en el manejo de narcolepsia: diseño, desarrollo y lugar en la terapia |
| [34521328](https://pubmed.ncbi.nlm.nih.gov/34521328/) | 2022 | Revisión | Curr Neuropharmacol | Cambios del sistema histaminérgico en trastornos neuropsiquiátricos y posibles consecuencias terapéuticas |
| [22356925](https://pubmed.ncbi.nlm.nih.gov/22356925/) | 2012 | Revisión | Clin Neuropharmacol | Pitolisant como estimulante alternativo en adolescentes con narcolepsia-cataplejía refractaria |

> Ninguna de las publicaciones anteriores estudia pitolisant en insomnio; todas se centran en narcolepsia u OSA/EDS.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Otras Indicaciones Predichas por TxGNN (Resumen)

Este Evidence Pack es multi-indicación. Se registran aquí las otras dos direcciones predichas para pitolisant, con menor prioridad que insomnio, para trazabilidad completa:

| Rank | Indicación | Score TxGNN | Nivel de Evidencia | Etapa | Recomendación | Resumen |
|---|---|---|---|---|---|---|
| 2 | TDAH (Trastorno por Déficit de Atención e Hiperactividad) | 99.36% | L4 | S1 | Research Question | El agonismo inverso H3 aumenta histamina/noradrenalina/acetilcolina prefrontal, con relación mecanística indirecta plausible con la fisiopatología del TDAH; sin embargo, no hay ningún ensayo clínico de pitolisant específico para TDAH — solo evidencia de clase (7 publicaciones de revisión/farmacología). |
| 3 | Síndrome faciodigitogenital (Aarskog-Scott) | 99.29% | L5 | S0 | Hold | Sin ensayos clínicos ni literatura disponible. Trastorno genético ligado al X (mutación FGD1) sin relación fisiopatológica conocida con el sistema H3. Interpretado como ruido del modelo. |

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- La predicción de TxGNN para insomnio presenta una contradicción mecanística direccional (fármaco promotor de la vigilia frente a una indicación que requiere sedación/inducción del sueño), y la única evidencia clínica disponible (NCT02800083) fue retirada sin reclutar pacientes, por lo que no hay respaldo clínico ni mecanístico suficiente para avanzar.

**Para avanzar se necesita:**
- Resolver la brecha de datos bloqueante sobre advertencias/contraindicaciones del prospecto (TFDA/AEMPS) antes de cualquier evaluación de seguridad S1
- Obtener datos estructurados del mecanismo de acción desde DrugBank para confirmar o descartar la contradicción direccional descrita
- Confirmar con el equipo de modelado si esta asociación corresponde a un falso positivo por confusión de categorías de trastornos del sueño en el embedding
- Si se desea explorar el espacio de indicaciones relacionadas con el sueño, priorizar hipótesis con coherencia mecanística (p. ej., hipersomnia o EDS residual) en lugar de insomnio
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

