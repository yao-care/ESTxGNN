---
layout: default
title: Dantrolene
parent: Solo predicción del modelo (L5)
nav_order: 220
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-24
monitor_inn: "Dantrolene"
predicted_indications: ["moderate multiminicore disease with hand involvement", "King-Denborough syndrome", "congenital multicore myopathy with external ophthalmoplegia", "central core myopathy", "hypokalemic periodic paralysis", "thyrotoxic periodic paralysis", "myopathy, centronuclear"]
description: "Dantrolene: nueva indicación predicha, Moderate multiminicore disease with hand involvement (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 1 (comercializadas: 1)"
---

# Dantrolene
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

## Dantrolene: Moderate multiminicore disease with hand involvement
{: .text-alpha }

## Resumen en Una Frase

Dantroleno es un relajante muscular que actúa sobre el receptor de rianodina, utilizado originalmente para tratar la hipertermia maligna asociada a la anestesia y la inducida por el ejercicio.
El modelo TxGNN predice que podría ser efectivo para **enfermedad multiminicore moderada con afectación de la mano** (puntaje 0,9990), con **0 ensayos clínicos** y **18 publicaciones** (guías, revisiones y estudios mecanísticos) que respaldan esta dirección.
Cabe señalar que esta predicción coincide en la práctica con la indicación original, por lo que no constituye un reposicionamiento propiamente dicho.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Moderate multiminicore disease with hand involvement |
| Puntaje de Predicción TxGNN | 0.9990 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 1) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Dantrolene (traducción no oficial): «En preparaciones aisladas de nervio-músculo, se ha demostrado que el dantroleno produce relajación al afectar la respuesta contráctil del músculo en un sitio más allá de la unión mioneural. En el músculo esquelético, el dantroleno disocia el acoplamiento excitación-contracción, probablemente al interferir en la liberación de Ca ++ del retículo sarcoplásmico.» Texto original en inglés: "In isolated nerve-muscle preparation, dantrolene has been shown to produce relaxation by affecting the contractile response of the muscle at a site beyond the myoneural junction. In skeletal muscle, dantrolene dissociates the excitation-contraction coupling, probably by interfering with the release of Ca ++ from the sarcoplasmic reticulum." ([DailyMed: Ryanodex Dantrolene Sodium (dantrolene sodium) prescribing information, Eagle Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8f7b3ac0-604d-4c78-b545-5e0f8ea3d698), versión del 2024-10-30; consultado el 2026-11-19). Según la información farmacológica compilada, dantroleno actúa sobre los receptores de rianodina (RyR1 y RyR3), canales de liberación de calcio del retículo sarcoplásmico del músculo esquelético. Al inhibir esta liberación, reduce la contractilidad y el estado hipermetabólico característico de la crisis.

La susceptibilidad a la hipertermia maligna se debe principalmente a variantes de ganancia de función en *RYR1*, que provocan una liberación descontrolada de calcio. Es el mismo mecanismo que justifica la indicación aprobada, y dantroleno es el tratamiento de referencia recomendado por las guías de la Association of Anaesthetists (PMID 33399225) y del European Malignant Hyperthermia Group (PMID 33131754). Un estudio mecanístico (PMID 28373535) además describe que el fármaco requiere Mg2+ para detener la crisis.

**Otras predicciones del modelo (contexto):**
- **Con respaldo indirecto (L4, "pregunta de investigación"):** síndrome de King-Denborough, miopatía multicore congénita con oftalmoplejía externa, miopatía del núcleo central y miopatía centronuclear. En ellas la relevancia del dantroleno se limita al manejo del riesgo de hipertermia maligna, sin evidencia de beneficio sobre la miopatía de base.
- **Solo predicción del modelo (L5, "Hold"):** enfermedad multiminicore moderada con afectación de la mano, parálisis periódica hipopotasémica y parálisis periódica tirotóxica (ambas formas). No hay ensayos ni literatura que las respalden.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Se muestran las publicaciones más relevantes (guías y revisiones priorizadas, más un estudio mecanístico):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33399225](https://pubmed.ncbi.nlm.nih.gov/33399225/) | 2021 | Guía | Anaesthesia | Guía de la Association of Anaesthetists 2020 sobre hipertermia maligna, con base genética y riesgo ante anestésicos inhalatorios y suxametonio |
| [33131754](https://pubmed.ncbi.nlm.nih.gov/33131754/) | 2021 | Guía/Consenso | British Journal of Anaesthesia | Consenso europeo sobre manejo perioperatorio de pacientes sospechosos o susceptibles; no hay ensayos intervencionistas por la rareza y límites éticos |
| [26238698](https://pubmed.ncbi.nlm.nih.gov/26238698/) | 2015 | Revisión | Orphanet J Rare Dis | Trastorno farmacogenético del músculo esquelético; incidencia de 1:10.000 a 1:250.000 anestesias |
| [39171998](https://pubmed.ncbi.nlm.nih.gov/39171998/) | 2024 | Revisión | Critical Care Medicine | Revisión narrativa de epidemiología clínica y manejo de pacientes críticos con hipertermia maligna |
| [32008650](https://pubmed.ncbi.nlm.nih.gov/32008650/) | 2020 | Revisión | Anesthesiology Clinics | Trastorno de los canales de liberación de calcio, herencia autosómica dominante; la mortalidad ha mejorado |
| [9538480](https://pubmed.ncbi.nlm.nih.gov/9538480/) | 1998 | Revisión | Postgrad Med J | Indica el dantroleno sódico como tratamiento definitivo y describe precauciones en pacientes susceptibles |
| [25989378](https://pubmed.ncbi.nlm.nih.gov/25989378/) | 2015 | Revisión | Acta Anaesthesiol Scand | Actualización escandinava; la mayoría de los casos se vinculan a mutaciones en *RYR1* |
| [28373535](https://pubmed.ncbi.nlm.nih.gov/28373535/) | 2017 | Mecanístico | PNAS | El dantroleno requiere Mg2+ para detener la hipertermia maligna |
| [23198031](https://pubmed.ncbi.nlm.nih.gov/23198031/) | 2012 | Revisión | Korean J Anesthesiol | Herencia autosómica dominante con expresión variable y penetrancia incompleta |
| [14661655](https://pubmed.ncbi.nlm.nih.gov/14661655/) | 2003 | Revisión | Best Pract Res Clin Anaesthesiol | Liberación descontrolada de calcio desde el retículo sarcoplásmico; posible relación con golpe de calor y rabdomiólisis |

---

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 1241805001 | AGILUS 120 MG POLVO PARA SOLUCION INYECTABLE | POLVO PARA SOLUCIÓN INYECTABLE | Norgine B.V. | Comercializada |

Se muestra la única autorización con este principio activo en los datos de CIMA (AEMPS).

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Contraindicaciones / enfermedades de precaución según el grafo de conocimiento** (no proceden del texto del prospecto): enfermedad hepática, enfermedad de la vesícula biliar, miopatía, enfermedad muscular, enfermedad del músculo esquelético, parálisis periódica familiar y enfermedad pulmonar (incluida una enfermedad pulmonar rara).
- **Interacciones farmacológicas:** no se registraron interacciones con otros fármacos. Solo constan las dianas farmacológicas RyR1 y RyR3 (humanas).

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Dantroleno es el tratamiento de referencia para la hipertermia maligna, respaldado por guías internacionales y por un mecanismo coherente con la indicación aprobada. El nivel L3 refleja que no hay ensayos registrados y que la evidencia se basa en guías y revisiones, no una debilidad del uso clínico.

**Para avanzar se necesita:**
- Obtener el prospecto oficial de la AEMPS (advertencias y contraindicaciones), cuya ausencia impide completar el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Confirmar la indicación aprobada en la autorización española.
- Para las indicaciones de miopatías congénitas y parálisis periódicas, considerar solo como preguntas de investigación (o mantener en espera), dado que no hay evidencia de beneficio sobre la enfermedad de base.
- Valorar con cautela el uso en pacientes con enfermedad hepática o muscular, según las contraindicaciones del grafo de conocimiento.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Ryanodex Dantrolene Sodium (dantrolene sodium) prescribing information, Eagle Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8f7b3ac0-604d-4c78-b545-5e0f8ea3d698) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

