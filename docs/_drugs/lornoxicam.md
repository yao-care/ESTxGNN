---
layout: default
title: Lornoxicam
parent: Evidencia alta (L1-L2)
nav_order: 486
evidence_level: L2
indication_count: 8
monitor_inn: "LORNOXICAM"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "headache disorder", "trigeminal autonomic cephalalgia", "tendinitis", "idiopathic granulomatous myositis"]
last_modified_at: 2026-10-28
description: "Lornoxicam: nueva indicación predicha, Trastorno de migraña (nivel de evidencia L2). Indicación original: No disponible (las autorizaciones no incluyen texto de indicación)"
---

# Lornoxicam
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

## Lornoxicam: De Indicación Original (sin texto de indicación disponible) a Trastorno de Migraña
{: .text-alpha }

## Resumen en Una Frase

Lornoxicam es un antiinflamatorio no esteroideo (AINE) de la clase de los oxicams, con propiedades analgésicas, antiinflamatorias y antipiréticas. Las autorizaciones españolas de los datos compilados no incluyen texto de indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **trastorno de migraña**, con **1 ensayo clínico** de Fase 2 y **2 publicaciones** que actualmente respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (las autorizaciones no incluyen texto de indicación) |
| Nueva Indicación Predicha | Trastorno de migraña |
| Puntaje de Predicción TxGNN | 0,9987 |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | Comercializado (registros vigentes: 1 de 7) |
| Número de Autorizaciones | 7 (vigentes: 1) |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la farmacología conocida de la clase, lornoxicam es un AINE que inhibe las enzimas COX-1 y COX-2 y, con ello, reduce la síntesis de prostaglandinas.

Las prostaglandinas participan en la inflamación neurogénica y en la sensibilización al dolor que ocurren en la migraña. Los AINE son una clase de fármacos establecida para el tratamiento de las crisis agudas de migraña, por lo que el mecanismo es biológicamente plausible y coherente con la clase. Esta vinculación se basa en la farmacología conocida de la clase y no en datos de mecanismo específicos de este fármaco.

Una revisión de 1992 sobre AINE en migraña incluye lornoxicam entre los fármacos evaluados. Además, un ensayo de Fase 2 completado estudió lornoxicam intravenoso en el dolor de cabeza agudo de la migraña.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00293657](https://clinicaltrials.gov/study/NCT00293657) | Fase 2 | Completado | 150 | Estudio aleatorizado, doble ciego y controlado con placebo de dosis única de lornoxicam intravenoso (8 mg o 16 mg) frente a placebo en el dolor de cabeza moderado o intenso de una crisis de migraña. Los resultados del criterio principal no figuran en los datos compilados. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [1495823](https://pubmed.ncbi.nlm.nih.gov/1495823/) | 1992 | Revisión | Pathologie-biologie | Revisa estudios controlados de AINE en el tratamiento de crisis de migraña y en la profilaxis, entre ellos lornoxicam. |
| [8706598](https://pubmed.ncbi.nlm.nih.gov/8706598/) | 1996 | Revisión | Drugs | Revisión de la farmacología y el potencial terapéutico de lornoxicam en dolor y afecciones inflamatorias; semivida de eliminación corta (3 a 5 horas). Es una fuente general sobre el fármaco, no específica de migraña. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 78274 | LORNOXICAM RAPID MEIJI 8 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG (vigente) | Comprimido recubierto con película | No disponible |
| 61836 | ACABEL 4 mg (cancelada) | Comprimido recubierto con película | No disponible |
| 61837 | ACABEL 8 mg (cancelada) | Comprimido recubierto con película | No disponible |
| 65059 | ACABEL RAPID 8 mg (cancelada) | Comprimido recubierto con película | No disponible |
| 62691 | BOSPORON 8 mg (cancelada) | Comprimido recubierto con película | No disponible |

Hay 7 autorizaciones en total (1 vigente y 6 canceladas); la tabla muestra las 5 principales.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ensayo de Fase 2 completado, aleatorizado y controlado con placebo, que estudia directamente lornoxicam en la migraña, junto con un mecanismo plausible de clase. Sin embargo, no hay resultados verificados del criterio principal ni ECA de Fase 3, por lo que la evidencia es limitada. Las predicciones de "trastorno de cefalea" se apoyan en el mismo ensayo y no constituyen evidencia independiente.

**Para avanzar se necesita:**
- Verificar los resultados del criterio principal del ensayo NCT00293657.
- Obtener el prospecto de la AEMPS (advertencias y contraindicaciones) y los datos de mecanismo de acción.
- Aclarar la vía de administración: el ensayo usó la vía intravenosa, y la única autorización vigente en España es oral.
- Evaluar el perfil de seguridad de los AINE (gastrointestinal, cardiovascular, renal) en uso repetido para migraña.

**Otras predicciones (nivel L5 salvo indicación):** las predicciones de subtipos de migraña, cefalea trigémino-autonómica y miositis granulomatosa idiopática no cuentan con estudios directos y se mantienen en Hold. El síndrome de braquidactilia-sindactilia y el síndrome de microftalmia colobomatosa-displasia rizomélica carecen de vínculo mecanístico plausible; sus puntuaciones provienen del modelo TxGNN (deep learning) y probablemente reflejan similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. La tendinitis (L3 asignado en los datos) solo tiene un estudio en síndrome de pinzamiento subacromial, donde lornoxicam inyectable resultó inferior a betametasona; no es un estudio directo de tendinitis, por lo que debe considerarse L5 según el criterio de evidencia directa.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

