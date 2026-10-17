---
layout: default
title: Vitamin A
parent: Solo predicción del modelo (L5)
nav_order: 855
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Vitamin A: nueva indicación predicha, Deficiencia congénita de protrombina (primera predicción del modelo (nivel de evidencia L5). Indicación original: Trastorno por deficiencia vitamínica / deficien…"
monitor_inn: "Vitamin A"
predicted_indications: ["congenital prothrombin deficiency", "biotin metabolic disease", "non-syndromic esophageal malformation", "injury", "cell proliferation disorder", "perinatal disease", "segmental odontomaxillary dysplasia", "florid cemento-osseous dysplasia", "disease by subcellular system affected", "radiation or chemically induced disorder"]
---

# Vitamin A
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

# Vitamina A: De Deficiencia Vitamínica a Enfermedad Perinatal

## Resumen en Una Frase

La vitamina A se utiliza originalmente para tratar los trastornos por deficiencia vitamínica, en particular la deficiencia de vitamina A.
El modelo TxGNN asigna su puntuación más alta a la **deficiencia congénita de protrombina**, pero sin ningún ensayo ni publicación que la respalde. Por eso este informe se centra en la **enfermedad perinatal**, la predicción con evidencia más sólida: **1 ensayo clínico** y **19 publicaciones**, entre ellas varias revisiones sistemáticas Cochrane sobre recién nacidos de muy bajo peso.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastorno por deficiencia vitamínica / deficiencia de vitamina A (la ficha de las autorizaciones españolas no incluye texto de indicación) |
| Nueva Indicación Predicha | Deficiencia congénita de protrombina (primera predicción del modelo; ver nota abajo) |
| Puntaje de Predicción TxGNN | 99,97 % |
| Nivel de Evidencia | L5 (solo predicción del modelo) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

**Nota:** la primera predicción no cuenta con ensayos clínicos ni literatura, y su vínculo con la vitamina A es especulativo. Entre las 10 predicciones evaluadas, las de mayor interés son:

| Predicción | Puntaje TxGNN | Nivel | Decisión |
|------|------|------|------|
| Enfermedad perinatal | 99,63 % | L2 | Pregunta de investigación |
| Lesión (injury) | 99,69 % | L2 | Pregunta de investigación |
| Trastorno de proliferación celular | 99,64 % | L4 | Hold |
| Trastorno inducido por radiación o agentes químicos | 99,63 % | L4 | Hold |
| Las 6 restantes (incluida la deficiencia congénita de protrombina) | 99,63 %–99,97 % | L5 | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la vitamina A (retinol) es un nutriente esencial cuyos metabolitos, como el ácido retinoico, actúan sobre receptores nucleares y regulan la diferenciación celular, la integridad epitelial, la inmunidad y la visión. Su eficacia en la deficiencia de vitamina A está comprobada, y mecanísticamente podría ser aplicable a las nuevas indicaciones.

**Deficiencia congénita de protrombina (primera predicción):** es un defecto genético raro de la síntesis de un factor de coagulación. La vitamina A no tiene un mecanismo establecido para corregirlo. Un posible vínculo con la coagulación dependiente de vitamina K es especulativo y los datos no lo respaldan.

**Enfermedad perinatal (mejor respaldada):** la vitamina A es necesaria para el desarrollo pulmonar y la integridad del epitelio respiratorio. Los prematuros nacen con reservas bajas, lo que se asocia a un mayor riesgo de displasia broncopulmonar. Las revisiones Cochrane de ensayos con vitamina A en recién nacidos de muy bajo peso apuntan a un beneficio modesto sobre la enfermedad pulmonar crónica. El uso intramuscular es molesto y el efecto limitado, por lo que su uso sistemático sigue siendo una pregunta de investigación.

---

## Evidencia de Ensayos Clínicos

Ensayos relacionados con la enfermedad perinatal:

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01115478](https://clinicaltrials.gov/study/NCT01115478) | N/A | Completado | 2500 | Suplementación con zinc y/o vitamina A en el embarazo para reducir la malaria placentaria y sus resultados adversos; relación solo indirecta con la enfermedad perinatal |

Otros ensayos del conjunto de predicciones (indicación «lesión»):

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01203488](https://clinicaltrials.gov/study/NCT01203488) | Fase 1/2 | Completado | 807 | Ensayo aleatorizado de dosis más alta de vitamina A en recién nacidos de peso extremadamente bajo; evalúa supervivencia sin displasia broncopulmonar y sepsis |
| [NCT02102711](https://clinicaltrials.gov/study/NCT02102711) | N/A | Completado | 62 | Vitamina A oral en neonatos <1500 g para prevenir displasia broncopulmonar y retinopatía del prematuro |
| [NCT04000789](https://clinicaltrials.gov/study/NCT04000789) | N/A | Desconocido | 96 | Colirio de vitamina A, vitamina E y hialuronato en retinopatía diabética (indicación «trastorno de proliferación celular»); estudio de superficie ocular, evidencia indirecta |

---

## Evidencia de Literatura

Publicaciones de mayor jerarquía para la enfermedad perinatal (revisiones sistemáticas y meta-análisis):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27552058](https://pubmed.ncbi.nlm.nih.gov/27552058/) | 2016 | Revisión sistemática | Cochrane Database Syst Rev | Vitamina A para prevenir mortalidad y morbilidad en recién nacidos de muy bajo peso |
| [21975731](https://pubmed.ncbi.nlm.nih.gov/21975731/) | 2011 | Revisión sistemática | Cochrane Database Syst Rev | Versión previa de la misma revisión; la vitamina A es necesaria para el crecimiento pulmonar |
| [17943744](https://pubmed.ncbi.nlm.nih.gov/17943744/) | 2007 | Revisión sistemática | Cochrane Database Syst Rev | Actualización de la revisión sobre enfermedad pulmonar crónica en prematuros |
| [12519545](https://pubmed.ncbi.nlm.nih.gov/12519545/) | 2002 | Revisión sistemática | Cochrane Database Syst Rev | Versión anterior sobre morbimortalidad en recién nacidos de muy bajo peso |
| [10796372](https://pubmed.ncbi.nlm.nih.gov/10796372/) | 2000 | Revisión sistemática | Cochrane Database Syst Rev | Primera versión de la revisión |
| [22742601](https://pubmed.ncbi.nlm.nih.gov/22742601/) | 2012 | Revisión sistemática y meta-análisis | Paediatr Perinat Epidemiol | Vitamina A y carotenoides durante el embarazo y resultados maternos, neonatales e infantiles |
| [25222155](https://pubmed.ncbi.nlm.nih.gov/25222155/) | 2014 | Revisión | JAMA Pediatrics | Déficit de vitamina A y riesgo de displasia broncopulmonar |
| [23445845](https://pubmed.ncbi.nlm.nih.gov/23445845/) | 2013 | Revisión | J Pediatr | Vitaminas A y D en el período materno-perinatal; faltan dosis óptimas, momento y vía de administración |
| [2672772](https://pubmed.ncbi.nlm.nih.gov/2672772/) | 1989 | Revisión | Am J Clin Nutr | Retinol en el neonato y problemas del prematuro, con reservas reducidas |
| [36479498](https://pubmed.ncbi.nlm.nih.gov/36479498/) | 2022 | Revisión | J Prev Med Hyg | Principales deficiencias nutricionales |

Hay otras publicaciones relevantes para la indicación «lesión», como una revisión sobre vitamina A y cicatrización de heridas ([31697447](https://pubmed.ncbi.nlm.nih.gov/31697447/), 2019). También hay un meta-análisis que asocia una ingesta alta de vitamina A con mayor riesgo de fractura ([34105132](https://pubmed.ncbi.nlm.nih.gov/34105132/), 2021).

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 28811 | RINOCUSI VITAMÍNICO 12.500 UI/g POMADA NASAL | Pomada nasal | No disponible en los datos compilados |
| 24328 | AUXINA A MASIVA 50.000 UI CÁPSULAS BLANDAS | Cápsula dura | No disponible en los datos compilados |
| 66883 | RINOVITEX 12.500 UI/g POMADA NASAL | Pomada nasal | No disponible en los datos compilados |

---

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no el prospecto):** enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, úlcera péptica, sarcoidosis, hipercalcemia, nefrocalcinosis, nefrolitiasis, hiperfosfatemia, enfermedad inflamatoria intestinal y colitis ulcerosa, anemia falciforme, anemia hemolítica, hemocromatosis hereditaria, hemosiderosis, enfermedad de Wilson, hiperoxaluria primaria, hipervitaminosis, arteriosclerosis obliterante y gastroenteritis, entre otras.
- **Interacciones farmacológicas:** se identificaron 68 interacciones. Las más relevantes son de nivel **mayor** con retinoides (isotretinoína, acitretina, tretinoína) y con tetraciclinas (doxiciclina, minociclina, tetraciclina, oxitetraciclina, demeclociclina, omadaciclina, eravaciclina, sarecyclina). De nivel **moderado**: bexaroteno, colestiramina, colesevelam, colestipol, sevelamer y selpercatinib. Con orlistat la interacción es menor.
- **Señales de seguridad en la literatura:** la ingesta elevada de vitamina A se asocia a riesgo de fracturas y a toxicidad hepática (hipervitaminosis A), por lo que se requieren límites de dosis.

Consultar el prospecto para las advertencias y contraindicaciones oficiales, que no están disponibles en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal (deficiencia congénita de protrombina) es solo una predicción del grafo, sin ensayos ni literatura, y sin mecanismo plausible. La mejor respaldada es la enfermedad perinatal (L2, revisiones Cochrane con efecto modesto), pero el único ensayo listado es indirecto. Podría avanzar como pregunta de investigación con salvaguardas de dosis.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y de las advertencias y contraindicaciones del prospecto de la AEMPS (carencias actuales).
- Confirmar la relevancia de los ensayos específicos en prematuros (p. ej., NCT01203488) para la enfermedad perinatal.
- Definir dosis, vía de administración y plan de monitorización de seguridad (hígado, hueso, calcio), en especial en recién nacidos y embarazadas.
- Evaluar la compatibilidad de vías de administración (pendiente) frente a las formas comercializadas (pomada nasal y cápsulas).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

