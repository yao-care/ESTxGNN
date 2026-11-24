---
layout: default
title: Fosinopril
parent: Solo predicción del modelo (L5)
nav_order: 360
evidence_level: L5
indication_count: 4
monitor_inn: "FOSINOPRIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
last_modified_at: 2026-11-24
description: "Fosinopril: nueva indicación predicha, Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) (nivel de evidencia L5). Indicación original: No registrada en los datos locales (l…"
---

# Fosinopril
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Fosinopril: inhibidor de la ECA (profármaco de fosinoprilato) → enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)
{: .text-alpha }

## Resumen en Una Frase

Fosinopril es un inhibidor de la enzima convertidora de angiotensina (ECA) que se comercializa en España en comprimidos. El modelo TxGNN predice que podría ser efectivo para la **enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que estudien directamente esta enfermedad.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No registrada en los datos locales (las autorizaciones no incluyen texto de indicación) |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) |
| Puntaje de Predicción TxGNN | 0,9987 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 2 de 4; revocadas o suspendidas: 2) |
| Número de Autorizaciones | 4 (comercializadas: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Fosinopril es un inhibidor de la ECA: se convierte en su forma activa, fosinoprilato, y reduce la angiotensina II, con lo que baja la presión arterial. Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Fosinopril (traducción no oficial): «En animales y en seres humanos, el fosinopril sódico es hidrolizado por esterasas a la forma farmacológicamente activa, el fosinoprilato, un inhibidor competitivo específico de la enzima convertidora de angiotensina (ECA). La ECA es una peptidil dipeptidasa que cataliza la conversión de la angiotensina I en la sustancia vasoconstrictora angiotensina II.» Texto original en inglés: "In animals and humans, fosinopril sodium is hydrolyzed by esterases to the pharmacologically active form, fosinoprilat, a specific competitive inhibitor of angiotensin-converting enzyme (ACE). ACE is a peptidyl dipeptidase that catalyzes the conversion of angiotensin I to the vasoconstrictor substance, angiotensin II." ([DailyMed: Fosinopril Sodium (fosinopril) prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fc38f1bb-f175-4a81-8ed9-c8701efdea35), versión del 2023-11-27; consultado el 2026-11-19).

La nefropatía hipertensiva maligna se produce por hipertensión muy grave y activación del sistema renina-angiotensina-aldosterona (SRAA). Por ello, el mecanismo es plausible: bloquear este sistema podría reducir la presión y la lesión renal.

Conviene ser prudente. Esta predicción es básicamente una extensión del uso del fármaco en hipertensión, y su puntaje alto probablemente refleja esa cercanía. Al no haber estudios sobre esta enfermedad concreta, el nivel de evidencia es L5 (solo predicción del modelo).

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 59716 | FOSITENS 20 mg COMPRIMIDOS | COMPRIMIDO | Bausch Health Ireland Limited | Comercializada |
| 83239 | FOSINOPRIL AUROVITAS 20 MG COMPRIMIDOS EFG | COMPRIMIDO | Aurovitas Spain, S.A.U. | Comercializada |
| 74975 | FOSINOPRIL AUROBINDO 20 mg COMPRIMIDOS EFG | COMPRIMIDO | Laboratorios Aurobindo S.L.U. | Revocada |
| 66779 | FOSINOPRIL TEVA 20 mg COMPRIMIDOS EFG | COMPRIMIDO | Teva Pharma S.L.U. | Revocada |

Se muestran las 4 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

De las 4 autorizaciones, 2 están vigentes y 2 canceladas.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las mostradas, las de nivel **mayor** son con citrato de potasio y bicarbonato de potasio (riesgo de hiperpotasemia). Las de nivel moderado incluyen corticoides (hidrocortisona, betametasona, budesonida, triamcinolona, dexametasona), ácido acetilsalicílico, antidiabéticos (metformina, alogliptina, saxagliptina, canagliflozina, dapagliflozina, empagliflozina, clorpropamida), bupropión, morfina y dronabinol.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es mecanísticamente plausible, pero carece de ensayos y publicaciones sobre esta enfermedad (nivel L5), y es esencialmente una extensión del uso en hipertensión.

**Para avanzar se necesita:**
- Estudios clínicos u observacionales que evalúen fosinopril en nefropatía hipertensiva maligna
- Datos detallados del mecanismo de acción
- Revisión del prospecto para advertencias y contraindicaciones, especialmente en enfermedad renal y estenosis de arteria renal
- Plan de monitorización de función renal y potasio

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Fosinopril Sodium (fosinopril) prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fc38f1bb-f175-4a81-8ed9-c8701efdea35) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

