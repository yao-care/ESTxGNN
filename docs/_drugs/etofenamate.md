---
layout: default
title: Etofenamate
parent: Solo predicción del modelo (L5)
nav_order: 316
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Etofenamate: nueva indicación predicha, Espondiloartropatía, susceptibilidad a (spondyloarthropathy… (nivel de evidencia L5). Indicación original: Osteoartritis / artropatía (según el grafo de conoci…"
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

# Etofenamato: De Osteoartritis a Espondiloartropatía (Susceptibilidad Genética)

## Resumen en Una Frase

Etofenamato es un antiinflamatorio no esteroideo (AINE) de uso tópico, éster del ácido flufenámico, utilizado originalmente en el tratamiento de la osteoartritis y otras artropatías.
El modelo TxGNN predice que podría ser efectivo para **espondiloartropatía (susceptibilidad genética)**,
pero **no hay ensayos clínicos ni publicaciones** que respalden directamente esta predicción: se basa únicamente en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Osteoartritis / artropatía (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Espondiloartropatía, susceptibilidad a (spondyloarthropathy, susceptibility to) |
| Puntaje de Predicción TxGNN | 99,9996 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Etofenamato es un AINE tópico (éster del ácido flufenámico) que inhibe la ciclooxigenasa y reduce la inflamación mediada por prostaglandinas. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank; esta descripción se basa en el conocimiento general de la clase.

Las espondiloartropatías inflamatorias comparten con la osteoartritis síntomas de dolor e inflamación articular, y los AINE son una terapia sintomática habitual en ellas. Por ello, mecanísticamente el efecto antiinflamatorio podría aliviar síntomas.

Sin embargo, la predicción tiene limitaciones importantes: la entidad predicha es una **etiqueta de susceptibilidad genética** y no una condición clínica tratable, y el vínculo se apoya solo en la predicción de TxGNN.

### Otras predicciones del modelo (contexto)

| Enfermedad predicha | Puntaje TxGNN | Nivel | Valoración |
|------|------|------|------|
| Espondilitis anquilosante | 99,998 % | L4 | Pregunta de investigación: los AINE son tratamiento de primera línea, pero la vía tópica es poco adecuada para la enfermedad axial |
| Artritis reumatoide juvenil poliarticular | 99,996 % | L5 | Pregunta de investigación: mecanismo plausible, sin evidencia; seguridad pediátrica no establecida |
| Vasculitis reumatoide, hipermovilidad del cóccix, displasia acromesomélica tipo Hunter-Thompson, síndrome braquiolmia-amelogénesis imperfecta, pseudoacondroplasia, miosclerosis, enfermedad de Kümmell | 99,996–99,997 % | L5 | Hold: sin evidencia y, en varios casos, sin mecanismo plausible (probables artefactos del grafo de conocimiento) |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para espondiloartropatía (susceptibilidad genética).

## Evidencia de Literatura

Para la indicación principal no hay literatura relacionada disponible. Como evidencia indirecta de la segunda predicción (espondilitis anquilosante), se recuperó una publicación:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11455681](https://pubmed.ncbi.nlm.nih.gov/11455681/) | 2001 | Estudio farmacocinético | Arzneimittel-Forschung | Niveles de etofenamato en suero y líquido sinovial tras iontoforesis (11 pacientes con lumbalgia y 13 con sinovitis de rodilla): demuestra penetración en el espacio articular, pero no evalúa eficacia en espondilitis anquilosante |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 55701 | Flogoprofen 50 mg/ml solución para pulverización cutánea | Solución para pulverización cutánea | No disponible |
| 56338 | Actromagel 50 mg/g gel | Gel | No disponible |
| 84578 | Flogopatch 70 mg apósito adhesivo medicamentoso | Parche cutáneo | No disponible |
| 55380 | Flogoprofen 50 mg/g gel | Gel | No disponible |
| 54646 | Zenavan 50 mg/g gel | Gel | No disponible |

Las cinco autorizaciones están vigentes y corresponden a formulaciones de un solo principio activo, de uso tópico (gel, solución para pulverización y parche cutáneo).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas ni contraindicaciones derivadas del grafo de conocimiento.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal se sustenta únicamente en el puntaje del modelo (nivel L5), sin ensayos ni literatura, y además corresponde a una etiqueta de susceptibilidad genética, no a una enfermedad tratable. La vía tópica también limita su utilidad en enfermedad axial. Entre las demás predicciones, solo la espondilitis anquilosante (L4) y la artritis idiopática juvenil poliarticular merecen consideración como preguntas de investigación.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), actualmente pendiente y bloqueante para el cribado de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Replantear la indicación objetivo hacia una condición clínica definida (p. ej., espondilitis anquilosante) y buscar estudios de eficacia
- Evaluar la compatibilidad de la vía de administración tópica con la enfermedad objetivo
- En el caso pediátrico, establecer seguridad y dosificación antes de cualquier consideración
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

