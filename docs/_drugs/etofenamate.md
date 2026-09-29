---
layout: default
title: Etofenamate
parent: Solo predicción del modelo (L5)
nav_order: 218
evidence_level: L5
indication_count: 10
---

# Etofenamate
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

# Etofenamato: De Antiinflamatorio Tópico (AINE) a Susceptibilidad a Espondiloartropatía

## Resumen en Una Frase

Etofenamato es un antiinflamatorio no esteroideo (AINE) de uso tópico, éster del ácido flufenámico, comercializado en España en gel, spray cutáneo y parche.
El modelo TxGNN predice que podría ser efectivo para **susceptibilidad a espondiloartropatía**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en los registros de licencias disponibles (todos los textos de indicación están vacíos) |
| Nueva Indicación Predicha | Susceptibilidad a espondiloartropatía (spondyloarthropathy, susceptibility to) |
| Puntaje de Predicción TxGNN | 99.9996% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información conocida, etofenamato es un AINE tópico con inhibición de la ciclooxigenasa (COX). Mecanísticamente podría aliviar síntomas inflamatorios y dolorosos de las espondiloartritis, donde los AINE son tratamiento sintomático de primera línea.

Sin embargo, la predicción es débil como candidato clínico. "Susceptibilidad a espondiloartropatía" es un término de predisposición genética y no una condición tratable. Además, la vía tópica encaja mal con la enfermedad axial. El puntaje alto del modelo probablemente refleja proximidad en el grafo a términos musculoesqueléticos y no evidencia clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

Como referencia, la segunda predicción del modelo, **espondilitis anquilosante** (puntaje 99.9984%, nivel L4), tiene un único estudio:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11455681](https://pubmed.ncbi.nlm.nih.gov/11455681/) | 2001 | Estudio farmacocinético | Arzneimittel-Forschung | Mide niveles de etofenamato en suero y líquido sinovial tras iontoforesis en 11 pacientes con lumbalgia y 13 con sinovitis de rodilla. Muestra penetración tisular, sin datos de eficacia ni seguridad en espondilitis anquilosante |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 55701 | FLOGOPROFEN 50 mg/ml solución para pulverización cutánea (Chiesi España) | Solución para pulverización cutánea | No especificada |
| 56338 | ACTROMAGEL 50 mg/g gel (Bayer Hispania) | Gel | No especificada |
| 84578 | FLOGOPATCH 70 mg apósito adhesivo medicamentoso (Chiesi España) | Parche cutáneo | No especificada |
| 55380 | FLOGOPROFEN 50 mg/g gel (Chiesi España) | Gel | No especificada |
| 54646 | ZENAVAN 50 mg/g gel (Laboratorios Bial) | Gel | No especificada |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos ni literatura y se basa en un término de susceptibilidad genética. Todas las formulaciones autorizadas son tópicas, lo que limita su utilidad en enfermedad axial o sistémica.

**Para avanzar se necesita:**
- Reformular la indicación como condición clínica tratable, por ejemplo espondilitis anquilosante (rank 2), que tiene al menos un estudio farmacocinético
- Obtener el mecanismo de acción desde DrugBank
- Obtener advertencias y contraindicaciones del prospecto de AEMPS
- Verificar la indicación aprobada de cada autorización
- Evaluar la compatibilidad de vía de administración con la enfermedad objetivo
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

