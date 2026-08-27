---
layout: default
title: Tivozanib
parent: 僅模型預測 (L5)
nav_order: 278
evidence_level: L5
indication_count: 10
---

# Tivozanib
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

# Tivozanib: De Indicación Original No Documentada a Carcinoma Endocervical

## Resumen en Una Frase

La indicación original de tivozanib no está documentada en este Evidence Pack (solo se consultó DrugBank y el campo de mecanismo de acción quedó como vacío de datos). El modelo TxGNN predice que podría ser efectivo para **Carcinoma Endocervical**, junto con otras nueve neoplasias ginecológicas de puntaje similar, pero **sin ningún ensayo clínico ni publicación** que respalde actualmente esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No documentada en este Evidence Pack |
| Nueva Indicación Predicha | Carcinoma Endocervical (endocervical carcinoma) |
| Puntaje de Predicción TxGNN | 99.81% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✗ No Comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de tivozanib. La única información confirmada en este Evidence Pack es el identificador DrugBank (DB11800) y el nombre INN; ni la indicación original ni la clase terapéutica pudieron extraerse de la consulta realizada.

Sin datos de MOA ni de indicación original, no es posible establecer una relación mecanística verificable entre el uso previo del fármaco y las indicaciones predichas. Se observa, eso sí, un patrón en los datos: las 10 indicaciones predichas por TxGNN (rangos 3894–4500, puntajes entre 99.76% y 99.81%) corresponden todas a subtipos de neoplasias ginecológicas (cérvix, ligamento uterino), lo que sugiere que el modelo detectó alguna señal compartida entre estas entidades. Sin embargo, esta observación es puramente estadística y no está respaldada por ningún mecanismo farmacológico confirmado ni por evidencia clínica o de literatura.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

No hay autorizaciones registradas (el fármaco figura como no comercializado, 0 licencias).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> Nota: existe una brecha de datos de severidad **Blocking** (DG001 — advertencias/contraindicaciones del prospecto TFDA) que impide actualmente completar la evaluación de seguridad inicial (S1).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Las 10 indicaciones predichas se sustentan únicamente en el puntaje del modelo TxGNN (nivel de evidencia L5), sin ningún ensayo clínico ni publicación de respaldo, y el fármaco no está comercializado en España. Además, la ausencia de datos de mecanismo de acción y de advertencias/contraindicaciones del prospecto (gap bloqueante) impide avanzar a la fase de evaluación de seguridad.

**Para avanzar se necesita:**
- Indicación original y mecanismo de acción (MOA) de tivozanib, actualmente en falta
- Prospecto/advertencias TFDA (gap bloqueante DG001) para poder iniciar la evaluación de seguridad S1
- Evidencia clínica real (ensayos o literatura) para al menos una de las 10 indicaciones predichas
- Categorías terapéuticas de DrugBank, para determinar si aplica evaluación de citotoxicidad
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

