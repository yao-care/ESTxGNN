---
layout: default
title: Tagraxofusp
parent: Solo predicción del modelo (L5)
nav_order: 760
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-20
monitor_inn: "TAGRAXOFUSP"
predicted_indications: ["esotropia", "pre-malignant neoplasm", "inner ear neoplasm", "benign neoplasm of tongue", "ductal or ductular proliferation", "non-seminomatous lesion", "bronchial adenomas/carcinoids childhood", "chondroid hamartoma", "cystic neoplasm", "thyroglossal duct cyst"]
description: "Tagraxofusp: nueva indicación predicha, Esotropía (esotropia) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 1 (comercializadas: 0; autorizadas no comercializadas: 1)"
---

# Tagraxofusp
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

## Tagraxofusp: Esotropía (esotropia)
{: .text-alpha }

## Resumen en Una Frase

Tagraxofusp es una proteína de fusión dirigida contra CD123, utilizada originalmente para tratar la neoplasia hematodérmica CD4+/CD56+.
El modelo TxGNN predice que podría ser efectivo para **esotropía**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Esotropía (esotropia) |
| Puntaje de Predicción TxGNN | 0.9973 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Autorizado pero no comercializado (registros: 1) |
| Número de Autorizaciones | 1 (comercializadas: 0) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Tagraxofusp (traducción no oficial): «El tagraxofusp-erzs es una citotoxina dirigida contra CD123 compuesta por una proteína de fusión de interleucina-3 (IL-3) humana recombinante y toxina diftérica (TD) truncada, que inhibe la síntesis de proteínas y causa la muerte celular en las células que expresan CD123.» Texto original en inglés: "Tagraxofusp-erzs is a CD123-directed cytotoxin composed of recombinant human interleukin-3 (IL-3) and truncated diphtheria toxin (DT) fusion protein that inhibits protein synthesis and causes cell death in CD123-expressing cells." ([DailyMed: Elzonris (tagraxofusp) prescribing information, Stemline Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=80eb1080-fe20-4af0-b2a5-a67999923fa8), versión del 2024-12-09; consultado el 2026-11-19). Según la información conocida, tagraxofusp es una proteína de fusión que une interleucina-3 con una toxina diftérica truncada; se dirige a células que expresan CD123 y las elimina. Su eficacia se ha establecido en una neoplasia hematológica con expresión de CD123.

La esotropía es un trastorno de la alineación motora ocular sin patología conocida dependiente de CD123. **No se identifica un vínculo mecanístico creíble** entre el fármaco y esta indicación. El puntaje elevado (0,9973) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica; no cuenta con respaldo clínico ni bibliográfico.

Las demás predicciones del modelo (neoplasia premaligna, neoplasia del oído interno, neoplasia benigna de lengua, proliferación ductal, entre otras) tampoco cuentan con ensayos ni literatura; todas se mantienen en nivel L5 y recomendación Hold. La más cercana a un fundamento mecanístico es la neoplasia premaligna, aunque la categoría es demasiado inespecífica y el perfil de toxicidad (síndrome de fuga capilar, hepatotoxicidad) sería difícil de justificar.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1201504001 | ELZONRIS 1 MG/ML concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos compilados |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (proteína de fusión IL-3/toxina diftérica dirigida a CD123) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto; se consideran relevantes la función hepática y los signos de fuga capilar (según el perfil de toxicidad conocido) |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registraron 66 interacciones, de nivel moderado en las principales mostradas, fundamentalmente con antidiabéticos e insulinas: acarbosa, albiglutida, alogliptina, metformina, pioglitazona, canagliflozina, clorpropamida, dapagliflozina, saxagliptina, dulaglutida, empagliflozina, linagliptina, glimepirida, semaglutida e insulinas (aspart, degludec, detemir, glargina, glulisina, isófana humana).
- **Riesgos del perfil terapéutico**: el síndrome de fuga capilar y la hepatotoxicidad son riesgos relevantes de la terapia con toxina, difíciles de justificar en indicaciones benignas o no oncológicas.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para esotropía carece de ensayos clínicos, literatura y mecanismo plausible; el riesgo de toxicidad sistémica de una toxina citotóxica no se justifica en un trastorno motor ocular.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank
- Advertencias y contraindicaciones del prospecto de la AEMPS
- Evidencia preclínica que demuestre expresión o dependencia de CD123 en la indicación propuesta
- Reevaluar candidatos con mayor plausibilidad biológica (p. ej., otras neoplasias hematológicas con expresión de CD123) antes de considerar esta predicción

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Elzonris (tagraxofusp) prescribing information, Stemline Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=80eb1080-fe20-4af0-b2a5-a67999923fa8) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

