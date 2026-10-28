---
layout: default
title: Insulin Glargine
parent: Solo predicción del modelo (L5)
nav_order: 420
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
monitor_inn: "Insulin glargine"
predicted_indications: ["autoimmune oophoritis", "thiamine-responsive dysfunction syndrome", "classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "pancreatic agenesis", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy"]
description: "Insulin Glargine: nueva indicación predicha, Ooforitis autoinmune (autoimmune oophoritis) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Insulin Glargine
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

## Insulin Glargine: Ooforitis autoinmune (autoimmune oophoritis)
{: .text-alpha }

## Resumen en Una Frase

Insulina glargina es una insulina basal de acción prolongada, utilizada originalmente para el tratamiento de la diabetes mellitus (tipo 1 y tipo 2).
El modelo TxGNN predice que podría ser efectiva para **ooforitis autoinmune**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Ooforitis autoinmune (autoimmune oophoritis) |
| Puntaje de Predicción TxGNN | 0.9988 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 7 de 16) |
| Número de Autorizaciones | 16 (vigentes: 7) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la insulina glargina es un análogo de insulina de acción prolongada que reemplaza la insulina endógena y regula el metabolismo de la glucosa. Su eficacia en la diabetes está comprobada.

No existe un vínculo mecanístico directo con la ooforitis autoinmune. La puntuación alta proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. Las posibles conexiones, como la señalización de la insulina en las células de la granulosa ovárica o la coexistencia de autoinmunidad endocrina poliglandular con la diabetes tipo 1, son plausibles pero especulativas.

La insulina glargina es una terapia de reemplazo metabólico y no tiene acción inmunomoduladora que pueda tratar la destrucción ovárica autoinmune. Por ello, la predicción debe considerarse con cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 16 autorizaciones vigentes (todas de principio activo único). El texto de indicación aprobada no figura en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 00134007 | Lantus 100 unidades/ml solución inyectable en un cartucho | Solución inyectable en cartucho | No disponible |
| 00134002 | Lantus 100 unidades/ml solución inyectable en un vial | Solución inyectable | No disponible |
| 1181270003 | Semglee 100 unidades/ml solución inyectable en pluma precargada | Solución inyectable | No disponible |
| 100133034 | Toujeo 300 unidades/ml SoloStar solución inyectable en pluma precargada | Solución inyectable en pluma precargada | No disponible |
| 1252000002 | Ondibta 100 unidades/ml solución inyectable en pluma precargada | Solución inyectable en pluma precargada | No disponible |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; la mayoría de las principales son de nivel moderado. Ejemplos:
  - Agentes simpaticomiméticos y broncodilatadores: fenilefrina, pseudoefedrina, epinefrina, salbutamol, formoterol.
  - Betabloqueantes: acebutolol.
  - Otros antidiabéticos (riesgo de hipoglucemia o efectos aditivos): metformina, pioglitazona, alogliptina, albiglutida.
  - Corticoides: hidrocortisona (moderada); hidrocortisona tópica y alclometasona tópica (leves).
  - Otros: acetazolamida, doxiciclina, etinilestradiol, estradiol, hidroclorotiazida, etanol, alpelisib.
- **Señal de seguridad relevante**: las inyecciones de insulina se asocian a lipodistrofia localizada (lipohipertrofia o lipoatrofia) en el sitio de inyección. Varias de las indicaciones predichas (lipodistrofias localizadas) probablemente reflejan este efecto adverso y no un beneficio terapéutico.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (L5), sin ensayos clínicos ni literatura, y no hay un mecanismo plausible: la insulina glargina no tiene acción inmunomoduladora frente a la destrucción ovárica autoinmune. Las demás indicaciones predichas parecen reflejar comorbilidad con la diabetes o efectos adversos conocidos de la insulina. La única con respaldo indirecto es la agenesia pancreática (nivel L4), que es en esencia la misma fisiopatología de déficit de insulina ya cubierta por la indicación original.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank.
- Advertencias y contraindicaciones del prospecto de la AEMPS.
- Textos de indicación aprobada de las autorizaciones españolas.
- Evidencia preclínica o clínica que vincule la insulina con la ooforitis autoinmune.
- Si se busca priorizar otra indicación, evaluar la agenesia pancreática como pregunta de investigación, reconociendo que no es un reposicionamiento genuino.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

