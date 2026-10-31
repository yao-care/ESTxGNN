---
layout: default
title: Duloxetine
parent: Solo predicción del modelo (L5)
nav_order: 270
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
monitor_inn: "Duloxetine"
predicted_indications: ["benign paroxysmal torticollis of infancy", "agoraphobia", "obsessive-compulsive disorder", "histrionic personality disorder (disease)", "paranoid personality disorder", "schizoid personality disorder", "schizotypal personality disorder", "Ohdo syndrome and variants", "ligneous conjunctivitis", "blepharophimosis - intellectual disability syndrome, Ohdo type"]
description: "Duloxetine: nueva indicación predicha, Benign paroxysmal torticollis of infancy (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Duloxetine
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

## Duloxetine: Benign paroxysmal torticollis of infancy
{: .text-alpha }

## Resumen en Una Frase

Duloxetina es un inhibidor de la recaptación de serotonina y noradrenalina (IRSN), utilizado originalmente para el tratamiento del trastorno depresivo mayor, los trastornos de ansiedad y la fibromialgia.
El modelo TxGNN predice que podría ser efectivo para el **Trastorno Obsesivo-Compulsivo (TOC)**, con **3 ensayos clínicos** (solo 1 directamente relevante) y **20 publicaciones** que actualmente respaldan esta dirección.

*Nota:* la predicción con mayor puntaje TxGNN (rank 1) es "tortícolis paroxística benigna de la infancia", pero carece de toda evidencia (L5). Este informe se centra en la predicción con mayor respaldo disponible: el TOC (rank 3). Se menciona también la agorafobia como segunda candidata con evidencia indirecta.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Benign paroxysmal torticollis of infancy |
| Puntaje de Predicción TxGNN | 0.9985 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 9) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información farmacológica conocida, duloxetina inhibe la recaptación de serotonina (SERT) y de noradrenalina (NET), y los datos de farmacología muestran además interacción con los receptores 5-HT2A, 5-HT2C y 5-HT6.

El TOC responde principalmente a fármacos serotoninérgicos (ISRS, clomipramina). Como duloxetina actúa sobre el transportador de serotonina y ya está establecida en depresión y ansiedad generalizada, es mecanísticamente plausible su aplicación en un trastorno del espectro ansioso-obsesivo. Las revisiones sobre IRSN apoyan esta idea, aunque indican que la evidencia es menos sólida que para los ISRS.

La evidencia clínica proviene de estudios pequeños (n≈20-26): un ensayo doble ciego de potenciación en TOC resistente, un estudio abierto y un ensayo de Fase 4. No existe un ECA de Fase 3 grande, por lo que el nivel es L2 y no superior.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00464698](https://clinicaltrials.gov/study/NCT00464698) | Fase 4 | Completado | 20 | Eficacia de duloxetina en TOC; directamente relevante, pero pequeño y probablemente abierto |
| [NCT01404871](https://clinicaltrials.gov/study/NCT01404871) | N/A | Completado | 26 | Predicción de respuesta a medicación en TOC (clomipramina o escitalopram; duloxetina para quienes ya los probaron) |
| [NCT02476136](https://clinicaltrials.gov/study/NCT02476136) | N/A | Desconocido | 8800 | Metaanálisis de datos individuales sobre gravedad inicial y eficacia de antidepresivos en ansiedad; relevancia solo indirecta |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27811556](https://pubmed.ncbi.nlm.nih.gov/27811556/) | 2016 | ECA | J Clin Psychopharmacol | Ensayo doble ciego de potenciación con duloxetina en TOC resistente |
| [25637377](https://pubmed.ncbi.nlm.nih.gov/25637377/) | 2015 | Estudio abierto | Int J Neuropsychopharmacol | Eficacia de duloxetina en TOC (DSM-IV) |
| [31749717](https://pubmed.ncbi.nlm.nih.gov/31749717/) | 2019 | Revisión sistemática | Front Psychiatry | Usos de duloxetina en trastornos psiquiátricos más allá de la depresión y la ansiedad generalizada |
| [16669725](https://pubmed.ncbi.nlm.nih.gov/16669725/) | 2006 | Revisión | J Clin Psychiatry | Revisión crítica de IRSN en TOC como alternativa a los ISRS |
| [24766145](https://pubmed.ncbi.nlm.nih.gov/24766145/) | 2014 | Revisión | Expert Opin Pharmacother | Revisión de estudios doble ciego con antidepresivos serotoninérgicos en TOC |
| [28477500](https://pubmed.ncbi.nlm.nih.gov/28477500/) | 2017 | Metaanálisis | J Affect Disord | El TOC muestra menor respuesta a placebo y antidepresivos que otros trastornos de ansiedad |
| [21779536](https://pubmed.ncbi.nlm.nih.gov/21779536/) | 2011 | Revisión | Innov Clin Neurosci | Los IRSN como alternativas farmacológicas para el TOC |
| [18208931](https://pubmed.ncbi.nlm.nih.gov/18208931/) | 2008 | Serie de casos | J Psychopharmacol | Cambio de inhibidores de recaptación de serotonina a duloxetina en TOC resistente |
| [19483491](https://pubmed.ncbi.nlm.nih.gov/19483491/) | 2009 | Reporte de caso | Clin Neuropharmacol | Dosis altas de duloxetina con remisión completa sostenida en TOC resistente |
| [39735048](https://pubmed.ncbi.nlm.nih.gov/39735048/) | 2024 | Reporte de caso | Cureus | Duloxetina supraterapéutica con TCC en TOC grave resistente con depresión |

### Candidata secundaria: agorafobia (L3, TxGNN 0.9984)

La evidencia es indirecta: estudios abiertos o pequeños en trastorno de pánico (con o sin agorafobia), como el [PMID 19228176](https://pubmed.ncbi.nlm.nih.gov/19228176/) (2009, estudio abierto) y el [PMID 24294001](https://pubmed.ncbi.nlm.nih.gov/24294001/) (2013, reporte de caso). El único ensayo vinculado ([NCT05930912](https://clinicaltrials.gov/study/NCT05930912)) no guarda relación con duloxetina. Se considera una pregunta de investigación.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 82593 | Dulotex 30 mg comprimidos gastrorresistentes | Comprimido gastrorresistente | Texto de indicación no disponible |
| 04296006 | Cymbalta 30 mg cápsulas duras gastrorresistentes | Cápsula gastrorresistente | Texto de indicación no disponible |
| 04296002IP2 | Cymbalta 60 mg cápsulas duras gastrorresistentes | Cápsula dura gastrorresistente | Texto de indicación no disponible |
| 04280003 | Yentreve 40 mg cápsulas duras gastrorresistentes | Cápsula dura gastrorresistente | Texto de indicación no disponible |
| 88002 | Duloxetina Cinfamed 120 mg cápsulas duras gastrorresistentes | Cápsula dura gastrorresistente | Texto de indicación no disponible |

Hay 20 autorizaciones vigentes en total (todas de principio activo único, ninguna cancelada).

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proviene del prospecto):** hipertensión, hipotensión ortostática, atrofia multisistémica, síndrome de taquicardia ortostática postural, epilepsia, trastorno bipolar, trastorno afectivo mayor, enfermedad hepática (incluidos cirrosis, hígado graso y hepatitis), enfermedad de la vesícula biliar, hiperglucemia, abuso/dependencia de sustancias, trastornos de la coagulación, glaucoma de ángulo cerrado, síndrome neuroléptico maligno, síndrome de secreción inadecuada de ADH (incluida la forma nefrogénica) y síndrome serotoninérgico.
- **Interacciones farmacológicas:** los datos compilados reflejan sobre todo dianas farmacológicas (SERT, NET, receptores 5-HT2A, 5-HT2C y 5-HT6, ZC3H14), no interacciones con otros fármacos de relevancia clínica. Dado el riesgo de síndrome serotoninérgico, conviene revisar con cuidado cualquier asociación con otros agentes serotoninérgicos.

Consultar el prospecto para las advertencias y contraindicaciones oficiales.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ECA doble ciego, un estudio abierto y un ensayo de Fase 4 que respaldan duloxetina en TOC, junto con un mecanismo plausible (inhibición de SERT/NET). Sin embargo, todos los estudios son pequeños, no hay ECA de Fase 3 y las revisiones consideran a los IRSN menos establecidos que los ISRS, por lo que se recomienda avanzar con cautela.

**Para avanzar se necesita:**
- Un ECA de mayor tamaño (Fase 2b/3) de duloxetina en TOC, frente a un ISRS o placebo
- Datos del mecanismo de acción (MOA) y de las advertencias y contraindicaciones del prospecto de la AEMPS, hoy pendientes
- Textos de indicación aprobada de las autorizaciones españolas
- Plan de monitorización de seguridad (presión arterial, función hepática, riesgo de síndrome serotoninérgico, historial bipolar)
- Las demás candidatas (rank 1 y 4-10) carecen de evidencia y mecanismo plausible: se recomienda **Hold**. La agorafobia puede mantenerse como pregunta de investigación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

