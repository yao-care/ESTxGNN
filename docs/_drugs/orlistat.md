---
layout: default
title: Orlistat
parent: 僅模型預測 (L5)
nav_order: 205
evidence_level: L5
indication_count: 1
---

# Orlistat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Orlistat: De Indicación Original No Documentada a Hipervitaminosis

## Resumen en Una Frase

Orlistat (DB01083) es un inhibidor de la lipasa intestinal cuya indicación original no está documentada en este Evidence Pack (dato pendiente de confirmación). El modelo TxGNN predice una posible relación con **Hipervitaminosis**, pero actualmente **no existe ningún ensayo clínico ni publicación** que respalde esta dirección — se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No documentada en esta Evidence Pack |
| Nueva Indicación Predicha | Hipervitaminosis |
| Puntaje de Predicción TxGNN | 99.42% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos formales sobre el mecanismo de acción (MOA) ni sobre la indicación original de orlistat en esta Evidence Pack. Sin embargo, el propio análisis de TxGNN aporta una hipótesis mecanística: orlistat es un inhibidor de la lipasa intestinal que bloquea la hidrólisis de triglicéridos, reduciendo la absorción intestinal de grasas y, de forma asociada, la absorción de vitaminas liposolubles (A, D, E, K).

A partir de ahí, el modelo plantea que este mismo mecanismo podría reducir las concentraciones plasmáticas de vitaminas liposolubles en cuadros de exceso (hipervitaminosis A/D/E/K). Es importante señalar que esta es una aplicación **inversa** del mecanismo conocido: el efecto adverso característico de orlistat en la práctica clínica es precisamente causar **déficit** de vitaminas liposolubles, no tratar su exceso. No existe ningún estudio experimental o clínico que valide esta hipótesis, y al no contar con la indicación original ni el MOA confirmados, no es posible realizar una validación cruzada. Esta predicción debe interpretarse como una hipótesis generativa de baja confianza, no como una relación mecanística establecida.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Orlistat no está comercializado en España según los registros consultados (0 autorizaciones).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. La obtención del prospecto TFDA (vigilancia de advertencias y contraindicaciones) es actualmente un vacío de datos de severidad **bloqueante**, lo que impide una evaluación de seguridad inicial (S1).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia corresponde al nivel L5 (predicción de modelo sin estudios reales que la respalden), sin ensayos clínicos ni literatura de apoyo. Además, la propia hipótesis mecanística es una aplicación inversa del efecto adverso conocido del fármaco, y falta información básica sobre indicación original, MOA y seguridad (TFDA), lo que impide avanzar a fases de evaluación posteriores.

**Para avanzar se necesita:**
- Prospecto TFDA (advertencias/contraindicaciones) — actualmente bloqueante
- Confirmación del mecanismo de acción (MOA) vía DrugBank u otra fuente primaria
- Indicación(es) original(es) documentada(s)
- Al menos un estudio preclínico o de mecanismo que valide la hipótesis antes de buscar evidencia clínica
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

