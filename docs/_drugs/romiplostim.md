---
layout: default
title: Romiplostim
parent: 僅模型預測 (L5)
nav_order: 248
evidence_level: L5
indication_count: 10
---

# Romiplostim
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

# Romiplostim: De Trombocitopenia Inmune (ITP) a Trastorno Primario de Liberación de Plaquetas

## Resumen en Una Frase

Romiplostim es un agonista del receptor de trombopoyetina (TPO-RA) utilizado originalmente para estimular la producción de plaquetas en la trombocitopenia inmune (ITP), la trombocitopenia inducida por quimioterapia y la trombocitopenia post-trasplante. El modelo TxGNN predice que podría ser efectivo para el **Trastorno Primario de Liberación de Plaquetas**, pero actualmente esta indicación concreta cuenta solo con **1 ensayo clínico indirecto** y **2 publicaciones**, ninguno diseñado para probar eficacia en esta enfermedad específica.

> **Nota:** Este Evidence Pack evalúa 10 indicaciones candidatas para romiplostim. Una de ellas — "platelet-type bleeding disorder" (rango 8, no es el objeto de este informe) — presenta evidencia sustancialmente más fuerte (Nivel L1, 8 ensayos clínicos incluyendo un Fase 3 aleatorizado doble-ciego completado, NCT03362177/RECITE). Se recomienda revisar esa candidata por separado, ya que corresponde en gran medida al espacio de uso ya establecido del fármaco.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trombocitopenia inmune (ITP), trombocitopenia inducida por quimioterapia, trombocitopenia post-trasplante (según contexto mecanístico del Evidence Pack; sin ficha técnica oficial disponible) |
| Nueva Indicación Predicha | Trastorno Primario de Liberación de Plaquetas |
| Puntaje de Predicción TxGNN | 99.9998% (rango interno del modelo: 23) |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de una ficha técnica ni de datos estructurados de mecanismo de acción (MOA) en este Evidence Pack. Según la información contextual disponible, romiplostim es un agonista del receptor de trombopoyetina (TPO-RA) que estimula directamente la megacariocitopoyesis y la liberación de plaquetas, mecanismo ya validado en su uso establecido para ITP, trombocitopenia inducida por quimioterapia y trombocitopenia tras trasplante.

El "Trastorno Primario de Liberación de Plaquetas" describe una alteración en la producción o liberación de plaquetas por el megacariocito, lo cual es direccionalmente compatible con el mecanismo estimulador de romiplostim. Sin embargo, la evidencia disponible (1 ensayo observacional sobre factores de riesgo de trombosis en ITP, y 2 publicaciones sobre biología de la megacariocitopoyesis y autoanticuerpos antiplaquetarios) se centra en el mecanismo de destrucción inmune de la ITP, no en un defecto primario de liberación plaquetaria como entidad propia. Por tanto, el vínculo mecanístico es plausible pero indirecto, y no existe hasta la fecha un ensayo diseñado específicamente para esta indicación.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03820960](https://clinicaltrials.gov/study/NCT03820960) | N/A | Completado | 10039 | Estudio observacional de factores de riesgo de trombosis en pacientes con trombocitopenia inmune (ITP); no evalúa eficacia de romiplostim directamente, solo caracteriza la población relacionada (grado de relevancia C). |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [23594368](https://pubmed.ncbi.nlm.nih.gov/23594368/) | 2013 | Revisión | British Journal of Haematology | Revisión de los avances en megacariocitopoyesis y trombopoyesis, describiendo a la trombopoyetina (TPO) como el principal factor de crecimiento del linaje megacariocítico. |
| [25682608](https://pubmed.ncbi.nlm.nih.gov/25682608/) | 2015 | Cohorte/Mecanístico | Haematologica | Los autoanticuerpos antiplaquetarios en ITP inhiben la formación de proplaquetas por los megacariocitos, alterando la producción de plaquetas in vitro. |

---

## Información de Mercado en España

Actualmente no hay autorizaciones registradas en España (medicamento no comercializado según este Evidence Pack).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

*(Nota interna: la ficha técnica/prospecto de la agencia reguladora aún no ha sido obtenida — ver "Para avanzar se necesita" abajo).*

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia disponible para "Trastorno Primario de Liberación de Plaquetas" corresponde a Nivel L4 (estudios mecanísticos/preclínicos indirectos), sin ningún ensayo clínico diseñado para probar eficacia de romiplostim en esta indicación concreta. El vínculo mecanístico es razonable pero insuficiente para avanzar a evaluación de seguridad o diseño de estudio en esta etapa.

**Para avanzar se necesita:**
- Obtener la ficha técnica/prospecto oficial (actualmente bloqueante para la evaluación de seguridad S1 — gap crítico DG001)
- Confirmar el mecanismo de acción detallado desde DrugBank u otra fuente estructurada (gap DG002)
- Un estudio mecanístico o serie de casos que caracterice específicamente el "defecto primario de liberación plaquetaria" como entidad distinta de la ITP, y su respuesta a agonistas TPO-RA
- Evaluar en paralelo la candidata "platelet-type bleeding disorder" (Nivel L1, Proceed with Guardrails), que presenta evidencia clínica sustancialmente más madura y podría representar una vía de avance más inmediata
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

