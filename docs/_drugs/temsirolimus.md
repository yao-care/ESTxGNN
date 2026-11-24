---
layout: default
title: Temsirolimus
parent: Solo predicción del modelo (L5)
nav_order: 773
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
monitor_inn: "TEMSIROLIMUS"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "vulva sarcoma"]
description: "Temsirolimus: nueva indicación predicha, Liposarcoma (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 2 (comercializadas: 1)"
---

# Temsirolimus
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Temsirolimus: Liposarcoma
{: .text-alpha }

## Resumen en Una Frase

Temsirolimus es un inhibidor de mTOR administrado por perfusión intravenosa, utilizado originalmente para el tratamiento del carcinoma de células renales y del linfoma de células del manto.
El modelo TxGNN predice que podría ser efectivo para **liposarcoma**, con **2 ensayos clínicos** (uno de ellos directamente relevante) y **1 publicación** de tipo revisión que actualmente respaldan esta dirección de forma limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Liposarcoma |
| Puntaje de Predicción TxGNN | 0.9954 |
| Nivel de Evidencia | L5 (ver nota abajo) |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 2; revocadas o suspendidas: 1) |
| Número de Autorizaciones | 2 (comercializadas: 1) |
| Decisión Recomendada | Hold |

> **Nota sobre el nivel de evidencia:** los datos compilados asignan L2 a esta indicación, pero según los criterios del informe L2 requiere un ensayo de Fase 2/3 completado en la indicación. El único ensayo directamente relevante es de Fase 1/2 en sarcomas avanzados en general, sin resultados específicos para liposarcoma. Por prudencia, se considera que la evidencia real se sitúa entre L4 y L5. Se indica L5 como valor conservador.

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Temsirolimus (traducción no oficial): «El temsirolimús es un inhibidor de mTOR (diana de la rapamicina en mamíferos). El temsirolimús se une a una proteína intracelular (FKBP-12), y el complejo proteína-fármaco inhibe la actividad de mTOR, que controla la división celular. La inhibición de la actividad de mTOR dio lugar a una detención del crecimiento en la fase G1 en las células tumorales tratadas.» Texto original en inglés: "Temsirolimus is an inhibitor of mTOR (mammalian target of rapamycin). Temsirolimus binds to an intracellular protein (FKBP-12), and the protein-drug complex inhibits the activity of mTOR that controls cell division. Inhibition of mTOR activity resulted in a G1 growth arrest in treated tumor cells." ([DailyMed: temsirolimus prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1c207bed-10e3-46f0-ad2c-69d5e5c97736), versión del 2020-03-30; consultado el 2026-11-19). Según el conocimiento farmacológico general, temsirolimus es un inhibidor de mTOR (diana de la rapamicina en mamíferos), una quinasa central en la regulación del crecimiento y la proliferación celular. Su eficacia en el carcinoma de células renales y en el linfoma de células del manto está establecida.

La vía PI3K/AKT/mTOR se activa con frecuencia en los sarcomas de partes blandas, incluido el liposarcoma. Los liposarcomas bien diferenciados y desdiferenciados presentan amplificación de MDM2/CDK4 con señalización descendente de PI3K/AKT, lo que ofrece una justificación plausible para inhibir mTOR.

Aunque el carcinoma renal y el liposarcoma son tumores de origen muy distinto, comparten la dependencia de esta vía de señalización. El puntaje TxGNN es muy alto (0.9954), pero una predicción del modelo no constituye evidencia clínica por sí sola.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Fase 1/2 | Completado | 24 | Temsirolimus (Torisel) con doxorrubicina liposomal en sarcomas de partes blandas y hueso avanzados; busca una dosis segura y evalúa eficacia en sarcoma recurrente. Probablemente incluye pacientes con liposarcoma, pero no hay datos específicos por subtipo. |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Fase 2 | Completado | 46 | Cixutumumab con temsirolimus en tumores sólidos pediátricos recurrentes o refractarios (sarcoma). Relevancia indirecta: población pediátrica con histologías distintas y combinación con anticuerpo anti-IGF-1R que dificulta atribuir el efecto a temsirolimus. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Revisión | Bulletin du Cancer | Revisión de tratamientos dirigidos en tumores raros del tejido conectivo y sarcomas, organizados en seis subgrupos según alteraciones moleculares específicas. |

---

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 07424001 | TORISEL 30 MG CONCENTRADO Y DISOLVENTE PARA SOLUCION PARA PERFUSION | CONCENTRADO Y DISOLVENTE PARA SOLUCIÓN PARA PERFUSIÓN | Pfizer Europe Ma Eeig | Comercializada |
| 86058 | TEMSIROLIMUS ACCORD 30 MG CONCENTRADO Y DISOLVENTE PARA SOLUCION PARA PERFUSION EFG | CONCENTRADO Y DISOLVENTE PARA SOLUCIÓN PARA PERFUSIÓN | Accord Healthcare S.L.U. | Revocada |

Se muestran las 2 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de mTOR) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma, función hepática y renal, glucosa y lípidos en sangre (según las contraindicaciones del grafo de conocimiento y el perfil conocido de la clase) |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Contraindicaciones o precauciones señaladas por el grafo de conocimiento** (no proceden del texto del prospecto): enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, hiperglucemia, diabetes mellitus, cetoacidosis diabética, hiperlipidemia (incluida la familiar), trastornos cerebrovasculares (ictus, infarto cerebral), hiperbilirrubinemia (incluido el síndrome de Gilbert), enfermedad pulmonar intersticial y diversos tumores cerebrales (astrocitomas, glioblastoma de células gigantes, tumores oligodendrogliales, entre otros).
- **Interacciones farmacológicas**: se identificaron 100 interacciones; entre las mostradas, las de nivel **mayor** son:
  - Anfotericina B (y su complejo lipídico)
  - Dexametasona
  - Claritromicina

  Entre las de nivel moderado figuran antidiabéticos (acarbosa, metformina, pioglitazona, alogliptina, albiglutida, canagliflozina, clorpropamida, dapagliflozina), corticoides (hidrocortisona, triamcinolona, betametasona, budesonida), aprepitant, mesalazina, balsalazida y cimetidina.

Consultar el prospecto para el resto de la información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es de alto puntaje, pero la evidencia clínica específica en liposarcoma es muy limitada: un ensayo de Fase 1/2 en sarcomas en general, sin datos por subtipo, y una única revisión narrativa. Además, la información de seguridad del prospecto no está disponible, lo que impide avanzar en el cribado de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar los resultados publicados de NCT00949325 para identificar la respuesta en pacientes con liposarcoma.
- Revisar los datos de seguridad (advertencias y contraindicaciones) del prospecto de la AEMPS.
- Confirmar los datos del mecanismo de acción en DrugBank.
- Evaluar las contraindicaciones del grafo de conocimiento (función renal y hepática, metabolismo de glucosa y lípidos, enfermedad pulmonar intersticial) y las interacciones mayores en la población objetivo.
- Revisar la literatura preclínica y clínica de inhibidores de mTOR en liposarcoma bien diferenciado y desdiferenciado.
- Considerar un estudio de Fase 2 específico en liposarcoma si los datos anteriores resultan favorables.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: temsirolimus prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1c207bed-10e3-46f0-ad2c-69d5e5c97736) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

