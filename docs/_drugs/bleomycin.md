---
layout: default
title: Bleomycin
parent: Solo predicción del modelo (L5)
nav_order: 109
evidence_level: L5
indication_count: 5
monitor_inn: "bleomycin"
predicted_indications: ["cauda equina neoplasm", "adult astrocytic tumour", "primary pulmonary lymphoma", "pulmonary blastoma", "well-differentiated fetal adenocarcinoma of the lung"]
last_modified_at: 2026-11-20
description: "Bleomycin: nueva indicación predicha, Neoplasia de la cauda equina (cauda equina neoplasm) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 2 (comercializadas: 1)"
---

# Bleomycin
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

## Bleomycin: Neoplasia de la cauda equina (cauda equina neoplasm)
{: .text-alpha }

## Resumen en Una Frase

Bleomicina es un antibiótico glicopéptido citotóxico que se utiliza como antineoplásico.
El modelo TxGNN predice que podría ser efectivo para **neoplasia de la cauda equina (cauda equina neoplasm)**, pero actualmente solo existe **1 publicación** indirecta y **ningún ensayo clínico** que respalde esta dirección, por lo que se trata de una hipótesis con evidencia muy débil.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Neoplasia de la cauda equina (cauda equina neoplasm) |
| Puntaje de Predicción TxGNN | 0.9930 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 2; revocadas o suspendidas: 1) |
| Número de Autorizaciones | 2 (comercializadas: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Bleomycin (traducción no oficial): «Aunque se desconoce el mecanismo de acción exacto de la bleomicina, la evidencia disponible indica que el principal modo de acción es la inhibición de la síntesis de ADN, con cierta evidencia de una inhibición menor de la síntesis de ARN y de proteínas. Se sabe que la bleomicina provoca roturas de cadena sencilla y, en menor medida, de doble cadena en el ADN.» Texto original en inglés: "Although the exact mechanism of action of bleomycin is unknown, available evidence indicates that the main mode of action is the inhibition of DNA synthesis with some evidence of lesser inhibition of RNA and protein synthesis. Bleomycin is known to cause single, and to a lesser extent, double-stranded breaks in DNA." ([DailyMed: Bleomycin (bleomycin sulfate) prescribing information, Meitheal Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=640602f9-a7df-46f0-a9b1-19c471008bee), versión del 2026-04-17; consultado el 2026-11-19). Según la información conocida, la bleomicina es un glicopéptido citotóxico que provoca roturas en las cadenas de ADN, y ese efecto es el que sustenta su uso en oncología.

No se ha establecido un vínculo directo con los tumores de la cauda equina. La única publicación recuperada trata de radioterapia en germinomas del sistema nervioso central recidivados tras quimioterapia (que incluía bleomicina), lo cual es indirecto y no demuestra un efecto de la bleomicina en esta localización.

Además, la penetración de la bleomicina a través de la barrera hematoencefálica y hematomedular es limitada, lo que reduce la plausibilidad de eficacia por vía sistémica. El puntaje alto del modelo (0,9930) es solo una predicción computacional.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9440744](https://pubmed.ncbi.nlm.nih.gov/9440744/) | 1998 | Cohorte | Journal of Clinical Oncology | Evaluación retrospectiva de la radioterapia de rescate en germinoma del SNC recidivado tras quimioterapia primaria con carboplatino, etopósido y bleomicina. Evidencia indirecta, no estudia la neoplasia de la cauda equina. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 49313 | BLEOMICINA VIATRIS 15.000 UI (PH EUR) = 15 U (USP) POLVO PARA SOLUCION INYECTABLE | Polvo para solución inyectable | No registrada en los datos locales |
| 81969 | BLEOMICINA ACCORD 15.000 UI POLVO PARA SOLUCION INYECTABLE Y PARA PERFUSION EFG | Polvo para solución inyectable | No registrada en los datos locales |

De las dos autorizaciones, una está vigente y otra cancelada.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (glicopéptido antitumoral que rompe cadenas de ADN) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Función pulmonar (la toxicidad pulmonar es el principal riesgo conocido), hemograma, función hepática y renal |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: los datos compilados registran 205 interacciones. Entre las listadas figuran levofloxacino (nivel menor) y, con nivel no clasificado, pantoprazol, palonosetrón, lactulosa, aprepitant, morfina, omeprazol, lansoprazol, vancomicina, prednisona e hidrocortisona, entre otros.
- La toxicidad pulmonar de la bleomicina es una preocupación conocida y relevante en cualquier nueva indicación.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún estudio o ensayo que investigue directamente la neoplasia de la cauda equina; la única publicación es indirecta, por lo que el nivel de evidencia es L5. El puntaje del modelo no basta por sí solo para avanzar, y la limitada penetración en el sistema nervioso central y la toxicidad pulmonar pesan en contra.

**Para avanzar se necesita:**
- Estudios preclínicos o clínicos que evalúen directamente la bleomicina en tumores de la cauda equina
- Datos del mecanismo de acción y de la penetración en el sistema nervioso central
- Información de advertencias y contraindicaciones del prospecto de la AEMPS
- Comparación con los tratamientos estándar actuales de esta neoplasia

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Bleomycin (bleomycin sulfate) prescribing information, Meitheal Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=640602f9-a7df-46f0-a9b1-19c471008bee) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

