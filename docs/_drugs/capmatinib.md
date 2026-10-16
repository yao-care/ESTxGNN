---
layout: default
title: Capmatinib
parent: Solo predicción del modelo (L5)
nav_order: 140
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Capmatinib: nueva indicación predicha, Artritis reumatoide (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (los textos de indicación de la…"
---

# Capmatinib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Capmatinib: De Indicación Original No Especificada a Artritis Reumatoide

## Resumen en Una Frase

Capmatinib es un inhibidor selectivo de la tirosina quinasa MET, un fármaco oncológico comercializado en España como Tabrecta. En los datos compilados para este informe no consta el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **artritis reumatoide**, pero actualmente no hay **ningún ensayo clínico** y solo **1 publicación** (una revisión general de inhibidores de quinasas) relacionada, que no describe actividad de capmatinib en esta enfermedad.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Artritis reumatoide |
| Puntaje de Predicción TxGNN | 99,45% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este fármaco. Según la información conocida, capmatinib es un inhibidor selectivo de la tirosina quinasa del receptor MET, una clase de fármacos dirigidos usada en oncología.

La vía de MET se ha relacionado con la inflamación sinovial, la angiogénesis y la capacidad invasiva de los sinoviocitos tipo fibroblasto en la artritis reumatoide. Por ello existe un vínculo biológicamente plausible, aunque inferido del conocimiento general de la clase y no de datos propios del fármaco.

Es importante ser prudente: la única publicación disponible es una revisión general de inhibidores de proteína quinasas aprobados por la FDA, que no reporta actividad de capmatinib en artritis reumatoide. El puntaje alto de TxGNN (0,994) es una predicción computacional y no está respaldado por datos preclínicos ni clínicos para este par fármaco-enfermedad. Tampoco se ha podido establecer la similitud con la indicación original, al no disponerse de ella.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33513356](https://pubmed.ncbi.nlm.nih.gov/33513356/) | 2021 | Revisión | Pharmacological Research | Actualización 2021 de las propiedades de los inhibidores de proteína quinasas de molécula pequeña aprobados por la FDA (62 agentes, todos orales salvo netarsudil). No aborda capmatinib en artritis reumatoide |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1221650002 | Tabrecta 150 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 1221650004 | Tabrecta 200 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa MET) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; se muestran las de mayor gravedad entre las listadas:
  - **Mayor**: dexametasona, claritromicina.
  - **Moderada**: metformina, alosetrón, loperamida, aprepitant, empagliflozina, fenilbutirato de glicerol, metilnaltrexona, metreleptina, naldemedina, naltrexona.
  - **Menor**: inhibidores de la bomba de protones (rabeprazol, dexlansoprazol, esomeprazol, lansoprazol, omeprazol, pantoprazol), fidaxomicina, naloxegol.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo computacional (nivel L5), sin ensayos clínicos ni estudios preclínicos que respalden capmatinib en artritis reumatoide. Además, faltan datos básicos de indicación, mecanismo y seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas)
- Completar los datos del mecanismo de acción desde DrugBank
- Estudios preclínicos de inhibición de MET en modelos de artritis reumatoide (sinoviocitos, modelos animales)
- Evaluar la relación beneficio-riesgo de un inhibidor oncológico en una enfermedad inflamatoria crónica, incluyendo las interacciones relevantes (p. ej., corticoides como la dexametasona)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

