---
layout: default
title: Diflunisal
parent: Solo predicción del modelo (L5)
nav_order: 176
evidence_level: L5
indication_count: 10
---

# Diflunisal
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

# Diflunisal: De Indicación Original No Registrada a Displasia Acromesomélica tipo Hunter-Thompson

## Resumen en Una Frase

Diflunisal es un antiinflamatorio no esteroideo (AINE) que inhibe la ciclooxigenasa (COX). Los datos de AEMPS disponibles no registran su indicación original.
El modelo TxGNN predice que podría ser efectivo para **displasia acromesomélica tipo Hunter-Thompson**, una displasia esquelética genética.
Actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción, por lo que es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No registrada en los datos de AEMPS |
| Nueva Indicación Predicha | Displasia acromesomélica tipo Hunter-Thompson |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos. Según la información conocida, diflunisal es un AINE que inhibe COX-1 y COX-2 y reduce la inflamación y el dolor mediados por prostaglandinas.

Esta predicción **no tiene un vínculo mecanístico plausible**. La displasia acromesomélica tipo Hunter-Thompson es una displasia esquelética genética que afecta a la vía GDF5/CDMP1. Diflunisal no actúa sobre esa vía. La inhibición de COX no modificaría el defecto genético subyacente.

El puntaje alto (99.99%) probablemente es un artefacto del grafo de conocimiento y no refleja una relación biológica real. No hay ensayos ni literatura que lo respalden.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1251929001 | ATTROGY 250 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA (Purpose Pharma International Ab) | Comprimido recubierto con película | No especificada en los datos disponibles |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de plausibilidad mecanística, ensayos clínicos y literatura (nivel L5). El puntaje alto de TxGNN parece un artefacto del grafo de conocimiento y no justifica avanzar.

**Para avanzar se necesita:**
- Datos del prospecto de AEMPS (advertencias y contraindicaciones), y confirmar la indicación original aprobada
- Datos detallados del mecanismo de acción (MOA) desde DrugBank
- Evidencia preclínica que vincule la vía GDF5/CDMP1 con la inhibición de COX, si se quisiera reconsiderar esta indicación
- **Nota:** en la misma evaluación, **espondilitis anquilosante** (rango 5, nivel L3) y **espondilopatía inflamatoria** (rango 10, nivel L3) tienen mayor respaldo. Existe un estudio clínico comparativo de diflunisal frente a fenilbutazona (PMID 3524970, 1986), cuyo diseño aleatorizado y doble ciego debe verificarse. Se recomienda priorizar estas indicaciones en una evaluación aparte.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

