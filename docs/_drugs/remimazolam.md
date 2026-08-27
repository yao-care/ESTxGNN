---
layout: default
title: Remimazolam
parent: 僅模型預測 (L5)
nav_order: 241
evidence_level: L5
indication_count: 2
---

# Remimazolam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Remimazolam: De Sedación de Procedimientos/Anestesia General a Insomnio

## Resumen en Una Frase

Remimazolam es una benzodiazepina de acción ultra-corta utilizada actualmente para sedación en procedimientos e inducción de anestesia general.
El modelo TxGNN predice que podría ser efectivo para **Insomnio**, con **8 ensayos clínicos** que actualmente exploran contextos relacionados
(principalmente sedación perioperatoria), aunque ninguno evalúa directamente el insomnio crónico como enfermedad primaria.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sedación en procedimientos / inducción de anestesia general (sin indicación formalmente registrada en España) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos estructurados sobre el mecanismo de acción original en la ficha de producto (Data Gap pendiente de resolución vía DrugBank). Según la evidencia disponible en este informe, remimazolam actúa como agonista/modulador alostérico positivo del receptor GABA-A, mecanismo compartido por toda la clase de las benzodiazepinas. Este mecanismo es la base farmacológica de su uso actual en sedación de procedimientos e inducción de anestesia general, y su perfil ultra-corto (metabolismo por esterasas tisulares, vida media de 5-10 minutos, administración por infusión intravenosa continua) lo hace idóneo para ese contexto.

La relación con el insomnio es mecanísticamente plausible en principio: el receptor GABA-A es la diana terapéutica clásica de los hipnóticos utilizados para tratar el insomnio (benzodiazepínicos y no benzodiazepínicos tipo zolpidem). Sin embargo, existe una brecha relevante entre el mecanismo y la aplicación clínica: el insomnio crónico requiere un patrón de dosificación oral que mantenga el sueño durante toda la noche, mientras que remimazolam solo está disponible como infusión intravenosa de efecto muy breve, un perfil incompatible con ese uso.

En consecuencia, la puntuación muy alta de TxGNN (99.91%) probablemente refleja similitud a nivel de embedding del mecanismo GABA-A/sedante compartido con los hipnóticos, más que evidencia clínica real de eficacia en insomnio como enfermedad. De hecho, todos los ensayos disponibles estudian sedación perioperatoria o en UCI, y solo dos de ellos miden la alteración del sueño como variable secundaria en un contexto postoperatorio agudo, no como tratamiento del insomnio crónico.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT05375747](https://clinicaltrials.gov/study/NCT05375747) | No aplica | Retirado | 0 | Comparación de remimazolam vs. propofol en anestesia para cirugía de mama; ensayo retirado sin reclutamiento, sin evidencia utilizable |
| [NCT04532606](https://clinicaltrials.gov/study/NCT04532606) | Fase 4 | Reclutando | 1128 | Impacto de la anestesia general con remimazolam en el pronóstico tras cirugía de cáncer de vejiga; explora delirium postoperatorio, no insomnio |
| [NCT05466279](https://clinicaltrials.gov/study/NCT05466279) | No aplica | Completado | 131 | Anestesia general con remimazolam vs. propofol+midazolam en contexto oncológico; información de título incompleta, sin relación directa con insomnio |
| [NCT06575530](https://clinicaltrials.gov/study/NCT06575530) | Fase 4 | Reclutando | 306 | Eficacia y seguridad de remimazolam en sedación de pacientes con ventilación mecánica en UCI tras cirugía no cardiaca |
| [NCT06284668](https://clinicaltrials.gov/study/NCT06284668) | No aplica | Completado | 315 | Esketamina vs. remimazolam para alteración del sueño y ansiedad postoperatoria tras extracción de ovocitos; mide directamente alteración del sueño, el ensayo más relevante disponible, aunque en contexto agudo postquirúrgico, no insomnio crónico |
| [NCT07046364](https://clinicaltrials.gov/study/NCT07046364) | Fase 4 | Reclutando | 248 | Efecto de remimazolam sobre delirium de emergencia en neurocirugía pediátrica con sevoflurano; estudia agitación, no insomnio |
| [NCT06108830](https://clinicaltrials.gov/study/NCT06108830) | No aplica | Reclutando | 400 | Esketamina combinada con remimazolam sobre alteración del sueño y ansiedad postoperatoria en gastroenteroscopias; diseño similar a NCT06284668, aún en reclutamiento |
| [NCT05606315](https://clinicaltrials.gov/study/NCT05606315) | Fase 4 | Desconocido | 285 | Remimazolam para sedación en UCI de pacientes con ventilación mecánica tras cirugía oral y maxilofacial; seguimiento interrumpido |

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
A pesar de una puntuación TxGNN muy alta (99.91%), los 8 ensayos clínicos disponibles se centran en sedación perioperatoria o en UCI, y no evalúan el insomnio como enfermedad primaria. Solo dos ensayos (NCT06284668 y NCT06108830) miden la alteración del sueño como variable secundaria en un contexto agudo postoperatorio, lo cual no equivale a evidencia sobre insomnio crónico. El nivel de evidencia (L4) refleja una plausibilidad mecanística, pero es insuficiente para avanzar a una evaluación clínica formal de esta indicación.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha técnica (TFDA) con advertencias y contraindicaciones — actualmente es un vacío de datos bloqueante para la evaluación de seguridad
- Datos estructurados del mecanismo de acción original vía DrugBank
- Ensayos clínicos diseñados específicamente para insomnio crónico (no sedación perioperatoria aguda) con remimazolam
- Evaluación de la compatibilidad de vía de administración: remimazolam es actualmente solo intravenoso, mientras que el tratamiento del insomnio requiere una formulación oral ambulatoria
- Dado que el fármaco no está comercializado en España, sería necesario un dossier regulatorio completo antes de cualquier desarrollo clínico en esta indicación

**Nota — segunda hipótesis predicha (menor prioridad):**
El modelo también predijo *alcohol withdrawal delirium* (puntuación TxGNN 99.30%, Nivel de Evidencia L5, sin ensayos clínicos ni literatura disponibles). El razonamiento mecanístico es coherente a nivel de clase farmacológica (las benzodiazepinas son tratamiento de primera línea para el síndrome de abstinencia alcohólica), pero al no existir ningún estudio real que la respalde, se mantiene como pregunta de investigación (Research Question) sin evidencia clínica actual.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

