---
layout: default
title: Levetiracetam
parent: 僅模型預測 (L5)
nav_order: 164
evidence_level: L5
indication_count: 10
---

# Levetiracetam
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

Using la información del Evidence Pack (v4, LEVETIRACETAM/DB01202), genero el informe siguiendo el formato indicado. Nota: `predicted_indications[0]` = "visual epilepsy" (score TxGNN mas alto), que es la indicación usada para el titulo/resumen segun la plantilla; al final senalo que otra prediccion mas abajo en el ranking tiene evidencia sustancialmente mas fuerte.

---

# Levetiracetam: De Epilepsia de Inicio Parcial a Epilepsia Visual

## Resumen en Una Frase

Levetiracetam (Keppra®) es un antiepiléptico de amplio espectro, utilizado originalmente para el tratamiento de crisis de inicio parcial en pacientes con epilepsia. El modelo TxGNN predice que podría ser efectivo para **Epilepsia Visual** (crisis reflejas inducidas por estímulos visuales/fotosensibilidad), con **9 ensayos clínicos** y **20 publicaciones** identificados, aunque ninguno diseñado específicamente para este subtipo.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicación Original | Epilepsia (crisis de inicio parcial, con o sin generalización secundaria) |
| Nueva Indicación Predicha | Epilepsia Visual (crisis reflejas fotosensibles) |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Research Question (evidencia insuficiente para avanzar de fase) |

## Por que es Razonable esta Prediccion?

No hay datos estructurados de DrugBank sobre el mecanismo de acción de levetiracetam (data gap identificado, severidad *High*). Sin embargo, la evidencia clínica y de literatura recopilada en este dossier describe de forma consistente que levetiracetam actúa uniéndose a la proteína de vesícula sináptica 2A (SV2A), modulando la liberación de neurotransmisores e inhibiendo canales de calcio tipo L, lo que reduce la sincronización de descargas corticales anómalas. Este es el mecanismo detrás de su indicación aprobada como antiepiléptico de amplio espectro (Keppra®).

La epilepsia visual pertenece al grupo de las epilepsias reflejas, en las que la hiperexcitabilidad cortical se desencadena por un estímulo específico (en este caso, luz intermitente o patrones visuales) en lugar de ocurrir de forma espontánea. Dado que el mecanismo de la epilepsia visual comparte la misma base fisiopatológica —hiperexcitabilidad cortical y sincronización anómala de descargas— que las crisis de inicio parcial ya tratadas por levetiracetam, existe una justificación mecanística razonable para la predicción.

No obstante, es importante matizar: de los 9 ensayos clínicos y 20 publicaciones recuperados, ninguno tiene diseño específico para epilepsia fotosensible/visual. La mayoría corresponde a poblaciones de hemorragia intracerebral, migraña, epilepsia neonatal o crisis post-traumáticas. Esto coloca la evidencia en nivel L4 (estudios de mecanismo/preclínicos y extrapolación), no en evidencia clínica directa del subtipo.

## Evidencia de Ensayos Clinicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT07336992](https://clinicaltrials.gov/study/NCT07336992) | Fase 3 | Aún no reclutando | 580 | Levetiracetam profiláctico en hemorragia intracerebral aguda para reducir crisis epilépticas; no específico de epilepsia visual (Relevancia C) |
| [NCT00203216](https://clinicaltrials.gov/study/NCT00203216) | N/A | Completado | 31 | Tratamiento profiláctico de migraña con o sin aura (incluye alteraciones visuales), abierto, monocéntrico |
| [NCT03107507](https://clinicaltrials.gov/study/NCT03107507) | Fase 4 | Desconocido | 40 | Eficacia de levetiracetam en control de crisis neonatales |
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Fase 4 | Completado | 111 | Estudio Liceo: eficacia de AEDs de nueva generación (incl. levetiracetam) como primera biterapia en epilepsia focal |
| [NCT04559529](https://clinicaltrials.gov/study/NCT04559529) | Fase 2 | Completado | 62 | Levetiracetam para reducir hiperactividad hipocampal en psicosis, usando tarea de procesamiento de escenas visuales por fMRI |
| [NCT04833907](https://clinicaltrials.gov/study/NCT04833907) | Fase 1/2 | Reclutamiento por invitación | 24 | Terapia génica intracraneal para enfermedad de Canavan; asociación indirecta, no evalúa levetiracetam como tratamiento primario |
| [NCT04277936](https://clinicaltrials.gov/study/NCT04277936) | Fase 2 | Terminado | 1 | Modulación farmacológica de hiperactividad hipocampal en psicosis; terminado prematuramente |
| [NCT04573803](https://clinicaltrials.gov/study/NCT04573803) | Fase 3 | Aún no reclutando | 1649 | Manejo de crisis post-traumatismo craneoencefálico (ensayo MAST), comparación de duración de tratamiento (Relevancia C) |
| [NCT00105040](https://clinicaltrials.gov/study/NCT00105040) | Fase 2 | Completado | 87 | Efectos cognitivos y neuropsicológicos de levetiracetam como tratamiento adyuvante en niños con crisis parciales refractarias |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35963261](https://pubmed.ncbi.nlm.nih.gov/35963261/) | 2022 | ECA Fase 3 (PEACH) | The Lancet Neurology | Levetiracetam profiláctico no redujo significativamente el riesgo de crisis epilépticas agudas tras hemorragia intracerebral |
| [32385134](https://pubmed.ncbi.nlm.nih.gov/32385134/) | 2020 | ECA | Pediatrics | Levetiracetam vs. fenobarbital para crisis neonatales; eficacia y seguridad comparadas en ausencia de terapias aprobadas por la FDA |
| [34286461](https://pubmed.ncbi.nlm.nih.gov/34286461/) | 2022 | Metaanálisis | Neurocritical Care | Revisión sistemática de levetiracetam como profilaxis de crisis en cuidados neurocríticos (HIC, TCE, hemorragia subaracnoidea) |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Revisión sistemática / meta-análisis en red | Journal of Neurology | Comparación de eficacia y seguridad de antiepilépticos en epilepsias generalizadas idiopáticas |
| [40450767](https://pubmed.ncbi.nlm.nih.gov/40450767/) | 2025 | Metaanálisis | Epilepsy & Behavior | Levetiracetam para crisis mioclónicas en epilepsia generalizada idiopática, incl. epilepsia mioclónica juvenil |
| [34260837](https://pubmed.ncbi.nlm.nih.gov/34260837/) | 2021 | Revisión | New England Journal of Medicine | Manejo inicial de crisis epilépticas en adultos |
| [38316735](https://pubmed.ncbi.nlm.nih.gov/38316735/) | 2024 | Guía de práctica clínica | Neurocritical Care | Guía para profilaxis de crisis en pacientes hospitalizados con TCE moderado-severo |
| [21936590](https://pubmed.ncbi.nlm.nih.gov/21936590/) | 2011 | Revisión | CNS Drugs | Revisión general de levetiracetam como antiepiléptico de segunda generación, incluidas sus indicaciones aprobadas |
| [38678766](https://pubmed.ncbi.nlm.nih.gov/38678766/) | 2024 | ECA abierto | Seizure | Fenitoína vs. levetiracetam para crisis sintomáticas agudas en niños con síndrome de encefalitis aguda |
| [35976303](https://pubmed.ncbi.nlm.nih.gov/35976303/) | 2022 | Revisión | Arquivos de Neuro-Psiquiatria | Revisión de diagnóstico, monitoreo y tratamiento del estado epiléptico |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad (no hay advertencias, contraindicaciones ni interacciones farmacológicas disponibles en las fuentes consultadas — TFDA/AEMPS y base de DDI no arrojaron resultados).

## Conclusion y Proximos Pasos

**Decisión: Research Question** *(evidencia insuficiente para avanzar; no listo para Go ni justifica bloqueo total tipo Hold)*

**Justificación:**
El mecanismo (modulación SV2A) es teóricamente compatible con la epilepsia visual, pero ninguno de los 9 ensayos ni de las 20 publicaciones evalúa específicamente este subtipo de epilepsia refleja. La evidencia actual es indirecta (extrapolada de poblaciones con HIC, TCE, migraña y epilepsia neonatal), lo que sitúa la predicción en nivel L4.

**Para avanzar se necesita:**
- Estudios clínicos o series de casos específicos de epilepsia fotosensible/visual tratada con levetiracetam
- Datos del prospecto/AEMPS sobre advertencias, contraindicaciones e interacciones (actualmente ausentes)
- Confirmación de mecanismo de acción desde fuente estructurada (DrugBank), dado que el campo original está marcado como data gap

**Nota importante — señal alternativa más fuerte:** Entre las 10 indicaciones evaluadas para levetiracetam en este mismo dossier, **"status epilepticus"** (rank 9, score TxGNN 99.91%) presenta evidencia sustancialmente más sólida: nivel **L1**, con al menos un ECA publicado en *NEJM* (ESETT trial, PMID 31774955) y un ensayo Fase 3 en reclutamiento activo (NCT06907173), con recomendación de decisión **"Proceed with Guardrails"**. Se recomienda priorizar esa vía de investigación por encima de la epilepsia visual, cuya evidencia es puramente mecanística/indirecta.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

