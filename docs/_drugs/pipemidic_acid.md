---
layout: default
title: Pipemidic Acid
parent: Solo predicción del modelo (L5)
nav_order: 641
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
monitor_inn: "pipemidic acid"
predicted_indications: ["heart disease", "Laubry-Pezzi syndrome", "Pierre Robin syndrome associated with a chromosomal anomaly", "genetic syndromic Pierre Robin syndrome", "partial deletion of the long arm of chromosome 7", "orofacial clefting syndrome", "pulmonary valve disease", "disorder of fucoglycosan synthesis", "mitral valve disease", "Jeune syndrome situs inversus"]
description: "Pipemidic Acid: nueva indicación predicha, Heart disease (nivel de evidencia L5). Indicación original: No consta en los datos locales"
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

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Pipemidic Acid: Heart disease
{: .text-alpha }

## Resumen en Una Frase

El ácido pipemídico es un antibacteriano de la familia de las quinolonas; actualmente no está comercializado en España (solo constan autorizaciones canceladas) y los datos compilados no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **enfermedad cardíaca**, pero **no hay ensayos clínicos** y solo **1 publicación indirecta** (de 1978) relacionada con esta dirección, que no demuestra eficacia cardíaca.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Heart disease |
| Puntaje de Predicción TxGNN | 0.9993 |
| Nivel de Evidencia | L5 (solo predicción del modelo; la única publicación es indirecta y no respalda la indicación) |
| Estado de Mercado en España | No comercializado (registros anulados: 1 de 1) |
| Número de Autorizaciones | 1 (vigentes: 0) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, el ácido pipemídico es una quinolona antibacteriana que inhibe la ADN girasa y la topoisomerasa IV bacterianas, y se ha utilizado como antibiótico, en particular en infecciones urinarias.

**No se identifica un vínculo mecanístico plausible** con la enfermedad cardíaca. No se conoce una diana cardíaca directa para este fármaco. La única publicación asociada (1978) describe su uso como antibiótico extraurinario en insuficiencia renal y hemodiálisis; se trata de un contexto de uso y farmacocinética antibacteriana, no de evidencia de eficacia en cardiopatías.

El puntaje elevado de TxGNN (0,9993) proviene de una predicción del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni clínica. Además, las quinolonas como clase presentan señales de seguridad cardíaca (p. ej., prolongación del intervalo QT y advertencias de aneurisma/disección aórtica), lo que aconseja cautela.

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

