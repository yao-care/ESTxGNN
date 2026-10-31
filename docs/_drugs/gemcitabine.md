---
layout: default
title: Gemcitabine
parent: Solo predicción del modelo (L5)
nav_order: 372
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-31
monitor_inn: "Gemcitabine"
predicted_indications: ["rectum mucinous adenocarcinoma", "colon mucinous adenocarcinoma", "villoglandular endometrial endometrioid adenocarcinoma", "endometrial mixed adenocarcinoma", "endometrial mucinous adenocarcinoma", "cervical mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma", "mucin-rich endometrial endometrioid adenocarcinoma"]
description: "Gemcitabine: nueva indicación predicha, Rectum mucinous adenocarcinoma (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Gemcitabine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Gemcitabine: Rectum mucinous adenocarcinoma
{: .text-alpha }

## Resumen en Una Frase

Gemcitabina es un análogo de nucleósidos citotóxico, originalmente utilizado para el tratamiento del cáncer de ovario (en combinación con carboplatino en la enfermedad recidivante).
El modelo TxGNN (aprendizaje profundo) predice que podría ser efectiva para **adenocarcinoma mucinoso de recto**,
con **39 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección, incluidos ensayos de Fase 3 completados.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Rectum mucinous adenocarcinoma |
| Puntaje de Predicción TxGNN | 0.9977 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 13) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco. Según la información conocida, la gemcitabina es un análogo de nucleósidos que inhibe la síntesis de ADN y actúa sobre la ribonucleótido reductasa (subunidades RRM1 y RRM2, identificadas como dianas farmacológicas). Su eficacia en cáncer de ovario ha sido comprobada, y mecanísticamente puede aplicarse a otros tumores de proliferación rápida.

Este mecanismo citotóxico no es específico de un tipo tumoral, por lo que es coherente que se aplique a las células proliferativas del carcinoma de mama. Además, el cáncer de ovario y el de mama comparten un paradigma de tratamiento basado en combinaciones con platino y taxanos.

Cabe destacar que la combinación de gemcitabina con paclitaxel ya es un régimen establecido para el cáncer de mama metastásico. Por tanto, esta predicción confirma un uso ya existente más que una señal de reposicionamiento nueva. El puntaje muy alto del modelo concuerda con la evidencia clínica.

## Evidencia de Ensayos Clínicos

Se muestran los ensayos más relevantes (de un total de 39 identificados):

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00006459](https://clinicaltrials.gov/study/NCT00006459) | Fase 3 | Completado | No disponible | Gemcitabina + paclitaxel vs paclitaxel en cáncer de mama irresecable, localmente recurrente o metastásico |
| [NCT00093795](https://clinicaltrials.gov/study/NCT00093795) | Fase 3 | Completado | 4894 | Tres regímenes adyuvantes en cáncer de mama con ganglios positivos, uno con gemcitabina añadida a paclitaxel |
| [NCT00408408](https://clinicaltrials.gov/study/NCT00408408) | Fase 3 | Desconocido | 1206 | Neoadyuvancia: capecitabina o gemcitabina añadida a docetaxel antes de AC, con o sin bevacizumab |
| [NCT00070278](https://clinicaltrials.gov/study/NCT00070278) | Fase 3 | Desconocido | 800 | Neoadyuvancia con epirubicina/ciclofosfamida y paclitaxel ± gemcitabina en cáncer de mama precoz de mal pronóstico |
| [NCT00039546](https://clinicaltrials.gov/study/NCT00039546) | Fase 3 | Desconocido | No disponible | Estudio tAnGo: gemcitabina añadida a quimioterapia adyuvante en cáncer de mama precoz ER/PgR-pobre |
| [NCT00006007](https://clinicaltrials.gov/study/NCT00006007) | Fase 2 | Completado | 59 | Pemetrexed + gemcitabina en cáncer de mama metastásico (brazo único) |
| [NCT00110084](https://clinicaltrials.gov/study/NCT00110084) | Fase 2 | Completado | 50 | Nab-paclitaxel + gemcitabina en cáncer de mama metastásico |
| [NCT00003540](https://clinicaltrials.gov/study/NCT00003540) | Fase 2 | Completado | 30 | Gemcitabina en cáncer de mama metastásico previamente tratado con adriamicina y taxol |
| [NCT00244933](https://clinicaltrials.gov/study/NCT00244933) | Fase 2 | Completado | 19 | Gemcitabina + genisteína en cáncer de mama metastásico |
| [NCT07528768](https://clinicaltrials.gov/study/NCT07528768) | Fase 2 | Aún sin reclutar | 750 | Gemcitabina vs paclitaxel en cáncer de mama triple negativo metastásico en mujeres de ascendencia africana |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15685819](https://pubmed.ncbi.nlm.nih.gov/15685819/) | 2004 | Revisión | Oncology (Williston Park) | Gemcitabina y paclitaxel son activos en cáncer de mama metastásico; respuestas objetivas del 52% en ensayos de Fase 2 |
| [15685821](https://pubmed.ncbi.nlm.nih.gov/15685821/) | 2004 | Revisión | Oncology (Williston Park) | Gemcitabina con platino aporta beneficio clínico y tasas de respuesta en cáncer de mama metastásico |
| [15685820](https://pubmed.ncbi.nlm.nih.gov/15685820/) | 2004 | Revisión | Oncology (Williston Park) | Combinación gemcitabina + docetaxel con toxicidades parcialmente no solapadas |
| [14768404](https://pubmed.ncbi.nlm.nih.gov/14768404/) | 2003 | Revisión | Oncology (Williston Park) | Combinaciones de gemcitabina, antraciclinas y taxanos en cáncer de mama avanzado |
| [12138397](https://pubmed.ncbi.nlm.nih.gov/12138397/) | 2002 | Revisión | Seminars in Oncology | Como agente único, respuestas del 16% al 37%; mayores tasas en combinación |
| [14754469](https://pubmed.ncbi.nlm.nih.gov/14754469/) | 2004 | Revisión | Clinical Breast Cancer | Gemcitabina + trastuzumab en cáncer de mama metastásico HER2 positivo |
| [40779028](https://pubmed.ncbi.nlm.nih.gov/40779028/) | 2025 | Estudio clínico (Fase I) | Breast Cancer Research and Treatment | Carboplatino, gemcitabina y mifepristona en cáncer de mama avanzado y ovario recurrente |
| [12057045](https://pubmed.ncbi.nlm.nih.gov/12057045/) | 2002 | Revisión | Clinical Breast Cancer | Gemcitabina neoadyuvante en cáncer de mama con buen perfil de toxicidad |
| [12057039](https://pubmed.ncbi.nlm.nih.gov/12057039/) | 2002 | Preclínico | Clinical Breast Cancer | Estudios en líneas celulares de gemcitabina y trastuzumab en mama y pulmón |
| [38472166](https://pubmed.ncbi.nlm.nih.gov/38472166/) | 2024 | Preclínico | Chemical Biology & Drug Design | El miR-3662 exosomal sérico promueve la resistencia a gemcitabina en células de cáncer de mama |

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones vigentes (todas de fármaco único):

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 73626 | Gemcitabina GP-Pharm 200 mg | Polvo para solución para perfusión | No disponible en los datos |
| 74479 | Gemcitabina Accord 2000 mg | Polvo para solución para perfusión | No disponible en los datos |
| 72981 | Gemcitabina Aurovitas 1000 mg | Concentrado para solución para perfusión | No disponible en los datos |
| 74082 | Gemcitabina Hospira 1000 mg | Concentrado para solución para perfusión | No disponible en los datos |
| 80814 | Gemcitabina Sun 10 mg/ml | Solución para perfusión | No disponible en los datos |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (análogo de nucleósidos / antimetabolito) |
| Riesgo de Mielosupresión | Medio a alto. El grafo de conocimiento asocia contraindicaciones con trombocitopenia, leucopenia y anemia |
| Clasificación de Emetogenicidad | Baja a media (según la categoría general del fármaco) |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos. Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Contraindicaciones / condiciones de riesgo (según el grafo de conocimiento, no texto del prospecto)**: enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, leucopenia, anemia (incluida la macrocítica), enfermedad pulmonar intersticial, síndrome hemolítico urémico (incluido el típico), infecciones y piouréter.
- **Interacciones farmacológicas**: no se identificaron interacciones con otros fármacos. Solo constan las dianas farmacológicas RRM1 y RRM2 (subunidades de la ribonucleótido reductasa).
- Un caso publicado describe retinopatía inducida por gemcitabina (reporte de caso).

Consultar el prospecto para la información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen varios ensayos de Fase 3 completados (como NCT00006459 y NCT00093795) y múltiples ensayos de Fase 2 en cáncer de mama, y la combinación de gemcitabina con paclitaxel ya es un régimen establecido en cáncer de mama metastásico. La evidencia es sólida, pero no constituye un uso nuevo, y faltan datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), un vacío de datos bloqueante para el cribado de seguridad
- Confirmar los datos detallados del mecanismo de acción (MOA) desde DrugBank
- Verificar la indicación de mama en la ficha técnica española, ya que los registros de la AEMPS no incluyen texto de indicación
- Plan de monitoreo hematológico, renal y hepático para poblaciones específicas
- Revisión de resultados publicados de los ensayos de Fase 3 con fecha de inscripción no disponible
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

