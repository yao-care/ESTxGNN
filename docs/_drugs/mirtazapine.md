---
layout: default
title: Mirtazapine
parent: Solo predicción del modelo (L5)
nav_order: 533
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
monitor_inn: "Mirtazapine"
predicted_indications: ["Ohdo syndrome and variants", "blepharophimosis - intellectual disability syndrome, Ohdo type", "benign paroxysmal torticollis of infancy"]
description: "Mirtazapine: nueva indicación predicha, Síndrome de Ohdo y variantes (Ohdo syndrome and variants) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: al menos 20"
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
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 15; revocadas o suspendidas: 5) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Mirtazapine (traducción no oficial): «El mecanismo de acción de la mirtazapina en el tratamiento del trastorno depresivo mayor no está claro. Sin embargo, su eficacia podría estar mediada por su actividad como antagonista de los autorreceptores y heterorreceptores inhibidores α 2 -adrenérgicos presinápticos centrales y por la potenciación de la actividad noradrenérgica y serotoninérgica central.» Texto original en inglés: "The mechanism of action of mirtazapine for the treatment of major depressive disorder, is unclear. However, its efficacy could be mediated through its activity as an antagonist at central presynaptic α 2 -adrenergic inhibitory autoreceptors and heteroreceptors and enhancing central noradrenergic and serotonergic activity." ([DailyMed: Remeronsoltab (mirtazapine) prescribing information, Organon LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98ad1917-a094-44f5-a28f-a64a8cfcd887), versión del 2025-08-06; consultado el 2026-11-19). Según la información conocida, mirtazapina es un antidepresivo noradrenérgico y serotoninérgico específico. Los datos de farmacología recopilados indican que tiene la mayor afinidad por los adrenoceptores α2 (2A > 2C > 2B) y por los receptores serotoninérgicos 5-HT2A y 5-HT2C, lo que sustenta su eficacia en la depresión mayor.

El síndrome de Ohdo es un trastorno genético raro (asociado a KAT6B) que implica la regulación de la cromatina. Con los datos disponibles **no se puede establecer un vínculo mecanístico** entre la acción de la mirtazapina sobre receptores monoaminérgicos y la fisiopatología de esta enfermedad. El puntaje del modelo es muy alto, pero es solo una predicción computacional.

Además, la segunda predicción (síndrome de blefarofimosis con discapacidad intelectual, tipo Ohdo; 0,9911) probablemente corresponde a la misma entidad o a una muy cercana; el puntaje proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica, por lo que ambas predicciones no son independientes y no deben contarse como apoyos separados. La tercera (tortícolis paroxística benigna de la infancia; 0,9911) solo tiene una conexión especulativa con variantes de migraña y canalopatías, y afecta a población lactante, para la cual mirtazapina no está establecida.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

<!-- review:begin es-lic-20261105-mirtazapine-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Se listan 5 de las 20 autorizaciones vigentes (todas de medicamentos de un solo principio activo; el texto de indicación aprobada no está disponible en los datos compilados)." Eliminado: afirmaba que el medicamento no está autorizado o comercializado en España, o que sus autorizaciones están revocadas o suspendidas, lo que no coincide con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-mirtazapine-1 -->

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 90891 | MIRTAZAPINA STADA 45 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Laboratorio Stada S.L. | Comercializada |
| 71841 | MIRTAZAPINA FLAS KERN PHARMA 15 mg COMPRIMIDOS BUCODISPERSABLES EFG | COMPRIMIDO BUCODISPERSABLE | Kern Pharma S.L. | Comercializada |
| 89479 | MIRTAZAPINA SANDOZ 30 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Sandoz Farmaceutica S.A. | Comercializada |
| 69802 | MIRTAZAPINA QUALIGEN 15 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Neuraxpharm Spain S.L. | Comercializada |
| 66982 | MIRTAZAPINA ALTER 15 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Laboratorios Alter S.A. | Comercializada |
| 90068 | MIRTAZAPINA COMBIX 15 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Laboratorios Combix S.L.U. | Comercializada |
| 69999 | MIRTAZAPINA FLAS ALTER 30 mg COMPRIMIDOS BUCODISPERSABLES EFG | COMPRIMIDO BUCODISPERSABLE | Laboratorios Alter S.A. | Comercializada |
| 65878 | MIRTAZAPINA STADA 30 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Laboratorio Stada S.L. | Comercializada |
| 89480 | MIRTAZAPINA SANDOZ 45 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Sandoz Farmaceutica S.A. | Comercializada |
| 69306 | MIRTAZAPINA ALMUS 15 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Almus Farmaceutica S.A.U. | Comercializada |

Se muestran 10 de al menos 20 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas. Los datos de este informe solo incluyen parte de las autorizaciones.

<!-- licenses:end -->

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

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Se listan 5 de las 20 autorizaciones vigentes (todas de medicamentos de un solo principio activo; el texto de indicación aprobada no está di" | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Remeronsoltab (mirtazapine) prescribing information, Organon LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98ad1917-a094-44f5-a28f-a64a8cfcd887) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

