---
layout: default
title: Cilazapril
parent: 僅模型預測 (L5)
nav_order: 71
evidence_level: L5
indication_count: 4
---

# Cilazapril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Cilazapril: De IECA sin Comercializar en España a Hipertensión Pulmonar de Mecanismo Multifactorial no Claro

## Resumen en Una Frase

Cilazapril es un profármaco IECA (inhibidor de la enzima convertidora de angiotensina) que, según este dossier, no cuenta con licencias de comercialización registradas en España, por lo que no existe una indicación original documentada aquí. El modelo TxGNN predice que podría ser efectivo para **Hipertensión Pulmonar de Mecanismo Multifactorial No Claro**, pero actualmente **no hay ningún ensayo clínico ni publicación** que respalde esta dirección específica: se trata únicamente de una puntuación algorítmica sin verificación clínica.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (sin licencias registradas en España) |
| Nueva Indicación Predicha | Hipertensión pulmonar de mecanismo multifactorial no claro |
| Puntaje de Predicción TxGNN | 99.20% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de cilazapril en este dossier. Según la información recogida en el análisis de otras indicaciones relacionadas dentro del mismo candidato, cilazapril es un profármaco IECA que inhibe la conversión de angiotensina I a angiotensina II, reduciendo la resistencia vascular sistémica. Sin embargo, esta caracterización proviene de una inferencia a nivel de clase farmacológica, no de un campo de MOA documentado específicamente para este fármaco.

No existe una indicación original registrada en España (el fármaco no consta como comercializado ni posee licencias vigentes), por lo que no es posible establecer una comparación directa entre una indicación previa y la nueva indicación predicha. La propia justificación mecanicista adjunta a esta predicción señala explícitamente que no hay ensayo clínico, literatura, ni indicación original o MOA específicos que la respalden, y que el nombre de la enfermedad en sí está etiquetado como "de mecanismo no claro" — lo que representa la fuerza de evidencia más baja posible.

Adicionalmente, la literatura recuperada para la indicación de puntaje equivalente (hipertensión pulmonar por enfermedad pulmonar y/o hipoxia) fue revisada y corresponde a artículos generales sobre fisiología de la hipoxia, neurodegeneración y metabolismo tumoral, sin ninguna mención a cilazapril ni a IECA en el contexto de hipertensión pulmonar. Esto se interpreta como coincidencia de palabras clave más que como una relación mecanística real, y los IECA no forman parte de las guías actuales de tratamiento de hipertensión pulmonar.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación con mayor puntaje TxGNN para este candidato (hipertensión pulmonar de mecanismo multifactorial no claro) carece por completo de ensayos clínicos y literatura de respaldo, y está clasificada como L5 — solo predicción de modelo. A esto se suma la ausencia de datos regulatorios (fármaco no comercializado en España, 0 licencias), de MOA documentado y de información de seguridad (advertencias, contraindicaciones e interacciones sin datos), lo que impide avanzar a evaluación de seguridad (S1).

**Para avanzar se necesita:**
- Datos de ficha técnica/prospecto de AEMPS (advertencias y contraindicaciones) — actualmente brecha bloqueante (DG001)
- Confirmación del mecanismo de acción específico del fármaco vía DrugBank u otra fuente primaria (DG002)
- Búsqueda dirigida de literatura y ensayos clínicos que combinen cilazapril con hipertensión pulmonar (las búsquedas actuales devolvieron 0 resultados)
- Si se desea continuar la investigación dentro de este mismo candidato, valorar en su lugar las indicaciones de rango 3 y 4 ("malignant hypertensive renal disease" y "malignant renovascular hypertension"), clasificadas como L4/Research Question, con plausibilidad mecanística de clase IECA algo más sólida — aunque también sin evidencia clínica directa y con riesgo conocido de insuficiencia renal aguda en estenosis renovascular bilateral
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

