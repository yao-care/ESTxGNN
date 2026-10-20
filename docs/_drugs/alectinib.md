---
layout: default
title: Alectinib
parent: Solo predicción del modelo (L5)
nav_order: 31
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Alectinib: nueva indicación predicha, Fibromatosis gingival (nivel de evidencia L5). Indicación original: Cáncer de pulmón no microcítico (según el grafo de conocimiento"
monitor_inn: "ALECTINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "lung germ cell tumor", "pulmonary sulcus neoplasm", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "junctional epidermolysis bullosa"]
---

# Alectinib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

# Alectinib: De Cáncer de Pulmón No Microcítico a Fibromatosis Gingival

## Resumen en Una Frase

Alectinib es un inhibidor selectivo de la quinasa del linfoma anaplásico (ALK), utilizado originalmente para el tratamiento del cáncer de pulmón no microcítico (CPNM).
El modelo TxGNN predice que podría ser efectivo para **fibromatosis gingival**, pero **no existen ensayos clínicos ni publicaciones** que respalden esta predicción; se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de pulmón no microcítico (según el grafo de conocimiento; el texto de indicación de las autorizaciones españolas no está disponible) |
| Nueva Indicación Predicha | Fibromatosis gingival |
| Puntaje de Predicción TxGNN | 99,97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, alectinib es un inhibidor de tirosina quinasa de ALK (con actividad también sobre RET), cuya eficacia en el CPNM con reordenamiento de ALK está bien establecida mediante ensayos de fase 3 (ALEX, J-ALEX, ALINA).

**No se ha identificado un vínculo mecanístico plausible** entre la inhibición de ALK/RET y la fibromatosis gingival. La fibromatosis gingival es una enfermedad de crecimiento fibroso benigno de las encías, sin relación conocida con una vía impulsada por ALK. El puntaje elevado del modelo refleja una predicción computacional basada en el grafo de conocimiento, y no una relación demostrada.

La similitud con la indicación original está pendiente de evaluar. Mientras no existan datos que respalden la hipótesis, esta predicción debe considerarse solo una pregunta de investigación.

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
| 1161169001 | ALECENSA 150 MG CÁPSULAS DURAS | Cápsula dura | No disponible en los datos compilados |
| 1161169001IP | ALECENSA 150 MG CÁPSULAS DURAS | Cápsula dura | No disponible en los datos compilados |

Titular: Roche Registration GmbH. Ambas autorizaciones son de medicamento único y están vigentes.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa ALK) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto (la literatura recuperada describe anemia, generalmente leve, y un caso de anemia hemolítica) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma, función hepática y renal; según la literatura, también perfil lipídico, peso y parámetros cardíacos (ECG) |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 92 interacciones en total. Entre las listadas en los datos compilados:
  - **Mayor**: ácido aminolevulínico.
  - **Moderada**: dolasetrón, naltrexona, edrofonio, fisostigmina, mefloquina, quinina, metoxaleno, acebutolol, ambenonio, asparaginasa (Erwinia chrysanthemi y E. coli), atazanavir, atenolol, bedaquilina, betaxolol y bisoprolol, entre otras.
- **Señales de seguridad en la literatura** (casos clínicos y análisis): pancreatitis por hipertrigliceridemia, anemia hemolítica, síndrome DRESS, eritema multiforme, aumento de peso grave y efectos sobre la electrofisiología cardíaca.

Las advertencias y contraindicaciones del prospecto no están disponibles en los datos compilados; consultar el prospecto de AEMPS para la información completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo computacional (nivel L5), sin ensayos clínicos, sin literatura y sin un vínculo mecanístico plausible entre la inhibición de ALK y la fibromatosis gingival.

**Para avanzar se necesita:**
- Obtener el prospecto de AEMPS (advertencias, contraindicaciones e indicaciones autorizadas) para completar la evaluación de seguridad.
- Completar los datos del mecanismo de acción (por ejemplo, desde DrugBank).
- Investigar si existe alguna base biológica (preclínica) que relacione las vías ALK/RET con la fibromatosis gingival.
- Evaluar si otras indicaciones predichas con evidencia indirecta (por ejemplo, tumores neuroendocrinos con fusión de ALK, predicción n.º 6) merecen priorizarse como pregunta de investigación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

