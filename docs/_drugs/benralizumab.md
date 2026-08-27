---
layout: default
title: Benralizumab
parent: 僅模型預測 (L5)
nav_order: 37
evidence_level: L5
indication_count: 5
---

# Benralizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Benralizumab: De Asma Eosinofílica Grave a Dermatitis Atópica

## Resumen en Una Frase

Benralizumab es un anticuerpo monoclonal anti-IL-5Rα, cuyo uso clínico establecido internacionalmente es el **asma eosinofílica grave** (no cuenta con autorización de comercialización registrada en España según este informe). El modelo TxGNN predice que podría ser efectivo para **Dermatitis Atópica**, con **6 ensayos clínicos** y **20 publicaciones** identificados, si bien el ensayo pivotal de Fase 2 (HILLIER) no demostró beneficio clínico significativo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Asma eosinofílica grave* (no hay licencias registradas en España en este Evidence Pack) |
| Nueva Indicación Predicha | Dermatitis Atópica |
| Puntaje de Predicción TxGNN | 99.16% |
| Nivel de Evidencia | L2 (ECA Fase 2 completado, con resultado negativo) |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

*\*Inferido del contexto de los ensayos clínicos y la literatura incluidos en este Evidence Pack (p. ej. NCT04126499, revisiones sobre biológicos anti-IL-5); no proviene de `taiwan_regulatory.licenses`, que está vacío.*

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack (`original_moa: [Data Gap]`). Según la información disponible en los ensayos y la literatura recopilados, benralizumab es un anticuerpo monoclonal que se une al receptor alfa de IL-5 (IL-5Rα), expresado principalmente en eosinófilos y basófilos, provocando su depleción mediante citotoxicidad celular dependiente de anticuerpos.

La dermatitis atópica es una enfermedad inflamatoria de tipo 2 en la que, en un subgrupo de pacientes, existe una eosinofilia tisular relevante. Un estudio incluido en este pack (PMID 40781582, 2025) confirma mecanísticamente que benralizumab **sí deplete las células IL-5Rα+ en las lesiones cutáneas** de pacientes con dermatitis atópica, validando el engagement del blanco molecular en la piel.

Sin embargo, esta plausibilidad mecanística no se tradujo en beneficio clínico: el ensayo de Fase 2 HILLIER (NCT04605094), diseñado específicamente para esta indicación, fue **terminado anticipadamente** y sus resultados publicados (PMID 37178404, 38695680) reportan **ausencia de efecto** sobre signos y síntomas de dermatitis atópica moderada-grave. Esto sugiere que, aunque el objetivo molecular se alcanza en piel, los eosinófilos no serían el motor dominante de la inflamación clínica en esta enfermedad, a diferencia del asma eosinofílica.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03563066](https://clinicaltrials.gov/study/NCT03563066) | Fase 2 | Completado | 20 | Estudio de biomarcadores: efecto de benralizumab sobre eosinófilos, basófilos e ILC2 en dermatitis atópica |
| [NCT04605094](https://clinicaltrials.gov/study/NCT04605094) | Fase 2 | Terminado | 194 | Estudio HILLIER: benralizumab vs. placebo en DA moderada-grave; terminado anticipadamente, resultados publicados muestran ausencia de eficacia clínica |
| [NCT04126499](https://clinicaltrials.gov/study/NCT04126499) | N/A | Completado | 28 | Estudio observacional retrospectivo en España, pacientes con asma eosinofílica grave en programa de acceso individualizado a benralizumab (no es DA; aporta contexto de indicación original) |
| [NCT04763447](https://clinicaltrials.gov/study/NCT04763447) | Fase 4 | Reclutando | 234 | Retirada de omalizumab (no benralizumab) en asma alérgica grave controlada; relevancia tangencial |
| [NCT06734884](https://clinicaltrials.gov/study/NCT06734884) | Fase 2 | Aún no reclutando | 96 | Benralizumab en síndrome DRESS (reacción cutánea grave con eosinofilia) — indicación nicho distinta de DA |
| [NCT06477653](https://clinicaltrials.gov/study/NCT06477653) | Fase 2 | Reclutando | 30 | Dupilumab (no benralizumab) como terapia añadida en síndrome hipereosinofílico; relevancia tangencial |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37178404](https://pubmed.ncbi.nlm.nih.gov/37178404/) | 2023 | ECA | J Eur Acad Dermatol Venereol | Resultados del ensayo HILLIER: benralizumab **no mostró eficacia** en signos/síntomas de DA moderada-grave |
| [38695680](https://pubmed.ncbi.nlm.nih.gov/38695680/) | 2024 | ECA (resumen en lenguaje llano) | Immunotherapy | Resumen accesible de los resultados negativos de HILLIER |
| [40781582](https://pubmed.ncbi.nlm.nih.gov/40781582/) | 2025 | Estudio mecanístico | Clin Transl Allergy | Benralizumab deplete células IL-5Rα+ en lesiones cutáneas de DA (validación de blanco, sin dato de eficacia clínica) |
| [36270814](https://pubmed.ncbi.nlm.nih.gov/36270814/) | 2023 | Reporte de caso | Therapie | Dermatitis granulomatosa intersticial **inducida por** benralizumab (señal de seguridad, efecto opuesto al terapéutico) |
| [39600395](https://pubmed.ncbi.nlm.nih.gov/39600395/) | 2024 | Revisión | Allergologie select | Actualización de biológicos en enfermedades atópicas, urticaria y angioedema |
| [34642091](https://pubmed.ncbi.nlm.nih.gov/34642091/) | 2021 | Revisión | Ann Allergy Asthma Immunol | Estrategias de selección de biológicos para alergia/asma, incluye DA |
| [31690400](https://pubmed.ncbi.nlm.nih.gov/31690400/) | 2019 | Revisión | Allergy Asthma Proc | Inmunobiológicos para asma grave, DA y urticaria crónica |
| [33138725](https://pubmed.ncbi.nlm.nih.gov/33138725/) | 2021 | Revisión | Otolaryngol Head Neck Surg | Terapias moleculares dirigidas en alergia y rinología |
| [33717370](https://pubmed.ncbi.nlm.nih.gov/33717370/) | 2020 | Revisión (real-life) | Open Respir Med J | Experiencia real de biológicos en urticaria crónica, asma y DA (EAU) |
| [36355314](https://pubmed.ncbi.nlm.nih.gov/36355314/) | 2023 | Revisión | Dermatol Ther | Combinación de dupilumab con otros anticuerpos monoclonales |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad (no hay datos estructurados de advertencias, contraindicaciones ni DDI en este Evidence Pack).

**Señales adicionales identificadas en la literatura revisada** (no proceden de ficha técnica, se citan por transparencia):
- Reporte de caso de **dermatitis granulomatosa intersticial inducida por benralizumab** (PMID 36270814) — relevante porque es un efecto cutáneo adverso, opuesto al uso terapéutico propuesto.
- Pacientes tratados con benralizumab, dupilumab o mepolizumab mostraron **menor inmunidad post-vacunación frente a SARS-CoV-2** (PMID 38878020).

---

## Otras Indicaciones Predichas (Menor Evidencia)

El Evidence Pack incluye 4 candidatos adicionales, todos sin ensayos clínicos ni literatura de respaldo (evidencia L5, únicamente predicción del modelo):

| Indicación Predicha | Puntaje TxGNN | Evidencia | Recomendación |
|---|---|---|---|
| Trombocitopenia por destrucción inmune | 99.34% | Ninguna | Hold |
| Queloide acneiforme (acne keloidalis) | 99.13% | Ninguna | Hold |
| Dermatomiositis neonatal | 99.05% | Ninguna | Hold |
| Dermatomiositis amiopática | 99.03% | Ninguna | Hold |

En todos estos casos, el mecanismo de benralizumab (IL-5Rα, eosinófilos/basófilos) no tiene una conexión mecanística establecida con la fisiopatología de estas enfermedades; el puntaje elevado probablemente refleja similitud indirecta de nodos en el grafo de conocimiento, no evidencia biológica real.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque benralizumab alcanza su blanco molecular en piel (depleción de células IL-5Rα+ confirmada), el único ensayo de Fase 2 diseñado para dermatitis atópica (HILLIER) fue terminado anticipadamente y **no mostró eficacia clínica**. La plausibilidad mecanística no se sostiene con el desenlace clínico observado, por lo que no se recomienda avanzar hacia S1 en este momento.

**Para avanzar se necesita:**
- Resolver DG001 (advertencias/contraindicaciones de ficha técnica) y DG002 (MOA detallado vía DrugBank), ambos bloqueantes para la evaluación de seguridad S1.
- Confirmar si existe un subgrupo de pacientes con DA de alto perfil eosinofílico que pudiera responder de forma diferenciada (no explorado en HILLIER).
- Seguimiento del ensayo en curso sobre síndrome DRESS (NCT06734884) como posible indicación nicho alternativa, distinta de la DA general.
- Dado que no hay autorización de comercialización en España, confirmar vía de acceso regulatorio (uso compasivo/acceso individualizado) si se decide investigar más.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

