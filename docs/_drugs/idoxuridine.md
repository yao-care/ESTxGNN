---
layout: default
title: Idoxuridine
parent: Solo predicción del modelo (L5)
nav_order: 404
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

# Idoxuridina: De Queratitis por Virus del Herpes Simple a Candidiasis Vulvovaginal

## Resumen en Una Frase

Idoxuridina es un análogo de la timidina que inhibe la síntesis del ADN viral, utilizado originalmente para tratar la queratitis por virus del herpes simple.
El modelo TxGNN predice que podría ser efectivo para **candidiasis vulvovaginal**, pero actualmente no hay **ningún ensayo clínico** ni **ninguna publicación** que respalde esta dirección (la predicción se basa solo en el modelo).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Queratitis por virus del herpes simple (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas están vacíos) |
| Nueva Indicación Predicha | Candidiasis vulvovaginal |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la idoxuridina es un análogo nucleosídico de la timidina que inhibe la síntesis de ADN viral, y su eficacia se ha establecido en infecciones por herpes simple de uso tópico (queratitis).

Para la candidiasis vulvovaginal, **la plausibilidad mecanística es baja**. *Candida* es un hongo, y un antiviral análogo de la timidina no tiene una actividad antifúngica directa conocida. El puntaje alto (99.92%) refleja una asociación derivada de la red de conocimiento, no una evidencia biológica o clínica. Además, existen tratamientos antifúngicos estándar bien establecidos.

Cabe señalar que, entre las demás indicaciones predichas para el mismo fármaco, la más plausible mecanísticamente es la **vulvovaginitis herpética** (puntaje 99.59%, nivel L5), ya que el patógeno es el mismo virus del herpes simple. Aun así, no hay ensayos ni literatura específica, y los antivirales sistémicos modernos (aciclovir, valaciclovir) están mucho mejor establecidos. Se recomienda considerarla como pregunta de investigación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para candidiasis vulvovaginal.

*Nota:* para otras indicaciones predichas (vaginitis, vulvitis, vulvovaginitis) se identificó literatura de baja calidad e indirecta, por ejemplo:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [7814938](https://pubmed.ncbi.nlm.nih.gov/7814938/) | 1994 | Estudio clínico | Nihon Sanka Fujinka Gakkai Zasshi | Tratamiento tópico de condiloma acuminado genital y neoplasia intraepitelial vaginal (VAIN) con idoxuridina y aclarubicina; condiciones relacionadas con VPH, no vaginitis en sentido estricto |
| [14275292](https://pubmed.ncbi.nlm.nih.gov/14275292/) | 1965 | Revisión/reporte descriptivo | Obstetrics and Gynecology | Infección por herpes simple en el tracto genital femenino; coherente con el mecanismo antiviral, pero no es un estudio controlado de idoxuridina |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 51201 | VIREXEN SOLUCION 10% | Solución cutánea | No disponible en el registro |
| 58135 | VIREXEN SOLUCION 40% | Solución cutánea | No disponible en el registro |
| 51202 | VIREXEN SOLUCION 2% | Solución cutánea | No disponible en el registro |

Las tres autorizaciones están vigentes, son de un solo principio activo y pertenecen a Laboratorios Viñas S.A. Todas son de uso cutáneo/tópico.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para candidiasis vulvovaginal se apoya únicamente en el puntaje del modelo (L5), sin ensayos clínicos ni literatura, y es mecanísticamente improbable al tratarse de un antiviral frente a un hongo.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consulta a DrugBank) y análisis del vínculo mecanístico
- Advertencias y contraindicaciones del prospecto de la AEMPS (necesarias antes de cualquier evaluación de seguridad)
- Evidencia preclínica (p. ej., actividad in vitro frente a *Candida*) antes de considerar estudios clínicos
- Evaluación de compatibilidad de vía de administración (las presentaciones actuales son soluciones cutáneas, no vaginales)
- Si se desea explorar una dirección con más sentido, priorizar la vulvovaginitis herpética como pregunta de investigación, comparándola con los antivirales actuales
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

