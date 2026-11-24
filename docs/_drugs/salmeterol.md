---
layout: default
title: Salmeterol
parent: Solo predicción del modelo (L5)
nav_order: 724
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
monitor_inn: "SALMETEROL"
predicted_indications: ["respiratory malformation", "Rienhoff syndrome", "atopic eczema"]
description: "Salmeterol: nueva indicación predicha, malformación respiratoria (respiratory malformation) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 9 (comercializadas: 5)"
---

# Salmeterol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Salmeterol: malformación respiratoria (respiratory malformation)
{: .text-alpha }

## Resumen en Una Frase

Salmeterol es un broncodilatador agonista beta2 de acción prolongada, administrado por vía inhalada y comercializado en España.
El modelo TxGNN predice que podría ser efectivo para **malformación respiratoria (respiratory malformation)**,
pero la evidencia directa es muy limitada: hay **2 ensayos clínicos** y **8 publicaciones** recopilados, ninguno de los cuales estudia directamente esta enfermedad.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | malformación respiratoria (respiratory malformation) |
| Puntaje de Predicción TxGNN | 0.9991 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 5 de 9; revocadas o suspendidas: 4) |
| Número de Autorizaciones | 9 (comercializadas: 5) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Salmeterol (traducción no oficial): «El salmeterol es un LABA selectivo. Los estudios in vitro muestran que el salmeterol es al menos 50 veces más selectivo por los adrenorreceptores beta 2 que el albuterol. Aunque los adrenorreceptores beta 2 son los receptores adrenérgicos predominantes en el músculo liso bronquial y los adrenorreceptores beta 1 son los receptores predominantes en el corazón, también existen adrenorreceptores beta 2 en el corazón humano, que constituyen entre el 10% y el 50% del total de adrenorreceptores beta.» Texto original en inglés: "Salmeterol is a selective LABA. In vitro studies show salmeterol to be at least 50 times more selective for beta 2 -adrenoceptors than albuterol. Although beta 2 -adrenoceptors are the predominant adrenergic receptors in bronchial smooth muscle and beta 1 -adrenoceptors are the predominant receptors in the heart, there are also beta 2 -adrenoceptors in the human heart comprising 10% to 50% of the total beta-adrenoceptors." ([DailyMed: Serevent Diskus (salmeterol xinafoate) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=12d9728e-6b5c-4aee-bfb0-745e542ed2e4), versión del 2022-10-10; consultado el 2026-11-19). Por su clase farmacológica, salmeterol actúa sobre los receptores beta2 adrenérgicos de la vía aérea, produciendo broncodilatación sostenida. También se ha descrito que puede aumentar la frecuencia del batido ciliar y el aclaramiento mucociliar.

Esa biología compartida de la vía aérea (función ciliar, aclaramiento de moco, señalización beta2) probablemente explica el puntaje elevado del modelo. Sin embargo, la "malformación respiratoria" es una categoría estructural y heterogénea, y la broncodilatación no corrige defectos estructurales.

Por ello, el vínculo es indirecto y, en el mejor de los casos, sintomático. Ningún estudio recopilado evalúa salmeterol en esta enfermedad, por lo que el nivel de evidencia se limita a L5 (solo predicción del modelo).

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00005110](https://clinicaltrials.gov/study/NCT00005110) | No especificada | Suspendido | No disponible | Salmeterol frente a albuterol o placebo durante 6 meses en fibrosis quística; sin resultados. Relación solo laxa con la indicación predicha. |
| [NCT01681979](https://clinicaltrials.gov/study/NCT01681979) | No aplicable | Completado | 1 | Tratamiento del asma en el embarazo y resultados adversos gestacionales; se centra en seguridad en el embarazo, no en malformación respiratoria. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15293609](https://pubmed.ncbi.nlm.nih.gov/15293609/) | 2004 | ECA | Eur Respir J | Efecto de salmeterol sobre la respuesta ventilatoria al ejercicio en EPOC (cruzado, doble ciego, 23 pacientes). |
| [34902004](https://pubmed.ncbi.nlm.nih.gov/34902004/) | 2022 | ECA | JAMA Pediatrics | Corticoides inhalados solos o con LABA para la función pulmonar reducida en niños nacidos prematuros. |
| [20528601](https://pubmed.ncbi.nlm.nih.gov/20528601/) | 2010 | Revisión | J Asthma | Revisión de budesonida/formoterol en asma persistente. |
| [26229457](https://pubmed.ncbi.nlm.nih.gov/26229457/) | 2015 | Revisión | Int J Chron Obstruct Pulmon Dis | Doble broncodilatación con indacaterol-glicopirronio en EPOC. |
| [22608352](https://pubmed.ncbi.nlm.nih.gov/22608352/) | 2012 | Cohorte | Respir Med | Batido ciliar deprimido en cilios nasales de sujetos con EPOC. |
| [30021361](https://pubmed.ncbi.nlm.nih.gov/30021361/) | 2018 | Preclínico | Biomed Pharmacother | Extracto de tomillo aumenta la frecuencia de batido mucociliar en células de pacientes con EPOC. |
| [37327273](https://pubmed.ncbi.nlm.nih.gov/37327273/) | 2023 | Reporte de caso | Medicine | Aspergilosis pulmonar tratada con omalizumab. |
| [20703071](https://pubmed.ncbi.nlm.nih.gov/20703071/) | 2010 | Reporte de caso | Arerugi | Discinesia ciliar primaria tratada inicialmente como asma. |

Ninguna de estas publicaciones estudia directamente la malformación respiratoria.

## Información de Mercado en España

Salmeterol cuenta con autorizaciones como principio activo único; están revocadas 59490, 59523, 59527 y 59676.

<!-- review:begin es-lic-20261117-salmeterol-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Salmeterol cuenta con 9 autorizaciones válidas como principio activo único, sin autorizaciones canceladas." Según CIMA (AEMPS), datos del 2026-11-17, están revocadas 59490 (SEREVENT 25 microgramos/inhalación), 59527 (INASPIR 25 microgramos/inhalación), 59523 y 59676; el estado de cada autorización figura en la tabla de Información de Mercado en España. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261117-salmeterol-1 -->

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 59489 | SEREVENT ACCUHALER 50 microgramos/inhalación, polvo para inhalación | POLVO PARA INHALACIÓN | Glaxosmithkline S.A. | Comercializada |
| 83247 | SOLTEL 25 MICROGRAMOS/INHALACION SUSPENSION PARA INHALACION EN ENVASE A PRESION | SUSPENSIÓN PARA INHALACIÓN EN ENVASE A PRESIÓN | Cipla Europe N.V. | Comercializada |
| 59675 | BETAMICAN ACCUHALER 50 microgramos/inhalación POLVO PARA INHALACION | POLVO PARA INHALACIÓN | Glaxosmithkline S.A. | Comercializada |
| 59522 | BEGLAN ACCUHALER 50 microgramos/inhalación, polvo para inhalación | POLVO PARA INHALACIÓN | Glaxosmithkline S.A. | Comercializada |
| 59526 | INASPIR ACCUHALER 50 microgramos/inhalacion, POLVO PARA INHALACION | POLVO PARA INHALACIÓN | Glaxosmithkline S.A. | Comercializada |
| 59490 | SEREVENT 25 microgramos/inhalación, suspensión para inhalación en envase a presión | SUSPENSIÓN PARA INHALACIÓN EN ENVASE A PRESIÓN | Glaxosmithkline S.A. | Revocada |
| 59527 | INASPIR 25 microgramos/inhalacion SUSPENSION PARA INHALACION EN ENVASE A PRESION | SUSPENSIÓN PARA INHALACIÓN EN ENVASE A PRESIÓN | Glaxosmithkline S.A. | Revocada |
| 59676 | BETAMICAN 25 microgramos/inhalación SUSPENSION PARA INHALACION EN ENVASE A PRESION | SUSPENSIÓN PARA INHALACIÓN EN ENVASE A PRESIÓN | Glaxosmithkline S.A. | Revocada |
| 59523 | BEGLAN 25 microgramos/inhalación, suspensión para inhalación en envase a presión | SUSPENSIÓN PARA INHALACIÓN EN ENVASE A PRESIÓN | Glaxosmithkline S.A. | Revocada |

Se muestran las 9 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (se identificaron 100 interacciones; se muestran las principales):
  - Mayor: claritromicina.
  - Moderadas: epinefrina, isometepteno, famotidina, acarbosa, albiglutida, alogliptina, canagliflozina, clorpropamida, dapagliflozina, dietilpropión, dolasetrón, dulaglutida, empagliflozina.
  - Menores: corticoides como hidrocortisona, triamcinolona, dexametasona, beclometasona, betametasona y budesonida.
- **Condiciones de precaución (no proceden del texto del prospecto):** hipertensión, síndrome de QT largo, epilepsia, hiperglucemia, osteoporosis, enfermedades del timo y diversos déficits de hormonas hipofisarias.

Consultar el prospecto para el resto de la información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje del modelo es alto (0.9991), pero ningún ensayo ni publicación estudia salmeterol en malformación respiratoria, y el vínculo mecanístico es indirecto, ya que la broncodilatación no corrige defectos estructurales. La evidencia se limita a L5.

**Para avanzar se necesita:**
- Datos del mecanismo de acción del fármaco.
- Estudios que evalúen directamente salmeterol en malformaciones respiratorias, o en subgrupos definidos con alteración de la función ciliar.
- Advertencias y contraindicaciones del prospecto de la AEMPS.
- Evaluación de la vía de administración inhalada para la población y la enfermedad de interés.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | Autorizaciones vigentes: 9 → 5 de 9 (4 revocadas) | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Serevent Diskus (salmeterol xinafoate) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=12d9728e-6b5c-4aee-bfb0-745e542ed2e4) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

