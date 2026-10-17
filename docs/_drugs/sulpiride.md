---
layout: default
title: Sulpiride
parent: Evidencia moderada (L3-L4)
nav_order: 754
evidence_level: L4
indication_count: 9
last_modified_at: 2026-10-14
description: "Sulpiride: nueva indicación predicha, Distrofia retiniana con o sin anomalías extraoculares (nivel de evidencia L4). Indicación original: Esquizofrenia (según el grafo de conocimiento de TxGNN"
monitor_inn: "Sulpiride"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "hydranencephaly (disease)", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "myopia X-linked", "congenital disorder of glycosylation with defective fucosylation", "myopia 26, X-linked, female-limited", "syndromic myopia", "atypical glycine encephalopathy"]
---

# Sulpiride
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **9** 
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

# Sulpirida: De Esquizofrenia a Distrofia Retiniana con o sin Anomalías Extraoculares

## Resumen en Una Frase

Sulpirida es un antagonista selectivo de los receptores de dopamina D2/D3, originalmente utilizado para el tratamiento de la esquizofrenia.
El modelo TxGNN predice que podría ser efectivo para **distrofia retiniana con o sin anomalías extraoculares**,
pero actualmente solo cuenta con **2 estudios preclínicos** (sin ensayos clínicos) que respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Esquizofrenia (según el grafo de conocimiento de TxGNN; los textos de indicación de las autorizaciones españolas están vacíos) |
| Nueva Indicación Predicha | Distrofia retiniana con o sin anomalías extraoculares |
| Puntaje de Predicción TxGNN | 99.95% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Sulpirida es un antagonista selectivo de los receptores de dopamina D2 y D3, con baja afinidad por el receptor D4. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción, pero sí señalan esta actividad farmacológica sobre DRD2 y DRD3. En la esquizofrenia, el bloqueo de D2 es la base de su efecto terapéutico.

La relación con la nueva indicación es indirecta. La dopamina participa en la modulación de las respuestas a la luz de las células ganglionares de la retina. En el modelo de rata P23H de retinitis pigmentosa, el sistema dopaminérgico retiniano parece estar alterado. Dos estudios preclínicos (2015 y 2016) indican que los antagonistas D2, entre ellos la sulpirida, podrían mejorar las respuestas visuales de estas células, aumentando su sensibilidad a la luz.

Esto aporta plausibilidad mecanística, pero **no** constituye evidencia de un efecto modificador de la enfermedad en distrofias retinianas hereditarias. El puntaje tan alto de TxGNN es únicamente una predicción computacional. No existen datos en humanos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27788033](https://pubmed.ncbi.nlm.nih.gov/27788033/) | 2016 | Preclínico (animal/electrofisiología) | J Ocul Pharmacol Ther | En el modelo de rata P23H de retinitis pigmentosa, los antagonistas D2 (sulpirida y eticloprida) parecen mejorar las respuestas visuales de las células ganglionares. Se evaluó si haloperidol y clozapina producen efectos similares. |
| [26717015](https://pubmed.ncbi.nlm.nih.gov/26717015/) | 2015 | Preclínico (animal/electrofisiología) | PLoS One | Se estudiaron los efectos de antagonistas de receptores D2-like sobre las respuestas a la luz de las células ganglionares en retinas de rata normales y P23H, en un contexto de disfunción dopaminérgica retiniana. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 51836 | PSICOCEN 50 mg CÁPSULAS | Cápsula dura | No disponible en los datos compilados |
| 48557 | DOGMATIL 50 mg/ml SOLUCIÓN INYECTABLE | Solución inyectable | No disponible en los datos compilados |
| 48558 | DOGMATIL FUERTE 200 mg COMPRIMIDOS | Comprimido | No disponible en los datos compilados |
| 73195 | SULPIRIDA KERN PHARMA 50 mg CÁPSULAS EFG | Cápsula dura | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Interacciones y dianas farmacológicas**: los datos compilados describen actividad sobre los receptores D2 y D3 (diana principal) y sobre las anhidrasas carbónicas 1, 7 y 12. No se dispone de una lista de interacciones con otros fármacos y su nivel de gravedad no está especificado.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en dos estudios preclínicos en ratas, sin ensayos clínicos ni evidencia en humanos. La indicación es una distrofia retiniana hereditaria, para la que los datos actuales no demuestran un efecto modificador de la enfermedad. Se mantiene como pregunta de investigación.

Las demás predicciones del modelo (hidranencefalia, polimicrogiria, Charcot-Marie-Tooth 1G, miopías, defecto de glicosilación y encefalopatía glicínica atípica) carecen de ensayos y literatura y de un vínculo mecanístico identificable. Para las miopías, el antagonismo D2 sería direccionalmente desfavorable, y todas quedan en Hold con nivel L5.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción
- Advertencias y contraindicaciones del prospecto de la AEMPS (actualmente sin datos)
- Textos de indicación aprobada de las autorizaciones españolas
- Estudios preclínicos adicionales que confirmen un efecto sobre la función o la degeneración retiniana, y no solo sobre respuestas electrofisiológicas
- Evaluación de la vía de administración y de la seguridad ocular antes de plantear estudios clínicos
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

