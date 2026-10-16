---
layout: default
title: Insulin Glargine
parent: Solo predicción del modelo (L5)
nav_order: 420
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Insulin Glargine: nueva indicación predicha, Ooforitis autoinmune (nivel de evidencia L5). Indicación original: Diabetes mellitus tipo 2 (también diabetes mellitus tipo 1 y cetoacid…"
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

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Insulina glargina: De Diabetes mellitus tipo 2 a Ooforitis autoinmune

## Resumen en Una Frase

Insulina glargina es una insulina basal de acción prolongada, utilizada originalmente para el tratamiento de la diabetes mellitus (tipo 1 y tipo 2).
El modelo TxGNN predice que podría ser efectiva para **ooforitis autoinmune**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Diabetes mellitus tipo 2 (también diabetes mellitus tipo 1 y cetoacidosis diabética, según el grafo de conocimiento) |
| Nueva Indicación Predicha | Ooforitis autoinmune |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 16 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la insulina glargina es un análogo de insulina de acción prolongada que reemplaza la insulina endógena y regula el metabolismo de la glucosa. Su eficacia en la diabetes está comprobada.

No existe un vínculo mecanístico directo con la ooforitis autoinmune. La puntuación alta es una predicción basada únicamente en el grafo de conocimiento. Las posibles conexiones, como la señalización de la insulina en las células de la granulosa ovárica o la coexistencia de autoinmunidad endocrina poliglandular con la diabetes tipo 1, son plausibles pero especulativas.

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

