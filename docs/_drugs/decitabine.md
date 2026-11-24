---
layout: default
title: Decitabine
parent: Solo predicción del modelo (L5)
nav_order: 228
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "Decitabine"
predicted_indications: ["refractory cytopenia of childhood"]
description: "Decitabine: nueva indicación predicha, Citopenia refractaria de la infancia (refractory cytopenia of childhood) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 2 (comercializadas: 1; autorizadas no comercializadas: 1)"
---

# Decitabine
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

## Decitabine: Citopenia refractaria de la infancia (refractory cytopenia of childhood)
{: .text-alpha }

## Resumen en Una Frase

Decitabina es un agente hipometilante (análogo nucleosídico), originalmente utilizado en la leucemia mieloide aguda y los síndromes mielodisplásicos.
El modelo TxGNN predice que podría ser efectivo para **citopenia refractaria de la infancia**,
con **0 ensayos clínicos** y **2 publicaciones** (un estudio de cohorte y un reporte de caso) que actualmente respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Citopenia refractaria de la infancia (refractory cytopenia of childhood) |
| Puntaje de Predicción TxGNN | 0.9903 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 2; autorizadas no comercializadas: 1) |
| Número de Autorizaciones | 2 (comercializadas: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Decitabine (traducción no oficial): «Se cree que decitabina ejerce sus efectos antineoplásicos tras su fosforilación e incorporación directa en el ADN y la inhibición de la ADN metiltransferasa, lo que provoca hipometilación del ADN y diferenciación celular o apoptosis. Decitabina inhibe la metilación del ADN in vitro, lo cual se logra a concentraciones que no provocan una supresión importante de la síntesis de ADN.» Texto original en inglés: "Decitabine is believed to exert its antineoplastic effects after phosphorylation and direct incorporation into DNA and inhibition of DNA methyltransferase, causing hypomethylation of DNA and cellular differentiation or apoptosis. Decitabine inhibits DNA methylation in vitro, which is achieved at concentrations that do not cause major suppression of DNA synthesis." ([DailyMed: decitabine prescribing information, BluePoint Laboratories](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5975fa81-1e29-4d56-e063-6394a90a9cd5), versión del 2026-11-03; consultado el 2026-11-19). Según la farmacología conocida, la decitabina es un análogo nucleosídico hipometilante que inhibe la ADN metiltransferasa, lo que produce hipometilación del ADN y reexpresión de genes silenciados.

La citopenia refractaria de la infancia (CRI) es el subtipo más frecuente de síndrome mielodisplásico (SMD) pediátrico. La decitabina ya se utiliza en neoplasias mieloides del adulto (LMA y SMD), por lo que la biología clonal mieloide compartida ofrece una base mecanística plausible.

Conviene subrayar que el puntaje de 0.9903 es solo una señal computacional y no constituye evidencia clínica. Este vínculo se apoya en la farmacología conocida del fármaco y no en datos de mecanismo del registro analizado.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35624441](https://pubmed.ncbi.nlm.nih.gov/35624441/) | 2022 | Cohorte (probablemente retrospectivo) | BMC Pediatrics | Experiencia de 10 años en un solo centro con decitabina combinada con un régimen mínimamente mielosupresor como puente al trasplante alogénico de progenitores hematopoyéticos en SMD pediátrico |
| [42125547](https://pubmed.ncbi.nlm.nih.gov/42125547/) | 2026 | Reporte de caso | Experimental and Therapeutic Medicine | Decitabina en monoterapia en un paciente de 8 años con SMD/CRI no elegible para trasplante ni inmunosupresión; los datos terapéuticos en este grupo son escasos |

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 112792001 | DACOGEN 50 mg polvo para concentrado para solucion para perfusion | POLVO PARA CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Janssen-Cilag International N.V | Comercializada |
| 91107 | DECITABINA HIKMA 50 MG POLVO PARA CONCENTRADO PARA SOLUCION PARA PERFUSION EFG | POLVO PARA CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Hikma Farmaceutica (Portugal) S.A. | Autorizada, no comercializada |

Se muestran las 2 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (agente hipometilante, análogo nucleosídico) |
| Riesgo de Mielosupresión | Alto (las contraindicaciones del grafo de conocimiento incluyen neutropenia, trombocitopenia y agranulocitosis; es esperable mielosupresión) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma completo con diferencial, función hepática y renal |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

- **Contraindicaciones/enfermedades de alerta (grafo de conocimiento, no texto del prospecto)**: enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, diabetes mellitus, cetoacidosis diabética, neutropenia y agranulocitosis.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las principales, de gravedad **mayor**: deferiprona, samario (153Sm) lexidronam, adalimumab y baricitinib. De gravedad **moderada**, entre otras: palifermina, cloruro de estroncio Sr-89, mercaptopurina, roflumilast, cloranfenicol, zidovudina, ganciclovir, gemcitabina, azatioprina, aldesleukina, alemtuzumab y vacunas (toxoide tetánico, ántrax).

Las advertencias y contraindicaciones del prospecto de la AEMPS no están disponibles; consultar el prospecto para la información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia se limita a un estudio de cohorte retrospectivo de un solo centro y un reporte de caso, sin ensayos clínicos registrados (nivel L4). Además, falta la información de seguridad del prospecto, lo que impide avanzar al cribado de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas)
- Completar los datos del mecanismo de acción (DrugBank)
- Evidencia clínica prospectiva en SMD/CRI pediátrico (ensayos de fase 2 o superior)
- Evaluar la compatibilidad de vías y formulaciones en población pediátrica y un plan de monitoreo hematológico

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: decitabine prescribing information, BluePoint Laboratories](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5975fa81-1e29-4d56-e063-6394a90a9cd5) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

