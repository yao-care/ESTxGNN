---
layout: default
title: Everolimus
parent: Evidencia alta (L1-L2)
nav_order: 321
evidence_level: L2
indication_count: 8
last_modified_at: 2026-10-31
monitor_inn: "EVEROLIMUS"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "dermatofibrosarcoma protuberans", "parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "embryonal extrahepatic bile duct rhabdomyosarcoma", "rhabdomyosarcoma (disease)", "prostate embryonal rhabdomyosarcoma"]
description: "Everolimus: nueva indicación predicha, Liposarcoma (nivel de evidencia L2). Indicación original: No consta en los datos locales"
---

# Everolimus
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **8** 
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

## Everolimus: Liposarcoma
{: .text-alpha }

## Resumen en Una Frase

Everolimus es un inhibidor de mTOR utilizado originalmente en el tratamiento del carcinoma de células renales, el cáncer de mama y el angiomiolipoma renal asociado a esclerosis tuberosa.
El modelo TxGNN predice que podría ser efectivo para **liposarcoma**, con **1 ensayo clínico** y **4 publicaciones** que actualmente respaldan esta dirección, aunque de forma indirecta (combinación con ribociclib y estudios preclínicos).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Liposarcoma |
| Puntaje de Predicción TxGNN | 0.9988 |
| Nivel de Evidencia | L2 (un ensayo de Fase 2 en curso, en combinación; sin resultados maduros) |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 12) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, everolimus inhibe mTORC1, una proteína situada por debajo de la vía PI3K/AKT que regula la proliferación y la supervivencia celular. Su eficacia en el carcinoma de células renales y en otros tumores está establecida.

En el liposarcoma desdiferenciado, que se caracteriza por la amplificación de CDK4/MDM2, se plantea la hipótesis de que combinar un inhibidor de CDK4/6 (ribociclib) con la inhibición de mTOR bloquearía vías proliferativas y de supervivencia paralelas. Existe por tanto una lógica biológica, aunque indirecta.

Conviene ser prudente: el puntaje del modelo es muy alto, pero el respaldo clínico se limita a un ensayo de Fase 2 de combinación, de un solo brazo por cohorte, sin resultados de eficacia maduros en los datos disponibles. No es posible aislar la contribución individual de everolimus.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Fase 2 | Activo, sin reclutamiento | 48 | Ribociclib + everolimus en liposarcoma desdiferenciado y leiomiosarcoma avanzados tras al menos una terapia sistémica previa; finalización prevista en diciembre de 2026 |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Informe de ensayo clínico (Fase 2) | Clin Cancer Res | Ribociclib + everolimus en liposarcoma desdiferenciado y leiomiosarcoma; sinergia previa en modelos tumorales |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Revisión (preclínico) | Front Oncol | Modelos PDOX de sarcoma que identifican combinaciones con palbociclib; no específico de everolimus |
| [41991999](https://pubmed.ncbi.nlm.nih.gov/41991999/) | 2026 | Preclínico | Oncogene | El inhibidor de XPO1 KPT-330 afecta la viabilidad del liposarcoma desdiferenciado; no específico de everolimus |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclínico | Anticancer Res | Actividad antitumoral de eribulina en combinación; no específico de everolimus |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 11710002 | VOTUBIA 2,5 MG COMPRIMIDOS | Comprimido | No disponible |
| 83446 | EVEROLIMUS ACCORD 5 MG COMPRIMIDOS EFG | Comprimido | No disponible |
| 83478 | EVEROLIMUS ETHYPHARM 2,5 MG COMPRIMIDOS EFG | Comprimido | No disponible |
| 86608 | EVEROLIMUS BIOCON 10 MG COMPRIMIDOS EFG | Comprimido | No disponible |
| 66007 | CERTICAN 0,75 MG COMPRIMIDOS | Comprimido | No disponible |

Se listan 5 de las 20 autorizaciones vigentes (todas de principio activo único). También existe una presentación de comprimido dispersable (VOTUBIA 5 mg).

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de mTOR) |
| Riesgo de Mielosupresión | Medio; las contraindicaciones del grafo de conocimiento incluyen neutropenia, trombocitopenia, leucopenia y anemia |
| Clasificación de Emetogenicidad | Baja (según la categoría del fármaco; consultar el prospecto) |
| Items de Monitoreo | Hemograma completo, función hepática y renal, glucosa y perfil lipídico |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo (grafo de conocimiento, no texto del prospecto)**:
  - Hepáticas y renales: insuficiencia hepática, enfermedad hepática, enfermedad renal, síndrome hemolítico-urémico.
  - Hematológicas: trombocitopenia, neutropenia, leucopenia, agranulocitosis, anemia, púrpura trombocitopénica.
  - Metabólicas: hiperglucemia, diabetes mellitus, cetoacidosis diabética, hipertrigliceridemia, hiperlipidemia.
  - Cardiopulmonares: insuficiencia cardíaca congestiva, enfermedad pulmonar intersticial, derrame pericárdico.
  - Otras: estomatitis y linfomas.
- **Interacciones Farmacológicas** (100 registradas; ejemplos):
  - Mayores: anfotericina B (incluida la formulación en complejo lipídico), aprepitant, dexametasona y claritromicina.
  - Moderadas: antidiabéticos (metformina, acarbosa, alogliptina, canagliflozina, dapagliflozina, empagliflozina, linagliptina, glimepiride, clorpropamida, albiglutida, dulaglutida), cimetidina, eliglustat y eluxadolina.
  - Menor: sulfato de zinc.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque el puntaje TxGNN es muy alto (0,9988), la única evidencia clínica es un ensayo de Fase 2 de combinación aún en curso y sin resultados de eficacia maduros, por lo que no se puede atribuir beneficio a everolimus por sí solo. Debe considerarse una pregunta de investigación más que una opción lista para avanzar.

**Para avanzar se necesita:**
- Resultados de eficacia maduros del ensayo NCT03114527 (finalización prevista a finales de 2026), con análisis específico del brazo de liposarcoma desdiferenciado.
- Datos detallados del mecanismo de acción y del prospecto (advertencias y contraindicaciones) en España.
- Datos que permitan aislar la contribución de everolimus frente a ribociclib.
- Plan de monitoreo de seguridad hematológica, metabólica y de interacciones, dada la complejidad del perfil de interacciones.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

