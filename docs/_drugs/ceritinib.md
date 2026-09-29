---
layout: default
title: Ceritinib
parent: Solo predicción del modelo (L5)
nav_order: 115
evidence_level: L5
indication_count: 10
---

# Ceritinib
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

# Ceritinib: De Cáncer de Pulmón No Microcítico ALK-positivo a Fibromatosis Gingival

## Resumen en Una Frase

Ceritinib es un inhibidor de la quinasa ALK (y ROS1) comercializado en España como Zykadia, y en la literatura recuperada se utiliza en el cáncer de pulmón no microcítico (CPNM) con reordenamiento ALK.
El modelo TxGNN predice que podría ser efectivo para **fibromatosis gingival**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CPNM ALK-positivo (deducido de la literatura y del razonamiento del paquete de evidencia; el texto de indicación de la autorización está vacío) |
| Nueva Indicación Predicha | Fibromatosis gingival |
| Puntaje de Predicción TxGNN | 99.86% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, ceritinib es un inhibidor de tirosina quinasa dirigido contra ALK y ROS1. Su eficacia en el CPNM con reordenamiento ALK está documentada, por ejemplo en el ensayo aleatorizado de fase 3 ASCEND-4, citado en la literatura recuperada para otras indicaciones predichas.

No se encontró ningún vínculo mecanístico entre la inhibición de ALK/ROS1 y la fibromatosis gingival. No hay patología dependiente de ALK documentada en esta enfermedad, que es un sobrecrecimiento benigno del tejido gingival. La relación con la indicación original es "pendiente" de análisis.

El puntaje de 99.86% proviene solo de una predicción basada en grafos de conocimiento (posición 3179 en el ranking del modelo). Ningún ensayo ni publicación lo respalda. Por tanto, este puntaje alto **no** debe interpretarse como evidencia de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 115999001 | ZYKADIA 150 MG CAPSULAS DURAS (Novartis Europharm Limited) | Cápsula dura | No consta en el texto de la autorización |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa ALK/ROS1) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (nivel L5), sin ensayos clínicos, sin literatura y sin un vínculo mecanístico plausible entre ALK y la fibromatosis gingival. Además, ceritinib es un fármaco oncológico y la enfermedad es benigna, lo que exigiría una justificación sólida de la relación beneficio-riesgo antes de avanzar.

**Para avanzar se necesita:**
- Datos de mecanismo de acción (MOA) desde DrugBank y una hipótesis biológica que conecte ALK/ROS1 con la fibromatosis gingival (por ejemplo, expresión o alteración de ALK en tejido gingival).
- Estudios preclínicos que muestren alguna actividad en modelos de esta enfermedad.
- Ficha técnica de la AEMPS (advertencias y contraindicaciones), pendiente de descarga y análisis, para poder realizar el cribado de seguridad.
- Revisión manual de las demás indicaciones predichas. Solo "lung benign neoplasm" y "lung germ cell tumor" tienen literatura asociada, y es indirecta, centrada en el CPNM maligno y en otros tumores con ALK alterado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

