---
layout: default
title: Clofarabine
parent: Solo predicción del modelo (L5)
nav_order: 135
evidence_level: L5
indication_count: 10
---

# Clofarabine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Clofarabina: De Leucemia Linfoblástica Aguda Pediátrica Refractaria a Leucemia Mieloide

## Resumen en Una Frase

Clofarabina es un análogo de nucleósido de purina, utilizado originalmente para tratar la leucemia linfoblástica aguda (LLA) pediátrica recidivante o refractoria.
El modelo TxGNN predice que podría ser efectiva para **leucemia mieloide**, con **50 ensayos clínicos** y **20 publicaciones** que respaldan esta dirección.
La mayoría de los ensayos evalúa clofarabina dentro de combinaciones o regímenes de acondicionamiento, por lo que su aporte individual es difícil de aislar.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | LLA pediátrica recidivante o refractoria (según la ficha farmacológica; el texto de indicación de la AEMPS no está disponible) |
| Nueva Indicación Predicha | Leucemia mieloide |
| Puntaje de Predicción TxGNN | 99,88% |
| Nivel de Evidencia | L1 según la regla de este informe (2 ECA de Fase 3 completados). El Evidence Pack asigna L2, y los resultados de eficacia de esos ensayos no están en los datos. |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 10 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el campo específico de DrugBank. Según la farmacología general, la clofarabina es un análogo de nucleósido de purina. Su metabolito trifosfato inhibe la ribonucleótido reductasa y la ADN polimerasa, y altera la función mitocondrial, lo que induce apoptosis tanto en células leucémicas en división como en reposo. Los datos farmacológicos del pack confirman como dianas humanas las subunidades **RRM1** y **RRM2** de la ribonucleótido reductasa.

La LLA y la leucemia mieloide son leucemias agudas de progenitores hematopoyéticos, con alta actividad proliferativa y metabolismo de nucleósidos. Un fármaco que bloquea la síntesis de ADN en blastos linfoides tiene, por tanto, una base biológica clara para actuar sobre blastos mieloides. Los ensayos en LMA de adultos mayores, LMA refractaria y síndromes mielodisplásicos apuntan en la misma dirección.

Esta indicación no es un reposicionamiento puramente especulativo. Hay Fase 2 y Fase 3 en LMA, pero varias publicaciones son revisiones y los resultados clave no aparecen en los datos. Además, la indicación aprobada en España no se pudo verificar en el pack.

---

## Evidencia de Ensayos Clínicos

Se muestran 10 de los 50 ensayos registrados, priorizando fase avanzada, uso directo de clofarabina y tamaño de muestra.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02085408](https://clinicaltrials.gov/study/NCT02085408) | Fase 3 | Completado | 727 | Clofarabina como inducción y postremisión frente a daunorrubicina y citarabina, seguida de decitabina o de observación, en LMA de novo en mayores de 60 años. |
| [NCT01471444](https://clinicaltrials.gov/study/NCT01471444) | Fase 3 | Completado | 256 | Aleatorizado: fludarabina-clofarabina frente a fludarabina sola con busulfán IV antes del trasplante alogénico en LMA o SMD. |
| [NCT05477589](https://clinicaltrials.gov/study/NCT05477589) | Fase 3 | Reclutando | 170 | Compara el acondicionamiento CloFluBu con BuCyMel en niños con LMA sometidos a trasplante alogénico. |
| [NCT00932412](https://clinicaltrials.gov/study/NCT00932412) | Fase 2 | Completado | 735 | Aleatorizado: clofarabina con citarabina a dosis intermedia (CLARA) frente a citarabina a dosis altas como consolidación en LMA de novo en adultos jóvenes. |
| [NCT00088218](https://clinicaltrials.gov/study/NCT00088218) | Fase 2 | Completado | 95 | Clofarabina sola frente a clofarabina con citarabina a dosis bajas en LMA y SMD de alto riesgo, en mayores de 60 años sin tratamiento previo. |
| [NCT00042354](https://clinicaltrials.gov/study/NCT00042354) | Fase 2 | Completado | 40 | Clofarabina en monoterapia en LMA pediátrica refractaria o recidivante, abierto. |
| [NCT00814164](https://clinicaltrials.gov/study/NCT00814164) | Fase 2 | Terminado | 21 | Clofarabina con daunorrubicina en LMA de novo en mayores de 60 años, con estudio de mecanismos de resistencia. Es el ensayo con relevancia directa "A" del pack. |
| [NCT01289457](https://clinicaltrials.gov/study/NCT01289457) | Fase 1/2 | Completado | 282 | Aleatorizado: clofarabina, idarrubicina y citarabina (CIA) frente a fludarabina, idarrubicina y citarabina (FLAI) en LMA y SMD de alto riesgo. |
| [NCT02686593](https://clinicaltrials.gov/study/NCT02686593) | Fase 2 | Completado | 50 | Clofarabina, citarabina y mitoxantrona (CLAM) como primer rescate en LMA recidivante o refractaria. |
| [NCT01252667](https://clinicaltrials.gov/study/NCT01252667) | Fase 2 | Completado | 44 | Clofarabina con irradiación corporal total a dosis baja como acondicionamiento para reducir recaídas tras el trasplante en LMA. |

Varios ensayos terminaron anticipadamente con muy pocos pacientes (por ejemplo, NCT01158885 y NCT00503880, con 2 pacientes cada uno), por lo que no aportan datos de eficacia.

---

## Evidencia de Literatura

Se muestran 10 de las 20 publicaciones. Los tipos se indican según la clasificación del pack o el título.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|---------|
| [31246522](https://pubmed.ncbi.nlm.nih.gov/31246522/) | 2019 | ECA Fase III | J Clin Oncol | Estudio AML08 en LMA infantil: incorporar clofarabina a la primera inducción permite reducir la exposición a daunorrubicina y etopósido. |
| [32187883](https://pubmed.ncbi.nlm.nih.gov/32187883/) | 2020 | Fase 2 (cohorte) | Cancer Med | CLAM en LMA refractaria o recidivante: altas tasas de respuesta y un puente eficaz hacia el trasplante alogénico. |
| [36336258](https://pubmed.ncbi.nlm.nih.gov/36336258/) | 2023 | Cohorte | Transplant Cell Ther | Acondicionamiento mieloablativo clofarabina-busulfán en neoplasias mieloides activas, con actividad antileucémica y toxicidad aceptable. |
| [40746302](https://pubmed.ncbi.nlm.nih.gov/40746302/) | 2025 | Fase I/II | Br J Haematol | Bisantreno con fludarabina y clofarabina como rescate en LMA recidivante o refractaria (21 pacientes). |
| [31637757](https://pubmed.ncbi.nlm.nih.gov/31637757/) | 2020 | Fase I/II | Am J Hematol | Clofarabina con irradiación corporal total de 2 Gy como acondicionamiento no mieloablativo en adultos con LMA no aptos para regímenes intensivos. |
| [22957815](https://pubmed.ncbi.nlm.nih.gov/22957815/) | 2013 | Revisión | Leuk Lymphoma | Papel de clofarabina en LMA: inhibe la ribonucleótido reductasa y la ADN polimerasa, con mayor estabilidad que fludarabina y cladribina. |
| [25457773](https://pubmed.ncbi.nlm.nih.gov/25457773/) | 2015 | Revisión | Crit Rev Oncol Hematol | Uso de clofarabina en adultos con LMA, desde la monoterapia hasta las combinaciones en primera y segunda línea. |
| [19852733](https://pubmed.ncbi.nlm.nih.gov/19852733/) | 2009 | Revisión | Future Oncol | Actividad como agente único comparable a los agentes estándar, y combinaciones seguras y eficaces. |
| [31281098](https://pubmed.ncbi.nlm.nih.gov/31281098/) | 2019 | Revisión | Lancet Oncol | Comentario sobre clofarabina y citarabina en LMA. |
| [33046037](https://pubmed.ncbi.nlm.nih.gov/33046037/) | 2020 | Preclínico | BMC Cancer | Venetoclax y alvocidib son citotóxicos en células de LMA resistentes a citarabina y clofarabina. |

---

## Información de Mercado en España

Se muestran 5 de las 10 autorizaciones. El texto de indicación aprobada no está disponible en los datos recibidos.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 83299 | Clofarabina Zentiva 1 mg/ml (Zentiva K.S.) | Concentrado para solución para perfusión |
| 82208 | Clofarabina Teva 1 mg/ml (Teva Pharma S.L.U.) | Concentrado para solución para perfusión |
| 06334002 | Evoltra 1 mg/ml (Sanofi B.V.) | Concentrado para solución para perfusión |
| 86158 | Clofarabina Aurovitas 1 mg/ml (Aurovitas Spain, S.A.U.) | Concentrado para solución para perfusión |
| 82636 | Clofarabina Bioorganics 1 mg/ml (Bioorganics B.V.) | Concentrado para solución para perfusión |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antimetabolito, análogo de nucleósido de purina) |
| Riesgo de Mielosupresión | Alto. La literatura clínica sobre clofarabina en LLA y LMA describe toxicidades hematológicas e infecciosas de grado >3 frecuentes. |
| Clasificación de Emetogenicidad | Media (según la categoría del fármaco; el pack no aporta datos específicos) |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal, electrolitos |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

Consultar las advertencias y precauciones del prospecto para los detalles de toxicidad.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

La consulta de interacciones solo devolvió las dianas moleculares del fármaco (RRM1 y RRM2). No hay interacciones fármaco-fármaco registradas en el pack.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay dos ensayos de Fase 3 completados y numerosos estudios de Fase 2 en LMA y SMD, con una base mecanística coherente con el uso original. Sin embargo, casi toda la evidencia corresponde a combinaciones o regímenes de acondicionamiento, y el pack no incluye los resultados de eficacia de los ensayos de Fase 3. Tampoco se pudo verificar la indicación autorizada en España.

**Para avanzar se necesita:**
- Descargar y revisar la ficha técnica de la AEMPS (indicaciones, advertencias y contraindicaciones), que es el vacío de datos bloqueante.
- Obtener los resultados publicados de NCT02085408 y NCT01471444 para confirmar el beneficio de clofarabina en LMA.
- Completar el mecanismo de acción desde DrugBank.
- Definir un plan de monitoreo hematológico, hepático y renal para poblaciones específicas (niños, adultos mayores, insuficiencia renal).

**Otras predicciones del modelo:**
- **LLA** (rangos 2 y 8): nivel L2 y recomendación Proceed with Guardrails, aunque parece un uso ya establecido más que un reposicionamiento.
- **Leucemia mieloide en fase blástica de LMC BCR-ABL1 positiva** (rango 7): L2, pero con recomendación "Research Question".
- **Neuroblastoma** (rango 4): L4, Hold.
- **Ganglioneuroblastoma, neoplasia retroperitoneal, LLC/LLP** (subtipos de LLC/LLP con mutación somática y pregerminal) **y el síndrome de anomalías vertebrales con disfunción endocrina y de células T**: L5 y Hold, sin ensayos ni literatura.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

