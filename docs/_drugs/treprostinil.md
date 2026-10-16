---
layout: default
title: Treprostinil
parent: Solo predicción del modelo (L5)
nav_order: 821
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Treprostinil: nueva indicación predicha, Malformación arteriovenosa pulmonar (nivel de evidencia L5). Indicación original: Hipertensión arterial pulmonar (los textos de indicación de las autor…"
monitor_inn: "treprostinil"
predicted_indications: ["pulmonary arteriovenous malformation (disease)", "pulmonary arterial hypertension associated with congenital heart disease", "pulmonary arterial hypertension associated with connective tissue disease", "pulmonary arterial hypertension associated with chronic hemolytic anemia", "pulmonary arterial hypertension associated with schistosomiasis", "pulmonary arterial hypertension associated with HIV infection", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "malformation syndrome with odontal and/or periodontal component", "Ambras type hypertrichosis universalis congenita"]
---

# Treprostinil
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Treprostinil: De Hipertensión Arterial Pulmonar a Malformación Arteriovenosa Pulmonar

## Resumen en Una Frase

Treprostinil es un análogo de la prostaciclina, originalmente utilizado para el tratamiento de la hipertensión arterial pulmonar (HAP).
El modelo TxGNN predice que podría ser efectivo para **malformación arteriovenosa pulmonar**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, por lo que se trata solo de una predicción computacional.

> **Nota importante:** la predicción de mayor puntaje (malformación arteriovenosa pulmonar) carece de plausibilidad biológica y de evidencia. Entre las predicciones secundarias, la **HAP asociada a cardiopatía congénita** y la **HAP asociada a enfermedad del tejido conectivo** son las que cuentan con mayor respaldo en la literatura; se describen en este informe como alternativas más prometedoras.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial pulmonar (los textos de indicación de las autorizaciones españolas no están disponibles; se toma la indicación de la base de conocimiento) |
| Nueva Indicación Predicha | Malformación arteriovenosa pulmonar |
| Puntaje de Predicción TxGNN | 99,70% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Treprostinil es un análogo estable de la prostaciclina que produce vasodilatación e inhibe la agregación plaquetaria. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente consultada, pero estas propiedades farmacológicas son bien conocidas.

En este caso, la relación mecanística es **débil**. Las malformaciones arteriovenosas pulmonares son cortocircuitos vasculares estructurales, no un problema de vasoconstricción o remodelado vascular como en la HAP. En teoría, la vasodilatación podría incluso empeorar el cortocircuito o la hipoxemia. Por ello, esta predicción debe interpretarse con mucha cautela.

Por el contrario, varias predicciones de menor puntaje son mecanísticamente coherentes, al ser subtipos de HAP del Grupo 1 de la OMS: cardiopatía congénita, enfermedad del tejido conectivo, VIH y esquistosomiasis. Otras predicciones (hipotricosis, hipertricosis congénita, síndromes malformativos con componente dental) parecen artefactos del grafo de conocimiento sin vínculo mecanístico plausible.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para malformación arteriovenosa pulmonar.

### Literatura de la alternativa más respaldada: HAP asociada a cardiopatía congénita

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29436381](https://pubmed.ncbi.nlm.nih.gov/29436381/) | 2018 | Cohorte | Heart | Eficacia y seguridad de treprostinil subcutáneo a 12 meses en adultos con HAP asociada a cardiopatía congénita |
| [23890862](https://pubmed.ncbi.nlm.nih.gov/23890862/) | 2013 | Cohorte | Int J Cardiol | Efectos hemodinámicos y clínicos a largo plazo de prostaciclinas continuas en 8 adultos con HAP-cardiopatía congénita; se discute el riesgo teórico de empeorar el cortocircuito derecha-izquierda |
| [35412560](https://pubmed.ncbi.nlm.nih.gov/35412560/) | 2022 | Revisión | JAMA | Revisión sobre diagnóstico y tratamiento de la HAP |
| [18473715](https://pubmed.ncbi.nlm.nih.gov/18473715/) | 2008 | Revisión | Expert Opin Pharmacother | Revisión del uso de treprostinil en hipertensión pulmonar |
| [35000655](https://pubmed.ncbi.nlm.nih.gov/35000655/) | 2022 | Reporte de caso | Cardiol Young | Mejora hemodinámica con treprostinil subcutáneo en un niño con trisomía 21 y HAP-cardiopatía congénita |
| [41201625](https://pubmed.ncbi.nlm.nih.gov/41201625/) | 2026 | Registro | J Heart Lung Transplant | Terapia añadida con prostaciclinas parenterales en HAP según el registro COMPERA |

### Literatura de HAP asociada a enfermedad del tejido conectivo

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11897647](https://pubmed.ncbi.nlm.nih.gov/11897647/) | 2002 | Ensayo doble ciego controlado con placebo | Am J Respir Crit Care Med | Infusión subcutánea continua de treprostinil durante 12 semanas en HAP (población general) |
| [15302727](https://pubmed.ncbi.nlm.nih.gov/15302727/) | 2004 | Análisis de subgrupo | Chest | Eficacia y seguridad de treprostinil subcutáneo en HAP asociada a enfermedad del tejido conectivo |
| [38378970](https://pubmed.ncbi.nlm.nih.gov/38378970/) | 2024 | Revisión sistemática y metaanálisis | Intern Emerg Med | Metaanálisis de ECA sobre el tratamiento de la HAP en enfermedades del tejido conectivo |
| [41594679](https://pubmed.ncbi.nlm.nih.gov/41594679/) | 2026 | Revisión | Biomolecules | Estrategias terapéuticas actuales y perspectivas en HAP-ETC |

### Literatura de HAP asociada a VIH

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [14720012](https://pubmed.ncbi.nlm.nih.gov/14720012/) | 2003 | Revisión | Am J Respir Med | Revisión de prostanoides en HAP, incluida la asociada a VIH (evidencia indirecta) |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1191419001 | TREPULMIX 1 mg/ml | Solución para perfusión | No disponible |
| 88063 | TREPROSTINILO ZENTIVA 5 mg/ml EFG | Solución para perfusión | No disponible |
| 83747 | TREPROSTINILO FERRER 2,5 mg/ml EFG | Solución para perfusión | No disponible |
| 84772 | TRESUVI 2,5 mg/ml EFG | Solución para perfusión | No disponible |
| 84986 | TREPROSTINILO DR REDDYS 5 mg/ml EFG | Solución para perfusión | No disponible |

Se muestran 5 de las 20 autorizaciones vigentes (todas de principio activo único, ninguna cancelada).

---

## Consideraciones de Seguridad

- **Contraindicaciones / enfermedades de precaución (base de conocimiento, no texto del prospecto)**: enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, trastornos hipotensivos, enfermedades de la coagulación sanguínea y enfermedad pulmonar.
- **Interacciones farmacológicas**: se registran 327 interacciones. Entre las de nivel moderado destacan epinefrina, ácido acetilsalicílico, inhibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina, ertugliflozina), manitol, efedrina, fenfluramina y dexfenfluramina, glicerina, papaverina y sibutramina. También constan interacciones de nivel no clasificado con pantoprazol, omeprazol, lansoprazol, prednisona, simvastatina y cloruro de potásico.
- **Precauciones específicas de las alternativas**: en HAP con cardiopatía congénita, la fisiología de Eisenmenger y los cortocircuitos sistémico-pulmonares requieren evaluación especializada; vigilar infecciones del sitio de infusión y relacionadas con el catéter. En HAP asociada a VIH, evaluar las interacciones con la terapia antirretroviral.

Para información completa de advertencias y contraindicaciones, consultar el prospecto, ya que no se ha podido obtener de la ficha técnica de la AEMPS.

---

## Conclusión y Próximos Pasos

**Decisión: Hold** (para malformación arteriovenosa pulmonar)

**Justificación:**
La predicción de mayor puntaje carece de ensayos, literatura y plausibilidad mecanística, y la vasodilatación podría empeorar el cortocircuito o la hipoxemia. Solo es una predicción del modelo (L5).

**Otras predicciones del modelo:**

| Indicación predicha | Puntaje | Nivel | Decisión |
|---|---|---|---|
| HAP asociada a cardiopatía congénita | 99,60% | L3 | Proceed with Guardrails |
| HAP asociada a enfermedad del tejido conectivo | 99,55% | L3 | Proceed with Guardrails |
| HAP asociada a VIH | 99,55% | L4 | Pregunta de investigación |
| HAP asociada a anemia hemolítica crónica | 99,55% | L5 | Hold |
| HAP asociada a esquistosomiasis | 99,55% | L5 | Hold |
| Hipotricosis simple del cuero cabelludo | 99,48% | L5 | Hold |
| Hipotricosis congénita con milia | 99,30% | L5 | Hold |
| Síndrome malformativo con componente dental/periodontal | 99,21% | L5 | Hold |
| Hipertricosis universal congénita tipo Ambras | 99,17% | L5 | Hold |

**Para avanzar se necesita:**
- Priorizar la evaluación de la HAP asociada a cardiopatía congénita y a enfermedad del tejido conectivo, confirmando el diseño de los estudios (los niveles L3 son asignaciones conservadoras basadas en títulos y resúmenes).
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), una brecha de datos bloqueante para la revisión de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Confirmar los textos de indicación aprobada de las autorizaciones españolas.
- Para HAP-VIH, estudios específicos y revisión de interacciones con antirretrovirales.
- Descartar o revisar manualmente las predicciones sin plausibilidad biológica (alopecia/hipertricosis, síndromes malformativos).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

