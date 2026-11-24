---
layout: default
title: Hemin
parent: Solo predicción del modelo (L5)
nav_order: 391
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "hemin"
predicted_indications: ["thrombocytopenic purpura", "hemophilia", "C1 inhibitor deficiency", "acquired coagulation factor deficiency", "serpinopathy with toxic serpin polymerization", "hereditary angioedema with C1Inh deficiency", "inherited thrombophilia", "symptomatic form of hemophilia in female carriers", "hereditary von Willebrand disease", "congenital factor XI deficiency"]
description: "Hemin: nueva indicación predicha, Púrpura trombocitopénica (thrombocytopenic purpura) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 1 (comercializadas: 1)"
---

# Hemin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Hemin: Púrpura trombocitopénica (thrombocytopenic purpura)
{: .text-alpha }

## Resumen en Una Frase

La hemina es un derivado del grupo hemo, utilizado originalmente para el tratamiento de la porfiria aguda intermitente.
El modelo TxGNN predice que podría ser efectiva para **púrpura trombocitopénica**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Púrpura trombocitopénica (thrombocytopenic purpura) |
| Puntaje de Predicción TxGNN | 0.9979 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Hemin (traducción no oficial): «El hemo actúa limitando la síntesis hepática y/o medular de porfirina. Es probable que esta acción se deba a la inhibición de la δ-aminolevulínico sintetasa, la enzima que limita la velocidad de la vía biosintética de la porfirina/hemo.» Texto original en inglés: "Heme acts to limit the hepatic and/or marrow synthesis of porphyrin. This action is likely due to the inhibition of δ-aminolevulinic acid synthetase, the enzyme which limits the rate of the porphyrin/heme biosynthetic pathway." ([DailyMed: Panhematin (hemin) prescribing information, Recordati Rare Diseases, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9984267a-4d57-4444-9bb5-16bca7dea691), versión del 2026-02-26; consultado el 2026-11-19). Según la información conocida, la hemina induce la hemooxigenasa-1 y reprime la ALA sintasa hepática, lo que explica su utilidad en la porfiria aguda intermitente, donde frena la sobreproducción de precursores porfirínicos.

No se ha establecido un vínculo mecanístico directo con la púrpura trombocitopénica. Un posible papel inmunomodulador a través de la hemooxigenasa-1 en la trombocitopenia inmune es meramente especulativo. La relación entre ambas indicaciones es, por tanto, débil, y el alto puntaje de TxGNN debe interpretarse como una señal computacional sin respaldo clínico.

Conviene señalar que las otras nueve predicciones principales (hemofilia, deficiencia de inhibidor de C1, déficit adquirido de factores de coagulación, trombofilia hereditaria, enfermedad de von Willebrand, etc.) tampoco cuentan con evidencia clínica. Además, la hemina puede tener un efecto anticoagulante transitorio, lo que va en contra de un beneficio en trastornos de la coagulación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la púrpura trombocitopénica.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 63116 | NORMOSANG 25 mg/ml CONCENTRADO PARA SOLUCION PARA PERFUSION | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Recordati Rare Diseases | Comercializada |

Se muestra la única autorización con este principio activo en los datos de CIMA (AEMPS).

<!-- licenses:end -->

Titular: Recordati Rare Diseases.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 74 interacciones en total. Entre las mostradas:
  - **Mayores**: etinilestradiol, estradiol, estrógenos conjugados, butalbital, amobarbital y fenobarbital.
  - **Moderadas**: ácido acetilsalicílico, abciximab, alteplasa, anagrelida, antitrombina III (humana y alfa), apixabán, dipiridamol, acalabrutinib, avapritinib, betrixabán, ibritumomab tiuxetán, tositumomab (I-131) y trastuzumab emtansina.
  
  Destaca el patrón de interacción con antitrombóticos y antiagregantes, coherente con el posible efecto anticoagulante de la hemina.
- Se ha descrito tromboflebitis en el lugar de la perfusión.

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para púrpura trombocitopénica se basa únicamente en el modelo (nivel L5), sin ensayos clínicos, sin literatura específica y sin vínculo mecanístico establecido. El efecto anticoagulante transitorio de la hemina añade dudas sobre su aplicabilidad.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (p. ej., desde DrugBank)
- Revisión del prospecto de la AEMPS (advertencias y contraindicaciones) para completar el análisis de seguridad
- Estudios preclínicos o de mecanismo que evalúen el papel de la hemooxigenasa-1 en la trombocitopenia inmune
- Revisión sistemática de la literatura específica sobre hemina y púrpura trombocitopénica
- Evaluación de la compatibilidad de la vía de administración y de la similitud con la indicación original

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Panhematin (hemin) prescribing information, Recordati Rare Diseases, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9984267a-4d57-4444-9bb5-16bca7dea691) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

