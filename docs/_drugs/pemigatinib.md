---
layout: default
title: Pemigatinib
parent: Solo predicción del modelo (L5)
nav_order: 414
evidence_level: L5
indication_count: 10
---

# Pemigatinib
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

# Pemigatinib: De Indicación Original No Disponible a Neoplasia Endocrina Múltiple

## Resumen en Una Frase

Pemigatinib es un inhibidor selectivo de FGFR1-3 comercializado en España, pero los datos recibidos no incluyen el texto de su indicación original.
El modelo TxGNN predice que podría ser efectivo para **neoplasia endocrina múltiple**, con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que la predicción se apoya solo en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos recibidos (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Neoplasia endocrina múltiple |
| Puntaje de Predicción TxGNN | 99,71% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Pemigatinib es un inhibidor selectivo de los receptores FGFR1, FGFR2 y FGFR3. No se dispone de datos detallados de mecanismo de acción procedentes de DrugBank. La descripción anterior proviene del análisis mecanístico del propio Evidence Pack.

La relación con la neoplasia endocrina múltiple (MEN) es débil. Estos síndromes se deben principalmente a alteraciones en MEN1 y RET, que pemigatinib no inhibe. La conexión entre la señalización FGFR y la tumorigénesis endocrina es solo especulativa.

El puntaje alto del modelo (99,71%) no cuenta con respaldo de ensayos ni de literatura. Debe interpretarse como una hipótesis del grafo de conocimiento, no como una señal de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1211535001 | PEMAZYRE 4,5 mg COMPRIMIDOS | Comprimido | No especificada en los datos recibidos |
| 1211535005 | PEMAZYRE 13,5 mg COMPRIMIDOS | Comprimido | No especificada en los datos recibidos |
| 1211535003 | PEMAZYRE 9 mg COMPRIMIDOS | Comprimido | No especificada en los datos recibidos |

Titular: Incyte Biosciences Distribution B.V.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de FGFR1-3) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Nota: la consulta de interacciones farmacológicas no devolvió resultados. Además, el mecanismo sugiere que los efectos endocrinos y del metabolismo del fosfato propios de la inhibición de FGFR deben evaluarse como consideraciones de seguridad, no como indicaciones.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (nivel L5), sin ensayos ni literatura, y con un vínculo mecanístico débil, ya que MEN depende de MEN1 y RET y no de FGFR. Las otras nueve predicciones del listado (amenorrea, infecciones virales, esclerosis lateral amiotrófica, displasia esquelética, etc.) tampoco tienen respaldo y quedan igualmente en Hold. La excepción es el carcinoma de mama HER2 positivo, con una única revisión general de inhibidores de quinasas (nivel L4, "Research Question").

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), que es una brecha bloqueante para el cribado de seguridad
- Obtener el texto de las indicaciones autorizadas para identificar la indicación original
- Consultar el mecanismo de acción en la API de DrugBank
- Buscar evidencia preclínica o clínica específica de pemigatinib en neoplasias endocrinas
- Valorar priorizar la hipótesis de cáncer de mama HER2 positivo (resistencia mediada por FGFR), que tiene un fundamento mecanístico más plausible
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

