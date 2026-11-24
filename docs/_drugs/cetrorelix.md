---
layout: default
title: Cetrorelix
parent: Solo predicción del modelo (L5)
nav_order: 167
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Cetrorelix: nueva indicación predicha, Hipertricosis (nivel de evidencia L5). Indicación original: Inhibición de picos prematuros de LH en estimulación ovárica controla…"
monitor_inn: "CETRORELIX"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "persistent fetal circulation syndrome", "familial isolated trichomegaly", "familial male-limited precocious puberty", "aromatase excess syndrome", "centra precocious puberty 1"]
---

# Cetrorelix
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

## Cetrorelix: De Inhibición de Picos Prematuros de LH en Estimulación Ovárica a Hipertricosis
{: .text-alpha }

## Resumen en Una Frase

Cetrorelix es un antagonista del receptor de GnRH, utilizado para inhibir los picos prematuros de LH en mujeres sometidas a estimulación ovárica controlada como parte de un tratamiento de fertilidad.
El modelo TxGNN predice que podría ser efectivo para **hipertricosis**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Inhibición de picos prematuros de LH en estimulación ovárica controlada (según datos farmacológicos; los textos de indicación de las autorizaciones españolas están vacíos) |
| Nueva Indicación Predicha | Hipertricosis |
| Puntaje de Predicción TxGNN | 0.9998 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 4; autorizadas no comercializadas: 2; revocadas o suspendidas: 1) |
| Número de Autorizaciones | 4 (comercializadas: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Cetrorelix es un antagonista del receptor de GnRH (receptor GnRH₁, gen GNRHR). Al bloquearlo, suprime la liberación de LH y FSH y, por tanto, la producción gonadal de andrógenos. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción, pero esta es la función farmacológica conocida del fármaco.

Existe un vínculo teórico con el crecimiento de vello de tipo hirsutismo mediante la reducción de andrógenos. Sin embargo, la hipertricosis en general no depende de andrógenos, por lo que el vínculo es débil. El alto puntaje proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni terapéutica.

Conviene subrayar que esta predicción es de baja plausibilidad mecanística. Las demás predicciones de mayor rango (síndrome de Ambras, malformaciones, anomalías del tallo piloso, tricomegalia familiar, circulación fetal persistente) tampoco tienen un mecanismo creíble. Solo dos predicciones de menor rango, la pubertad precoz central y la pubertad precoz familiar limitada a varones, pertenecen a un área biológicamente relacionada con la farmacología de cetrorelix. En la primera el mecanismo es coherente, pero el estándar de tratamiento son los agonistas de GnRH y la formulación de cetrorelix, de acción corta y pensada para FIV, limita su uso crónico pediátrico. En la segunda el mecanismo argumenta en contra del beneficio.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 85838 | CEZIBOE 0,25 MG SOLUCION INYECTABLE EN JERINGA PRECARGADA | SOLUCIÓN INYECTABLE EN JERINGA PRECARGADA | Sun Pharmaceutical Industries (Europe) B.V. | Comercializada |
| 99100002 | CETROTIDE 0,25 mg POLVO Y DISOLVENTE PARA SOLUCION INYECTABLE | POLVO Y DISOLVENTE PARA SOLUCIÓN INYECTABLE | Merck Europe B.V. | Autorizada, no comercializada |
| 99100001 | CETROTIDE 0,25 mg POLVO Y DISOLVENTE PARA SOLUCION INYECTABLE | POLVO Y DISOLVENTE PARA SOLUCIÓN INYECTABLE | Merck Europe B.V. | Autorizada, no comercializada |
| 85740 | CETRORELIX EDEST 0,25 MG POLVO PARA SOLUCION INYECTABLE | POLVO PARA SOLUCIÓN INYECTABLE | Intas Third Party Sales 2005 S.L. | Revocada |

Se muestran las 4 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como dato farmacológico, el único registro de interacción disponible corresponde a la unión de cetrorelix a su diana, el receptor GnRH₁, y no a una interacción con otros fármacos.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para hipertricosis es solo del modelo (nivel L5), sin ensayos ni literatura, y con un vínculo mecanístico débil, ya que la hipertricosis generalmente no depende de andrógenos. No hay base para avanzar en esta indicación.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), actualmente sin datos y necesario para cualquier evaluación de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Completar los textos de indicación aprobada de las autorizaciones españolas.
- Realizar una revisión sistemática de literatura y de registros de ensayos sobre cetrorelix en hipertricosis o hirsutismo.
- Valorar priorizar la pubertad precoz central, que tiene un mecanismo coherente, aunque con evidencia aún de nivel de predicción y limitaciones prácticas por la formulación de acción corta.
- Evaluar la compatibilidad de la vía de administración (actualmente pendiente) y la similitud con la indicación original.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

