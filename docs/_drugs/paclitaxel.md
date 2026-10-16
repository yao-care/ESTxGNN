---
layout: default
title: Paclitaxel
parent: Solo predicción del modelo (L5)
nav_order: 602
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Paclitaxel: nueva indicación predicha, Carcinoma de mama femenino (nivel de evidencia L5). Indicación original: Cáncer de ovario (el texto de indicación aprobada de las autorizacion…"
monitor_inn: "PACLITAXEL"
predicted_indications: ["female breast carcinoma", "estrogen-receptor negative breast cancer", "estrogen-receptor positive breast cancer", "hormone-resistant breast carcinoma", "Ehrlich tumor carcinoma", "bilateral breast carcinoma", "breast carcinoma by gene expression profile", "nipple carcinoma", "parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
---

# Paclitaxel
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

# Paclitaxel: De Cáncer de Ovario a Carcinoma de Mama Femenino

## Resumen en Una Frase

Paclitaxel es un citotóxico antimicrotúbulos, originalmente utilizado para el tratamiento del cáncer de ovario (además de otras indicaciones registradas en el grafo de conocimiento, como hipertensión y glaucoma de ángulo abierto).
El modelo TxGNN predice que podría ser efectivo para **carcinoma de mama femenino**, con **41 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección. Se trata, en la práctica, de un uso ya establecido en la clínica más que de un reposicionamiento en sentido estricto.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de ovario (el texto de indicación aprobada de las autorizaciones españolas no está disponible; se toma la indicación original del grafo de conocimiento) |
| Nueva Indicación Predicha | Carcinoma de mama femenino |
| Puntaje de Predicción TxGNN | 99.995% |
| Nivel de Evidencia | L2 (según la puntuación del análisis; ver nota en la conclusión) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 12 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, paclitaxel pertenece a la clase de los taxanos: estabiliza los microtúbulos, impide el desensamblaje del huso mitótico y provoca detención del ciclo celular en G2/M y apoptosis en células que se dividen rápidamente.

El cáncer de ovario y el cáncer de mama son ambos tumores ginecológicos/mamarios de rápida proliferación, sensibles a quimioterapia citotóxica. Como el mecanismo antimitótico no depende de receptores hormonales, es mecanísticamente aplicable a la mama. De hecho, la literatura señala que los taxanos son componentes basados en evidencia del tratamiento del cáncer avanzado de mama, pulmón y ovario, y que paclitaxel fue extendido a cáncer de mama metastásico y adyuvante.

Por ello, la predicción es coherente con la práctica clínica establecida. La limitación es que la mayoría de los ensayos listados son estudios de combinación de fase 1/2, y los datos no incluyen un ECA de fase 3 que aísle la contribución de paclitaxel en esta entrada específica.

## Evidencia de Ensayos Clínicos

Se muestran los 10 ensayos más relevantes, de 41 registrados.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00003539](https://clinicaltrials.gov/study/NCT00003539) | Fase 2 | Completado | 50 | Paclitaxel semanal más anticuerpo anti-HER2 (trastuzumab) en cáncer de mama metastásico o recurrente |
| [NCT00006120](https://clinicaltrials.gov/study/NCT00006120) | Fase 2 | Desconocido | N/D | Comparación aleatorizada de dos pautas de docetaxel o paclitaxel en cáncer de mama metastásico |
| [NCT00667251](https://clinicaltrials.gov/study/NCT00667251) | Fase 3 | Completado | 652 | Quimioterapia con taxano más lapatinib vs. trastuzumab en primera línea de cáncer de mama metastásico HER2 positivo |
| [NCT01822314](https://clinicaltrials.gov/study/NCT01822314) | Fase 3 | Completado | 632 | Nab-paclitaxel neoadyuvante vs. paclitaxel con solvente, seguido de antraciclinas, en cáncer de mama HER2 negativo de alto riesgo |
| [NCT00006459](https://clinicaltrials.gov/study/NCT00006459) | Fase 3 | Completado | N/D | Gemcitabina más paclitaxel vs. paclitaxel en cáncer de mama avanzado irresecable o metastásico |
| [NCT00553358](https://clinicaltrials.gov/study/NCT00553358) | Fase 3 | Completado | 455 | Neo-ALTTO: lapatinib, trastuzumab o ambos más paclitaxel neoadyuvante en cáncer de mama HER2 positivo |
| [NCT00513292](https://clinicaltrials.gov/study/NCT00513292) | Fase 3 | Completado | 280 | Neoadyuvancia FEC seguido de paclitaxel más trastuzumab vs. secuencia inversa en cáncer de mama HER2 positivo |
| [NCT00075270](https://clinicaltrials.gov/study/NCT00075270) | Fase 3 | Completado | 580 | Lapatinib más paclitaxel vs. paclitaxel solo en primera línea de cáncer de mama avanzado o metastásico |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | Fase 3 | Completado | 478 | FE75C denso en dosis seguido de docetaxel vs. paclitaxel como adyuvancia en mama con ganglios positivos |
| [NCT00002826](https://clinicaltrials.gov/study/NCT00002826) | Fase 2 | Completado | 36 | Piloto de PSC 833 para modular la resistencia a paclitaxel en cáncer de mama metastásico |

## Evidencia de Literatura

Se muestran las publicaciones más relevantes, priorizando ensayos y revisiones.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Ensayo clínico (fase II) | Cancer | Eficacia y toxicidad de doxorrubicina más paclitaxel en cáncer de mama metastásico; importancia del tratamiento previo con antraciclinas |
| [10791395](https://pubmed.ncbi.nlm.nih.gov/10791395/) | 2000 | Revisión | Lancet | Los taxanos son componentes basados en evidencia del tratamiento del cáncer avanzado de mama, pulmón y ovario; paclitaxel aprobado en EE. UU. como adyuvante en mama con ganglios positivos |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Revisión | Drug and Therapeutics Bulletin | Paclitaxel y docetaxel en cáncer de mama y ovario; ampliación de la licencia a primera línea en ovario y mama metastásico |
| [10898354](https://pubmed.ncbi.nlm.nih.gov/10898354/) | 2000 | Revisión | Cancer | Evolución de la quimioterapia del cáncer de mama, incluidos los regímenes con antraciclinas y taxanos |
| [9296218](https://pubmed.ncbi.nlm.nih.gov/9296218/) | 1997 | Estudio de búsqueda de dosis | Annals of Oncology | Dosis máximas toleradas de paclitaxel en infusión de 3 horas con ciclofosfamida en cáncer de mama avanzado |
| [11745249](https://pubmed.ncbi.nlm.nih.gov/11745249/) | 2001 | Estudio clínico | Cancer | Papel de paclitaxel en el tratamiento multimodal del carcinoma inflamatorio de mama |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | Estudio genómico | Nature Communications | Variaciones en TEKT4 y resistencia del cáncer de mama a paclitaxel |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | Preclínico/computacional | Chemical Biology & Drug Design | Combinaciones de paclitaxel contra carcinoma de mama e identificación de biomarcadores in vivo |
| [20665703](https://pubmed.ncbi.nlm.nih.gov/20665703/) | 2011 | Preclínico | Journal of Cellular Physiology | ZD6474 potencia los efectos antiproliferativos y apoptóticos de paclitaxel en células de carcinoma de mama |
| [7904376](https://pubmed.ncbi.nlm.nih.gov/7904376/) | 1993 | Revisión | Seminars in Oncology Nursing | Panorama histórico del desarrollo de paclitaxel (Taxol) |

## Información de Mercado en España

Existen 12 autorizaciones vigentes (todas de medicamentos con un solo principio activo). Los datos compilados no incluyen el texto de la indicación aprobada. Se muestran las 5 principales.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 73010 | Paclitaxel Accord 6 mg/ml EFG | Concentrado para solución para perfusión | No disponible en los datos compilados |
| 66997 | Paclitaxel Teva 6 mg/ml EFG | Concentrado para solución para perfusión | No disponible en los datos compilados |
| 66311 | Paclitaxel Hospira 6 mg/ml EFG | Concentrado para solución para perfusión | No disponible en los datos compilados |
| 07428001 | Abraxane 5 mg/ml | Polvo para dispersión para perfusión | No disponible en los datos compilados |
| 89649 | Bugvi 5 mg/ml EFG | Polvo para dispersión para perfusión | No disponible en los datos compilados |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (taxano, inhibidor de la despolimerización de microtúbulos) |
| Riesgo de Mielosupresión | Alto (neutropenia y trombocitopenia; el grafo de conocimiento registra neutropenia, agranulocitosis, trombocitopenia y anemia como condiciones de precaución) |
| Clasificación de Emetogenicidad | Baja a moderada |
| Items de Monitoreo | Hemograma con diferencial, función hepática (bilirrubina) y renal, signos de neuropatía periférica y reacciones de hipersensibilidad |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos. Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de precaución (según el grafo de conocimiento, no el prospecto)**: neutropenia, agranulocitosis, trombocitopenia, anemia, neuropatía periférica, enfermedad hepática, hiperbilirrubinemia (incluido síndrome de Gilbert), enfermedad renal, infarto de miocardio y paro cardíaco súbito, hipotensión, asma, diabetes (incluida cetoacidosis diabética), psoriasis, enfermedad de la vesícula biliar y trastornos de ansiedad/neuróticos/distímicos.
- **Interacciones Farmacológicas** (100 registradas; principales): nivel moderado con aprepitant, cimetidina, claritromicina, clotrimazol, dexametasona, eliglustat, metronidazol, miconazol, rolapitant, rosuvastatina, simvastatina, tinidazol y troglitazona. Nivel menor con ácido ascórbico y levofloxacino.
- **Eventos adversos descritos en la literatura**: neumonitis, uveítis intermedia, lesiones epiteliales corneales, síndrome PATEO y polineuropatía inducida por taxanos.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Paclitaxel tiene un mecanismo antimitótico plausible y un uso establecido en cáncer de mama, respaldado por numerosos ensayos de fase 2 y 3 (la mayoría de combinación o con paclitaxel como parte del esquema base). El nivel de evidencia asignado a esta entrada es L2, porque los datos no incluyen un ECA de fase 3 que aísle el aporte de paclitaxel.

**Otras predicciones del análisis (resumen):**
- Cáncer de mama negativo para receptor de estrógeno: L2, Proceed with Guardrails.
- Cáncer de mama positivo para receptor de estrógeno: L1, Proceed with Guardrails (los ensayos de fase 3 son indirectos, con paclitaxel como esquema base o comparador).
- Carcinoma de mama resistente a hormonas: L2, Proceed with Guardrails.
- Carcinoma de Ehrlich, carcinoma de mama bilateral, carcinoma de mama por perfil de expresión génica y carcinoma del pezón: evidencia limitada a estudios preclínicos o reportes de caso (L3-L4), con decisión Hold o pregunta de investigación.
- Rabdomiosarcoma embrionario parameníngeo y rabdomiosarcoma botrioide de vagina: solo predicción del modelo (L5), Hold.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones oficiales), actualmente ausente y que bloquea el cribado de seguridad.
- Completar los datos de mecanismo de acción (por ejemplo, consultando la API de DrugBank).
- Confirmar el texto de indicaciones aprobadas de las autorizaciones españolas, para verificar si mama ya figura en la ficha técnica.
- Priorizar evidencia de fase 3 específica de paclitaxel en cada subtipo de mama.
- Plan de monitoreo de seguridad (mielosupresión, neuropatía, hipersensibilidad, interacciones con inhibidores o inductores del CYP).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

