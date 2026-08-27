---
layout: default
title: Erenumab
parent: 僅模型預測 (L5)
nav_order: 109
evidence_level: L5
indication_count: 1
---

# Erenumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Erenumab: De la Prevención de la Migraña a la Migraña con Aura de Tronco Encefálico

## Resumen en Una Frase

Erenumab es un anticuerpo monoclonal humano dirigido contra el receptor de CGRP (Calcitonin Gene-Related Peptide), utilizado originalmente para la prevención de la migraña episódica y crónica. El modelo TxGNN predice que podría ser efectivo específicamente para la **migraña con aura de tronco encefálico**, con una puntuación de predicción del **99.89%**. Actualmente no existen ensayos clínicos diseñados específicamente para este subtipo, pero la dirección está respaldada por **20 publicaciones**, incluyendo análisis post-hoc de ensayos de Fase 3 y estudios de cohorte del mundo real.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Prevención de la migraña (episódica y crónica) — inferido de la literatura incluida; no hay ficha técnica/autorización registrada en el mercado objetivo |
| Nueva Indicación Predicha | Migraña con aura de tronco encefálico |
| Puntaje de Predicción TxGNN | 99.89% (rank #2680) |
| Nivel de Evidencia | L3 |
| Estado de Mercado | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos estructurados sobre el mecanismo de acción de erenumab en esta ficha (campo MOA marcado como brecha de datos, DG002, pendiente de consulta en DrugBank). Según la información contenida en la literatura recopilada en este informe, erenumab es un anticuerpo monoclonal de la clase anti-CGRP (antagonista del receptor de CGRP), cuya eficacia en la prevención de la migraña ha sido ampliamente comprobada en múltiples ensayos clínicos de Fase 3, y mecanísticamente podría ser aplicable a la migraña con aura de tronco encefálico.

El mecanismo propuesto es el siguiente: erenumab bloquea la vasodilatación mediada por CGRP y la sensibilización del sistema trigeminovascular, una vía considerada relevante en la fisiopatología de la migraña, incluyendo los subtipos con aura. En teoría, la inhibición de la señalización de CGRP podría reducir la frecuencia de la depresión cortical propagada (*cortical spreading depression*), fenómeno asociado a los síntomas de aura. A diferencia de los triptanes (agonistas 5-HT1B/1D, con efecto vasoconstrictor, tradicionalmente evitados en la migraña con aura de tronco encefálico o hemipléjica por riesgo isquémico), erenumab no provoca vasoconstricción cerebral directa —el estudio PMID 32867533 mostró que no altera la hemodinámica cerebral ni la función endotelial—, lo que teóricamente podría ofrecer un perfil de seguridad más favorable para este subtipo específico.

Sin embargo, esta extrapolación mecanística tiene límites: el estudio PMID 38850034 demuestra que algunas vías de inducción de la migraña (mediadas por cGMP) son independientes de la activación del receptor de CGRP, incluso en pacientes pretratados con erenumab. Esto evidencia una heterogeneidad mecanística dentro de la migraña con aura y limita la certeza de que el bloqueo de CGRP sea suficiente para controlar específicamente el subtipo de tronco encefálico. En conjunto, el vínculo mecanístico es razonable pero indirecto, y carece de validación fisiopatológica dedicada a este subtipo concreto.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados específicamente para "migraña con aura de tronco encefálico" (0 resultados en ClinicalTrials.gov e ICTRP).

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34928306](https://pubmed.ncbi.nlm.nih.gov/34928306/) | 2022 | ECA (análisis post-hoc Fase 3) | JAMA Neurology | Análisis secundario de ECAs sobre seguridad y eficacia de erenumab en migraña con y sin aura; sin diferencias relevantes de seguridad entre subgrupos |
| [30360965](https://pubmed.ncbi.nlm.nih.gov/30360965/) | 2018 | ECA Fase 3b | Lancet | Ensayo aleatorizado, doble ciego, controlado con placebo: eficacia y tolerabilidad en migraña episódica refractaria a 2-4 tratamientos preventivos previos |
| [37012858](https://pubmed.ncbi.nlm.nih.gov/37012858/) | 2023 | Revisión sistemática | Int Immunopharmacol | Confirma la eficacia de erenumab en la profilaxis de migraña episódica y crónica |
| [41888647](https://pubmed.ncbi.nlm.nih.gov/41888647/) | 2026 | Cohorte (estudio REFORM) | J Headache Pain | Caracteriza cambios longitudinales en la frecuencia de aura migrañosa durante y después del tratamiento con erenumab |
| [40275185](https://pubmed.ncbi.nlm.nih.gov/40275185/) | 2025 | Cohorte (biomarcador, REFORM) | J Headache Pain | Niveles plasmáticos de suPAR (biomarcador inflamatorio elevado en migraña con aura) asociados a la respuesta terapéutica a erenumab |
| [36942409](https://pubmed.ncbi.nlm.nih.gov/36942409/) | 2023 | Cohorte/Observacional | Headache | Análisis post-hoc de datos a largo plazo: riesgo cardiovascular de erenumab en pacientes con y sin aura, sin señales de alarma según nivel de riesgo CV basal |
| [38850034](https://pubmed.ncbi.nlm.nih.gov/38850034/) | 2024 | Mecanístico/Experimental | Cephalalgia | La inducción de migraña mediada por cGMP (sildenafilo) es independiente de la activación del receptor de CGRP, incluso con pretratamiento con erenumab |
| [32867533](https://pubmed.ncbi.nlm.nih.gov/32867533/) | 2021 | Mecanístico/Fisiológico | Cephalalgia | Erenumab no altera la hemodinámica cerebral ni la función endotelial en migraña sin aura |
| [35151970](https://pubmed.ncbi.nlm.nih.gov/35151970/) | 2022 | Cohorte (mundo real) | Clin Neurol Neurosurg | Efectivo y seguro tras 6 meses en migraña crónica resistente a múltiples clases de tratamiento preventivo (experiencia croata) |
| [35538414](https://pubmed.ncbi.nlm.nih.gov/35538414/) | 2022 | Cohorte (seguridad a largo plazo) | J Headache Pain | Estudio retrospectivo de 12 meses: buen perfil de seguridad y tolerabilidad, baja tasa de discontinuación por eventos adversos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se dispone de advertencias, contraindicaciones ni datos de interacciones farmacológicas verificados en esta ficha (consulta a TFDA aún pendiente — ver brecha de datos DG001, de severidad *Blocking*).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia disponible se limita a análisis post-hoc/secundarios de ECAs de Fase 3 y estudios de cohorte del mundo real sobre migraña con aura en general (nivel L3); no existe ningún ensayo clínico diseñado específicamente para el subtipo "migraña con aura de tronco encefálico". Además, una brecha de datos de severidad *Blocking* (DG001: ausencia de advertencias/contraindicaciones del prospecto TFDA) impide completar la evaluación de seguridad inicial (S1), por lo que no es posible avanzar de etapa en este momento.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha técnica de TFDA con advertencias y contraindicaciones (remediación de DG001, *bloqueante*)
- Completar los datos de mecanismo de acción (MOA) vía DrugBank (remediación de DG002)
- Datos de interacciones farmacológicas (DDI), actualmente no encontrados
- Diseño o identificación de un ensayo clínico dirigido específicamente a la subpoblación de migraña con aura de tronco encefálico (actualmente 0 ensayos registrados)
- Evaluación de la viabilidad regulatoria y de mercado, dado que el fármaco actualmente no está comercializado (0 autorizaciones)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

