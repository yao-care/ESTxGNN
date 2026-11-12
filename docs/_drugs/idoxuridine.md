---
layout: default
title: Idoxuridine
parent: Solo predicción del modelo (L5)
nav_order: 404
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
monitor_inn: "Idoxuridine"
predicted_indications: ["vulvovaginal candidiasis", "vaginitis (disease)", "trichomonal vulvovaginitis", "vulvitis", "herpetic vulvovaginitis", "vaginal discharge", "bacterial vaginosis", "leukoplakia of vagina", "vulvovaginitis", "postmenopausal atrophic vaginitis"]
description: "Idoxuridine: nueva indicación predicha, Candidiasis vulvovaginal (vulvovaginal candidiasis) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
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

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Idoxuridine: Candidiasis vulvovaginal (vulvovaginal candidiasis)
{: .text-alpha }

## Resumen en Una Frase

Idoxuridina es un análogo de la timidina que inhibe la síntesis del ADN viral, utilizado originalmente para tratar la queratitis por virus del herpes simple.
El modelo TxGNN predice que podría ser efectivo para **candidiasis vulvovaginal**, pero actualmente no hay **ningún ensayo clínico** ni **ninguna publicación** que respalde esta dirección (la predicción se basa solo en el modelo).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Candidiasis vulvovaginal (vulvovaginal candidiasis) |
| Puntaje de Predicción TxGNN | 0.9992 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado (registros anulados: 3 de 3) |
| Número de Autorizaciones | 3 (comercializadas: 0) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la idoxuridina es un análogo nucleosídico de la timidina que inhibe la síntesis de ADN viral, y su eficacia se ha establecido en infecciones por herpes simple de uso tópico (queratitis).

Para la candidiasis vulvovaginal, **la plausibilidad mecanística es baja**. *Candida* es un hongo, y un antiviral análogo de la timidina no tiene una actividad antifúngica directa conocida. El puntaje alto (0.9992) refleja una asociación derivada de la red de conocimiento, no una evidencia biológica o clínica. Además, existen tratamientos antifúngicos estándar bien establecidos.

Cabe señalar que, entre las demás indicaciones predichas para el mismo fármaco, la más plausible mecanísticamente es la **vulvovaginitis herpética** (puntaje 0.9959, nivel L5), ya que el patógeno es el mismo virus del herpes simple. Aun así, no hay ensayos ni literatura específica, y los antivirales sistémicos modernos (aciclovir, valaciclovir) están mucho mejor establecidos. Se recomienda considerarla como pregunta de investigación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para candidiasis vulvovaginal.

*Nota:* para otras indicaciones predichas (vaginitis, vulvitis, vulvovaginitis) se identificó literatura de baja calidad e indirecta, por ejemplo:

<!-- review:begin es-lic-20261105-idoxuridine-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Las tres autorizaciones están vigentes, son de un solo principio activo y pertenecen a Laboratorios Viñas S.A. Todas son de uso cutáneo/tópico." Eliminado: el número o el estado de comercialización de las autorizaciones no coincidía con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 3 autorizaciones (comercializadas: 0); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en España. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-idoxuridine-1 -->

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

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Las tres autorizaciones están vigentes, son de un solo principio activo y pertenecen a Laboratorios Viñas S.A. Todas son de uso cutáneo/tópi" | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

