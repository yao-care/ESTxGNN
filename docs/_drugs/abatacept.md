---
layout: default
title: Abatacept
parent: 僅模型預測 (L5)
nav_order: 12
evidence_level: L5
indication_count: 10
---

# Abatacept
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

# Abatacept: De Artritis Reumatoide a Vasculitis Reumatoide

## Resumen en Una Frase

Abatacept es una proteína de fusión biológica (CTLA4-Ig) utilizada originalmente para el tratamiento de la artritis reumatoide (indicación de referencia internacionalmente conocida; no existen datos de licencia local en este Evidence Pack).
El modelo TxGNN predice que podría ser efectivo para **Vasculitis Reumatoide**, una manifestación extraarticular grave de la artritis reumatoide,
con **1 ensayo clínico** (aún no reclutando, solo indirectamente relacionado) y **20 publicaciones** —en su mayoría reportes de caso— que respaldan de forma preliminar esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Artritis Reumatoide *(información general conocida sobre el fármaco; no se dispone de datos de licencia local — ver nota abajo)* |
| Nueva Indicación Predicha | Vasculitis Reumatoide |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Taiwán/España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

> **Nota sobre la Indicación Original**: El Evidence Pack no contiene ningún registro de licencia local (`taiwan_regulatory.licenses` está vacío) ni indicaciones originales estructuradas (`drug.original_indications` está vacío). La indicación "Artritis Reumatoide" se cita aquí como información pública ampliamente conocida sobre este principio activo, no como un dato extraído del Evidence Pack.

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, Abatacept es una proteína de fusión que combina la región Fc de la inmunoglobulina IgG1 con el dominio extracelular de CTLA-4; se une a CD80/CD86 en las células presentadoras de antígeno y bloquea la señal de coestimulación CD28, inhibiendo así la activación de los linfocitos T. Esta acción ha demostrado eficacia clínica establecida en la artritis reumatoide.

La vasculitis reumatoide es la manifestación extraarticular más grave de la artritis reumatoide, y comparte con ella una base fisiopatológica de inflamación crónica mediada por linfocitos T, lo que da soporte teórico a la hipótesis de que Abatacept —ya activo sobre esta vía— podría tener beneficio también en la vasculitis asociada.

Sin embargo, la vasculitis reumatoide en sí misma se caracteriza patológicamente más por el depósito de inmunocomplejos y la activación de linfocitos B/neutrófilos que por la vía de coestimulación CD28, por lo que la relación mecanística directa es más débil que en la artritis reumatoide clásica. Además, existe una señal contradictoria en la literatura: un caso documentado (PMID 27052429) describe la aparición de novo de vasculitis reumatoide **durante** el tratamiento con Abatacept, con mejoría posterior tras cambiar a rituximab. Esto obliga a una evaluación cautelosa antes de avanzar.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Fase 2 | Aún no reclutando | 80 | Evalúa el manejo perioperatorio de inmunosupresores en pacientes reumatológicos sometidos a artroplastia total de hombro (brotes, dolor, complicaciones de la herida). Solo indirectamente relacionado con vasculitis reumatoide; no es un ensayo de eficacia de Abatacept en esta indicación. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29930884](https://pubmed.ncbi.nlm.nih.gov/29930884/) | 2018 | Reporte de caso | Cureus | Abatacept usado con éxito en un caso de vasculitis reumatoide cutánea en paciente con inmunodeficiencia común variable, tras evitar rituximab por riesgo de exacerbación inmunológica. |
| [27052429](https://pubmed.ncbi.nlm.nih.gov/27052429/) | 2016 | Reporte de caso | Joint Bone Spine | **Señal contradictoria**: aparición de novo de vasculitis reumatoide durante el tratamiento con Abatacept, con mejoría posterior tras cambio a rituximab. |
| [22124545](https://pubmed.ncbi.nlm.nih.gov/22124545/) | 2012 | Reporte de caso | Modern Rheumatology | Abatacept produjo rápida mejoría clínica en una paciente con vasculitis reumatoide refractaria a metotrexato, anti-TNF, esteroides e IL-6i. |
| [36418100](https://pubmed.ncbi.nlm.nih.gov/36418100/) | 2023 | Reporte de caso | Internal Medicine (Tokyo) | Nefritis asociada a ANCA (MPO) desarrollada durante tratamiento con Abatacept y adalimumab en artritis reumatoide; tocilizumab atenuó el cuadro. |
| [30119075](https://pubmed.ncbi.nlm.nih.gov/30119075/) | 2018 | Reporte de caso | Ophthalmic Plastic and Reconstructive Surgery | Vasculitis orbitaria bilateral asociada a artritis reumatoide en paciente bajo Abatacept, con progresión pese a ciclofosfamida. |
| [34068884](https://pubmed.ncbi.nlm.nih.gov/34068884/) | 2021 | Revisión | Journal of Clinical Medicine | Revisión sobre diagnóstico y tratamiento de epiescleritis/escleritis asociadas a artritis reumatoide, manifestaciones relacionadas con vasculitis ocular. |
| [24854356](https://pubmed.ncbi.nlm.nih.gov/24854356/) | 2014 | Estudio de cohorte | Annals of the Rheumatic Diseases | Estudio de cohorte único centro sobre la utilidad del ANA seriado para predecir lupus/vasculitis inducidos por bDMARD en artritis reumatoide. |
| [31174819](https://pubmed.ncbi.nlm.nih.gov/31174819/) | 2018 | Revisión | Best Practice & Research Clin Rheumatology | Revisión sobre afectación del sistema nervioso central (incluyendo vasculitis cerebral) en artritis reumatoide y el papel de los agentes biológicos. |
| [33482962](https://pubmed.ncbi.nlm.nih.gov/33482962/) | 2020 | Reporte de caso | The Permanente Journal | Caso de derrames pleural y pericárdico loculados en artritis reumatoide, con mención de vasculitis reumatoide entre las manifestaciones sistémicas. |
| [24493331](https://pubmed.ncbi.nlm.nih.gov/24493331/) | 2015 | Revisión de casos | Clinical Rheumatology | Revisión de uso off-label de Abatacept en miositis, con evidencia limitada a reportes de caso y estudios mecanísticos. |

---

## Información de Mercado en Taiwán/España

Abatacept **no está actualmente comercializado** en la jurisdicción de referencia (`market_status`: 未上市 / No comercializado). No existen autorizaciones de comercialización registradas en el Evidence Pack (`total_licenses`: 0), por lo que no es posible presentar una tabla de productos/formas farmacéuticas locales.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

*(El Evidence Pack marca las advertencias principales, contraindicaciones e interacciones farmacológicas como datos no disponibles. Adicionalmente, el registro de brechas de datos (`data_gaps`) identifica esta ausencia de advertencias/contraindicaciones del TFDA como una brecha de severidad **Blocking** (DG001), que impide actualmente completar la evaluación de seguridad en la etapa S1.)*

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia disponible para Abatacept en vasculitis reumatoide corresponde al Nivel L4 (mayormente reportes de caso y un único ensayo Fase 2 aún sin reclutar, solo indirectamente relacionado). El vínculo mecanístico es plausible pero más débil que en la artritis reumatoide clásica, y existe una señal contradictoria documentada (PMID 27052429) de aparición de vasculitis reumatoide *durante* el propio tratamiento con Abatacept. Además, la ausencia de datos de advertencias/contraindicaciones del TFDA (brecha bloqueante DG001) impide completar la evaluación de seguridad inicial, y el fármaco no está comercializado en la jurisdicción de referencia.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha técnica del TFDA (advertencias, contraindicaciones) — brecha bloqueante (DG001)
- Obtener datos detallados del mecanismo de acción (MOA) vía DrugBank — brecha de alta prioridad (DG002)
- Un estudio controlado (observacional o ensayo clínico) específico para vasculitis reumatoide, dado que la evidencia actual se limita a reportes de caso aislados
- Resolver la señal contradictoria (PMID 27052429) mediante revisión sistemática o análisis de farmacovigilancia antes de continuar
- Confirmar el estatus regulatorio/de comercialización local si se decide continuar la evaluación
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

