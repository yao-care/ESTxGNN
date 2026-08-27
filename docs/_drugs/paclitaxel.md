---
layout: default
title: Paclitaxel
parent: 僅模型預測 (L5)
nav_order: 207
evidence_level: L5
indication_count: 10
---

# Paclitaxel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Paclitaxel: De Cáncer de Ovario a Carcinoma de Mama Femenino

## Resumen en Una Frase

Paclitaxel es un agente quimioterapéutico taxano cuya indicación original, según la información conocida, fue el cáncer de ovario refractario a platino. El modelo TxGNN predice que también podría ser efectivo para **Carcinoma de Mama Femenino**, con **50 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de ovario refractario (según información conocida sobre el fármaco; este Evidence Pack no registra autorizaciones ni indicaciones aprobadas en España) |
| Nueva Indicación Predicha | Carcinoma de Mama Femenino |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Paclitaxel se une a la subunidad β de la tubulina y estabiliza los microtúbulos, impidiendo su despolimerización normal. Esto bloquea la célula en la fase de metafase de la mitosis e induce apoptosis. Es un mecanismo antiproliferativo directo, independiente del tejido de origen del tumor, que actúa sobre cualquier población celular con alta tasa de división.

El cáncer de ovario (indicación original) y el carcinoma de mama comparten esta característica biológica: son tumores sólidos con subpoblaciones celulares de proliferación elevada, altamente sensibles a agentes antimicrotúbulo. De hecho, el uso de paclitaxel en cáncer de mama ya está ampliamente documentado y validado clínicamente desde hace décadas (regímenes adyuvantes y metastásicos con doxorrubicina/ciclofosfamida seguidos de paclitaxel, combinaciones con trastuzumab en enfermedad HER2-positiva, nab-paclitaxel en triple negativo, etc.), lo que explica la puntuación extremadamente alta del modelo TxGNN.

Es importante señalar que, en este caso, la "nueva indicación predicha" corresponde en realidad a un uso oncológico ya consolidado de paclitaxel a nivel mundial. La señal TxGNN aquí actúa más como una confirmación de plausibilidad mecanística que como el descubrimiento de un uso genuinamente inédito, lo cual refuerza la solidez del razonamiento pero reduce el valor de "novedad" del hallazgo.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00016406](https://clinicaltrials.gov/study/NCT00016406) | Fase 3 | Completado | 399 | Doxorrubicina+ciclofosfamida seguido de paclitaxel semanal vs. régimen alternativo con filgrastim, en cáncer de mama inflamatorio/localmente avanzado |
| [NCT00014222](https://clinicaltrials.gov/study/NCT00014222) | Fase 3 | Completado | 2104 | Comparación de tres regímenes adyuvantes que incluyen paclitaxel secuencial (EC+filgrastim+epoetina vs. AC vs. CEF) en cáncer de mama con ganglios positivos o alto riesgo |
| [NCT00003612](https://clinicaltrials.gov/study/NCT00003612) | Fase 2 | Completado | 92 | Paclitaxel+carboplatino+trastuzumab como primera línea en cáncer de mama metastásico HER2-positivo |
| [NCT02413320](https://clinicaltrials.gov/study/NCT02413320) | Fase 2 | Completado | 101 | Neoadyuvante carboplatino+docetaxel vs. carboplatino+paclitaxel en cáncer de mama triple negativo en estadio I-III |
| [NCT00003992](https://clinicaltrials.gov/study/NCT00003992) | Fase 2 | Completado | 200 | Paclitaxel+trastuzumab adyuvante en cáncer de mama en estadio temprano HER2-positivo |
| [NCT00003539](https://clinicaltrials.gov/study/NCT00003539) | Fase 2 | Completado | 50 | Paclitaxel semanal (1 hora) + trastuzumab en cáncer de mama metastásico |
| [NCT01705691](https://clinicaltrials.gov/study/NCT01705691) | Fase 2 | Completado | 50 | Paclitaxel semanal o eribulina seguido de doxorrubicina+ciclofosfamida, neoadyuvante en cáncer de mama HER2-negativo localmente avanzado |
| [NCT01307891](https://clinicaltrials.gov/study/NCT01307891) | Fase 2 | Completado | 64 | Abraxane (nab-paclitaxel) con o sin tigatuzumab en cáncer de mama metastásico triple negativo |
| [NCT00005649](https://clinicaltrials.gov/study/NCT00005649) | Fase 2 | Completado | N/A | Combinación de capecitabina y paclitaxel estándar como primera o segunda línea en carcinoma de mama metastásico |
| [NCT00054028](https://clinicaltrials.gov/study/NCT00054028) | Fase 1/2 | Completado | 31 | Suramina + paclitaxel en cáncer de mama metastásico avanzado (estadio IIIB/IV) |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Estudio Clínico/Cohorte | Cancer | Ensayo fase II multicéntrico de doxorrubicina+paclitaxel en carcinoma de mama avanzado; relevancia de terapia adyuvante previa con antraciclinas |
| [31783552](https://pubmed.ncbi.nlm.nih.gov/31783552/) | 2019 | Revisión | Biomolecules | Revisión de los efectos mecanísticos y clínicos de paclitaxel en cáncer de mama, incluyendo resistencia al tratamiento |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Revisión | Drug and Therapeutics Bulletin | Revisión histórica de paclitaxel y docetaxel en cáncer de mama y ovario, ampliación de indicación a primera línea |
| [17272681](https://pubmed.ncbi.nlm.nih.gov/17272681/) | 2007 | Preclínico/Mecanístico | Molecular Pharmacology | Mecanismos de resistencia mediada por estatmina a paclitaxel y vinblastina en células de carcinoma de mama |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | Pendiente clasificación | Chemical Biology & Drug Design | Potencial terapéutico de combinaciones de paclitaxel en carcinoma de mama con biomarcadores in vivo |
| [31515668](https://pubmed.ncbi.nlm.nih.gov/31515668/) | 2019 | Pendiente clasificación | Cancer Chemotherapy and Pharmacology | Regulación de SRSF3 y sensibilización a paclitaxel en cáncer de mama y carcinoma oral de células escamosas |
| [39009452](https://pubmed.ncbi.nlm.nih.gov/39009452/) | 2024 | Pendiente clasificación | Journal for Immunotherapy of Cancer | Papel de paclitaxel sobre macrófagos asociados a tumor y potenciación del bloqueo PD-1 en cáncer de mama triple negativo |
| [20665703](https://pubmed.ncbi.nlm.nih.gov/20665703/) | 2011 | Pendiente clasificación | Journal of Cellular Physiology | ZD6474 potencia efectos antiproliferativos y apoptóticos de paclitaxel en células de carcinoma de mama |
| [32461977](https://pubmed.ncbi.nlm.nih.gov/32461977/) | 2020 | Pendiente clasificación | BioMed Research International | Estudio de mundo real de quimioterapia neoadyuvante con epirubicina/ciclofosfamida y paclitaxel semanal+trastuzumab en cáncer de mama HER2-positivo |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | Pendiente clasificación | Nature Communications | Variantes en TEKT4 asociadas a resistencia de cáncer de mama a paclitaxel |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (clase taxano, agente estabilizador de microtúbulos) |
| Riesgo de Mielosupresión | Alto — la neutropenia es la toxicidad dosis-limitante más frecuentemente documentada para esta clase de fármaco, con riesgo de neutropenia febril |
| Clasificación de Emetogenicidad | Moderada |
| Items de Monitoreo | Hemograma completo con diferencial (especialmente recuento de neutrófilos), función hepática, evaluación de neuropatía periférica, vigilancia de reacciones de hipersensibilidad durante la infusión |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos/antineoplásicos (equipo de protección personal, preparación en cabina de bioseguridad, manejo seguro de residuos) |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El nivel de evidencia L1 (respaldado por al menos un ECA de Fase 3 completado, NCT00016406, más múltiples ensayos Fase 2 completados) y una puntuación TxGNN extremadamente alta (99.99%) confirman que el uso de paclitaxel en carcinoma de mama es mecanística y clínicamente sólido. Sin embargo, existen brechas regulatorias relevantes en este Evidence Pack (sin datos de MOA estructurados, sin registro de autorizaciones en España) que impiden avanzar sin salvaguardas adicionales.

**Para avanzar se necesita:**
- Ficha técnica/prospecto de la AEMPS para España (advertencias, contraindicaciones, interacciones farmacológicas)
- Verificación del estado real de comercialización en España, ya que el estado "no comercializado" registrado aquí es inconsistente con el uso clínico global ampliamente establecido de paclitaxel y podría reflejar una brecha en la fuente de datos
- Datos estructurados de mecanismo de acción (MOA) a nivel de fármaco (actualmente marcado como brecha de datos DG002)
- Revisión de posible redundancia con otras indicaciones predichas del mismo candidato (ER-positivo, ER-negativo, perfil de expresión génica), que probablemente representan el mismo fenómeno clínico de uso de paclitaxel en cáncer de mama
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

