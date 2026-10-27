---
layout: default
title: Regadenoson
parent: Solo predicción del modelo (L5)
nav_order: 688
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Regadenoson: nueva indicación predicha, Anafilaxia (nivel de evidencia L5). Indicación original: No disponible en la autorización de AEMPS (uso diagnóstico en MPI seg…"
monitor_inn: "regadenoson"
predicted_indications: ["anaphylaxis", "food-dependent exercise-induced anaphylaxis", "esotropia", "pseudoallergy"]
---

# Regadenoson
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

## Regadenoson: De Agente Diagnóstico de Estrés Farmacológico a Anafilaxia
{: .text-alpha }

## Resumen en Una Frase

Regadenoson es un agonista selectivo del receptor de adenosina A2A, utilizado como agente diagnóstico en la gammagrafía de perfusión miocárdica (MPI). El modelo TxGNN predice que podría ser efectivo para **anafilaxia**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en la autorización de AEMPS (uso diagnóstico en MPI según datos farmacológicos) |
| Nueva Indicación Predicha | Anafilaxia |
| Puntaje de Predicción TxGNN | 99.85% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción detallado. Según la información conocida, regadenoson actúa como agonista selectivo del receptor A2A de adenosina (también tiene afinidad registrada por los receptores A1, A2B y A3). Se utiliza como agente diagnóstico en la gammagrafía de perfusión miocárdica, donde provoca vasodilatación coronaria.

El vínculo teórico con la anafilaxia es que la señalización A2A puede suprimir la activación de mastocitos y otras células inflamatorias. Esto sugiere, de forma especulativa, un posible efecto modulador sobre la degranulación mastocitaria.

Sin embargo, existe una contradicción importante: regadenoson causa vasodilatación e hipotensión, lo que podría agravar el shock anafiláctico. Además, se administra como bolo único, lo que no encaja con un uso crónico o preventivo. El alto puntaje del modelo (0.998) no está respaldado por ninguna evidencia clínica en los datos disponibles.

**Otras predicciones del modelo (todas con nivel L5 y decisión Hold):**

| Indicación Predicha | Puntaje TxGNN | Comentario |
|------|------|------|
| Anafilaxia inducida por ejercicio dependiente de alimentos | 99.74% | Solo vínculo general antiinflamatorio A2A en mastocitos; el estrés hemodinámico y la vasodilatación plantean preocupación de seguridad |
| Esotropía | 99.12% | Sin vínculo mecanístico creíble; probable falso positivo (artefacto del grafo de conocimiento) |
| Pseudoalergia | 99.12% | Vínculo especulativo por inhibición de la degranulación mastocitaria; uso práctico limitado |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 110643001 | Rapiscan 400mcg solución inyectable (Ge Healthcare As) | Solución inyectable | Texto de indicación no disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proviene del prospecto):** el grafo de conocimiento TxGNN (PrimeKG) asocia el fármaco con contraindicaciones en las siguientes áreas:
  - Cardiovasculares: hipertensión, hipotensión, estenosis aórtica y valvulopatías aórticas, estenosis mitral, bloqueo auriculoventricular, síndrome del seno enfermo, enfermedad arterial coronaria, pericarditis, derrame pericárdico y hemopericardio, estenosis y trombosis carotídea, accidente isquémico transitorio e insuficiencia vertebrobasilar.
  - Respiratorias: asma (incluidas las formas intrínseca y alérgica), EPOC y enfermedad bronquial.
  - Neurológicas y autonómicas: epilepsia, enfermedades del sistema nervioso autónomo y síndrome de Horner.
- **Interacciones farmacológicas (6 de nivel moderado):** cafeína, dipiridamol, difilina, teofilina, aminofilina y oxtrifilina. Las metilxantinas y el dipiridamol pueden modificar la respuesta a los agonistas de adenosina.

Para el resto de la información de seguridad (advertencias y contraindicaciones oficiales), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa exclusivamente en el modelo (nivel L5), sin ensayos clínicos ni literatura. Además, el perfil farmacológico de regadenoson (vasodilatación, hipotensión, bolo único) es potencialmente contrario a las necesidades de la anafilaxia, y las contraindicaciones del grafo incluyen asma y trastornos cardiovasculares frecuentes en pacientes con riesgo anafiláctico.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias, contraindicaciones e indicación aprobada).
- Completar los datos del mecanismo de acción desde DrugBank.
- Estudios preclínicos que evalúen el efecto de la activación de A2A sobre mastocitos y modelos de anafilaxia, considerando la seguridad hemodinámica.
- Revisión sistemática de la literatura sobre agonistas A2A en enfermedades alérgicas.
- Evaluar la compatibilidad de la vía de administración y de la pauta (bolo único frente a necesidad terapéutica).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

