---
layout: default
title: Itopride
parent: Solo predicción del modelo (L5)
nav_order: 436
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Itopride: nueva indicación predicha, Enfermedad de Crohn del intestino delgado (nivel de evidencia L5). Indicación original: Gastritis (según el grafo de conocimiento"
monitor_inn: "Itopride"
predicted_indications: ["small bowel Crohn disease", "venous insufficiency (disease)", "achlorhydria", "hiatus hernia (disease)"]
---

# Itopride
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

# Itopride: De Gastritis a Enfermedad de Crohn del Intestino Delgado

## Resumen en Una Frase

Itopride es un procinético gastrointestinal, originalmente utilizado para el tratamiento de la gastritis.
El modelo TxGNN predice que podría ser efectivo para la **enfermedad de Crohn del intestino delgado**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Gastritis (según el grafo de conocimiento; el texto de indicación de la autorización española no está disponible) |
| Nueva Indicación Predicha | Enfermedad de Crohn del intestino delgado |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Español | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Según la información conocida, itopride es un antagonista del receptor de dopamina D2 e inhibidor de la acetilcolinesterasa que favorece la motilidad gastrointestinal, y su uso en trastornos gástricos como la gastritis está establecido. Mecanísticamente, su aplicabilidad a la enfermedad de Crohn es muy dudosa.

La enfermedad de Crohn es una afección inflamatoria, y la actividad procinética no tiene un papel antiinflamatorio establecido. Cualquier vínculo sería especulativo (por ejemplo, una posible vía antiinflamatoria colinérgica) y no está respaldado por los datos disponibles. Además, los procinéticos podrían estar contraindicados o ser riesgosos en la enfermedad de Crohn con estenosis u obstrucción.

El puntaje TxGNN (0.999) es solo una predicción computacional sin corroboración clínica y no debe interpretarse como evidencia de eficacia.

### Otras indicaciones predichas (solo con fines de contexto)

| Indicación predicha | Puntaje TxGNN | Nivel de evidencia | Comentario |
|------|------|------|------|
| Insuficiencia venosa | 99.23% | L5 | Sin vínculo mecanístico plausible; podría reflejar artefactos del grafo de conocimiento |
| Aclorhidria | 99.16% | L5 | Relativamente más cercana a la indicación gástrica original, pero el beneficio se limitaría a aliviar síntomas (p. ej., vaciamiento gástrico retrasado o dispepsia), sin corregir la deficiencia de ácido |
| Hernia de hiato | 99.02% | L5 | Un procinético no corrige el defecto anatómico; posible beneficio sintomático en reflujo o dispepsia asociados |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 86657 | PROGIT 50 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA EFG | Comprimido recubierto con película | No disponible en los datos compilados |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura, y el vínculo mecanístico entre un procinético y una enfermedad inflamatoria como el Crohn es especulativo, con posibles riesgos en casos con estenosis u obstrucción.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA) y análisis de un posible vínculo antiinflamatorio
- Revisión de la ficha técnica/prospecto de la AEMPS (advertencias y contraindicaciones), indispensable antes de cualquier evaluación de seguridad
- Revisión sistemática de la literatura preclínica y clínica sobre procinéticos o agonismo colinérgico en enfermedad inflamatoria intestinal
- Evaluación de riesgos en pacientes con estenosis u obstrucción intestinal
- Si se prioriza otra indicación, definir un criterio de valoración clínico claro (p. ej., aclorhidria o hernia de hiato con síntomas de dispepsia o reflujo), ya que parecen más plausibles a nivel sintomático
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

