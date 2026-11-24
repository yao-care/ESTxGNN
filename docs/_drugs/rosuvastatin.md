---
layout: default
title: Rosuvastatin
parent: Solo predicción del modelo (L5)
nav_order: 713
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
monitor_inn: "Rosuvastatin"
predicted_indications: ["cholesterol-ester transfer protein deficiency", "brain stem infarction", "HIV infectious disease", "hypoalphalipoproteinemia", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "ABri amyloidosis"]
description: "Rosuvastatin: nueva indicación predicha, Deficiencia de la proteína de transferencia de ésteres de colesterol (cholesterol-ester transfer protein deficiency) (nivel de evidencia L5). Indicación origi…"
---

# Rosuvastatin
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

## Rosuvastatin: Deficiencia de la proteína de transferencia de ésteres de colesterol (cholesterol-ester transfer protein deficiency)
{: .text-alpha }

## Resumen en Una Frase

Rosuvastatina es una estatina utilizada originalmente para tratar la hipertrigliceridemia, la hipercolesterolemia familiar homocigota y otras dislipidemias, así como la enfermedad aterosclerótica y cerebrovascular.
El modelo TxGNN predice que podría ser efectiva para la **deficiencia de la proteína de transferencia de ésteres de colesterol (CETP)**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es una predicción exclusivamente del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Deficiencia de la proteína de transferencia de ésteres de colesterol (cholesterol-ester transfer protein deficiency) |
| Puntaje de Predicción TxGNN | 0.9954 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 12; autorizadas no comercializadas: 4; revocadas o suspendidas: 4) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Rosuvastatin (traducción no oficial): «CRESTOR es un inhibidor de la HMG‑CoA reductasa, la enzima limitante de la velocidad que convierte la 3‑hidroxi‑3‑metilglutaril coenzima A en mevalonato, un precursor del colesterol.» Texto original en inglés: "CRESTOR is an inhibitor of HMG‑CoA reductase, the rate-limiting enzyme that converts 3‑hydroxy‑3‑methylglutaryl coenzyme A to mevalonate, a precursor of cholesterol." ([DailyMed: Crestor (rosuvastatin) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=325a5d0e-9a72-4015-9fcd-1655fb504cee), versión del 2026-09-23; consultado el 2026-11-19). Según la información conocida, rosuvastatina es una estatina cuya diana farmacológica registrada es la HMG-CoA reductasa (gen *HMGCR*). Su eficacia en dislipidemias ha sido comprobada, y la predicción se apoya en la proximidad entre ambas enfermedades dentro del metabolismo lipídico.

La relación con la indicación original es débil. La deficiencia de CETP **eleva el colesterol HDL y reduce el LDL**. Por eso, reducir el colesterol LDL con una estatina no encaja de forma evidente como tratamiento. No se identificaron ensayos clínicos ni literatura que respalden la hipótesis.

La puntuación alta del modelo TxGNN (aprendizaje profundo) (0.9954) puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. No constituye evidencia clínica. Con los datos actuales, la aplicabilidad mecanística es solo especulativa.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran las 5 primeras. Los textos de indicación aprobada no estaban disponibles en los datos compilados.

<!-- review:begin es-lic-20261105-rosuvastatin-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Hay 20 autorizaciones vigentes, todas de medicamentos con un único principio activo y en forma de comprimido recubierto con película. Se muestran las 5 primeras." Eliminado: el número o el estado de comercialización de las autorizaciones no coincidía con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-rosuvastatin-1 -->

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 82539 | ROSUVASTATINA VIR 5 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Industria Quimica Y Farmaceutica Vir S.A. | Comercializada |
| 86107 | VAXAR 10 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Adamed Laboratorios S.L.U. | Comercializada |
| 86108 | VAXAR 20 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Adamed Laboratorios S.L.U. | Comercializada |
| 86110 | VAXAR 5 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Adamed Laboratorios S.L.U. | Comercializada |
| 81846 | ROSUVASTATINA KRKA 30 MG COMPRIMIDOS RECUBIERTOS CON PELICULA | COMPRIMIDO RECUBIERTO CON PELÍCULA | Krka D.D. Novo Mesto | Comercializada |

Se muestran 5 de al menos 20 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas. Los datos de este informe solo incluyen parte de las autorizaciones.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Contraindicaciones y enfermedades de riesgo (según el grafo de conocimiento, no según el prospecto)**: enfermedad hepática, enfermedad de la vesícula biliar, hipotiroidismo (incluidos mixedema e hipotiroidismo congénito), miopatía y enfermedades musculares, parálisis periódica familiar, abuso o dependencia de sustancias, rabdomiólisis, fascitis nodular, lesiones y proteinuria.
- **Interacciones farmacológicas**: la consulta se completó, pero solo devolvió la diana farmacológica (HMG-CoA reductasa). No hay interacciones medicamentosas específicas documentadas.

Para las advertencias formales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos ni publicaciones. Además, la fisiopatología de la deficiencia de CETP (HDL elevado y LDL bajo) no sugiere beneficio de una estatina.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones oficiales de AEMPS).
- Una justificación fisiopatológica de por qué una estatina aportaría beneficio en la deficiencia de CETP.
- Estudios preclínicos o series de casos que sustenten la hipótesis.

**Nota:** en los datos compilados, otras indicaciones predichas tienen mucho más respaldo, como la hipercolesterolemia familiar y la hiperlipidemia (ambas L1, "Proceed with Guardrails"). Sin embargo, son usos prácticamente dentro de ficha técnica y no un reposicionamiento propiamente dicho.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Hay 20 autorizaciones vigentes, todas de medicamentos con un único principio activo y en forma de comprimido recubierto con película" | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Crestor (rosuvastatin) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=325a5d0e-9a72-4015-9fcd-1655fb504cee) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

