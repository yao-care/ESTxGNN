---
layout: default
title: Trametinib
parent: Solo predicción del modelo (L5)
nav_order: 811
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-05
monitor_inn: "TRAMETINIB"
predicted_indications: ["choroideremia"]
description: "Trametinib: nueva indicación predicha, Choroideremia (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 4 (comercializadas: 4)"
---

# Trametinib
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

## Trametinib: Choroideremia
{: .text-alpha }

**Nota sobre la selección de la indicación:** la predicción de mayor puntaje (rank 1) es la coriorremia, pero carece por completo de evidencia (L5) y de vínculo mecanístico. Esta es la indicación que sigue el formato del informe. Como contexto, el informe también señala que las predicciones de rank 2 a 10 se concentran en subtipos de melanoma, donde la evidencia es considerablemente mayor.

---

## Resumen en Una Frase

Trametinib es un inhibidor de MEK, originalmente utilizado para el tratamiento del melanoma metastásico.
El modelo TxGNN predice que podría ser efectivo para **coriorremia**, con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.
Se trata de una predicción puramente computacional, sin respaldo mecanístico conocido.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Choroideremia |
| Puntaje de Predicción TxGNN | 0.9931 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 4 de 4) |
| Número de Autorizaciones | 4 (comercializadas: 4) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Trametinib (traducción no oficial): «Trametinib es un inhibidor reversible de la activación de la cinasa 1 regulada por señales extracelulares activada por mitógenos (MEK1) y MEK2, y de la actividad cinasa de MEK1 y MEK2. Las proteínas MEK son reguladores anteriores en la vía de la cinasa relacionada con señales extracelulares (ERK), que promueve la proliferación celular.» Texto original en inglés: "Trametinib is a reversible inhibitor of mitogen-activated extracellular signal-regulated kinase 1 (MEK1) and MEK2 activation and of MEK1 and MEK2 kinase activity. MEK proteins are upstream regulators of the extracellular signal-related kinase (ERK) pathway, which promotes cellular proliferation." ([DailyMed: Mekinist (trametinib) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0002ad27-779d-42ab-83b5-bc65453412a1), versión del 2026-05-07; consultado el 2026-11-19). Según la información conocida, trametinib inhibe MEK1 y MEK2 (genes MAP2K1 y MAP2K2), componentes de la vía MAPK situados por debajo de BRAF. Su eficacia en melanoma con mutación BRAF V600 está establecida, y se usa también en combinación con dabrafenib.

La coriorremia es una degeneración retiniana ligada al cromosoma X, causada por la pérdida de función del gen CHM (REP1). No existe un vínculo establecido con la activación de la vía MAPK/MEK, por lo que el puntaje elevado (0,9931) debe interpretarse como una predicción computacional sin sustento mecanístico. No se aportaron ensayos clínicos ni literatura.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para coriorremia.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para coriorremia.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 114931002 | MEKINIST 0,5 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos |
| 114931006 | MEKINIST 2 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos |
| 1231781001 | SPEXOTRAS 0,05 mg/ml polvo para solución oral | Polvo para solución oral | No disponible en los datos |
| 114931006IP | MEKINIST 2 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos |

Titular de todas las autorizaciones: Novartis Europharm Limited.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de MEK1/MEK2) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 17 registros, 15 de ellos de nivel moderado según DDInter. Los principales son: fostamatinib, elagolix, apalutamida, brigatinib, dabrafenib, encorafenib, isavuconazonio, lasmiditán, midostaurina, sarecyclina, enzalutamida, erdafitinib, gilteritinib, idelalisib y tucatinib. Los dos registros restantes corresponden a las dianas farmacológicas de trametinib (MEK1 y MEK2).
- En los estudios sobre subtipos de melanoma se describen eventos adversos cutáneos asociados a la combinación BRAF/MEK, como la paniculitis.

No se dispone de advertencias principales ni contraindicaciones del prospecto; consultar el prospecto para esta información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para coriorremia se apoya únicamente en el puntaje del modelo (nivel L5), sin ensayos, sin literatura y sin vínculo biológico conocido entre la vía MEK y la enfermedad.

**Para avanzar se necesita:**
- Datos preclínicos que justifiquen un vínculo entre la deficiencia de CHM/REP1 y la vía MAPK/MEK
- Revisión de las predicciones de melanoma (rank 2 a 10), en particular melanoma no cutáneo y nodular, como candidatas con mayor respaldo. En el melanoma no cutáneo, el nivel L1 depende de evidencia de fase 3 externa a los datos aportados y debe verificarse de forma independiente; con los datos aportados correspondería L2. Habría que confirmar el estado de BRAF y el subtipo.
- Datos del mecanismo de acción y las advertencias y contraindicaciones del prospecto de la AEMPS
- Textos de indicación aprobada de las autorizaciones españolas

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Mekinist (trametinib) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0002ad27-779d-42ab-83b5-bc65453412a1) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

