---
layout: default
title: Amiloride
parent: Solo predicción del modelo (L5)
nav_order: 50
evidence_level: L5
indication_count: 5
monitor_inn: "amiloride"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-11-24
description: "Amiloride: nueva indicación predicha, Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 4 (comercializadas: 3)"
---

# Amiloride
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Amilorida: diurético ahorrador de potasio → enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)
{: .text-alpha }

## Resumen en Una Frase

La amilorida es un diurético ahorrador de potasio. El modelo TxGNN predice que podría ser útil para la **enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)**. Actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción, por lo que se trata solo de una señal computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) |
| Puntaje de Predicción TxGNN | 0,9982 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 3 de 4; revocadas o suspendidas: 1) |
| Número de Autorizaciones | 4 (comercializadas: 3) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Amiloride (traducción no oficial): «El clorhidrato de amilorida es un fármaco ahorrador de potasio (antikaliurético) que posee una actividad natriurética, diurética y antihipertensiva débil (en comparación con los diuréticos tiazídicos). En algunos estudios clínicos, estos efectos han sido parcialmente aditivos a los efectos de los diuréticos tiazídicos.» Texto original en inglés: "Amiloride HCl is a potassium-conserving (antikaliuretic) drug that possesses weak (compared with thiazide diuretics) natriuretic, diuretic, and antihypertensive activity. These effects have been partially additive to the effects of thiazide diuretics in some clinical studies." ([DailyMed: amiloride hydrochloride prescribing information, Kesin Pharma Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5eedadbd-9be9-b920-e063-6394a90afa68), versión del 2026-11-11; consultado el 2026-11-19). Por su clase, la amilorida es un diurético ahorrador de potasio que actúa sobre el transporte de sodio en el riñón. Esto da una plausibilidad general en trastornos de la presión arterial con afectación renal.

La relación con la nueva indicación es solo predictiva. No se recuperaron ensayos ni literatura sobre la enfermedad renal hipertensiva maligna, por lo que no hay datos de eficacia que sustenten un vínculo mecanístico específico.

La hipertensión maligna con afectación renal es un cuadro agudo y de alto riesgo. La amilorida conlleva riesgo de hiperpotasemia en la insuficiencia renal. Por ello no se dispone de una justificación de seguridad ni de eficacia para esta indicación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Los productos siguientes contienen amilorida. Varios son combinaciones a dosis fija (5 mg/50 mg con hidroclorotiazida), por lo que sus autorizaciones no describen la situación de la amilorida como principio activo único.

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 86330 | AMILORIDA/HIDROCLOROTIAZIDA AUROVITAS 5 MG/50 MG COMPRIMIDOS EFG | COMPRIMIDO | Aurovitas Spain, S.A.U. | Comercializada |
| 55423 | DIUZINE 5 mg/50 mg COMPRIMIDOS | COMPRIMIDO | Teofarma S.R.L. | Comercializada |
| 53265 | AMERIDE 5 mg/50 mg COMPRIMIDOS | COMPRIMIDO | Pan Quimica Farmaceutica S.A. | Comercializada |
| 57632 | KALTEN | CÁPSULA DURA | Teofarma S.R.L. | Revocada |

Se muestran las 4 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Riesgo de hiperpotasemia**: la amilorida puede elevar el potasio, sobre todo en insuficiencia renal, que es el contexto de la indicación predicha.
- **Interacciones farmacológicas**: se registraron 136 interacciones. Entre las de nivel moderado destacan:
  - corticoides (hidrocortisona, betametasona, budesonida, dexametasona);
  - antidiabéticos (metformina, exenatida, canagliflozina, dapagliflozina, empagliflozina, ertugliflozina);
  - bupropión y dronabinol;
  - laxantes y similares (bisacodilo, aceite de ricino, glicerina, lactitol, lactulosa).
- Entre las de nivel leve figuran doxiciclina, amoxicilina y cimetidina.

Para advertencias y contraindicaciones formales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (0,9982), pero no cuenta con ensayos clínicos ni literatura que estudien directamente esta enfermedad (nivel L5). Además, el contexto renal agudo plantea un riesgo de seguridad por hiperpotasemia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de la amilorida aplicables a la enfermedad renal hipertensiva maligna.
- Revisión sistemática de literatura clínica y preclínica específica de esta indicación.
- Análisis de seguridad en insuficiencia renal (riesgo de hiperpotasemia) a partir del prospecto.
- Evaluación de viabilidad de un estudio exploratorio con vigilancia estrecha de potasio y función renal.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: amiloride hydrochloride prescribing information, Kesin Pharma Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5eedadbd-9be9-b920-e063-6394a90afa68) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

