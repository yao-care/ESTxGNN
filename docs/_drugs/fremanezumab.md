---
layout: default
title: Fremanezumab
parent: 僅模型預測 (L5)
nav_order: 128
evidence_level: L5
indication_count: 2
---

# Fremanezumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Fremanezumab: De Prevención de Migraña a Migraña con Aura del Tronco Encefálico

## Resumen en Una Frase

Fremanezumab es un anticuerpo monoclonal humanizado anti-CGRP, utilizado originalmente para la prevención de la migraña episódica y crónica.
El modelo TxGNN predice que podría ser efectivo para **migraña con aura del tronco encefálico**,
con **0 ensayos clínicos** específicos y **20 publicaciones** relacionadas que respaldan parcialmente esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Prevención de migraña episódica y crónica (según literatura asociada; no hay indicación oficial registrada en España, ya que el fármaco no está comercializado) |
| Nueva Indicación Predicha | Migraña con aura del tronco encefálico |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos estructurados de DrugBank sobre el mecanismo de acción (data gap DG002, severidad Alta). Sin embargo, la literatura asociada permite reconstruir el contexto: fremanezumab es un anticuerpo monoclonal humanizado (IgG2Δa) que se une selectivamente al péptido relacionado con el gen de la calcitonina (CGRP), bloqueando su acción en el sistema trigémino-vascular. Su eficacia como tratamiento preventivo de la migraña episódica y crónica está bien establecida en ensayos y estudios de vida real (PMID 37638190, PMID 41539111).

La migraña con aura del tronco encefálico es un subtipo específico (clasificación ICHD-3) en el que el aura se origina en síntomas de tronco encefálico (vértigo, disartria, diplopía, entre otros). La relación con la migraña común es la vía fisiopatológica compartida del CGRP en el sistema trigeminovascular (PMID 30725283), lo que sustenta la hipótesis de TxGNN.

No obstante, la evidencia mecanística disponible es mixta más que confirmatoria: dos estudios preclínicos muestran que fremanezumab **no** modifica la dilatación arterial ni la extravasación de proteína plasmática inducidas por depresión cortical propagada (CSD, el correlato electrofisiológico del aura) (PMID 31127003), aunque sí acorta el período de recuperación cortical (PMID 31895266). Esto sugiere que el efecto del fármaco sobre el aura en sí —a diferencia de su efecto sobre el dolor migrañoso— podría ser limitado o indirecto, lo cual matiza la fortaleza de la predicción.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31127003](https://pubmed.ncbi.nlm.nih.gov/31127003/) | 2019 | Preclínico/Mecanístico | J Neurosci | Fremanezumab no afecta la dilatación arterial ni la extravasación de proteína plasmática inducidas por CSD, cuestionando su efecto directo sobre el aura |
| [31895266](https://pubmed.ncbi.nlm.nih.gov/31895266/) | 2020 | Preclínico/Mecanístico | Pain | Fremanezumab enlentece la propagación y acorta la recuperación cortical, pero no previene la CSD en ratas con barrera hematoencefálica comprometida |
| [35268319](https://pubmed.ncbi.nlm.nih.gov/35268319/) | 2022 | Casos clínicos/Revisión | J Clin Med | Revisión de casos sobre el uso de anti-CGRP mAbs para prevenir el aura migrañosa; evidencia aún escasa |
| [38332541](https://pubmed.ncbi.nlm.nih.gov/38332541/) | 2024 | Serie de casos observacional | CNS Neurosci Ther | Evalúa el efecto de terapias anti-CGRP sobre el aura migrañosa en una serie de casos |
| [41618146](https://pubmed.ncbi.nlm.nih.gov/41618146/) | 2026 | Análisis cuantitativo de pacientes individuales | J Headache Pain | Eficacia y seguridad de anti-CGRP mAbs en migraña hemipléjica, subtipo con aura motora |
| [40264646](https://pubmed.ncbi.nlm.nih.gov/40264646/) | 2025 | Caso clínico y revisión | Front Neurol | Caso de migraña hemipléjica crónica tratada con anti-CGRP mAb, con revisión de literatura |
| [35302681](https://pubmed.ncbi.nlm.nih.gov/35302681/) | 2022 | Cohorte (post-hoc del estudio FOCUS) | Eur J Neurol | Fremanezumab mejora la calidad de vida en subgrupos con y sin aura/disfunción neurológica asociada |
| [30725283](https://pubmed.ncbi.nlm.nih.gov/30725283/) | 2019 | Revisión | Handb Exp Pharmacol | Revisión del rol del CGRP en la fisiopatología de la migraña, incluyendo el aura |
| [37638190](https://pubmed.ncbi.nlm.nih.gov/37638190/) | 2023 | Cohorte prospectiva | Front Neurol | Eficacia y tolerabilidad real-world de fremanezumab en migraña crónica a 3 meses |
| [41539111](https://pubmed.ncbi.nlm.nih.gov/41539111/) | 2026 | Cohorte observacional | J Neurol Sci | Estudio observacional de 12 meses sobre seguridad, eficacia y satisfacción con anti-CGRP mAbs en pacientes japoneses |

---

## Información de Mercado en España

Fremanezumab no está comercializado actualmente en España (0 autorizaciones registradas).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad (datos de advertencias, contraindicaciones e interacciones farmacológicas no disponibles actualmente; ver data gap DG001, severidad Bloqueante).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia disponible es de nivel L4 (solo estudios preclínicos/mecanísticos y series observacionales), sin ningún ensayo clínico dedicado a la migraña con aura del tronco encefálico. Además, la evidencia mecanística directa sobre el aura es mixta —incluso parcialmente negativa respecto al efecto sobre la depresión cortical propagada—, y el fármaco no está actualmente comercializado en España.

**Para avanzar se necesita:**
- Ensayos clínicos dedicados a subtipos de migraña con aura (incluyendo aura de tronco encefálico)
- Datos de ficha técnica/prospecto de la AEMPS sobre advertencias, contraindicaciones e interacciones (data gap DG001, bloqueante)
- Confirmación estructurada del mecanismo de acción vía DrugBank (data gap DG002)
- Evaluación de la vía de administración disponible en caso de futura comercialización en España
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

