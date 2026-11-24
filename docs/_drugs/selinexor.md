---
layout: default
title: Selinexor
parent: Solo predicción del modelo (L5)
nav_order: 729
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Selinexor: nueva indicación predicha, Osteoporosis inducida por fármacos (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (el texto de indicación de la a…"
monitor_inn: "SELINEXOR"
predicted_indications: ["drug-induced osteoporosis"]
---

# Selinexor
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

## Selinexor: De Indicación Original No Disponible a Osteoporosis Inducida por Fármacos
{: .text-alpha }

## Resumen en Una Frase

Selinexor es un inhibidor selectivo de la exportación nuclear (XPO1/CRM1) comercializado en España como NEXPOVIO. En los datos compilados para este informe no consta el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **osteoporosis inducida por fármacos**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; la predicción se basa únicamente en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (el texto de indicación de la autorización está vacío) |
| Nueva Indicación Predicha | Osteoporosis inducida por fármacos |
| Puntaje de Predicción TxGNN | 0,9922 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Selinexor (traducción no oficial): «En estudios no clínicos, el selinexor inhibe de forma reversible la exportación nuclear de proteínas supresoras de tumores (TSP), reguladores del crecimiento y ARNm de proteínas oncogénicas mediante el bloqueo de la exportina 1 (XPO1). La inhibición de XPO1 por el selinexor provoca la acumulación de TSP en el núcleo y la reducción de varias oncoproteínas, como c-myc y la ciclina D1, la detención del ciclo celular y la apoptosis de las células cancerosas.» Texto original en inglés: "In nonclinical studies, selinexor reversibly inhibits nuclear export of tumor suppressor proteins (TSPs), growth regulators, and mRNAs of oncogenic proteins by blocking exportin 1 (XPO1). XPO1 inhibition by selinexor leads to accumulation of TSPs in the nucleus and reductions in several oncoproteins, such as c-myc and cyclin D1, cell cycle arrest, and apoptosis of cancer cells." ([DailyMed: Xpovio (selinexor) prescribing information, Karyopharm Therapeutics Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f6dd2682-75a6-4863-90a8-a3197f6f78a8), versión del 2026-05-12; consultado el 2026-11-19). Según la información conocida, selinexor es un inhibidor selectivo de la exportación nuclear que actúa sobre XPO1/CRM1 y es un fármaco oncológico.

Una hipótesis plausible, pero no verificada, es que la inhibición de XPO1 modifique vías de señalización relevantes para la remodelación ósea (por ejemplo, NF-κB, Wnt/β-catenina o la regulación de osteoclastos y osteoblastos). Este vínculo es especulativo y no está respaldado por evidencia aportada.

Además, selinexor es un fármaco oncológico con toxicidad significativa (citopenias, náuseas, anorexia, pérdida de peso, fatiga), por lo que no encaja de forma evidente en una enfermedad crónica y no mortal como la osteoporosis inducida por fármacos. Su perfil de seguridad y las 81 interacciones farmacológicas registradas pesan en contra de su uso en este contexto sin datos que lo respalden. La similitud con la indicación original aún está pendiente de evaluar.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 1211537001 | NEXPOVIO 20 MG COMPRIMIDOS RECUBIERTOS CON PELICULA | COMPRIMIDO RECUBIERTO CON PELÍCULA | Stemline Therapeutics B.V. | Comercializada |

Se muestra la única autorización con este principio activo en los datos de CIMA (AEMPS).

<!-- licenses:end -->

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor selectivo de la exportación nuclear XPO1) |
| Riesgo de Mielosupresión | Medio a alto (se describen citopenias como toxicidad relevante; confirmar en el prospecto) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto (se describen náuseas como toxicidad frecuente) |
| Items de Monitoreo | Hemograma completo, función hepática y renal, electrolitos, peso y estado nutricional |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registran 81 interacciones en total. Entre las principales mostradas:
  - **Mayores**: deferiprona, samario (153Sm) lexidronam, adalimumab, baricitinib, certolizumab pegol, cladribina y clozapina.
  - **Moderadas**: cloruro de estroncio Sr-89, roflumilast, cloranfenicol (incluida la forma oftálmica), zidovudina, alefacept, alemtuzumab, anakinra, azatioprina, canakinumab, además de vacunas (toxoide tetánico, ántrax, cólera vivo).
  - Muchas de ellas afectan a la médula ósea o al sistema inmunitario, lo que sugiere riesgo aditivo de mielosupresión e inmunosupresión.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única base es una puntuación alta del modelo TxGNN (nivel de evidencia L5), sin ensayos clínicos ni literatura, con un vínculo mecanístico especulativo y un perfil de toxicidad desfavorable para una enfermedad crónica no mortal.

**Para avanzar se necesita:**
- Obtener las advertencias y contraindicaciones del prospecto de AEMPS (brecha bloqueante para el cribado de seguridad).
- Completar los datos del mecanismo de acción desde DrugBank.
- Confirmar la indicación aprobada de la autorización española.
- Estudios preclínicos que respalden el efecto de la inhibición de XPO1 sobre el metabolismo óseo.
- Revisión sistemática de literatura sobre selinexor y salud ósea.
- Evaluación de la relación beneficio-riesgo frente a las alternativas existentes para la osteoporosis inducida por fármacos.
- Evaluación de compatibilidad de vía de administración y similitud con la indicación original (actualmente pendientes).

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Xpovio (selinexor) prescribing information, Karyopharm Therapeutics Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f6dd2682-75a6-4863-90a8-a3197f6f78a8) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

