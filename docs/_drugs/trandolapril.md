---
layout: default
title: Trandolapril
parent: Solo predicción del modelo (L5)
nav_order: 812
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-24
monitor_inn: "TRANDOLAPRIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease"]
description: "Trandolapril: nueva indicación predicha, Malignant hypertensive renal disease (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 2 (comercializadas: 2)"
---

# Trandolapril
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

## Trandolapril: Malignant hypertensive renal disease
{: .text-alpha }

## Resumen en Una Frase

Trandolapril es un inhibidor de la enzima convertidora de angiotensina (IECA), utilizado originalmente para el tratamiento de la hipertensión arterial.
El modelo TxGNN predice que podría ser efectivo para **hipertensión renovascular maligna**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden directamente esta indicación; la predicción se apoya solo en el modelo y en un razonamiento mecanístico.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Malignant hypertensive renal disease |
| Puntaje de Predicción TxGNN | 0.9992 |
| Nivel de Evidencia | L5 (según la clasificación de los datos compilados; sin ensayos ni literatura propios para esta indicación, lo que en rigor corresponde a L5) |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 2 de 2) |
| Número de Autorizaciones | 2 (comercializadas: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Trandolapril (traducción no oficial): «El trandolapril se desesterifica al metabolito diácido, trandolaprilato, que es aproximadamente ocho veces más activo como inhibidor de la actividad de la ECA. La ECA es una peptidil dipeptidasa que cataliza la conversión de la angiotensina I en el vasoconstrictor angiotensina II.» Texto original en inglés: "Trandolapril is deesterified to the diacid metabolite, trandolaprilat, which is approximately eight times more active as an inhibitor of ACE activity. ACE is a peptidyl dipeptidase that catalyzes the conversion of angiotensin I to the vasoconstrictor, angiotensin II." ([DailyMed: trandolapril prescribing information, Lupin Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8143a6cf-dadc-4ef7-a8db-d16d7150ad34), versión del 2025-10-31; consultado el 2026-11-19). Según la información conocida, trandolapril pertenece a la clase de los inhibidores de la ECA: bloquea la conversión de angiotensina I en angiotensina II, reduciendo la vasoconstricción y la secreción de aldosterona. Su eficacia en hipertensión arterial está establecida.

La hipertensión renovascular está impulsada en gran medida por la activación del sistema renina-angiotensina, por lo que el bloqueo de este eje es mecanísticamente plausible. La predicción tiene, por tanto, una base biológica razonable.

Sin embargo, el puntaje elevado probablemente refleja la cercanía con la indicación ya aprobada (hipertensión) y no una evidencia independiente. Además, los IECA pueden precipitar insuficiencia renal aguda en la estenosis bilateral de la arteria renal, lo que exige especial cautela en este escenario.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal (hipertensión renovascular maligna).

Para otras indicaciones predichas (por ejemplo, hipertensión pulmonar asociada a enfermedad pulmonar o hipoxia) se identificaron publicaciones preclínicas o indirectas, ninguna en humanos con hipertensión pulmonar. No constituyen respaldo para la indicación principal y se mencionan solo como contexto.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 59984 | GOPTEN 0,5 mg CAPSULAS DURAS | CÁPSULA DURA | Viatris Healthcare Limited | Comercializada |
| 59985 | GOPTEN 2 mg CAPSULAS DURAS | CÁPSULA DURA | Viatris Healthcare Limited | Comercializada |

Se muestran las 2 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

Ambas autorizaciones son de monofármaco, están vigentes y pertenecen a Viatris Healthcare Limited.

## Consideraciones de Seguridad

- **Contraindicaciones / condiciones de riesgo según el grafo de conocimiento** (no proceden del texto del prospecto): enfermedad renal, enfermedad hepática, angioedema (incluido el hereditario, el adquirido y el inducido por bloqueadores del sistema renina-angiotensina-aldosterona), neutropenia y agranulocitosis, estenosis aórtica, miocardiopatía hipertrófica, obstrucción de la arteria renal, trastornos hipotensivos, miastenia gravis, taquicardia ventricular, bloqueo auriculoventricular e insuficiencia cardíaca, entre otras.
- **Interacciones farmacológicas**: se registraron 100 interacciones en total. Entre las mostradas, las de nivel **mayor** son con **citrato de potasio** y **bicarbonato de potasio** (riesgo de hiperpotasemia). Hay numerosas interacciones de nivel **moderado**, por ejemplo con corticoides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona), antidiabéticos (metformina, alogliptina, canagliflozina, dapagliflozina, empagliflozina, glimepirida, clorpropamida), ácido acetilsalicílico, morfina, bupropión, dronabinol, ácido picosulfúrico y polietilenglicol con electrolitos.
- Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos ni literatura que respalden la hipertensión renovascular maligna; la predicción se basa solo en el modelo y en la plausibilidad mecanística, con un riesgo renal relevante en este contexto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto oficial de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas).
- Completar los datos del mecanismo de acción.
- Realizar una búsqueda sistemática de ensayos y literatura clínica sobre IECA en hipertensión renovascular maligna.
- Evaluar el riesgo de insuficiencia renal aguda (estenosis bilateral de arteria renal) e hiperpotasemia, con un plan de monitoreo de función renal y potasio.
- Confirmar la compatibilidad de vía y forma farmacéutica con la nueva indicación.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: trandolapril prescribing information, Lupin Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8143a6cf-dadc-4ef7-a8db-d16d7150ad34) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

