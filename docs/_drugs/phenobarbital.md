---
layout: default
title: Phenobarbital
parent: Solo predicción del modelo (L5)
nav_order: 631
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
monitor_inn: "Phenobarbital"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
description: "Phenobarbital: nueva indicación predicha, Neoplasia del nervio trigémino (trigeminal nerve neoplasm) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Phenobarbital
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

## Phenobarbital: Neoplasia del nervio trigémino (trigeminal nerve neoplasm)
{: .text-alpha }

## Resumen en Una Frase

Fenobarbital es un barbitúrico anticonvulsivo utilizado originalmente para el tratamiento de la epilepsia (incluidas las crisis tónico-clónicas generalizadas, la epilepsia parcial y el síndrome de Lennox-Gastaut) y de algunas cefaleas.
El modelo TxGNN predice que podría ser efectivo para **neoplasia del nervio trigémino**, pero **no hay ensayos clínicos** y solo **1 publicación** (una serie de casos sobre el síndrome de Sturge-Weber, no relacionada directamente con la indicación), por lo que la evidencia es esencialmente nula.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Neoplasia del nervio trigémino (trigeminal nerve neoplasm) |
| Puntaje de Predicción TxGNN | 0.9996 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 3 de 4) |
| Número de Autorizaciones | 4 (vigentes: 3) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, el fenobarbital es un modulador alostérico positivo del receptor GABA-A con actividad anticonvulsiva de amplio espectro. Además, la base de datos farmacológica lo registra como ligando del receptor X de pregnano (NR1I2), lo que explica su efecto inductor enzimático.

**En este caso la predicción no es creíble.** La neoplasia del nervio trigémino es un tumor, y no existe un vínculo mecanístico creíble con el fenobarbital: como mucho podría controlar crisis asociadas, pero no trataría el tumor. La única publicación recuperada (PMID 9157801) trata del síndrome de Sturge-Weber, que es otra enfermedad. El puntaje alto proviene del modelo TxGNN (deep learning) y probablemente refleja similitudes que el modelo aprendió entre enfermedades relacionadas (epilepsia y trigémino), no evidencia biológica.

**Otras predicciones del modelo.** Entre las candidatas posteriores predominan las epilepsias reflejas (crisis por alimentación, sobresalto, audiógenas, lectura, etc.), que son extensiones de la clase anticonvulsiva ya cubierta por las indicaciones existentes, y sin evidencia directa de eficacia. La neuralgia del trigémino (puntaje 0,9988) tiene como tratamiento de referencia la carbamazepina, no el fenobarbital.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Serie de casos | Anales Españoles de Pediatría | Revisión de 14 casos de síndrome de Sturge-Weber en un centro durante 25 años (características clínicas, evolución y respuesta terapéutica). No aborda la neoplasia del nervio trigémino. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 35052 | LUMINAL 100 MG COMPRIMIDOS | Comprimido | No disponible |
| 3275 | LUMINALETAS 15 MG COMPRIMIDOS | Comprimido | No disponible |
| 49002 | GARDENAL 50 mg COMPRIMIDOS | Comprimido | No disponible |
| 3905 | LUMINAL 200 MG/ML SOLUCIÓN INYECTABLE | Solución inyectable | No disponible |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proceden del prospecto):** insuficiencia y enfermedad hepática, enfermedad renal, porfiria (incluida la porfiria hereditaria), enfermedad pulmonar obstructiva crónica, trombocitopenia, hipotiroidismo/mixedema, hiperglucemia, lupus eritematoso sistémico, úlcera gástrica/péptica y gastritis, hipertensión, enfermedad de la vesícula biliar, y trastornos de ansiedad, neuróticos, distímicos y psicóticos.
- **Interacciones farmacológicas:** se registra la interacción farmacológica con el receptor X de pregnano (NR1I2), lo que apunta a inducción enzimática y posibles interacciones con otros fármacos metabolizados por esa vía. No se dispone de una lista de fármacos con nivel de gravedad.
- **Señales de seguridad en la literatura recuperada:** riesgos teratogénicos y cognitivos de los anticonvulsivos, deterioro cognitivo tardío tras la exposición temprana (PMID 10416094) y apoptosis neuronal en modelos animales neonatales.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para neoplasia del nervio trigémino carece de ensayos clínicos, de literatura relevante y de un vínculo mecanístico creíble; el puntaje elevado proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. El nivel de evidencia es L5.

**Para avanzar se necesita:**
- Datos de advertencias y contraindicaciones del prospecto de la AEMPS (lagunas de seguridad que bloquean el cribado).
- Datos detallados del mecanismo de acción (MOA).
- Evidencia preclínica o clínica directa en tumores del trigémino; de lo contrario, no se recomienda priorizar esta indicación.
- Si se busca reposicionamiento dentro de la neurología, valorar candidatas con más sustento (por ejemplo, epilepsias reflejas), teniendo en cuenta que son extensiones de clase y que existe evidencia de riesgo cognitivo en edades tempranas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

