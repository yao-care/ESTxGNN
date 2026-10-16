---
layout: default
title: Brigatinib
parent: Solo predicción del modelo (L5)
nav_order: 112
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Brigatinib: nueva indicación predicha, Fibromatosis gingival (nivel de evidencia L5). Indicación original: Cáncer de pulmón no microcítico (según el grafo de conocimiento"
monitor_inn: "BRIGATINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung hilum carcinoma", "lung benign neoplasm", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "pulmonary sulcus neoplasm", "lung germ cell tumor", "junctional epidermolysis bullosa", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
---

# Brigatinib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Brigatinib: De Cáncer de Pulmón No Microcítico a Fibromatosis Gingival

## Resumen en Una Frase

Brigatinib es un inhibidor de la quinasa del linfoma anaplásico (ALK) de nueva generación, utilizado originalmente para el tratamiento del cáncer de pulmón no microcítico (CPNM).
El modelo TxGNN predice que podría ser efectivo para **fibromatosis gingival**, aunque **no existe ningún ensayo clínico ni publicación** que respalde esta predicción; se trata únicamente de una predicción basada en el grafo de conocimiento.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de pulmón no microcítico (según el grafo de conocimiento; el texto de indicación de las autorizaciones españolas no está disponible) |
| Nueva Indicación Predicha | Fibromatosis gingival |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, brigatinib es un inhibidor de tirosina quinasas con actividad establecida frente a ALK, y también frente a EGFR y FAK. Su eficacia en el CPNM con ALK positivo está demostrada en el ensayo de Fase 3 ALTA-1L.

Para la fibromatosis gingival no se ha identificado un vínculo mecanístico plausible. Es un trastorno fibroso benigno de las encías, muy distinto de una neoplasia maligna impulsada por ALK. El puntaje elevado (99.89%) refleja una asociación dentro del grafo, no una evidencia biológica ni clínica.

Por tanto, esta predicción debe considerarse especulativa. Conviene tratarla como una hipótesis que requeriría respaldo preclínico antes de cualquier avance.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1181264008 | ALUNBRIG 90 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 1181264011 | ALUNBRIG 30 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 1181264012 | ALUNBRIG 90 mg + 180 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 1181264010 | ALUNBRIG 180 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |

Titular de todas las autorizaciones: Takeda Pharma A/S.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasas, ALK) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; se muestran 20 de ellas.
  - **Mayores**: aprepitant, dexametasona y claritromicina.
  - **Moderadas** (entre otras): acarbosa, famotidina, ranitidina, rabeprazol, cimetidina, cisaprida, loperamida, morfina, clotrimazol, y antidiabéticos como metformina, pioglitazona, alogliptina, canagliflozina y dapagliflozina.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (nivel L5), sin ensayos ni literatura, y no hay un mecanismo plausible que vincule la inhibición de ALK/EGFR/FAK con la fibromatosis gingival. La evidencia de Fase 3 de brigatinib corresponde al CPNM ya aprobado y no puede atribuirse a esta indicación.

**Para avanzar se necesita:**
- Datos del mecanismo de acción, para evaluar un posible vínculo con la fibrosis gingival
- Estudios preclínicos (modelos celulares o animales de fibrosis gingival)
- Revisión de las advertencias y contraindicaciones del prospecto de la AEMPS
- Evaluación de la relación beneficio-riesgo, dado que se trata de una enfermedad benigna y brigatinib es un antineoplásico con riesgos de seguridad relevantes

---

### Nota sobre otras predicciones

Entre las demás predicciones de mayor puntaje, las siguientes tienen alguna evidencia indirecta, aunque ninguna directa:

- **Neoplasia benigna de pulmón (puntaje 99.85%)**: las 20 publicaciones vinculadas (10 en los datos mostrados) se refieren al CPNM con ALK positivo, ya aprobado, por lo que no respaldan esta indicación. Nivel L5, Hold.
- **Tumor de células germinales de pulmón (99.84%)**: solo hay evidencia indirecta en otros tumores relacionados con ALK, como neuroblastoma, feocromocitoma y carcinoma neuroendocrino de células grandes de pulmón. Nivel L4, "Research Question".
- **Síndrome de leucomelanodermia-infantilismo-discapacidad intelectual-hipodoncia-hipotricosis (99.83%)**: la coincidencia de nombre parece un artefacto del grafo. La literatura vinculada trata sobre la **schwannomatosis relacionada con NF2**, con un informe clínico de 2024 (PMID 38904277) y un estudio preclínico (PMID 34264955). Esta indicación debería evaluarse por separado. Nivel L4, Hold. También consta un caso de síndrome de lisis tumoral mortal (PMID 34987411), que exige cautela.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

