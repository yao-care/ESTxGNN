---
layout: default
title: Sunitinib
parent: 僅模型預測 (L5)
nav_order: 266
evidence_level: L5
indication_count: 10
---

# Sunitinib
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

Usando el Evidence Pack proporcionado, aquí está el informe de evaluación:

---

# Sunitinib: De Carcinoma de Células Renales y GIST a Liposarcoma

## Resumen en Una Frase

Sunitinib es un inhibidor multidiana de tirosina quinasas cuya eficacia está documentada en la literatura clínica incluida en este Evidence Pack para el carcinoma de células renales avanzado, el tumor del estroma gastrointestinal (GIST) y el tumor neuroendocrino pancreático avanzado (no hay registro formal de comercialización en España). El modelo TxGNN predice que podría ser efectivo para **Liposarcoma**, con **3 ensayos clínicos** y **9 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Carcinoma de células renales (RCC) avanzado, tumor del estroma gastrointestinal (GIST) y tumor neuroendocrino pancreático avanzado* |
| Nueva Indicación Predicha | Liposarcoma |
| Puntaje de Predicción TxGNN | 99.87% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Research Question (Pregunta de Investigación) |

\* *No existe un registro regulatorio formal en España (el fármaco no está comercializado; 0 autorizaciones). Esta indicación original se ha derivado de los ensayos clínicos incluidos en el Evidence Pack — p. ej., NCT01829217 describe explícitamente que "sunitinib ha sido aprobado por la FDA para el tratamiento de tumores del estroma gastrointestinal, carcinoma de células renales avanzado y tumores neuroendocrinos pancreáticos avanzados".*

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos verificados de mecanismo de acción (MOA) procedentes de una fuente regulatoria — este es un vacío de datos de prioridad **alta** (DG002) que debe resolverse antes de avanzar. Según la evidencia disponible en este Evidence Pack, sunitinib es un inhibidor multidiana de tirosina quinasas (VEGFR1-3, PDGFR-α/β, KIT, FLT3, RET), cuya eficacia antiangiogénica y antiproliferativa ha sido comprobada en carcinoma de células renales y GIST.

El liposarcoma (especialmente los subtipos mixoide y de células redondas) presenta una elevada angiogénesis tumoral y, en parte, activación de la vía de señalización de PDGFR, lo que otorga plausibilidad biológica al mecanismo antiangiogénico de sunitinib. Esta hipótesis está respaldada por un ensayo clínico de fase II centrado específicamente en tres histologías prevalentes de sarcoma de tejido blando —incluido el liposarcoma— (PMID 21154746), así como por un reporte de caso de beneficio clínico prolongado con sunitinib en liposarcoma metastásico intensamente pretratado (PMID 23482782).

No obstante, ninguno de los ensayos clínicos disponibles fue diseñado específicamente para el subtipo liposarcoma (se trata de poblaciones mixtas de sarcoma de tejido blando), por lo que la evidencia mecanística es plausible pero no concluyente.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00400569](https://clinicaltrials.gov/study/NCT00400569) | Fase 2 | Completado | 48 | Estudio abierto de sunitinib malato en sarcoma de tejido blando metastásico/irresecable en adultos (leiomiosarcoma, liposarcoma, fibrosarcoma y histiocitoma fibroso maligno). |
| [NCT00474994](https://clinicaltrials.gov/study/NCT00474994) | Fase 2 | Completado | 53 | Dosificación continua de sunitinib en sarcomas no-GIST, incluyendo liposarcoma, sin diseño específico para este subtipo. |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Fase 2 | Completado | 131 | Ensayo SARC024 de regorafenib (no sunitinib) en subtipos seleccionados de sarcoma; solo relevancia poblacional, evidencia indirecta. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21154746](https://pubmed.ncbi.nlm.nih.gov/21154746/) | 2011 | Ensayo Fase 2 | International Journal of Cancer | Estudio de fase II de sunitinib malato en sarcomas de tejido blando recidivantes/refractarios, centrado en leiomiosarcoma, liposarcoma e histiocitoma fibroso maligno. |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Protocolo de Ensayo | BMC Cancer | Protocolo del ensayo REGOSARC (regorafenib, no sunitinib) en sarcoma de tejido blando avanzado; menciona la angiogénesis como vía clave en la biología del sarcoma. |
| [38717131](https://pubmed.ncbi.nlm.nih.gov/38717131/) | 2024 | Cohorte/Serie de casos | American Journal of Surgical Pathology | Análisis clinicopatológico de 25 casos de sarcoma miofibroblástico inflamatorio mixoide, un subtipo distinto con alteraciones moleculares dirigibles. |
| [28423517](https://pubmed.ncbi.nlm.nih.gov/28423517/) | 2017 | Cohorte Molecular | Oncotarget | Secuenciación de nueva generación en condrosarcoma mixoide extraesquelético; evalúa factores predictivos de beneficio con sunitinib en un subconjunto de pacientes. |
| [23482782](https://pubmed.ncbi.nlm.nih.gov/23482782/) | 2013 | Reporte de Caso | Anticancer Research | Beneficio clínico prolongado con sunitinib malato en un caso de liposarcoma metastásico intensamente pretratado. |
| [38254762](https://pubmed.ncbi.nlm.nih.gov/38254762/) | 2024 | Revisión | Cancers | Revisión de alteraciones genéticas, epigenéticas y transcriptómicas en liposarcoma para la selección de terapia dirigida. |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Revisión | Magyar Onkológia | Tratamiento médico del sarcoma de tejido blando según el subtipo histológico. |
| [24555529](https://pubmed.ncbi.nlm.nih.gov/24555529/) | 2014 | Revisión | Expert Review of Anticancer Therapy | Terapias emergentes para el sarcoma de tejido blando en adultos. |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Revisión | Annals of Oncology | Tratamiento dirigido por histología en sarcoma de tejido blando; menciona trabectedina con actividad especialmente alta en liposarcoma mixoide. |

---

## Información de Mercado en España

Sunitinib no dispone actualmente de autorización de comercialización en España (0 registros). No es posible presentar una tabla de autorizaciones al no existir datos de licencias.

---

## Citotoxicidad

Sunitinib es un fármaco antineoplásico (inhibidor multidiana de tirosina quinasas utilizado en oncología), por lo que aplica esta sección.

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor multidiana de tirosina quinasas, TKI) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma completo, función hepática y renal, presión arterial (riesgo de hipertensión descrito en la literatura de multiquinasa, PMID 28230776) y función tiroidea (prevalencia de hipotiroidismo reportada en estudio no intervencionista, NCT00684645) |
| Protección en Manejo | Debe seguir las normativas estándar de manejo de fármacos citotóxicos/antineoplásicos orales |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Research Question (Pregunta de Investigación)**

**Justificación:**
- La evidencia para "Liposarcoma" es de nivel L2: existe un ensayo de fase II centrado específicamente en esta histología (junto a leiomiosarcoma y MFH) y un caso documentado de beneficio clínico prolongado, pero ningún ensayo fue diseñado exclusivamente para liposarcoma como subtipo único. El mecanismo (antiangiogénico/PDGFR) es biológicamente plausible pero no está confirmado para esta indicación específica.
- Las demás indicaciones predichas para sunitinib en este ciclo de evaluación fueron revisadas: **dermatofibrosarcoma protuberans** (L2, Proceed with Guardrails) tiene el respaldo mecanístico más directo (fusión COL1A1-PDGFB) y estudios prospectivos tras fallo de imatinib; **carcinoma de células renales no clasificado** (L2, Proceed with Guardrails) cuenta con múltiples cohortes y el ensayo Cabosun II; **carcinoma renal con fusión Xp11.2/TFE3** (L3) y **carcinoma renal infantil** (L3) tienen plausibilidad mecanística (vía MET) pero solo casos aislados, con datos pediátricos de seguridad muy limitados; **liposarcoma mixoide ovárico** (L3, Hold) es un subtipo extremadamente raro sin evidencia dedicada; **carcinoma de células renales asociado a neuroblastoma** (L4, Hold) presenta un posible error de vinculación de datos (el ensayo citado trata en realidad carcinoma de células claras ovárico); **angiolipoma** y **fibrosarcoma cardíaco** (ambos L5, Hold) carecen de todo respaldo clínico o bibliográfico. Por separado, **"renal carcinoma"** (rango 9, L1) coincide sustancialmente con la indicación ya aprobada de sunitinib (carcinoma de células renales avanzado) y no representa un verdadero reposicionamiento, sino una señal de calidad a considerar en la validación del modelo.

**Para avanzar se necesita:**
- Datos del prospecto de TFDA/EMA (advertencias y contraindicaciones) — actualmente es un vacío de datos bloqueante (DG001) que impide la evaluación de seguridad inicial (S1)
- Datos detallados del mecanismo de acción (MOA) verificados con fuente regulatoria (DrugBank) (DG002)
- Al menos un ensayo clínico diseñado específicamente para el subtipo liposarcoma (o su análisis en subgrupo) antes de reconsiderar el nivel de evidencia
- Evaluar en paralelo el candidato dermatofibrosarcoma protuberans, que presenta el mecanismo mejor definido dentro de este mismo Evidence Pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

