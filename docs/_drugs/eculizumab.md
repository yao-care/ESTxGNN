---
layout: default
title: Eculizumab
parent: 僅模型預測 (L5)
nav_order: 99
evidence_level: L5
indication_count: 10
---

# Eculizumab
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

# Eculizumab: De Síndrome Hemolítico Urémico Atípico a Hematopoyesis Cíclica

## Resumen en Una Frase

Eculizumab es un inhibidor del complemento C5, con uso establecido en enfermedades mediadas por el complemento como el síndrome hemolítico urémico atípico (SHUa) y la hemoglobinuria paroxística nocturna (HPN), según se documenta en la literatura incluida en este Evidence Pack. El modelo TxGNN predice que podría ser efectivo para **hematopoyesis cíclica**, pero actualmente **no existe ningún ensayo clínico ni publicación** que respalde específicamente esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en el registro regulatorio de España (fármaco no comercializado); documentada en la literatura del pack como inhibidor del complemento C5 aprobado para SHUa y HPN |
| Nueva Indicación Predicha | Hematopoyesis cíclica (cyclic hematopoiesis) |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos estructurados sobre el mecanismo de acción original de eculizumab (dato marcado como pendiente en el pack). Sin embargo, según la literatura citada en este mismo Evidence Pack, eculizumab se describe como un **inhibidor del complemento C5** que bloquea la vía terminal del complemento y la formación del complejo de ataque de membrana (MAC), mecanismo que respalda su uso en enfermedades mediadas por el complemento como el SHUa (PMID 39543505) y la HPN (PMID 25237200).

La hematopoyesis cíclica, en cambio, está causada principalmente por mutaciones en el gen **ELANE**, que provocan una desregulación periódica de la elastasa de neutrófilos — un trastorno de la diferenciación mieloide en la médula ósea, sin relación estructural ni funcional conocida con la vía terminal del complemento.

El propio análisis mecanístico incluido en el pack concluye explícitamente que **no existe intersección conocida** entre ambos mecanismos y que la predicción **carece de razonabilidad mecanística**. Por tanto, pese al alto puntaje del modelo TxGNN (99.97%), la plausibilidad biológica de esta predicción específica es baja y no está respaldada por evidencia clínica ni preclínica dirigida a esta indicación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje TxGNN es alto, pero no existe ningún ensayo clínico ni publicación específica para hematopoyesis cíclica, y el propio análisis mecanístico del pack descarta una relación biológica plausible entre la inhibición de C5 y la fisiopatología asociada a ELANE. La evidencia no supera el nivel L5 (predicción de modelo sin respaldo real).

**Para avanzar se necesita:**
- Ficha técnica/prospecto de eculizumab en la UE/España (actualmente bloqueante — DG001) para poder iniciar la evaluación de seguridad S1
- Datos de mecanismo de acción vía API de DrugBank (actualmente pendiente — DG002)
- Búsqueda dirigida de estudios preclínicos que exploren una posible relación indirecta entre inhibición del complemento e inflamación neutrofílica en hematopoyesis cíclica, dado que hoy no existe evidencia real alguna
- Revisar si alguna de las otras indicaciones predichas por TxGNN para este fármaco cuenta con mejor respaldo mecanístico o documental antes de priorizar recursos de evaluación
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

