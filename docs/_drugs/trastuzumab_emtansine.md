---
layout: default
title: Trastuzumab Emtansine
parent: Evidencia moderada (L3-L4)
nav_order: 817
evidence_level: L4
indication_count: 4
---

# Trastuzumab Emtansine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **4** 
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

# Trastuzumab emtansina: De Carcinoma de Mama HER2 Positivo a Cáncer de Mama con Receptor de Progesterona Positivo

## Resumen en Una Frase

Trastuzumab emtansina (T-DM1) es un conjugado anticuerpo-fármaco originalmente utilizado para el tratamiento del carcinoma de mama HER2 positivo.
El modelo TxGNN predice que podría ser efectivo para **cáncer de mama con receptor de progesterona positivo**, aunque esta predicción corresponde en gran medida a un subconjunto de la indicación original (tumores HER2 positivos que además expresan receptor de progesterona).
Actualmente no hay ensayos clínicos registrados para esta indicación específica y la evidencia disponible (**15 publicaciones**) consiste sobre todo en revisiones, guías y casos clínicos, de carácter indirecto.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Carcinoma de mama HER2 positivo (según las relaciones de indicación del grafo de conocimiento; los textos de indicación de las autorizaciones españolas están vacíos) |
| Nueva Indicación Predicha | Cáncer de mama con receptor de progesterona positivo |
| Puntaje de Predicción TxGNN | 99.82% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, T-DM1 combina el anticuerpo trastuzumab, que se une al receptor HER2, con el agente DM1 (emtansina), un inhibidor de microtúbulos que se libera en el interior de la célula tumoral tras la internalización del conjugado. Su eficacia en el cáncer de mama HER2 positivo está bien establecida.

La relación entre la indicación original y la nueva es muy estrecha: los tumores HER2 positivos con receptor de progesterona positivo (enfermedad HR+/HER2+) ya están cubiertos por la indicación aprobada de cáncer de mama HER2 positivo. Por tanto, se trata más bien de un subtipo por receptores que de una indicación verdaderamente nueva. La eficacia de T-DM1 depende del estado de HER2, no del estado del receptor de progesterona.

El puntaje elevado de TxGNN probablemente refleja la cercanía entre ambas enfermedades en la ontología, no una evidencia independiente de eficacia. Conviene interpretarlo con cautela.

### Otras predicciones del modelo (para contexto)

| Enfermedad predicha | Puntaje | Nivel | Comentario |
|------|------|------|------|
| Subtipo de carcinoma de mama tipo normal | 99.82% | L5 | Habitualmente HER2 bajo o negativo; sin justificación mecanística ni evidencia; solo predicción computacional |
| Cáncer de mama con receptor de progesterona negativo | 99.82% | L3 | Un ensayo de Fase 2 terminado y literatura de subtipo; no independiente de la indicación original |
| Tumor de mama luminal A o B | 99.81% | L4 | Solo los luminales B HER2 positivos se solapan con la indicación aprobada; los luminales A suelen ser HER2 negativos |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para la indicación principal (cáncer de mama con receptor de progesterona positivo).

A modo de referencia, para la indicación vecina de cáncer de mama con receptor de progesterona negativo se identificó un ensayo:

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04675827](https://clinicaltrials.gov/study/NCT04675827) | Fase 2 | Terminado | 139 | DECRESCENDO: desescalada de quimioterapia adyuvante en cáncer de mama precoz HER2 positivo, receptor de estrógeno negativo y ganglios negativos, tras respuesta patológica completa con quimioterapia neoadyuvante y bloqueo dual de HER2. No se confirma que T-DM1 sea el fármaco estudiado. |

---

## Evidencia de Literatura

Selección de las publicaciones más relevantes para la indicación principal (se priorizan guías, cohortes y revisiones sobre casos clínicos):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guía | J Clin Oncol | Actualización de la guía ASCO sobre tratamiento sistémico del cáncer de mama avanzado HER2 positivo |
| [28259011](https://pubmed.ncbi.nlm.nih.gov/28259011/) | 2017 | Guía | Eur J Cancer | Guías EGTM: los receptores de estrógeno y progesterona guían la terapia endocrina; el estado de HER2 es obligatorio para seleccionar terapias anti-HER2, incluido T-DM1 |
| [34215766](https://pubmed.ncbi.nlm.nih.gov/34215766/) | 2021 | Cohorte | Sci Rep | Relevancia pronóstica de la ganancia de positividad HER2 en cáncer de mama metastásico tratado con pertuzumab y/o T-DM1 (ensayo ChangeHER) |
| [33726508](https://pubmed.ncbi.nlm.nih.gov/33726508/) | 2021 | Revisión | Future Oncol | Tendencias en el tratamiento de HR+/HER2+; menciona neratinib y T-DM1 y combinaciones sin quimioterapia |
| [39631485](https://pubmed.ncbi.nlm.nih.gov/39631485/) | 2024 | Revisión | Pharmacol Res | Inhibidores dirigidos y citotóxicos en cáncer de mama; el manejo depende del estado de HER2, HR, ER y PR |
| [24892840](https://pubmed.ncbi.nlm.nih.gov/24892840/) | 2013 | Revisión | Clin Adv Hematol Oncol | Novedades en cáncer de mama metastásico según subtipos inmunohistoquímicos |
| [25873876](https://pubmed.ncbi.nlm.nih.gov/25873876/) | 2015 | Caso clínico | Case Rep Oncol | T-DM1 a dosis reducida, activo y seguro en disfunción hepática aguda |
| [33482449](https://pubmed.ncbi.nlm.nih.gov/33482449/) | 2021 | Caso clínico | Int J Surg Case Rep | Supervivencia favorable con tratamiento combinado en cáncer de mama metastásico en hemodiálisis |
| [35140078](https://pubmed.ncbi.nlm.nih.gov/35140078/) | 2022 | Caso clínico | BMJ Case Rep | Conversión de receptores y parálisis de cuerda vocal en una paciente con cáncer de mama |
| [35251981](https://pubmed.ncbi.nlm.nih.gov/35251981/) | 2022 | Caso clínico | Front Oncol | Pirotinib y vinorelbina metronómica en cáncer de mama HER2 positivo con enfermedad leptomeníngea |

Ninguna de estas publicaciones es un ensayo aleatorizado dirigido específicamente al subtipo con receptor de progesterona positivo.

---

## Información de Mercado en España

Las 6 autorizaciones son de comercialización vigente, del titular Roche Registration GmbH, en forma de polvo para concentrado para solución para perfusión. Los textos de indicación aprobada no figuran en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 113885001 | KADCYLA 100 mg | Polvo para concentrado para solución para perfusión | No disponible |
| 113885001IP | KADCYLA 100 mg | Polvo para concentrado para solución para perfusión | No disponible |
| 113885001IP1 | KADCYLA 100 mg | Polvo para concentrado para solución para perfusión | No disponible |
| 113885002 | KADCYLA 160 mg | Polvo para concentrado para solución para perfusión | No disponible |
| 113885002IP | KADCYLA 160 mg | Polvo para concentrado para solución para perfusión | No disponible |

(Existe una sexta autorización, 113885002IP1, de KADCYLA 160 mg, con las mismas características.)

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Conjugado anticuerpo-fármaco (terapia dirigida) con carga citotóxica inhibidora de microtúbulos (DM1) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto (no hay datos de toxicidad en los datos compilados) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto; en general, hemograma y función hepática. La literatura recoge un caso con dosis reducida en disfunción hepática aguda |
| Protección en Manejo | Consultar el prospecto; seguir las normas de manejo de fármacos citotóxicos de la institución |

---

## Consideraciones de Seguridad

**Interacciones Farmacológicas** (se identificaron 100 interacciones; se muestran las principales):

- **Gravedad mayor**: ácido acetilsalicílico, deferasirox, abciximab, apixabán, argatrobán, betrixabán, bivalirudina, cangrelor, caplacizumab, cilostazol. Predominan antitrombóticos, anticoagulantes y antiagregantes, lo que sugiere un mayor riesgo hemorrágico que requiere vigilancia.
- **Gravedad moderada**: claritromicina, dexfenfluramina, fenfluramina, metronidazol, naltrexona, rosuvastatina, sibutramina, simvastatina, tinidazol, cobicistat.

Para advertencias y contraindicaciones, consultar el prospecto, ya que no están disponibles en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación predicha es esencialmente un subconjunto de receptores de la indicación ya aprobada (HER2 positivo), y su eficacia depende de HER2 y no del receptor de progesterona. No hay ensayos dedicados y la evidencia es indirecta (nivel L4), por lo que no aporta un caso de reposicionamiento independiente. Además, faltan los datos de seguridad de la ficha técnica.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), actualmente un vacío bloqueante para el cribado de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Aclarar si la indicación aprobada ya cubre explícitamente los tumores HR+/HER2+, lo que anularía el carácter de "nueva indicación"
- Definir si tiene sentido evaluar subtipos con HER2 bajo o negativo (por ejemplo, luminal A o tipo normal), donde no existe justificación mecanística actual
- Revisar con detalle los datos de subtipos HR+/HER2+ en ensayos pivotales de T-DM1
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

