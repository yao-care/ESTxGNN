---
layout: default
title: Lorlatinib
parent: Solo predicción del modelo (L5)
nav_order: 484
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
monitor_inn: "LORLATINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "lung germ cell tumor", "pulmonary sulcus neoplasm", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "junctional epidermolysis bullosa", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
description: "Lorlatinib: nueva indicación predicha, Fibromatosis gingival (fibromatosis, gingival) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Lorlatinib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Lorlatinib: Fibromatosis gingival (fibromatosis, gingival)
{: .text-alpha }

## Resumen en Una Frase

Lorlatinib es un inhibidor de tirosina quinasas (ALK/ROS1) de tercera generación, utilizado originalmente para el tratamiento del cáncer de pulmón no microcítico (CPNM).
El modelo TxGNN predice que podría ser efectivo para **fibromatosis gingival**, pero **no existen ensayos clínicos ni publicaciones** que respalden esta predicción; se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Fibromatosis gingival (fibromatosis, gingival) |
| Puntaje de Predicción TxGNN | 0.9981 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 2 de 2) |
| Número de Autorizaciones | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos compilada. Según la información conocida, lorlatinib es un inhibidor de tirosina quinasas de tercera generación dirigido contra ALK y ROS1, con eficacia comprobada en el CPNM con reordenamientos de ALK, incluida la actividad intracraneal.

Para la fibromatosis gingival no se ha identificado una justificación mecanística. La fibromatosis gingival es un trastorno de proliferación del tejido conectivo de la encía, y no se ha establecido ningún vínculo con las vías de ALK/ROS1. El puntaje alto (0.9981) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no una base biológica demostrada.

Por tanto, esta predicción debe considerarse una hipótesis sin respaldo y no una candidata con apoyo mecanístico o clínico.

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
| 1191355001 | LORVIQUA 25 MG comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |
| 1191355002 | LORVIQUA 100 MG comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |

Ambas autorizaciones corresponden a Pfizer Europe MA EEIG, están vigentes y son de monofármaco.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasas ALK/ROS1) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto. La literatura sobre eventos adversos del fármaco describe alteraciones metabólicas (hipercolesterolemia, hipertrigliceridemia, aumento de peso) y efectos sobre el sistema nervioso central, por lo que se sugiere vigilar el perfil lipídico y la función neurocognitiva |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; entre las principales mostradas:
  - **Mayores**: dexametasona, claritromicina.
  - **Moderadas**: hidrocortisona, betametasona, triamcinolona, aprepitant, bupropión, morfina, cimetidina, alosetrón, dronabinol, eliglustat, naldemedina, naloxegol, y antidiabéticos como dapagliflozina, empagliflozina, saxagliptina, linagliptina, glimepirida y clorpropamida.

Consultar el prospecto para el resto de la información de seguridad (advertencias y contraindicaciones).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para fibromatosis gingival carece de ensayos clínicos, literatura y justificación mecanística; el puntaje del modelo es el único respaldo (nivel L5). No se recomienda avanzar sin una hipótesis biológica fundamentada.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y una hipótesis biológica que vincule ALK/ROS1 con la fibromatosis gingival.
- Revisión de la literatura preclínica sobre vías de proliferación fibroblástica gingival.
- Información de seguridad del prospecto de AEMPS (advertencias y contraindicaciones), actualmente no disponible.
- Evaluación de la compatibilidad de vías de administración (el fármaco es oral sistémico y la enfermedad es localizada).

---

### Nota sobre otras predicciones evaluadas

Entre las otras candidatas, **cáncer de hilio pulmonar** (L4, puntaje 0.9974) es la que cuenta con respaldo más plausible, aunque se trata en gran medida de una extensión de la indicación aprobada de CPNM y se apoya en un único reporte de caso. Para **neoplasia benigna de pulmón** y **tumor de células germinales de pulmón**, la literatura es indirecta (corresponde a CPNM maligno y neuroblastoma, respectivamente) y no debe extrapolarse. El resto carece de evidencia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

