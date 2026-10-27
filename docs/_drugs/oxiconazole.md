---
layout: default
title: Oxiconazole
parent: Evidencia moderada (L3-L4)
nav_order: 596
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-14
description: "Oxiconazole: nueva indicación predicha, Candidiasis cutánea (nivel de evidencia L4). Indicación original: Tiña del pie, tiña del cuerpo…"
---

# Oxiconazole
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **1** 
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

## Oxiconazol: De Tiña del Pie a Candidiasis Cutánea
{: .text-alpha }

## Resumen en Una Frase

Oxiconazol es un antifúngico imidazólico de uso tópico, utilizado originalmente para el tratamiento de las infecciones cutáneas por dermatofitos (como la tiña del pie y la tiña del cuerpo) y la pitiriasis versicolor.
El modelo TxGNN predice que podría ser efectivo para **candidiasis cutánea**,
con **0 ensayos clínicos** y **5 publicaciones** (en su mayoría revisiones generales sobre micosis superficiales) que actualmente respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tiña del pie, tiña del cuerpo, pitiriasis versicolor y dermatofitosis de la ingle y la zona perianal (según el grafo de conocimiento; el texto de la ficha técnica no está disponible) |
| Nueva Indicación Predicha | Candidiasis cutánea |
| Puntaje de Predicción TxGNN | 99,81 % |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada para este informe. Según el conocimiento general de la clase, oxiconazol es un antifúngico imidazólico tópico que inhibe la lanosterol 14-alfa-desmetilasa (CYP51) del hongo. Esto bloquea la síntesis de ergosterol y altera la integridad de la membrana celular fúngica. Esta descripción se infiere del mecanismo conocido de los imidazoles, no de los datos aportados.

Las especies de *Candida* dependen del ergosterol y, en general, son sensibles a los azoles, por lo que el mecanismo es biológicamente plausible para la candidiasis cutánea. Las indicaciones originales (tiñas y pitiriasis versicolor) son micosis superficiales, de modo que la candidiasis cutánea sería una extensión cercana y no un reposicionamiento distante.

El puntaje elevado de TxGNN (0,998) probablemente refleja la similitud con otros antifúngicos azólicos ya utilizados en esta indicación. Conviene señalar que este puntaje es una predicción del modelo y no sustituye a la evidencia clínica directa.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [6382000](https://pubmed.ncbi.nlm.nih.gov/6382000/) | 1984 | Estudio clínico comparativo | Mykosen | Compara oxiconazol con econazol en dermatomicosis. No se ha confirmado la aleatorización ni resultados específicos para *Candida* (sin resumen disponible). |
| [10439936](https://pubmed.ncbi.nlm.nih.gov/10439936/) | 1999 | Revisión | Drugs | Actualización de terbinafina en micosis superficiales: eficaz en infecciones por dermatofitos, con actividad fungistática frente a *Candida albicans*. |
| [24196340](https://pubmed.ncbi.nlm.nih.gov/24196340/) | 2013 | Revisión | J Drugs Dermatol | Optimización del tratamiento antifúngico tópico en infecciones fúngicas cutáneas superficiales, con foco en naftifina. |
| [7501581](https://pubmed.ncbi.nlm.nih.gov/7501581/) | 1995 | Revisión | Postgrad Med | Diagnóstico y tratamiento de infecciones cutáneas por dermatofitos y *Candida*; menciona múltiples antifúngicos tópicos. |
| [2670516](https://pubmed.ncbi.nlm.nih.gov/2670516/) | 1989 | Revisión | Drugs | Revisión de bifonazol (imidazol) en micosis superficiales. |

Ninguna de las publicaciones evalúa directamente oxiconazol en candidiasis cutánea; la evidencia es indirecta y procede de fármacos de la misma clase o de revisiones generales.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 59854 | SALONGO 10 mg/g CREMA (Meda Pharma S.L.) | Crema | Texto de indicación no disponible |

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no texto de ficha técnica)**: dermatitis.

Para el resto de la información de seguridad (advertencias, contraindicaciones e interacciones), consultar el prospecto. No se encontraron interacciones farmacológicas registradas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo y en literatura indirecta (L4), sin ensayos clínicos con oxiconazol en candidiasis cutánea. Además, faltan los datos de seguridad de la ficha técnica, lo que impide completar el cribado de seguridad. El mecanismo es plausible y la indicación está cercana a las ya conocidas, por lo que la hipótesis merece seguimiento.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias, contraindicaciones, indicaciones aprobadas) para completar el cribado de seguridad.
- Confirmar el mecanismo de acción con datos de DrugBank.
- Revisar si la ficha técnica ya incluye candidiasis cutánea o actividad frente a *Candida*.
- Buscar estudios comparativos o ensayos específicos de oxiconazol en candidiasis cutánea, incluyendo el estudio de 1984 (Mykosen).
- Evaluar la relevancia de la contraindicación asociada a dermatitis para la población objetivo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

