---
layout: default
title: Dantrolene
parent: Solo predicción del modelo (L5)
nav_order: 155
evidence_level: L5
indication_count: 9
---

# Dantrolene
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

# Dantroleno: De Relajante Muscular a Hipertermia Maligna (Susceptibilidad)

## Resumen en Una Frase

Dantroleno es un relajante muscular de acción directa sobre el músculo esquelético, utilizado en crisis de hipertermia maligna.
El modelo TxGNN predice que podría ser efectivo para **hipertermia maligna, susceptibilidad a**, con un puntaje del 99,93 %.
Actualmente no hay **ensayos clínicos** ni **publicaciones** asociados a esta indicación en el conjunto de datos, por lo que el respaldo proviene del mecanismo farmacológico conocido.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Hipertermia maligna, susceptibilidad a |
| Puntaje de Predicción TxGNN | 99,93 % |
| Nivel de Evidencia | L4 (solo mecanismo farmacológico; sin ensayos ni literatura en los datos) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Dantroleno actúa sobre los receptores de rianodina, en particular **RyR1** (gen *RYR1*) y **RyR3** (gen *RYR3*), según los datos farmacológicos disponibles. RyR1 es el canal que libera calcio desde el retículo sarcoplásmico en el músculo esquelético. Al inhibir esta liberación, el fármaco reduce la contracción muscular sostenida y la respuesta hipermetabólica.

La hipertermia maligna es un trastorno farmacogenético del músculo esquelético. Las mutaciones de *RYR1* provocan una liberación descontrolada de calcio cuando el paciente se expone a anestésicos volátiles o a relajantes musculares despolarizantes. La relación entre el mecanismo del fármaco y la fisiopatología de la enfermedad es directa, y el puntaje alto del modelo es coherente con ella.

Los datos farmacológicos indican que dantroleno se usa en crisis de hipertermia maligna y de forma perioperatoria para prevenirlas. También indican que una formulación de dantroleno sódico hemiheptahidrato fue aprobada por la EMA en mayo de 2024. Es probable que esta predicción describa un uso ya establecido y no un reposicionamiento nuevo. El texto de indicación de la autorización española no consta en los datos, así que conviene verificarlo con la ficha técnica vigente antes de tratarlo como uso aprobado.

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
| 1241805001 | AGILUS 120 MG POLVO PARA SOLUCIÓN INYECTABLE (Norgine B.V.) | Polvo para solución inyectable | No consta en los datos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El mecanismo (inhibición de RyR1) coincide con la causa de la enfermedad y el puntaje del modelo es muy alto. Sin embargo, los datos no incluyen ensayos, literatura, indicación autorizada ni información de seguridad, por lo que no se puede confirmar el uso con la evidencia proporcionada.

**Para avanzar se necesita:**
- Obtener el prospecto o ficha técnica de AEMPS de AGILUS para confirmar la indicación autorizada, las advertencias y las contraindicaciones.
- Completar los datos del mecanismo de acción y de la indicación original del fármaco.
- Recopilar literatura clínica específica sobre dantroleno en hipertermia maligna, con la que ahora no se cuenta.
- Aclarar si esta predicción es un uso ya aprobado o un reposicionamiento genuino.

**Otras predicciones del modelo (no evaluadas en este informe):** el síndrome de King-Denborough, la enfermedad del núcleo central y otras miopatías relacionadas con *RYR1* tienen literatura que respalda solo el riesgo de hipertermia maligna, no un beneficio de dantroleno sobre la miopatía. Las parálisis periódicas tienen una vinculación solo especulativa y una posible preocupación por debilidad muscular. Ninguna se recomienda avanzar por ahora.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

