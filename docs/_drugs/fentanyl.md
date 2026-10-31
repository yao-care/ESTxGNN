---
layout: default
title: Fentanyl
parent: Solo predicción del modelo (L5)
nav_order: 331
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-31
description: "Fentanyl: nueva indicación predicha, Síndrome nefrogénico de antidiuresis inapropiada (nivel de evidencia L5). Indicación original: No disponible en los datos compilados para este informe"
monitor_inn: "fentanyl"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "Tourette syndrome"]
---

# Fentanyl
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Fentanilo: De Indicación Original No Especificada a Síndrome Nefrogénico de Antidiuresis Inapropiada
{: .text-alpha }

## Resumen en Una Frase

Fentanilo es un opioide agonista del receptor mu, comercializado en España en parches transdérmicos y en formas de administración transmucosa (comprimidos bucales, sublinguales, para chupar y película bucal). El modelo TxGNN predice que podría ser efectivo para el **síndrome nefrogénico de antidiuresis inapropiada**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, por lo que la predicción debe considerarse puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados para este informe |
| Nueva Indicación Predicha | Síndrome nefrogénico de antidiuresis inapropiada |
| Puntaje de Predicción TxGNN | 0,9946 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 17) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Por farmacología general, el fentanilo es un agonista potente del receptor opioide mu, utilizado como analgésico.

El síndrome nefrogénico de antidiuresis inapropiada (SNAI) se debe a mutaciones con ganancia de función del receptor V2 de la vasopresina (AVPR2), que provocan retención de agua independiente de la vasopresina. El fentanilo no tiene acción conocida sobre el receptor V2 ni sobre su señalización posterior. Además, los opioides pueden modular la liberación central de vasopresina y se asocian a veces con efectos de tipo SIADH, lo que tendería a empeorar la antidiuresis y no a tratarla.

**No se identifica un vínculo mecanístico creíble.** El puntaje elevado de TxGNN (0,9946) probablemente sea un artefacto del modelo TxGNN (aprendizaje profundo) y carece de respaldo farmacológico.

Como segunda predicción de menor interés, el modelo propone el **síndrome de Tourette** (puntaje 0,9905, también nivel L5, decisión Hold). Existe solo una hipótesis débil e indirecta (interacción del sistema opioide con circuitos dopaminérgicos estriatales). El fentanilo es un agonista mu completo con alto potencial de abuso, riesgo de depresión respiratoria y una gran carga de interacciones (327 fármacos), por lo que es un mal candidato para una afección del neurodesarrollo que suele iniciarse en la infancia. Tampoco hay ensayos ni literatura que lo apoyen.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones vigentes (todas de principio activo único). Los textos de indicación aprobada no figuran en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 69731 | Fentanilo Matrix Sandoz 50 µg/hora | Parche transdérmico | Sandoz Farmacéutica S.A. |
| 61960 | Durogesic Matrix 50 µg/h | Parche transdérmico | Janssen Cilag S.A. |
| 64061 | Actiq 1600 µg | Comprimido para chupar con aplicador bucal | Phoenix Labs Unlimited Company |
| 76980 | Avaric 800 µg | Comprimido sublingual | Angelini Pharma España S.L. |
| 74148 | Breakyl 600 µg | Película bucal | Viatris Healthcare Limited |

## Consideraciones de Seguridad

- **Contraindicaciones potenciales (grafo de conocimiento, no texto de prospecto)**: el grafo de conocimiento asocia el fentanilo con enfermedades como hipertensión, hipotensión ortostática, síndrome de QT largo y torsades de pointes, insuficiencia y enfermedad hepática, enfermedad renal, EPOC, asma, pancreatitis, enfermedad de la vesícula biliar, enfermedad inflamatoria intestinal, hiperplasia prostática benigna, trastornos de ansiedad, deficiencia de potasio y abuso/dependencia de sustancias, entre otras.
- **Interacciones farmacológicas**: se registran 327 interacciones. Entre las de nivel **mayor** figuran alvimopán, aprepitant, bupropión, claritromicina, clotrimazol, dexametasona, dexfenfluramina, dolasetrón, fenfluramina, granisetrón y lorcaserina. Entre las de nivel **moderado**: atropina, cimetidina, clidinio, diciclomina, dronabinol, eluxadolina, glicerol fenilbutirato, glicopirronio e hiosciamina.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L5), sin ensayos ni literatura, y no existe un vínculo mecanístico plausible entre un agonista opioide mu y un defecto del receptor V2 de la vasopresina; además, los opioides podrían agravar la retención de agua. El perfil de seguridad del fentanilo (abuso, depresión respiratoria, numerosas interacciones) tampoco favorece su reposicionamiento.

**Para avanzar se necesita:**
- Datos del mecanismo de acción del fármaco y de las indicaciones autorizadas (prospecto de la AEMPS).
- Evidencia preclínica que demuestre algún efecto sobre la señalización de AVPR2 o la reabsorción renal de agua.
- Revisión formal de advertencias y contraindicaciones antes de cualquier evaluación de seguridad.
- Dado que el SNAI es una enfermedad rara, valorar si existe alguna alternativa terapéutica con racional mecanístico más sólido antes de invertir recursos en este candidato.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

