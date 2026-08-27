---
layout: default
title: Ranibizumab
parent: 僅模型預測 (L5)
nav_order: 237
evidence_level: L5
indication_count: 10
---

# Ranibizumab
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

Usando conocimiento de dominio en reposicionamiento de fármacos para redactar el informe directamente a partir del Evidence Pack proporcionado (tarea de generación de contenido totalmente especificada por la plantilla, sin necesidad de herramientas adicionales).

Nota metodológica antes del informe: el Evidence Pack incluye 10 indicaciones predichas por TxGNN, pero solo el rank 1 (retinopatía diabética no proliferativa grave) tiene evidencia clínica sólida (L1); las otras 9 son subtipos de catarata y hemorragia neonatal con evidencia L4-L5 y recomendación "Hold" — probablemente asociaciones espurias del modelo (co-ocurrencia con diabetes o coincidencia semántica de palabras clave como "hemorrágica"). Por eso el informe, siguiendo el formato de una indicación principal, se centra en el candidato viable (rank 1) y deja constancia de los demás al final para transparencia.

---

# Ranibizumab: De Degeneración Macular Húmeda / Edema Macular Diabético a Retinopatía Diabética No Proliferativa Grave

## Resumen en Una Frase

Ranibizumab es un fragmento Fab de anticuerpo monoclonal anti-VEGF-A de uso oftalmológico establecido en degeneración macular húmeda (DMAE) y edema macular diabético (EMD).
El modelo TxGNN predice que también podría ser efectivo para retrasar la progresión de la **Retinopatía Diabética No Proliferativa Grave (NPDR grave)**,
con **6 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Degeneración macular húmeda (DMAE) y edema macular diabético (uso oftalmológico establecido; no consta registro de comercialización en España) |
| Nueva Indicación Predicha | Retinopatía diabética no proliferativa grave |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de una ficha estructurada del mecanismo de acción original en la base de datos consultada (DrugBank marca este dato como pendiente de verificación — brecha DG002, severidad alta). No obstante, según el análisis mecanístico disponible en este paquete de evidencia, ranibizumab es un fragmento Fab de anticuerpo monoclonal humanizado dirigido contra el VEGF-A. Administrado mediante inyección intravítrea, neutraliza el VEGF sobreexpresado en el ojo, inhibiendo la neovascularización retiniana y la permeabilidad vascular anómala.

La indicación original (DMAE húmeda y edema macular diabético) y la nueva indicación predicha (NPDR grave) comparten el mismo sustrato fisiopatológico: ambas son enfermedades vasculares retinianas mediadas por VEGF. La NPDR grave es, de hecho, la etapa previa a la retinopatía diabética proliferativa (PDR) y al EMD, por lo que tratar tempranamente con anti-VEGF busca frenar la progresión antes de que aparezcan las complicaciones que ya son indicaciones aprobadas del fármaco.

Esta plausibilidad mecanística no es solo teórica: los propios ensayos RIDE/RISE y estudios equivalentes a Protocol S/Protocol I del DRCR.net ya han establecido esta vía causal (mejora del grado de severidad en la escala DRSS con tratamiento anti-VEGF), lo que refuerza la razonabilidad de la predicción de TxGNN más allá de una simple asociación estadística.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04503551](https://clinicaltrials.gov/study/NCT04503551) | Fase 3 | Completado | 174 | Sistema de liberación port delivery (PDS) con ranibizumab vs. comparador en retinopatía diabética sin edema macular central; evalúa eficacia, seguridad y farmacocinética (evidencia directa, grado A). |
| [NCT02634333](https://clinicaltrials.gov/study/NCT02634333) | Fase 3 | Completado | 399 | Tratamiento anti-VEGF intravítreo para prevenir complicaciones de retinopatía diabética que amenazan la visión en ojos de alto riesgo (grado A). |
| [NCT00444600](https://clinicaltrials.gov/study/NCT00444600) | Fase 3 | Completado | 691 | Compara láser solo, láser+triamcinolona, láser+ranibizumab y ranibizumab solo para edema macular diabético; equivalente al DRCR.net Protocolo I (grado A). |
| [NCT02834663](https://clinicaltrials.gov/study/NCT02834663) | Fase 4 | Completado | 25 | Estudio piloto de ranibizumab intravítreo en NPDR con EMD: retraso/regresión evaluado por cambios en microaneurismas y área no perfundida (grado A). |
| [NCT03452657](https://clinicaltrials.gov/study/NCT03452657) | Fase 3 | Desconocido | 118 | Eficacia y seguridad de ranibizumab intravítreo vs. inyección simulada para prevención de RD de alto riesgo; resultado no confirmado (grado B). |
| [NCT05222633](https://clinicaltrials.gov/study/NCT05222633) | N/A | Desconocido | 1000 | Estudio observacional del mundo real de terapia anti-VEGF en DMAE húmeda, RD proliferativa, edema macular y neovascularización coroidea; población no específica de NPDR (grado C, baja relevancia). |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40048178](https://pubmed.ncbi.nlm.nih.gov/40048178/) | 2025 | ECA | JAMA Ophthalmology | Ensayo Pavilion: sistema PDS con ranibizumab vs. monitorización en NPDR sin edema macular, evaluando reducción de la frecuencia de inyecciones. |
| [36774994](https://pubmed.ncbi.nlm.nih.gov/36774994/) | 2023 | ECA (post-hoc) | Ophthalmology Retina | Metaanálisis de ensayos de Fase 3: tiempo hasta la resolución del EMD según la severidad basal de la retinopatía diabética. |
| [32606578](https://pubmed.ncbi.nlm.nih.gov/32606578/) | 2020 | ECA (post-hoc) | Clinical Ophthalmology | Predictores de regresión temprana de la retinopatía diabética con ranibizumab en los ensayos RIDE/RISE. |
| [35417296](https://pubmed.ncbi.nlm.nih.gov/35417296/) | 2022 | ECA (post-hoc) | Ophthalmic Surgery, Lasers & Imaging Retina | Análisis post-hoc de RIDE/RISE: progresión de la retinopatía diabética en ojos contralaterales no tratados. |
| [39673354](https://pubmed.ncbi.nlm.nih.gov/39673354/) | 2024 | Revisión sistemática | Health Technology Assessment | Revisión sistemática y metaanálisis: fármacos anti-VEGF comparados con fotocoagulación láser para retinopatía diabética. |
| [33966556](https://pubmed.ncbi.nlm.nih.gov/33966556/) | 2021 | Revisión | Expert Opinion on Biological Therapy | Revisión sobre el uso de ranibizumab en el tratamiento de la retinopatía diabética. |
| [31669065](https://pubmed.ncbi.nlm.nih.gov/31669065/) | 2019 | Revisión | Journal of Diabetes and its Complications | Avances en el tratamiento de la retinopatía diabética; papel central del VEGF-A en la enfermedad ocular diabética. |
| [20964459](https://pubmed.ncbi.nlm.nih.gov/20964459/) | 2010 | Revisión | Drugs | Enfoques actuales para el manejo de la retinopatía diabética y el edema macular diabético. |
| [30973596](https://pubmed.ncbi.nlm.nih.gov/30973596/) | 2019 | Cohorte | JAMA Ophthalmology | Características de la no perfusión retiniana mediante angiografía de campo ultra-amplio en NPDR grave y RD proliferativa. |
| [36580154](https://pubmed.ncbi.nlm.nih.gov/36580154/) | 2023 | Cohorte/Biomarcador | International Ophthalmology | Niveles séricos y vítreos de VEGF en retinopatía diabética; comparación tras inyecciones de bevacizumab, ranibizumab y triamcinolona. |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen tres ensayos de Fase 3 completados (NCT00444600, NCT02634333, NCT04503551) más un ensayo Fase 4 completado (NCT02834663), respaldados por el ensayo Pavilion de 2025 (PMID 40048178) diseñado específicamente para NPDR sin EMD, y por análisis post-hoc consistentes de RIDE/RISE. Esto cumple el criterio de nivel L1. Sin embargo, gran parte de la evidencia proviene de estudios centrados en el tratamiento del EMD ya establecido (no en NPDR grave "pura" sin edema), por lo que se recomienda avanzar con salvaguardas antes de una recomendación "Go" plena.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha técnica con advertencias y contraindicaciones (brecha DG001, bloqueante para la evaluación de seguridad S1)
- Completar los datos estructurados del mecanismo de acción vía DrugBank (brecha DG002)
- Dado que el fármaco no consta como comercializado en España (0 autorizaciones), evaluar la vía regulatoria aplicable (extensión de indicación vs. nueva solicitud)
- Diferenciar mejor en los subgrupos de ensayos entre "tratamiento de EMD ya presente" y "prevención de progresión en NPDR grave sin EMD", que es la hipótesis específica de reposicionamiento
- Establecer un plan de monitorización de seguridad e interacciones farmacológicas (no se encontraron datos de DDI en la consulta actual)

---

*Nota sobre otros candidatos evaluados:* TxGNN identificó adicionalmente 9 indicaciones con puntajes de predicción similares (~99.99%), correspondientes en su mayoría a subtipos de catarata (madura, inmadura, cortical, nuclear senil, senil, tetánica, de craneostenosis) y a hemorragia del recién nacido. Ninguna de ellas cuenta con vínculo mecanístico plausible con la vía anti-VEGF, y la evidencia disponible es nula o indirecta (nivel L3-L5), por lo que se recomienda **Hold** para todas y no se incluyen como candidatos activos en este informe.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

