---
layout: default
title: Atenolol
parent: Solo predicción del modelo (L5)
nav_order: 73
evidence_level: L5
indication_count: 5
monitor_inn: "ATENOLOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-11-20
description: "Atenolol: nueva indicación predicha, Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: al menos 20"
---

# Atenolol
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

## Atenolol: betabloqueante cardioselectivo β1 → enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)
{: .text-alpha }

## Resumen en Una Frase

Atenolol es un betabloqueante cardioselectivo (β1) que se comercializa en España en comprimidos y solución inyectable.
El modelo TxGNN predice que podría ser efectivo para la **enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta indicación concreta; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) |
| Puntaje de Predicción TxGNN | 0,9985 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 15; revocadas o suspendidas: 5) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Atenolol (traducción no oficial): «TENORMIN es un bloqueante de los receptores beta-adrenérgicos selectivo beta 1 (cardioselectivo) sin actividad estabilizadora de membrana ni actividad simpaticomimética intrínseca (agonista parcial). Sin embargo, este efecto preferencial no es absoluto y, a dosis más altas, TENORMIN inhibe los adrenorreceptores beta 2, localizados principalmente en la musculatura bronquial y vascular.» Texto original en inglés: "TENORMIN is a beta 1 -selective (cardioselective) beta-adrenergic receptor blocking agent without membrane stabilizing or intrinsic sympathomimetic (partial agonist) activities. This preferential effect is not absolute, however, and at higher doses, TENORMIN inhibits beta 2 -adrenoreceptors, chiefly located in the bronchial and vascular musculature." ([DailyMed: Tenormin (atenolol) prescribing information, Upsher-Smith Laboratories, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6e850b1e-28a4-4ff8-8ed7-bb0b29faa28a), versión del 2025-09-18; consultado el 2026-11-19). Según la información conocida, atenolol es un bloqueante selectivo de los receptores β1-adrenérgicos que reduce la presión arterial y suprime la liberación de renina.

Esta reducción de la presión arterial y de la actividad de la renina es plausiblemente relevante para el daño renal causado por la hipertensión. El puntaje alto del modelo podría reflejar, en gran parte, la cercanía de esta enfermedad con la hipertensión.

Sin embargo, el vínculo sigue siendo puramente computacional. La hipertensión maligna suele tratarse con fármacos que permiten una reducción de la presión controlada y titulable, y no se aportó ningún estudio que evalúe atenolol en esta enfermedad.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

## Información de Mercado en España

Se identificaron al menos 20 autorizaciones (la lista puede ser parcial): 15 vigentes y 5 canceladas. Principales autorizaciones vigentes:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 56967 | TENORMIN 50 mg comprimidos | Comprimido |
| 56777 | TENORMIN 0,5 mg/ml solución inyectable | Solución inyectable |
| 62446 | Atenolol Alter 50 mg comprimidos EFG | Comprimido |
| 84415 | Atenolol Aurovitas 100 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 61493 | Atenolol Normon 100 mg comprimidos recubiertos EFG | Comprimido recubierto |

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: se registraron 100 interacciones. Entre las de nivel moderado figuran epinefrina, hidrocortisona, hiosciamina, bupropión, triamcinolona, morfina, atropina, betametasona, budesonida y varias sales de calcio. Con ácido acetilsalicílico, hidróxido de aluminio y atapulgita el nivel es menor.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ensayos clínicos ni literatura que estudien directamente esta enfermedad (nivel L5), y el puntaje alto del modelo no sustituye a la evidencia clínica.

**Para avanzar se necesita:**
- Estudios clínicos o series de casos de atenolol en enfermedad renal hipertensiva maligna
- Datos detallados del mecanismo de acción
- Revisión de las advertencias y contraindicaciones del prospecto de AEMPS
- Evaluación frente a los tratamientos habituales de la hipertensión maligna, que requieren reducción de presión titulable

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Tenormin (atenolol) prescribing information, Upsher-Smith Laboratories, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6e850b1e-28a4-4ff8-8ed7-bb0b29faa28a) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

