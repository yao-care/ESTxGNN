---
layout: default
title: Tapentadol
parent: 僅模型預測 (L5)
nav_order: 269
evidence_level: L5
indication_count: 3
---

# Tapentadol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# TAPENTADOL: De Analgesia (Dolor) a Migraña

## Resumen en Una Frase

TAPENTADOL es un analgésico con mecanismo dual —agonista μ-opioide e inhibidor de la recaptación de noradrenalina (NRI)— utilizado en el manejo del dolor. El modelo TxGNN predice que podría ser efectivo para **Migraña (migraine disorder)**, con un puntaje de predicción del **99.67%**, pero actualmente **no existen ensayos clínicos** que estudien directamente esta combinación y solo **2 publicaciones** indirectamente relacionadas la respaldan.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No confirmada en fuente oficial (dato regulatorio ausente); mecanismo descrito sugiere uso analgésico |
| Nueva Indicación Predicha | Migraña (migraine disorder) |
| Puntaje de Predicción TxGNN | 99.67% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos oficiales confirmados sobre el mecanismo de acción (MOA) de TAPENTADOL en este Evidence Pack. Según la información contenida en el análisis de racionalidad del modelo, TAPENTADOL combina un componente **agonista μ-opioide** con **inhibición de la recaptación de noradrenalina (NRI)**, mecanismo compartido en parte con algunos fármacos preventivos de migraña (p. ej., venlafaxina, que actúa también vía NRI).

Sin embargo, esta similitud mecanística es solo parcial y presenta una señal negativa relevante: múltiples guías clínicas de cefalea —la guía EAN MOH 2020 y la revisión de evidencia AHRQ sobre migraña aguda— desaconsejan explícitamente el uso de opioides en el tratamiento de la migraña, debido a su falta de especificidad analgésica, el riesgo de cefalea por uso excesivo de medicación (medication overuse headache), la cronificación de la migraña y el riesgo de abuso/dependencia. Por tanto, la predicción del componente NRI es mecánicamente plausible, pero el componente opioide constituye una contraindicación relativa de clase, no solo un vacío de evidencia.

El modelo TxGNN también predijo dos subtipos adicionales relacionados con migraña: "migraine with brainstem aura" (sin ningún respaldo de literatura o ensayos, con riesgo teórico añadido de depresión respiratoria/alteración de consciencia en un subtipo con síntomas de origen troncoencefálico) y "migraine with or without aura, susceptibility to" (una clasificación de susceptibilidad genética, no una indicación tratable; su literatura asociada —20 publicaciones— trata sobre genética de comorbilidad epilepsia-migraña, sin relación con la farmacología de TAPENTADOL). Ambos fueron evaluados y también reciben recomendación Hold.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27096578](https://pubmed.ncbi.nlm.nih.gov/27096578/) | 2016 | Revisión (Cochrane) | Cochrane Database of Systematic Reviews | Revisión sobre dipirona (metamizol) para dolor postoperatorio agudo; menciona su uso en migraña en algunos países, pero **no estudia TAPENTADOL** |
| [27096438](https://pubmed.ncbi.nlm.nih.gov/27096438/) | 2016 | Revisión (Cochrane) | Cochrane Database of Systematic Reviews | Revisión sobre sumatriptán + naproxeno para crisis agudas de migraña; describe tratamientos abortivos estándar (triptanes, AINE), **no estudia TAPENTADOL** |

**Nota:** Ninguna de las dos publicaciones estudia directamente TAPENTADOL en migraña; ambas fueron recuperadas por asociación temática con "migraña" y "analgesia", no por evidencia farmacológica específica del fármaco.

---

## Información de Mercado en España

No se han identificado autorizaciones de comercialización en España (total de autorizaciones: 0).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. (No se dispone de advertencias, contraindicaciones ni datos de interacciones farmacológicas en las fuentes consultadas; la obtención del prospecto de la agencia reguladora está pendiente y ha sido marcada como bloqueante para la evaluación de seguridad.)

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Las tres indicaciones predichas relacionadas con migraña se encuentran en nivel de evidencia L5 (solo predicción del modelo, sin estudios reales que estudien TAPENTADOL en estas indicaciones). Además, el componente opioide del fármaco representa una señal mecanística desfavorable según las guías clínicas vigentes de tratamiento de migraña, y persiste un vacío de seguridad bloqueante (ausencia del prospecto/advertencias de la agencia reguladora).

**Para avanzar se necesita:**
- Obtener el prospecto oficial (advertencias, contraindicaciones) desde la agencia reguladora correspondiente — actualmente bloqueante
- Confirmar la indicación original y el mecanismo de acción (MOA) mediante DrugBank u otra fuente primaria
- Evaluación mecanística especializada que sopese el componente NRI (potencialmente favorable) frente al componente opioide (desfavorable según guías de migraña)
- Monitoreo de nuevos ensayos clínicos o literatura que estudien específicamente TAPENTADOL en migraña
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

