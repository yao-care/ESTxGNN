---
layout: default
title: Insulin Detemir
parent: Solo predicción del modelo (L5)
nav_order: 419
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
monitor_inn: "Insulin detemir"
predicted_indications: ["autoimmune oophoritis", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "focal stiff limb syndrome", "classic stiff person syndrome", "pancreatic agenesis", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy"]
description: "Insulin Detemir: nueva indicación predicha, Autoimmune oophoritis (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Insulin Detemir
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

## Insulin Detemir: Autoimmune oophoritis
{: .text-alpha }

## Resumen en Una Frase

Insulina detemir es un análogo de insulina basal de acción prolongada, originalmente utilizado para el tratamiento de la diabetes mellitus y la cetoacidosis diabética.
El modelo TxGNN predice que podría ser efectivo para la **diabetes mellitus tipo 1**, con **39 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección. Cabe señalar que esta predicción coincide con el uso central del fármaco, por lo que no constituye un reposicionamiento en sentido estricto.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Autoimmune oophoritis |
| Puntaje de Predicción TxGNN | 0.9967 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 1 de 2) |
| Número de Autorizaciones | 2 (vigentes: 1) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Insulina detemir es un análogo de insulina soluble de acción prolongada. Se diferencia de la insulina humana por la eliminación del aminoácido treonina en la posición B30 y la acilación de un ácido graso de 14 carbonos (ácido mirístico) en la lisina B29. Esta modificación permite que se una de forma reversible a la albúmina tras la inyección subcutánea, lo que produce una absorción lenta y un efecto metabólico prolongado de hasta 24 horas. Se une al receptor de insulina para reemplazar la insulina endógena deficiente. Los datos compilados no incluyen un campo formal de mecanismo de acción, pero esta farmacología está bien descrita en la literatura (por ejemplo, PMID 17881328).

La diabetes tipo 1 se caracteriza por una deficiencia absoluta de insulina, por lo que la terapia basal con insulina es el tratamiento de referencia.

Otras predicciones del modelo (por ejemplo, ooforitis autoinmune, opsismodisplasia, síndrome de la persona rígida o lipodistrofias) carecen de ensayos clínicos y de literatura de respaldo. En el caso de las lipodistrofias, la insulina es más bien una causa conocida en el sitio de inyección. La agenesia pancreática es mecanísticamente plausible, pero la evidencia es indirecta y solo trataría la manifestación diabética. Ninguna de ellas se desarrolla en este informe.

---

## Evidencia de Ensayos Clínicos

Se listan los 10 ensayos más relevantes, priorizando los de mayor relevancia directa y fase más avanzada, de un total de 39 registrados.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00595374](https://clinicaltrials.gov/study/NCT00595374) | Fase 3 | Completado | 114 | Detemir + aspart vs. NPH + aspart en adultos con diabetes tipo 1 en Europa; compara control glucémico y seguridad |
| [NCT00447382](https://clinicaltrials.gov/study/NCT00447382) | Fase 3 | Completado | 330 | Comparación doble ciego de 12 meses entre detemir del proceso actual y del proceso NN729 en diabetes tipo 1 |
| [NCT00312156](https://clinicaltrials.gov/study/NCT00312156) | Fase 3 | Completado | 347 | Detemir vs. NPH, con aspart en las comidas, en niños y adolescentes con diabetes tipo 1 |
| [NCT00184639](https://clinicaltrials.gov/study/NCT00184639) | Fase 3 | Completado | 71 | Detemir vs. insulina Semilente MC durante 32 semanas en niños, adolescentes y adultos jóvenes (6-21 años) |
| [NCT01709929](https://clinicaltrials.gov/study/NCT01709929) | Fase 3 | Completado | 2287 | Estudio de seguridad abierto y no aleatorizado de detemir en diabetes tipo 1 o 2 en Norteamérica |
| [NCT00978627](https://clinicaltrials.gov/study/NCT00978627) | Fase 3 | Completado | 548 | NN5401 (degludec/aspart) vs. detemir + aspart en diabetes tipo 1; detemir como comparador |
| [NCT00322257](https://clinicaltrials.gov/study/NCT00322257) | Fase 3 | Terminado | 596 | Insulina inhalada vs. aspart subcutánea, ambas con detemir como basal; detemir es tratamiento de fondo y la terminación temprana limita la interpretación |
| [NCT00117780](https://clinicaltrials.gov/study/NCT00117780) | Fase 4 | Completado | 520 | Detemir una vez vs. dos veces al día en régimen basal-bolo con aspart en diabetes tipo 1 |
| [NCT01440439](https://clinicaltrials.gov/study/NCT01440439) | Fase 4 | Desconocido | 30 | Detemir vs. glargina sobre el control glucémico y el metabolismo durante el ejercicio; muestra pequeña y estado incierto |
| [NCT01542463](https://clinicaltrials.gov/study/NCT01542463) | N/A | Completado | 4464 | Estudio no intervencionista europeo sobre seguridad, control glucémico y peso con detemir en diabetes tipo 1 o 2 |

---

## Evidencia de Literatura

Se listan 10 de las 20 publicaciones, priorizando ECA y revisiones sistemáticas.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | ECA | Lancet Diabetes Endocrinol | Ensayo EXPECT de no inferioridad: degludec vs. detemir, con aspart, en embarazadas con diabetes tipo 1 |
| [33662147](https://pubmed.ncbi.nlm.nih.gov/33662147/) | 2021 | Revisión sistemática/Metaanálisis | Cochrane Database Syst Rev | Análogos de insulina de acción (ultra)larga en diabetes tipo 1, con foco en complicaciones e hipoglucemia |
| [21878861](https://pubmed.ncbi.nlm.nih.gov/21878861/) | 2011 | Revisión sistemática/Metaanálisis | Pol Arch Med Wewn | Detemir vs. insulina NPH en diabetes tipo 1; los beneficios sobre el control glucémico no se confirmaron en todos los estudios |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Revisión sistemática/Metaanálisis en red | Value Health | Eficacia y seguridad relativas de regímenes de insulina basal en adultos con diabetes tipo 1 |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | Revisión sistemática/Metaanálisis | Clin Ther | Eficacia y tolerabilidad de degludec frente a glargina y detemir en diabetes tipo 1 y 2 |
| [23243636](https://pubmed.ncbi.nlm.nih.gov/23243636/) | 2012 | Revisión sistemática | Drugs Today (Barc) | Análogos de insulina en niños y adolescentes con diabetes tipo 1 |
| [17326333](https://pubmed.ncbi.nlm.nih.gov/17326333/) | 2006 | Revisión | Vasc Health Risk Manag | Detemir tiene un perfil farmacocinético menos variable que NPH y puede reducir el riesgo de hipoglucemia, sobre todo nocturna |
| [15516157](https://pubmed.ncbi.nlm.nih.gov/15516157/) | 2004 | Revisión | Drugs | Efecto más predecible y consistente que NPH, con hasta 24 horas de duración |
| [20539842](https://pubmed.ncbi.nlm.nih.gov/20539842/) | 2010 | Revisión | Vasc Health Risk Manag | Actualización sobre detemir en diabetes tipo 1 y 2 |
| [17881328](https://pubmed.ncbi.nlm.nih.gov/17881328/) | 2007 | Revisión | Endocrinol Metab Clin North Am | Farmacología de detemir: acilación con ácido mirístico y unión a albúmina |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 04278005 | LEVEMIR FLEXPEN 100 U/ML solución inyectable en una pluma precargada | Solución inyectable en pluma precargada | No disponible en los datos compilados |
| 04278008 | LEVEMIR INNOLET 100 U/ML solución inyectable en una pluma precargada | Solución inyectable en pluma precargada | No disponible en los datos compilados |

Ambas autorizaciones son de monofármaco, están vigentes y pertenecen a Novo Nordisk A/S.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las listadas, la mayoría son de gravedad moderada; entre ellas:
  - Antidiabéticos (metformina, pioglitazona, alogliptina, albiglutida): posible efecto hipoglucemiante aditivo.
  - Simpaticomiméticos y agonistas beta (epinefrina, fenilefrina, pseudoefedrina, salbutamol, formoterol): pueden alterar el control glucémico.
  - Betabloqueantes (acebutolol): pueden enmascarar los síntomas de hipoglucemia.
  - Corticoides (hidrocortisona), estrógenos (etinilestradiol, estradiol), hidroclorotiazida, acetazolamida, doxiciclina, etanol y alpelisib: pueden modificar los requerimientos de insulina o el control glucémico.
  - Corticoides tópicos (hidrocortisona tópica, alclometasona tópica): interacción de gravedad leve.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen varios ensayos de Fase 3 completados en diabetes tipo 1 y numerosas revisiones sistemáticas que respaldan la eficacia y seguridad de insulina detemir (nivel L1). Sin embargo, esta indicación es el uso central ya consolidado del fármaco, no un reposicionamiento. Las demás indicaciones predichas carecen de evidencia y deberían mantenerse en espera (Hold).

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de la AEMPS (advertencias y contraindicaciones), actualmente no disponible en los datos compilados.
- Confirmar el texto de indicación aprobado en las autorizaciones españolas.
- Completar los datos del mecanismo de acción en las fuentes del fármaco.
- Establecer un plan de monitoreo de hipoglucemia y de interacciones, especialmente con otros antidiabéticos y betabloqueantes.
- Si se desea un reposicionamiento genuino, evaluar por separado las indicaciones de menor evidencia (por ejemplo, agenesia pancreática) con estudios específicos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

