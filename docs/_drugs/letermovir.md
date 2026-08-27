---
layout: default
title: Letermovir
parent: 僅模型預測 (L5)
nav_order: 163
evidence_level: L5
indication_count: 1
---

# Letermovir
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

# Letermovir: De Profilaxis de Infección por CMV a Candidiasis Vulvovaginal

## Resumen en Una Frase

Letermovir es un antiviral cuya indicación conocida es la profilaxis de la infección por citomegalovirus (CMV) en receptores de trasplante (dato no incluido explícitamente en este Evidence Pack, que no registra indicaciones originales ni comercialización en España). El modelo TxGNN predice, con una puntuación muy alta (**99.88%**), que podría ser efectivo para **Candidiasis Vulvovaginal**, pero actualmente **no existe ningún ensayo clínico ni publicación** que respalde esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en el Evidence Pack (sin licencias registradas en España) |
| Nueva Indicación Predicha | Candidiasis Vulvovaginal |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por que es Razonable esta Predicción?

Actualmente no se dispone de datos estructurados del mecanismo de acción (campo `original_moa` marcado como Data Gap). Sin embargo, la propia justificación mecanística generada para esta predicción describe a letermovir como un inhibidor del complejo terminasa del citomegalovirus (CMV) (pUL51/pUL56/pUL89), un antiviral específico que bloquea el empaquetamiento del ADN viral y la maduración del virión.

Este mecanismo **no tiene ninguna relación conocida** con las vías de síntesis de la pared/membrana celular de *Candida albicans* (por ejemplo, síntesis de ergosterol o glucano sintasa), que son las dianas típicas de los antifúngicos. No existe literatura pública que respalde actividad antifúngica de letermovir.

La puntuación alta de TxGNN (99.88%) probablemente refleja asociaciones indirectas en el grafo de conocimiento (por ejemplo, poblaciones inmunosuprimidas que comparten comorbilidades o co-medicación), y no una relación farmacológica real. Por lo tanto, esta predicción debe tratarse como un **posible falso positivo** hasta que exista evidencia experimental (in vitro o preclínica) que la respalde.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún ensayo clínico ni publicación que respalde la eficacia de letermovir en candidiasis vulvovaginal, y el análisis mecanístico disponible indica una falta de plausibilidad biológica (antiviral inhibidor de terminasa vs. diana antifúngica). La puntuación alta de TxGNN, sin apoyo experimental, no es suficiente para avanzar.

**Para avanzar se necesita:**
- Estudios in vitro que evalúen actividad antifúngica directa de letermovir frente a *Candida* spp.
- Datos completos del mecanismo de acción (MOA) desde DrugBank u otra fuente primaria
- Confirmación de indicaciones originales y estado regulatorio (actualmente ausentes en el Evidence Pack)
- Datos de seguridad (advertencias, contraindicaciones, interacciones) desde el prospecto de TFDA, actualmente bloqueados (DG001)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

