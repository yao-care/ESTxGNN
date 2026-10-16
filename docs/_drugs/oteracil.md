---
layout: default
title: Oteracil
parent: Evidencia alta (L1-L2)
nav_order: 593
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Oteracil: nueva indicación predicha, Neoplasia de colon (nivel de evidencia L1). Indicación original: Cáncer gástrico (según el grafo de conocimiento"
monitor_inn: "oteracil"
predicted_indications: ["colonic neoplasm", "cecum villous adenoma", "cecum neuroendocrine tumor G1", "lipoma of colon", "cecal disease", "rectosigmoid junction neoplasm", "benign neoplasm of cecum", "colonic lymphangioma", "colon leiomyoma", "cavernous hemangioma of colon"]
---

# Oteracil
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **10** 
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

# Oteracil: De Cáncer Gástrico a Neoplasia de Colon

## Resumen en Una Frase

Oteracil es un componente de la combinación S-1 (tegafur/gimeracil/oteracil), comercializada en España como Teysuno y utilizada originalmente para el tratamiento del cáncer gástrico.
El modelo TxGNN predice que podría ser efectivo para **neoplasia de colon**, con **6 ensayos clínicos** y **10 publicaciones** que actualmente respaldan esta dirección (casi toda la evidencia corresponde a la combinación S-1 y no a oteracil por sí solo).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer gástrico (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Neoplasia de colon |
| Puntaje de Predicción TxGNN | 99,99 % |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Oteracil es un componente de la combinación S-1 (tegafur + gimeracil + oteracil). Por sí solo no tiene actividad antitumoral: inhibe la orotato fosforribosiltransferasa en el tracto gastrointestinal, lo que reduce la activación local del 5-FU y, con ello, la toxicidad gastrointestinal. El efecto antitumoral proviene de tegafur (profármaco del 5-FU) y de gimeracil, que inhibe la DPD y prolonga la exposición al 5-FU. Los datos detallados del mecanismo de acción no figuran en las fuentes compiladas para este informe; esta descripción procede del análisis mecanístico asociado a la predicción.

El cáncer gástrico y la neoplasia de colon son tumores del tracto gastrointestinal que responden a fluoropirimidinas. Por ello, el vínculo mecanístico es válido, pero aplica a la combinación S-1 de dosis fija y no a oteracil aislado.

Conviene interpretar con cautela el puntaje TxGNN, muy alto: probablemente refleja el contexto compartido de S-1 y las fluoropirimidinas más que un efecto propio de oteracil.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Fase 3 | Completado | 1535 | UFT + leucovorina vs. S-1 (TS-1) como tratamiento adyuvante en cáncer de colon estadio III |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Fase 3 | Desconocido | 1191 | SOX (oxaliplatino + S-1) vs. XELOX como quimioterapia adyuvante en cáncer colorrectal estadio III |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Fase 2 | Desconocido | 40 | S-1 + bevacizumab en cáncer colorrectal irresecable o recurrente tras fracaso de quimioterapia previa |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Fase 2 | Desconocido | 82 | Raltitrexed + S-1 en cáncer colorrectal metastásico tras fracaso de quimioterapia estándar; objetivo principal: supervivencia libre de progresión |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Fase 2 | Aún no recluta | 52 | Fruquintinib + tegafur/gimeracil/oteracil en tercera línea de CCR metastásico (brazo único) |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Fase 2 | Terminado | 20 | Efecto de S-1 y capecitabina con oxaliplatino sobre el flujo coronario (seguridad cardíaca, no eficacia) |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21084813](https://pubmed.ncbi.nlm.nih.gov/21084813/) | 2010 | Cohorte retrospectiva | Gan to Kagaku Ryoho | Factores de riesgo de toxicidad hematológica grave grado 3-4 (16,1 %) con S-1/irinotecán en 87 pacientes con cáncer de colon avanzado o recurrente |
| [20811661](https://pubmed.ncbi.nlm.nih.gov/20811661/) | 2010 | Preclínico (xenoinjerto) | Oncology Reports | Irinotecán supera la resistencia al 5-FU en xenoinjertos de cáncer de colon al reducir la timidilato sintasa; combinación con S-1 |
| [32936722](https://pubmed.ncbi.nlm.nih.gov/32936722/) | 2021 | Reporte de caso | J Oncol Pharm Pract | Hipertrigliceridemia inducida por S-1 |
| [28414195](https://pubmed.ncbi.nlm.nih.gov/28414195/) | 2017 | Reporte de caso | Eur J Dermatol | Eritrodermia con afectación mucosa extensa y síndrome mano-pie inducidos por TS-1 |
| [18630468](https://pubmed.ncbi.nlm.nih.gov/18630468/) | 2008 | Reporte de caso | Anticancer Research | Respuesta completa mantenida con S-1 + CPT-11 en metástasis hepáticas de cáncer de colon |
| [29394831](https://pubmed.ncbi.nlm.nih.gov/29394831/) | 2017 | Reporte de caso | Gan to Kagaku Ryoho | Hepatectomía en dos tiempos tras quimioterapia SOX + panitumumab en metástasis hepáticas de CCR |
| [41253353](https://pubmed.ncbi.nlm.nih.gov/41253353/) | 2025 | Reporte de caso | Gan to Kagaku Ryoho | Retención urinaria como neuropatía aguda por oxaliplatino en paciente previamente tratado con tegafur/gimeracil/oteracil |
| [35444144](https://pubmed.ncbi.nlm.nih.gov/35444144/) | 2022 | Reporte de caso | Gan to Kagaku Ryoho | Resecciones repetidas de recurrencias peritoneales tras cirugía de cáncer colorrectal |
| [30692384](https://pubmed.ncbi.nlm.nih.gov/30692384/) | 2018 | Reporte de caso | Gan to Kagaku Ryoho | Neurólisis del plexo celíaco guiada por TC para dolor por recurrencia de cáncer de colon |
| [34650027](https://pubmed.ncbi.nlm.nih.gov/34650027/) | 2021 | Reporte de caso | Am J Case Rep | Resección en bloque de cáncer de cola de páncreas con perforación colónica tras quimioterapia neoadyuvante |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 111669001 | TEYSUNO 15 mg/4,35 mg/11,8 mg cápsulas duras | Cápsula dura | No disponible en los datos compilados |
| 111669002 | TEYSUNO 15 mg/4,35 mg/11,8 mg cápsulas duras | Cápsula dura | No disponible en los datos compilados |
| 111669003 | TEYSUNO 20 mg/5,8 mg/15,8 mg cápsulas duras | Cápsula dura | No disponible en los datos compilados |
| 111669004 | TEYSUNO 20 mg/5,8 mg/15,8 mg cápsulas duras | Cápsula dura | No disponible en los datos compilados |

Titular de todas las autorizaciones: Nordic Group B.V.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (clase fluoropirimidina; S-1 con profármaco de 5-FU) |
| Riesgo de Mielosupresión | Medio: en un estudio retrospectivo de S-1/irinotecán, la toxicidad hematológica grado 3-4 fue del 16,1 % |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal; vigilar toxicidad cutánea (síndrome mano-pie, eritrodermia) y alteraciones lipídicas (hipertrigliceridemia), según los casos publicados |
| Protección en Manejo | Seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como referencia, la literatura compilada describe casos de síndrome mano-pie, eritrodermia e hipertrigliceridemia asociados a S-1. No se encontraron interacciones farmacológicas registradas en la base de datos consultada.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ensayo de Fase 3 completado (NCT00660894, n=1535) que evalúa S-1 en cáncer de colon estadio III, además de otro de Fase 3 en curso o con estado desconocido, lo que respalda la plausibilidad clínica. Sin embargo, la evidencia corresponde a la combinación S-1 y no a oteracil aislado, que carece de actividad antitumoral propia. Además, faltan los resultados publicados de varios ensayos y los datos de seguridad de la ficha técnica.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), actualmente sin datos y bloqueante para el cribado de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Confirmar los resultados de NCT00660894 y el estado de NCT03448549
- Aclarar si la indicación en colon aplica a la combinación S-1 de dosis fija y no a oteracil como agente único
- Definir un plan de monitoreo de seguridad hematológica, cutánea y metabólica
- Evaluar la compatibilidad de vías de administración y la similitud con la indicación original (actualmente pendientes)

**Nota sobre otras predicciones:** las demás indicaciones predichas (adenoma velloso de ciego, tumor neuroendocrino G1 de ciego, lipoma de colon, linfangioma, leiomioma, hemangioma cavernoso, entre otras) son lesiones benignas o carecen de evidencia propia, por lo que se recomienda mantenerlas en espera (Hold). La neoplasia de la unión rectosigmoidea constituye una pregunta de investigación razonable por extensión de la evidencia en cáncer colorrectal.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

