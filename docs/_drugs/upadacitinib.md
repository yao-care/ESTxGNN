---
layout: default
title: Upadacitinib
parent: Solo predicción del modelo (L5)
nav_order: 834
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-25
monitor_inn: "UPADACITINIB"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
description: "Upadacitinib: nueva indicación predicha, Síndrome de microftalmia colobomatosa con displasia rizomélica (colobomatous microphthalmia-rhizomelic dysplasia syndro… (nivel de evidencia L5). Indicación o…"
---

# Upadacitinib
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

## Upadacitinib: Síndrome de microftalmia colobomatosa con displasia rizomélica (colobomatous microphthalmia-rhizomelic dysplasia syndrome)
{: .text-alpha }

## Resumen en Una Frase

Upadacitinib es un inhibidor selectivo de JAK1, originalmente utilizado para el tratamiento de la artritis reumatoide.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de microftalmia colobomatosa con displasia rizomélica**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Síndrome de microftalmia colobomatosa con displasia rizomélica (colobomatous microphthalmia-rhizomelic dysplasia syndrome) |
| Puntaje de Predicción TxGNN | 0.9961 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 3 de 5; autorizadas no comercializadas: 2) |
| Número de Autorizaciones | 5 (comercializadas: 3) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Upadacitinib (traducción no oficial): «El upadacitinib es un inhibidor de las cinasas Janus (JAK). Las JAK son enzimas intracelulares que transmiten señales derivadas de las interacciones entre citocinas o factores de crecimiento y sus receptores en la membrana celular para influir en los procesos celulares de la hematopoyesis y la función de las células inmunitarias.» Texto original en inglés: "Upadacitinib is a Janus kinase (JAK) inhibitor. JAKs are intracellular enzymes which transmit signals arising from cytokine or growth factor-receptor interactions on the cellular membrane to influence cellular processes of hematopoiesis and immune cell function." ([DailyMed: Rinvoq (upadacitinib) prescribing information, AbbVie Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2966aec7-2ef0-923c-d8ff-fe1a957bf095), versión del 2026-06-30; consultado el 2026-11-19). Según la información conocida, upadacitinib es un inhibidor selectivo de JAK1 que se emplea en enfermedades inflamatorias de base inmunitaria, y su eficacia en artritis reumatoide está establecida.

Sin embargo, **los datos disponibles no respaldan un vínculo mecanístico** con la nueva indicación. Este síndrome es un trastorno del desarrollo extremadamente raro, con malformaciones oculares y esqueléticas, y en general no está impulsado por inflamación mediada por la vía JAK-STAT. El puntaje del modelo TxGNN (aprendizaje profundo) es muy alto (0.9961), pero es una predicción derivada del modelo; puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

Como segunda predicción, el modelo propone el **síndrome de braquidactilia-sindactilia** (puntaje 0,9958), también una malformación congénita de origen genético y del desarrollo, sin respuesta esperable a la inmunomodulación en pacientes posnatales. Tampoco cuenta con evidencia clínica ni bibliográfica y recibe la misma recomendación de Hold.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 1191404001 | RINVOQ 15 MG COMPRIMIDOS DE LIBERACION PROLONGADA | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Abbvie Deutschland Gmbh & Co. Kg | Comercializada |
| 1191404010 | RINVOQ 45 MG COMPRIMIDOS DE LIBERACION PROLONGADA | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Abbvie Deutschland Gmbh & Co. Kg | Comercializada |
| 1191404006 | RINVOQ 30 MG COMPRIMIDOS DE LIBERACION PROLONGADA | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Abbvie Deutschland Gmbh & Co. Kg | Comercializada |
| 1191404006IP | RINVOQ 30 MG COMPRIMIDOS DE LIBERACION PROLONGADA | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Abbvie Deutschland Gmbh & Co. Kg | Autorizada, no comercializada |
| 1191404012 | RINVOQ 1MG/ML SOLUCION ORAL | SOLUCIÓN ORAL | Abbvie Deutschland Gmbh & Co. Kg | Autorizada, no comercializada |

Se muestran las 5 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

Titular: Abbvie Deutschland GmbH & Co.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; a continuación se muestran las principales de la muestra consultada.
  - **Gravedad mayor**: corticoides (hidrocortisona, triamcinolona, dexametasona, beclometasona, betametasona, budesonida, prednisona, prednisolona), claritromicina, cobicistat, deferiprona e iobenguano (I-131).
  - **Gravedad moderada**: aprepitant, cimetidina, miconazol y deferasirox.
  - **Gravedad menor**: sales de zinc (sulfato, acetato, gluconato).

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y carece de plausibilidad biológica: ambos síndromes predichos son malformaciones congénitas del desarrollo sin un componente inflamatorio mediado por JAK1 que justifique el tratamiento.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) de upadacitinib y un análisis de su posible relación con la fisiopatología del síndrome.
- Revisión de la ficha técnica de AEMPS (advertencias y contraindicaciones), actualmente no disponible.
- Evidencia preclínica o biológica que vincule la vía JAK1-STAT con el síndrome predicho.
- Una revisión sistemática de la literatura y de registros de ensayos que confirme la ausencia de estudios.
- Considerar priorizar otras indicaciones predichas con mayor plausibilidad mecanística.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Rinvoq (upadacitinib) prescribing information, AbbVie Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2966aec7-2ef0-923c-d8ff-fe1a957bf095) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

