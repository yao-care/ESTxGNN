---
layout: default
title: Vismodegib
parent: 僅模型預測 (L5)
nav_order: 294
evidence_level: L5
indication_count: 10
---

# Vismodegib
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

# Vismodegib: De Carcinoma Basocelular a Meduloblastoma con Nodularidad Extensa

## Resumen en Una Frase

Vismodegib es un inhibidor oral de la via Hedgehog (antagonista de SMO), originalmente aprobado para el carcinoma basocelular localmente avanzado o metastasico. El modelo TxGNN predice que podria ser efectivo para **Meduloblastoma con Nodularidad Extensa** (subtipo SHH-activado), con una puntuacion del **99.93%**, pero actualmente **no hay ensayos clinicos ni publicaciones especificas** en este Evidence Pack que respalden directamente esta asociacion — la base es unicamente mecanistica.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Carcinoma basocelular localmente avanzado o metastasico |
| Nueva Indicacion Predicha | Meduloblastoma con nodularidad extensa |
| Puntaje de Prediccion TxGNN | 99.93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion en la ficha del farmaco (campo MOA marcado como vacio). Segun la literatura disponible en este mismo Evidence Pack, vismodegib es un inhibidor de la via Hedgehog que se une a Smoothened (SMO), bloqueando la activacion aberrante de esta via de senalizacion y la proliferacion tumoral asociada; fue el primer farmaco de esta clase aprobado para carcinoma basocelular.

La nueva indicacion predicha, meduloblastoma con nodularidad extensa, corresponde a un subtipo de meduloblastoma **SHH-activado** (dependiente de la misma via Sonic Hedgehog/SMO que el carcinoma basocelular). Existe por tanto una logica mecanistica compartida entre ambas indicaciones: en ambos casos el tumor depende de una activacion anomala de la via Hedgehog, lo que en principio haria a vismodegib farmacologicamente aplicable.

Sin embargo, esta relacion es puramente una inferencia mecanistica del modelo. No se han identificado en este Evidence Pack ensayos clinicos ni literatura que evaluen directamente vismodegib en este subtipo especifico de meduloblastoma, por lo que la asociacion debe considerarse una hipotesis de investigacion, no una evidencia clinica.

---

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Citotoxicidad

Vismodegib es un farmaco antineoplasico (indicacion original oncologica, carcinoma basocelular), por lo que aplica esta seccion.

| Item | Contenido |
|------|------|
| Clasificacion de Citotoxicidad | Terapia dirigida (inhibidor de la via Hedgehog/SMO), no es quimioterapia citotoxica convencional |
| Riesgo de Mielosupresion | Consultar las advertencias y precauciones del prospecto (sin datos de toxicidad en este informe) |
| Clasificacion de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Proteccion en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

---

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La prediccion tiene una puntuacion TxGNN elevada (99.93%) y una racional mecanistica coherente (via Hedgehog/SMO compartida entre carcinoma basocelular y meduloblastoma SHH-activado), pero no cuenta con ningun ensayo clinico ni publicacion especifica en este Evidence Pack (Nivel de Evidencia L5). Sin datos reales, no se justifica avanzar mas alla de la fase de hipotesis de investigacion.

**Para avanzar se necesita:**
- Datos del mecanismo de accion (MOA) desde DrugBank (actualmente vacio)
- Ficha tecnica/prospecto de la AEMPS con advertencias, contraindicaciones e interacciones (actualmente vacio, marcado como bloqueante)
- Busqueda dirigida de ensayos clinicos y literatura sobre vismodegib especificamente en meduloblastoma SHH-activado o con nodularidad extensa
- Evaluacion adicional de otras indicaciones predichas con evidencia mas solida detectadas en el mismo lote (p. ej. la asociacion con "skin cancer", que ya cuenta con 23 ensayos clinicos y 20 publicaciones, aunque coincide en gran medida con la indicacion original)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

