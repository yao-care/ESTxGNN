---
layout: default
title: Ruxolitinib
parent: 僅模型預測 (L5)
nav_order: 250
evidence_level: L5
indication_count: 10
---

# Ruxolitinib
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

# Ruxolitinib: De Mielofibrosis a Síndrome Hemofagocítico Asociado a Infección

## Resumen en Una Frase

Ruxolitinib es un inhibidor de JAK1/JAK2 cuyo uso original conocido es la mielofibrosis y otras neoplasias mieloproliferativas (dato no confirmado en este Evidence Pack por brecha de datos). El modelo TxGNN, junto con evidencia clínica real ya existente, señala como direccion mas solida el **Síndrome Hemofagocítico Asociado a Infección (HLH/MAS)**, con **2 ensayos clínicos** y **20 publicaciones** localizadas, de las cuales 10 aportan evidencia directa (guías de consenso, cohortes y series de casos).

> Nota: este Evidence Pack (`TW-DB08877-multi`) trae 10 indicaciones predichas por TxGNN. Las primeras 4 (PEComa, linfangiomioma, LAM) tienen puntuación TxGNN muy alta pero **cero** evidencia clínica o de literatura (nivel L5, "Hold") y un vínculo mecanístico débil (vía TSC-mTOR, no JAK-STAT). Este informe se centra en la indicación con evidencia real más sólida del conjunto (rank 9).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Mielofibrosis / neoplasias mieloproliferativas (conocimiento general del compuesto; **no disponible en los datos regulatorios de este pack**) |
| Nueva Indicación Predicha | Síndrome hemofagocítico asociado a infección (HLH/MAS) |
| Puntaje de Predicción TxGNN | 99.32% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en este Evidence Pack (brecha de datos DG002, severidad Alta — pendiente de consulta directa a DrugBank). Según la información científica conocida y confirmada indirectamente por la literatura incluida en este pack (p. ej. PMID 34353999, que describe a los inhibidores de JAK como clase terapéutica), Ruxolitinib es un inhibidor de JAK1/JAK2.

El síndrome hemofagocítico (HLH), tanto de origen infeccioso como asociado a neoplasia, tiene como mecanismo central una tormenta de citoquinas impulsada por IFN-γ que activa de forma excesiva la vía JAK-STAT. Al bloquear JAK1/2 de forma directa, Ruxolitinib actúa río arriba de ese eje inflamatorio, lo cual explica por qué ya existe uso clínico real (off-label y en ensayos) en HLH mucho antes de esta predicción del modelo — es decir, TxGNN está recuperando una señal biológica con respaldo clínico preexistente, no solo una asociación estadística del grafo de conocimiento.

Esto contrasta con las indicaciones de PEComa/LAM/linfangiomioma del mismo pack, donde el mecanismo dominante es la vía TSC1/TSC2-mTOR, sin relación directa con JAK-STAT, y sin ningún ensayo o publicación que respalde la predicción.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04424056](https://clinicaltrials.gov/study/NCT04424056) | Fase 3 | Desconocido (no confirmado completado ni resultados publicados) | 216 | Ensayo abierto y aleatorizado que compara Anakinra o Tocilizumab solos vs. en combinación con Ruxolitinib en enfermedad grave por COVID-19 en estadios 2b/3 (con síndrome inflamatorio grave tipo HLH) |
| [NCT07424222](https://clinicaltrials.gov/study/NCT07424222) | Fase 1 | Aún no reclutando | 16 | Estudio piloto de seguridad/eficacia de Ruxolitinib para el síndrome tipo HLH asociado a células efectoras inmunes (IEC-HS) tras terapia CAR-T |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34605776](https://pubmed.ncbi.nlm.nih.gov/34605776/) | 2022 | Guía de Consenso | Critical Care Medicine | Guía de consenso para el reconocimiento, diagnóstico y manejo de HLH en pacientes críticos |
| [35344583](https://pubmed.ncbi.nlm.nih.gov/35344583/) | 2022 | Cohorte (pediátrica, prospectiva) | Blood | Ruxolitinib como tratamiento de primera línea estratificado por respuesta en HLH pediátrica; estudio registrado en ChiCTR |
| [37787838](https://pubmed.ncbi.nlm.nih.gov/37787838/) | 2023 | Cohorte (uso compasivo, n=12) | Annals of Hematology | Sintilimab combinado con Ruxolitinib como terapia compasiva en HLH asociado a VEB en 12 adultos |
| [40665481](https://pubmed.ncbi.nlm.nih.gov/40665481/) | 2025 | Cohorte (pediátrica, retrospectiva comparativa) | British Journal of Haematology | Régimen basado en Ruxolitinib (n=53) vs. quimioterapia HLH-94 ajustada (n=42) en HLH pediátrica asociada a VEB |
| [38691058](https://pubmed.ncbi.nlm.nih.gov/38691058/) | 2024 | Serie de casos | Journal of Pediatric Hematology/Oncology | Emapalumab combinado con Ruxolitinib y dexametasona en HLH asociado a VEB con daño multiorgánico e infección grave |
| [31943120](https://pubmed.ncbi.nlm.nih.gov/31943120/) | 2020 | Revisión | QJM | Revisión sobre HLH del adulto, mortalidad elevada pese a avances diagnósticos y terapéuticos |
| [36533357](https://pubmed.ncbi.nlm.nih.gov/36533357/) | 2022 | Reporte de caso (2 casos) | J Peking Univ Health Sci | Ruxolitinib como tratamiento eficaz en síndrome hemofagocítico asociado a paniculitis |
| [34864445](https://pubmed.ncbi.nlm.nih.gov/34864445/) | 2022 | Reporte de caso | Blood Cells Mol Dis | Caso de síndrome VEXAS con HLH asociado a VEB |
| [38984023](https://pubmed.ncbi.nlm.nih.gov/38984023/) | 2024 | Reporte de caso | Translational Pediatrics | Ruxolitinib como terapia de rescate en HLH refractario asociado a adenovirus post-trasplante haploidéntico |
| [39620213](https://pubmed.ncbi.nlm.nih.gov/39620213/) | 2024 | Reporte de caso | Frontiers in Immunology | HLH durante el embarazo tratado con protocolo HLH-94 e inducción con Ruxolitinib |

---

## Información de Mercado en España

Ruxolitinib no cuenta con autorizaciones registradas en este Evidence Pack (`market_status: 未上市`, 0 autorizaciones). No es posible construir la tabla de comercialización con los datos disponibles.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Este Evidence Pack no contiene advertencias, contraindicaciones ni datos de interacciones farmacológicas verificados (consulta a base DDI sin resultados; obtención del prospecto TFDA marcada como brecha bloqueante, DG001).

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El vínculo mecanístico entre inhibición de JAK1/2 y la tormenta de citoquinas del HLH es sólido y ya cuenta con uso clínico real documentado (múltiples cohortes, series de casos y una guía de consenso), pero ningún ensayo controlado de Fase 2/3 ha completado reclutamiento ni publicado resultados confirmatorios — el ensayo Fase 3 más relevante (NCT04424056) tiene estado desconocido.

**Para avanzar se necesita:**
- Resolver las brechas de datos bloqueantes: ficha técnica/advertencias de TFDA (DG001) y mecanismo de acción confirmado vía DrugBank (DG002)
- Seguimiento del resultado final de NCT04424056 y avance del reclutamiento de NCT07424222
- Datos de interacciones farmacológicas (DDI), actualmente sin registros
- Evaluar por separado la indicación relacionada "HLH asociado a neoplasia maligna" (rank 10, nivel L3), que comparte mecanismo pero carece de ensayos propios
- Las demás indicaciones predichas de este pack (PEComa, linfangiomioma, LAM, tumor rabdoide) permanecen en Hold por ausencia total de evidencia clínica/literatura y mecanismo biológico no coincidente (vía mTOR, no JAK-STAT)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

