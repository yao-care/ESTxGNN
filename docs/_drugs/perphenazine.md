---
layout: default
title: Perphenazine
parent: Solo predicción del modelo (L5)
nav_order: 628
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Perphenazine: nueva indicación predicha, Distrofia retiniana con o sin anomalías extraoculares (nivel de evidencia L5). Indicación original: Esquizofrenia y trastorno mixto de ansiedad y depresión (s…"
monitor_inn: "perphenazine"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "syndromic myopia", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "hydranencephaly (disease)", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "myopia 26, X-linked, female-limited", "congenital disorder of glycosylation with defective fucosylation", "myopia X-linked", "atypical glycine encephalopathy", "anxiety disorder"]
---

# Perphenazine
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

# Perfenazina: De Esquizofrenia a Distrofia Retiniana con o sin Anomalías Extraoculares

## Resumen en Una Frase

La perfenazina es un antipsicótico fenotiazínico, utilizado originalmente para el tratamiento de la esquizofrenia y del trastorno mixto de ansiedad y depresión.
El modelo TxGNN predice que podría ser efectiva para **distrofia retiniana con o sin anomalías extraoculares**, pero **no hay ensayos clínicos** y solo **1 publicación**, que además describe un efecto adverso de otro fármaco, no un beneficio.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Esquizofrenia y trastorno mixto de ansiedad y depresión (según el grafo de conocimiento; el texto de indicación autorizado en España no está disponible) |
| Nueva Indicación Predicha | Distrofia retiniana con o sin anomalías extraoculares |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la perfenazina es una fenotiazina de alta potencia, cuya eficacia en esquizofrenia y en cuadros mixtos de ansiedad y depresión está establecida. No se ha podido establecer un vínculo mecanístico con la nueva indicación a partir de los datos compilados.

Los datos compilados no respaldan un vínculo mecanístico creíble. La única publicación disponible (PMID 14129300, de 1964) describe una retinopatía pigmentaria causada por **tioridazina**, otra fenotiazina. Es un reporte de efecto adverso, no una evidencia de beneficio. Sugiere que la toxicidad retiniana de las fenotiazinas es una preocupación de seguridad, no una justificación terapéutica.

El puntaje tan alto del modelo (99.96%) probablemente es un artefacto de la estructura del grafo de conocimiento y no está respaldado por datos clínicos. Debe interpretarse como una hipótesis sin sustento, no como una señal de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [14129300](https://pubmed.ncbi.nlm.nih.gov/14129300/) | 1964 | Reporte de caso | The American Journal of Psychiatry | Retinopatía pigmentaria asociada a tioridazina (otro fármaco) con una dosis diaria máxima de 1400 mg. Es un reporte de efecto adverso, no de beneficio terapéutico. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 29406 | DECENTAN 8 MG COMPRIMIDOS (Laboratorios Ern S.A.) | Comprimido | — |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad, no texto del prospecto): síndrome de QT largo (incluido el familiar) y torsades de pointes, paro cardíaco súbito, infarto de miocardio, hipotensión ortostática, epilepsia, enfermedades de los ganglios basales, enfermedad hepática, neutropenia, agranulocitosis, trombocitopenia, glaucoma de ángulo abierto, hiperplasia benigna de próstata, trastorno bipolar maníaco, hiperglucemia, abuso o dependencia de sustancias, entre otras.
- **Interacciones farmacológicas**: se registraron 282 interacciones. Entre las de nivel **mayor** figuran bupropión, morfina y citrato de potasio. Entre las de nivel **moderado** figuran acarbosa, famotidina, epinefrina, metformina, pioglitazona, atropina, claritromicina y loperamida, entre otras.
- **Seguridad ocular**: las fenotiazinas se asocian a toxicidad retiniana (ver PMID 14129300), lo que va en contra de un posible uso en enfermedades de la retina.
- Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5): no hay ensayos clínicos, la única publicación describe un efecto adverso de otro fármaco, y no existe un mecanismo plausible. Además, la toxicidad retiniana de las fenotiazinas supone un riesgo de seguridad para esta indicación.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) del fármaco.
- Advertencias y contraindicaciones del prospecto de la AEMPS (hoy faltan).
- Evidencia preclínica que justifique un posible efecto en distrofias retinianas, y un análisis de la toxicidad retiniana.

**Nota:** entre las demás predicciones, **trastorno de ansiedad** (posición 10, puntaje 99.53%) tiene más respaldo: nivel L3, 1 ensayo de Fase 3 (farmacovigilancia en pacientes gerontopsiquiátricos, terminado, solo relevancia indirecta) y 20 publicaciones, sobre todo estudios antiguos con la combinación perfenazina-amitriptilina. Su recomendación en el análisis es "pregunta de investigación". Podría evaluarse como alternativa, aunque es cercana a una indicación ya existente.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

