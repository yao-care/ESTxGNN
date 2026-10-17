---
layout: default
title: Cobicistat
parent: Solo predicción del modelo (L5)
nav_order: 203
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Cobicistat: nueva indicación predicha, Infección por el virus de la inmunodeficiencia simia (nivel de evidencia L5). Indicación original: Infección por VIH / SIDA (según el grafo de conocimiento"
monitor_inn: "COBICISTAT"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Cobicistat
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Cobicistat: De Infección por VIH a Infección por el Virus de la Inmunodeficiencia Simia

## Resumen en Una Frase

Cobicistat es un potenciador farmacocinético utilizado originalmente en el tratamiento de la infección por VIH y el SIDA.
El modelo TxGNN predice que podría ser efectivo para **infección por el virus de la inmunodeficiencia simia (VIS)**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección por VIH / SIDA (según el grafo de conocimiento; el texto de indicación autorizado no está disponible) |
| Nueva Indicación Predicha | Infección por el virus de la inmunodeficiencia simia |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento general, cobicistat es un inhibidor del CYP3A basado en mecanismo que se usa como potenciador farmacocinético de antirretrovirales (por ejemplo, elvitegravir, atazanavir, darunavir) en el tratamiento del VIH-1. No tiene actividad antiviral intrínseca conocida.

El VIS es un lentivirus muy cercano al VIH y es el modelo de primates no humanos más habitual de esta enfermedad. Por ello, el alto puntaje de TxGNN probablemente refleja la proximidad en la red de conocimiento con la indicación de VIH. Cualquier beneficio dependería de potenciar un antirretroviral administrado conjuntamente.

Conviene tener en cuenta que el VIS es un modelo veterinario/preclínico y no una enfermedad humana, lo que limita la traslación clínica. Las otras dos predicciones del modelo tampoco aportan una vía de reposicionamiento humana sólida: el SIDA felino (enfermedad veterinaria, puntaje 99.92%) y un trastorno del neurodesarrollo raro con marcha atáxica, ausencia del habla y reducción de la sustancia blanca cortical (puntaje 99.91%), para el cual no se identificó ningún vínculo mecanístico claro.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 113872001 | TYBOST 150 mg comprimidos recubiertos con película (Gilead Sciences Ireland Unlimited Company) | Comprimido recubierto con película | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registraron 100 interacciones (fuente: DDInter). Entre las principales de gravedad **Mayor**:
  - Loperamida
  - Triamcinolona
  - Cisaprida
  - Budesonida

  Entre las de gravedad **Moderada** figuran hidrocortisona, aprepitant, betametasona, clotrimazol, dexametasona, fenfluramina, dexfenfluramina, metoclopramida, repaglinida y claritromicina. También se registró una interacción **Menor** con prucaloprida. Muchas se explican por la inhibición del CYP3A.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura. Además, el VIS es un modelo animal y no una enfermedad humana, y cobicistat carece de actividad antiviral propia.

**Para avanzar se necesita:**
- Obtener y revisar las advertencias y contraindicaciones del prospecto de la AEMPS
- Completar los datos del mecanismo de acción
- Evaluar si la indicación tiene relevancia clínica humana o solo valor como modelo preclínico
- Buscar estudios preclínicos o de farmacocinética que respalden el uso como potenciador en el contexto del VIS
- Revisar el perfil de interacciones farmacológicas (100 registradas) antes de cualquier uso fuera de indicación
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

