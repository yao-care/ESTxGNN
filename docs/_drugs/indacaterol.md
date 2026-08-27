---
layout: default
title: Indacaterol
parent: 僅模型預測 (L5)
nav_order: 144
evidence_level: L5
indication_count: 10
---

# Indacaterol
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

# Indacaterol: De Broncodilatador en EPOC/Asma a la Validación en Enfermedad Bronquial (Bronchial Disease)

## Resumen en Una Frase

Indacaterol es un agonista β2-adrenérgico de acción ultra-larga (ultra-LABA), utilizado como broncodilatador en el tratamiento de EPOC y asma. De las 10 indicaciones que el modelo TxGNN predice para este fármaco, solo **Enfermedad Bronquial (bronchial disease)** cuenta con respaldo real, con **37 ensayos clínicos** y **20 publicaciones**, incluyendo varios ensayos de Fase 3 completados con miles de pacientes. Las otras 9 predicciones —algunas con puntuación TxGNN incluso más alta— carecen por completo de evidencia clínica o bibliográfica y se consideran señales de bajo valor del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | EPOC / Asma (broncodilatación) — inferido de la evidencia clínica del propio pack; no hay registro formal en DrugBank ni en el prospecto (brecha de datos, ver DG001/DG002) |
| Nueva Indicación Predicha | Enfermedad Bronquial (bronchial disease) |
| Puntaje de Predicción TxGNN | 99.18% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos estructurados sobre el mecanismo de acción (`original_moa` = brecha de datos). Sin embargo, la propia evidencia recopilada es consistente: indacaterol es un agonista β2-adrenérgico de acción ultra-larga (ultra-LABA) que activa los receptores β2 del músculo liso de las vías respiratorias, produciendo broncodilatación. Este es precisamente el mecanismo central del tratamiento de EPOC y asma, y coincide de forma directa —no por analogía— con la indicación predicha "enfermedad bronquial".

La combinación fija QVM149 (indacaterol/glicopirronio/mometasona, comercializada como Enerzair® Breezhaler®) y QMF149 (indacaterol/mometasona, Atectura® Breezhaler®) ya han sido evaluadas en múltiples ensayos de Fase 3 de gran tamaño (NCT02554786, n=2216; NCT02571777, n=3092; NCT03158311, n=1426) y cuentan con estudios de vigilancia poscomercialización activos. Esto significa que, en sentido estricto, esta "predicción" no es un reposicionamiento novedoso, sino la confirmación por parte del modelo de una indicación ya establecida para el fármaco. Se recomienda etiquetarla como **validación de indicación existente**, no como nueva oportunidad de reposicionamiento.

En contraste, las 9 predicciones restantes (nephrogenic syndrome of inappropriate antidiuresis, headache disorder, trigeminal autonomic cephalalgia, paratenonitis, calcific tendinitis, hypertrichosis, myositis, anaphylaxis, Ambras type hypertrichosis) no tienen ningún ensayo clínico ni publicación de respaldo (nivel L5), y sus propios análisis mecanísticos señalan ausencia de vínculo fisiopatológico razonable con el mecanismo β2-agonista. El caso de "headache disorder" es notable: probablemente refleja contaminación de la señal, ya que la cefalea es un efecto adverso frecuente de los β2-agonistas, no una indicación terapéutica.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03158311](https://clinicaltrials.gov/study/NCT03158311) | Fase 3 | Completado | 1426 | QVM149 (triple combinación) no inferior a salmeterol/fluticasona + tiotropio en asma no controlada |
| [NCT02571777](https://clinicaltrials.gov/study/NCT02571777) | Fase 3 | Completado | 3092 | Comparación de dos dosis de QVM149 frente a QMF149 en asma mal controlada, 52 semanas |
| [NCT02554786](https://clinicaltrials.gov/study/NCT02554786) | Fase 3 | Completado | 2216 | Eficacia y seguridad de QMF149 frente a mometasona en asma, 52 semanas |
| [NCT00941798](https://clinicaltrials.gov/study/NCT00941798) | Fase 2 | Completado | 2283 | Seguridad de QMF149 Twisthaler® frente a mometasona en asma persistente, enfoque en exacerbaciones graves |
| [NCT00529529](https://clinicaltrials.gov/study/NCT00529529) | Fase 3 | Completado | 805 | Seguridad de indacaterol (300/600 µg) frente a salmeterol en asma moderada-grave, 26 semanas |
| [NCT05217810](https://clinicaltrials.gov/study/NCT05217810) | N/A | Reclutando | 600 | Vigilancia poscomercialización (rPMS) de Atectura® en condiciones reales, 24 semanas |
| [NCT02892019](https://clinicaltrials.gov/study/NCT02892019) | Fase 2 | Completado | 79 | Efecto sobre función pulmonar de indacaterol acetato en asma pediátrica (6-11 años) |
| [NCT02573155](https://clinicaltrials.gov/study/NCT02573155) | Fase 1 | Completado | 134 | Seguridad, tolerabilidad, PK/PD de AZD8871 inhalado en asma y EPOC |
| [NCT02059434](https://clinicaltrials.gov/study/NCT02059434) | Fase 1 | Completado | 55 | Seguridad y broncodilatación de LAS190792 en asma y EPOC |
| [NCT02953041](https://clinicaltrials.gov/study/NCT02953041) | Fase 4 | Completado | 31 | Efecto de glicopirronio + indacaterol sobre la curva dosis-respuesta a metacolina |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32653074](https://pubmed.ncbi.nlm.nih.gov/32653074/) | 2020 | ECA | Lancet Respir Med | Estudio IRIDIUM: mometasona/indacaterol/glicopirronio superior a mometasona/indacaterol y a fluticasona/salmeterol en asma no controlada |
| [35348408](https://pubmed.ncbi.nlm.nih.gov/35348408/) | 2023 | ECA | J Asthma | Seguridad a largo plazo (52 semanas) de indacaterol/glicopirronio/mometasona en pacientes japoneses con asma |
| [33711782](https://pubmed.ncbi.nlm.nih.gov/33711782/) | 2021 | ECA | Respir Med | Análisis conjunto de seguridad cardiovascular de combinaciones con mometasona/indacaterol en ensayos de Fase 3 |
| [32967685](https://pubmed.ncbi.nlm.nih.gov/32967685/) | 2020 | ECA | Respir Res | Función pulmonar, PK y tolerabilidad de indacaterol maleato y acetato inhalados en asma |
| [31404293](https://pubmed.ncbi.nlm.nih.gov/31404293/) | 2019 | Cohorte | Front Pharmacol | Inflamación eosinofílica e hiperreactividad de vías aéreas como fenotipos de EPOC, utilidad de corticoides inhalados |
| [33871819](https://pubmed.ncbi.nlm.nih.gov/33871819/) | 2021 | Revisión | Drugs | Revisión de indacaterol/glicopirronio/mometasona (Enerzair® Breezhaler®) en asma |
| [31425937](https://pubmed.ncbi.nlm.nih.gov/31425937/) | 2019 | Revisión | Respir Med | Ultra-LABAs (incluye indacaterol) en el tratamiento del asma |
| [34783265](https://pubmed.ncbi.nlm.nih.gov/34783265/) | 2022 | Revisión | Expert Rev Respir Med | Combinación fija inhalada indacaterol/glicopirronio/mometasona en asma moderada-grave |
| [24247039](https://pubmed.ncbi.nlm.nih.gov/24247039/) | 2014 | Revisión | Curr Opin Pulm Med | Broncodilatadores actuales y en desarrollo para enfermedades respiratorias |
| [25364503](https://pubmed.ncbi.nlm.nih.gov/25364503/) | 2014 | Revisión | Multidiscip Respir Med | Maximización de la broncodilatación en EPOC |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se dispone de datos estructurados de advertencias, contraindicaciones ni interacciones farmacológicas en este pack de evidencia (búsqueda de DDI: sin resultados).

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La indicación "enfermedad bronquial" cuenta con nivel de evidencia L1 (múltiples ECA de Fase 3 completados, miles de pacientes) y ya corresponde a combinaciones comercializadas con indacaterol (Enerzair®, Atectura®). No obstante, se trata de una confirmación de uso ya establecido, no de un reposicionamiento nuevo, y el fármaco actualmente no está comercializado en España (0 autorizaciones), por lo que cualquier avance regulatorio requiere guardrails específicos de registro local.

**Para avanzar se necesita:**
- Prospecto/ficha técnica de AEMPS (DG001, bloqueante) para completar la evaluación de seguridad S1
- Datos de mecanismo de acción vía API de DrugBank (DG002)
- Vía de registro/comercialización en España, dado el estado actual "no comercializado"
- Las otras 9 indicaciones predichas (L5, sin evidencia) permanecen en Hold; no se recomienda inversión de recursos salvo que surja evidencia mecanística o clínica independiente
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

