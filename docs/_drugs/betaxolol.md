---
layout: default
title: Betaxolol
parent: 僅模型預測 (L5)
nav_order: 39
evidence_level: L5
indication_count: 1
---

# Betaxolol
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

# Betaxolol: De Indicación Original No Documentada a Glaucoma Hereditario Primario

## Resumen en Una Frase

Betaxolol es un antagonista selectivo de los receptores adrenérgicos β1; en este informe no se dispone de datos sobre su(s) indicación(es) original(es) aprobada(s), ya que el fármaco actualmente **no está comercializado en Taiwán**. El modelo TxGNN predice que podría ser efectivo para **Glaucoma Hereditario Primario**, pero esta dirección **no cuenta con ningún ensayo clínico ni publicación de respaldo** — se trata únicamente de una puntuación de inferencia del grafo de conocimiento.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No documentada en este conjunto de datos |
| Nueva Indicación Predicha | Glaucoma Hereditario Primario |
| Puntaje de Predicción TxGNN | 99.74% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Taiwán | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone del mecanismo de acción (MOA) formal de Betaxolol en este conjunto de datos (brecha de datos DG002). Sin embargo, la propia justificación de reposicionamiento generada aporta contexto mecanístico parcial: Betaxolol es un antagonista selectivo de los receptores adrenérgicos β1. El bloqueo beta-adrenérgico reduce la producción de humor acuoso por el epitelio ciliar, disminuyendo la presión intraocular (PIO) — uno de los mecanismos centrales en el tratamiento del glaucoma. Fármacos de la misma clase farmacológica, como timolol y levobunolol, ya se utilizan en oftalmología precisamente para reducir la PIO.

La puntuación alta de TxGNN (99.74%) es consistente con esta dirección mecanística. No obstante, es importante subrayar que esta predicción **no está respaldada por ningún ensayo clínico ni literatura científica** en este registro; es exclusivamente una puntuación de inferencia del grafo de conocimiento y no debe interpretarse como evidencia clínica.

Adicionalmente, este conjunto de datos indica que el fármaco no está comercializado en Taiwán y carece de información sobre sus indicaciones aprobadas originales, lo que aumenta la incertidumbre general sobre la comparabilidad entre la indicación original y la nueva indicación predicha.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Taiwán

Betaxolol no está actualmente comercializado en Taiwán (0 autorizaciones registradas ante TFDA).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. (No se identificaron advertencias, contraindicaciones ni interacciones farmacológicas en las fuentes consultadas hasta la fecha; la ficha técnica de TFDA está marcada como brecha de datos bloqueante — DG001.)

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se sustenta únicamente en la puntuación del modelo TxGNN (nivel de evidencia L5), sin ningún ensayo clínico ni publicación que la respalde. Además, existe una brecha de datos bloqueante sobre advertencias/contraindicaciones (DG001), lo que impide iniciar siquiera la evaluación de seguridad S1.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha técnica de TFDA con advertencias y contraindicaciones (DG001, bloqueante)
- Confirmar el mecanismo de acción formal vía DrugBank (DG002)
- Documentar la(s) indicación(es) original(es) aprobada(s) de Betaxolol (actualmente ausente en el conjunto de datos)
- Búsqueda de evidencia clínica real (ensayos y literatura) específicamente para "glaucoma hereditario primario"
- Evaluar la vía regulatoria para comercialización en Taiwán, dado el estado actual "no comercializado"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

