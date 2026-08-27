---
layout: default
title: Voxelotor
parent: 僅模型預測 (L5)
nav_order: 296
evidence_level: L5
indication_count: 7
---

# Voxelotor
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Voxelotor: De Indicación Original No Documentada a Trombocitopenia Hereditaria con Plaquetas Normales

## Resumen en Una Frase

La indicación original de Voxelotor no está disponible en este Evidence Pack (ni el mecanismo de acción ni las indicaciones aprobadas fueron extraídas de DrugBank).
El modelo TxGNN predice que podría ser efectivo para **Trombocitopenia Hereditaria con Plaquetas Normales**,
pero actualmente **no existen ensayos clínicos ni publicaciones** que respalden esta ni ninguna de las otras 6 hipótesis generadas en este mismo lote.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | No disponible en el Evidence Pack (dato pendiente de extracción) |
| Nueva Indicacion Predicha | Trombocitopenia Hereditaria con Plaquetas Normales |
| Puntaje de Prediccion TxGNN | 99.58% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Espana | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos sobre el mecanismo de acción de Voxelotor ni de su indicación original documentada en este Evidence Pack, por lo que no es posible establecer una base mecanística para evaluar la plausibilidad de esta predicción.

TxGNN generó, en este mismo lote, 7 hipótesis relacionadas con trastornos hematológicos poco frecuentes de las plaquetas (trombocitopenias hereditarias, enfermedad de gránulos densos, trastorno de liberación plaquetaria) y una relacionada con patología renal asociada a gammapatía monoclonal (síndrome de Fanconi). Todas presentan puntuaciones de similitud topológica muy altas (>99%), pero esto refleja únicamente cercanía estructural dentro del grafo de conocimiento, no evidencia mecanística ni clínica real.

Sin datos de MOA ni de indicación original, no es posible argumentar por qué el fármaco sería aplicable a estas nuevas indicaciones; la relación observada debe considerarse exploratoria y pendiente de validación completa.

## Otras Hipotesis Generadas por TxGNN (Mismo Lote)

| Rank | Indicacion | Puntaje TxGNN | Evidencia |
|------|-----------|---------------|-----------|
| 2 | Macrotrombocitopenia con Insuficiencia Mitral | 99.58% | Ninguna |
| 3 | Enfermedad de Gránulos Densos | 99.58% | Ninguna |
| 4 | Trombocitopenia Neonatal Transitoria | 99.57% | Ninguna |
| 5 | Trombocitopenia | 99.51% | Ninguna |
| 6 | Síndrome de Fanconi Asociado a Cadena Ligera Ig Monoclonal Adquirida | 99.13% | Ninguna |
| 7 | Trastorno Primario de Liberación Plaquetaria | 99.00% | Ninguna |

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
Las 7 indicaciones predichas se encuentran en Nivel de Evidencia L5 (solo predicción del modelo, sin ningún ensayo clínico ni publicación de respaldo), y faltan datos fundamentales sobre indicación original, mecanismo de acción y seguridad. El fármaco tampoco está comercializado en España. No hay base suficiente para avanzar más allá de la etapa exploratoria.

**Para avanzar se necesita:**
- Extracción completa de indicación original y MOA desde DrugBank (actualmente marcado como brecha de datos High, DG002)
- Obtención de advertencias, contraindicaciones y DDI del prospecto/TFDA (brecha bloqueante, DG001)
- Búsqueda dirigida de literatura preclínica o mecanística que vincule Voxelotor con trastornos plaquetarios, dado que la vía de descubrimiento actual (TxGNN) no aportó evidencia clínica ni bibliográfica
- Reevaluación una vez cerradas estas brechas antes de considerar cualquier paso hacia S1
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

