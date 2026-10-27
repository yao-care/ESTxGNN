---
layout: default
title: Imidapril
parent: Solo predicción del modelo (L5)
nav_order: 407
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Imidapril: nueva indicación predicha, Hipertensión pulmonar secundaria a enfermedad pulmonar y/o hipoxia (nivel de evidencia L5). Indicación original: Hipertensión arterial (según el grafo de conocim…"
monitor_inn: "IMIDAPRIL"
predicted_indications: ["pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "Braddock syndrome"]
---

# Imidapril
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Imidapril: De Hipertensión a Hipertensión Pulmonar Secundaria a Enfermedad Pulmonar y/o Hipoxia
{: .text-alpha }

## Resumen en Una Frase

Imidapril es un inhibidor de la enzima convertidora de angiotensina (IECA) utilizado originalmente para el tratamiento de la hipertensión arterial.
El modelo TxGNN predice que podría ser efectivo para **hipertensión pulmonar secundaria a enfermedad pulmonar y/o hipoxia**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Hipertensión pulmonar secundaria a enfermedad pulmonar y/o hipoxia |
| Puntaje de Predicción TxGNN | 99.78% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 12 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Imidapril es un profármaco IECA cuyo metabolito activo, el imidaprilato, reduce la producción de angiotensina II. Esto puede disminuir la vasoconstricción y el remodelado vascular. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción del fármaco, por lo que este razonamiento se basa en la farmacología general de la clase de los IECA.

La hipertensión sistémica y la hipertensión pulmonar son ambas enfermedades vasculares con alteración del tono y del remodelado vascular, y el sistema renina-angiotensina podría participar en ambas. Sin embargo, en la hipertensión pulmonar por hipoxia los principales factores son la vasoconstricción pulmonar hipóxica y el remodelado, y los IECA no han mostrado un beneficio consistente en este contexto.

Por tanto, el puntaje alto de TxGNN (99.78%) debe interpretarse con cautela: es una señal computacional basada en el grafo de conocimiento, sin respaldo clínico propio. Otra entrada de hipertensión pulmonar de causa multifactorial poco clara comparte exactamente el mismo puntaje, lo que sugiere una señal común del grafo y no evidencia independiente.

## Otras Predicciones del Modelo

| Posición | Indicación Predicha | Puntaje TxGNN | Nivel | Comentario |
|------|------|------|------|------|
| 2 | Hipertensión pulmonar de mecanismo multifactorial poco claro | 99.78% | L5 | Justificación teórica por el sistema renina-angiotensina; sin ensayos ni literatura |
| 3 | Enfermedad renal hipertensiva maligna | 99.76% | L5 | La más coherente mecanísticamente (efecto renoprotector de los IECA), pero se maneja de forma aguda con fármacos parenterales; riesgo de lesión renal aguda e hiperpotasemia |
| 4 | Hipertensión renovascular maligna | 99.76% | L5 | Dependiente de angiotensina II; en estenosis bilateral de arteria renal o de riñón único los IECA pueden precipitar insuficiencia renal aguda |
| 5 | Síndrome de Braddock | 99.70% | L5 | Sin justificación mecanística clara; probablemente refleja proximidad en el grafo con nodos de hipertensión |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 63425 | HIPERTENE 5 mg comprimidos | Comprimido | No disponible |
| 63426 | HIPERTENE 10 mg comprimidos | Comprimido | No disponible |
| 63427 | HIPERTENE 20 mg comprimidos | Comprimido | No disponible |
| 83139 | IMIDAPRIL QUALIGEN 5 mg comprimidos EFG | Comprimido | No disponible |
| 83140 | IMIDAPRIL QUALIGEN 10 mg comprimidos EFG | Comprimido | No disponible |

Se muestran 5 de las 12 autorizaciones vigentes (todas de monofármaco). El resto corresponde a genéricos (EFG) de Neuraxpharm (Qualigen y Asibilan) y Dari Pharma, en dosis de 5, 10 y 20 mg.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta se completó y devolvió un único registro, relativo a la diana farmacológica de imidapril (la enzima convertidora de angiotensina, ACE), sin nivel de gravedad asignado. No se identificaron interacciones con otros fármacos.
- **Consideraciones específicas de clase** (según el análisis mecanístico de las predicciones): los IECA pueden causar lesión renal aguda e hiperpotasemia, y en estenosis bilateral de arteria renal o de riñón único pueden precipitar insuficiencia renal aguda.

No se dispone de advertencias ni contraindicaciones del prospecto en los datos compilados. Consultar el prospecto para información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Todas las predicciones son de nivel L5: solo existe la señal del modelo, sin ensayos clínicos ni literatura. Además, la plausibilidad mecanística para la hipertensión pulmonar hipóxica es débil y los IECA no han mostrado beneficio consistente en ese contexto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), actualmente ausente y bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción de imidapril (por ejemplo, desde DrugBank).
- Realizar una revisión sistemática de la literatura sobre IECA en hipertensión pulmonar y registrar ensayos relevantes.
- Estudios preclínicos o de mecanismo que respalden el vínculo con la hipertensión pulmonar.
- Si se desea una alternativa más cercana a la indicación original, evaluar la enfermedad renal hipertensiva con atención a los riesgos renales y de potasio.
- Verificar la compatibilidad de vía de administración (actualmente pendiente; el fármaco solo está disponible en comprimidos).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

