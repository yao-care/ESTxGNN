---
layout: default
title: Lusutrombopag
parent: 僅模型預測 (L5)
nav_order: 175
evidence_level: L5
indication_count: 10
---

# Lusutrombopag
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

# LUSUTROMBOPAG: De Trombocitopenia a Trombocitopenia Hereditaria con Plaquetas Normales

## Resumen en Una Frase

Lusutrombopag es un agonista del receptor de trombopoyetina (TPO-RA); su indicación original detallada y su mecanismo de acción completo no están disponibles en las fuentes consultadas (brecha de datos bloqueante). El modelo TxGNN predice que podría ser efectivo para **Trombocitopenia Hereditaria con Plaquetas Normales**, con una puntuación de **99.995%**, pero actualmente **no existe ningún ensayo clínico ni publicación** que respalde esta dirección.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | No disponible en las fuentes consultadas (clase farmacológica: agonista del receptor de TPO) |
| Nueva Indicacion Predicha | Trombocitopenia Hereditaria con Plaquetas Normales |
| Puntaje de Prediccion TxGNN | 99.995% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Espana | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de Lusutrombopag (brecha de datos DG002, severidad Alta). Según la información disponible en el análisis de reposicionamiento, Lusutrombopag es un **agonista del receptor de trombopoyetina (TPO-RA)**, clase farmacológica que estimula la proliferación y maduración de megacariocitos para incrementar el recuento plaquetario, de forma análoga a otros fármacos de la clase como eltrombopag o romiplostim.

Sin embargo, el vínculo mecanístico con la indicación predicha es débil. El propio nombre de la enfermedad — "trombocitopenia hereditaria **con plaquetas normales**" — es internamente contradictorio: sugiere un trastorno **funcional** de las plaquetas (defecto cualitativo) más que un déficit de **producción** (defecto cuantitativo). Un TPO-RA actúa aumentando la cantidad de plaquetas producidas, pero no corrige defectos estructurales o funcionales intrínsecos, por lo que su aplicabilidad terapéutica en este contexto es cuestionable.

La puntuación elevada de TxGNN probablemente refleja una agrupación semántica en el espacio de embeddings alrededor del término "thrombocytopenia", más que una correspondencia mecanística real. Esto se refuerza por el hecho de que, de las 10 indicaciones predichas en este candidato, ninguna cuenta con ensayo clínico ni publicación alguna, y varias (esclerosis lateral amiotrófica, polimicrogiria, displasia esquelética) carecen de cualquier relación biológica plausible con el eje TPO/MPL, lo que sugiere ruido del modelo antes que señal genuina.

---

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Informacion de Mercado en Espana

Lusutrombopag no está comercializado en España (0 autorizaciones registradas), por lo que no hay información de producto, forma farmacéutica ni indicación aprobada disponible en este mercado.

---

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad. (La advertencia principal del TFDA está identificada como brecha de datos bloqueante — DG001 — que impide actualmente la evaluación de seguridad inicial S1; no se dispone de contraindicaciones ni interacciones farmacológicas verificadas.)

---

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La predicción se apoya únicamente en la puntuación del modelo TxGNN (L5), sin ningún ensayo clínico, dato observacional o publicación que la respalde, y el mecanismo propuesto es mecanísticamente débil dado el carácter aparentemente funcional (no cuantitativo) del trastorno. Además, el candidato carece de datos de seguridad verificados (MOA y advertencias TFDA son brechas bloqueantes), y el fármaco no está comercializado en España.

**Para avanzar se necesita:**
- Resolver la brecha bloqueante DG001: obtener y analizar el prospecto/ficha técnica de TFDA para habilitar la evaluación de seguridad S1
- Completar los datos de mecanismo de acción (MOA) detallado (DG002)
- Clarificar la definición clínica exacta de "trombocitopenia hereditaria con plaquetas normales" para confirmar si el defecto es cuantitativo o cualitativo
- Estudios preclínicos o de caso que evalúen TPO-RA en trastornos funcionales plaquetarios antes de considerar cualquier avance
- Revisar el resto de las 9 indicaciones predichas en este candidato, dado que ninguna presenta evidencia real y varias carecen de plausibilidad biológica
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

