---
layout: default
title: Teprotumumab
parent: 僅模型預測 (L5)
nav_order: 274
evidence_level: L5
indication_count: 10
---

# Teprotumumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Teprotumumab: Indicación Original No Disponible → Monosomy X (Señal Predictiva sin Evidencia de Respaldo)

## Resumen en Una Frase

Este Evidence Pack no contiene información sobre la indicación original aprobada de teprotumumab (sin licencias registradas ni datos de indicación en la fuente consultada). El modelo TxGNN predice una posible asociación con **Monosomy X**, pero esta direccion actualmente no cuenta con **ningun ensayo clinico** ni **ninguna publicacion** de respaldo, y el propio analisis mecanistico incluido en el paquete indica que la logica farmacologica apunta en sentido contrario al beneficio clinico esperado.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | No disponible en la fuente consultada (DrugBank); no hay licencias registradas en España |
| Nueva Indicacion Predicha | Monosomy X |
| Puntaje de Prediccion TxGNN | 99.79% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion original de teprotumumab en este Evidence Pack (campo marcado como dato pendiente). Sin embargo, el propio analisis mecanistico incluido junto a las predicciones identifica a teprotumumab como un **antagonista de IGF-1R** que inhibe la senalizacion de IGF-1.

Para Monosomy X (cariotipo asociado al Sindrome de Turner), el analisis incluido en el paquete señala que esta prediccion probablemente **no es aplicable**: el retraso de crecimiento propio de esta poblacion se trata clasicamente con terapias que *suplementan* la señal de IGF-1/hormona de crecimiento, mientras que teprotumumab actua en direccion opuesta, *bloqueando* dicha señal. El propio analisis atribuye el puntaje alto a una similitud de "embedding" entre enfermedades del mismo grupo (cariotipos X: monosomy X, mosaic monosomy X, Turner syndrome, mixed gonadal dysgenesis, X chromosome number anomaly), es decir, a un **efecto de agrupamiento estructural del grafo** y no a una relacion farmacologica real.

En conjunto, las 10 indicaciones predichas en este paquete (que incluyen ademas varices esofagicas, disgenesia gonadal mixta y trastornos mitocondriales) comparten el mismo patron: puntajes TxGNN muy altos (>99%) pero **sin ningun mecanismo de soporte independiente**, sin ensayos clinicos y sin literatura, y en el caso especifico de los cariotipos X, con una direccion mecanistica potencialmente contraria al beneficio clinico. Esto sugiere que el conjunto debe tratarse como señales exploratorias de bajo nivel de confianza, no como candidatos de reposicionamiento con respaldo cientifico.

---

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados (búsqueda en ClinicalTrials.gov e ICTRP sin resultados para las 10 indicaciones evaluadas).

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible (búsqueda en PubMed sin resultados para las 10 indicaciones evaluadas).

---

## Informacion de Mercado en España

Teprotumumab no está comercializado en España; no existen autorizaciones registradas en la fuente consultada.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Otras Indicaciones Predichas Consideradas

Todas las indicaciones predichas en este paquete presentan el mismo nivel de evidencia (L5) y la misma recomendación (Hold):

| Rango | Indicacion | Puntaje TxGNN | Observacion |
|------|-----------|--------------|-------------|
| 1 | Monosomy X | 99.79% | Mecanismo opuesto al beneficio clinico esperado |
| 2 | Esophageal varices with bleeding | 99.64% | Sin hipotesis mecanistica publicada |
| 3 | Esophageal varices without bleeding | 99.64% | Mismo grupo que #2, sin evidencia independiente |
| 4 | Mixed gonadal dysgenesis | 99.50% | Sin vinculo patologico conocido con IGF-1R |
| 5 | Mitochondrial oxidative phosphorylation disorder | 99.44% | Sin interseccion conocida con la via del farmaco |
| 6 | Turner syndrome (X estructural) | 99.37% | Direccion mecanistica opuesta a la necesidad clinica |
| 7 | Mosaic monosomy X | 99.37% | Mismo grupo que #1 y #6 |
| 8 | Sex chromosome disorder of sex development | 99.34% | Nodo de categoria superior del mismo cluster |
| 9 | Varicose disease | 99.33% | Mismo cluster vascular que #2 y #3 |
| 10 | X chromosome number anomaly | 99.32% | Nodo estructural del mismo cluster de cariotipo X |

---

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
Ninguna de las 10 indicaciones predichas cuenta con ensayos clinicos, literatura o mecanismo de soporte independiente; el propio analisis del paquete atribuye los puntajes altos a agrupamiento estructural en el grafo de enfermedades (clusters de cariotipo X y de patologia vascular), y en el caso de la indicacion principal (Monosomy X) señala una posible direccion mecanistica contraria al beneficio clinico esperado.

**Para avanzar se necesita:**
- Datos del prospecto/TFDA (advertencias, contraindicaciones, DDI) — actualmente bloqueante para cualquier evaluacion de seguridad (S1)
- Confirmacion del mecanismo de accion original desde fuente regulatoria (DrugBank API u otra fuente primaria)
- Confirmacion de la indicacion original aprobada del farmaco, ausente en este paquete
- Si se desea continuar explorando reposicionamiento, priorizar busqueda de literatura/ensayos en indicaciones con hipotesis mecanistica plausible (p. ej. enfermedad tiroidea ocular relacionada con IGF-1R), en lugar de las señales de cluster identificadas aqui
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

