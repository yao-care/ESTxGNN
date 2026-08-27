---
layout: default
title: Ceritinib
parent: 僅模型預測 (L5)
nav_order: 66
evidence_level: L5
indication_count: 10
---

# Ceritinib
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

# Ceritinib: De Cáncer de Pulmón No Microcítico ALK-positivo a Fibromatosis Gingival

## Resumen en Una Frase

Ceritinib es un inhibidor de tirosina quinasa de segunda generación (ALK/ROS1/IGF-1R), utilizado originalmente para el tratamiento del cáncer de pulmón no microcítico (NSCLC) con reordenamiento del gen ALK. El modelo TxGNN predice, con la puntuación más alta de todo el panel de candidatos evaluados (**99.86%**), que podría ser efectivo para **Fibromatosis Gingival**, pero actualmente **no existe ningún ensayo clínico ni publicación** que respalde esta dirección específica.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de pulmón no microcítico (NSCLC) ALK-positivo *(no consta en `taiwan_regulatory.licenses`, que está vacío; inferido de la literatura incluida en el propio Evidence Pack, p. ej. ensayo ASCEND-4, PMID 28126333)* |
| Nueva Indicación Predicha | Fibromatosis Gingival |
| Puntaje de Predicción TxGNN | 99.86% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en este Evidence Pack (dato marcado como brecha de alta severidad, DG002). Según la información conocida por la literatura incluida en el propio pack, ceritinib es un inhibidor de ALK/ROS1/IGF-1R de segunda generación, cuya eficacia en el NSCLC con reordenamiento de ALK ha sido comprobada en múltiples ensayos de Fase 3 (p. ej. ASCEND-4).

Sin embargo, para esta indicación concreta —fibromatosis gingival, una hiperplasia fibrosa benigna de la encía— **no existe ningún vínculo mecanístico conocido con la vía de señalización ALK**. El propio análisis de racionalidad de reposicionamiento incluido en el Evidence Pack lo señala explícitamente: la fibromatosis gingival no presenta alteraciones conocidas de la vía ALK, y esta predicción carece de cualquier hipótesis mecanística de respaldo, tratándose únicamente de una puntuación alta generada por el modelo.

Es relevante notar que, de los 10 candidatos evaluados en este pack, solo uno (*lung benign neoplasm*, rango 5) alcanzó nivel de evidencia L4 con literatura asociada — aunque incluso en ese caso, el análisis de racionalidad sugiere que se trata probablemente de un error de mapeo de ontología de enfermedades (la literatura recuperada corresponde a NSCLC maligno ALK-positivo, no a neoplasias pulmonares benignas). Ningún candidato del panel alcanzó nivel L1-L3.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Citotoxicidad

*(Sección aplicable: ceritinib es un antineoplásico dirigido, con indicación original oncológica en NSCLC ALK-positivo.)*

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa ALK/ROS1/IGF-1R) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto (sin datos de toxicidad hematológica en este pack) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Ítems de Monitoreo | Función hepática (transaminasas), glucemia, lipasa/amilasa (riesgo de pancreatitis), intervalo QTc, síntomas respiratorios (riesgo de neumonitis/enfermedad pulmonar intersticial) — toxicidades de clase documentadas en la literatura del propio pack (p. ej. PMID 29413968 sobre prolongación de QT, PMID 31280988 sobre neumopatía intersticial e hipersensibilidad) |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos/antineoplásicos orales |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. *(El Evidence Pack marca esta brecha como bloqueante — DG001 — pendiente de obtener el prospecto oficial y su análisis de advertencias, contraindicaciones e interacciones.)*

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
A pesar de tener la puntuación TxGNN más alta del panel (99.86%), la predicción para fibromatosis gingival carece por completo de respaldo clínico o bibliográfico, y el propio análisis mecanístico del pack confirma que no existe relación biológica plausible conocida entre la inhibición de ALK y esta patología. Es una predicción puramente computacional sin validación alguna.

**Para avanzar se necesita:**
- Validación de una hipótesis mecanística real que vincule la vía ALK con la fibromatosis gingival (actualmente inexistente)
- Estudios preclínicos (in vitro/in vivo) antes de cualquier consideración clínica
- Datos de MOA completos de DrugBank (DG002)
- Prospecto TFDA/AEMPS con advertencias y contraindicaciones (DG001, bloqueante)
- Revisión de la calidad del mapeo de ontología de enfermedades en este candidato, dado que otros nodos del mismo panel (rangos 5 y 7) muestran indicios de errores de asociación similares
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

