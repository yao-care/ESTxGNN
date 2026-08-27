---
layout: default
title: Canakinumab
parent: 僅模型預測 (L5)
nav_order: 55
evidence_level: L5
indication_count: 10
---

# Canakinumab
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

# Canakinumab: De Enfermedades Autoinflamatorias Mediadas por IL-1β a Nuevas Indicaciones Candidatas

*Evaluación multi-indicación — TW-DB06168-multi*

## Resumen en Una Frase

Canakinumab es un anticuerpo monoclonal anti-IL-1β (nombre comercial Ilaris), cuyo mecanismo ya está validado clínicamente en enfermedades autoinflamatorias como el síndrome periódico asociado a criopirina (CAPS) y la fiebre mediterránea familiar (FMF). El modelo TxGNN generó **10 predicciones** de nuevas indicaciones para este fármaco; de ellas, solo la asociada a **fiebre mediterránea familiar autosómica dominante** cuenta con evidencia clínica sólida (**7 ensayos clínicos, 20 publicaciones**), mientras que la mayoría de las demás candidatas carecen de evidencia real y son probables coincidencias de similitud del modelo (*embedding noise*), según señala el propio análisis de racionalidad incluido en el paquete de evidencia.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Mecanismo de Acción | No disponible como campo estructurado (Data Gap — DG002, severidad High). Las justificaciones mecanísticas del propio paquete de evidencia describen a canakinumab como anticuerpo monoclonal anti-IL-1β |
| Indicaciones Originales Registradas | No disponibles en este paquete de datos |
| Candidata Principal Predicha (mayor score) | Hepatic infarction — 99.86% (evidencia L5, Hold) |
| Candidata con Mejor Evidencia Real | Familial Mediterranean fever, autosomal dominant — 99.41% (evidencia L1, Proceed with Guardrails) |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Vacío de Datos Bloqueante | Advertencias/contraindicaciones del prospecto TFDA no disponibles (DG001, Blocking) — impide evaluación de seguridad S1 |

---

## Comparación de las 10 Candidatas Predichas

| Rango | Enfermedad Predicha | Score TxGNN | Nivel de Evidencia | Etapa | Recomendación |
|---|---|---|---|---|---|
| 1 | Hepatic infarction | 99.86% | L5 | S0 | Hold |
| 2 | Hepatic veno-occlusive disease | 99.82% | L5 | S0 | Hold |
| 3 | Peliosis hepatis | 99.78% | L5 | S0 | Hold |
| 4 | Syndrome with combined immunodeficiency | 99.71% | L4 | S0 | Hold |
| 5 | Periodic fever-infantile enterocolitis-autoinflammatory syndrome | 99.57% | L3 | S2 | Research Question |
| 6 | **Familial Mediterranean fever, autosomal dominant** | 99.41% | **L1** | **S3** | **Proceed with Guardrails** |
| 7 | Extracutaneous mastocytoma | 99.35% | L5 | S0 | Hold |
| 8 | Blau syndrome | 99.34% | L3 | S2 | Research Question |
| 9 | Monosomy X | 99.31% | L5 | S0 | Hold |
| 10 | Liver angiosarcoma | 99.30% | L5 | S0 | Hold |

---

## Por qué son Razonables (o no) estas Predicciones

Actualmente no se dispone de datos estructurados sobre el mecanismo de acción (MOA) de canakinumab en este paquete de evidencia. Sin embargo, las propias justificaciones de reposicionamiento incluidas en los datos describen consistentemente a canakinumab como un **anticuerpo monoclonal anti-IL-1β** cuya acción neutraliza la señalización de esta citocina proinflamatoria.

**Candidatas mecanísticamente coherentes (ranks 5, 6, 8):** Las tres corresponden al espectro de enfermedades autoinflamatorias dependientes de IL-1β — CAPS, fiebre mediterránea familiar (FMF) y síndrome de Blau (mutación NOD2/CARD15 que amplifica la vía IL-1β de forma indirecta). De hecho, el propio análisis señala que la FMF **ya es una indicación aprobada de canakinumab (Ilaris)**, por lo que no se trata de un reposicionamiento novedoso sino de una confirmación del uso ya validado. Los casos de "periodic fever-infantile enterocolitis-autoinflammatory syndrome" y "Blau syndrome" presentan un problema adicional: el nombre de la enfermedad en el paquete de evidencia no corresponde con precisión a las patologías reales cubiertas por la literatura recuperada (CAPS, FMF, PFAPA), por lo que requieren aclaración de mapeo ontológico antes de avanzar.

**Candidatas sin base biológica (ranks 1, 2, 3, 4, 7, 9, 10):** Para infarto hepático, enfermedad veno-oclusiva hepática, peliosis hepatis, mastocitoma extracutáneo, monosomía X y angiosarcoma hepático, el propio paquete de evidencia concluye explícitamente que **no existe relación mecanicista conocida** entre la inhibición de IL-1β y estas patologías, y que la literatura recuperada en varios casos ni siquiera trata sobre canakinumab (p. ej. bempedoic acid, metotrexato). Estas se interpretan como falsos positivos de similitud de embeddings del modelo TxGNN, no como candidatas biológicamente plausibles.

---

## Evidencia Detallada — Candidata Principal: Familial Mediterranean Fever (Rank 6)

### Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---|---|---|---|---|
| [NCT00465985](https://clinicaltrials.gov/study/NCT00465985) | Fase 3 | Completado | 35 | ECA doble ciego, controlado con placebo, diseño de retirada — Síndrome de Muckle-Wells |
| [NCT00685373](https://clinicaltrials.gov/study/NCT00685373) | Fase 3 | Completado | 166 | Seguridad y eficacia a largo plazo en CAPS |
| [NCT01302860](https://clinicaltrials.gov/study/NCT01302860) | Fase 3 | Completado | 17 | Eficacia/seguridad en CAPS en menores de 4 años, incluye vacunación infantil |
| [NCT00991146](https://clinicaltrials.gov/study/NCT00991146) | Fase 3 | Completado | 19 | Eficacia/seguridad en pacientes japoneses con CAPS (24 semanas) |
| [NCT01576367](https://clinicaltrials.gov/study/NCT01576367) | Fase 3 | Completado | 17 | Extensión abierta de seguimiento a largo plazo en CAPS |
| [NCT01242813](https://clinicaltrials.gov/study/NCT01242813) | Fase 2 | Completado | 20 | Tratamiento de 4 meses en TRAPS activo recurrente/crónico |
| [NCT06838143](https://clinicaltrials.gov/study/NCT06838143) | N/A | Reclutando | 25 | Estudio de vida real (REASSURE) en CAPS, crFMF, TRAPS, HIDS/MKD y sJIA |

### Literatura (top 10 de 20)

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|---|---|---|---|---|
| [35874710](https://pubmed.ncbi.nlm.nih.gov/35874710/) | 2022 | Revisión Sistemática | Frontiers in Immunology | Revisión sistemática de seguridad y eficacia de biológicos anti-IL-1 |
| [37769252](https://pubmed.ncbi.nlm.nih.gov/37769252/) | 2024 | Revisión Sistemática/Meta-análisis | Rheumatology (Oxford) | Eficacia y seguridad de anti-IL-1 en FMF resistente/intolerante a colchicina |
| [32806879](https://pubmed.ncbi.nlm.nih.gov/32806879/) | 2020 | Revisión | Turkish J Med Sci | Patogénesis y tratamiento contemporáneo de FMF |
| [29768139](https://pubmed.ncbi.nlm.nih.gov/29768139/) | 2018 | Revisión | NEJM | Canakinumab en síndromes de fiebre autoinflamatoria recurrente |
| [30686512](https://pubmed.ncbi.nlm.nih.gov/30686512/) | 2019 | Revisión | Presse Médicale | Revisión general de FMF |
| [36062765](https://pubmed.ncbi.nlm.nih.gov/36062765/) | 2022 | Revisión | Clin Exp Rheumatol | Inhibición de IL-1 en FMF: resultados clínicos y expectativas |
| [40040547](https://pubmed.ncbi.nlm.nih.gov/40040547/) | 2025 | Cohorte | Int J Rheum Dis | Canakinumab en FMF con/sin colchicina |
| [27286236](https://pubmed.ncbi.nlm.nih.gov/27286236/) | 2016 | Revisión | Curr Opin Rheumatol | Actualización clínica de FMF |
| [34684086](https://pubmed.ncbi.nlm.nih.gov/34684086/) | 2021 | Revisión | Medicina (Kaunas) | Amiloidosis y enfermedad glomerular en FMF |
| [28362189](https://pubmed.ncbi.nlm.nih.gov/28362189/) | 2017 | Revisión | Expert Rev Clin Immunol | Canakinumab para el tratamiento de FMF |

---

## Evidencia — Candidatas de Investigación (Research Question)

### Rank 5: Periodic fever-infantile enterocolitis-autoinflammatory syndrome (L3, S2)

No hay ensayos clínicos registrados bajo este nombre exacto. Literatura relevante (top 10 de 19):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|---|---|---|---|---|
| [35874710](https://pubmed.ncbi.nlm.nih.gov/35874710/) | 2022 | Revisión Sistemática | Frontiers in Immunology | Seguridad/eficacia de biológicos anti-IL-1 |
| [29768139](https://pubmed.ncbi.nlm.nih.gov/29768139/) | 2018 | Revisión | NEJM | Canakinumab en síndromes de fiebre autoinflamatoria recurrente |
| [38268504](https://pubmed.ncbi.nlm.nih.gov/38268504/) | 2024 | Cohorte | Arthritis & Rheumatology | Eficacia/tolerabilidad real de canakinumab en CAPS (Japón) |
| [20065636](https://pubmed.ncbi.nlm.nih.gov/20065636/) | 2010 | Revisión | mAbs | Perfil farmacológico de canakinumab |
| [30175395](https://pubmed.ncbi.nlm.nih.gov/30175395/) | 2018 | Revisión | Curr Treat Options Neurol | CAPS y el sistema nervioso |
| [25438464](https://pubmed.ncbi.nlm.nih.gov/25438464/) | 2014 | Revisión | Israel Med Assoc J | Revisión de CAPS |
| [39334417](https://pubmed.ncbi.nlm.nih.gov/39334417/) | 2024 | Retrospectivo | Pediatr Rheumatol | Eficacia/seguridad de canakinumab en CAPS (China) |
| [38376736](https://pubmed.ncbi.nlm.nih.gov/38376736/) | 2024 | Revisión | Paediatric Drugs | Manejo práctico de enfermedades autoinflamatorias mediadas por IL-1 (CAPS, TRAPS, MKD, DIRA) |
| [30447083](https://pubmed.ncbi.nlm.nih.gov/30447083/) | 2019 | Estudio | Clin Pharmacol Ther | Consideraciones de dosis pediátrica de canakinumab |
| [28454496](https://pubmed.ncbi.nlm.nih.gov/28454496/) | 2017 | Revisión | Expert Rev Clin Immunol | Canakinumab en TRAPS |

**Nota importante:** el nombre de enfermedad predicho por TxGNN no corresponde con precisión a las patologías realmente cubiertas por esta literatura (CAPS, TRAPS, PFAPA), por lo que se requiere aclarar el mapeo terminológico antes de avanzar.

### Rank 8: Blau syndrome (L3, S2)

No hay ensayos clínicos registrados. Literatura disponible (7 de 7):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|---|---|---|---|---|
| [40147219](https://pubmed.ncbi.nlm.nih.gov/40147219/) | 2025 | Revisión Sistemática/Meta-análisis | J Autoimmun | Tratamientos sistémicos para uveítis en Blau syndrome |
| [23124805](https://pubmed.ncbi.nlm.nih.gov/23124805/) | 2013 | Cohorte | Arthritis & Rheumatism | Respuesta clínica/transcripcional a canakinumab en uveítis por Blau syndrome |
| [29110911](https://pubmed.ncbi.nlm.nih.gov/29110911/) | 2018 | Reporte de Caso | Semin Arthritis Rheum | Caso tratado con tocilizumab (no canakinumab) |
| [36186408](https://pubmed.ncbi.nlm.nih.gov/36186408/) | 2022 | Reporte de Caso | JAAD Case Reports | Síndrome de Yao refractario tratado con canakinumab |
| [25182201](https://pubmed.ncbi.nlm.nih.gov/25182201/) | 2014 | Revisión | Autoimmun Rev | Aspectos genéticos/clínicos de Blau syndrome |
| [34947964](https://pubmed.ncbi.nlm.nih.gov/34947964/) | 2021 | Reporte de Casos | Life (Basel) | Edema de disco óptico bilateral en Blau syndrome/CAPS |
| [33269139](https://pubmed.ncbi.nlm.nih.gov/33269139/) | 2020 | Reporte de Caso | Cureus | Caso de Blau syndrome tratado con bloqueo de IL-1β |

**Racionalidad mecanística:** el mecanismo de Blau syndrome (mutación NOD2, vía CARD15/RIP2) amplifica la producción de IL-1β de forma indirecta, por lo que el bloqueo de IL-1β es plausible pero de vínculo menos directo que en CAPS/FMF.

---

## Candidatas sin Evidencia Real (Hold)

Las siguientes 7 candidatas no cuentan con ensayos clínicos ni literatura relevante, o la literatura recuperada no guarda relación real con canakinumab ni con la enfermedad predicha. Se consideran probables coincidencias de similitud del modelo TxGNN, sin fundamento biológico:

- **Hepatic infarction** (99.86%, L5) — única publicación relacionada trata sobre bempedoic acid en prevención cardiovascular; sin conexión con canakinumab.
- **Hepatic veno-occlusive disease** (99.82%, L5) — sin ensayos ni literatura.
- **Peliosis hepatis** (99.78%, L5) — sin ensayos ni literatura.
- **Syndrome with combined immunodeficiency** (99.71%, L4) — única publicación es un caso de CAPS neonatal, sin relación con inmunodeficiencia combinada; además, canakinumab es inmunosupresor, lo que contraindicaría su uso en poblaciones inmunodeficientes.
- **Extracutaneous mastocytoma** (99.35%, L5) — sin ensayos ni literatura.
- **Monosomy X** (99.31%, L5) — literatura recuperada trata sobre metotrexato, reclutamiento de ensayos durante COVID-19 y deficiencia de mevalonato quinasa; ninguna relacionada con canakinumab o síndrome de Turner.
- **Liver angiosarcoma** (99.30%, L5) — sin ensayos ni literatura.

---

## Información de Mercado en España

Canakinumab **no está comercializado** en España según los datos consultados (0 autorizaciones registradas). No hay licencias disponibles para detallar.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. (No hay datos estructurados de advertencias, contraindicaciones ni interacciones disponibles en este paquete de evidencia — vacío de datos bloqueante DG001.)

---

## Conclusión y Próximos Pasos

**Decisión por candidata:**

- **Familial Mediterranean fever (Rank 6): Proceed with Guardrails.** Respaldada por evidencia L1 (múltiples ensayos Fase 2/3 completados) y corresponde a un uso ya validado de canakinumab (Ilaris), no a un reposicionamiento novedoso.
- **Periodic fever syndrome (Rank 5) y Blau syndrome (Rank 8): Research Question.** Mecanismo plausible y literatura de apoyo, pero requieren aclaración del mapeo entre el nombre de enfermedad predicho y las patologías reales antes de asignar un nivel de evidencia definitivo.
- **Las 7 candidatas restantes: Hold.** Sin ensayos clínicos, sin literatura relevante o con literatura no relacionada; se interpretan como ruido del modelo (falsos positivos de similitud de embeddings).

**Justificación general:**
Ninguna candidata puede avanzar a evaluación de seguridad (S1) porque falta el prospecto/ficha técnica con advertencias y contraindicaciones (vacío de datos **Blocking**, DG001).

**Para avanzar se necesita:**
- Obtener las advertencias y contraindicaciones del prospecto (TFDA/EMA) — bloqueante para cualquier candidata.
- Confirmar el mecanismo de acción estructurado de canakinumab (DrugBank API) — vacío de datos de severidad High.
- Aclarar el mapeo terminológico entre "periodic fever-infantile enterocolitis-autoinflammatory syndrome" y las entidades clínicas reales cubiertas por la literatura (CAPS, TRAPS, PFAPA).
- Para las candidatas Hold, no se recomienda inversión adicional salvo que aparezca nueva evidencia real (ensayos clínicos o literatura específica).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

