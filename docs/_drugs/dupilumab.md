---
layout: default
title: Dupilumab
parent: 僅模型預測 (L5)
nav_order: 97
evidence_level: L5
indication_count: 10
---

# Dupilumab
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

# Dupilumab: De Dermatitis Atópica a Bronquitis

## Resumen en Una Frase

Dupilumab (Dupixent) es un anticuerpo monoclonal anti-IL-4Rα cuya indicación principal aprobada es la dermatitis atópica moderada-severa (y también el asma no controlada, según la literatura recopilada). El modelo TxGNN predice que podría ser efectivo para **Bronquitis**, pero actualmente esta dirección solo cuenta con **1 ensayo clínico** (que no evalúa bronquitis de forma directa) y **6 publicaciones**, en su mayoría centradas en asma, EPOC y rinosinusitis crónica.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dermatitis atópica (indicación aprobada de Dupixent, según el propio Evidence Pack); también asma, documentada en la literatura recopilada |
| Nueva Indicación Predicha | Bronquitis (Bronchitis) |
| Puntaje de Predicción TxGNN | 99.92% (rank #2028) |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold (etapa de Pregunta de Investigación) |

---

## Por qué es Razonable esta Predicción?

No se dispone de datos estructurados del mecanismo de acción (MOA) procedentes de DrugBank para este fármaco (dato faltante clasificado como severidad Alta en el propio Evidence Pack). No obstante, la evidencia clínica y bibliográfica recopilada indica de forma consistente que dupilumab es un anticuerpo monoclonal que bloquea la subunidad IL-4Rα, inhibiendo la señalización de IL-4 e IL-13, citoquinas centrales de la inflamación tipo 2 (Th2). Esta vía es la base mecanística de su indicación aprobada en dermatitis atópica y ha sido ampliamente validada también en asma no controlada de perfil eosinofílico (extensión TRAVERSE, metaanálisis de Zayed et al. 2019).

La bronquitis, especialmente en sus fenotipos eosinofílicos (bronquitis eosinofílica, componente bronquítico del EPOC/asma con endotipo Th2, y la bronquitis plástica eosinofílica pediátrica), comparte el mismo sustrato inflamatorio de vía aérea mediado por IL-4/IL-13. Mecánicamente, el bloqueo de esta vía podría en teoría reducir la inflamación eosinofílica también en bronquitis.

Sin embargo, la evidencia directa es limitada: el único ensayo clínico disponible evalúa rinosinusitis crónica sin pólipos nasales (CRSsNP), no bronquitis, y solo una revisión (sobre bronquitis plástica eosinofílica pediátrica) menciona la enfermedad por su nombre. El resto de la literatura se centra en asma, EPOC y enfermedades de vía aérea relacionadas pero distintas, por lo que la señal de TxGNN debe interpretarse como una hipótesis mecanística respaldada indirectamente, no como evidencia clínica directa de eficacia en bronquitis.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04362501](https://clinicaltrials.gov/study/NCT04362501) | Fase 2 | Completado | 33 | Estudio aleatorizado, doble ciego, controlado con placebo, evaluando dupilumab en rinosinusitis crónica sin pólipos nasales (CRSsNP). No evalúa bronquitis directamente; comparte con esta solo el mecanismo de inflamación Th2 de vía aérea superior (grado de relevancia: C). |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30273510](https://pubmed.ncbi.nlm.nih.gov/30273510/) | 2019 | Revisión Sistemática/Metaanálisis | The Journal of Asthma | Metaanálisis de RCTs que evalúa eficacia y seguridad de dupilumab en asma no controlada frente a placebo. |
| [38488768](https://pubmed.ncbi.nlm.nih.gov/38488768/) | 2024 | Revisión | Pediatric Pulmonology | Terapias novedosas para bronquitis plástica eosinofílica pediátrica; única publicación que coincide directamente con el nombre de la enfermedad "bronquitis". |
| [34597534](https://pubmed.ncbi.nlm.nih.gov/34597534/) | 2022 | Extensión Abierta (TRAVERSE) | The Lancet Respiratory Medicine | Seguridad y eficacia a largo plazo de dupilumab en asma moderada-severa, más allá de 1 año de tratamiento. |
| [39904363](https://pubmed.ncbi.nlm.nih.gov/39904363/) | 2025 | Revisión | Tuberculosis and Respiratory Diseases | Revisión de terapias farmacológicas para prevenir exacerbaciones de EPOC, incluyendo agentes biológicos tipo dupilumab. |
| [32428511](https://pubmed.ncbi.nlm.nih.gov/32428511/) | 2020 | Cohorte | Chest | Efectos del tratamiento anti-T2 (dupilumab) sobre la ventilación pulmonar evaluada por RMN en asma dependiente de prednisona. |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Revisión | Expert Opinion on Pharmacotherapy | Desafíos en el manejo del asma asociada a enfermedades de vía aérea inducidas por tabaquismo, incluyendo bronquitis crónica. |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. El Evidence Pack no contiene datos de advertencias, contraindicaciones ni interacciones farmacológicas (DDI) para dupilumab; la obtención del prospecto TFDA está identificada como brecha de datos **bloqueante** (DG001) para avanzar a la evaluación de seguridad S1.

---

## Conclusión y Próximos Pasos

**Decisión: Hold (Pregunta de Investigación)**

**Justificación:**
- La evidencia directa sobre "bronquitis" es escasa: un único ensayo clínico que en realidad evalúa CRSsNP, y una sola revisión que nombra la enfermedad directamente (bronquitis plástica eosinofílica pediátrica). El resto de la evidencia procede de asma, EPOC y CRSsNP — patologías relacionadas por mecanismo Th2 pero clínicamente distintas.
- Nota de contexto: este Evidence Pack contiene 10 indicaciones candidatas para dupilumab. La dermatitis (rank 2) corresponde a la indicación ya aprobada (Dupixent), no a una hipótesis nueva. Las 8 indicaciones restantes (acné queloide, exantema, dermatomiositis neonatal, etc.) tienen evidencia nula o contradictoria (nivel L4–L5) y están clasificadas como Hold.

**Para avanzar se necesita:**
- Prospecto TFDA con advertencias y contraindicaciones (DG001, bloqueante)
- Datos estructurados del mecanismo de acción vía DrugBank (DG002)
- Ensayos clínicos diseñados específicamente para "bronquitis" (no solo asma/EPOC/CRSsNP)
- Confirmación del estatus regulatorio en España, dado que actualmente no hay licencias registradas (0 autorizaciones, no comercializado)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

