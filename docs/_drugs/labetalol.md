---
layout: default
title: Labetalol
parent: Solo predicción del modelo (L5)
nav_order: 443
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Labetalol: nueva indicación predicha, Enfermedad renal hipertensiva maligna (nivel de evidencia L5). Indicación original: Hipertensión / trastorno hipertensivo (según el grafo de conocimiento"
monitor_inn: "LABETALOL"
predicted_indications: ["malignant hypertensive renal disease", "malignant renovascular hypertension", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia"]
---

# Labetalol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Labetalol: De Hipertensión a Enfermedad Renal Hipertensiva Maligna

## Resumen en Una Frase

Labetalol es un bloqueador adrenérgico combinado (alfa-1 y beta no selectivo), utilizado originalmente para el tratamiento de la hipertensión y los trastornos hipertensivos.
El modelo TxGNN predice que podría ser efectivo para la **enfermedad renal hipertensiva maligna**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden específicamente esta indicación; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión / trastorno hipertensivo (según el grafo de conocimiento; los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna |
| Puntaje de Predicción TxGNN | 99,08% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, labetalol es un bloqueador combinado alfa-1 y beta-adrenérgico no selectivo, con eficacia comprobada en hipertensión y en emergencias hipertensivas. Mecanísticamente, la reducción de la resistencia vascular periférica y de la frecuencia cardíaca podría ser aplicable a la hipertensión maligna con afectación renal.

La relación con la indicación original es muy estrecha: la enfermedad renal hipertensiva maligna es una forma grave de hipertensión. Por ello, esta predicción es más bien una extensión de la indicación existente que una oportunidad de reposicionamiento distinta. El puntaje alto del modelo (99,08%) debe interpretarse con cautela, ya que no cuenta con respaldo clínico directo.

Como referencia, el mismo modelo generó otras predicciones con puntajes similares (hipertensión renovascular maligna y dos formas de hipertensión pulmonar). Para la hipertensión pulmonar, el bloqueo beta sistémico no tiene una justificación establecida y podría ser desfavorable (por ejemplo, por efectos sobre la función del ventrículo derecho o por broncoespasmo), por lo que esas predicciones parecen reflejar la etiqueta compartida "hipertensión" más que un mecanismo real.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 55318 | TRANDATE 5 mg/ml solución inyectable | Solución inyectable | No especificada |
| 54527 | TRANDATE 100 mg comprimidos recubiertos | Comprimido recubierto con película | No especificada |
| 89082 | LABETALOL S.A.L.F. 5 mg/ml solución inyectable y para perfusión EFG | Solución inyectable y para perfusión | No especificada |
| 54528 | TRANDATE 200 mg comprimidos recubiertos | Comprimido recubierto con película | No especificada |

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
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

