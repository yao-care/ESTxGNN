---
layout: default
title: Propafenone
parent: Solo predicción del modelo (L5)
nav_order: 668
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
monitor_inn: "Propafenone"
predicted_indications: ["manic bipolar affective disorder", "periodic paralysis with transient compartment-like syndrome", "Prinzmetal angina", "arrhythmogenic right ventricular cardiomyopathy", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania"]
description: "Propafenone: nueva indicación predicha, Trastorno bipolar maníaco (manic bipolar affective disorder) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 5 (comercializadas: 3)"
---

# Propafenone
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

## Propafenone: Trastorno bipolar maníaco (manic bipolar affective disorder)
{: .text-alpha }

## Resumen en Una Frase

La propafenona es un antiarrítmico utilizado originalmente en el tratamiento de la fibrilación auricular y de la taquicardia ventricular.
El modelo TxGNN predice que podría ser efectiva para el **trastorno bipolar maníaco**, pero **no hay ensayos clínicos** y solo hay **3 publicaciones** (una revisión y dos reportes de caso), que describen **riesgos de seguridad** y no un beneficio terapéutico.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Trastorno bipolar maníaco (manic bipolar affective disorder) |
| Puntaje de Predicción TxGNN | 0.9980 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 3 de 5; revocadas o suspendidas: 2) |
| Número de Autorizaciones | 5 (comercializadas: 3) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Propafenone (traducción no oficial): «La propafenona es un fármaco antiarrítmico de clase 1C con efectos anestésicos locales y una acción estabilizadora directa sobre las membranas miocárdicas. El efecto electrofisiológico de la propafenona se manifiesta en una reducción de la velocidad de ascenso (fase 0) del potencial de acción monofásico.» Texto original en inglés: "Propafenone is a Class 1C antiarrhythmic drug with local anesthetic effects, and a direct stabilizing action on myocardial membranes. The electrophysiological effect of propafenone manifests itself in a reduction of upstroke velocity (Phase 0) of the monophasic action potential." ([DailyMed: propafenone hydrochloride prescribing information, Northstar Rx LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2ecd6452-ccc3-493f-9a4a-69f0fbf67a42), versión del 2026-06-04; consultado el 2026-11-19). Según la información conocida, la propafenona es un antiarrítmico con eficacia comprobada en arritmias auriculares y ventriculares. Los datos compilados la vinculan farmacológicamente con los receptores β1 y β2 adrenérgicos y con el canal de potasio Kv1.5.

**En este caso, la predicción no es razonable desde el punto de vista mecanístico.** No se identifica ningún mecanismo terapéutico plausible que conecte un antiarrítmico cardíaco con el tratamiento de la manía. La literatura recuperada describe a la propafenona como una posible **causa** de manía (reporte de caso de 1985) y como fuente de interacciones medicamentosas (psicosis orgánica por interacción con venlafaxina en 2001; interacciones entre antipsicóticos y fármacos cardiovasculares en 2020).

El puntaje alto del modelo parece reflejar una asociación en la red con efectos adversos psiquiátricos y con la comorbilidad cardiovascular en pacientes bipolares, no una señal de eficacia. Debe interpretarse como una señal de seguridad y no como una oportunidad de reposicionamiento.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32124390](https://pubmed.ncbi.nlm.nih.gov/32124390/) | 2020 | Revisión | Pharmacological Reports | Evalúa interacciones perjudiciales entre antipsicóticos y fármacos cardiovasculares, dada la alta comorbilidad entre trastorno bipolar o esquizofrenia y enfermedad cardiovascular |
| [11949740](https://pubmed.ncbi.nlm.nih.gov/11949740/) | 2001 | Reporte de caso | International Journal of Psychiatry in Medicine | Psicosis orgánica por interacción venlafaxina-propafenona en un paciente con trastorno bipolar |
| [2579063](https://pubmed.ncbi.nlm.nih.gov/2579063/) | 1985 | Reporte de caso | Journal of Clinical Psychiatry | Caso de manía secundaria a propafenona; se plantea como complicación no reconocida previamente |

Ninguna de estas publicaciones demuestra un beneficio de la propafenona en la manía.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 55538 | RYTMONORM 150 mg COMPRIMIDOS RECUBIERTOS | COMPRIMIDO RECUBIERTO | Teva B.V. | Comercializada |
| 55541 | RYTMONORM 300 mg COMPRIMIDOS RECUBIERTOS | COMPRIMIDO RECUBIERTO | Teva B.V. | Comercializada |
| 58275 | RYTMONORM 3,5 mg/ml SOLUCION INYECTABLE | SOLUCIÓN INYECTABLE | Teva B.V. | Comercializada |
| 82299 | PROPAFENONA HIDROCLORURO ACCORD 300 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Accord Healthcare S.L.U. | Revocada |
| 82298 | PROPAFENONA HIDROCLORURO ACCORD 150 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Accord Healthcare S.L.U. | Revocada |

Se muestran las 5 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

Los textos de indicación aprobada no figuran en los datos compilados.

<!-- review:begin es-lic-20261105-propafenone-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Las 5 autorizaciones están vigentes y son de monofármaco. Los textos de indicación aprobada no figuran en los datos compilados." Eliminado: el número o el estado de comercialización de las autorizaciones no coincidía con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en España. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-propafenone-1 -->

## Consideraciones de Seguridad

- **Contraindicaciones o enfermedades de riesgo según el grafo de conocimiento** (no proceden del texto del prospecto):
  - Cardiovasculares: síndrome de QT largo (incluida la forma familiar), torsades de pointes, infarto de miocardio, enfermedad coronaria, aterosclerosis e hipotensión.
  - Metabólicas y orgánicas: hipopotasemia, hepatopatía, enfermedad de la vesícula biliar y nefropatía.
  - Neuromusculares: miastenia gravis.
  - Hematológicas: agranulocitosis y neutropenia, incluidas las formas congénitas.
- **Interacciones y señales de seguridad en este contexto**: la literatura recuperada documenta una posible inducción de manía y una interacción con venlafaxina que causó psicosis orgánica. Esto es especialmente relevante en pacientes con trastorno bipolar.

Para el resto de la información de seguridad, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (L5), sin ensayos clínicos, y la literatura disponible indica que la propafenona puede inducir manía o interactuar con psicofármacos. No hay base para avanzar en esta indicación.

**Para avanzar se necesita:**
- Datos del mecanismo de acción que justifiquen un efecto antimaníaco, algo que hoy no existe.
- Estudios preclínicos que demuestren un efecto terapéutico y no solo una asociación con efectos adversos psiquiátricos.
- Revisión de las advertencias y contraindicaciones del prospecto de la AEMPS.

Cuenta con estudios preclínicos sobre el bloqueo del receptor de rianodina RyR2, cohortes observacionales y un reporte de 35 años de tratamiento eficaz con propafenona. Se sitúa en el nivel L3 y se recomienda como "Proceed with Guardrails". Las salvaguardas son descartar cardiopatía estructural, usar un betabloqueante como terapia base y vigilar de cerca el ECG y la anchura del QRS. Conviene evaluarla en un informe específico.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | Eliminado: "Las 5 autorizaciones están vigentes y son de monofármaco" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: propafenone hydrochloride prescribing information, Northstar Rx LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2ecd6452-ccc3-493f-9a4a-69f0fbf67a42) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

