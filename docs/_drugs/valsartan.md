---
layout: default
title: Valsartan
parent: Evidencia moderada (L3-L4)
nav_order: 838
evidence_level: L4
indication_count: 6
last_modified_at: 2026-10-31
monitor_inn: "valsartan"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease", "Prinzmetal angina"]
description: "Valsartan: nueva indicación predicha, Malignant hypertensive renal disease (nivel de evidencia L4). Indicación original: No consta en los datos locales"
---

# Valsartan
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **6** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Valsartan: Malignant hypertensive renal disease
{: .text-alpha }

## Resumen en Una Frase

Valsartán es un antagonista del receptor de angiotensina II tipo 1 (AT1), originalmente utilizado para el tratamiento de la hipertensión arterial.
El modelo TxGNN predice que podría ser efectivo para **hipertensión renovascular maligna**,
pero actualmente solo existe **1 publicación preclínica** (estudio en animales) y **ningún ensayo clínico** que respalde esta dirección. Además, la indicación está muy cerca de la ya existente, por lo que no constituye un reposicionamiento genuino.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Malignant hypertensive renal disease |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 18) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, valsartán es un bloqueador del receptor AT1 de angiotensina II, su eficacia en hipertensión está comprobada y, mecanísticamente, podría ser aplicable a la hipertensión maligna.

La hipertensión maligna se asocia en parte con la activación del sistema renina-angiotensina (SRA), por lo que el bloqueo de AT1 es biológicamente plausible. La única publicación disponible (PMID 11560862, 2001) es un estudio preclínico en el que el bloqueo del receptor AT1 previno la hipertensión maligna letal en ratas, incluso con relación a la inflamación renal. Es una evidencia indirecta y no demuestra eficacia clínica de valsartán en humanos.

Cabe destacar que esta indicación es muy cercana a la hipertensión ya autorizada, por lo que el puntaje alto del modelo refleja sobre todo proximidad en la red de conocimiento y no un hallazgo nuevo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11560862](https://pubmed.ncbi.nlm.nih.gov/11560862/) | 2001 | Preclínico (animal) | Circulation | El bloqueo del receptor AT1 de angiotensina II previno la hipertensión maligna letal, con relación a la inflamación renal |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 72942 | Valsartan Sandoz 160 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos |
| 70360 | Valsartan Normon 80 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos |
| 72385 | Diovan 3 mg/ml solución oral | Solución oral | No disponible en los datos |
| 66910 | Diovan Cardio 40 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos |
| 77990 | Presar 320 mg comprimidos bucodispersables EFG | Comprimido bucodispersable | No disponible en los datos |

Se muestran 5 de las 20 autorizaciones vigentes (todas de monofármaco, ninguna cancelada).

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no provienen del texto del prospecto): insuficiencia hepática y enfermedad hepática, pancreatitis, enfermedad de la vesícula biliar, angioedema (incluido el hereditario y el inducido por bloqueantes del SRA), lupus eritematoso sistémico, deficiencia de potasio, diabetes mellitus y cetoacidosis diabética, neutropenia y agranulocitosis, trastornos hipotensivos, hiperparatiroidismo, hipercalcemia, nefrocalcinosis, gota, anuria, obstrucción de la arteria renal y deterioro de la función renal.
- **Interacciones farmacológicas**: se identificaron 254 interacciones. Las de nivel **mayor** incluyen **cloruro de potasio** y **bicarbonato de potasio** (riesgo de hiperpotasemia). Entre las de nivel moderado figuran hidrocortisona, exenatida, eluxadolina, polietilenglicol con electrolitos y múltiples insulinas.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única evidencia es un estudio preclínico indirecto, sin ensayos clínicos, y la indicación predicha es prácticamente una variante de la hipertensión ya autorizada, por lo que aporta poco valor como reposicionamiento.

**Para avanzar se necesita:**
- Estudios clínicos que evalúen directamente valsartán en hipertensión renovascular o maligna.
- Descargar y analizar el prospecto de la AEMPS (advertencias y contraindicaciones oficiales), pendiente para la revisión de seguridad.
- Datos detallados del mecanismo de acción (MOA) desde DrugBank.
- Aclarar si la indicación ya queda cubierta por la ficha técnica actual, lo que anularía la necesidad de reposicionamiento.
- Plan de vigilancia de potasio y función renal, dadas las interacciones y contraindicaciones identificadas.

---

**Nota sobre otras predicciones:** el modelo también predijo hipertensión pulmonar por enfermedad pulmonar/hipoxia (L4, solo evidencia preclínica indirecta, con línea de investigación abierta), cardiopatía pulmonar crónica (L4, evidencia mayoritariamente de sacubitrilo/valsartán en insuficiencia cardíaca, no de valsartán solo), y otras (nefropatía hipertensiva maligna, síndrome de Braddock, angina de Prinzmetal, hipertensión pulmonar multifactorial) sin evidencia directa (L4–L5, Hold).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

