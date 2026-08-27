---
layout: default
title: Rimegepant
parent: 僅模型預測 (L5)
nav_order: 244
evidence_level: L5
indication_count: 6
---

# Rimegepant
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Rimegepant: De Migraña a Migraña con Aura de Tronco Encefálico

## Resumen en Una Frase

Rimegepant es un antagonista del receptor CGRP (gepant) aprobado internacionalmente para el tratamiento agudo y preventivo de la migraña.
El modelo TxGNN predice que podría ser efectivo para **Migraña con Aura de Tronco Encefálico**,
con **0 ensayos clínicos** dirigidos específicamente a este subtipo y **14 publicaciones** relacionadas con rimegepant en migraña de forma general que respaldan el razonamiento mecanístico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Migraña (tratamiento agudo y preventivo, con o sin aura) |
| Nueva Indicación Predicha | Migraña con Aura de Tronco Encefálico |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Rimegepant es un antagonista de molécula pequeña del receptor CGRP (péptido relacionado con el gen de la calcitonina), perteneciente a la clase de fármacos conocida como "gepants". Ya está aprobado para el tratamiento agudo de la migraña con o sin aura y para la prevención de la migraña episódica en adultos, dado que la vía de señalización CGRP se considera ampliamente uno de los mecanismos patológicos centrales de la migraña.

La migraña con aura de tronco encefálico (antes denominada migraña de tipo basilar) es un subtipo de migraña definido por la clasificación ICHD-3 que, en teoría, comparte la misma vía patológica CGRP que la migraña convencional. Sin embargo, este subtipo ha sido excluido históricamente de los criterios de inclusión de los ensayos clínicos de migraña debido a la preocupación por el efecto vasoconstrictor de los triptanes. Los gepants, a diferencia de los triptanes, no presentan teóricamente este efecto vasoconstrictor, lo que respalda la plausibilidad mecanística de extender su uso a este subtipo. No obstante, actualmente no existe ningún ensayo clínico diseñado específicamente para esta población que confirme de forma directa su seguridad y eficacia, por lo que se trata de una hipótesis mecanísticamente razonable pero con una brecha de evidencia específica de subgrupo.

Cabe señalar que los datos estructurados de DrugBank sobre el mecanismo de acción (MOA) presentan actualmente una brecha de información; la descripción anterior se basa en la literatura disponible sobre la clase farmacológica de los gepants.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados específicamente para migraña con aura de tronco encefálico.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35790906](https://pubmed.ncbi.nlm.nih.gov/35790906/) | 2022 | Metaanálisis en red | J Headache Pain | Comparación de eficacia relativa entre lasmiditan, rimegepant y ubrogepant en tratamiento agudo de migraña, ante ausencia de ensayos comparativos directos |
| [41066271](https://pubmed.ncbi.nlm.nih.gov/41066271/) | 2025 | Ensayo Fase 3 abierto | Cephalalgia | Seguridad y eficacia a largo plazo de rimegepant ODT 75 mg en tratamiento agudo de migraña en adultos chinos |
| [36739335](https://pubmed.ncbi.nlm.nih.gov/36739335/) | 2023 | Revisión | CNS Drugs | Revisión de rimegepant en tratamiento agudo y preventivo de migraña; superioridad frente a placebo en ensayos Fase III pivotales |
| [32270407](https://pubmed.ncbi.nlm.nih.gov/32270407/) | 2020 | Revisión (resumen regulatorio) | Drugs | Resumen de la primera aprobación de rimegepant ODT (Nurtec ODT) por la FDA como tratamiento agudo de migraña |
| [41366286](https://pubmed.ncbi.nlm.nih.gov/41366286/) | 2025 | Ensayo Fase 4 abierto | J Headache Pain | Seguridad y tolerabilidad de dosis diaria de 75 mg de rimegepant durante 24 semanas para prevención de migraña episódica |
| [41652664](https://pubmed.ncbi.nlm.nih.gov/41652664/) | 2026 | Cohorte retrospectiva | Headache | Análisis retrospectivo de tolerabilidad y eficacia del uso off-label de rimegepant en adolescentes con migraña |
| [41133671](https://pubmed.ncbi.nlm.nih.gov/41133671/) | 2026 | Ensayo Fase 1 (PK/seguridad) | Headache | Farmacocinética, seguridad y tolerabilidad de dosis única de rimegepant en niños de 6 a <12 años con migraña |
| [36808268](https://pubmed.ncbi.nlm.nih.gov/36808268/) | 2023 | Ensayo Fase 1 aleatorizado controlado con placebo | Clin Pharmacol Drug Dev | Farmacocinética y seguridad de dosis única y múltiple de rimegepant ODT 75 mg en adultos chinos sanos |
| [33550872](https://pubmed.ncbi.nlm.nih.gov/33550872/) | 2021 | Revisión | Pain Management | Revisión de opciones de tratamiento agudo de migraña, incluyendo rimegepant, lasmiditan y ubrogepant |
| [38307667](https://pubmed.ncbi.nlm.nih.gov/38307667/) | 2024 | Revisión de clase farmacológica | Handb Clin Neurol | Revisión de antagonistas del receptor CGRP (gepants), incluyendo rimegepant y ubrogepant como tratamiento agudo de migraña |

*Nota: las 14 publicaciones recuperadas documentan la eficacia y seguridad de rimegepant en migraña de forma general; ninguna aborda directamente el subtipo "migraña con aura de tronco encefálico".*

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La vía CGRP ofrece una base mecanística sólida y rimegepant ya cuenta con aprobación establecida para la migraña en general (incluyendo con aura), pero no existe ningún ensayo clínico ni caso publicado dirigido específicamente a la migraña con aura de tronco encefálico, y la información de seguridad estructurada (advertencias, contraindicaciones, DDI) presenta una brecha de datos de severidad bloqueante que impide una evaluación de seguridad completa en este momento.

**Para avanzar se necesita:**
- Obtener el prospecto/etiquetado regulatorio de rimegepant (advertencias, contraindicaciones, interacciones farmacológicas) — actualmente bloqueante para la evaluación de seguridad S1
- Datos estructurados de mecanismo de acción (MOA) desde DrugBank para confirmar la vía CGRP formalmente
- Diseño de un estudio piloto u observacional específico en pacientes con migraña con aura de tronco encefálico, dado que este subtipo ha sido históricamente excluido de los ensayos pivotales
- Evaluación de la ausencia de efecto vasoconstrictor de rimegepant en esta población, dada la relevancia clínica de este subtipo
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

