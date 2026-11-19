---
layout: default
title: Ravulizumab
parent: Solo predicción del modelo (L5)
nav_order: 686
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-05
monitor_inn: "RAVULIZUMAB"
predicted_indications: ["autosomal recessive severe congenital neutropenia due to G6PC3 deficiency", "cyclic hematopoiesis", "primary hyperoxaluria", "severe congenital neutropenia", "autosomal recessive severe congenital neutropenia due to CXCR2 deficiency", "primary immunodeficiency syndrome due to p14 deficiency", "pseudo-von Willebrand disease", "X-linked severe congenital neutropenia", "primary release disorder of platelets", "megaloblastic anemia (disease)"]
description: "Ravulizumab: nueva indicación predicha, Neutropenia congénita grave autosómica recesiva por deficiencia de G6PC3 (autosomal recessive severe congenital neutrop… (nivel de evidencia L5). Indicación or…"
---

# Ravulizumab
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

## Ravulizumab: Neutropenia congénita grave autosómica recesiva por deficiencia de G6PC3 (autosomal recessive severe congenital neutropenia due to G6PC3 deficiency)
{: .text-alpha }

## Resumen en Una Frase

Ravulizumab es un inhibidor del componente C5 del complemento, originalmente utilizado para el tratamiento de la hemoglobinuria paroxística nocturna (HPN).
El modelo TxGNN predice que podría ser efectivo para **neutropenia congénita grave autosómica recesiva por deficiencia de G6PC3**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Neutropenia congénita grave autosómica recesiva por deficiencia de G6PC3 (autosomal recessive severe congenital neutropenia due to G6PC3 deficiency) |
| Puntaje de Predicción TxGNN | 0.9996 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 2 de 2) |
| Número de Autorizaciones | 2 (comercializadas: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Ravulizumab es un anticuerpo monoclonal que inhibe el componente C5 del complemento terminal. Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Ravulizumab (traducción no oficial): «Ravulizumab-cwvz es un inhibidor del complemento terminal que se une específicamente y con alta afinidad a la proteína del complemento C5, con lo que inhibe su escisión en C5a (la anafilatoxina proinflamatoria) y C5b (la subunidad iniciadora del complejo de ataque a la membrana [MAC o C5b-9]) y, de este modo, impide la formación del MAC. ULTOMIRIS inhibe la hemólisis intravascular mediada por el complemento terminal en pacientes con HPN y la microangiopatía trombótica (MAT) mediada por el complemento en pacientes con SHUa.» Texto original en inglés: "Ravulizumab-cwvz is a terminal complement inhibitor that specifically binds to the complement protein C5 with high affinity, thereby inhibiting its cleavage to C5a (the proinflammatory anaphylatoxin) and C5b (the initiating subunit of the membrane attack complex [MAC or C5b-9]) thus preventing MAC formation. ULTOMIRIS inhibits terminal complement-mediated intravascular hemolysis in patients with PNH and complement-mediated thrombotic microangiopathy (TMA) in patients with aHUS." ([DailyMed: Ultomiris (ravulizumab) prescribing information, Alexion Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a9a590d9-0217-43c7-908d-e62a71279791), versión del 2026-10-29; consultado el 2026-11-19). Por su clase farmacológica, su eficacia en la HPN, una enfermedad de hemólisis intravascular mediada por complemento, es conocida.

La relación entre la indicación original y la nueva es débil. La deficiencia de G6PC3 es un defecto metabólico y de maduración mieloide sin patología conocida dirigida por el complemento. La puntuación proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica; no cuenta con respaldo mecanístico ni clínico.

Por ello, la alta puntuación del modelo (0.9996) debe interpretarse con cautela: no hay una justificación biológica establecida para que la inhibición de C5 sea aplicable a esta enfermedad. Otras predicciones del mismo análisis (neutropenia cíclica, hiperoxaluria primaria, neutropenia congénita grave, entre otras) presentan igualmente evidencia de nivel L5 y recomendación Hold.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1191371003 | ULTOMIRIS 1100 mg/11 ml concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos compilados |
| 1191371002 | ULTOMIRIS 300 mg/3 ml concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones (grafo de conocimiento)**: infección meningocócica. Este dato procede de las relaciones fármaco-enfermedad del grafo de conocimiento, no del texto del prospecto.
- **Interacciones Farmacológicas**: se identificaron 4 interacciones de nivel menor, todas con inmunoglobulina G humana (intravenosa, subcutánea, intramuscular e intravenosa/subcutánea).

Para el resto de la información de seguridad, consultar el prospecto. Cabe señalar que la inhibición del complemento terminal conlleva un riesgo de infección meningocócica, que sería especialmente relevante en poblaciones con inmunodeficiencia o neutropenia.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa exclusivamente en el modelo (nivel L5), sin ensayos clínicos, literatura ni racional mecanístico que vincule la inhibición de C5 con la deficiencia de G6PC3. Además, el riesgo de infecciones graves por inhibición del complemento sería preocupante en pacientes neutropénicos.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y evidencia preclínica que relacione el complemento con la fisiopatología de la deficiencia de G6PC3
- Texto de las advertencias y contraindicaciones del prospecto de AEMPS
- Texto de las indicaciones aprobadas en las autorizaciones españolas
- Evaluación de la compatibilidad de vía de administración y de la similitud con la indicación original
- Un plan de seguridad que contemple el riesgo de infección meningocócica y de infecciones en pacientes neutropénicos

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Ultomiris (ravulizumab) prescribing information, Alexion Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a9a590d9-0217-43c7-908d-e62a71279791) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

