---
layout: default
title: Fosaprepitant
parent: 僅模型預測 (L5)
nav_order: 124
evidence_level: L5
indication_count: 10
---

# Fosaprepitant
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

# Fosaprepitant: De Náuseas y Vómitos Inducidos por Quimioterapia a Síndrome Nefrogénico de Antidiuresis Inapropiada

## Resumen en Una Frase

Fosaprepitant es un antagonista del receptor NK1 (Substance P), profármaco de aprepitant, utilizado originalmente para la prevención de náuseas y vómitos inducidos por quimioterapia (CINV). El modelo TxGNN predice que podría ser efectivo para el **Síndrome Nefrogénico de Antidiuresis Inapropiada (NSIAD)**, con una puntuación de predicción del 99,92%, pero **sin ningún ensayo clínico ni publicación** que respalde actualmente esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Prevención de náuseas y vómitos inducidos por quimioterapia (CINV) — no consta autorización en España |
| Nueva Indicación Predicha | Síndrome Nefrogénico de Antidiuresis Inapropiada (NSIAD) |
| Puntaje de Predicción TxGNN | 99,92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

El mecanismo de acción detallado de fosaprepitant es oficialmente un dato pendiente (data gap) en esta ficha, pero la evidencia recogida en este mismo paquete lo identifica como **antagonista del receptor NK1/Substance P** (ver evidencia de literatura del candidato "retinitis", PMID 32058829). Su indicación original, la prevención de CINV, se basa precisamente en el bloqueo de la vía Substance P/NK1 a nivel central, que media el reflejo emético.

El NSIAD, en cambio, es un trastorno causado por **mutaciones de ganancia de función en el gen AVPR2** (receptor de vasopresina V2), una vía completamente distinta de la señalización NK1/Substance P. La propia justificación mecanística generada para esta predicción es explícita al respecto: *"NSIAD 为 AVPR2 基因功能获得性突变所致，与 NK1/Substance P 讯号无已知交集，无临床或机转证据支持"* — es decir, no existe solapamiento mecanístico conocido ni evidencia clínica que respalde esta dirección.

En conjunto, esta predicción parece ser una asociación generada puramente por el modelo (score alto en el grafo de conocimiento), sin respaldo biológico ni clínico identificable hasta la fecha.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
A pesar de la alta puntuación de TxGNN, no existe ningún ensayo clínico ni publicación que respalde la asociación entre fosaprepitant y NSIAD, y el propio análisis mecanístico indica que ambas entidades no comparten vía biológica conocida (NK1/Substance P vs. AVPR2). Además, el fármaco no está comercializado en España y faltan datos de seguridad de TFDA necesarios incluso para una evaluación preliminar (S1).

**Para avanzar se necesita:**
- Ficha técnica/prospecto de TFDA con advertencias y contraindicaciones — actualmente bloqueante (DG001)
- Confirmación del mecanismo de acción vía DrugBank (DG002)
- Evidencia mecanística o clínica específica que conecte la vía NK1/Substance P con la fisiopatología del NSIAD
- Nota: dentro de este mismo paquete de evidencia, el candidato "retinitis" (rank 7) cuenta con un estudio preclínico que sí vincula fosaprepitant con la vía NK1 en tejido ocular, y está clasificado como "Research Question" — podría ser una dirección de mayor interés que NSIAD para investigación adicional.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

