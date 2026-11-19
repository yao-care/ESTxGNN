---
layout: default
title: Verapamil
parent: Solo predicción del modelo (L5)
nav_order: 843
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-12
monitor_inn: "verapamil"
predicted_indications: ["obsolete bundle branch block", "malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "periodic paralysis with transient compartment-like syndrome"]
description: "Verapamil: nueva indicación predicha, Bloqueo de rama (obsolete bundle branch block) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 7 (comercializadas: 6)"
---

# Verapamil
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Verapamil: Bloqueo de rama (obsolete bundle branch block)
{: .text-alpha }

## Resumen en Una Frase

Verapamilo es un bloqueador de los canales de calcio tipo L, utilizado originalmente para el tratamiento de la hipertensión, la fibrilación auricular, el síndrome coronario agudo, la angina de Prinzmetal y la taquicardia ventricular.
El modelo TxGNN predice que podría ser efectivo para **bloqueo de rama (entrada obsoleta)**, con un puntaje muy alto pero **sin ensayos clínicos ni publicaciones** que respalden esta dirección.
Se trata de una predicción puramente computacional, por lo que la recomendación es **Hold**.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Bloqueo de rama (obsolete bundle branch block) |
| Puntaje de Predicción TxGNN | 0.9962 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 6 de 7; revocadas o suspendidas: 1) |
| Número de Autorizaciones | 7 (comercializadas: 6) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Verapamil (traducción no oficial): «Angina: El mecanismo de acción preciso del clorhidrato de verapamilo como agente antianginoso aún no se ha determinado por completo, pero incluye los dos mecanismos siguientes: 1. Relajación y prevención del espasmo de las arterias coronarias: El clorhidrato de verapamilo dilata las arterias coronarias principales y las arteriolas coronarias, tanto en las regiones normales como en las isquémicas, y es un potente inhibidor del espasmo de las arterias coronarias, ya sea espontáneo o inducido por ergonovina.» Texto original en inglés: "Angina: The precise mechanism of action of verapamil hydrochloride as an antianginal agent remains to be fully determined, but includes the following two mechanisms: 1. Relaxation and prevention of coronary artery spasm: Verapamil hydrochloride dilates the main coronary arteries and coronary arterioles, both in normal and ischemic regions, and is a potent inhibitor of coronary artery spasm, whether spontaneous or ergonovine-induced." ([DailyMed: verapamil hydrochloride prescribing information, Preferred Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c7a54ee0-80c0-4c7e-a6a3-cb60142f860c), versión del 2026-10-30; consultado el 2026-11-19). Según la información conocida, verapamilo es un bloqueador de los canales de calcio tipo L que enlentece la conducción del nodo auriculoventricular y produce vasodilatación. Su eficacia en hipertensión y en arritmias supraventriculares y ventriculares está establecida.

Sin embargo, la relación mecanística con el bloqueo de rama es débil. Enlentecer la conducción por el nodo AV no supone un beneficio evidente en trastornos de conducción intraventricular, y el fármaco podría incluso empeorarlos. Además, el grafo de conocimiento lista el bloqueo auriculoventricular y la insuficiencia cardíaca como contraindicaciones, lo que refuerza la cautela.

La etiqueta de la enfermedad es obsoleta, lo que reduce la fiabilidad de la entrada. El puntaje alto (0,9962) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni validación clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

<!-- review:begin es-lic-20261105-verapamil-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Existen 7 autorizaciones vigentes en total (todas de principio activo único); además de las anteriores figuran Manidon HTA 240 mg (58369) y Tarka 180 mg/2 mg (61369, cápsula de liberación modificada)." Eliminado: el número o el estado de comercialización de las autorizaciones no coincidía con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 7 autorizaciones (comercializadas: 6); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en España. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-verapamil-1 -->

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 60724 | Manidon Retard 180 mg | Comprimido de liberación prolongada | No disponible en los datos compilados |
| 58-157-87-C | Manidon HTA | Comprimido de liberación prolongada | No disponible en los datos compilados |
| 39784 | Manidon 2,5 mg/ml | Solución inyectable | No disponible en los datos compilados |
| 53434 | Manidon Retard 120 mg | Comprimido de liberación prolongada | No disponible en los datos compilados |
| 50891 | Manidon 80 mg | Comprimido recubierto con película | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones señaladas por el grafo de conocimiento** (no proceden del prospecto): bloqueo auriculoventricular, insuficiencia cardíaca, hipotensión, estenosis aórtica, miocardiopatía hipertrófica, taquicardia ventricular, miastenia gravis, enfermedad renal, enfermedad hepática, neutropenia/agranulocitosis y angioedema, entre otras.
- **Interacciones farmacológicas**: se identificaron 328 interacciones. Entre las principales figura **loperamida (mayor)**. Otras de nivel moderado incluyen claritromicina, cimetidina, metformina, bupropión, aprepitant, ácido acetilsalicílico y varios corticoides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona), además de sales de calcio y canagliflozina. Morfina presenta una interacción menor.

Para las advertencias formales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo (nivel L5), sin ensayos ni literatura, con una etiqueta de enfermedad obsoleta y un mecanismo que podría incluso ser perjudicial para los trastornos de conducción.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), actualmente un vacío bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción (por ejemplo, consultando la API de DrugBank).
- Revisar la entrada obsoleta y valorar si corresponde a una entidad vigente.
- Considerar priorizar otras predicciones de la lista, por ejemplo, la hipertensión pulmonar por enfermedad pulmonar o hipoxia (L4, con evidencia preclínica indirecta), aunque con importantes reservas de seguridad.
- Realizar una revisión sistemática de la literatura clínica antes de cualquier avance.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Existen 7 autorizaciones vigentes en total (todas de principio activo único); además de las anteriores figuran Manidon HTA 240 mg (58369) y " | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: verapamil hydrochloride prescribing information, Preferred Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c7a54ee0-80c0-4c7e-a6a3-cb60142f860c) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

