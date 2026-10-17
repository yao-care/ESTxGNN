---
layout: default
title: Pegvaliase
parent: Solo predicción del modelo (L5)
nav_order: 617
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Pegvaliase: nueva indicación predicha, Retinopatía diabética (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (los textos de indicación de la…"
monitor_inn: "pegvaliase"
predicted_indications: ["diabetic retinopathy", "severe nonproliferative diabetic retinopathy", "diabetic cataract"]
---

# Pegvaliase
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Pegvaliasa: De Indicación Original No Especificada a Retinopatía Diabética

## Resumen en Una Frase

Pegvaliasa es una enzima fenilalanina amoníaco liasa pegilada que degrada la fenilalanina y está comercializada en España con el nombre PALYNZIQ. Los datos compilados para este informe no incluyen el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **retinopatía diabética**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Retinopatía diabética |
| Puntaje de Predicción TxGNN | 99,17 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

Otras predicciones del modelo, con el mismo nivel de evidencia (L5) y recomendación (Hold):

| Indicación Predicha | Puntaje TxGNN |
|------|------|
| Retinopatía diabética grave no proliferativa | 99,16 % |
| Catarata diabética | 99,11 % |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, pegvaliasa es una fenilalanina amoníaco liasa pegilada que degrada la fenilalanina y está comercializada para la fenilcetonuria. No obstante, la indicación original no figura en los textos de autorización disponibles.

**Los datos compilados no respaldan un vínculo mecanístico** entre esta enzima y la retinopatía diabética. El puntaje elevado (99,17 %) es una predicción del grafo de conocimiento y no constituye evidencia clínica. Una hipótesis meramente especulativa sería que la alteración del metabolismo de aminoácidos influya en las vías vasculares o neurodegenerativas de la retina, pero no hay datos que la sustenten.

Las tres indicaciones predichas (retinopatía diabética, su forma grave no proliferativa y catarata diabética) son complicaciones diabéticas estrechamente relacionadas. Probablemente comparten una misma señal subyacente del grafo y **no deben considerarse evidencia independiente**. Tampoco se ha establecido una justificación biológica para la depleción de fenilalanina en enfermedad del cristalino o de la retina.

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
| 1191362004 | PALYNZIQ 20 mg solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada | No especificada en los datos disponibles |
| 1191362002 | PALYNZIQ 10 mg solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada | No especificada en los datos disponibles |
| 1191362001 | PALYNZIQ 2,5 mg solución inyectable en jeringa precargada | Solución inyectable | No especificada en los datos disponibles |

Titular de las tres autorizaciones: Biomarin International Limited (todas vigentes, de tipo monofármaco).

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 16 interacciones de nivel **moderado**. Corresponden en su mayoría a otros fármacos pegilados o proteínas terapéuticas:
  - Factores de coagulación: factor antihemofílico recombinante humano, factor IX de coagulación humano.
  - Productos pegilados: certolizumab pegol, pegaptanib (oftálmico), pegloticasa, pegademasa, pegaspargasa, pegfilgrastim, peginesatida, peginterferón alfa-2a, peginterferón alfa-2b, peginterferón beta-1a, pegvisomant.
  - Otros: doxorubicina liposomal, acetato de medroxiprogesterona, naloxegol.
- **Nota de precaución**: pegvaliasa conlleva riesgo de anafilaxia y requiere un manejo de riesgos estricto (tipo REMS), lo que sería una consideración de seguridad relevante para cualquier nuevo uso.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es exclusivamente computacional (nivel L5), sin ensayos clínicos ni publicaciones, y sin vínculo mecanístico respaldado por los datos. Además, el riesgo de anafilaxia exige cautela para cualquier nuevo uso.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicación aprobada).
- Completar los datos del mecanismo de acción (por ejemplo, mediante consulta a DrugBank).
- Realizar una revisión de literatura preclínica sobre el metabolismo de la fenilalanina en la retina y el cristalino.
- Evaluar la compatibilidad de la vía de administración con la enfermedad ocular propuesta (actualmente pendiente).
- Valorar si las tres predicciones representan una única señal del grafo antes de asignar recursos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

