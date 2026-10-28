---
layout: default
title: Emtricitabine
parent: Solo predicción del modelo (L5)
nav_order: 288
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
monitor_inn: "Emtricitabine"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
description: "Emtricitabine: nueva indicación predicha, Síndrome de inmunodeficiencia adquirida felina (feline acquired immunodeficiency syndrome) (nivel de evidencia L5). Indicación original: No consta en los dat…"
---

# Emtricitabine
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

## Emtricitabine: Síndrome de inmunodeficiencia adquirida felina (feline acquired immunodeficiency syndrome)
{: .text-alpha }

## Resumen en Una Frase

Emtricitabina es un inhibidor nucleosídico de la transcriptasa inversa, originalmente utilizado para el tratamiento de la infección por VIH y el SIDA.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia adquirida felina**, con **0 ensayos clínicos** y **1 publicación** (un estudio preclínico/veterinario) que respaldan esta dirección.
Se trata de una indicación veterinaria, fuera del alcance del reposicionamiento en medicina humana.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina (feline acquired immunodeficiency syndrome) |
| Puntaje de Predicción TxGNN | 0.9992 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 2 de 2) |
| Número de Autorizaciones | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento general, emtricitabina es un inhibidor nucleosídico de la transcriptasa inversa (NRTI) con actividad frente a la transcriptasa inversa del VIH-1, y su eficacia en la infección por VIH está establecida.

El virus de la inmunodeficiencia felina (FIV) es un lentivirus con una transcriptasa inversa relacionada, por lo que la actividad de los NRTI es biológicamente plausible. La única publicación disponible (2023) evalúa una terapia antirretroviral combinada (dolutegravir, tenofovir y emtricitabina) en gatos infectados por FIV, por lo que aporta evidencia indirecta para emtricitabina en particular.

Al ser una indicación veterinaria, queda fuera del ámbito del reposicionamiento en humanos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Estudio preclínico/veterinario | Viruses | Evalúa la farmacocinética y los resultados clínicos de la terapia antirretroviral combinada (dolutegravir, tenofovir, emtricitabina) en gatos infectados por FIV, y el inmunofenotipo asociado. Diseño no confirmado a partir del título. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 03261001 | EMTRIVA 200 MG CÁPSULAS | Cápsula dura | No disponible |
| 03261003 | EMTRIVA 10 MG/ML SOLUCIÓN ORAL | Solución oral | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no el prospecto)**: se han asociado, entre otras, las siguientes enfermedades: síndrome de QT largo (familiar), torsades de pointes, insuficiencia hepática, hepatopatía, hígado graso y esteatohepatitis no alcohólica, enfermedad renal, síndrome de Fanconi, acidosis láctica, hipofosfatemia, osteomalacia y raquitismo, infección crónica por virus de la hepatitis B y C, hipertrigliceridemia, obesidad, epilepsia, trastornos de ansiedad y trastornos delirantes/esquizofrenia paranoide. Deben verificarse con el prospecto oficial.
- **Interacciones Farmacológicas**: se identificaron 20 interacciones.
  - **Mayores**: leflunomida y teriflunomida.
  - **Moderadas** (principales): cobicistat, metotrexato, naltrexona, orlistat, interferón beta-1a/1b, peginterferón beta-1a, cladribina, clofarabina, tioguanina, epirrubicina, idelalisib, cabozantinib, brentuximab vedotina, trabectedina, asparaginasa y pegaspargasa.
  - **Menores**: eribulina.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en un estudio preclínico/veterinario indirecto, sin ensayos clínicos, y la indicación es veterinaria, fuera del alcance de la evaluación de reposicionamiento en humanos. El puntaje TxGNN alto no sustituye a la evidencia clínica.

**Para avanzar se necesita:**
- Aclarar si el alcance del programa admite indicaciones veterinarias.
- Datos de eficacia específicos de emtricitabina en FIV (estudios controlados en gatos).
- Datos del mecanismo de acción y del prospecto oficial de la AEMPS (advertencias y contraindicaciones).

---

### Nota sobre otras predicciones del modelo

- **Infección por virus de inmunodeficiencia simia (SIV)** (puntaje 0.9992, nivel L4): hay numerosos estudios preclínicos en macacos que respaldan la profilaxis preexposición con emtricitabina combinada con tenofovir. Es un modelo traslacional del VIH ya aprobado en humanos, no una nueva indicación humana.
- **Trastorno del neurodesarrollo con marcha atáxica, ausencia del habla y reducción de la sustancia blanca cortical** (puntaje 0.9992, nivel L5): sin vínculo mecanístico identificado ni evidencia; probablemente un artefacto del modelo TxGNN (aprendizaje profundo).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

