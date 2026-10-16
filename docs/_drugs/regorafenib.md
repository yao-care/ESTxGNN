---
layout: default
title: Regorafenib
parent: Solo predicción del modelo (L5)
nav_order: 689
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Regorafenib: nueva indicación predicha, Liposarcoma (nivel de evidencia L5). Indicación original: Cáncer colorrectal metastásico…"
monitor_inn: "REGORAFENIB"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "clear cell renal carcinoma", "renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions", "renal cell carcinoma associated with neuroblastoma", "unclassified renal cell carcinoma", "childhood kidney cell carcinoma", "vulva sarcoma"]
---

# Regorafenib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

# Regorafenib: De Cáncer Colorrectal Metastásico y Carcinoma Hepatocelular a Liposarcoma

## Resumen en Una Frase

Regorafenib es un inhibidor oral de múltiples quinasas, utilizado originalmente para el cáncer colorrectal metastásico, el carcinoma hepatocelular y los tumores del estroma gastrointestinal (GIST).
El modelo TxGNN predice que podría ser efectivo para **liposarcoma**, con **1 ensayo clínico** y **9 publicaciones** que respaldan esta dirección. Sin embargo, los resultados clínicos específicos en liposarcoma son desfavorables (ver más abajo).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer colorrectal metastásico, carcinoma hepatocelular y tumor del estroma gastrointestinal (GIST) (según el grafo de conocimiento; el texto de indicación de la autorización española no está disponible) |
| Nueva Indicación Predicha | Liposarcoma |
| Puntaje de Predicción TxGNN | 99.76% |
| Nivel de Evidencia | L1 (con salvedades, ver más abajo) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Regorafenib es un inhibidor multiquinasa que actúa sobre VEGFR1-3, TIE2, PDGFR, FGFR, KIT, RET y RAF. Estas vías impulsan la angiogénesis y la señalización tumor-estroma, y son relevantes en los sarcomas de tejidos blandos, incluido el liposarcoma. Los datos de mecanismo de acción de DrugBank no estaban disponibles en los datos compilados para este informe; esta descripción procede de la literatura revisada.

Regorafenib ya está establecido en tumores sólidos de origen gastrointestinal (colorrectal, GIST, hepatocelular). Los sarcomas de tejidos blandos comparten dependencia de angiogénesis y de quinasas como KIT y PDGFR, lo que justifica la extrapolación mecanística.

**Advertencia importante:** los ensayos aleatorizados controlados con placebo (REGOSARC y SARC024) mostraron actividad en sarcomas no adipocíticos (leiomiosarcoma, sarcoma sinovial), **pero no en liposarcoma**. La cohorte de liposarcoma de SARC024 concluyó que los resultados "no apoyan el uso rutinario de regorafenib" en esta población. Por tanto, el puntaje alto del modelo no se corresponde con evidencia clínica favorable.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Fase 2 | Completado | 131 | SARC024: protocolo general de regorafenib oral en subtipos seleccionados de sarcoma, con una cohorte de liposarcoma |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32701199](https://pubmed.ncbi.nlm.nih.gov/32701199/) | 2020 | ECA | The Oncologist | Cohorte de liposarcoma de SARC024 (fase II, doble ciego, placebo): no respalda el uso rutinario de regorafenib |
| [27751846](https://pubmed.ncbi.nlm.nih.gov/27751846/) | 2016 | ECA | Lancet Oncol | REGOSARC (fase 2): eficacia y seguridad de regorafenib en sarcoma de tejidos blandos previamente tratado con antraciclinas |
| [29902612](https://pubmed.ncbi.nlm.nih.gov/29902612/) | 2018 | ECA (análisis actualizado) | Eur J Cancer | Actividad frente a placebo y tras el cruce en sarcoma no adipocítico; sin eficacia en liposarcoma |
| [28295221](https://pubmed.ncbi.nlm.nih.gov/28295221/) | 2017 | Análisis post hoc de ECA | Cancer | Análisis Q-TWiST de REGOSARC: beneficio clínico integrado en sarcoma no adipocítico |
| [29931504](https://pubmed.ncbi.nlm.nih.gov/29931504/) | 2018 | Revisión | Targeted Oncology | Papel creciente de regorafenib en pacientes con sarcoma |
| [40975452](https://pubmed.ncbi.nlm.nih.gov/40975452/) | 2025 | Revisión | Crit Rev Oncol Hematol | Tratamiento de mantenimiento tras la primera línea en sarcoma de tejidos blandos avanzado |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Protocolo de estudio | BMC Cancer | Protocolo del ensayo REGOSARC |
| [33290314](https://pubmed.ncbi.nlm.nih.gov/33290314/) | 2021 | Estudio retrospectivo (otro fármaco: anlotinib) | Anti-Cancer Drugs | Anlotinib en liposarcoma bien/desdiferenciado; evidencia indirecta |
| [26266019](https://pubmed.ncbi.nlm.nih.gov/26266019/) | 2015 | Reporte de caso (otro fármaco: pazopanib) | Rare Tumors | Respuesta a pazopanib en sarcoma de Ewing extraóseo; evidencia indirecta |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 113858002 | STIVARGA 40 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | No disponible en los datos compilados |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor multiquinasa) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto; la literatura revisada señala toxicidad hepática, proteinuria, hipertensión y reacción cutánea mano-pie como eventos relevantes de esta clase (hemograma, función hepática y renal, presión arterial) |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones. Las más relevantes de las mostradas:
  - **Graves (Major)**: ácido acetilsalicílico, deferasirox, ibritumomab tiuxetán, tositumomab (incluido I-131), abciximab, alteplasa, antitrombina III humana y apixabán (principalmente por riesgo hemorrágico y anticoagulación).
  - **Moderadas**: dexametasona, claritromicina, naltrexona, dexfenfluramina, fenfluramina, rosuvastatina, sibutramina, cobicistat.
  - **Leves**: dapagliflozina, naloxegol, prucaloprida.

Las advertencias y contraindicaciones del prospecto no estaban disponibles en los datos compilados; consultar el prospecto de la AEMPS para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ECA de fase 2 completado y varios ECA publicados, pero demuestran actividad en sarcomas no adipocíticos y **no en liposarcoma**; la cohorte específica no respalda el uso rutinario. El nivel L1 refleja la existencia de ensayos controlados, no un resultado positivo para esta indicación. Cualquier avance debería ser cauteloso, y una decisión "Hold" sería igualmente defendible desde el punto de vista clínico.

**Para avanzar se necesita:**
- Revisar el prospecto de la AEMPS (advertencias, contraindicaciones, texto de indicaciones aprobadas), que es un vacío bloqueante para el cribado de seguridad.
- Obtener datos de mecanismo de acción de DrugBank.
- Analizar por subtipos histológicos de liposarcoma (bien diferenciado, desdiferenciado, mixoide, pleomórfico) para identificar subgrupos con posible respuesta.
- Evaluar estrategias de combinación, dado que los autores de SARC024 señalan que la monoterapia no es suficiente.
- Plan de manejo de interacciones, en especial con anticoagulantes y antiagregantes, y de monitoreo hepático, de presión arterial y proteinuria.

---

*Nota sobre otras indicaciones predichas:* el carcinoma renal de células claras (puntaje 99.47%, nivel L3) cuenta con un ensayo de fase 2 de un solo brazo y un ensayo de combinación de fase 1/2 (NCT03475953), pero sin evidencia de fase 3, y se considera una pregunta de investigación. Las demás predicciones (liposarcoma mixoide ovárico, subtipos raros de carcinoma renal, carcinoma renal infantil y sarcoma de vulva) carecen de ensayos y literatura específicos (nivel L5, decisión Hold).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

