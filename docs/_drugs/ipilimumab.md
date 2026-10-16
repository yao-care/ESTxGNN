---
layout: default
title: Ipilimumab
parent: Solo predicción del modelo (L5)
nav_order: 429
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Ipilimumab: nueva indicación predicha, Coroideremia (nivel de evidencia L5). Indicación original: Melanoma metastásico"
monitor_inn: "IPILIMUMAB"
predicted_indications: ["choroideremia", "non-cutaneous melanoma"]
---

# Ipilimumab
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

# Ipilimumab: De Melanoma Metastásico a Coroideremia

## Resumen en Una Frase

Ipilimumab es un anticuerpo monoclonal que bloquea CTLA-4, utilizado originalmente para el tratamiento del melanoma metastásico.
El modelo TxGNN predice que podría ser efectivo para **coroideremia**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Melanoma metastásico |
| Nueva Indicación Predicha | Coroideremia |
| Puntaje de Predicción TxGNN | 99.06% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Ipilimumab bloquea el receptor CTLA-4 en los linfocitos T. Esto potencia su activación y su capacidad de atacar células tumorales, y es la base de su uso en melanoma. No se dispone de una descripción detallada del mecanismo de acción más allá de este bloqueo de CTLA-4.

**La relación mecanística con la coroideremia es muy débil.** La coroideremia es una degeneración retiniana hereditaria ligada al cromosoma X, causada por la pérdida de función del gen *CHM* (REP1). Su patología consiste en la degeneración progresiva del epitelio pigmentario de la retina, los fotorreceptores y la coroides. No depende de la evasión inmune tumoral, que es el proceso sobre el que actúa ipilimumab.

Además, la inhibición de puntos de control inmunitarios puede provocar eventos adversos oculares inmunomediados (por ejemplo, uveítis), lo que supondría un riesgo adicional en una retina ya vulnerable. La puntuación alta del modelo probablemente es un artefacto derivado de la estructura del grafo de conocimiento y no refleja una plausibilidad biológica real.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 11698001 | YERVOY 5 mg/ml concentrado para solución para perfusión | Concentrado para solución para perfusión | Bristol-Myers Squibb Pharma EEIG |
| 11698002 | YERVOY 5 mg/ml concentrado para solución para perfusión | Concentrado para solución para perfusión | Bristol-Myers Squibb Pharma EEIG |
| 11698001IP | YERVOY 5 mg/ml concentrado para solución para perfusión | Concentrado para solución para perfusión | Bristol-Myers Squibb Pharma EEIG |

Las tres autorizaciones están vigentes y corresponden a medicamentos de un único principio activo. Los datos compilados no incluyen el texto de la indicación aprobada para estas autorizaciones.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (anticuerpo monoclonal anti-CTLA-4); no es un citotóxico convencional |
| Riesgo de Mielosupresión | Bajo; el riesgo principal son los eventos adversos inmunomediados y no la supresión medular directa |
| Clasificación de Emetogenicidad | Baja |
| Items de Monitoreo | Hemograma, función hepática, función renal, función tiroidea y suprarrenal, glucemia; vigilancia de síntomas oculares, cutáneos y gastrointestinales |
| Protección en Manejo | Manejo estándar de preparados parenterales; consultar las advertencias y precauciones del prospecto |

Esta información se basa en conocimiento general de la clase farmacológica. Los datos compilados no incluyen datos específicos de toxicidad.

---

## Consideraciones de Seguridad

- **Riesgo ocular:** la inhibición de puntos de control inmunitarios puede causar eventos adversos oculares inmunomediados (por ejemplo, uveítis), un riesgo especialmente relevante en una retina ya degenerada.
- **Interacciones farmacológicas:** se identificaron 100 interacciones. Las principales entre las 20 revisadas son:
  - **Gravedad mayor:** anticoagulantes (apixabán, betrixabán, bivalirudina, dalteparina, desirudina, edoxabán, argatrobán, danaparoide).
  - **Gravedad moderada:** corticoides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida, prednisolona, prednisona), metronidazol, tinidazol, naltrexona, y estatinas (rosuvastatina, simvastatina).

Para el resto de la información de seguridad, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para coroideremia carece de ensayos clínicos y de literatura, y su nivel de evidencia es L5. Además, no existe un vínculo mecanístico plausible entre el bloqueo de CTLA-4 y una enfermedad degenerativa monogénica, y existe un riesgo ocular inmunomediado.

**Para avanzar se necesita:**
- Un fundamento biológico que justifique el uso de un inhibidor de puntos de control en una degeneración retiniana hereditaria. Hasta ahora no se ha identificado ninguno.
- Estudios preclínicos en modelos de coroideremia que evalúen eficacia y seguridad ocular.
- Revisión de las alternativas terapéuticas ya dirigidas a la causa de la enfermedad (por ejemplo, enfoques de terapia génica).
- Verificación del texto de indicaciones, advertencias y contraindicaciones en la ficha técnica vigente de la AEMPS.

**Nota adicional:** la segunda predicción del modelo para este fármaco, el **melanoma no cutáneo** (puntaje 99.02%), cuenta con mucha más evidencia: ensayos de Fase 2 y 3 en melanoma, incluida la combinación nivolumab + ipilimumab en melanoma uveal, y literatura clínica. Esta dirección parece una candidata mucho más sólida para una evaluación de reposicionamiento. Debe analizarse en un informe específico, ya que la evidencia depende del subtipo y los estudios de Fase 3 identificados corresponden sobre todo a melanoma cutáneo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

