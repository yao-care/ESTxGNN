---
layout: default
title: Lornoxicam
parent: 僅模型預測 (L5)
nav_order: 174
evidence_level: L5
indication_count: 10
---

# Lornoxicam
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

# Lornoxicam: De Dolor y Trastornos Musculoesqueléticos Inflamatorios a Artritis Reumatoide

## Resumen en Una Frase

Lornoxicam es un antiinflamatorio no esteroideo (AINE) de la clase oxicam, tradicionalmente utilizado para el dolor agudo y los trastornos musculoesqueléticos e inflamatorios como la osteoartritis y el dolor postoperatorio. El modelo TxGNN predice que también podría ser efectivo para la **Artritis Reumatoide**, dirección respaldada actualmente por **20 publicaciones** (aunque sin ensayos clínicos registrados específicamente para esta indicación en la base consultada).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dolor y trastornos inflamatorios musculoesqueléticos (osteoartritis, dolor postoperatorio agudo, lumbociática aguda) — sin ficha técnica TFDA/AEMPS disponible para confirmar texto oficial |
| Nueva Indicación Predicha | Artritis Reumatoide |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos estructurados sobre el mecanismo de acción (Data Gap en la ficha de DrugBank). Según la literatura disponible, lornoxicam es un AINE de la clase oxicam que inhibe de forma no selectiva las enzimas ciclooxigenasa COX-1 y COX-2, reduciendo la síntesis de prostaglandinas y ejerciendo así efectos analgésicos, antiinflamatorios y antipiréticos comparables en potencia a analgésicos opioides como la morfina o la petidina.

La propia literatura de perfil farmacológico del fármaco (Ahmed & Al-Badr, 2011) ya lo describe como un medicamento "utilizado en trastornos musculares, esqueléticos y articulares como la osteoartritis y la artritis reumatoide", lo que indica que la predicción de TxGNN no es una extrapolación lejana, sino una extensión dentro del mismo espectro de enfermedades articulares inflamatorias para las que el fármaco ya cuenta con antecedentes de uso descritos en la literatura.

Mecanísticamente, la inhibición de COX-1/COX-2 reduce los mediadores inflamatorios (prostaglandinas) responsables del dolor, la rigidez matutina y la sinovitis características de la artritis reumatoide. El hecho de que múltiples grupos de investigación hayan desarrollado formulaciones cronoterapéuticas específicas (mini-tabletas de liberación pulsátil, geles transdérmicos) diseñadas para el patrón de rigidez matutina de la AR confirma que la comunidad científica ya considera esta indicación un objetivo terapéutico plausible para el fármaco.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación (artritis reumatoide).

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|------------------------|
| [12404032](https://pubmed.ncbi.nlm.nih.gov/12404032/) | 2002 | ECA cruzado, doble ciego | Reumatismo | Comparó lornoxicam (8 y 16 mg/día) con diclofenac 150 mg/día en pacientes con AR; evaluó eficacia analgésica y seguridad |
| [12207202](https://pubmed.ncbi.nlm.nih.gov/12207202/) | 2002 | Estudio clínico de largo plazo | Minerva Medica | Evaluación a largo plazo de la eficacia y seguridad de lornoxicam en artritis reumatoide |
| [12087911](https://pubmed.ncbi.nlm.nih.gov/12087911/) | 2002 | Estudio clínico | Terapevticheskii Arkhiv | Eficacia clínica de xefocam (lornoxicam) y su efecto sobre presión arterial y variabilidad del ritmo cardíaco en pacientes con AR e hipertensión |
| [19821419](https://pubmed.ncbi.nlm.nih.gov/19821419/) | 2009 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Confirma el uso establecido de lornoxicam en osteoartritis, AR, lumbociática aguda y dolor postoperatorio en 31 países |
| [8706598](https://pubmed.ncbi.nlm.nih.gov/8706598/) | 1996 | Revisión | Drugs | Perfil farmacológico de lornoxicam; eficacia comparable a analgésicos opioides en dolor e inflamación |
| [22469263](https://pubmed.ncbi.nlm.nih.gov/22469263/) | 2011 | Revisión | Profiles Drug Subst Excip Relat Methodol | Perfil integral del fármaco; describe su uso en osteoartritis y artritis reumatoide |
| [12240779](https://pubmed.ncbi.nlm.nih.gov/12240779/) | 2002 | Revisión de literatura | Clinical Therapeutics | Relaciones dosis-efecto de AINEs (incluye lornoxicam) en AR y osteoartritis |
| [29056774](https://pubmed.ncbi.nlm.nih.gov/29056774/) | 2017 | Revisión | Reumatologia | Manejo de glucocorticoides en AR según cronoterapia, relevante para el diseño cronoterapéutico de lornoxicam |
| [27042335](https://pubmed.ncbi.nlm.nih.gov/27042335/) | 2016 | Revisión | RMD Open | Relación entre el ritmo circadiano de la inflamación nocturna y los síntomas matutinos en AR |
| [29026298](https://pubmed.ncbi.nlm.nih.gov/29026298/) | 2017 | Estudio en animales | Int J Nanomedicine | Comparó eficacia de formulación nanomicelar de lornoxicam vs. lornoxicam libre en modelos experimentales de AR |

---

## Información de Mercado en España

Lornoxicam no está actualmente comercializado en España (0 autorizaciones registradas en los datos consultados).

---

## Consideraciones de Seguridad

No se dispone de datos de advertencias, contraindicaciones ni interacciones farmacológicas en las fuentes consultadas. Este vacío está clasificado como **Blocking** (DG001: ausencia de ficha técnica/prospecto TFDA), lo que impide realizar la evaluación de seguridad preliminar (S1) para este fármaco. Consultar el prospecto oficial en cuanto esté disponible.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje TxGNN es muy alto (99.90%) y la evidencia de nivel L3 —incluyendo un ensayo cruzado doble ciego frente a diclofenac y un estudio clínico de largo plazo en AR, además de literatura de perfil farmacológico que ya sitúa a la AR entre los usos documentados del fármaco— hace de esta una hipótesis razonable. Sin embargo, la ausencia total de datos de seguridad regulatoria (advertencias, contraindicaciones, interacciones), clasificada como vacío **Blocking**, impide avanzar responsablemente a la etapa de evaluación de seguridad, independientemente de la solidez de la evidencia de eficacia.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha técnica (TFDA/AEMPS) para completar advertencias, contraindicaciones e interacciones farmacológicas (DG001, prioridad Blocking)
- Confirmar el mecanismo de acción detallado vía DrugBank (DG002)
- Actualizar o replicar con un ensayo clínico aleatorizado controlado moderno dirigido específicamente a artritis reumatoide (la evidencia clínica existente data de 2002 y tiene tamaños muestrales limitados)
- Evaluar la viabilidad regulatoria de una nueva autorización de comercialización en España, dado que el fármaco no está actualmente registrado en el mercado español
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

