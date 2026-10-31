---
layout: default
title: Rosuvastatin
parent: Solo predicción del modelo (L5)
nav_order: 713
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-31
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
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 12) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, rosuvastatina es una estatina cuya diana farmacológica registrada es la HMG-CoA reductasa (gen *HMGCR*). Su eficacia en dislipidemias ha sido comprobada, y la predicción se apoya en la proximidad entre ambas enfermedades dentro del metabolismo lipídico.

La relación con la indicación original es débil. La deficiencia de CETP **eleva el colesterol HDL y reduce el LDL**. Por eso, reducir el colesterol LDL con una estatina no encaja de forma evidente como tratamiento. No se identificaron ensayos clínicos ni literatura que respalden la hipótesis.

La puntuación alta del modelo TxGNN (aprendizaje profundo) (0.9954) puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. No constituye evidencia clínica. Con los datos actuales, la aplicabilidad mecanística es solo especulativa.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Hay 20 autorizaciones vigentes, todas de medicamentos con un único principio activo y en forma de comprimido recubierto con película. Se muestran las 5 primeras. Los textos de indicación aprobada no estaban disponibles en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 82539 | Rosuvastatina Vir 5 mg EFG | Comprimido recubierto con película |
| 82543 | Rosuvastatina Farmaprojects 10 mg EFG | Comprimido recubierto con película |
| 86107 | Vaxar 10 mg EFG | Comprimido recubierto con película |
| 86108 | Vaxar 20 mg EFG | Comprimido recubierto con película |
| 70335 | Crestor 40 mg | Comprimido recubierto con película |

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
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

