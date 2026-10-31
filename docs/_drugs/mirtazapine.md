---
layout: default
title: Mirtazapine
parent: Solo predicción del modelo (L5)
nav_order: 533
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-31
monitor_inn: "Mirtazapine"
predicted_indications: ["Ohdo syndrome and variants", "blepharophimosis - intellectual disability syndrome, Ohdo type", "benign paroxysmal torticollis of infancy"]
description: "Mirtazapine: nueva indicación predicha, Síndrome de Ohdo y variantes (Ohdo syndrome and variants) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Mirtazapine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Mirtazapine: Síndrome de Ohdo y variantes (Ohdo syndrome and variants)
{: .text-alpha }

## Resumen en Una Frase

Mirtazapina es un antidepresivo utilizado originalmente para el tratamiento de la depresión (depresión unipolar, depresión endógena, trastorno depresivo mayor) y los trastornos de ansiedad.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de Ohdo y variantes**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Síndrome de Ohdo y variantes (Ohdo syndrome and variants) |
| Puntaje de Predicción TxGNN | 0.9942 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 15) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, mirtazapina es un antidepresivo noradrenérgico y serotoninérgico específico. Los datos de farmacología recopilados indican que tiene la mayor afinidad por los adrenoceptores α2 (2A > 2C > 2B) y por los receptores serotoninérgicos 5-HT2A y 5-HT2C, lo que sustenta su eficacia en la depresión mayor.

El síndrome de Ohdo es un trastorno genético raro (asociado a KAT6B) que implica la regulación de la cromatina. Con los datos disponibles **no se puede establecer un vínculo mecanístico** entre la acción de la mirtazapina sobre receptores monoaminérgicos y la fisiopatología de esta enfermedad. El puntaje del modelo es muy alto, pero es solo una predicción computacional.

Además, la segunda predicción (síndrome de blefarofimosis con discapacidad intelectual, tipo Ohdo; 0,9911) probablemente corresponde a la misma entidad o a una muy cercana; el puntaje proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica, por lo que ambas predicciones no son independientes y no deben contarse como apoyos separados. La tercera (tortícolis paroxística benigna de la infancia; 0,9911) solo tiene una conexión especulativa con variantes de migraña y canalopatías, y afecta a población lactante, para la cual mirtazapina no está establecida.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones vigentes (todas de medicamentos de un solo principio activo; el texto de indicación aprobada no está disponible en los datos compilados).

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 90891 | Mirtazapina Stada 45 mg EFG | Comprimido recubierto con película | Laboratorio Stada S.L. |
| 71841 | Mirtazapina Flas Kern Pharma 15 mg EFG | Comprimido bucodispersable | Kern Pharma S.L. |
| 89479 | Mirtazapina Sandoz 30 mg EFG | Comprimido recubierto con película | Sandoz Farmacéutica S.A. |
| 69802 | Mirtazapina Qualigen 15 mg EFG | Comprimido recubierto con película | Neuraxpharm Spain S.L. |
| 66985 | Afloyan 15 mg | Comprimido recubierto con película | Laboratorios Alter S.A. |

## Consideraciones de Seguridad

- **Contraindicaciones o condiciones de precaución según el grafo de conocimiento** (no proceden del texto del prospecto): síndrome de serotonina, acatisia inducida por fármacos, epilepsia, trastorno bipolar maníaco, hepatopatía, enfermedad de la vesícula biliar, neutropenia, agranulocitosis, deterioro de la función renal, hipotensión ortostática y otros trastornos hipotensivos, atrofia multisistémica, síndrome de taquicardia postural ortostática, hipertrigliceridemia, obesidad, ictus y trastornos cerebrovasculares, infarto de miocardio y trombosis coronaria, y hemoglobinopatías.
- **Interacciones farmacológicas / dianas farmacológicas**: la consulta se completó con 5 registros, que corresponden a dianas farmacológicas y no a interacciones con otros fármacos: receptores 5-HT2A, 5-HT2C y adrenoceptores α2A, α2B y α2C. Se señala que la combinación con otros antidepresivos (ISRS, IRSN) cuenta con cierto respaldo clínico en depresión grave, pero conviene vigilar el riesgo de síndrome serotoninérgico.

Las advertencias y contraindicaciones oficiales del prospecto de la AEMPS no están disponibles; consultar el prospecto para la información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el puntaje del modelo (nivel L5), sin ensayos clínicos, literatura ni vínculo mecanístico plausible con una enfermedad genética rara de regulación de la cromatina. Las predicciones principales se solapan entre sí y la tercera implica población pediátrica, lo que añade barreras de seguridad.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA) y análisis de su relación con la vía de KAT6B/regulación de la cromatina
- Estudios preclínicos o de mecanismo que justifiquen la hipótesis
- Revisión sistemática de literatura y de registros de ensayos clínicos para el síndrome de Ohdo
- Obtención y análisis del prospecto de la AEMPS (advertencias y contraindicaciones) para el cribado de seguridad
- Evaluación de la compatibilidad de vías de administración y de la viabilidad en poblaciones pediátricas
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

