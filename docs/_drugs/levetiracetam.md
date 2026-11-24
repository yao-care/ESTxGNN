---
layout: default
title: Levetiracetam
parent: Solo predicción del modelo (L5)
nav_order: 463
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "LEVETIRACETAM"
predicted_indications: ["beta-ketothiolase deficiency"]
description: "Levetiracetam: nueva indicación predicha, Beta-ketothiolase deficiency (nivel de evidencia L5). En España, autorizaciones de la AEMPS: al menos 20"
---

# Levetiracetam
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Levetiracetam: Beta-ketothiolase deficiency
{: .text-alpha }

## Resumen en Una Frase

Levetiracetam es un antiepiléptico de segunda generación, utilizado originalmente para el tratamiento de la epilepsia parcial.
El modelo TxGNN predice que podría ser efectivo para el **déficit de beta-cetotiolasa**, con **16 ensayos clínicos** y **20 publicaciones** que respaldan actualmente esta dirección, incluidos varios ensayos de Fase 3 completados.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Beta-ketothiolase deficiency |
| Puntaje de Predicción TxGNN | 0.9990 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 9; autorizadas no comercializadas: 4; revocadas o suspendidas: 7) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Levetiracetam (traducción no oficial): «Se desconoce(n) el(los) mecanismo(s) preciso(s) mediante el(los) cual(es) el levetiracetam ejerce su efecto antiepiléptico. Se ha descrito para el levetiracetam un sitio de unión neuronal saturable y estereoselectivo en tejido cerebral de rata. Los datos experimentales indican que este sitio de unión es la proteína de las vesículas sinápticas SV2A, que se cree que participa en la regulación de la exocitosis de las vesículas.» Texto original en inglés: "The precise mechanism(s) by which levetiracetam exerts its antiepileptic effect is unknown. A saturable and stereoselective neuronal binding site in rat brain tissue has been described for levetiracetam. Experimental data indicate that this binding site is the synaptic vesicle protein SV2A, thought to be involved in the regulation of vesicle exocytosis." ([DailyMed: Keppra (levetiracetam) prescribing information, UCB, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c6d5784d-abf9-45fe-ac5a-d5c53bd50f7e), versión del 2026-11-11; consultado el 2026-11-19). Según la literatura recuperada, levetiracetam se une a la proteína de la vesícula sináptica SV2A y modula la liberación de neurotransmisores, lo que reduce la hiperexcitabilidad neuronal.

La epilepsia parcial y el estado epiléptico comparten la misma base fisiopatológica: una descarga neuronal excesiva y sostenida. Un fármaco que reduce la liberación de neurotransmisores excitadores es, por tanto, mecanísticamente aplicable a crisis prolongadas que no ceden con benzodiazepinas.

El ensayo ESETT (NCT01960075) comparó levetiracetam, fosfenitoína y valproato en estado epiléptico refractario a benzodiazepinas. Levetiracetam mostró una eficacia comparable, pero no superior, a las alternativas.

## Evidencia de Ensayos Clínicos

Se listan los 10 ensayos más relevantes (de 16 registrados):

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01960075](https://clinicaltrials.gov/study/NCT01960075) | Fase 3 | Completado | 478 | Fosfenitoína vs valproato vs levetiracetam en estado epiléptico refractario a benzodiazepinas (ESETT) |
| [NCT01150331](https://clinicaltrials.gov/study/NCT01150331) | Fase 3 | Completado | 203 | Levetiracetam IV + clonazepam vs clonazepam solo en atención prehospitalaria de estado epiléptico tónico-clónico |
| [NCT02920060](https://clinicaltrials.gov/study/NCT02920060) | Fase 2 | Completado | 80 | Levetiracetam vs valproato en niños con estado epiléptico convulsivo refractario |
| [NCT04926844](https://clinicaltrials.gov/study/NCT04926844) | Fase 2 | Completado | 144 | Levetiracetam + midazolam en estado epiléptico convulsivo generalizado pediátrico |
| [NCT07046611](https://clinicaltrials.gov/study/NCT07046611) | Fase 2/3 | Reclutando | 124 | Ketamina + levetiracetam vs levetiracetam solo en niños |
| [NCT06907173](https://clinicaltrials.gov/study/NCT06907173) | Fase 3 | Reclutando | 770 | KESETT: dos dosis de ketamina + levetiracetam vs levetiracetam solo |
| [NCT06403150](https://clinicaltrials.gov/study/NCT06403150) | Fase 4 | Completado | 62 | Levetiracetam vs fosfenitoína en estado epiléptico convulsivo, ensayo abierto |
| [NCT04176887](https://clinicaltrials.gov/study/NCT04176887) | Fase 4 | Desconocido | 60 | Levetiracetam vs fenitoína en estado epiléptico pediátrico |
| [NCT07052136](https://clinicaltrials.gov/study/NCT07052136) | N/A | Completado | 138 | Levetiracetam vs ácido valproico en estado epiléptico pediátrico |
| [NCT07163572](https://clinicaltrials.gov/study/NCT07163572) | N/A | Completado | 152 | Brivaracetam IV vs levetiracetam en estado epiléptico pediátrico |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31774955](https://pubmed.ncbi.nlm.nih.gov/31774955/) | 2019 | ECA | N Engl J Med | Ensayo aleatorizado de tres anticonvulsivos en estado epiléptico refractario a benzodiazepinas |
| [32203691](https://pubmed.ncbi.nlm.nih.gov/32203691/) | 2020 | ECA (ESETT por grupos de edad) | Lancet | Eficacia y seguridad de levetiracetam, fosfenitoína y valproato por grupo de edad |
| [33190679](https://pubmed.ncbi.nlm.nih.gov/33190679/) | 2020 | ECA | Health Technol Assess | EcLiPSE: levetiracetam como alternativa a fenitoína de segunda línea en niños |
| [38580318](https://pubmed.ncbi.nlm.nih.gov/38580318/) | 2024 | Revisión | Semin Neurol | Actualización del manejo farmacológico; fenitoína, valproato y levetiracetam con perfiles similares |
| [38830068](https://pubmed.ncbi.nlm.nih.gov/38830068/) | 2024 | Revisión | Continuum | Manejo urgente del estado epiléptico |
| [38117319](https://pubmed.ncbi.nlm.nih.gov/38117319/) | 2024 | Revisión | Intensive Care Med | Estado epiléptico en UCI |
| [37391637](https://pubmed.ncbi.nlm.nih.gov/37391637/) | 2023 | Revisión | Pediatr Rev | Benzodiazepinas, levetiracetam, fosfenitoína y valproato pueden detener el estado epiléptico |
| [34659919](https://pubmed.ncbi.nlm.nih.gov/34659919/) | 2021 | Revisión | Cureus | Comparación entre fenitoína y levetiracetam |
| [39626562](https://pubmed.ncbi.nlm.nih.gov/39626562/) | 2025 | Guía | Brain Dev | Guías japonesas 2023 para el estado epiléptico pediátrico |
| [35333156](https://pubmed.ncbi.nlm.nih.gov/35333156/) | 2022 | Síntesis de evidencia | Health Technol Assess | Tratamiento prehospitalario y en urgencias del estado epiléptico convulsivo en adultos |

## Información de Mercado en España

Los textos de indicación aprobada no están disponibles en los datos compilados.

<!-- review:begin es-lic-20261105-levetiracetam-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Se listan 5 de las 20 autorizaciones vigentes (todas monofármaco). Los textos de indicación aprobada no están disponibles en los datos compilados." Eliminado: el número o el estado de comercialización de las autorizaciones no coincidía con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-levetiracetam-1 -->

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 86140 | LEVETIRACETAM TARBIS FARMA 250 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Tarbis Farma S.L. | Comercializada |
| 75608 | LEVETIRACETAM QUALIGEN 1000 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Neuraxpharm Spain S.L. | Comercializada |
| 83242 | LAURAK 500 MG GRANULADO EN SOBRE EFG | GRANULADO PARA SOLUCIÓN ORAL EN SOBRE | Neuraxpharm Spain S.L. | Comercializada |
| 76449 | LEVETIRACETAM COMBIX 500 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Laboratorios Combix S.L.U. | Comercializada |
| 75157 | LEVETIRACETAM SANDOZ 100 mg/ml SOLUCION ORAL EFG | SOLUCIÓN ORAL | Sandoz Farmaceutica S.A. | Comercializada |
| 83241 | LAURAK 250 MG GRANULADO EN SOBRE EFG | GRANULADO PARA SOLUCIÓN ORAL EN SOBRE | Neuraxpharm Spain S.L. | Comercializada |
| 83843 | LEVETIRACETAM ZENTIVA 100 MG/ML CONCENTRADO PARA SOLUCION PARA PERFUSION EFG | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Zentiva K.S. | Comercializada |
| 75040 | LEVETIRACETAM NORMON 250 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Laboratorios Normon S.A. | Comercializada |
| 74891 | LEVETIRACETAM ALTER 500 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Laboratorios Alter S.A. | Comercializada |
| 11702014 | LEVETIRACETAM RATIOPHARM 500 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Ratiopharm Gmbh | Autorizada, no comercializada |

Se muestran 10 de al menos 20 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas. Los datos de este informe solo incluyen parte de las autorizaciones.

<!-- licenses:end -->

La presentación intravenosa (concentrado para perfusión) es relevante para el estado epiléptico, que requiere administración parenteral.

## Consideraciones de Seguridad

- **Contraindicaciones y enfermedades de riesgo (grafo de conocimiento, no texto del prospecto):** ansiedad, trastornos neuróticos, trastorno distímico, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, trastornos psicóticos, esquizofreniforme y esquizoafectivo, trastorno mental, neutropenia, agranulocitosis, leucopenia, pancitopenia y trastorno de despersonalización.
- **Interacciones farmacológicas:** se identificaron 100 interacciones. De las 20 primeras, las de nivel moderado son morfina (incluida la liposomal), dronabinol, metoclopramida, nabilona, opio y sibutramina. Las demás (calcitriol, pantoprazol, glimepirida, mesalazina, doxiciclina, clotrimazol, metformina, omeprazol, lansoprazol, vancomicina, atropina, levocarnitina, triamcinolona) tienen nivel desconocido.
- **Señales de la literatura:** hiponatremia, hiperplasia gingival (caso aislado) y agravamiento de crisis inducido por levetiracetam (hasta 18 % en ciertas poblaciones).

Las advertencias y contraindicaciones oficiales del prospecto de AEMPS no están disponibles; consultar el prospecto.

## Otras Predicciones del Modelo (Contexto)

| Indicación | Puntaje TxGNN | Nivel | Recomendación |
|---|---|---|---|
| Déficit de beta-cetotiolasa | 0.9990 | L5 | Hold (el puntaje proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica) |

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay dos ensayos de Fase 3 completados (NCT01960075 y NCT01150331), además de ECAs publicados, que respaldan el uso de levetiracetam en el estado epiléptico. La eficacia es comparable, pero no superior, a fosfenitoína y valproato, y falta información oficial de seguridad del prospecto español.

**Para avanzar se necesita:**
- Obtener las advertencias, contraindicaciones e indicaciones aprobadas del prospecto de AEMPS (vacío crítico de datos).
- Datos detallados del mecanismo de acción (MOA) desde DrugBank.
- Verificar si la indicación de estado epiléptico ya figura en la ficha técnica española de la presentación intravenosa.
- Definir pautas de dosificación según población (pediátrica vs adulta) y ajuste en insuficiencia renal y hepática.
- Plan de monitoreo de efectos psiquiátricos, hiponatremia y alteraciones hematológicas.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Se listan 5 de las 20 autorizaciones vigentes (todas monofármaco)" | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Keppra (levetiracetam) prescribing information, UCB, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c6d5784d-abf9-45fe-ac5a-d5c53bd50f7e) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

