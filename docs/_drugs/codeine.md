---
layout: default
title: Codeine
parent: Solo predicción del modelo (L5)
nav_order: 205
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
monitor_inn: "Codeine"
predicted_indications: ["nasal cavity disease", "trigeminal autonomic cephalalgia", "allergic urticaria"]
description: "Codeine: nueva indicación predicha, Enfermedad de la cavidad nasal (nasal cavity disease) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Codeine
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

## Codeine: Enfermedad de la cavidad nasal (nasal cavity disease)
{: .text-alpha }

## Resumen en Una Frase

La codeína es un opioide natural, comercializado en España en jarabes, soluciones orales y comprimidos, cuyas indicaciones originales en el conocimiento disponible incluyen rinitis alérgica, rinitis vasomotora, faringitis, resfriado común, nasofaringitis y cefalea.
El modelo TxGNN predice que podría ser efectiva para **enfermedad de la cavidad nasal**, con una puntuación muy alta (0,9993).
Sin embargo, no hay ensayos clínicos y la única publicación disponible es un reporte de caso que describe un hallazgo accidental, no un efecto terapéutico, por lo que la evidencia es de **nivel L5**.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Enfermedad de la cavidad nasal (nasal cavity disease) |
| Puntaje de Predicción TxGNN | 0.9993 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 4 de 6) |
| Número de Autorizaciones | 6 (vigentes: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la codeína es un agonista del receptor opioide μ (OPRM1), con uso clínico como analgésico, antitusígeno y antidiarreico.

La predicción del modelo TxGNN (deep learning) puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica: la codeína ya figura para rinitis, resfriado común y nasofaringitis, que afectan a la cavidad nasal. Esto sugiere una extensión de las indicaciones existentes más que una señal de reposicionamiento genuina.

Además, la única publicación recuperada describe un "opioma" (una rinolitiasis formada alrededor de una mezcla endurecida de codeína y opio), es decir, un hallazgo accidental asociado al fármaco, no un beneficio terapéutico. No hay evidencia de que la codeína sea útil para la enfermedad de la cavidad nasal como categoría.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | Reporte de caso | Ear, Nose, & Throat Journal | Varón de 21 años con rinolito unilateral formado alrededor de un cuerpo extraño compuesto por codeína y opio ("opioma"); se extrajo bajo anestesia local. No describe efecto terapéutico. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 65343 | Notusin solución oral | Solución oral | No disponible |
| 24797 | Histaverin 2 mg/ml jarabe | Jarabe | No disponible |
| 32357 | Toseína 2 mg/ml solución oral | Solución oral | No disponible |
| 5255 | Codeisan 1,26 mg/ml jarabe | Jarabe | No disponible |
| 1778 | Codeisan 28,7 mg comprimidos | Comprimido | No disponible |

Hay una sexta autorización vigente (20709, Fludan Codeína 10 mg/5 ml solución oral, Faes Farma). Las 6 autorizaciones son de monofármaco y están vigentes.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): hipertensión, insuficiencia hepática y hepatopatía, epilepsia, insomnio, EPOC, trastornos de ansiedad y neuróticos, distimia, porfiria, enfermedad renal, pancreatitis, enfermedad de la vesícula biliar, trombocitopenia, hipotiroidismo/mixedema, úlcera péptica, enfermedad inflamatoria intestinal, gastritis, trastornos psicóticos y esquizoafectivos, y dermatitis herpetiforme.
- **Interacciones farmacológicas**: solo consta la interacción farmacodinámica con el receptor μ opioide (OPRM1); no hay datos de interacciones con otros fármacos.
- **Señales de otras predicciones**: la codeína es un liberador no inmunológico de histamina de los mastocitos y puede provocar urticaria. Además, los opioides no se recomiendan en cefalea en racimos por su eficacia limitada y el riesgo de cefalea por abuso de medicación.

Para las advertencias y contraindicaciones del prospecto, consultar la ficha técnica de la AEMPS.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Pese a la puntuación alta del modelo, no existen ensayos clínicos y la única publicación es un reporte de caso sobre un hallazgo accidental, sin valor terapéutico. La predicción refleja la cercanía con las indicaciones ya existentes (rinitis, resfriado), no una nueva oportunidad.

Las otras indicaciones predichas tampoco respaldan el reposicionamiento: laringofaringitis aguda (L5, sin evidencia, extensión de indicaciones actuales), cefalea trigémino-autonómica (L4, evidencia indirecta y preocupación de seguridad) y urticaria alérgica (L4, la codeína la provoca, por lo que estaría mecanísticamente contraindicada).

**Para avanzar se necesita:**
- Obtener los textos de indicación y el prospecto de las autorizaciones de la AEMPS (advertencias y contraindicaciones), actualmente ausentes.
- Datos detallados del mecanismo de acción.
- Definir qué se entiende por "enfermedad de la cavidad nasal" y si existe un beneficio sintomático distinto de las indicaciones actuales.
- Estudios clínicos o revisiones sistemáticas que evalúen eficacia en patología nasal.
- Evaluación de compatibilidad de vías de administración y de la relación beneficio-riesgo de un opioide en esta población.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

