---
layout: default
title: Almasilate
parent: Solo predicción del modelo (L5)
nav_order: 40
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Almasilate: nueva indicación predicha, Úlcera péptica activa (nivel de evidencia L5). Indicación original: Enfermedad ulcerosa péptica (según el grafo de conocimiento"
monitor_inn: "Almasilate"
predicted_indications: ["gastroduodenitis"]
---

# Almasilate
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

## Almasilato: De Enfermedad Ulcerosa Péptica a Úlcera Péptica Activa
{: .text-alpha }

## Resumen en Una Frase

Almasilato es un antiácido de silicato de aluminio y magnesio, utilizado originalmente para la enfermedad ulcerosa péptica, el reflujo gastroesofágico, la esofagitis y la dispepsia.
El modelo TxGNN predice que podría ser efectivo para **úlcera péptica activa**, aunque esta indicación ya está incluida en sus usos originales, por lo que no constituye un reposicionamiento genuino.
Actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción concreta.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad ulcerosa péptica (según el grafo de conocimiento; la autorización española no incluye texto de indicación) |
| Nueva Indicación Predicha | Úlcera péptica activa |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, almasilato es un antiácido tamponante de silicato de aluminio y magnesio que neutraliza el ácido gástrico, y su uso en patología ácido-péptica es conocido.

La úlcera péptica activa está comprendida dentro de la indicación original de enfermedad ulcerosa péptica. El puntaje alto (0.999) refleja con toda probabilidad este solapamiento con una indicación ya conocida y no un hallazgo nuevo. Por ello, esta predicción debe interpretarse como una confirmación del uso existente y no como reposicionamiento.

Entre las otras candidatas predichas, la **úlcera gastroyeyunal** (99.87%) cuenta con una única publicación indirecta (una revisión de 1985 sobre antiácidos tamponantes complejos). Mecanísticamente es plausible como tratamiento adyuvante, ya que estas úlceras son de naturaleza ácido-péptica. La **perforación de úlcera péptica** (99.87%) no es tratable con antiácidos, al ser una urgencia quirúrgica. La **gastroduodenitis** (99.77%) y la **úlcera gástrica** (99.55%) son cercanas a las indicaciones originales y carecen de evidencia propia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Para la indicación principal (úlcera péptica activa) actualmente no hay literatura relacionada disponible. Para la segunda candidata (úlcera gastroyeyunal) se identificó:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [3888581](https://pubmed.ncbi.nlm.nih.gov/3888581/) | 1985 | Revisión | Drug and Therapeutics Bulletin | Revisión de antiácidos tamponantes complejos (magaldrato y almasilato); evidencia general e indirecta, sin datos específicos de la enfermedad |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 52255 | DOLCOPIN 1 g polvo para suspensión oral | Polvo para suspensión oral | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): enfermedad renal, piouréter, enfermedades diarreicas (incluida la diarrea crónica), estreñimiento, hipofosfatemia, impactación intestinal y hemorroides.

Consultar el prospecto para el resto de la información de seguridad, incluidas advertencias e interacciones.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación predicha ya forma parte de los usos originales del fármaco, de modo que no es un reposicionamiento real, y no hay ensayos ni literatura que la respalden (nivel L5). La evidencia indirecta para úlcera gastroyeyunal (L4) es limitada y antigua.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de la AEMPS (advertencias y contraindicaciones), requisito previo para cualquier evaluación de seguridad.
- Completar los datos del mecanismo de acción.
- Si se desea explorar reposicionamiento, priorizar indicaciones realmente distintas de las originales y buscar literatura específica (por ejemplo, úlcera gastroyeyunal).
- Valorar las contraindicaciones del grafo de conocimiento, en especial la enfermedad renal, por el contenido de aluminio y magnesio.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

