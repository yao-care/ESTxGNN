---
layout: default
title: Dantrolene
parent: Solo predicción del modelo (L5)
nav_order: 220
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
monitor_inn: "Dantrolene"
predicted_indications: ["moderate multiminicore disease with hand involvement", "King-Denborough syndrome", "congenital multicore myopathy with external ophthalmoplegia", "central core myopathy", "hypokalemic periodic paralysis", "thyrotoxic periodic paralysis", "myopathy, centronuclear"]
description: "Dantrolene: nueva indicación predicha, Moderate multiminicore disease with hand involvement (nivel de evidencia L5). Indicación original: No consta en los datos locales"
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
| Estado de Mercado en España | Comercializado (registros vigentes: 1 de 1) |
| Número de Autorizaciones | 1 (vigentes: 1) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco. Según la información farmacológica compilada, dantroleno actúa sobre los receptores de rianodina (RyR1 y RyR3), canales de liberación de calcio del retículo sarcoplásmico del músculo esquelético. Al inhibir esta liberación, reduce la contractilidad y el estado hipermetabólico característico de la crisis.

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

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1241805001 | AGILUS 120 MG POLVO PARA SOLUCIÓN INYECTABLE (Norgine B.V.) | Polvo para solución inyectable | No disponible en los datos compilados |

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
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

