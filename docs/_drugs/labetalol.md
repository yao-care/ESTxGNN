---
layout: default
title: Labetalol
parent: Solo predicción del modelo (L5)
nav_order: 443
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
monitor_inn: "LABETALOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia"]
description: "Labetalol: nueva indicación predicha, Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 4 (comercializadas: 4)"
---

# Labetalol
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

## Labetalol: Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)
{: .text-alpha }

## Resumen en Una Frase

Labetalol es un bloqueador adrenérgico combinado (alfa-1 y beta no selectivo), utilizado originalmente para el tratamiento de la hipertensión y los trastornos hipertensivos.
El modelo TxGNN predice que podría ser efectivo para la **enfermedad renal hipertensiva maligna**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden específicamente esta indicación; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) |
| Puntaje de Predicción TxGNN | 0.9908 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 4 de 4) |
| Número de Autorizaciones | 4 (comercializadas: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Labetalol (traducción no oficial): «El labetalol tiene actividad bloqueante alfa1-adrenérgica competitiva y actividad bloqueante beta-adrenérgica competitiva. En el ser humano, se ha estimado que la relación entre el bloqueo alfa y el bloqueo beta es de aproximadamente 1:7 tras la administración intravenosa.» Texto original en inglés: "Labetalol has both competitive alpha1-adrenergic blocking and competitive beta-adrenergic blocking activity. In man, the ratio of alpha- to beta-blockade has been estimated to be approximately 1:7 following intravenous administration." ([DailyMed: Labetalol Hcl In Dextrose (labetalol hydrochloride) prescribing information, Hikma Pharmaceuticals USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=99a715a0-4579-410c-b102-7ef6fab8db55), versión del 2025-12-19; consultado el 2026-11-19). Según la información conocida, labetalol es un bloqueador combinado alfa-1 y beta-adrenérgico no selectivo, con eficacia comprobada en hipertensión y en emergencias hipertensivas. Mecanísticamente, la reducción de la resistencia vascular periférica y de la frecuencia cardíaca podría ser aplicable a la hipertensión maligna con afectación renal.

La relación con la indicación original es muy estrecha: la enfermedad renal hipertensiva maligna es una forma grave de hipertensión. Por ello, esta predicción es más bien una extensión de la indicación existente que una oportunidad de reposicionamiento distinta. El puntaje alto del modelo (0,9908) debe interpretarse con cautela, ya que no cuenta con respaldo clínico directo.

Como referencia, el mismo modelo generó otras predicciones con puntajes similares (hipertensión renovascular maligna y dos formas de hipertensión pulmonar). Para la hipertensión pulmonar, el bloqueo beta sistémico no tiene una justificación establecida y podría ser desfavorable (por ejemplo, por efectos sobre la función del ventrículo derecho o por broncoespasmo), por lo que esas predicciones parecen reflejar la etiqueta compartida "hipertensión" más que un mecanismo real.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 55318 | TRANDATE 5 mg/ml SOLUCIÓN INYECTABLE | SOLUCIÓN INYECTABLE | Kern Pharma S.L. | Comercializada |
| 54527 | TRANDATE 100 mg, COMPRIMIDOS RECUBIERTOS | COMPRIMIDO RECUBIERTO CON PELÍCULA | Kern Pharma S.L. | Comercializada |
| 89082 | LABETALOL S.A.L.F. 5 MG/ML SOLUCION INYECTABLE Y PARA PERFUSION EFG | SOLUCIÓN INYECTABLE Y PARA PERFUSIÓN | S.A.L.F. S.P.A. Laboratorio Farmacologico | Comercializada |
| 54528 | TRANDATE 200 mg COMPRIMIDOS RECUBIERTOS | COMPRIMIDO RECUBIERTO CON PELÍCULA | Kern Pharma S.L. | Comercializada |

Se muestran las 4 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no provienen del texto del prospecto): insuficiencia hepática y enfermedad hepática, encefalopatía hepática, enfermedad renal, anuria, diabetes mellitus y cetoacidosis diabética, bloqueo auriculoventricular, enfisema pulmonar y enfermedad bronquial, hipotensión, lupus eritematoso sistémico, gota, pancreatitis, enfermedad de la vesícula biliar, trastornos de ansiedad y neuróticos, entre otras.
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Entre las principales:
  - **Mayores**: epinefrina, dolasetrón.
  - **Moderadas**: hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida, morfina, atropina, cimetidina, canagliflozina, dapagliflozina, clorpropamida, entre otras.
  - **Menores**: ácido acetilsalicílico, óxido de magnesio.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos clínicos ni literatura directa, y constituye en gran medida una extensión de la indicación hipertensiva ya existente. Además, varias contraindicaciones del grafo de conocimiento afectan a poblaciones con enfermedad renal, lo que exige cautela.

**Para avanzar se necesita:**
- Revisión de la literatura clínica específica sobre labetalol en hipertensión maligna con afectación renal
- Datos detallados del mecanismo de acción
- Obtención y análisis del prospecto oficial de la AEMPS (advertencias y contraindicaciones), en especial para pacientes con insuficiencia renal
- Evaluación de si esta indicación aporta un valor distinto del uso ya establecido en emergencias hipertensivas

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Labetalol Hcl In Dextrose (labetalol hydrochloride) prescribing information, Hikma Pharmaceuticals USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=99a715a0-4579-410c-b102-7ef6fab8db55) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

