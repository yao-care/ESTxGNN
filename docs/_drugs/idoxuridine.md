---
layout: default
title: Idoxuridine
parent: Solo predicción del modelo (L5)
nav_order: 271
evidence_level: L5
indication_count: 10
---

# Idoxuridine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Idoxuridina: De Antiviral Tópico a Candidiasis Vulvovaginal

## Resumen en Una Frase

Idoxuridina es un análogo de la timidina con actividad antiviral, comercializado en España como solución cutánea (Virexen).
El modelo TxGNN predice que podría ser efectiva para **candidiasis vulvovaginal**, pero hay **0 ensayos clínicos** y solo **1 publicación** vinculada, una revisión de 1972 sobre herpes genital que no trata la candidiasis.
La predicción no tiene respaldo biológico ni clínico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (los textos de indicación de las autorizaciones de AEMPS están vacíos) |
| Nueva Indicación Predicha | Candidiasis vulvovaginal |
| Puntaje de Predicción TxGNN | 99,92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, la idoxuridina es un análogo de la timidina que inhibe la síntesis de ADN viral, por lo que su uso se asocia a infecciones por herpesvirus.

**Esta predicción no parece razonable.** *Candida* es un hongo y no hay un mecanismo antiviral plausible contra él. El único artículo vinculado (PMID 4564724) trata sobre la infección genital por herpesvirus, no sobre candidiasis.

El puntaje alto (99,92%) parece un artefacto del grafo de conocimiento. Probablemente se debe a la proximidad de contexto entre las infecciones del tracto genital, y no a una relación farmacológica real.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [4564724](https://pubmed.ncbi.nlm.nih.gov/4564724/) | 1972 | Revisión | Obstetrics and Gynecology | Revisión sobre la infección genital femenina por herpesvirus. No aborda candidiasis ni demuestra eficacia de la idoxuridina. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 51201 | Virexen Solución 10% | Solución cutánea | Texto de indicación no disponible |
| 58135 | Virexen Solución 40% | Solución cutánea | Texto de indicación no disponible |
| 51202 | Virexen Solución 2% | Solución cutánea | Texto de indicación no disponible |

Titular de las tres autorizaciones: Laboratorios Viñas S.A.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni literatura relevante, y no existe un mecanismo plausible entre un antiviral análogo de nucleósido y una infección fúngica. La evidencia es solo la predicción del modelo (L5).

Entre las otras predicciones de la lista, la más coherente mecanísticamente es la **vulvovaginitis herpética**. Las indicaciones de herpes genital (vulvitis, vaginitis, vulvovaginitis) tienen evidencia L4 y están marcadas como "Research Question". Sin embargo, la literatura es histórica (1965-1978) y los antivirales modernos como el aciclovir ya cubren esta necesidad.

**Para avanzar se necesita:**
- Descartar la candidiasis vulvovaginal como objetivo y reorientar la evaluación hacia las indicaciones herpéticas, si se desea continuar.
- Obtener los datos de mecanismo de acción (DrugBank).
- Obtener las advertencias y contraindicaciones del prospecto de AEMPS y los textos de indicación aprobados.
- Confirmar la compatibilidad de la vía de administración: los productos actuales son soluciones cutáneas y la nueva indicación requeriría una vía vaginal.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

