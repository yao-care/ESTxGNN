---
layout: default
title: Ezetimibe
parent: Solo predicción del modelo (L5)
nav_order: 323
evidence_level: L5
indication_count: 1
monitor_inn: "Ezetimibe"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-11-24
description: "Ezetimibe: nueva indicación predicha, Deficiencia de la proteína de transferencia de ésteres de colesterol (cholesterol-ester transfer protein deficiency) (nivel de evidencia L5). Indicación original…"
---

# Ezetimibe
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

## Ezetimibe: Deficiencia de la proteína de transferencia de ésteres de colesterol (cholesterol-ester transfer protein deficiency)
{: .text-alpha }

## Resumen en Una Frase

Ezetimiba es un inhibidor de la absorción intestinal de colesterol, utilizado originalmente en el tratamiento de la hiperlipidemia (incluidas la hipercolesterolemia familiar homocigota y la sitosterolemia).
El modelo TxGNN predice que podría ser efectivo para la **deficiencia de la proteína de transferencia de ésteres de colesterol (CETP)**, pero actualmente hay **0 ensayos clínicos** y **2 publicaciones** de carácter general que no estudian directamente esta enfermedad.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Deficiencia de la proteína de transferencia de ésteres de colesterol (cholesterol-ester transfer protein deficiency) |
| Puntaje de Predicción TxGNN | 0.9909 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 13; autorizadas no comercializadas: 1; revocadas o suspendidas: 6) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Ezetimiba inhibe la absorción intestinal de colesterol mediante su acción sobre NPC1L1 (transportador de colesterol intracelular tipo Niemann-Pick C1), lo que reduce el colesterol LDL. Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Ezetimibe (traducción no oficial): «La ezetimiba reduce el colesterol en sangre al inhibir la absorción del colesterol en el intestino delgado. Se ha demostrado que la diana molecular de la ezetimiba es el transportador de esteroles Niemann-Pick C1-Like 1 (NPC1L1), que participa en la captación intestinal del colesterol y de los fitoesteroles.» Texto original en inglés: "Ezetimibe reduces blood cholesterol by inhibiting the absorption of cholesterol by the small intestine. The molecular target of ezetimibe has been shown to be the sterol transporter, Niemann-Pick C1-Like 1 (NPC1L1), which is involved in the intestinal uptake of cholesterol and phytosterols." ([DailyMed: ezetimibe prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c37c695b-fb40-423c-9b73-d1aa58a34db9), versión del 2026-10-08; consultado el 2026-11-19).

La deficiencia de CETP es una condición genética caracterizada por colesterol HDL elevado y una transferencia reducida de ésteres de colesterol entre lipoproteínas. La única relación con la indicación original es el solapamiento en el metabolismo lipídico, ya que ambas condiciones implican el manejo del colesterol en las lipoproteínas.

Es importante ser cautos: la puntuación alta de TxGNN es una predicción computacional. No hay evidencia mecanística ni clínica directa de que ezetimiba trate la deficiencia de CETP, y esta condición suele ser un fenotipo lipídico benigno o incluso protector, por lo que la necesidad terapéutica no está clara.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40911366](https://pubmed.ncbi.nlm.nih.gov/40911366/) | 2025 | Revisión | European Heart Journal | Panorama de dianas para reducir lípidos (estatinas, triglicéridos, apoB, Lp(a)); contexto general, no estudia la deficiencia de CETP con ezetimiba |
| [31779098](https://pubmed.ncbi.nlm.nih.gov/31779098/) | 2019 | Estudio preclínico en animales | International Journal of Molecular Sciences | Modelo de hámster con Ldlr heterocigoto para evaluar un anticuerpo anti-PCSK9 en hiperlipidemia y aterosclerosis; no evalúa ezetimiba en deficiencia de CETP |

Ninguna de las publicaciones estudia directamente la deficiencia de CETP como enfermedad tratada con ezetimiba.

## Información de Mercado en España

Se muestran 5 de las al menos 20 autorizaciones (la lista puede ser parcial). Los textos de indicación aprobada no figuran en los datos compilados.

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 79108 | EZETIMIBA VIATRIS 10 MG COMPRIMIDOS EFG | COMPRIMIDO | Viatris Limited | Comercializada |
| 31-267-03-C | EZETROL 10 mg COMPRIMIDOS | COMPRIMIDO | Organon N.V. | Comercializada |
| 82832 | EZETIMIBA ALMUS 10 MG COMPRIMIDOS EFG | COMPRIMIDO | Almus Farmaceutica S.A.U. | Comercializada |
| 81631 | EZETIMIBA ALTER 10 MG COMPRIMIDOS EFG | COMPRIMIDO | Laboratorios Alter S.A. | Comercializada |
| 78507 | EZETIMIBA COMBIX 10 MG COMPRIMIDOS EFG | COMPRIMIDO | Laboratorios Combix S.L.U. | Comercializada |

Se muestran 5 de al menos 20 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas. Los datos de este informe solo incluyen parte de las autorizaciones.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Contraindicaciones (relaciones recogidas en el grafo de conocimiento, no texto de prospecto)**: pancreatitis, enfermedad hepática, enfermedad de la vesícula biliar, miopatía, enfermedad muscular, enfermedad del músculo esquelético, parálisis periódica familiar, abuso/dependencia de sustancias, rabdomiólisis y fascitis nodular.
- **Interacciones farmacológicas**: la consulta no identificó interacciones con otros fármacos; solo se registra la diana farmacológica NPC1L1.

Consultar el prospecto para confirmar las advertencias y contraindicaciones oficiales.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5): no hay ensayos clínicos ni estudios que analicen directamente la deficiencia de CETP con ezetimiba, y la necesidad terapéutica es dudosa, dado que esta condición suele ser benigna.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción y su vínculo con la deficiencia de CETP
- Estudios preclínicos o clínicos que evalúen directamente ezetimiba en esta condición
- Justificación clínica de la necesidad terapéutica
- Advertencias y contraindicaciones oficiales del prospecto de la AEMPS

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: ezetimibe prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c37c695b-fb40-423c-9b73-d1aa58a34db9) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

