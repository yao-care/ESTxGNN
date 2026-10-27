---
layout: default
title: Clobetasone
parent: Solo predicción del modelo (L5)
nav_order: 193
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Clobetasone: nueva indicación predicha, Linfoma cutáneo primario de células T (nivel de evidencia L5). Indicación original: No disponible en los datos de la autorización de AEMPS (texto de indi…"
monitor_inn: "clobetasone"
predicted_indications: ["primary cutaneous T-cell lymphoma", "Sezary syndrome", "primary cutaneous B-cell lymphoma", "granulomatous slack skin disease", "Crohn's colitis", "adrenocortical insufficiency", "primary cutaneous T-cell non-Hodgkin lymphoma", "nephrotic syndrome", "cystic teratoma", "spinal cord dermoid cyst"]
---

# Clobetasone
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

## Clobetasona: De Corticoide Tópico a Linfoma Cutáneo Primario de Células T
{: .text-alpha }

## Resumen en Una Frase

Clobetasona es un corticoide tópico de potencia moderada, comercializado en España en forma de crema (EMOVATE CREMA). El modelo TxGNN predice que podría ser efectivo para el **linfoma cutáneo primario de células T**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo con un racional mecanístico indirecto, basado en la clase farmacológica.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de la autorización de AEMPS (texto de indicación vacío) |
| Nueva Indicación Predicha | Linfoma cutáneo primario de células T |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L4 (según la clasificación asignada en los datos; no hay estudios clínicos ni publicaciones aportados) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de clobetasona. Según la información conocida, clobetasona es un corticoide tópico de potencia moderada. Los corticoides tópicos ejercen efectos antiinflamatorios y linfocitolíticos a través de la señalización del receptor de glucocorticoides.

En el linfoma cutáneo primario de células T, en particular en la micosis fungoide en estadio temprano (placas y parches), los corticoides tópicos de mayor potencia se utilizan como terapia dirigida a la piel. Por ello, existe un racional de clase plausible: la acción linfocitolítica y antiinflamatoria podría ser aplicable a esta enfermedad, y la vía de administración cutánea es coherente con la localización de las lesiones.

Es importante subrayar que el vínculo es **indirecto y basado en la clase farmacológica**. No se han aportado datos específicos de clobetasona en esta enfermedad, y la única señal propia del fármaco es el puntaje elevado de TxGNN. Además, clobetasona es de potencia moderada, inferior a los corticoides de alta potencia empleados habitualmente en este contexto.

## Otras Indicaciones Predichas (Resumen)

Además de la predicción principal, el modelo generó otras predicciones, todas sin ensayos clínicos ni literatura:

| Enfermedad | Puntaje TxGNN | Nivel | Recomendación | Valoración |
|------|------|------|------|------|
| Linfoma cutáneo primario de células T no Hodgkin | 99.70% | L4 | Pregunta de investigación | Categoría que se solapa con la predicción principal; racional de clase indirecto |
| Síndrome de Sézary | 99.78% | L5 | Hold | Enfermedad leucémica y sistémica; un agente tópico de potencia moderada ofrecería, como mucho, alivio sintomático |
| Linfoma cutáneo primario de células B | 99.77% | L5 | Hold | Los corticoides tópicos no son terapia establecida (se emplean escisión, radioterapia y rituximab) |
| Enfermedad de la piel laxa granulomatosa | 99.74% | L5 | Hold | Racional genérico; probablemente refleja proximidad en la red a otros linfomas cutáneos |
| Colitis de Crohn | 99.72% | L5 | Hold | Fármaco tópico con baja exposición sistémica y sin formulación intestinal |
| Insuficiencia suprarrenal | 99.71% | L5 | Hold | El uso prolongado puede causar supresión del eje HHA; es un asunto de seguridad, no una oportunidad |
| Síndrome nefrótico | 99.69% | L5 | Hold | Biodisponibilidad sistémica mínima; no alcanza la exposición requerida |
| Teratoma quístico | 99.65% | L5 | Hold | Sin racional plausible; probable artefacto del grafo |
| Quiste dermoide de médula espinal | 99.65% | L5 | Hold | Sin racional plausible; probable artefacto de asociaciones en la red |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 56273 | EMOVATE CREMA | Crema | No especificada en los datos |

Titular: Nutrición Médica S.L. Estado: vigente (monofármaco).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como consideración derivada de la clase farmacológica: el uso prolongado de corticoides tópicos puede provocar supresión del eje hipotálamo-hipófisis-suprarrenal, lo que es relevante si se contemplara un uso extendido o sobre grandes superficies en enfermedades cutáneas crónicas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo (99.97%) y en un racional de clase indirecto; no hay ensayos clínicos ni publicaciones específicos de clobetasona, y la indicación original no figura en los datos de la autorización disponible. Entre las predicciones, el linfoma cutáneo primario de células T es la más plausible, pero debe tratarse como una pregunta de investigación.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias, contraindicaciones e indicación aprobada), actualmente ausente.
- Completar los datos del mecanismo de acción desde DrugBank.
- Revisión sistemática de la literatura sobre corticoides tópicos de potencia moderada en micosis fungoide temprana, comparando con corticoides de alta potencia.
- Evaluar la compatibilidad de la vía de administración y la relación con la indicación original (aún pendientes).
- Valorar un estudio exploratorio o preclínico antes de cualquier avance clínico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

