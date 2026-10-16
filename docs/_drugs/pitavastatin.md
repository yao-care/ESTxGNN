---
layout: default
title: Pitavastatin
parent: Solo predicción del modelo (L5)
nav_order: 645
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Pitavastatin: nueva indicación predicha, Hipercolesterolemia familiar homocigota (nivel de evidencia L5). Indicación original: Hiperlipidemia familiar combinada (según el grafo de conocimiento"
monitor_inn: "pitavastatin"
predicted_indications: ["homozygous familial hypercholesterolemia", "hyperlipoproteinemia", "familial hypercholesterolemia", "cholesterol-ester transfer protein deficiency", "hypercholesterolemia, autosomal dominant", "hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency", "HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "hyperlipidemia due to hepatic triglyceride lipase deficiency", "feline acquired immunodeficiency syndrome"]
---

# Pitavastatin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Pitavastatina: De Hiperlipidemia Familiar Combinada a Hipercolesterolemia Homocigota Familiar

## Resumen en Una Frase

Pitavastatina es una estatina (inhibidor de la HMG-CoA reductasa), originalmente utilizada para el tratamiento de la hiperlipidemia familiar combinada.
El modelo TxGNN predice que podría ser efectivo para **hipercolesterolemia familiar homocigota**, pero actualmente **no hay ensayos clínicos** y solo **2 publicaciones** de relevancia indirecta que respaldan esta dirección concreta.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hiperlipidemia familiar combinada (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Hipercolesterolemia familiar homocigota |
| Puntaje de Predicción TxGNN | 99.996% |
| Nivel de Evidencia | L4 (según la clasificación de los datos compilados; ver nota abajo) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

> **Nota:** Según las reglas de nivel de evidencia de este informe, la ausencia de estudios específicos en hipercolesterolemia familiar homocigota (HoFH) correspondería más bien a L5 (solo predicción del modelo). Los datos compilados asignan L4. En cualquier caso, la decisión es Hold.

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, pitavastatina es una estatina que inhibe la HMG-CoA reductasa, reduce la síntesis hepática de colesterol y aumenta la expresión del receptor de LDL, favoreciendo la depuración del colesterol LDL.

La hiperlipidemia familiar combinada y la HoFH son dislipidemias hereditarias con elevación del colesterol LDL, de modo que existe una cercanía clínica y mecanística que explica la puntuación elevada del modelo.

Sin embargo, en la HoFH la eficacia de las estatinas depende de la actividad residual del receptor de LDL, por lo que la respuesta sería limitada en genotipos con ausencia total de receptor. No se aportan ensayos específicos en HoFH. Las dos publicaciones recuperadas son un ensayo en adultos con VIH y dislipidemia y un reporte de casos de hipercolesterolemia autosómica recesiva, una entidad distinta.

> **Contexto de otras predicciones:** Para otras indicaciones predichas hay mayor respaldo, aunque en su mayoría no constituyen un reposicionamiento real: la hipercolesterolemia familiar (heterocigota, nivel L2) y, de forma destacada, la reducción del riesgo cardiovascular en personas con VIH (nivel L1, ensayo REPRIEVE, NEJM 2023), que no trata la infección por VIH sino su riesgo cardiovascular. La hiperlipoproteinemia corresponde esencialmente a la indicación ya aprobada.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para hipercolesterolemia familiar homocigota.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28416195](https://pubmed.ncbi.nlm.nih.gov/28416195/) | 2017 | ECA (Fase 4) | The Lancet HIV | Pitavastatina frente a pravastatina en adultos con VIH-1 y dislipidemia (INTREPID), a 12 y 52 semanas; población distinta de la HoFH |
| [39532566](https://pubmed.ncbi.nlm.nih.gov/39532566/) | 2025 | Reporte de casos | Journal of Clinical Lipidology | Respuesta hipolipemiante rápida en dos casos de hipercolesterolemia autosómica recesiva (LDLRAP1), clínicamente indistinguible de la HoFH |

## Información de Mercado en España

Pitavastatina está comercializada en España con 20 autorizaciones vigentes (todas monofármaco), en comprimidos recubiertos con película. Se muestran las 5 principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 73040 | ALIPZA 4 mg (Kowa Pharmaceutical Europe) | Comprimido recubierto con película | No disponible en los datos |
| 5324538IP | LIVAZO 1 mg (Kowa Pharmaceutical Europe) | Comprimido recubierto con película | No disponible en los datos |
| 89062 | VASPIT 2 mg EFG (Medochemie) | Comprimido recubierto con película | No disponible en los datos |
| 85214 | Pitavastatina Normogen 1 mg EFG (Laboratorios Normon) | Comprimido recubierto con película | No disponible en los datos |
| 84888 | Pitavastatina Krka 2 mg EFG (Krka) | Comprimido recubierto con película | No disponible en los datos |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no texto de prospecto):** enfermedad hepática, enfermedad de la vesícula biliar, hipotiroidismo (incluidos mixedema e hipotiroidismo congénito), miopatía y enfermedades musculares, parálisis periódica familiar, trastornos hipotensivos, rabdomiólisis, fascitis nodular, insuficiencia renal y lesiones.
- **Interacciones farmacológicas:** se registran 86 interacciones. Entre las principales: **eritromicina (Mayor)**; de nivel moderado, rosuvastatina, simvastatina, cobicistat, eltrombopag, etanol, metronidazol, tinidazol, cloroquina e hidroxicloroquina, entre otras; de nivel menor, warfarina y dicumarol. Otras fuentes citan contraindicación con ciclosporina e inhibidores de OATP1B1.

Se debe consultar el prospecto para las advertencias y contraindicaciones oficiales, ya que no están disponibles en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para HoFH se apoya solo en el modelo y en literatura indirecta (una población con VIH y una serie de casos de otra entidad), sin ensayos clínicos específicos. Además, la eficacia de las estatinas en HoFH depende de la actividad residual del receptor de LDL, por lo que la respuesta podría ser limitada.

**Para avanzar se necesita:**
- Estudios clínicos o series de casos de pitavastatina en HoFH con genotipo caracterizado (receptor LDL residual frente a receptor-negativo).
- Datos del mecanismo de acción y de las advertencias y contraindicaciones oficiales (prospecto de la AEMPS).
- Valorar las alternativas con mayor respaldo de las predicciones del modelo: hipercolesterolemia familiar heterocigota (L2, estudios pediátricos y de adultos) y reducción del riesgo cardiovascular en personas con VIH (L1, REPRIEVE), con vigilancia de interacciones, función hepática, riesgo de miopatía y, en población pediátrica, crecimiento y maduración.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

