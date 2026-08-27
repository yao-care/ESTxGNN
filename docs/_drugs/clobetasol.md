---
layout: default
title: Clobetasol
parent: 僅模型預測 (L5)
nav_order: 74
evidence_level: L5
indication_count: 1
---

# Clobetasol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Clobetasol: De Dermatosis Corticosensibles a Linfoma Cutáneo de Células T

## Resumen en Una Frase

Clobetasol propionato es un corticosteroide tópico de clase I (superpotente), tradicionalmente empleado en dermatosis inflamatorias corticosensibles.
El modelo TxGNN predice que podría ser efectivo para **Linfoma Cutáneo Primario de Células T (CTCL/Micosis Fungoide)**,
con **20 publicaciones** que actualmente respaldan esta dirección, aunque sin ensayos clínicos registrados específicamente para esta indicación.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dermatosis corticosensibles (uso tópico establecido de corticosteroides de clase I) |
| Nueva Indicación Predicha | Linfoma Cutáneo Primario de Células T (Micosis Fungoide) |
| Puntaje de Predicción TxGNN | 99.51% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción estructurado. Según la información conocida, clobetasol propionato es un corticosteroide tópico de clase I (superpotente) que actúa uniéndose al receptor glucocorticoide, induciendo apoptosis de linfocitos (incluidos los linfocitos T epidermotrópicos malignos) e inhibiendo la producción local de citoquinas inflamatorias.

La Micosis Fungoide, la variante más común del linfoma cutáneo de células T, es una neoplasia dirigida a la piel donde el infiltrado maligno reside predominantemente en la epidermis y dermis superficial. Este contexto anatómico hace que la terapia dirigida a la piel —incluidos los corticosteroides tópicos superpotentes— sea mecánicamente aplicable, ya que actúa directamente sobre las células neoplásicas epidermotrópicas sin necesidad de exposición sistémica.

De hecho, guías de referencia como NCCN ya incluyen los corticosteroides tópicos como opción de primera línea en estadios tempranos (IA-IIA) de Micosis Fungoide. Por lo tanto, esta predicción de TxGNN corresponde más a una **confirmación de la fuerza de evidencia de una práctica clínica ya establecida** que a una hipótesis mecanística completamente nueva.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32603400](https://pubmed.ncbi.nlm.nih.gov/32603400/) | 2020 | Cohorte (retrospectiva) | Cutis | Estudio observacional sobre el riesgo de efectos adversos cutáneos con clobetasol propionato 0.05% crema en Micosis Fungoide de estadio temprano; confirma alta eficacia con efectos secundarios menores |
| [39741016](https://pubmed.ncbi.nlm.nih.gov/39741016/) | 2025 | Pendiente | Anais brasileiros de dermatologia | Comparación de eficacia entre clobetasol propionato y bexaroteno en Micosis Fungoide de estadio temprano |
| [9722724](https://pubmed.ncbi.nlm.nih.gov/9722724/) | 1998 | Pendiente | Archives of Dermatology | Serie de 79 pacientes evaluando la eficacia de corticosteroides tópicos en el tratamiento de Micosis Fungoide |
| [8987063](https://pubmed.ncbi.nlm.nih.gov/8987063/) | 1996 | Pendiente | Pediatric Dermatology | Terapia pulsátil semanal con corticosteroide tópico superpotente exitosa en tres pacientes pediátricos con papulosis linfomatoide |
| [25027222](https://pubmed.ncbi.nlm.nih.gov/25027222/) | 2014 | Pendiente | Nederlands tijdschrift voor geneeskunde | Niña con Micosis Fungoide hipopigmentada tratada exitosamente con ungüento de clobetasol 0.05% |
| [28031140](https://pubmed.ncbi.nlm.nih.gov/28031140/) | 2016 | Reporte de Caso | Skinmed | Caso de linfoma T angioinmunoblástico con presentación cutánea previamente tratado con crema tópica de clobetasol, empeoramiento tras diagnóstico erróneo de psoriasis |
| [36846176](https://pubmed.ncbi.nlm.nih.gov/36846176/) | 2023 | Pendiente | Clinical Case Reports | Caso de Micosis Fungoide con placas psoriasiformes, inicialmente tratada con esteroides tópicos tras diagnóstico erróneo de psoriasis |
| [39803735](https://pubmed.ncbi.nlm.nih.gov/39803735/) | 2024 | Pendiente | Acta dermatovenerologica Croatica | Evaluación por ultrasonido de alta frecuencia de terapia tópica de primera línea en Micosis Fungoide (contexto de tratamiento dirigido a la piel) |
| [17083888](https://pubmed.ncbi.nlm.nih.gov/17083888/) | 2006 | Revisión | Dermatology Online Journal | Revisión sobre distinción diagnóstica y manejo del linfoma T cutáneo CD30+ de células grandes |
| [30677799](https://pubmed.ncbi.nlm.nih.gov/30677799/) | 2018 | Revisión | Dermatology Online Journal | Papulosis linfomatoide como variante de bajo grado de CTCL; pronóstico favorable a largo plazo |

## Información de Mercado en España

Clobetasol no cuenta con autorizaciones de comercialización registradas en España en el marco de este candidato (estado: no comercializado, 0 autorizaciones).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La evidencia de literatura (incluyendo un estudio de cohorte retrospectivo y una comparación de eficacia) respalda de forma consistente el uso de clobetasol propionato en Micosis Fungoide de estadio temprano, alineado con guías clínicas ya existentes. Sin embargo, la ausencia de ensayos clínicos registrados específicamente para esta indicación y la falta de datos regulatorios en España limitan la solidez de la evidencia a nivel L3.

**Para avanzar se necesita:**
- Datos del prospecto de TFDA/AEMPS sobre advertencias y contraindicaciones (gap bloqueante)
- Datos estructurados sobre el mecanismo de acción (MOA)
- Confirmación de vía de administración y disponibilidad de formulación tópica en España
- Evaluación de ensayos clínicos dedicados a clobetasol en CTCL, más allá de la evidencia observacional actual
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

