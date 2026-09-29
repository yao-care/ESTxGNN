---
layout: default
title: Morphine
parent: Evidencia moderada (L3-L4)
nav_order: 366
evidence_level: L3
indication_count: 10
---

# Morphine
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **10** 
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

# Morfina: De Dolor Intenso a Síndrome de Dolor Miofascial

## Resumen en Una Frase

La morfina es un agonista opioide utilizado desde hace décadas para el tratamiento y manejo del dolor intenso.
El modelo TxGNN predice que podría ser efectiva para el **síndrome de dolor miofascial**, pero los **33 ensayos clínicos** y las **17 publicaciones** recuperados son en su mayoría indirectos: ninguno evalúa la eficacia de la morfina en esta enfermedad.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dolor intenso (según datos farmacológicos; los textos de indicación de las autorizaciones no están disponibles) |
| Nueva Indicación Predicha | Síndrome de dolor miofascial |
| Puntaje de Predicción TxGNN | 99.75% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente de datos. Según la información farmacológica disponible, la morfina se une a los receptores opioides μ (OPRM1), δ (OPRD1) y κ (OPRK1), y actúa sobre todo como agonista μ. Su eficacia analgésica en el dolor intenso está bien establecida, y por eso el vínculo con otras condiciones dolorosas resulta plausible.

El síndrome de dolor miofascial se caracteriza por puntos gatillo y por sensibilización periférica y central. Es una condición dolorosa, pero no suele responder a opioides. La predicción del modelo probablemente refleja la cercanía entre "dolor" y "dolor musculoesquelético" en el grafo de conocimiento, y no una evidencia terapéutica específica.

La evidencia directa se limita a contextos perioperatorios o de infiltración y a informes retrospectivos sobre el uso de opioides. El uso prolongado de opioides en esta condición conlleva riesgo de dependencia e hiperalgesia. Por eso la predicción se considera una pregunta de investigación y no una opción terapéutica lista para aplicarse.

## Evidencia de Ensayos Clínicos

Se recuperaron 33 ensayos. Ninguno prueba la morfina como tratamiento del síndrome miofascial. Se listan los 10 más relacionados con la condición o con el uso de opioides.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT07413770](https://clinicaltrials.gov/study/NCT07413770) | N/A | Completado | 60 | Masaje clásico solo o combinado con fisioterapia en personas con síndrome miofascial |
| [NCT05478928](https://clinicaltrials.gov/study/NCT05478928) | N/A | Desconocido | 60 | Microelectrólisis percutánea y punción seca en puntos gatillo miofasciales |
| [NCT04640896](https://clinicaltrials.gov/study/NCT04640896) | Fase 4 | Completado | 60 | Inyecciones en puntos gatillo frente a terapias tradicionales en dolor miofascial cervical tras cirugía |
| [NCT06955923](https://clinicaltrials.gov/study/NCT06955923) | Fase 2 | Completado | 11 | Inyección en puntos gatillo tras artroplastia de rodilla para reducir dolor y uso de opioides |
| [NCT04504812](https://clinicaltrials.gov/study/NCT04504812) | Fase 3 | Completado | 1937 | Estrategia secuenciada de tratamientos en dolor por artrosis de rodilla; otra condición, no evalúa morfina |
| [NCT04862845](https://clinicaltrials.gov/study/NCT04862845) | Fase 1 | Completado | 90 | Duloxetina más pregabalina para dolor tras liposucción; no es morfina |
| [NCT06533345](https://clinicaltrials.gov/study/NCT06533345) | N/A | Reclutando | 120 | Programa de investigación en una clínica de dolor crónico; inespecífico |
| [NCT06179199](https://clinicaltrials.gov/study/NCT06179199) | N/A | Aún no reclutando | 40 | Estimulación transcraneal (tDCS) para reducir el uso de morfina en pacientes sedados en UCI |
| [NCT03271151](https://clinicaltrials.gov/study/NCT03271151) | Fase 4 | Completado | 160 | Efecto de la duloxetina sobre el consumo de opioides tras artroplastia de rodilla |
| [NCT03161795](https://clinicaltrials.gov/study/NCT03161795) | N/A | Completado | 258 | Estudio observacional en Corea sobre riesgos del tratamiento opioide prolongado en dolor crónico no oncológico |

## Evidencia de Literatura

Se recuperaron 17 publicaciones. Se listan las 10 más pertinentes, con prioridad para los ensayos aleatorizados.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41664327](https://pubmed.ncbi.nlm.nih.gov/41664327/) | 2026 | ECA | Asian Spine J | Dexmedetomidina más morfina frente a ropivacaína 0.2% en infiltración miofascial en fusión espinal toracolumbar |
| [17870625](https://pubmed.ncbi.nlm.nih.gov/17870625/) | 2008 | ECA | Eur J Pain | Analgesia epidural (bupivacaína y morfina) frente a crioanalgesia intercostal en dolor postoracotomía, 107 pacientes |
| [35066974](https://pubmed.ncbi.nlm.nih.gov/35066974/) | 2022 | Cohorte retrospectiva | Pain Pract | Programa estructurado de estiramientos para resolver dolor miofascial y reducir el uso de opioides |
| [21419546](https://pubmed.ncbi.nlm.nih.gov/21419546/) | 2011 | Observacional/revisión | J Oral Maxillofac Surg | El uso de opioides a largo plazo en disfunción temporomandibular no puede apoyarse ni refutarse con la evidencia actual |
| [20390305](https://pubmed.ncbi.nlm.nih.gov/20390305/) | 2010 | Estudio longitudinal | Schmerz | Cambios en los umbrales de dolor durante y después de la retirada de opioides en lumbalgia crónica |
| [16713811](https://pubmed.ncbi.nlm.nih.gov/16713811/) | 2006 | Serie clínica | J Oral Maxillofac Surg | Artrocentesis de la articulación temporomandibular seguida de infusión intraarticular de morfina |
| [22648287](https://pubmed.ncbi.nlm.nih.gov/22648287/) | 2012 | Estudio clínico | J Anesth | Inyecciones facetarias cervicales en un programa multimodal para dolor miofascial cervical de larga evolución |
| [39793344](https://pubmed.ncbi.nlm.nih.gov/39793344/) | 2025 | Estudio clínico | Eur J Obstet Gynecol Reprod Biol | Bloqueo del nervio pudendo para el dolor perioperatorio tras toxina botulínica en dolor pélvico miofascial |
| [7478690](https://pubmed.ncbi.nlm.nih.gov/7478690/) | 1995 | Preclínico | Pain | Modelo en ratas de litiasis ureteral: relación entre dolor visceral e hiperalgesia muscular lumbar referida |
| [21691691](https://pubmed.ncbi.nlm.nih.gov/21691691/) | 2011 | Serie descriptiva | Rev Assoc Med Bras | Enfoque terapéutico en 56 pacientes con síndrome de dolor tras cirugía de espalda fallida |

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones registradas. Los textos de indicación aprobada no están disponibles en los datos recibidos.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 61909 | MST CONTINUS 200 mg comprimidos de liberación prolongada | Comprimido de liberación prolongada | Mundipharma Pharmaceuticals S.L. |
| 59655 | SEVREDOL 20 mg comprimidos recubiertos con película | Comprimido recubierto con película | Mundipharma Pharmaceuticals S.L. |
| 86588 | MORFINA SUN 2 mg/ml solución para perfusión en jeringa precargada | Solución para perfusión en jeringa precargada | Sun Pharmaceutical Industries (Europe) B.V. |
| 57897 | MST CONTINUS 30 mg comprimidos de liberación prolongada | Comprimido de liberación prolongada | Mundipharma Pharmaceuticals S.L. |
| 61080 | MST CONTINUS 5 mg comprimidos de liberación prolongada | Comprimido de liberación prolongada | Mundipharma Pharmaceuticals S.L. |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta se completó, pero no devolvió interacciones con otros medicamentos. Solo registró la farmacología de dianas: la morfina se une a los receptores opioides δ (OPRD1), κ (OPRK1) y μ (OPRM1).
- **Riesgos señalados en la evidencia revisada**: el uso prolongado de opioides en dolor miofascial conlleva riesgo de dependencia e hiperalgesia. En otros trastornos dolorosos se ha descrito además la aparición de síntomas durante la retirada de opioides.

Consultar el prospecto para las advertencias y contraindicaciones.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene una puntuación alta (99.75%), pero no hay ningún ensayo ni estudio que pruebe la morfina en el síndrome miofascial. La evidencia disponible es indirecta (perioperatoria, de infiltración o retrospectiva). Además, esta condición no suele responder a opioides y el perfil de riesgo del uso prolongado es desfavorable.

**Para avanzar se necesita:**
- Un estudio controlado que evalúe la morfina, u otro opioide con justificación clara, específicamente en síndrome de dolor miofascial.
- Las advertencias y contraindicaciones del prospecto de la AEMPS, hoy no disponibles, para poder completar el cribado de seguridad.
- Datos detallados del mecanismo de acción para analizar el vínculo mecanístico.
- Una comparación con alternativas no opioides ya usadas en esta condición (punción seca, inyección de puntos gatillo, medidas físicas).

Entre las demás predicciones para la morfina, el síndrome de piernas inquietas (L3, etapa S2) es la única con recomendación "Proceed with Guardrails" y con mejor respaldo clínico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

