---
layout: default
title: Linaclotide
parent: Solo predicción del modelo (L5)
nav_order: 471
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Linaclotide: nueva indicación predicha, Síndrome de la cola de caballo (nivel de evidencia L5). Indicación original: Síndrome del intestino irritable (según el grafo de conocimiento"
monitor_inn: "Linaclotide"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "insomnia (disease)"]
---

# Linaclotide
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

# Linaclotida: De Síndrome del Intestino Irritable a Síndrome de la Cola de Caballo

## Resumen en Una Frase

Linaclotida es un agonista de la guanilato ciclasa-C, utilizado originalmente para el tratamiento del síndrome del intestino irritable (con estreñimiento) y el estreñimiento crónico.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de la cola de caballo**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Síndrome del intestino irritable (según el grafo de conocimiento; el texto de indicación autorizado en España no está disponible) |
| Nueva Indicación Predicha | Síndrome de la cola de caballo |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Linaclotida es un agonista de la guanilato ciclasa-C (GC-C, gen GUCY2C) que actúa localmente sobre el epitelio intestinal y se absorbe de forma mínima a nivel sistémico. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción, pero la farmacología conocida indica que su uso clínico se centra en el estreñimiento crónico y el síndrome del intestino irritable con estreñimiento (SII-E).

El síndrome de la cola de caballo es un trastorno neurológico por compresión de las raíces nerviosas lumbosacras, que provoca disfunción intestinal y vesical, incluido el estreñimiento neurógeno. Teóricamente, linaclotida podría aliviar el síntoma intestinal (estreñimiento) secundario a esta condición, pero **no actuaría sobre la compresión nerviosa de fondo**.

No se identificó un vínculo mecanístico directo con la patología de la enfermedad. El puntaje tan alto (99.96%) es solo una predicción del modelo y probablemente refleja asociaciones a nivel de síntomas (estreñimiento, disfunción intestinal) y no un efecto modificador de la enfermedad. Por ello, esta predicción debe interpretarse como potencial uso sintomático.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 112801002 | Constella 290 microgramos cápsulas duras | Cápsula dura | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta se completó y solo se registró una interacción de tipo farmacológico (no una interacción con otro medicamento): la unión de linaclotida con su diana, la guanilato ciclasa-C (GUCY2C), que corresponde a su mecanismo de acción. No se identificaron interacciones con otros fármacos con nivel de gravedad asignado.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico directo con la patología de la enfermedad. El beneficio plausible se limitaría al alivio sintomático del estreñimiento neurógeno.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones autorizadas)
- Completar los datos del mecanismo de acción desde DrugBank
- Buscar evidencia clínica o preclínica en estreñimiento neurógeno o disfunción intestinal por lesión de la cola de caballo
- Definir si el objetivo sería únicamente sintomático (manejo del intestino neurógeno) y evaluar su relevancia clínica
- Evaluar la compatibilidad de la vía de administración (oral) con el escenario clínico propuesto
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

