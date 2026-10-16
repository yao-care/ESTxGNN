---
layout: default
title: Gimeracil
parent: Evidencia alta (L1-L2)
nav_order: 375
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Gimeracil: nueva indicación predicha, Neoplasia de colon (nivel de evidencia L1). Indicación original: Cáncer gástrico (según el grafo de conocimiento"
monitor_inn: "gimeracil"
predicted_indications: ["colonic neoplasm", "cecum villous adenoma", "malignant gastric granular cell tumor", "lipoma of colon", "cecum neuroendocrine tumor G1", "rectosigmoid junction neoplasm", "cardia cancer", "colonic lymphangioma", "colon leiomyoma", "gastric lymphoma"]
---

# Gimeracil
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

# Gimeracil: De Cáncer Gástrico a Neoplasia de Colon

## Resumen en Una Frase

Gimeracil es el componente inhibidor de la enzima DPD de la combinación S-1 (tegafur/gimeracil/oteracil), originalmente utilizada para el tratamiento del cáncer gástrico.
El modelo TxGNN predice que podría ser efectivo para **neoplasia de colon**, con **6 ensayos clínicos** y **12 publicaciones** que actualmente respaldan esta dirección (la eficacia se atribuye a la combinación S-1, no a gimeracil por sí solo).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer gástrico (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Neoplasia de colon |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento farmacológico, gimeracil es el inhibidor de la dihidropirimidina deshidrogenasa (DPD) dentro de S-1. Al inhibir esta enzima, ralentiza el catabolismo del 5-fluorouracilo (5-FU) y mantiene la exposición sistémica a este fármaco, generado a partir de su profármaco tegafur. Además, se ha descrito que gimeracil podría inhibir la reparación del ADN por recombinación homóloga, lo que podría aportar un efecto quimiosensibilizante o radiosensibilizante.

El cáncer gástrico y el cáncer de colon son tumores del tubo digestivo sensibles a las fluoropirimidinas. Por ello, un régimen que prolonga la exposición al 5-FU resulta mecanísticamente aplicable al cáncer colorrectal. Conviene subrayar que la eficacia clínica se atribuye a la combinación S-1 en conjunto y no a gimeracil de forma aislada.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Fase 3 | Completado | 1535 | S-1 (TS-1) frente a UFT+leucovorina como tratamiento adyuvante en cáncer de colon estadio III |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Fase 3 | Desconocido | 1191 | SOX (oxaliplatino + S-1) frente a XELOX como quimioterapia adyuvante en cáncer colorrectal estadio III |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Fase 2 | Desconocido | 40 | S-1 + bevacizumab en cáncer colorrectal irresecable o recurrente tras fracaso de quimioterapia previa |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Fase 2 | Desconocido | 82 | Raltitrexed + S-1 en cáncer colorrectal metastásico tras fracaso de quimioterapia estándar; objetivo principal: supervivencia libre de progresión |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Fase 2 | Aún no reclutando | 52 | Fruquintinib + tegafur/gimeracil/oteracil en tercera línea de CCR metastásico (un solo brazo) |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Fase 2 | Terminado | 20 | S-1 o capecitabina con oxaliplatino; evalúa flujo coronario (cardiotoxicidad subclínica), no eficacia |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21084813](https://pubmed.ncbi.nlm.nih.gov/21084813/) | 2010 | Estudio retrospectivo | Gan To Kagaku Ryoho | Factores de riesgo de toxicidad hematológica grado 3-4 (16,1 %) con S-1/irinotecán en 87 pacientes con cáncer de colon avanzado o recurrente |
| [20841935](https://pubmed.ncbi.nlm.nih.gov/20841935/) | 2010 | Estudio farmacocinético | Gan To Kagaku Ryoho | Utilidad de S-1 en metástasis peritoneal de cáncer de colon en un modelo murino |
| [20811661](https://pubmed.ncbi.nlm.nih.gov/20811661/) | 2010 | Preclínico (xenoinjerto) | Oncology Reports | Irinotecán supera la resistencia al 5-FU en xenoinjertos de cáncer de colon al reducir la timidilato sintasa; combinación con S-1 |
| [18630468](https://pubmed.ncbi.nlm.nih.gov/18630468/) | 2008 | Reporte de caso | Anticancer Research | Respuesta completa mantenida con S-1 e irinotecán en metástasis hepáticas de cáncer de colon |
| [29394831](https://pubmed.ncbi.nlm.nih.gov/29394831/) | 2017 | Reporte de caso | Gan To Kagaku Ryoho | Hepatectomía en dos tiempos tras quimioterapia SOX + panitumumab en metástasis hepáticas irresecables |
| [29483452](https://pubmed.ncbi.nlm.nih.gov/29483452/) | 2018 | Reporte de caso | Gan To Kagaku Ryoho | Cáncer de colon transverso con metástasis hepática y trombosis portal tratado con quimioterapia (CapeOX y cambio posterior de régimen) |
| [32936722](https://pubmed.ncbi.nlm.nih.gov/32936722/) | 2021 | Reporte de caso | J Oncol Pharm Pract | Hipertrigliceridemia inducida por S-1 y revisión de la literatura |
| [28414195](https://pubmed.ncbi.nlm.nih.gov/28414195/) | 2017 | Reporte de caso | Eur J Dermatol | Eritrodermia con afectación mucosa extensa y síndrome mano-pie inducidos por TS-1 |
| [41253353](https://pubmed.ncbi.nlm.nih.gov/41253353/) | 2025 | Reporte de caso | Gan To Kagaku Ryoho | Retención urinaria como neuropatía aguda por oxaliplatino en paciente tratado previamente con tegafur/gimeracil/oteracil |
| [35444144](https://pubmed.ncbi.nlm.nih.gov/35444144/) | 2022 | Reporte de caso | Gan To Kagaku Ryoho | Resecciones laparoscópicas repetidas por recurrencias peritoneales tras cirugía de cáncer colorrectal |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 111669001 | TEYSUNO 15 mg/4,35 mg/11,8 mg cápsulas duras | Cápsula dura | No disponible en los datos compilados |
| 111669002 | TEYSUNO 15 mg/4,35 mg/11,8 mg cápsulas duras | Cápsula dura | No disponible en los datos compilados |
| 111669003 | TEYSUNO 20 mg/5,8 mg/15,8 mg cápsulas duras | Cápsula dura | No disponible en los datos compilados |
| 111669004 | TEYSUNO 20 mg/5,8 mg/15,8 mg cápsulas duras | Cápsula dura | No disponible en los datos compilados |

Titular: Nordic Group B.V.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (combinación con fluoropirimidina; gimeracil actúa como modulador de su metabolismo) |
| Riesgo de Mielosupresión | Medio a alto en combinación con otros fármacos; un estudio con S-1/irinotecán describió toxicidad hematológica grado 3-4 en el 16,1 % de los pacientes |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal, electrolitos |
| Protección en Manejo | Seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

Los casos publicados describen eventos adversos asociados a S-1, como hipertrigliceridemia, eritrodermia con afectación mucosa, síndrome mano-pie y toxicidad hematológica. No se han encontrado interacciones farmacológicas registradas en la consulta realizada.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen dos ensayos de Fase 3 relevantes (uno completado, con 1535 pacientes, y otro de estado desconocido) que evalúan regímenes con S-1 en cáncer colorrectal, lo que sitúa la evidencia en nivel L1. Sin embargo, la eficacia corresponde a la combinación S-1 y no a gimeracil de forma aislada, y varios ensayos tienen estado desconocido.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones autorizadas), actualmente no disponible.
- Completar los datos del mecanismo de acción desde DrugBank.
- Verificar los resultados publicados de NCT00660894 y NCT03448549 (entorno tumoral, comparador y desenlaces).
- Definir un plan de monitoreo de seguridad hematológica, cutánea y cardíaca, incluida la evaluación de la actividad de DPD.
- Confirmar que la indicación de cáncer colorrectal no está cubierta ya por la ficha técnica española de Teysuno.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

