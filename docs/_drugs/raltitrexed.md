---
layout: default
title: Raltitrexed
parent: Solo predicción del modelo (L5)
nav_order: 234
evidence_level: L5
indication_count: 10
---

# Raltitrexed
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

# Raltitrexed: De Quimioterapia Antimetabolito a Colangitis Esclerosante

## Resumen en Una Frase

Raltitrexed es un fármaco citotóxico antimetabolito (inhibidor de la timidilato sintetasa) cuya indicación original aprobada no está confirmada en los datos actualmente disponibles.
El modelo TxGNN predice que podría ser efectivo para **Colangitis Esclerosante**,
pero actualmente **no existen ensayos clínicos ni publicaciones** que respalden esta direccion — la puntuación proviene únicamente del modelo predictivo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (datos de ficha técnica/DrugBank aún no recopilados; solo se conoce que pertenece a la clase de quimioterapia antimetabolito) |
| Nueva Indicación Predicha | Colangitis Esclerosante (sclerosing cholangitis) |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción confirmados por ficha técnica (data gap de severidad "High"). Según la información disponible en el análisis del modelo, raltitrexed es un inhibidor de la timidilato sintetasa (TS), un fármaco citotóxico antimetabolito de la familia de las fluoropirimidinas, cuya eficacia se ha demostrado históricamente en quimioterapia oncológica.

La colangitis esclerosante es una enfermedad autoinmune/fibrótica de la vía biliar, mecanísticamente muy distinta de los tumores sólidos en los que este tipo de fármacos suele emplearse. Según el propio análisis de la predicción, el vínculo mecanístico es "extremadamente indirecto": se especula un posible efecto antiproliferativo/antifibrótico, pero **sin ningún dato mecanístico, preclínico o de literatura que lo respalde**.

En conjunto, esta predicción se apoya únicamente en la similitud de embeddings del modelo TxGNN, no en una hipótesis biológica sólida. La ausencia total de ensayos clínicos y literatura relacionada (ver secciones siguientes) refuerza que esta es una hipótesis exploratoria de nivel de evidencia mínimo (L5).

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Raltitrexed no está comercializado en España según los datos actuales (0 autorizaciones registradas). No hay información de producto, forma farmacéutica ni indicación aprobada disponible para tabular.

---

## Citotoxicidad

Raltitrexed pertenece a la clase de quimioterapia citotóxica antimetabolito (inhibidor de timidilato sintetasa, familia de fluoropirimidinas), por lo que aplica esta sección.

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (inhibidor de la timidilato sintetasa, clase antimetabolito) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto (dato de seguridad específico aún no disponible; los antimetabolitos de esta clase suelen asociarse a mielosupresión) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma completo, función hepática y renal (monitoreo estándar esperado para agentes citotóxicos; no confirmado por ficha técnica local) |
| Protección en Manejo | Debe seguir las normativas de manejo de fármacos citotóxicos; pendiente de confirmación con ficha técnica oficial |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún ensayo clínico ni publicación que respalde la predicción de colangitis esclerosante (ni ninguna de las otras 9 indicaciones predichas, todas con nivel de evidencia L5 y etapa de decisión S0). Además, faltan datos críticos de seguridad (advertencias, contraindicaciones, DDI) marcados como brecha bloqueante (Blocking), lo que impide una evaluación de seguridad inicial (S1).

**Para avanzar se necesita:**
- Ficha técnica/prospecto oficial (advertencias, contraindicaciones, DDI) — brecha bloqueante actual
- Confirmación del mecanismo de acción (MOA) y de la indicación original vía DrugBank/regulador
- Búsqueda ampliada de literatura preclínica sobre efecto antifibrótico/antiproliferativo en enfermedad biliar autoinmune, dado que el vínculo mecanístico actual es especulativo
- Reevaluación tras la aparición de al menos evidencia preclínica (L4) antes de considerar cualquier avance
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

