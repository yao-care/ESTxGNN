---
layout: default
title: Etravirine
parent: Solo predicción del modelo (L5)
nav_order: 221
evidence_level: L5
indication_count: 10
---

# Etravirine
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

# Etravirina: De Infección por VIH-1 a Síndrome de Inmunodeficiencia Adquirida Felina

## Resumen en Una Frase

La etravirina es un inhibidor de la transcriptasa inversa no análogo de nucleósidos (ITINN) que se utiliza contra la infección por VIH-1.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia adquirida felina (SIDA felino)**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en los datos de AEMPS (uso conocido: infección por VIH-1) |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, la etravirina es un ITINN que bloquea la transcriptasa inversa del VIH-1. Su eficacia en la infección por VIH-1 está establecida y, mecanísticamente, podría ser aplicable a otros lentivirus, aunque con reservas importantes.

El virus de la inmunodeficiencia felina (FIV) es un lentivirus emparentado con el VIH, y de ahí probablemente proviene la cercanía en el grafo de conocimiento. Sin embargo, según la literatura general, la transcriptasa inversa del FIV es poco sensible a los ITINN. Por eso el fundamento mecanístico es débil y el puntaje alto probablemente refleja la proximidad en el grafo con términos de VIH, no una eficacia esperada en el gato.

Además, el Evidence Pack no incluye ensayos, literatura ni datos de compatibilidad de vía de administración para esta indicación. La evaluación depende, por tanto, únicamente de la predicción del modelo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 08468001 | INTELENCE 100 MG COMPRIMIDOS | Comprimido | Janssen-Cilag International N.V |
| 08468002 | INTELENCE 200 MG COMPRIMIDOS | Comprimido | Janssen-Cilag International N.V |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ensayos ni literatura propios (L5) y su plausibilidad mecanística es baja, porque el FIV es poco sensible a los ITINN. Además, no se dispone de las advertencias ni contraindicaciones de AEMPS.

**Para avanzar se necesita:**
- Datos in vitro de actividad de la etravirina frente a la transcriptasa inversa del FIV
- Datos del mecanismo de acción (MOA) desde DrugBank
- Advertencias y contraindicaciones del prospecto de AEMPS
- Confirmación de la indicación original aprobada, ya que el texto de indicación de las dos autorizaciones está vacío
- Evaluación de la compatibilidad de vía de administración y de la relevancia veterinaria de esta indicación

**Nota sobre otras predicciones del Evidence Pack:** «Complejo relacionado con el SIDA» y «VIH congénito» (rangos 4 y 5) tienen nivel L3 y decisión «Research Question». Probablemente son concordantes con el uso ya conocido en VIH y no reposicionamiento real. Los tres ensayos de fase 3 listados para el VIH congénito parecen evaluar otros regímenes, no etravirina. Por eso no elevan el nivel de evidencia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

