---
layout: default
title: Amantadine
parent: Solo predicción del modelo (L5)
nav_order: 35
evidence_level: L5
indication_count: 4
---

# Amantadine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Amantadina: De Antivírico y Enfermedad de Parkinson a Encefalitis Subaguda de Rasmussen

## Resumen en Una Frase

La amantadina se ha usado históricamente como antivírico contra la gripe y, más tarde, para la discinesia y la enfermedad de Parkinson. El modelo TxGNN predice que podría ser efectiva para la **encefalitis subaguda de Rasmussen**, pero esta predicción **no tiene ensayos clínicos ni publicaciones** que la respalden: es solo una señal del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en la autorización de AEMPS. Según la farmacología: gripe (uso ya no recomendado), discinesia y enfermedad de Parkinson |
| Nueva Indicación Predicha | Encefalitis subaguda de Rasmussen |
| Puntaje de Predicción TxGNN | 99.48% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro de origen. Los datos farmacológicos indican que la amantadina actúa sobre las subunidades del receptor NMDA (GluN2A, GluN2B, GluN2C y GluN2D, genes GRIN2A-D), con un efecto antagonista débil.

La encefalitis de Rasmussen es una enfermedad inflamatoria cerebral crónica que cursa con crisis epilépticas. En teoría, el antagonismo del receptor NMDA podría influir en la excitotoxicidad mediada por glutamato y en las crisis. Esta hipótesis **no está respaldada por estudios** y no se pudo contrastar con el mecanismo de acción de la fuente.

Un puntaje alto del grafo, por sí solo, no se considera evidencia. Por ahora la predicción es una pista para investigar, no una base para uso clínico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 44541 | AMANTADINE LEVEL 100 mg CAPSULAS DURAS | Cápsula dura | Laboratorios Ern S.A. |

El texto de la indicación aprobada no figura en los datos recibidos.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

La consulta de interacciones devolvió solo registros farmacológicos de dianas (subunidades del receptor NMDA), no interacciones clínicas con otros fármacos.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es de nivel L5: solo el modelo, sin ensayos ni publicaciones, y sin mecanismo de acción ni ficha técnica verificados. No hay base suficiente para avanzar.

**Para avanzar se necesita:**
- Descargar y analizar la ficha técnica de AEMPS (advertencias y contraindicaciones).
- Obtener el mecanismo de acción desde DrugBank.
- Hacer una búsqueda de literatura específica sobre amantadina y encefalitis de Rasmussen.
- Confirmar la compatibilidad de la vía y forma farmacéutica (hoy solo hay cápsula dura oral).

**Otras predicciones del mismo fármaco (fuera de esta evaluación principal):**
- **Mielitis** (L4, "Research Question"): la literatura trata sobre todo el síndrome postpolio, donde se probó la amantadina para la fatiga, y solo aporta evidencia indirecta. Conviene una revisión dirigida para definir qué subtipo de mielitis, si alguno, sería un objetivo razonable.
- **Neurodegeneración asociada a PLA2G6** (L4, Hold): los dos artículos tratan sobre PKAN, una enfermedad hermana, y no hay evidencia específica de PLA2G6.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

