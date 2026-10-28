---
layout: default
title: Inotersen
parent: Solo predicción del modelo (L5)
nav_order: 416
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Inotersen: nueva indicación predicha, Porfiria aguda intermitente (nivel de evidencia L4). Indicación original: No disponible en los datos de la autorización de AEMPS"
monitor_inn: "INOTERSEN"
predicted_indications: ["acute intermittent porphyria", "appendicitis", "IgG4-related pachymeningitis", "IgG4-related retroperitoneal fibrosis", "non-infectious meningitis", "peritonitis", "infectious meningitis", "IgG4-related mesenteritis", "IgG4-related mediastinitis", "IgG4-related aortitis"]
---

# Inotersen
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

## Inotersen: De Indicación Original No Especificada a Porfiria Aguda Intermitente
{: .text-alpha }

## Resumen en Una Frase

Inotersen es un oligonucleótido antisentido que reduce la producción de transtiretina (TTR). En los datos compilados para este informe no consta el texto de la indicación aprobada en España.
El modelo TxGNN predice que podría ser efectivo para **porfiria aguda intermitente**, pero no hay ensayos clínicos registrados y solo hay **1 publicación** (una revisión general) que ofrece un apoyo indirecto.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de la autorización de AEMPS |
| Nueva Indicación Predicha | Porfiria aguda intermitente |
| Puntaje de Predicción TxGNN | 0.9992 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 1 de 1) |
| Número de Autorizaciones | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco. Según la información conocida, inotersen es un oligonucleótido antisentido 2'-O-metoxietilo que se dirige al ARNm de la transtiretina (TTR), expresada principalmente en el hígado. Su efecto es disminuir la producción de la proteína TTR.

La porfiria aguda intermitente es un trastorno hepático en el que la biosíntesis del grupo hemo está desregulada y puede causar neuropatía. Existen terapias dirigidas al ARN para esta enfermedad (por ejemplo, givosirán, un ARNip contra ALAS1), por lo que el silenciamiento génico hepático tiene una justificación conceptual.

Sin embargo, la diana de inotersen (TTR) no está vinculada mecanísticamente con la vía de las porfirinas. La única publicación disponible es una revisión general sobre trastornos neuromusculares genéticos y sus terapias, que aporta apoyo indirecto a nivel de clase. El puntaje alto de TxGNN probablemente refleja características de red compartidas (neuropatía y terapias con oligonucleótidos) más que un vínculo biológico directo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30847674](https://pubmed.ncbi.nlm.nih.gov/30847674/) | 2019 | Revisión | Neurological Sciences | Revisión de terapias nuevas y ya disponibles para trastornos neuromusculares genéticos, en particular neuropatías periféricas como la amiloidosis hereditaria por transtiretina (hATTR). No aborda directamente la porfiria aguda intermitente. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1181296002 | TEGSEDI 284 MG SOLUCIÓN INYECTABLE EN JERINGA PRECARGADA | Solución inyectable en jeringa precargada | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proviene del prospecto)**: trombocitopenia y glomerulonefritis.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones registradas. Entre las principales, de nivel **Mayor**:
  - Anfotericina B (incluidas las formulaciones lipídicas, de sulfato de colesterilo y liposomal)
  - Aminoglucósidos: kanamicina, neomicina, estreptomicina
  - Polimixina B y vancomicina
  - Antiinflamatorios y salicilatos: ácido acetilsalicílico, mesalazina, balsalazida, olsalazina, sulfasalazina
  - Ácido iotalámico

  De nivel **Moderado**: dexfenfluramina, fenfluramina, exenatida, naltrexona y sibutramina.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto en TxGNN, pero carece de ensayos clínicos y de un vínculo mecanístico directo entre la diana (TTR) y la vía del hemo. La única publicación es una revisión general con apoyo indirecto. Además, el perfil de riesgo (trombocitopenia y glomerulonefritis) exige cautela. Por ahora debe tratarse como una pregunta de investigación.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias, contraindicaciones e indicación aprobada).
- Completar los datos del mecanismo de acción desde DrugBank.
- Estudios preclínicos que evalúen si la reducción de TTR influye en la vía del hemo o en la neuropatía de la porfiria.
- Comparar con terapias ya establecidas, como givosirán.
- Evaluar la relación beneficio-riesgo, dado el riesgo de trombocitopenia y glomerulonefritis.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

