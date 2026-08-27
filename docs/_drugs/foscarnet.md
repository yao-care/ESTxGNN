---
layout: default
title: Foscarnet
parent: 僅模型預測 (L5)
nav_order: 125
evidence_level: L5
indication_count: 4
---

# Foscarnet
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

# Foscarnet: De Infecciones Virales Resistentes a Síndrome HANAC (Hematuria Familiar con Tortuosidad Arteriolar Retiniana y Contracturas)

## Resumen en Una Frase

Foscarnet es un antiviral utilizado clásicamente en infecciones graves por citomegalovirus (CMV), herpes simple (HSV) y varicela-zóster (VZV) resistentes a otros antivirales, aunque actualmente no está comercializado en España y su indicación registrada no consta en este evidence pack. El modelo TxGNN predice que podría ser efectivo para el **síndrome de hematuria familiar autosómica dominante con tortuosidad arteriolar retiniana y contracturas (síndrome HANAC, asociado a COL4A1)**, con una puntuación del **99,56%**, pero actualmente **0 ensayos clínicos** y **0 publicaciones** respaldan esta dirección, lo que sugiere una señal de baja confiabilidad.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en el registro español (fármaco no comercializado en España) |
| Nueva Indicación Predicha | Síndrome HANAC (hematuria familiar, tortuosidad arteriolar retiniana y contracturas) |
| Puntaje de Predicción TxGNN | 99,56% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción documentados en este evidence pack. Según la información farmacológica conocida, foscarnet es un análogo del pirofosfato inorgánico que inhibe directamente la ADN polimerasa viral (y la transcriptasa inversa) sin necesitar activación previa por timidina quinasa, lo que lo hace útil en infecciones por CMV/HSV/VZV resistentes a aciclovir o ganciclovir.

El síndrome HANAC es un trastorno hereditario del colágeno tipo IV (COL4A1/COL4A3) que provoca fragilidad estructural de la membrana basal vascular y glomerular. No existe relación fisiopatológica conocida entre la inhibición de la replicación viral y un defecto estructural congénito del colágeno, por lo que no hay una base mecanística que sustente esta predicción.

La puntuación de TxGNN es alta (99,56%), pero corresponde a la posición 7.190 del ranking global del modelo, y no cuenta con ningún ensayo clínico ni publicación de respaldo. El propio análisis de razonabilidad incluido en el evidence pack clasifica esta asociación como probable ruido del modelo (falso positivo), derivado de proximidad en el espacio de embeddings más que de una relación biológica real.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Consideraciones de Seguridad

> Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La puntuación alta de TxGNN no está respaldada por ningún ensayo clínico ni publicación, y no existe plausibilidad mecanística entre la inhibición de la ADN polimerasa viral y un trastorno hereditario del colágeno vascular. El propio evidence pack identifica esta asociación como probable falso positivo del modelo.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank — actualmente ausentes
- Ficha técnica/prospecto de TFDA con advertencias y contraindicaciones — brecha bloqueante para cualquier evaluación de seguridad (S1)
- Evidencia biológica o clínica independiente que vincule foscarnet con trastornos del colágeno tipo IV, antes de reconsiderar esta dirección

**Nota adicional:** los otros 3 candidatos evaluados en este mismo evidence pack (artritis reumatoide, nefropatía diabética, enfermedad de vasos pequeños cerebrales) también recibieron recomendación Hold — en dos casos por error de emparejamiento en base de datos (ensayo de brolucizumab en DMAE, no relacionado con foscarnet) y en el tercero por ausencia de literatura que evalúe directamente foscarnet en la indicación propuesta.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

