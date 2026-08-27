---
layout: default
title: Tramadol
parent: 僅模型預測 (L5)
nav_order: 280
evidence_level: L5
indication_count: 10
---

# Tramadol
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

# Tramadol: De Dolor Moderado-Intenso a Displasia Acromesomélica tipo Hunter-Thompson

## Resumen en Una Frase

Tramadol es un analgésico opioide de acción central (con componente SNRI) utilizado habitualmente para el dolor moderado a moderadamente intenso.
El modelo TxGNN predice que podría ser efectivo para **Displasia Acromesomélica tipo Hunter-Thompson**,
pero actualmente **0 ensayos clínicos** y **0 publicaciones** respaldan esta dirección específica.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Dolor moderado a moderadamente intenso (conocimiento general sobre tramadol; no incluido en el Evidence Pack, ver vacíos de datos) |
| Nueva Indicacion Predicha | Displasia Acromesomélica tipo Hunter-Thompson |
| Puntaje de Prediccion TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de tramadol en este Evidence Pack. Según la información general conocida, tramadol es un analgésico opioide de acción central (agonista débil del receptor mu) con un componente adicional inhibidor de la recaptación de serotonina/noradrenalina (SNRI), y su eficacia en el dolor moderado a moderadamente intenso está bien establecida.

Sin embargo, para la indicación predicha en primer lugar por TxGNN, la propia evaluación mecanística incluida en el Evidence Pack señala explícitamente que **no existe una relación fisiopatológica conocida**: la displasia acromesomélica tipo Hunter-Thompson es un trastorno congénito del desarrollo óseo asociado a la vía GDF5/CDMP1, sin conexión establecida con los mecanismos analgésicos (opioide/SNRI) de tramadol. Es decir, la puntuación alta del modelo no viene acompañada de una hipótesis biológica verificable con los datos actuales.

Por este motivo, esta predicción debe interpretarse como una señal exploratoria del modelo (L5), no como una hipótesis de reposicionamiento con respaldo mecanístico o clínico.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La indicación mejor puntuada por TxGNN (displasia acromesomélica tipo Hunter-Thompson) no cuenta con ningún ensayo clínico ni publicación de respaldo, y el propio análisis mecanístico del Evidence Pack indica que no hay relación fisiopatológica plausible con el mecanismo de acción de tramadol. La evidencia es insuficiente para avanzar (L5, sin hipótesis validable).

**Para avanzar se necesita:**
- Datos de ficha técnica/prospecto (advertencias y contraindicaciones), marcados como vacío bloqueante (DG001) — imprescindibles antes de cualquier evaluación de seguridad (S1)
- Datos del mecanismo de acción (MOA) de tramadol desde DrugBank (DG002), necesarios para evaluar la plausibilidad de cualquier indicación predicha
- Estudios preclínicos o de mecanismo que conecten la vía GDF5/CDMP1 con la analgesia opioide/SNRI, si se quiere sostener esta hipótesis concreta
- Nota adicional: entre las 10 indicaciones predichas, la **artritis idiopática juvenil** (rank 7, L4, etapa S1, "Research Question") presenta una racionalidad mecanística más plausible (uso analgésico off-label ya descrito en dolor reumático pediátrico refractario) y cuenta con literatura indexada, aunque no específica de tramadol. Podría ser un candidato secundario más prometedor para investigación adicional que la indicación de mayor puntaje.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

