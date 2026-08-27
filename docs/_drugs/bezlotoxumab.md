---
layout: default
title: Bezlotoxumab
parent: 僅模型預測 (L5)
nav_order: 41
evidence_level: L5
indication_count: 10
---

# Bezlotoxumab
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

# Bezlotoxumab: De Infección por *Clostridioides difficile* a Peritonitis Pélvica Aguda Femenina

## Resumen en Una Frase

Bezlotoxumab es un anticuerpo monoclonal dirigido contra la toxina B de *Clostridioides difficile*, empleado en el contexto de la infección por este patógeno (no hay ficha de indicación original formalmente registrada en este Evidence Pack). El modelo TxGNN señala como principal candidato la **Peritonitis Pélvica Aguda Femenina**, con una puntuación del **99.89%**, pero esta predicción no cuenta actualmente con **ningún ensayo clínico ni publicación** que la respalde, y el propio análisis mecanístico incluido en el pack la identifica como un probable falso positivo del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en ficha formal (mecanismo descrito en el pack: anticuerpo anti-toxina B de *C. difficile*) |
| Nueva Indicación Predicha | Peritonitis Pélvica Aguda Femenina |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L5 (sin ensayos clínicos ni literatura) |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción a nivel de ficha del fármaco (marcado como carencia de datos de alta prioridad, DG002). Según la información mecanística incluida en el propio análisis de cada candidato, Bezlotoxumab neutraliza específicamente la toxina B de *Clostridioides difficile*, sin actividad antiinflamatoria sistémica ni actividad antimicrobiana de amplio espectro.

La Peritonitis Pélvica Aguda Femenina es, en la mayoría de los casos, una infección ascendente causada por gonococos, clamidia u organismos anaerobios — patógenos sin relación conocida con la toxina B de *C. difficile*. No existe, por tanto, un vínculo fisiopatológico plausible entre el mecanismo de acción del fármaco y esta nueva indicación.

De hecho, el propio *repurposing rationale* del Evidence Pack concluye explícitamente que, al no existir ensayos clínicos ni literatura de respaldo, esta pareja fármaco-enfermedad debe interpretarse como **ruido de similitud por embeddings del grafo de conocimiento (falso positivo)** más que como una hipótesis biológicamente fundamentada. Este mismo patrón se repite en las 10 indicaciones mejor puntuadas para este fármaco (todas L5, todas con recomendación Hold), lo que refuerza que el conjunto de predicciones actual no ofrece candidatos viables.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Bezlotoxumab no cuenta actualmente con ninguna autorización de comercialización registrada en España (0 autorizaciones, estado de mercado: no comercializado).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de mayor puntuación (Peritonitis Pélvica Aguda Femenina, 99.89%) carece por completo de respaldo clínico o bibliográfico, y el propio análisis mecanístico del pack la señala como probable falso positivo por similitud de grafo. Las 10 indicaciones mejor puntuadas para este fármaco comparten el mismo patrón (nivel de evidencia L5, sin ensayos ni literatura, sin plausibilidad mecanística), por lo que no se identifica ningún candidato viable para avanzar en este momento.

**Para avanzar se necesita:**
- Resolver la carencia bloqueante de advertencias/contraindicaciones de ficha técnica (DG001), indispensable para cualquier evaluación de seguridad inicial (S1)
- Obtener datos verificados del mecanismo de acción (DG002) para poder evaluar correctamente la plausibilidad biológica de futuras predicciones
- Ampliar la búsqueda de literatura y ensayos clínicos a un conjunto más amplio de indicaciones candidatas, dado que ninguna de las 10 principales predicciones actuales presenta evidencia real de respaldo
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

