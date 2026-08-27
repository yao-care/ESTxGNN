---
layout: default
title: Erdafitinib
parent: 僅模型預測 (L5)
nav_order: 108
evidence_level: L5
indication_count: 6
---

# Erdafitinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Usando el formato del Prompt de Informe de Evaluación de Reposicionamiento de Fármacos, genero el informe a partir del Evidence Pack proporcionado. Antes de completar campos con datos ausentes, sigo la regla de no adivinar: cuando el JSON no trae el dato (p. ej. indicación original, MOA formal, licencias en España), lo señalo explícitamente como pendiente en lugar de inventarlo, y me apoyo únicamente en lo que consta en `meta.data_gaps`, `drug`, `taiwan_regulatory`, `predicted_indications` y `safety`.

---

# Erdafitinib: De Indicación Original No Disponible a Hipertensión Pulmonar

## Resumen en Una Frase

Este *evidence pack* no incluye la(s) indicación(es) original(es) aprobada(s) de erdafitinib ni su mecanismo de acción formal (brechas de datos DG001 y DG002).
El modelo TxGNN predice que erdafitinib podría ser efectivo para **Hipertensión Pulmonar** (la de mayor puntaje entre 6 indicaciones candidatas evaluadas),
pero actualmente **no existe ningún ensayo clínico ni publicación** que respalde específicamente esta dirección — se trata de una predicción de nivel **L5** (solo modelo, sin estudios reales).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en este evidence pack (ver Limitaciones de Datos, DG001) |
| Nueva Indicación Predicha | Hipertensión Pulmonar |
| Puntaje de Predicción TxGNN | 99.38% |
| Nivel de Evidencia | L5 (predicción del modelo, sin estudios reales) |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

### Panorama de las 6 Indicaciones Predichas

Este candidato (`TW-DB12147-multi`) fue evaluado frente a 6 indicaciones posibles. Ninguna alcanza un nivel de evidencia superior a L4, y todas mantienen recomendación **Hold**:

| Rank | Indicación Predicha | Puntaje TxGNN | Nivel de Evidencia | Decisión |
|------|---------------------|---------------|---------------------|----------|
| 1 | Hipertensión Pulmonar | 99.38% | L5 | Hold |
| 2 | Cardiopatía Cifoscoliótica | 99.27% | L5 | Hold |
| 3 | Amenorrea | 99.26% | L5 | Hold |
| 4 | Artritis Reumatoide | 99.25% | L4 | Hold |
| 5 | Esclerosis Lateral Amiotrófica (ELA) | 99.06% | L5 | Hold |
| 6 | Síndrome de Braquidactilia-Sindactilia | 99.03% | L5 | Hold |

---

## Por qué es Razonable esta Predicción?

El campo formal de mecanismo de acción (MOA) de erdafitinib no está disponible en este evidence pack (brecha DG002, severidad Alta). Sin embargo, las justificaciones mecanísticas asociadas a cada indicación predicha señalan de forma consistente que erdafitinib actúa como **inhibidor pan-FGFR** (Fibroblast Growth Factor Receptor), lo cual es coherente con su clasificación como inhibidor de proteína quinasa de molécula pequeña descrita en la literatura recuperada (Roskoski, 2020).

La plausibilidad mecanística varía considerablemente entre las 6 indicaciones candidatas. En el extremo más favorable, el **Síndrome de Braquidactilia-Sindactilia** (rank 6) y la **Artritis Reumatoide** (rank 4) tienen una base biológica razonable: mutaciones de ganancia de función en FGFR1-3 causan síndromes esqueléticos de este tipo, y la señalización FGF/FGFR participa en la angiogénesis del pannus sinovial en artritis reumatoide. En el extremo opuesto, **Amenorrea** (rank 3) y **Esclerosis Lateral Amiotrófica** (rank 5) presentan una dirección mecanística contradictoria: la pérdida de función de FGFR1 es causa conocida del Síndrome de Kallmann (que produce amenorrea secundaria), y la señalización FGF/FGFR suele ser neuroprotectora, por lo que un inhibidor de FGFR podría en teoría agravar estos cuadros en vez de tratarlos.

Dado que la indicación original de erdafitinib no consta en este evidence pack, no es posible establecer aquí una relación mecanística formal entre el uso aprobado y las indicaciones predichas; el análisis anterior se basa exclusivamente en las justificaciones de reposicionamiento (`repurposing_rationale`) incluidas en el propio evidence pack, ninguna de las cuales cuenta con respaldo preclínico o clínico directo específico para erdafitinib.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para Hipertensión Pulmonar (indicación principal).

De hecho, según el registro de consultas (`query_log`), **ninguna de las 6 indicaciones candidatas** tiene ensayos registrados en ClinicalTrials.gov ni en ICTRP.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para Hipertensión Pulmonar (indicación principal).

La única indicación candidata con literatura asociada es **Artritis Reumatoide** (rank 4):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31862477](https://pubmed.ncbi.nlm.nih.gov/31862477/) | 2020 | Revisión | Pharmacological Research | Revisión general de inhibidores de proteína quinasa aprobados por la FDA (incluye erdafitinib); no evalúa específicamente su eficacia en artritis reumatoide |

**Nota importante:** este artículo es una revisión farmacológica general sobre inhibidores de quinasas aprobados en 2019 (entrectinib, erdafitinib, pexidartinib, fedratinib), no un estudio clínico ni preclínico dirigido a artritis reumatoide. No debe interpretarse como evidencia de eficacia.

---

Erdafitinib no está actualmente comercializado en España — no hay autorizaciones registradas en este evidence pack (0 licencias).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

*Nota: la brecha de datos DG001 (advertencias/contraindicaciones del prospecto de la TFDA) está clasificada como **Bloqueante**, ya que impide completar la evaluación de seguridad inicial (S1). Este dato debe obtenerse antes de avanzar cualquier candidato de erdafitinib a fases posteriores.*

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Las 6 indicaciones predichas para erdafitinib se encuentran en nivel de evidencia L4 (mecanístico/revisión, sin estudio dirigido) o L5 (solo predicción del modelo), sin ningún ensayo clínico registrado. Además, persiste una brecha de datos **bloqueante** sobre las advertencias y contraindicaciones del prospecto, lo que impide completar la evaluación de seguridad inicial.

**Para avanzar se necesita:**
- Resolver la brecha bloqueante DG001: obtener el prospecto/ficha técnica oficial (advertencias, contraindicaciones) desde la fuente regulatoria correspondiente
- Resolver la brecha DG002: confirmar el mecanismo de acción formal y las categorías DrugBank (para determinar, entre otras cosas, si aplica clasificación antineoplásica/citotóxica)
- Obtener la(s) indicación(es) original(es) aprobada(s) de erdafitinib, actualmente ausente en este evidence pack
- Para Artritis Reumatoide (la única candidata en L4): buscar estudios preclínicos o mecanísticos dirigidos específicamente a esta indicación, no solo revisiones farmacológicas generales
- Para las indicaciones con dirección mecanística contradictoria (Amenorrea, ELA): evaluar si corresponden más a señales de riesgo/efecto adverso que a candidatas de reposicionamiento
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

