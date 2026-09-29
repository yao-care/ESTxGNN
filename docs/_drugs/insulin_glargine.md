---
layout: default
title: Insulin Glargine
parent: Solo predicción del modelo (L5)
nav_order: 282
evidence_level: L5
indication_count: 10
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

# Insulina glargina: De Diabetes Mellitus a Ooforitis Autoinmune

## Resumen en Una Frase

La insulina glargina es una insulina basal de acción prolongada, utilizada habitualmente para el control de la glucemia en la diabetes mellitus. El modelo TxGNN predice que podría ser efectiva para la **ooforitis autoinmune**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción. Se trata de una señal puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Diabetes mellitus (uso conocido del fármaco; las autorizaciones de AEMPS del paquete no incluyen el texto de indicación) |
| Nueva Indicación Predicha | Ooforitis autoinmune |
| Puntaje de Predicción TxGNN | 99,88% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 16 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la insulina glargina es un análogo de insulina basal que actúa sobre el receptor de insulina para regular el metabolismo de la glucosa. Su eficacia en la diabetes está establecida.

La ooforitis autoinmune es un trastorno ovárico de origen inmunomediado. No se identifica un mecanismo plausible por el cual regular la glucosa mediante el receptor de insulina pueda tratar una enfermedad autoinmune ovárica. El puntaje alto (0,9988) proviene solo de asociaciones en el grafo de conocimiento, sin ensayos ni literatura de apoyo. Por ello, esta predicción debe considerarse sin respaldo mecanístico hasta que se demuestre lo contrario.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 16 autorizaciones. El texto de indicación aprobada está vacío en los datos recibidos, por lo que no se incluye.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 00134007 | LANTUS 100 unidades/ml solución inyectable en un cartucho | Solución inyectable en cartucho |
| 00134002 | LANTUS 100 unidades/ml solución inyectable en un vial | Solución inyectable |
| 1181270003 | SEMGLEE 100 unidades/ml solución inyectable en pluma precargada | Solución inyectable |
| 100133034 | TOUJEO 300 unidades/ml SoloStar solución inyectable en pluma precargada | Solución inyectable en pluma precargada |
| 1252000002 | ONDIBTA 100 unidades/ml solución inyectable en pluma precargada | Solución inyectable en pluma precargada |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe evidencia clínica ni bibliográfica, ni un mecanismo plausible que vincule la insulina glargina con la ooforitis autoinmune. El puntaje TxGNN por sí solo no basta para avanzar.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS para completar advertencias y contraindicaciones (brecha bloqueante para el cribado de seguridad).
- Obtener el mecanismo de acción desde DrugBank para poder evaluar el vínculo mecanístico.
- Una búsqueda bibliográfica dirigida a insulina y ooforitis autoinmune que justifique reabrir el caso.
- Revisar el resto de predicciones del paquete:
  - **Agenesia pancreática** (nivel L4, etapa S1): la sustitución con insulina basal es mecanísticamente racional, pero es terapia de reemplazo y no reposicionamiento. La literatura aportada es indirecta.
  - **Lipodistrofias localizadas** (incluida la inducida por fármacos): probablemente reflejan un efecto adverso conocido de la insulina inyectada, es decir, una señal de seguridad y no una indicación.
  - **Síndrome de la persona rígida, síndrome sensible a tiamina y otras**: la asociación parece derivar de la diabetes comórbida, por lo que la insulina trataría solo ese componente.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

