---
layout: default
title: Metyrapone
parent: Solo predicción del modelo (L5)
nav_order: 521
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "metyrapone"
predicted_indications: ["exercise-induced malignant hyperthermia", "King-Denborough syndrome", "central core myopathy", "moderate multiminicore disease with hand involvement", "congenital multicore myopathy with external ophthalmoplegia", "myopathy, centronuclear", "familial periodic paralysis", "renal tubular acidosis", "malignant hyperthermia of anesthesia"]
description: "Metyrapone: nueva indicación predicha, Hipertermia maligna inducida por el ejercicio (nivel de evidencia L5). Indicación original: No disponible en la autorización de la AEMPS (el texto de indicación"
---

# Metyrapone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Metirapona: De Indicación Original No Especificada a Hipertermia Maligna Inducida por el Ejercicio
{: .text-alpha }

## Resumen en Una Frase

Metirapona es un inhibidor de la síntesis de cortisol, utilizado como herramienta diagnóstica de la función hipotálamo-hipofisaria y, de forma ocasional, en el tratamiento del síndrome de Cushing.
El modelo TxGNN predice que podría ser efectivo para **hipertermia maligna inducida por el ejercicio**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en la autorización de la AEMPS (el texto de indicación está vacío). Según fuentes farmacológicas: prueba diagnóstica de la función hipotálamo-hipofisaria y, ocasionalmente, síndrome de Cushing |
| Nueva Indicación Predicha | Hipertermia maligna inducida por el ejercicio |
| Puntaje de Predicción TxGNN | 0.9995 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Metyrapone (traducción no oficial): «El efecto farmacológico de Metopirone consiste en reducir la producción de cortisol y corticosterona mediante la inhibición de la reacción de 11-beta-hidroxilación en la corteza suprarrenal. La eliminación del potente mecanismo de retroalimentación inhibitoria ejercido por el cortisol da lugar a un aumento de la producción de hormona adrenocorticotrópica (ACTH) por parte de la hipófisis.» Texto original en inglés: "The pharmacological effect of Metopirone is to reduce cortisol and corticosterone production by inhibiting the 11-beta-hydroxylation reaction in the adrenal cortex. Removal of the strong inhibitory feedback mechanism exerted by cortisol results in an increase in adrenocorticotropic hormone (ACTH) production by the pituitary." ([DailyMed: Metopirone (metyrapone) prescribing information, ESTEVE PHARMACEUTICALS, S.A.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4046b167-7a46-8f4a-e063-6394a90a147f), versión del 2026-05-19; consultado el 2026-11-19). Según la información farmacológica compilada, la metirapona actúa sobre CYP11B1 (11-beta-hidroxilasa) y CYP11B2 (aldosterona sintasa), con lo que bloquea la síntesis de cortisol.

**En este caso, la predicción no resulta biológicamente plausible.** La hipertermia maligna depende de una liberación desregulada de calcio en el músculo esquelético (variantes de RYR1), una vía sin relación con la esteroidogénesis suprarrenal. El análisis no identifica ningún vínculo mecanístico establecido. El puntaje alto proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

Las demás predicciones del modelo (miopatías congénitas relacionadas con RYR1, síndrome de King-Denborough, enfermedad del núcleo central, miopatía centronuclear, otras formas de hipertermia maligna, acidosis tubular renal) siguen el mismo patrón: nivel L5, sin ensayos ni literatura. La única excepción es la parálisis periódica familiar, comentada a continuación.

### Nota sobre otra predicción con literatura

Para la **parálisis periódica familiar** (puntaje 0.9940) existe una publicación de 1971 (PMID 4322666) sobre parálisis periódica hiperpotasémica. En ella, un paciente presentó parálisis inducida por glucocorticoides, pero no por ACTH más metirapona. Es un estudio fisiológico y mecanístico, no una evaluación terapéutica; se clasifica como L4 y su relevancia es indirecta y no confirmada.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para hipertermia maligna inducida por el ejercicio.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 79004 | METOPIRONE 250 MG CAPSULAS BLANDAS | CÁPSULA BLANDA | Esteve Pharmaceuticals S.A. | Comercializada |

Se muestra la única autorización con este principio activo en los datos de CIMA (AEMPS).

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proviene del texto del prospecto): enfermedad de Addison, insuficiencia suprarrenal (incluida la primaria crónica), insuficiencia corticosuprarrenal, deficiencia familiar de glucocorticoides, hipoplasia suprarrenal congénita ligada al X, hipoplasia suprarrenal familiar con ausencia de hormona luteinizante hipofisaria, insuficiencia suprarrenal aislada hereditaria por deficiencia parcial de CYP11A1 e hiperplasia suprarrenal congénita.
- **Interacciones farmacológicas** (12 registradas):
  - Gravedad moderada: etinilestradiol, estradiol (incluida la vía tópica), estrógenos conjugados (incluida la vía tópica), mestranol, estrógenos esterificados, sulfato de estrona (incluida la vía tópica) y ciproheptadina.
  - Dianas farmacológicas: CYP11B1 y CYP11B2.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo (L5), sin ensayos ni literatura, y carece de vínculo mecanístico con la inhibición de la 11-beta-hidroxilasa. El puntaje alto proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

**Para avanzar se necesita:**
- Una hipótesis mecanística con respaldo biológico que conecte la inhibición de la síntesis de cortisol con la fisiopatología de RYR1/calcio.
- Estudios preclínicos que demuestren algún efecto en modelos de hipertermia maligna.
- Obtener y analizar el prospecto de la AEMPS (indicaciones, advertencias y contraindicaciones oficiales).
- Datos del mecanismo de acción confirmados en DrugBank.
- Si se desea explorar la parálisis periódica, revisar el texto completo de la publicación de 1971 y valorar su relevancia real.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Metopirone (metyrapone) prescribing information, ESTEVE PHARMACEUTICALS, S.A.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4046b167-7a46-8f4a-e063-6394a90a147f) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

