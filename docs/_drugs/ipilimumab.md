---
layout: default
title: Ipilimumab
parent: Solo predicción del modelo (L5)
nav_order: 429
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-25
description: "Ipilimumab: nueva indicación predicha, Coroideremia (nivel de evidencia L5). Indicación original: Melanoma metastásico"
monitor_inn: "IPILIMUMAB"
predicted_indications: ["choroideremia"]
---

# Ipilimumab
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

## Ipilimumab: De Melanoma Metastásico a Coroideremia
{: .text-alpha }

## Resumen en Una Frase

Ipilimumab es un anticuerpo monoclonal que bloquea CTLA-4, utilizado originalmente para el tratamiento del melanoma metastásico.
El modelo TxGNN predice que podría ser efectivo para **coroideremia**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Melanoma metastásico |
| Nueva Indicación Predicha | Coroideremia |
| Puntaje de Predicción TxGNN | 0.9906 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 2 de 5; autorizadas no comercializadas: 3) |
| Número de Autorizaciones | 5 (comercializadas: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Ipilimumab bloquea el receptor CTLA-4 en los linfocitos T. Esto potencia su activación y su capacidad de atacar células tumorales, y es la base de su uso en melanoma. Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Ipilimumab (traducción no oficial): «CTLA-4 es un regulador negativo de la actividad de los linfocitos T. Ipilimumab es un anticuerpo monoclonal que se une a CTLA-4 y bloquea la interacción de CTLA-4 con sus ligandos, CD80/CD86. Se ha demostrado que el bloqueo de CTLA-4 aumenta la activación y la proliferación de los linfocitos T, incluidas la activación y la proliferación de los linfocitos T efectores infiltrantes de tumores.» Texto original en inglés: "CTLA-4 is a negative regulator of T-cell activity. Ipilimumab is a monoclonal antibody that binds to CTLA-4 and blocks the interaction of CTLA-4 with its ligands, CD80/CD86. Blockade of CTLA-4 has been shown to augment T-cell activation and proliferation, including the activation and proliferation of tumor infiltrating T-effector cells." ([DailyMed: Yervoy (ipilimumab) prescribing information, E.R. Squibb & Sons, L.L.C.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2265ef30-253e-11df-8a39-0800200c9a66), versión del 2026-08-20; consultado el 2026-11-20).

**La relación mecanística con la coroideremia es muy débil.** La coroideremia es una degeneración retiniana hereditaria ligada al cromosoma X, causada por la pérdida de función del gen *CHM* (REP1). Su patología consiste en la degeneración progresiva del epitelio pigmentario de la retina, los fotorreceptores y la coroides. No depende de la evasión inmune tumoral, que es el proceso sobre el que actúa ipilimumab.

Además, la inhibición de puntos de control inmunitarios puede provocar eventos adversos oculares inmunomediados (por ejemplo, uveítis), lo que supondría un riesgo adicional en una retina ya vulnerable. La puntuación alta proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 11698001 | YERVOY 5 MG/ML CONCENTRADO PARA SOLUCION PARA PERFUSION | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Bristol-Myers Squibb Pharma Eeig | Comercializada |
| 11698002 | YERVOY 5 MG/ML CONCENTRADO PARA SOLUCION PARA PERFUSION | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Bristol-Myers Squibb Pharma Eeig | Comercializada |
| 11698001IP | YERVOY 5 MG/ML CONCENTRADO PARA SOLUCION PARA PERFUSION | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Bristol-Myers Squibb Pharma Eeig | Autorizada, no comercializada |
| 11698001IP1 | YERVOY 5 MG/ML CONCENTRADO PARA SOLUCION PARA PERFUSION | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Bristol-Myers Squibb Pharma Eeig | Autorizada, no comercializada |
| 11698002IP | YERVOY 5 MG/ML CONCENTRADO PARA SOLUCION PARA PERFUSION | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Bristol-Myers Squibb Pharma Eeig | Autorizada, no comercializada |

Se muestran las 5 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

Todas las autorizaciones están vigentes y corresponden a medicamentos de un único principio activo. Los datos compilados no incluyen el texto de la indicación aprobada para estas autorizaciones.

<!-- review:begin es-lic-20261125-ipilimumab-1 -->

> **Corrección de revisión (2026-11-25)**: Texto original: "Las tres autorizaciones están vigentes y corresponden a medicamentos de un único principio activo." Corregido: desde el 2026-11-25 se incorporan a los datos las autorizaciones de CIMA (AEMPS) posteriores a marzo de 2026 (incluidas importaciones paralelas) con el mismo criterio de recogida; la frase ya no coincidía con ellas. Las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en España. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261125-ipilimumab-1 -->

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (anticuerpo monoclonal anti-CTLA-4); no es un citotóxico convencional |
| Riesgo de Mielosupresión | Bajo; el riesgo principal son los eventos adversos inmunomediados y no la supresión medular directa |
| Clasificación de Emetogenicidad | Baja |
| Items de Monitoreo | Hemograma, función hepática, función renal, función tiroidea y suprarrenal, glucemia; vigilancia de síntomas oculares, cutáneos y gastrointestinales |
| Protección en Manejo | Manejo estándar de preparados parenterales; consultar las advertencias y precauciones del prospecto |

Esta información se basa en conocimiento general de la clase farmacológica. Los datos compilados no incluyen datos específicos de toxicidad.

---

## Consideraciones de Seguridad

- **Riesgo ocular:** la inhibición de puntos de control inmunitarios puede causar eventos adversos oculares inmunomediados (por ejemplo, uveítis), un riesgo especialmente relevante en una retina ya degenerada.
- **Interacciones farmacológicas:** se identificaron 100 interacciones. Las principales entre las 20 revisadas son:
  - **Gravedad mayor:** anticoagulantes (apixabán, betrixabán, bivalirudina, dalteparina, desirudina, edoxabán, argatrobán, danaparoide).
  - **Gravedad moderada:** corticoides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida, prednisolona, prednisona), metronidazol, tinidazol, naltrexona, y estatinas (rosuvastatina, simvastatina).

Para el resto de la información de seguridad, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para coroideremia carece de ensayos clínicos y de literatura, y su nivel de evidencia es L5. Además, no existe un vínculo mecanístico plausible entre el bloqueo de CTLA-4 y una enfermedad degenerativa monogénica, y existe un riesgo ocular inmunomediado.

**Para avanzar se necesita:**
- Un fundamento biológico que justifique el uso de un inhibidor de puntos de control en una degeneración retiniana hereditaria. Hasta ahora no se ha identificado ninguno.
- Estudios preclínicos en modelos de coroideremia que evalúen eficacia y seguridad ocular.
- Revisión de las alternativas terapéuticas ya dirigidas a la causa de la enfermedad (por ejemplo, enfoques de terapia génica).
- Verificación del texto de indicaciones, advertencias y contraindicaciones en la ficha técnica vigente de la AEMPS.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-20 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Yervoy (ipilimumab) prescribing information, E.R. Squibb & Sons, L.L.C.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2265ef30-253e-11df-8a39-0800200c9a66) |
| 2026-11-25 | «Las tres» → todas | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

