---
layout: default
title: Fostamatinib
parent: 僅模型預測 (L5)
nav_order: 127
evidence_level: L5
indication_count: 2
---

# Fostamatinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Fostamatinib: De Trombocitopenia Inmune (PTI) a Trombocitopenia Autosómica con Plaquetas Normales

## Resumen en Una Frase

Fostamatinib es un inhibidor de Syk (tirosina quinasa esplénica) cuyo único uso conocido, según la información recogida en este Evidence Pack, es la trombocitopenia inmune (PTI), donde actúa bloqueando la señalización de FcγR para reducir la destrucción inmunomediada de plaquetas. El modelo TxGNN predice que podría ser efectivo para **Trombocitopenia Autosómica con Plaquetas Normales**, con una puntuación de **99.45%**, pero actualmente **no existe ningún ensayo clínico ni publicación** que respalde esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trombocitopenia inmune (PTI) — dato tomado del razonamiento mecanístico del pack, no de ficha técnica verificada (fármaco no comercializado en España) |
| Nueva Indicación Predicha | Trombocitopenia Autosómica con Plaquetas Normales |
| Puntaje de Predicción TxGNN | 99.45% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos consultada (DrugBank: [Data Gap]). Según la información incluida en el razonamiento del pack, fostamatinib es un inhibidor de Syk cuyo uso establecido es la PTI, donde reduce la fagocitosis de plaquetas mediada por macrófagos.

La trombocitopenia autosómica con plaquetas normales es una entidad genética distinta: se debe a defectos hereditarios en la producción o estructura de las plaquetas, no a su destrucción inmunomediada. El propio análisis mecanístico del pack advierte que la puntuación TxGNN tan alta (99.45%) podría reflejar simplemente la proximidad semántica de los nodos "trombocitopenia" dentro del grafo de conocimiento, y no una correspondencia farmacológica real — una advertencia que se refuerza por la ausencia total de datos de MOA verificados con los que contrastar la hipótesis.

Como referencia de contraste, el pack también evaluó un segundo candidato (malformación esofágica no sindrómica, puntuación 99.05%) para el que no se identificó ningún vínculo mecanístico reconocible, y que fue directamente clasificado como Hold — lo que respalda la lectura de que puntuaciones TxGNN muy altas no equivalen por sí solas a plausibilidad biológica en este fármaco.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Consideraciones de Seguridad

No se dispone de datos de seguridad verificados en este Evidence Pack: las advertencias, contraindicaciones y la ficha técnica TFDA no han sido obtenidas, y este vacío está clasificado como **bloqueante** para la evaluación de seguridad inicial (S1). Tampoco se identificaron interacciones farmacológicas (DDI) en la búsqueda realizada (0 resultados).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo TxGNN (nivel L5), sin ningún ensayo clínico ni publicación que la respalde, y el propio razonamiento mecanístico advierte que podría tratarse de un artefacto del grafo de conocimiento más que de un mecanismo farmacológico real. Además, la falta de ficha técnica TFDA está clasificada como una brecha bloqueante que impide avanzar siquiera a la evaluación de seguridad preliminar.

**Para avanzar se necesita:**
- Obtener la ficha técnica/prospecto TFDA con advertencias y contraindicaciones (brecha bloqueante DG001)
- Confirmar el mecanismo de acción detallado vía DrugBank u otra fuente primaria (DG002)
- Estudios preclínicos o casos clínicos que evalúen la inhibición de Syk específicamente en trombocitopenias hereditarias
- Revisión por un experto en hematología genética sobre la plausibilidad mecanística real de este vínculo
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

