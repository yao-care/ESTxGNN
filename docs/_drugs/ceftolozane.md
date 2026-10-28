---
layout: default
title: Ceftolozane
parent: Solo predicción del modelo (L5)
nav_order: 158
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
monitor_inn: "ceftolozane"
predicted_indications: ["Ureaplasma urethritis", "gonococcal urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "urogenital tuberculosis", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease"]
description: "Ceftolozane: nueva indicación predicha, Uretritis por Ureaplasma (Ureaplasma urethritis) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Ceftolozane
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

## Ceftolozane: Uretritis por Ureaplasma (Ureaplasma urethritis)
{: .text-alpha }

## Resumen en Una Frase

Ceftolozano es una cefalosporina (beta-lactámico) originalmente utilizada para el tratamiento de las infecciones del tracto urinario.
El modelo TxGNN predice que podría ser efectivo para **uretritis por Ureaplasma**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo, y además biológicamente poco plausible.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Uretritis por Ureaplasma (Ureaplasma urethritis) |
| Puntaje de Predicción TxGNN | 0.9989 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 1 de 1) |
| Número de Autorizaciones | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, ceftolozano es una cefalosporina que inhibe la síntesis de la pared celular bacteriana, y se comercializa en combinación con tazobactam (Zerbaxa). Su actividad está optimizada frente a *Pseudomonas aeruginosa* y Enterobacterales.

La relación con la indicación original es solo contextual: ambas son infecciones del tracto urogenital. Sin embargo, **el mecanismo no respalda la predicción**: *Ureaplasma* carece de pared celular, por lo que los beta-lactámicos son intrínsecamente ineficaces.

Cabe señalar que otras predicciones del modelo tienen una base más sólida. La **uretritis gonocócica** es un objetivo plausible para cefalosporinas (la ceftriaxona es tratamiento estándar), aunque sin evidencia específica para ceftolozano. La **pielonefritis xantogranulomatosa** (puntaje 0,9988, nivel L4) es la más cercana a la indicación original de infección urinaria complicada y pielonefritis, aunque su manejo suele requerir cirugía y los antibióticos son coadyuvantes.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la uretritis por Ureaplasma.

Como referencia sobre la predicción alternativa más cercana (pielonefritis xantogranulomatosa), se recuperó una publicación de evidencia indirecta:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [26658652](https://pubmed.ncbi.nlm.nih.gov/26658652/) | 2016 | Revisión | Current Opinion in Infectious Diseases | Revisión general de infecciones urinarias febriles, pielonefritis y urosepsis desde julio de 2014; no evalúa ceftolozano específicamente |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1151032001 | ZERBAXA 1 G/0,5 G POLVO PARA CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Polvo para concentrado para solución para perfusión | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (11 interacciones de nivel moderado registradas):
  - Aminoglucósidos: kanamicina, neomicina, estreptomicina, amikacina (incluida la forma liposomal), gentamicina
  - Anticoagulantes: warfarina, dicumarol
  - Otros: cloranfenicol, etinilestradiol, ácido micofenólico

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para uretritis por Ureaplasma se basa solo en el modelo (L5), sin ensayos ni literatura, y contradice el mecanismo conocido de los beta-lactámicos, ya que *Ureaplasma* no tiene pared celular. No se recomienda avanzar con esta indicación.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), actualmente un vacío bloqueante para el cribado de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Reorientar el análisis hacia candidatas con mayor plausibilidad biológica, como la pielonefritis xantogranulomatosa o la uretritis gonocócica, con revisión de literatura específica y datos de sensibilidad *in vitro*
- Descartar o deprioritizar las predicciones no infecciosas (síndrome de hiperviscosidad policlonal, hiperamilasemia, analbuminemia congénita, incompatibilidad de grupo sanguíneo, enfermedades hematológicas premalignas), que parecen artefactos del modelo
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

