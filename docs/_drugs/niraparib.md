---
layout: default
title: Niraparib
parent: Solo predicción del modelo (L5)
nav_order: 569
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
monitor_inn: "NIRAPARIB"
predicted_indications: ["epiglottis neoplasm", "cystic neoplasm", "benign neoplasm of hypopharynx", "benign neoplasm of tongue", "benign neoplasm of floor of mouth", "cervical neuroblastoma", "tumor of testis and paratestis", "inner ear neoplasm", "pre-malignant neoplasm", "schwannoma of jugular foramen"]
description: "Niraparib: nueva indicación predicha, Epiglottis neoplasm (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Niraparib
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

## Niraparib: Epiglottis neoplasm
{: .text-alpha }

## Resumen en Una Frase

Niraparib es un inhibidor de PARP, originalmente asociado a tumores de ovario y peritoneo (cáncer peritoneal primario, carcinoma seroso peritoneal y neoplasia epitelial maligna de ovario).
El modelo TxGNN predice que podría ser efectivo para **Neoplasia Quística**, la predicción con mayor respaldo de evidencia entre las candidatas,
con **3 ensayos clínicos** (1 de ellos terminado con solo 11 pacientes y 1 retirado sin inscripción) y **10 publicaciones**, en su mayoría preclínicas o de cohorte.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Epiglottis neoplasm |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 (según la clasificación de los datos; ver nota en la conclusión) |
| Estado de Mercado en España | Comercializado (registros vigentes: 1 de 2) |
| Número de Autorizaciones | 2 (vigentes: 1) |
| Decisión Recomendada | Hold (con la neoplasia quística tratada como pregunta de investigación) |

> **Nota sobre la lista de candidatas:** Las otras nueve indicaciones predichas (p. ej., neoplasia de epiglotis, neoplasia benigna de hipofaringe, neoplasia benigna de lengua, neuroblastoma cervical, tumor de testículo y paratestículo) no tienen ensayos clínicos ni literatura en los datos compilados. Su nivel de evidencia es L5 y su recomendación es Hold. Este informe se centra en la candidata de rango 2, la única con evidencia.

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, niraparib pertenece a la clase de los inhibidores de PARP, que explotan la letalidad sintética en tumores con deficiencia de recombinación homóloga (HRD).

La etiqueta "neoplasia quística" parece ser una asignación amplia de la ontología hacia tumores de tipo seroso/ovárico. Los ensayos y publicaciones disponibles se refieren al carcinoma seroso de endometrio y al carcinoma seroso de alto grado de ovario, tumores con características moleculares similares (inestabilidad cromosómica, alteraciones en el número de copias) y con posible HRD, lo que los hace plausiblemente sensibles a los inhibidores de PARP.

Por ello, esta predicción es en parte una extensión de las indicaciones ya conocidas de niraparib (ovario y peritoneo) y no una señal clara de reposicionamiento. La relación con la indicación original es cercana, pero la similitud formal con la indicación original figura como pendiente de evaluar.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04716686](https://clinicaltrials.gov/study/NCT04716686) | Fase 2 | Reclutando | 83 | Niraparib en monoterapia como mantenimiento y tratamiento de recurrencia en carcinoma seroso de endometrio; sin resultados disponibles aún |
| [NCT04159155](https://clinicaltrials.gov/study/NCT04159155) | Fase 2/3 | Terminado | 11 | Ensayo multibrazo y multietapa de tratamiento de primera línea y mantenimiento en cáncer de endometrio seroso o con p53 mutado; con solo 11 pacientes aporta datos de eficacia mínimos |
| [NCT05289648](https://clinicaltrials.gov/study/NCT05289648) | Fase 0 / Fase 1 temprana | Retirado | 0 | Niraparib preoperatorio en cáncer de endometrio de alto grado; sin pacientes, no aporta evidencia |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31466953](https://pubmed.ncbi.nlm.nih.gov/31466953/) | 2019 | Reporte de caso | BMJ Case Reports | Niraparib como mantenimiento en una paciente con cáncer de ovario y metástasis cerebrales |
| [40473279](https://pubmed.ncbi.nlm.nih.gov/40473279/) | 2025 | Protocolo de ensayo fase II | BMJ Open | Mantenimiento con niraparib en carcinoma seroso uterino en estadios III/IV o recurrente |
| [41323499](https://pubmed.ncbi.nlm.nih.gov/41323499/) | 2025 | Cohorte | Pathol Oncol Res | El perfil genómico completo para HRD orienta las recomendaciones de inhibidores de PARP en cáncer de ovario |
| [42442041](https://pubmed.ncbi.nlm.nih.gov/42442041/) | 2026 | Cohorte | Gynecol Oncol | Utilidad real de las pruebas de HRD en carcinoma seroso de alto grado sin mutación BRCA1/2; la amplificación de MYC como posible marcador sustituto |
| [42157333](https://pubmed.ncbi.nlm.nih.gov/42157333/) | 2026 | Cohorte | Clin Epigenetics | Nomograma basado en la metilación de promotores de genes HRR para predecir la eficacia de inhibidores de PARP y la supervivencia libre de progresión |
| [34321239](https://pubmed.ncbi.nlm.nih.gov/34321239/) | 2021 | Preclínico | Cancer Res | La pérdida de metilación del promotor de RAD51C causa resistencia a inhibidores de PARP en carcinoma seroso de alto grado |
| [41520277](https://pubmed.ncbi.nlm.nih.gov/41520277/) | 2026 | Preclínico | Cancer Biol Ther | Eficacia de la combinación de carboplatino e inhibidor de PARP en esferoides y organoides de carcinoma seroso de alto grado |
| [41465250](https://pubmed.ncbi.nlm.nih.gov/41465250/) | 2025 | Preclínico | Int J Mol Sci | Análisis proteómico de los efectos poli-farmacológicos de los inhibidores de PARP en células de cáncer de ovario seroso de alto grado |
| [41214101](https://pubmed.ncbi.nlm.nih.gov/41214101/) | 2025 | Preclínico | Sci Rep | Claudina-4 como regulador de la estabilidad genómica y la evasión inmunitaria en carcinoma seroso de alto grado |
| [40702505](https://pubmed.ncbi.nlm.nih.gov/40702505/) | 2025 | Preclínico | J Ovarian Res | Subtipos de carcinoma seroso de ovario de alto grado basados en células madre y modelo pronóstico |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1171235001 | ZEJULA 100 mg cápsulas duras | Cápsula dura | No disponible en los datos compilados |
| 1171235006 | ZEJULA 100 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de PARP) |
| Riesgo de Mielosupresión | Medio a alto (los datos de las candidatas mencionan mielosupresión como un riesgo relevante; consultar el prospecto para frecuencias) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma completo, presión arterial (se menciona hipertensión como riesgo), función hepática y renal |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto y la normativa local de manejo de medicamentos peligrosos |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total (fuente: DDInter). Entre las mostradas, las de nivel **Mayor** son:
  - Deferiprona
  - Lexidronam de samario (153Sm)

  Las de nivel **Moderado** incluyen:
  - Ácido acetilsalicílico
  - Rolapitant
  - Radiofármacos y anticuerpos radiomarcados: iobenguano (I-131), ibritumomab tiuxetán, tositumomab (con y sin I-131), cloruro de estroncio Sr-89
  - Palifermina
  - Antitrombóticos y anticoagulantes: abciximab, alteplasa, antitrombina III humana, apixabán, dipiridamol, betrixabán, bivalirudina, cangrelor, caplacizumab, cilostazol

  Predominan los fármacos con riesgo de mielosupresión (radiofármacos, deferiprona) y los que afectan a la hemostasia (anticoagulantes y antiagregantes), lo que sugiere vigilar el riesgo hematológico y hemorrágico.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La candidata "neoplasia quística" tiene solo evidencia de fase 2 en curso (sin resultados), un ensayo de fase 2/3 terminado con 11 pacientes y otro retirado sin inscripción; la literatura es mayormente preclínica o de cohorte. Aunque los datos la clasifican como L2, no hay ningún ensayo de fase 3 completado, y la etiqueta parece un mapeo amplio a tumores serosos próximos a las indicaciones ya conocidas de niraparib, por lo que se trata más de una pregunta de investigación que de un reposicionamiento claro. Las otras nueve candidatas carecen totalmente de evidencia (L5).

**Para avanzar se necesita:**
- Obtener los datos de mecanismo de acción (DrugBank) y el texto de indicaciones aprobadas y advertencias/contraindicaciones del prospecto de la AEMPS, hoy ausentes y necesarios para el cribado de seguridad
- Definir con precisión qué subtipos de neoplasia quística se pretende tratar y su relación con las indicaciones ya autorizadas
- Esperar los resultados del ensayo de fase 2 NCT04716686 y de nuevos ensayos de fase 3
- Establecer la presencia de HRD u otros biomarcadores en la población objetivo
- Elaborar un plan de monitoreo hematológico y de presión arterial, y revisar las interacciones de nivel Mayor y Moderado
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

