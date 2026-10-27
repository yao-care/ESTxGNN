---
layout: default
title: Bedaquiline
parent: Evidencia moderada (L3-L4)
nav_order: 89
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Bedaquiline: nueva indicación predicha, Tuberculosis bovina (nivel de evidencia L4). Indicación original: Tuberculosis pulmonar y tuberculosis multirresistente"
monitor_inn: "Bedaquiline"
predicted_indications: ["vulvovaginal candidiasis", "fascioliasis", "urea cycle disorder", "esophageal candidiasis"]
---

# Bedaquiline
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

## Bedaquilina: De Tuberculosis Pulmonar a Tuberculosis Bovina
{: .text-alpha }

## Resumen en Una Frase

Bedaquilina es un antibiótico antituberculoso, utilizado originalmente para tratar la tuberculosis pulmonar y la tuberculosis multirresistente.
El modelo TxGNN predice que podría ser efectivo para **tuberculosis bovina**,
pero actualmente no hay **ningún ensayo clínico** y solo **1 publicación** (un estudio in vitro sobre *M. tuberculosis*) respalda esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tuberculosis pulmonar y tuberculosis multirresistente |
| Nueva Indicación Predicha | Tuberculosis bovina |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento general, bedaquilina inhibe la ATP sintasa de las micobacterias (subunidad c de la F-ATP sintasa), por lo que bloquea la producción de energía de la bacteria. Esta información no procede de los datos compilados y debe confirmarse en una fuente oficial.

La tuberculosis bovina la causa *Mycobacterium bovis*, que pertenece al mismo complejo que *M. tuberculosis*, el agente de la tuberculosis humana. Como ambas especies comparten gran parte de su biología, es plausible que un fármaco activo contra una también lo sea contra la otra.

Sin embargo, la única evidencia disponible es un artículo metodológico in vitro sobre la concentración mínima inhibitoria (CMI) de bedaquilina frente a *M. tuberculosis* H37Rv. No hay datos específicos de *M. bovis* ni datos clínicos. El puntaje alto del modelo refleja sobre todo la cercanía en el grafo de conocimiento con la tuberculosis, no una demostración de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27210281](https://pubmed.ncbi.nlm.nih.gov/27210281/) | 2016 | Estudio in vitro | Medecine et maladies infectieuses | Evalúa cómo las condiciones de cultivo in vitro afectan la CMI de bedaquilina frente a *M. tuberculosis* H37Rv, con el fin de estandarizar las pruebas de sensibilidad. No aborda la tuberculosis bovina. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 113901001 | SIRTURO 100 MG COMPRIMIDOS | Comprimido | No especificada en los datos compilados |
| 113901002 | SIRTURO 100 MG COMPRIMIDOS | Comprimido | No especificada en los datos compilados |

Ambas autorizaciones están vigentes, corresponden a monofármaco y su titular es Janssen-Cilag International N.V.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registraron 100 interacciones (la lista revisada incluye 20). Entre las de nivel **Mayor** figuran dexametasona, claritromicina, ácido picosulfúrico, polietilenglicol (3350 con electrolitos), dolasetrón, palonosetrón y sulfato de sodio. Hay además varias de nivel **Moderado**, como acarbosa, famotidina, doxiciclina, pioglitazona, loperamida, bupropión, bisacodilo, ácido quenodesoxicólico, minociclina, oxandrolona, oximetolona, tetraciclina y naltrexona.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en un estudio in vitro sobre *M. tuberculosis*, sin ensayos clínicos ni datos específicos de *M. bovis* (nivel L4). El mecanismo es plausible, pero no hay evidencia directa que justifique avanzar.

**Para avanzar se necesita:**
- Datos de actividad in vitro e in vivo de bedaquilina frente a *M. bovis*.
- Confirmación del mecanismo de acción en una fuente oficial.
- Revisión de advertencias y contraindicaciones del prospecto de la AEMPS.
- Análisis detallado de interacciones, dado el elevado número de las de nivel Mayor.
- Valorar si esta indicación tiene relevancia clínica real en humanos, porque la tuberculosis bovina es poco frecuente y se maneja dentro del espectro de la tuberculosis.

**Nota complementaria:** entre las otras predicciones del modelo, la **tuberculosis inactiva (infección latente)** cuenta con evidencia más sólida, en particular el ensayo de fase 2/3 BREACH-TB (NCT06568484), aún en reclutamiento y sin resultados. Podría ser una dirección más prometedora para una evaluación posterior.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

