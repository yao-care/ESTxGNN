---
layout: default
title: Sacituzumab Govitecan
parent: Solo predicción del modelo (L5)
nav_order: 719
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Sacituzumab Govitecan: nueva indicación predicha, Osteoporosis inducida por fármacos (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (el texto de indicación de la …"
monitor_inn: "sacituzumab govitecan"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "diabetic cataract"]
---

# Sacituzumab Govitecan
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Sacituzumab govitecan: De Indicación Original No Disponible a Osteoporosis Inducida por Fármacos

## Resumen en Una Frase

Sacituzumab govitecan es un conjugado anticuerpo-fármaco dirigido a Trop-2 que porta SN-38 (inhibidor de la topoisomerasa I) y se utiliza en oncología; los datos compilados para este informe no incluyen el texto de su indicación aprobada en España.
El modelo TxGNN predice que podría ser efectivo para **osteoporosis inducida por fármacos**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.
Se trata de una predicción puramente computacional (nivel de evidencia L5).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (el texto de indicación de la autorización de la AEMPS está vacío); se utiliza en oncología |
| Nueva Indicación Predicha | Osteoporosis inducida por fármacos |
| Puntaje de Predicción TxGNN | 99,78 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados en los datos compilados. Según la información conocida, sacituzumab govitecan es un conjugado anticuerpo-fármaco dirigido a Trop-2 que libera SN-38, un inhibidor de la topoisomerasa I con acción citotóxica, y se emplea en oncología.

**No se ha establecido un vínculo mecanístico** con la osteoporosis inducida por fármacos. El puntaje de 99,78 % proviene únicamente de un grafo de conocimiento y no está respaldado por evidencia clínica ni bibliográfica. No existe una vía del metabolismo óseo que conecte este fármaco con la osteoporosis, y la quimioterapia citotóxica se asocia en general con pérdida ósea, no con protección.

Por ello, esta predicción debe considerarse una hipótesis sin respaldo mecanístico, y no una candidatura de reposicionamiento sólida.

### Otras predicciones del modelo

Las demás indicaciones predichas tampoco cuentan con ensayos ni literatura, y su nivel de evidencia es L5 con recomendación Hold:

| Posición | Indicación predicha | Puntaje TxGNN | Comentario |
|------|------|------|------|
| 2 | Retinopatía diabética no proliferativa grave | 99,69 % | Sin vínculo mecanístico; la toxicidad sistémica (neutropenia, diarrea) desaconseja su uso en una enfermedad crónica no maligna |
| 3 | Retinopatía diabética | 99,60 % | Trop-2 y la citotoxicidad de SN-38 no son relevantes para su fisiopatología; balance riesgo-beneficio desfavorable |
| 4 | Catarata diabética | 99,12 % | El fármaco no actúa sobre la vía de los polioles, el estrés oxidativo ni la glicación del cristalino |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1211592001 | TRODELVY 200 MG POLVO PARA CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Polvo para concentrado para solución para perfusión | No disponible en los datos compilados |

Titular: Gilead Sciences Ireland Unlimited Company.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Conjugado anticuerpo-fármaco (terapia dirigida a Trop-2) con carga citotóxica de SN-38, inhibidor de la topoisomerasa I |
| Riesgo de Mielosupresión | Alto (la neutropenia es una toxicidad sistémica señalada en los datos compilados); consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial; vigilancia de diarrea; función hepática y renal. Consultar el prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto; seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 40 interacciones. Entre las 20 detalladas en los datos compilados:
  - **Gravedad mayor**: deferiprona, fostamatinib, adalimumab, apalutamida, certolizumab pegol, cladribina, dacomitinib, irinotecán, leflunomida, natalizumab, nilotinib y ozanimod.
  - **Gravedad moderada**: alefacept, alemtuzumab, anakinra, canakinumab, fumarato de dimetilo, lorlatinib, ocrelizumab y omacetaxina mepesuccinato.
  - Destaca la interacción mayor con **irinotecán**, ya que SN-38 es su metabolito activo.
  - Muchas de las interacciones mayores corresponden a fármacos inmunosupresores o mielosupresores, lo que sugiere riesgo aditivo de mielosupresión e infecciones.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L5), sin ensayos clínicos, literatura ni vínculo mecanístico, y el perfil de toxicidad de un citotóxico es desfavorable para una indicación no oncológica crónica.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicación aprobada), un vacío de datos bloqueante para el cribado de seguridad.
- Completar el mecanismo de acción desde DrugBank.
- Disponer de evidencia preclínica que respalde un vínculo biológico con la osteoporosis inducida por fármacos.
- Evaluar la compatibilidad de la vía de administración y la relación con la indicación original, hoy pendientes.
- Valorar si alguna de las otras predicciones tiene más plausibilidad; con los datos actuales ninguna la muestra.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

