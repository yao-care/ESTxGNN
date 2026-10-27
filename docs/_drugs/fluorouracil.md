---
layout: default
title: Fluorouracil
parent: Solo predicción del modelo (L5)
nav_order: 345
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Fluorouracil: nueva indicación predicha, Rabdomiosarcoma embrionario botrioide de vagina (nivel de evidencia L5). Indicación original: Carcinoma basocelular superficial multifocal (según el grafo de …"
monitor_inn: "fluorouracil"
predicted_indications: ["botryoid-type embryonal rhabdomyosarcoma of the vagina", "rhabdomyosarcoma (disease)", "parameningeal embryonal rhabdomyosarcoma", "embryonal extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "liver sarcoma", "sickle cell-beta-thalassemia disease syndrome", "hereditary persistence of fetal hemoglobin-sickle cell disease syndrome", "sickle cell-hemoglobin E disease syndrome"]
---

# Fluorouracil
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

## Fluorouracilo: De Carcinoma Basocelular Superficial Multifocal a Rabdomiosarcoma Embrionario Botrioide de Vagina
{: .text-alpha }

## Resumen en Una Frase

Fluorouracilo es un antimetabolito citotóxico utilizado originalmente para el tratamiento de tumores cutáneos y premalignos de la piel (carcinoma basocelular superficial, queratosis actínica) y de tumores digestivos (cáncer gástrico, adenocarcinoma de páncreas, metástasis de cáncer de colon).
El modelo TxGNN predice que podría ser efectivo para **rabdomiosarcoma embrionario botrioide de vagina**,
pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Carcinoma basocelular superficial multifocal (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Rabdomiosarcoma embrionario botrioide de vagina |
| Puntaje de Predicción TxGNN | 99.75% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento farmacológico general, fluorouracilo es un antimetabolito que inhibe la timidilato sintasa e interfiere con la síntesis de ADN y ARN en células de proliferación rápida. Su eficacia está establecida en tumores epiteliales (cutáneos y digestivos), y mecanísticamente podría actuar sobre otras células tumorales en proliferación.

La relación con la nueva indicación es débil. El rabdomiosarcoma es un sarcoma de tejidos blandos, biológicamente distinto de los carcinomas para los que se usa fluorouracilo. El tratamiento estándar se basa en vincristina, actinomicina D y ciclofosfamida (VAC) o regímenes relacionados, no en fluorouracilo. El único respaldo es la puntuación del modelo, probablemente heredada del nodo padre "rabdomiosarcoma".

Otras indicaciones predichas (rabdomiosarcoma general, subtipos parameníngeo, de vía biliar extrahepática y prostático, sarcoma hepático y síndromes de células falciformes) muestran puntuaciones similares (0.996–0.998). Tampoco cuentan con ensayos clínicos y presentan evidencia indirecta o ausente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para el rabdomiosarcoma embrionario botrioide de vagina. Para la indicación general de rabdomiosarcoma (segunda predicción) solo existe evidencia indirecta:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [3884137](https://pubmed.ncbi.nlm.nih.gov/3884137/) | 1985 | Revisión | Cancer | Valor de la quimioterapia adyuvante en sarcomas infantiles; no aporta datos específicos de fluorouracilo |
| [6277228](https://pubmed.ncbi.nlm.nih.gov/6277228/) | 1981 | Revisión | Ann Acad Med Singapore | Curabilidad de cánceres avanzados con quimioterapia, incluido el rabdomiosarcoma infantil |
| [3951398](https://pubmed.ncbi.nlm.nih.gov/3951398/) | 1986 | Cohorte | Med Pediatr Oncol | Carcinoma indiferenciado de nasofaringe en niños; indirecto |
| [42483493](https://pubmed.ncbi.nlm.nih.gov/42483493/) | 2026 | Reporte de caso | Case Rep Oncol Med | Rabdomiosarcoma lingual en adulto joven; cisplatino + 5-FU provocó progresión de la enfermedad, y la respuesta llegó con vincristina, actinomicina D y ciclofosfamida |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 71868 | Fluorouracilo Accord 50 mg/ml solución inyectable o para perfusión EFG | Solución inyectable y para perfusión | No disponible |
| 84849 | Tolak 40 mg/g crema | Crema | No disponible |
| 77675 | Actikerall 5 mg/g + 100 mg/g solución cutánea | Solución cutánea | No disponible |
| 86061 | Verrucutan 5 mg/g + 100 mg/g solución cutánea | Solución cutánea | No disponible |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antimetabolito, clase fluoropirimidina) |
| Riesgo de Mielosupresión | Medio a alto por vía sistémica (el grafo de conocimiento asocia contraindicaciones con trombocitopenia, neutropenia, agranulocitosis y leucopenia) |
| Clasificación de Emetogenicidad | Baja a moderada por vía intravenosa |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal, electrolitos; considerar la determinación de la deficiencia de DPD antes del tratamiento |
| Protección en Manejo | La presentación inyectable debe manejarse según las normas para medicamentos citotóxicos |

## Consideraciones de Seguridad

- **Contraindicaciones / condiciones de riesgo (según el grafo de conocimiento, no el texto del prospecto)**: enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, neutropenia, agranulocitosis, leucopenia, enfermedad diarreica, úlcera péptica activa, faringitis, estomatitis, piuria y déficit de dihidropirimidina deshidrogenasa (DPD).
- **Interacciones farmacológicas**: se identificaron 361 interacciones. Las de nivel moderado incluyen **metronidazol** y **tinidazol**. Las de nivel menor incluyen **cimetidina** y **levofloxacino**. Varias más (por ejemplo omeprazol, pantoprazol, metformina, morfina) tienen nivel no clasificado.

Para las advertencias formales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en la puntuación del modelo (nivel L5), sin ensayos clínicos ni literatura específica. El tratamiento estándar del rabdomiosarcoma no incluye fluorouracilo, y un caso publicado describe progresión con cisplatino + 5-FU.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank
- Advertencias y contraindicaciones del prospecto de AEMPS, y textos de indicación aprobada de las autorizaciones
- Revisión sistemática de la literatura sobre fluorouracilo en rabdomiosarcoma, incluida la actividad preclínica
- Evaluación de compatibilidad de vías de administración y comparación con los regímenes estándar (VAC)
- Si se desea explorar alternativas, priorizar el rabdomiosarcoma general (nivel L4), que cuenta al menos con evidencia indirecta
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

