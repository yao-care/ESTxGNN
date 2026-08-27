---
layout: default
title: Danazol
parent: 僅模型預測 (L5)
nav_order: 81
evidence_level: L5
indication_count: 10
---

# Danazol
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

# Danazol: De Endometriosis a Amenorrea

## Resumen en Una Frase

Danazol es un esteroide sintético derivado de la 17α-etiniltestosterona, utilizado tradicionalmente en el tratamiento de la endometriosis, la enfermedad fibroquística mamaria y el angioedema hereditario. El modelo TxGNN predice que podría ser efectivo para la **Amenorrea**, con **20 publicaciones** que actualmente respaldan esta dirección, aunque sin ensayos clínicos registrados específicamente para esta indicación.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Endometriosis, enfermedad fibroquística mamaria y angioedema hereditario (según literatura; no hay datos formales de autorización en España) |
| Nueva Indicacion Predicha | Amenorrea |
| Puntaje de Prediccion TxGNN | 99.9995% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos estructurados sobre el mecanismo de acción (MOA) en la fuente regulatoria consultada. Según la literatura recopilada, Danazol es un esteroide sintético derivado de la 17α-etiniltestosterona que actúa inhibiendo la secreción hipotalámico-hipofisaria de gonadotropinas (efecto antigonadotrópico) y uniéndose directamente a receptores androgénicos en el endometrio, suprimiendo la ovulación e induciendo amenorrea.

Esta inducción de amenorrea no es un efecto adverso incidental, sino el mecanismo terapéutico central por el cual Danazol trata sus indicaciones clásicas: en la endometriosis, la supresión de la función ovárica provoca la regresión del tejido endometrial ectópico; en la enfermedad fibroquística mamaria, la reducción de estrógeno circulante disminuye la proliferación del tejido mamario; y en el angioedema hereditario, el efecto androgénico incrementa los niveles de C1-inhibidor. La amenorrea es, por tanto, un desenlace farmacológico directo y ya documentado del fármaco, lo cual explica mecanísticamente por qué el modelo TxGNN la identifica como indicación de alta probabilidad.

Esto se ve reforzado por un estudio de cohorte reciente (2024) sobre el uso de Danazol para supresión menstrual en personas transgénero, que confirma que la inducción de amenorrea es un efecto reproducible y clínicamente aprovechable, más allá de su uso en las indicaciones ya aprobadas.

---

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [2140996](https://pubmed.ncbi.nlm.nih.gov/2140996/) | 1990 | ECA | Fertility and Sterility | Comparación doble ciego de nafarelina vs. danazol (600 mg/día) en endometriosis: ambos indujeron regresión significativa de la enfermedad. |
| [39051650](https://pubmed.ncbi.nlm.nih.gov/39051650/) | 2024 | Cohorte | Women's Health (London) | Estudio multisitio: danazol usado para supresión menstrual induce amenorrea, con efectos androgénicos reversibles asociados. |
| [1533675](https://pubmed.ncbi.nlm.nih.gov/1533675/) | 1992 | Revisión | J Royal Army Medical Corps | Revisión sobre la inducción terapéutica de amenorrea y sus alternativas hormonales, incluyendo agonistas de GnRH. |
| [6819580](https://pubmed.ncbi.nlm.nih.gov/6819580/) | 1982 | Revisión | Progress in Clinical and Biological Research | Danazol suprime la función ovárica y es eficaz en endometriosis e infertilidad asociada. |
| [1807260](https://pubmed.ncbi.nlm.nih.gov/1807260/) | 1991 | Serie de casos | Asian Pac J Allergy Immunol | Danazol en trombocitopenia lúpica: respuesta completa en 4 de 5 pacientes evaluables. |
| [16280355](https://pubmed.ncbi.nlm.nih.gov/16280355/) | 2006 | Revisión | Human Reproduction Update | Las lesiones de endometriosis regresan durante estados de supresión ovárica, como amenorrea o menopausia. |
| [36434439](https://pubmed.ncbi.nlm.nih.gov/36434439/) | 2023 | Revisión sistemática | Archives of Gynecology and Obstetrics | Gestrinona (antiestrógeno relacionado) induce atrofia endometrial y/o amenorrea en el tratamiento de endometriosis. |
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Revisión | Menopause | Revisión de terapias farmacológicas hormonales y no hormonales para el sangrado uterino anormal. |
| [2404115](https://pubmed.ncbi.nlm.nih.gov/2404115/) | 1990 | No clasificado | J Reprod Med | Revisión de los efectos biológicos diversos de danazol: inhibición de gonadotropinas y esteroidogénesis gonadal/adrenal. |
| [2013670](https://pubmed.ncbi.nlm.nih.gov/2013670/) | 1991 | No clasificado | J Allergy Clin Immunol | Seguimiento de 13 años con andrógenos atenuados (danazol/estanozolol) en angioedema hereditario; menstruación irregular como efecto frecuente. |

---

## Informacion de Mercado en España

Danazol no está actualmente comercializado en España (0 autorizaciones registradas en la fuente consultada).

---

## Consideraciones de Seguridad

> Consultar el prospecto para información de seguridad.

---

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
Existen 20 publicaciones que documentan el efecto amenorreico de danazol, incluyendo un estudio de cohorte reciente (2024) sobre su uso deliberado para supresión menstrual, pero ningún ensayo clínico evalúa la amenorrea como indicación primaria. Además, el fármaco no está comercializado en España y existe un vacío de datos (DG001, severidad *Blocking*) que impide completar la evaluación preliminar de seguridad (S1). Con esta combinación de ausencia de vía regulatoria local y bloqueo en seguridad, no se justifica avanzar más allá de la fase de investigación.

**Para avanzar se necesita:**
- Advertencias y contraindicaciones del prospecto (TFDA/AEMPS) — actualmente bloqueante para la evaluación S1
- Mecanismo de acción (MOA) formalmente documentado desde DrugBank
- Evaluación de la vía regulatoria para comercialización en España, dado que actualmente no cuenta con autorización
- Un protocolo de investigación o ensayo clínico prospectivo específico para amenorrea, ya que la evidencia actual es únicamente observacional y de revisión
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

