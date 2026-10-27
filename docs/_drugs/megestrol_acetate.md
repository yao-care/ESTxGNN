---
layout: default
title: Megestrol Acetate
parent: Evidencia alta (L1-L2)
nav_order: 501
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-14
description: "Megestrol Acetate: nueva indicación predicha, Carcinoma endometrial de cuerpo uterino (nivel de evidencia L2). Indicación original: Carcinoma de endometrio (según el grafo de conocimiento"
monitor_inn: "Megestrol acetate"
predicted_indications: ["hereditary breast ovarian cancer syndrome", "borderline epithelial tumor of ovary", "uterine carcinosarcoma", "placenta cancer", "ovarian clear cell adenocarcinoma", "ovarian cancer", "malignant dysgerminomatous germ cell tumor of ovary"]
---

# Megestrol Acetate
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **10** 
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

## Acetato de megestrol: De Carcinoma de Endometrio a Carcinoma Endometrial de Cuerpo Uterino
{: .text-alpha }

## Resumen en Una Frase

El acetato de megestrol es un progestágeno sintético, originalmente utilizado en el tratamiento del carcinoma de endometrio.
El modelo TxGNN predice que podría ser efectivo para **carcinoma endometrial de cuerpo uterino**, con **1 ensayo clínico** y **ninguna publicación** que respaldan directamente esta predicción.
Esta nueva indicación coincide en la práctica con la indicación original, por lo que no constituye un reposicionamiento propiamente dicho.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Carcinoma de endometrio (según el grafo de conocimiento; el texto de indicación de las autorizaciones españolas no está disponible) |
| Nueva Indicación Predicha | Carcinoma endometrial de cuerpo uterino |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, el acetato de megestrol es un progestágeno que actúa a través de los receptores de progesterona y glucocorticoides. La terapia con progestágenos es un tratamiento hormonal establecido para el cáncer de endometrio con receptores hormonales positivos.

La nueva indicación predicha es esencialmente la indicación original, de modo que la alta puntuación del modelo es coherente con el uso clínico conocido. Esto respalda la validez de la predicción, pero no aporta un beneficio de reposicionamiento más allá de la indicación existente.

Otras predicciones del modelo, con menor respaldo, incluyen el cáncer de ovario (evidencia L2: un estudio de fase 2 con megestrol a dosis altas en cáncer epitelial de ovario refractario a platino, PMID 11593052, y revisiones sobre terapia hormonal) y el carcinosarcoma uterino (L4, solo evidencia indirecta). El resto de predicciones se basan únicamente en el modelo (L5) y quedan en espera (Hold).

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00729586](https://clinicaltrials.gov/study/NCT00729586) | Fase 2 | Completado | 73 | Ensayo aleatorizado de temsirolimus solo o combinado con terapia hormonal (megestrol y tamoxifeno) en carcinoma de endometrio avanzado, persistente o recurrente. El papel exacto del brazo con megestrol debe verificarse |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 4376IP | MAYGACE ALTAS DOSIS 40 MG/ML | Suspensión oral | No disponible |
| 58775 | BOREA 160 mg | Comprimido | No disponible |
| 62012 | MEGEFREN SOBRES | Granulado | No disponible |
| 60783 | MAYGACE ALTAS DOSIS 40 mg/ml | Suspensión oral | No disponible |
| 58773 | MEGEFREN 160 mg | Comprimido | No disponible |

Hay una sexta autorización vigente (62011, BOREA 160 mg granulado para suspensión oral en sobres). Todas son monofármaco y están vigentes.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia hormonal (progestágeno); no es un citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto; por las contraindicaciones del grafo de conocimiento, conviene vigilar glucemia, presión arterial y función hepática y renal. También se ha descrito supresión suprarrenal secundaria (PMID 10491532) |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no texto del prospecto)**: trastorno hipertensivo e hipertensión, enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, hiperglucemia, diabetes mellitus, cetoacidosis diabética, insuficiencia suprarrenal y enfermedad de Addison, hipogonadismo masculino, eunucoidismo, menopausia prematura y síndrome de insensibilidad a los andrógenos.
- **Interacciones farmacológicas**: se identificaron 100 interacciones, las mostradas son de nivel moderado. Destacan los antidiabéticos (acarbosa, metformina, pioglitazona, glimepirida, repaglinida, sitagliptina, saxagliptina, linagliptina, alogliptina, canagliflozina, dapagliflozina, empagliflozina, clorpropamida), los agonistas del receptor de GLP-1 (albiglutida, dulaglutida, semaglutida), las insulinas (aspart, degludec), el aprepitant y la claritromicina. El patrón sugiere un posible efecto sobre el control glucémico.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La indicación predicha coincide con la indicación original, y existe un ensayo de fase 2 completado en carcinoma de endometrio avanzado o recurrente. Sin embargo, no aporta valor de reposicionamiento nuevo, y la información de seguridad oficial y del mecanismo no está disponible.

**Para avanzar se necesita:**
- Obtener los datos de advertencias y contraindicaciones del prospecto de la AEMPS (carencia bloqueante para el cribado de seguridad).
- Completar los datos del mecanismo de acción desde DrugBank.
- Confirmar el diseño del brazo con megestrol en NCT00729586.
- Si se busca un reposicionamiento real, priorizar el cáncer de ovario (revisar PMID 11593052 y verificar la aplicabilidad de NCT00005975) y el carcinosarcoma uterino.
- Definir un plan de monitoreo para pacientes con diabetes, hipertensión o enfermedad hepática o renal.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

