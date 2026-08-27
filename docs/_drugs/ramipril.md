---
layout: default
title: Ramipril
parent: 僅模型預測 (L5)
nav_order: 235
evidence_level: L5
indication_count: 10
---

# Ramipril
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

# RAMIPRIL: De Hipertensión Arterial (IECA) a Hipertensión Pulmonar por Enfermedad Pulmonar y/o Hipoxia

## Resumen en Una Frase

Ramipril es un inhibidor de la enzima convertidora de angiotensina (IECA), clase farmacológica utilizada clásicamente para la hipertensión arterial y la insuficiencia cardíaca (el Evidence Pack no registra licencias ni texto de indicación original en España). El modelo TxGNN predice que podría ser efectivo para **Hipertensión Pulmonar por Enfermedad Pulmonar y/o Hipoxia**, con un puntaje de predicción del **99.93%**, pero actualmente **no hay ensayos clínicos** registrados y las 20 publicaciones disponibles no abordan directamente esta combinación fármaco-indicación, por lo que la evidencia real es mínima.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial (clase IECA); sin licencias ni texto de indicación registrado en España en este dataset |
| Nueva Indicación Predicha | Hipertensión pulmonar por enfermedad pulmonar y/o hipoxia |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de ramipril en este Evidence Pack. Según la información conocida, ramipril pertenece a la clase de los inhibidores de la ECA (IECA), cuya eficacia en hipertensión arterial e insuficiencia cardíaca está ampliamente comprobada, y mecanísticamente podría ser aplicable a la hipertensión pulmonar mediante la modulación del sistema renina-angiotensina-aldosterona (RAAS), que participa en el remodelado vascular pulmonar.

Sin embargo, la relación entre la indicación original y la nueva indicación predicha por TxGNN es, por ahora, puramente teórica. La totalidad de la literatura recuperada trata sobre fisiología de la hipoxia en contextos no relacionados (envejecimiento cerebral, deterioro cognitivo, metabolismo tumoral, migraña, esclerosis múltiple), sin abordar ni a ramipril ni a la hipertensión pulmonar de forma directa. El vínculo mecanístico solo puede inferirse indirectamente a través del papel del RAAS en el remodelado vascular pulmonar, lo que constituye una base de evidencia extremadamente débil.

No existen ensayos clínicos registrados para esta combinación fármaco-indicación, lo que sitúa esta predicción en el nivel de evidencia más bajo (L5): se trata únicamente de una predicción del modelo, sin respaldo de estudios reales.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Revisión | Ageing Research Reviews | Revisa el rol dual de la hipoxia (aguda vs. crónica) en neurodegeneración (Alzheimer, Parkinson) y posibles efectos protectores de la baja oxigenación a gran altitud. |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Revisión | Metabolic Brain Disease | Deterioro cognitivo inducido por hipoxia aguda y crónica, desde evidencia clínica hasta mecanismos moleculares. |
| [37328448](https://pubmed.ncbi.nlm.nih.gov/37328448/) | 2023 | Estudio mecanístico | Advanced Science | La modificación ac4C del ARNm impulsa adicción a la glucólisis en cáncer gástrico vía el eje NAT10/SEPT9/HIF-1α, confiriendo tolerancia a hipoxia y resistencia a terapia antiangiogénica. |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Revisión | Journal of Cellular Biochemistry | La detección de oxígeno regula crecimiento, metabolismo, homeostasis de pH y angiogénesis; la hipoxia contribuye a enfermedad vascular, inflamación y cáncer. |
| [31706510](https://pubmed.ncbi.nlm.nih.gov/31706510/) | 2019 | Revisión | Trends in Cancer | Las desubiquitinasas (DUBs) regulan la abundancia de los factores inducibles por hipoxia (HIF) en cáncer. |
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Revisión | Respiratory Care Clinics of North America | Describe los mecanismos de hipoxemia: baja oxigenación ambiental, hipoventilación, desajuste V/Q y shunt derecha-izquierda. |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Revisión | Clinical Oncology | Modificación terapéutica de la hipoxia tumoral y su impacto en la resistencia a radioterapia e inmunoterapia. |
| [40815459](https://pubmed.ncbi.nlm.nih.gov/40815459/) | 2025 | Revisión/Comentario | Revista Médica del IMSS | Consideraciones sobre la hipoxia hipobárica asociada a la altitud y la aclimatación fisiológica en habitantes de gran altitud. |
| [24557798](https://pubmed.ncbi.nlm.nih.gov/24557798/) | 2014 | Comentario | Journal of Applied Physiology | Nota editorial sobre el estado de la investigación en hipoxia (sin resumen disponible). |
| [40347693](https://pubmed.ncbi.nlm.nih.gov/40347693/) | 2025 | Revisión | Redox Biology | Analiza si la hipoxia es causa o consecuencia de la patología y sintomatología en la esclerosis múltiple. |

**Nota:** ninguna de las publicaciones recuperadas menciona a ramipril ni estudia directamente la hipertensión pulmonar; todas abordan la fisiología general de la hipoxia en otros contextos clínicos.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
A pesar del alto puntaje de predicción de TxGNN (99.93%), no existen ensayos clínicos ni literatura que relacione directamente a ramipril con la hipertensión pulmonar por enfermedad pulmonar y/o hipoxia; el vínculo mecanístico es solo teórico (vía RAAS) y el nivel de evidencia es L5 (predicción sin estudios reales).

**Para avanzar se necesita:**
- Resolver DG001 (bloqueante): obtener advertencias y contraindicaciones del prospecto TFDA/AEMPS antes de cualquier evaluación de seguridad (S1)
- Obtener datos detallados del mecanismo de acción (MOA) de ramipril vía DrugBank (DG002)
- Confirmar indicación original y estado de autorización/comercialización en España
- Estudios preclínicos o clínicos que evalúen específicamente ramipril en hipertensión pulmonar por enfermedad pulmonar/hipoxia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

