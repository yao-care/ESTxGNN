---
layout: default
title: Crizotinib
parent: Solo predicción del modelo (L5)
nav_order: 208
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Crizotinib: nueva indicación predicha, Fibromatosis gingival (nivel de evidencia L5). Indicación original: Carcinoma de pulmón no microcítico / cáncer de pulmón (según la base…"
monitor_inn: "CRIZOTINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "lung germ cell tumor", "pulmonary sulcus neoplasm", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "junctional epidermolysis bullosa", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
---

# Crizotinib
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

## Crizotinib: De Cáncer de Pulmón No Microcítico a Fibromatosis Gingival
{: .text-alpha }

## Resumen en Una Frase

Crizotinib es un inhibidor de tirosina quinasa utilizado originalmente para el tratamiento del carcinoma de pulmón no microcítico (CPNM).
El modelo TxGNN predice que podría ser efectivo para **fibromatosis gingival**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Carcinoma de pulmón no microcítico / cáncer de pulmón (según la base de conocimiento del modelo; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Fibromatosis gingival |
| Puntaje de Predicción TxGNN | 0.9981 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 5 de 5) |
| Número de Autorizaciones | 5 (vigentes: 5) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida de la literatura, crizotinib es un inhibidor competitivo de ATP de las tirosina quinasas receptoras ALK, ROS1 y c-MET. Su eficacia en CPNM con reordenamientos de ALK o ROS1 está bien establecida.

Para la fibromatosis gingival, sin embargo, **no se ha identificado un vínculo mecanístico plausible** entre la inhibición de ALK/ROS1/MET y esta enfermedad en los datos disponibles. La puntuación alta del modelo (0.9981) no está acompañada de ensayos, literatura ni una hipótesis biológica respaldada, por lo que debe interpretarse con mucha cautela. Es una señal computacional que requeriría validación preclínica antes de cualquier consideración clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 112793007 | XALKORI 150 MG granulado en cápsulas para abrir | Granulado en cápsulas para abrir | No disponible en los datos compilados |
| 112793003 | XALKORI 250 MG cápsulas duras | Cápsula dura | No disponible en los datos compilados |
| 112793005 | XALKORI 20 MG granulado en cápsulas para abrir | Granulado en cápsulas para abrir | No disponible en los datos compilados |
| 112793001 | XALKORI 200 MG cápsulas duras | Cápsula dura | No disponible en los datos compilados |
| 112793006 | XALKORI 50 MG granulado en cápsulas para abrir | Granulado en cápsulas para abrir | No disponible en los datos compilados |

Todas las autorizaciones pertenecen a Pfizer Europe MA EEIG, son de monofármaco y están vigentes.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa ALK/ROS1/MET), no citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Función hepática (se ha notificado insuficiencia hepática fulminante mortal), ECG/frecuencia cardíaca (bradicardia, prolongación del QT), hemograma |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Las de nivel **mayor** incluidas entre las principales son claritromicina, cisaprida, dolasetrón, eliglustat y granisetrón. Hay además numerosas interacciones de nivel moderado, entre ellas famotidina, metformina, loperamida, bupropión, aprepitant, dexametasona, bisacodilo y budesonida.
- **Señales de seguridad en la literatura**: se han descrito casos de insuficiencia hepática fulminante mortal, toxicidad cardíaca múltiple (bradicardia, prolongación del QT, pericarditis), síndrome del seno enfermo, eritema multiforme y esofagitis erosiva en un paciente pediátrico. Son casos aislados, pero relevantes para cualquier evaluación de reposicionamiento.

No se dispone de datos de advertencias y contraindicaciones del prospecto; consultar el prospecto para esa información.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en la puntuación del modelo (nivel L5), sin ensayos clínicos, sin literatura y sin vínculo mecanístico plausible con la fibromatosis gingival. Además, el perfil de seguridad de crizotinib (hepatotoxicidad, cardiotoxicidad, múltiples interacciones) exige un beneficio claro que hoy no está respaldado.

**Para avanzar se necesita:**
- Una hipótesis mecanística que vincule ALK/ROS1/MET con la fibromatosis gingival, y validación preclínica (modelos celulares o animales)
- Datos del mecanismo de acción del fármaco desde fuentes primarias
- Advertencias y contraindicaciones del prospecto de la AEMPS
- Evaluación de la relación beneficio-riesgo en una enfermedad benigna, dada la toxicidad conocida
- Revisión de otras predicciones mejor respaldadas, como los tumores pulmonares con alteraciones de ALK/ROS1, aunque estas se solapan con la indicación ya aprobada y no constituyen reposicionamiento genuino
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

