---
layout: default
title: Sulthiame
parent: Solo predicción del modelo (L5)
nav_order: 755
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Sulthiame: nueva indicación predicha, Síndrome de la cola de caballo (cauda equina syndrome) (nivel de evidencia L5). Indicación original: No disponible en los datos de la autorización de AEMPS"
monitor_inn: "sulthiame"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome", "neurocirculatory asthenia", "anaphylaxis", "food-dependent exercise-induced anaphylaxis", "familial mitral valve prolapse", "mitral valve prolapse (disease)", "MVP1", "autonomic nervous system disease"]
---

# Sulthiame
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

# Sultiamo: De Indicación Original No Especificada a Síndrome de la Cola de Caballo

## Resumen en Una Frase

Sultiamo es un inhibidor de la anhidrasa carbónica comercializado en España como suspensión oral (OSPOLOT 20 mg/ml), pero los datos compilados para este informe no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de la cola de caballo**, con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de la autorización de AEMPS |
| Nueva Indicación Predicha | Síndrome de la cola de caballo (cauda equina syndrome) |
| Puntaje de Predicción TxGNN | 99,97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, el sultiamo es un inhibidor de la anhidrasa carbónica. Sin embargo, los datos compilados no documentan su eficacia en una indicación original concreta, y no se ha establecido una vía plausible hacia la nueva indicación.

El síndrome de la cola de caballo es una afección neurológica compresiva, de manejo habitualmente quirúrgico. No hay evidencia en los datos de que un inhibidor de la anhidrasa carbónica tenga un papel en ella. La similitud con la indicación original queda pendiente de evaluar.

El puntaje de TxGNN (0,9997) es una predicción basada en el grafo de conocimiento y no constituye prueba de eficacia. Hay que interpretarlo con cautela.

### Otras indicaciones predichas (referencia)

| Rango | Enfermedad | Puntaje TxGNN | Nivel de Evidencia | Recomendación |
|---|---|---|---|---|
| 2 | Vejiga neurógena (término obsoleto) | 99,94% | L5 | Hold |
| 3 | Síndrome del intestino irritable | 99,86% | L5 | Hold |
| 4 | Astenia neurocirculatoria | 99,79% | L5 | Hold |
| 5 | Anafilaxia | 99,72% | L5 | Hold |
| 6 | Anafilaxia inducida por ejercicio dependiente de alimentos | 99,62% | L5 | Hold |
| 7 | Prolapso de la válvula mitral familiar | 99,49% | L5 | Hold |
| 8 | Prolapso de la válvula mitral | 99,48% | L5 | Hold |
| 9 | MVP1 | 99,43% | L5 | Hold |
| 10 | Enfermedad del sistema nervioso autónomo | 99,35% | L5 | Hold |

Ninguna cuenta con ensayos clínicos ni literatura. Varias se solapan entre sí (las tres de prolapso mitral y las relacionadas con anafilaxia), por lo que probablemente reflejan la misma señal del grafo y no evidencia independiente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 89631 | OSPOLOT 20 MG/ML SUSPENSIÓN ORAL | Suspensión oral | No especificada en los datos |

Titular: Desitin Arzneimittel GmbH. Autorización vigente, de tipo monofármaco.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

No se encontraron interacciones farmacológicas registradas en la consulta realizada.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5), sin ensayos, sin literatura y sin vínculo mecanístico plausible. Además, faltan los datos de seguridad y la indicación original aprobada, por lo que no es posible avanzar.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), que es un requisito bloqueante para el cribado de seguridad.
- Completar el mecanismo de acción desde DrugBank y analizar su relación con la nueva indicación.
- Confirmar la indicación original aprobada del producto.
- Realizar una revisión sistemática de la literatura y de registros de ensayos para el síndrome de la cola de caballo.
- Evaluar la compatibilidad de la vía de administración (actualmente solo oral) con las necesidades de la nueva indicación.
- Valorar si alguna de las otras indicaciones predichas tiene una justificación farmacológica más sólida, dado que las predicciones de mayor rango no tienen respaldo mecanístico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

