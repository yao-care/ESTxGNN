---
layout: default
title: Pipemidic Acid
parent: Solo predicción del modelo (L5)
nav_order: 641
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Pipemidic Acid: nueva indicación predicha, Enfermedad cardíaca (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (el texto de indicación de la a…"
---

# Pipemidic Acid
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

# Ácido pipemídico: De Indicación No Registrada a Enfermedad Cardíaca

## Resumen en Una Frase

El ácido pipemídico es un antibacteriano de la familia de las quinolonas, comercializado en España como GALUSAN CÁPSULAS; los datos compilados no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **enfermedad cardíaca**, pero **no hay ensayos clínicos** y solo **1 publicación indirecta** (de 1978) relacionada con esta dirección, que no demuestra eficacia cardíaca.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (el texto de indicación de la autorización está vacío) |
| Nueva Indicación Predicha | Enfermedad cardíaca |
| Puntaje de Predicción TxGNN | 99,93% |
| Nivel de Evidencia | L5 (solo predicción del modelo; la única publicación es indirecta y no respalda la indicación) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, el ácido pipemídico es una quinolona antibacteriana que inhibe la ADN girasa y la topoisomerasa IV bacterianas, y se ha utilizado como antibiótico, en particular en infecciones urinarias.

**No se identifica un vínculo mecanístico plausible** con la enfermedad cardíaca. No se conoce una diana cardíaca directa para este fármaco. La única publicación asociada (1978) describe su uso como antibiótico extraurinario en insuficiencia renal y hemodiálisis; se trata de un contexto de uso y farmacocinética antibacteriana, no de evidencia de eficacia en cardiopatías.

El puntaje elevado de TxGNN (0,999) proviene de una predicción basada en grafos de conocimiento y no constituye evidencia clínica. Además, las quinolonas como clase presentan señales de seguridad cardíaca (p. ej., prolongación del intervalo QT y advertencias de aneurisma/disección aórtica), lo que aconseja cautela.

Otras predicciones del modelo (síndrome de Laubry-Pezzi, síndromes de Pierre Robin, deleción parcial del brazo largo del cromosoma 7, síndrome de fisura orofacial, valvulopatías pulmonar y mitral, trastorno de síntesis de fucoglicanos, síndrome de Jeune con situs inversus) tampoco presentan vínculo mecanístico plausible, ensayos ni literatura pertinente. Se trata de predicciones puramente computacionales.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [372558](https://pubmed.ncbi.nlm.nih.gov/372558/) | 1978 | Informe de uso clínico (indirecto) | Journal d'urologie et de nephrologie | Uso del ácido pipemídico como antibiótico extraurinario en insuficiencia renal y hemodiálisis; no aborda enfermedad cardíaca |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 55224 | GALUSAN CAPSULAS | Cápsula dura | No disponible en los datos compilados |

Titular: Laboratorios Almirall S.L. Estado: vigente (monofármaco).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Los datos compilados no incluyen advertencias ni contraindicaciones del prospecto de la AEMPS, ni se encontraron interacciones farmacológicas registradas.

Como consideración de clase (no proveniente del prospecto), las quinolonas se asocian con señales de seguridad cardiovascular, como prolongación del QT y riesgo de aneurisma/disección aórtica, relevantes si se plantease su uso en pacientes cardíacos.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo (L5): no hay ensayos clínicos, la única publicación es indirecta y no existe vínculo mecanístico plausible entre un antibacteriano inhibidor de girasa y la enfermedad cardíaca. Además, las señales de seguridad cardíaca de las quinolonas aumentan el riesgo.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicación aprobada), cuya ausencia bloquea el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Identificar una hipótesis mecanística o evidencia preclínica que relacione el fármaco con alguna cardiopatía concreta.
- Evaluar el perfil de seguridad cardiovascular de las quinolonas antes de cualquier consideración adicional.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

