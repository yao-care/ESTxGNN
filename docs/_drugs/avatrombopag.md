---
layout: default
title: Avatrombopag
parent: 僅模型預測 (L5)
nav_order: 30
evidence_level: L5
indication_count: 10
---

# Avatrombopag
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

# Avatrombopag: De Trombocitopenia Crónica a Macrotrombocitopenia con Insuficiencia de la Válvula Mitral

## Resumen en Una Frase

Avatrombopag es un agonista del receptor de trombopoyetina (TPO-RA), utilizado habitualmente en trombocitopenia asociada a hepatopatía crónica y en púrpura trombocitopénica inmune. El modelo TxGNN predice que podría ser efectivo para **macrotrombocitopenia con insuficiencia de la válvula mitral**, con una puntuación de predicción del **99.995%**, pero actualmente **no existe ningún ensayo clínico ni publicación** que respalde esta dirección — se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trombocitopenia crónica (hepatopatía crónica / PTI) — uso conocido, sin registro en España |
| Nueva Indicación Predicha | Macrotrombocitopenia con insuficiencia de la válvula mitral |
| Puntaje de Predicción TxGNN | 99.995% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción (MOA) en este informe (brecha de datos DG002, prioridad alta). Según la información pública conocida, avatrombopag es un agonista no peptídico del receptor de trombopoyetina (TPO-R), que estimula la megacariopoyesis y aumenta el recuento plaquetario; su uso establecido es en trombocitopenia asociada a hepatopatía crónica antes de procedimientos invasivos y en púrpura trombocitopénica inmune crónica refractaria.

La nueva indicación predicha es un síndrome hereditario raro que combina plaquetas gigantes disfuncionales con una valvulopatía cardíaca estructural. El propio análisis mecanístico incluido en el pack de evidencia señala que, si bien un TPO-RA como avatrombopag podría elevar el recuento plaquetario, **no corrige el defecto estructural de las plaquetas gigantes ni la insuficiencia valvular subyacente** — es decir, el fármaco actuaría, en el mejor de los casos, sobre un parámetro secundario (cantidad) sin abordar la causa (calidad/estructura) ni la comorbilidad cardíaca.

En consecuencia, aunque la puntuación de TxGNN es muy alta, la propia justificación mecanística la califica como "débil" y "sin validación clínica alguna". Esto sugiere que la predicción probablemente refleja una proximidad estructural en el grafo de conocimiento (comorbilidad general con trombocitopenia) más que una relación causal real. Cabe destacar además que el término usado en las búsquedas, *marcothrombocytopenia*, podría ser un error tipográfico de *macrothrombocytopenia*, lo que pudo haber afectado la recuperación de ensayos y literatura relacionada.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia corresponde únicamente a nivel L5 (predicción de modelo, sin ensayos clínicos ni literatura de respaldo), y el propio análisis mecanístico cuestiona la validez biológica del vínculo. Además, el fármaco no está comercializado en España y faltan datos regulatorios críticos de seguridad (brecha DG001, bloqueante).

**Para avanzar se necesita:**
- Advertencias y contraindicaciones del prospecto/TFDA (DG001, bloqueante)
- Datos completos del mecanismo de acción desde DrugBank (DG002)
- Verificar si "marcothrombocytopenia" es un error tipográfico de "macrothrombocytopenia" y repetir la búsqueda de ensayos y literatura con el término corregido
- Estudios de caso o series que evalúen TPO-RA en síndromes de macrotrombocitopenia hereditaria con comorbilidad valvular
- Revisión de calidad de esta ejecución del modelo: los otros 9 candidatos (rangos 2-10) incluyen enfermedades sin relación mecanística plausible con la vía de TPO (ELA, síndromes de neurona motora, malformación cortical congénita), lo que sugiere ruido en las predicciones de este lote antes de priorizar nuevas indicaciones para este fármaco
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

