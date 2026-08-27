---
layout: default
title: Crizotinib
parent: 僅模型預測 (L5)
nav_order: 80
evidence_level: L5
indication_count: 10
---

# Crizotinib
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

# Crizotinib: De Cáncer de Pulmón No Microcítico ALK+/ROS1+ a Fibromatosis Gingival

## Resumen en Una Frase

Crizotinib es un inhibidor de tirosina quinasa (ALK/ROS1/MET) utilizado originalmente para el cáncer de pulmón no microcítico (NSCLC) con reordenamiento de ALK o ROS1.
El modelo TxGNN predice que podría ser efectivo para **Fibromatosis Gingival**,
con una puntuación de predicción de **99.81%**, pero actualmente **no existe ningún ensayo clínico ni publicación** que respalde esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de pulmón no microcítico (NSCLC) con reordenamiento ALK/ROS1 (según literatura incluida en este paquete; el campo estructurado `original_indications` está vacío) |
| Nueva Indicación Predicha | Fibromatosis Gingival |
| Puntaje de Predicción TxGNN | 99.81% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos estructurados sobre el mecanismo de acción en este Evidence Pack (brecha de datos DG002, severidad Alta). Sin embargo, según la literatura incluida en este mismo paquete (p. ej. PMID 24756793, 30069759), crizotinib es un inhibidor de molécula pequeña competitivo por ATP de las tirosina quinasas receptoras ALK, ROS1 y c-MET, aprobado para NSCLC con reordenamiento EML4-ALK o ROS1, representando entre el 3-5% de todos los casos de NSCLC.

La fibromatosis gingival es una condición de crecimiento excesivo benigno del tejido gingival, de etiología generalmente fibrótica/hereditaria o inducida por fármacos (p. ej. fenitoína, ciclosporina, bloqueadores de canales de calcio), sin relación fisiopatológica conocida con las vías ALK, ROS1 o MET.

De hecho, el propio paquete de evidencia señala explícitamente que **no existe ningún ensayo clínico, publicación ni vínculo mecanístico conocido** entre crizotinib y la fibromatosis gingival: la predicción se basa únicamente en la puntuación del modelo TxGNN (rank 3879 de la lista, nivel L5), sin respaldo biológico o clínico identificado. Por lo tanto, esta predicción debe interpretarse como una hipótesis exploratoria de muy baja confianza, no como una señal de reposicionamiento clínicamente accionable en su estado actual.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Crizotinib no está comercializado en España (0 autorizaciones registradas en este Evidence Pack).

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa ALK/ROS1/MET) |
| Riesgo de Mielosupresión | Bajo — la literatura incluida en este paquete no describe mielosupresión relevante; los riesgos predominantes documentados son hepatotoxicidad, cardiotoxicidad (bradicardia, prolongación de QT) y neumonitis/enfermedad pulmonar intersticial (PMID 41617059, 26898609, 29717400) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto (sin datos en este Evidence Pack) |
| Items de Monitoreo | Función hepática (transaminasas, bilirrubina), ECG/intervalo QT, función pulmonar y síntomas respiratorios (riesgo de neumonitis) |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto (sin datos en este Evidence Pack) |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación predicha de mayor rango (fibromatosis gingival) carece por completo de ensayos clínicos, literatura y vínculo mecanístico conocido; la evidencia se limita a la puntuación del modelo (nivel L5), lo que es insuficiente para avanzar a evaluación clínica.

**Para avanzar se necesita:**
- Warnings/contraindicaciones del prospecto TFDA (DG001, severidad Blocking) — actualmente bloquea la evaluación de seguridad S1
- Datos de mecanismo de acción (MOA) desde DrugBank (DG002)
- Evidencia mecanística o preclínica que vincule específicamente la fibromatosis gingival con las vías ALK/ROS1/MET
- Revisión del pipeline de mapeo de ontología: varias otras indicaciones predichas en este mismo paquete (p. ej. "lung benign neoplasm", "inclusion body myopathy with early-onset Paget disease...") muestran literatura adjunta que no corresponde al nombre de la enfermedad, sugiriendo posible desajuste de entidades que debería corregirse antes de repetir este análisis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

