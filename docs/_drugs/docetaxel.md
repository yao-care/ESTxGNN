---
layout: default
title: Docetaxel
parent: 僅模型預測 (L5)
nav_order: 94
evidence_level: L5
indication_count: 10
---

# Docetaxel
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

# Docetaxel: De Quimioterapia Citotóxica Establecida a Sarcoma de Ewing Recidivante/Refractario (Régimen GEMDOX)

## Resumen en Una Frase

Docetaxel es un taxano citotóxico que ya se utiliza como quimioterapia estándar en múltiples tumores sólidos (la propia evidencia del pack confirma su uso establecido en cáncer de mama, pulmón, gástrico, próstata y vejiga). El modelo TxGNN generó su predicción de mayor puntuación para **Carcinoma de Mama Femenino** (99.90%), pero el propio análisis mecanístico del pack advierte que esta señal refleja un hecho clínico ya conocido y **no una hipótesis de reposicionamiento genuina**. La señal de reposicionamiento más sólida y clínicamente accionable de este pack corresponde a **Sarcoma de Ewing** (rank 2, score 99.90%), respaldada por **13 ensayos clínicos** y **20 publicaciones**, incluyendo el régimen off-label ya consolidado gemcitabina+docetaxel (GEMDOX).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible como texto regulatorio formal en este informe (0 autorizaciones registradas). Las descripciones de ensayos clínicos del propio pack confirman uso establecido como quimioterapia citotóxica en tumores sólidos (mama, pulmón, gástrico, próstata, vejiga) |
| Nueva Indicación Predicha | Sarcoma de Ewing (Ewing sarcoma) |
| Puntaje de Predicción TxGNN | 99.90% (score 0.9990, rank global 2443) |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

**Nota sobre la señal de mayor puntuación (Carcinoma de Mama):** se excluyó como indicación destacada de este informe porque el propio análisis del pack la identifica como una indicación ya aprobada/establecida, no como una hipótesis nueva de reposicionamiento — el alto score de TxGNN simplemente refleja un hecho clínico ya conocido, no una señal predictiva novedosa.

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción (MOA) de docetaxel en las fuentes estructuradas de este pack (DrugBank marcado como Data Gap). Según la información disponible en la evidencia clínica recogida, docetaxel es un taxano estabilizador de microtúbulos ("紫杉類，微管穩定劑" según el razonamiento mecanístico del propio pack) que inhibe la mitosis; este mecanismo es la base de su uso citotóxico establecido en múltiples tumores sólidos.

El sarcoma de Ewing es un tumor de células pequeñas y redondas con una tasa de proliferación muy alta, biológicamente sensible a agentes que interfieren con la mitosis. La combinación gemcitabina+docetaxel (conocida clínicamente como régimen "GEMDOX") se ha consolidado como una opción off-label madura para sarcoma de Ewing recidivante o refractario, respaldada por múltiples ensayos fase 2 completados a lo largo de casi dos décadas (SARC Study, GEIS-21 del grupo español de sarcomas, entre otros), lo cual da soporte mecanístico y clínico razonable a la predicción de TxGNN, más allá de una simple asociación estadística.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00073983](https://clinicaltrials.gov/study/NCT00073983) | Fase 2 | Completado | 54 | Estudio SARC: gemcitabina secuencial seguida de docetaxel en sarcoma de Ewing recurrente, osteosarcoma o condrosarcoma localmente recurrente/irresecable |
| [NCT03449901](https://clinicaltrials.gov/study/NCT03449901) | Fase 2 | Completado | 98 | ADI-PEG20 + gemcitabina + docetaxel en sarcoma de tejidos blandos, osteosarcoma, sarcoma de Ewing y cáncer de pulmón de células pequeñas, en tumores con deficiencia de ASS1 |
| [NCT02511132](https://clinicaltrials.gov/study/NCT02511132) | Fase 2 | Completado | 22 | Comparación de supervivencia global: inmunoterapia Vigil vs. gemcitabina+docetaxel en sarcoma de Ewing metastásico |
| [NCT01696669](https://clinicaltrials.gov/study/NCT01696669) | Fase 2 | Completado | 43 | Quimioterapia intensiva, cirugía y radioterapia en sarcoma de Ewing en niños y adultos jóvenes (estudio prospectivo multicéntrico) |
| [NCT00014456](https://clinicaltrials.gov/study/NCT00014456) | Fase 1 | Completado | 35 | Escalada de dosis de docetaxel + gemcitabina + filgrastim en tumores sólidos avanzados |
| [NCT00002825](https://clinicaltrials.gov/study/NCT00002825) | Fase 2 | Completado | 20 | Docetaxel en monoterapia en niños con tumores sólidos recurrentes, incluyendo sarcoma de Ewing |
| [NCT06669013](https://clinicaltrials.gov/study/NCT06669013) | Fase 3 | Reclutando | 40 | Dinutuximab beta + quimioterapia de elección del investigador en sarcomas óseos/tejidos blandos GD2+ con progresión tras 1ª línea (incluye Ewing) |
| [NCT05634369](https://clinicaltrials.gov/study/NCT05634369) | Fase 1/2 | Reclutando | 50 | Células NK universales + gemcitabina/docetaxel (GEM/DOX) en sarcomas pediátricos óseos/tejidos blandos recidivantes o refractarios |
| [NCT05999994](https://clinicaltrials.gov/study/NCT05999994) | Fase 2 | Reclutando | 105 | CAMPFIRE: protocolo maestro pediátrico/adultos jóvenes para ensayos oncológicos innovadores, incluye cohortes de sarcoma |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28787430](https://pubmed.ncbi.nlm.nih.gov/28787430/) | 2017 | Fase 2 multicéntrico | British Journal of Cancer | GEIS-21: primer ensayo español de sarcoma de Ewing (niños y adultos), evalúa eficacia de gemcitabina+docetaxel en pacientes de alto riesgo de nuevo diagnóstico |
| [22363068](https://pubmed.ncbi.nlm.nih.gov/22363068/) | 2012 | Fase 2 | The Oncologist | Estudio SARC 003: gemcitabina secuencial seguida de docetaxel en sarcoma de Ewing recurrente, osteosarcoma o condrosarcoma; tasa de respuesta objetiva según RECIST |
| [18521364](https://pubmed.ncbi.nlm.nih.gov/18521364/) | 2003 | Fase 2 | Sarcoma | Docetaxel en monoterapia en tumores de Ewing recidivantes/refractarios: resultados iniciales de ensayo prospectivo fase II (14 pacientes) |
| [18484657](https://pubmed.ncbi.nlm.nih.gov/18484657/) | 2008 | Cohorte | Cancer | Combinación gemcitabina+docetaxel en sarcoma óseo refractario en niños y adultos jóvenes |
| [25164234](https://pubmed.ncbi.nlm.nih.gov/25164234/) | 2014 | Fase 1/2 | BMC Cancer | Docetaxel + irinotecán en niños y adultos jóvenes con sarcoma de Ewing recurrente/refractario |
| [22302783](https://pubmed.ncbi.nlm.nih.gov/22302783/) | 2012 | Retrospectivo | Pediatric Blood & Cancer | GEMDOX (gemcitabina+docetaxel) en sarcomas pediátricos recidivantes/refractarios |
| [19727011](https://pubmed.ncbi.nlm.nih.gov/19727011/) | 2009 | pendiente | Journal of Pediatric Hematology/Oncology | Experiencia con gemcitabina-docetaxel en sarcomas pediátricos recidivantes/refractarios |
| [28221727](https://pubmed.ncbi.nlm.nih.gov/28221727/) | 2017 | pendiente | Pediatric Blood & Cancer | Docetaxel + bevacizumab + gemcitabina en sarcomas de muy alto riesgo en adolescentes y adultos jóvenes |
| [34496122](https://pubmed.ncbi.nlm.nih.gov/34496122/) | 2021 | pendiente | Pediatric Blood & Cancer | Resultados en sarcoma de Ewing recidivante/progresivo en ensayos fase 2 cooperativos (Children's Oncology Group); docetaxel fue el único agente que alcanzó la tasa de respuesta especificada por protocolo |
| [15117993](https://pubmed.ncbi.nlm.nih.gov/15117993/) | 2004 | pendiente | Journal of Clinical Oncology | Evidencia de laboratorio y clínica de citotoxicidad sinérgica con tratamiento secuencial gemcitabina→docetaxel en sarcoma |

---

## Información de Mercado en España

Docetaxel figura como **no comercializado** en los datos regulatorios de este informe, con **0 autorizaciones** registradas y ninguna licencia disponible para extraer forma farmacéutica o indicación aprobada.

---

## Citotoxicidad

**Docetaxel es un fármaco antineoplásico** (taxano citotóxico, confirmado por la propia descripción mecanística y por las múltiples menciones en los ensayos clínicos recogidos en este pack).

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (clase taxano, estabilizador de microtúbulos) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto (dato específico no disponible en este pack) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto (dato específico no disponible en este pack) |
| Items de Monitoreo | Hemograma completo con diferencial, función hepática y renal, previos a cada ciclo |
| Protección en Manejo | Debe seguir las regulaciones estándar de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Existe evidencia clínica real y consolidada (SARC Study, GEIS-21 y múltiples ensayos fase 1/2 a lo largo de casi dos décadas) que respalda el uso off-label de docetaxel en sarcoma de Ewing recidivante/refractario mediante el régimen GEMDOX. Sin embargo, este candidato presenta dos bloqueos operativos críticos señalados en el propio pack: (1) un **data gap de severidad Blocking** sobre advertencias/contraindicaciones del prospecto TFDA/AEMPS, que impide completar la evaluación inicial de seguridad (S1), y (2) el fármaco figura como **no comercializado en España** en este informe (0 autorizaciones). No procede avanzar hasta resolver ambos puntos.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha técnica oficial (AEMPS) con advertencias y contraindicaciones para completar la evaluación de seguridad S1
- Confirmar el estado real de comercialización de docetaxel en España (posible discrepancia con el dato "no comercializado" de este pack, dado que es un citostático de uso muy extendido) y, si aplica, la vía de acceso (medicamento extranjero/uso compasivo)
- Datos de mecanismo de acción (MOA) desde DrugBank para reforzar el análisis de plausibilidad mecanística
- Evaluar si existe un ensayo fase 3 confirmatorio en curso para sarcoma de Ewing que pueda elevar el nivel de evidencia de L2 a L1
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

