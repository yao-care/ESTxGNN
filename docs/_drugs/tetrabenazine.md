---
layout: default
title: Tetrabenazine
parent: Solo predicción del modelo (L5)
nav_order: 784
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tetrabenazine: nueva indicación predicha, Enfermedad renal poliquística tipo 3 con o sin enfermedad hepática po… (nivel de evidencia L5). Indicación original: Enfermedad de Huntington (según el grafo…"
monitor_inn: "Tetrabenazine"
predicted_indications: ["polycystic kidney disease 3 with or without polycystic liver disease", "renal-hepatic-pancreatic dysplasia", "Joubert syndrome with renal defect", "karyomegalic interstitial nephritis", "thoracic malformation", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "acute intermittent porphyria", "adult familial nephronophthisis-spastic quadriparesia syndrome", "atypical glycine encephalopathy", "congenital disorder of glycosylation with defective fucosylation"]
---

# Tetrabenazine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Tetrabenazina: De Enfermedad de Huntington a Enfermedad Renal Poliquística Tipo 3 (con o sin Enfermedad Hepática Poliquística)

## Resumen en Una Frase

Tetrabenazina es un inhibidor del transportador vesicular de monoaminas, utilizado originalmente para el tratamiento sintomático de trastornos hipercinéticos como la corea de la enfermedad de Huntington.
El modelo TxGNN predice que podría ser efectivo para la **enfermedad renal poliquística tipo 3 con o sin enfermedad hepática poliquística**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Huntington (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Enfermedad renal poliquística tipo 3 con o sin enfermedad hepática poliquística |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, tetrabenazina es un inhibidor reversible del transportador vesicular de monoaminas tipo 2 (VMAT2), que agota las monoaminas presinápticas en el sistema nervioso central. Los datos de farmacología confirman que se une a VMAT1 (SLC18A1) y VMAT2 (SLC18A2).

La indicación original (corea de Huntington y otros trastornos hipercinéticos) es un trastorno neurológico del movimiento. La nueva indicación predicha es una enfermedad genética relacionada con ciliopatías, caracterizada por la formación de quistes renales y hepáticos. **No se identifica ningún vínculo mecanístico plausible** entre ambas: la inhibición de VMAT2 actúa sobre la neurotransmisión monoaminérgica y no sobre la formación de quistes.

El puntaje elevado del modelo parece ser un artefacto del grafo de conocimiento y no una justificación biológica. Esta predicción debe considerarse puramente computacional.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 84164 | Tetrabenazina Aristo 25 mg comprimidos EFG | Comprimido | No disponible en los datos compilados |
| 82080 | Tetrabenazina Sun 25 mg comprimidos EFG | Comprimido | No disponible en los datos compilados |
| 70142 | Nitoman 25 mg comprimidos | Comprimido | No disponible en los datos compilados |
| 72730 | Tetmodis 25 mg comprimidos EFG | Comprimido | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo según el grafo de conocimiento** (no provienen del prospecto): atrofia multisistémica, síndrome de taquicardia postural ortostática, hipotensión ortostática y trastornos hipotensivos, síndrome de QT largo (incluida la forma familiar) y torsades de pointes, trastornos de ansiedad, trastorno neurótico, trastorno distímico, enfermedad hepática, enfermedad de la vesícula biliar, discinesia tardía, discinesia linguo-facial-bucal, parkinsonismo y enfermedad de Parkinson, acatisia inducida por fármacos e hiperprolactinemia (incluidas las formas familiar, adquirida y por tumor hipofisario productor de prolactina).
- **Interacciones farmacológicas**: los datos disponibles solo describen la unión a los transportadores VMAT1 y VMAT2; no hay interacciones fármaco-fármaco clínicas listadas.

Consultar el prospecto para el resto de la información de seguridad (advertencias y contraindicaciones oficiales).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y sin ningún vínculo mecanístico plausible entre la inhibición de VMAT2 y la enfermedad renal poliquística. Además, el perfil de seguridad del fármaco (por ejemplo, riesgo de depresión, QT largo y enfermedad hepática) no justifica avanzar sin una base biológica.

**Para avanzar se necesita:**
- Datos oficiales de advertencias y contraindicaciones del prospecto de la AEMPS
- Datos del mecanismo de acción (MOA) desde DrugBank
- Evidencia preclínica que demuestre una relación entre la vía monoaminérgica/VMAT2 y la quistogénesis renal o hepática
- Textos de indicación aprobada de las autorizaciones españolas para confirmar la indicación original
- Reevaluación de las demás predicciones de mayor puntaje, que tampoco cuentan con evidencia clínica, solo si surge una hipótesis biológica sólida
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

