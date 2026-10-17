---
layout: default
title: Perindopril
parent: Solo predicción del modelo (L5)
nav_order: 627
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Perindopril: nueva indicación predicha, Enfermedad renal hipertensiva maligna (nivel de evidencia L5). Indicación original: Hipertensión arterial (trastorno hipertensivo)"
monitor_inn: "PERINDOPRIL"
predicted_indications: ["malignant hypertensive renal disease"]
---

# Perindopril
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Perindopril: De Hipertensión a Enfermedad Renal Hipertensiva Maligna

## Resumen en Una Frase

Perindopril es un inhibidor de la enzima convertidora de angiotensina (IECA), utilizado originalmente para el tratamiento de la hipertensión arterial.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna**,
pero actualmente no hay ensayos clínicos registrados y solo se dispone de **1 publicación** recuperada, que no aborda directamente esta indicación, por lo que la predicción se apoya únicamente en el modelo computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial (trastorno hipertensivo) |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna |
| Puntaje de Predicción TxGNN | 99.77% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 13 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, perindopril es un IECA, su eficacia en hipertensión está establecida, y mecanísticamente podría ser aplicable a la nefropatía hipertensiva maligna.

La inhibición de la ECA reduce la lesión vascular mediada por angiotensina II y la hipertensión glomerular, lo que es biológicamente plausible en la afectación renal de la hipertensión maligna. Sin embargo, se trata más bien de una extensión de la indicación antihipertensiva existente que de una señal de reposicionamiento realmente distinta.

Conviene tener cautela: el puntaje elevado de TxGNN (0,998) es solo una predicción computacional. La única publicación recuperada (PMID 36382821) trata sobre la función del riñón solitario tras nefrectomía por cáncer renal y no menciona perindopril ni la enfermedad renal hipertensiva maligna.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36382821](https://pubmed.ncbi.nlm.nih.gov/36382821/) | 2022 | Estudio clínico/observacional (sin clasificar con certeza) | Urologiia | Función del riñón solitario tras nefrectomía por cáncer renal; no aborda perindopril ni la nueva indicación predicha |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 68827 | PERINDOPRIL KRKA 4 mg COMPRIMIDOS EFG | Comprimido | No disponible en los datos |
| 72240 | PERINDOPRIL TECNIGEN 4 mg COMPRIMIDOS EFG | Comprimido | No disponible en los datos |
| 74661 | PERINDOPRIL MARIPER 2 MG COMPRIMIDOS | Comprimido | No disponible en los datos |
| 71941 | COVERSORAL 10 mg COMPRIMIDOS BUCODISPERSABLES | Comprimido bucodispersable | No disponible en los datos |
| 58636 | COVERSYL 4 mg COMPRIMIDOS | Comprimido | No disponible en los datos |

Se muestran 5 de las 13 autorizaciones vigentes (todas de monofármaco, ninguna cancelada).

## Consideraciones de Seguridad

- **Contraindicaciones / condiciones de riesgo (según relaciones del grafo de conocimiento, no texto del prospecto)**: enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, angioedema (incluido el hereditario, el adquirido y el inducido por bloqueadores del sistema renina-angiotensina-aldosterona), neutropenia, agranulocitosis, trastorno hipotensivo, enfermedad del tejido conectivo, enfermedades óseas y del cartílago, obstrucción de la arteria renal y piouréter.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones potenciales. Las de nivel **mayor** incluyen **citrato de potasio** y **bicarbonato de potasio** (riesgo de hiperpotasemia). Entre las de nivel moderado figuran corticoides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona), antidiabéticos (metformina, alogliptina, saxagliptina, canagliflozina, dapagliflozina, empagliflozina, clorpropamida), ácido acetilsalicílico, morfina, bupropión, dronabinol, ácido picosulfúrico y polietilenglicol con electrolitos.
- **Consideración específica de la nueva indicación**: en la hipertensión renovascular, los IECA conllevan riesgo de deterioro agudo de la función renal en estenosis bilateral de arteria renal o de riñón único, lo cual es especialmente relevante.
- Consultar el prospecto de la AEMPS para las advertencias y contraindicaciones oficiales, que no figuran en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5): no hay ensayos clínicos y la única publicación recuperada no es pertinente. Además, existen riesgos renales relevantes con los IECA en ciertos contextos de enfermedad renovascular.

**Para avanzar se necesita:**
- Obtener y analizar las advertencias y contraindicaciones del prospecto de la AEMPS (dato bloqueante para el cribado de seguridad).
- Completar los datos de mecanismo de acción desde DrugBank.
- Realizar una búsqueda bibliográfica dirigida sobre IECA en nefropatía hipertensiva maligna y registros de ensayos.
- Evaluar el riesgo renal en estenosis de arteria renal y la monitorización de potasio y función renal.

### Otras predicciones de menor prioridad (para referencia)

- **Hipertensión renovascular maligna** (99.77%, L5, Hold): plausible por dependencia del sistema renina-angiotensina, sin ensayos ni literatura.
- **Hipertensión pulmonar de mecanismo multifactorial incierto** (99.75%, L5, Hold): vínculo débil e inespecífico; los IECA no son terapia recomendada.
- **Hipertensión pulmonar por enfermedad pulmonar o hipoxia** (99.75%, L4, pregunta de investigación): solo datos preclínicos en ratas hipóxicas (PMID 11282121 y 10602319), sin ensayos en humanos.
- **Síndrome de Braddock** (99.66%, L5, Hold): sin fundamento mecanístico identificable.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

