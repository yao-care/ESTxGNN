---
layout: default
title: Imidapril
parent: 僅模型預測 (L5)
nav_order: 142
evidence_level: L5
indication_count: 5
---

# Imidapril
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

Usando el Evidence Pack proporcionado, genero el informe siguiendo el formato indicado (indicación original con datos limitados, se documenta explícitamente en la tabla en lugar de omitirse por completo, ya que el meta del propio pack la marca como brecha de datos):

```markdown
# Imidapril: De Inhibidor de la ECA a Hipertensión Pulmonar por Enfermedad Pulmonar y/o Hipoxia

## Resumen en Una Frase

Imidapril es un inhibidor de la enzima convertidora de angiotensina (IECA), profármaco de imidaprilat, cuya clase terapéutica se emplea habitualmente en el control de la hipertensión arterial mediante el bloqueo del eje renina-angiotensina-aldosterona (RAAS).
El modelo TxGNN predice que podría ser efectivo para **Hipertensión Pulmonar por Enfermedad Pulmonar y/o Hipoxia (Grupo 3)**,
pero esta dirección cuenta únicamente con **20 publicaciones** de biología general de la hipoxia —ninguna sobre imidapril, IECA o tratamiento de hipertensión pulmonar— y **0 ensayos clínicos** que la respalden.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No registrada en los datos regulatorios disponibles (imidapril pertenece a la clase IECA) |
| Nueva Indicación Predicha | Hipertensión Pulmonar por Enfermedad Pulmonar y/o Hipoxia |
| Puntaje de Predicción TxGNN | 99.78% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción específico de imidapril. Según la información recogida en el propio evidence pack, imidapril es un profármaco de imidaprilat perteneciente a la clase de los IECA, cuya eficacia en el control de la hipertensión arterial mediante el bloqueo del RAAS es un efecto de clase bien establecido.

La conexión mecanística con la hipertensión pulmonar por enfermedad pulmonar/hipoxia (Grupo 3) es débil. Las 20 publicaciones asociadas a esta predicción tratan biología general de la hipoxia (envejecimiento cerebral, deterioro cognitivo, metabolismo tumoral, vía HIF-1α), y ninguna aborda imidapril, IECA o el tratamiento de la hipertensión pulmonar; se trata de una asociación de ruido generada por co-ocurrencia de términos ("hipoxia") en la red del modelo, no de una hipótesis mecanística verificable. Además, no existe evidencia de que vasodilatadores sistémicos no selectivos como los IECA sean eficaces en la HP Grupo 3, y teóricamente podrían agravar el desajuste ventilación/perfusión (V/Q) por vasodilatación no selectiva.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

**Nota de relevancia:** las publicaciones listadas abajo son de biología general de la hipoxia; ninguna trata directamente imidapril, IECA ni el tratamiento de la hipertensión pulmonar. Se incluyen por transparencia sobre la base bibliográfica que generó la predicción, no como evidencia de eficacia.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Revisión | Ageing Research Reviews | Hipoxia y envejecimiento cerebral: neurodegeneración vs. neuroprotección |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Revisión | Metabolic Brain Disease | Deterioro cognitivo inducido por hipoxia: mecanismos moleculares |
| [37328448](https://pubmed.ncbi.nlm.nih.gov/37328448/) | 2023 | Investigación Básica | Advanced Science | Adicción a la glucólisis en cáncer gástrico vía eje NAT10/SEPT9/HIF-1α en hipoxia |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Revisión | Journal of Cellular Biochemistry | Control biológico mediado por hipoxia |
| [31706510](https://pubmed.ncbi.nlm.nih.gov/31706510/) | 2019 | Revisión | Trends in Cancer | Deubiquitinasas (DUBs), hipoxia y cáncer |
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Revisión | Respiratory Care Clinics of North America | Mecanismos de la hipoxemia |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Revisión | Clinical Oncology | Modificación terapéutica de la hipoxia tumoral |
| [40815459](https://pubmed.ncbi.nlm.nih.gov/40815459/) | 2025 | Revisión | Revista Médica del IMSS | Consideraciones sobre hipoxia y altitud |
| [24557798](https://pubmed.ncbi.nlm.nih.gov/24557798/) | 2014 | Revisión | Journal of Applied Physiology | Avances en la comprensión de la hipoxia |
| [40347693](https://pubmed.ncbi.nlm.nih.gov/40347693/) | 2025 | Revisión | Redox Biology | Hipoxia en esclerosis múltiple |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación con mayor puntaje (hipertensión pulmonar por enfermedad pulmonar/hipoxia) carece de ensayos clínicos y su literatura de respaldo no aborda imidapril, IECA ni hipertensión pulmonar —es ruido de co-ocurrencia del modelo—. Además, faltan datos críticos de seguridad (ficha técnica de la AEMPS, advertencias, contraindicaciones), lo que bloquea incluso la evaluación inicial de seguridad (S1), y el fármaco no está comercializado en España. Las otras cuatro indicaciones candidatas evaluadas (hipertensión pulmonar Grupo 5, nefropatía hipertensiva maligna, hipertensión renovascular maligna y síndrome de Braddock) presentan el mismo nivel de evidencia L5 sin ensayos ni literatura de respaldo, y una de ellas (hipertensión renovascular maligna) implica más bien un riesgo de seguridad conocido de clase (IECA) que una ventaja terapéutica.

**Para avanzar se necesita:**
- Ficha técnica/prospecto de la AEMPS (advertencias, contraindicaciones, interacciones) — actualmente bloqueante
- Datos de mecanismo de acción (MOA) desde DrugBank u otra fuente farmacológica
- Evidencia clínica específica que relacione IECA/imidapril con hipertensión pulmonar, actualmente inexistente
- Reevaluación de las demás indicaciones candidatas (todas en L5/Hold) antes de continuar el desarrollo
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

