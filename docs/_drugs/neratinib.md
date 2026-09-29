---
layout: default
title: Neratinib
parent: Solo predicción del modelo (L5)
nav_order: 377
evidence_level: L5
indication_count: 4
---

# Neratinib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Neratinib: De Cáncer de Mama HER2 Positivo (adyuvancia extendida) a Cáncer de Mama con Receptor de Progesterona Positivo

## Resumen en Una Frase

Neratinib es un inhibidor irreversible de tirosina quinasa de la familia HER (EGFR/HER2/HER4). Según la literatura del Evidence Pack, se usa en cáncer de mama HER2 positivo, incluida la adyuvancia extendida tras trastuzumab. El modelo TxGNN predice que podría ser efectivo para el **cáncer de mama con receptor de progesterona positivo**, con **5 ensayos clínicos** y **10 publicaciones** relacionados. La evidencia directa se limita a la enfermedad HR+/HER2+.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos de AEMPS del pack. Según la literatura: cáncer de mama HER2 positivo (adyuvancia extendida) |
| Nueva Indicación Predicha | Cáncer de mama con receptor de progesterona positivo |
| Puntaje de Predicción TxGNN | 99,68% |
| Nivel de Evidencia | L2 (ver nota) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Proceed with Guardrails |

*Nota sobre el nivel de evidencia: el pack asigna L1, pero ningún ensayo de Fase 3 completado corresponde directamente a esta indicación. Solo se cita un ECA de Fase 3 (ExteNET, en HER2+), por lo que aplicando estrictamente las reglas corresponde L2.*

## ¿Por qué es Razonable esta Predicción?

Neratinib bloquea de forma irreversible las señales de EGFR, HER2 y HER4. En tumores HR+/HER2+, la señalización de HER2 favorece la resistencia a la terapia endocrina. Por eso combinar el bloqueo de HER2 con terapia hormonal es biológicamente coherente. El Evidence Pack no incluye datos detallados de mecanismo de acción de DrugBank; esta explicación procede de la justificación mecanística del propio pack.

Los tumores con receptor de progesterona positivo suelen ser luminales y hormonodependientes. Cuando además son HER2 positivos, se benefician de tratamiento anti-HER2 junto con terapia endocrina. Los ensayos de Fase 2 que combinan neratinib con terapia endocrina, como NCT04886531, ponen a prueba esta interacción.

Existe una salvedad importante. La evidencia directa cubre la enfermedad HR+/HER2+ (uso adyuvante extendido). El uso en tumores HR+ HER2-negativos o HER2-bajos es solo exploratorio, y los dos ensayos en HER2-negativo del pack fueron retirado o terminado con pocos pacientes.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04886531](https://clinicaltrials.gov/study/NCT04886531) | Fase 2 | Reclutando | 30 | Neratinib + inhibidor de aromatasa + trastuzumab preoperatorio (24 semanas) en cáncer ER+/HER2+. Directamente relevante, sin resultados aún |
| [NCT04460430](https://clinicaltrials.gov/study/NCT04460430) | Fase 2 | Terminado | 12 | Neratinib en cáncer avanzado HR+/HER2-negativo de subtipo HER2-enriched. Sin señal de eficacia utilizable |
| [NCT04901299](https://clinicaltrials.gov/study/NCT04901299) | Fase 2 | Retirado | 0 | Fulvestrant + neratinib en HR+/HER2-negativo. Sin pacientes, sin evidencia |
| [NCT05599334](https://clinicaltrials.gov/study/NCT05599334) | N/A (observacional) | Completado | 111 | Estudio retrospectivo de neratinib como adyuvante extendido en cáncer de mama HER2+ precoz (programa de acceso temprano europeo). Contexto de práctica real |
| [NCT06131424](https://clinicaltrials.gov/study/NCT06131424) | N/A (observacional) | Completado | 1151 | Estudio retrospectivo de prevalencia de HER2-bajo y patrones de tratamiento en cáncer de mama metastásico. Solo contexto |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [26874901](https://pubmed.ncbi.nlm.nih.gov/26874901/) | 2016 | ECA (Fase 3) | The Lancet Oncology | ExteNET: 12 meses de neratinib tras adyuvancia con trastuzumab en cáncer de mama HER2+ precoz |
| [27406346](https://pubmed.ncbi.nlm.nih.gov/27406346/) | 2016 | ECA (Fase 2) | N Engl J Med | I-SPY 2: aleatorización adaptativa de neratinib neoadyuvante en cáncer de mama precoz de alto riesgo |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guía | J Clin Oncol | Actualización de la guía ASCO sobre terapia sistémica en cáncer de mama avanzado HER2+ |
| [29784737](https://pubmed.ncbi.nlm.nih.gov/29784737/) | 2018 | Guía | J Natl Compr Canc Netw | Actualización de las guías NCCN: inhibidores de CDK4/6 y duración de la terapia endocrina extendida |
| [33726508](https://pubmed.ncbi.nlm.nih.gov/33726508/) | 2021 | Revisión | Future Oncology | Tendencias en el tratamiento del cáncer de mama HR+/HER2+; combinar terapia hormonal y anti-HER2 sin quimioterapia da control a largo plazo en algunos pacientes |
| [32139271](https://pubmed.ncbi.nlm.nih.gov/32139271/) | 2020 | Revisión | Clinical Breast Cancer | Mesa redonda de expertos sobre el manejo del cáncer de mama HER2+ (incluye neratinib) |
| [24892840](https://pubmed.ncbi.nlm.nih.gov/24892840/) | 2013 | Revisión | Clin Adv Hematol Oncol | Novedades en cáncer de mama metastásico según subtipos inmunohistoquímicos |
| [39153126](https://pubmed.ncbi.nlm.nih.gov/39153126/) | 2024 | Cohorte | Breast Cancer Res Treat | Patrones de uso y tolerancia de neratinib adyuvante en HR+/HER2+. Los efectos gastrointestinales causan a menudo la interrupción |
| [32782013](https://pubmed.ncbi.nlm.nih.gov/32782013/) | 2020 | Cohorte (in silico) | Breast Cancer Res | Las mutaciones ERBB2 accionables se asocian a peor pronóstico en carcinoma lobulillar ER+ sin amplificación de HER2 |
| [35251981](https://pubmed.ncbi.nlm.nih.gov/35251981/) | 2022 | Reporte de caso | Frontiers in Oncology | Piroti­nib + vinorelbina metronómica en cáncer HER2+ con enfermedad leptomeníngea (no es neratinib) |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 1181311001 | NERLYNX 40 MG comprimidos recubiertos con película | Comprimido recubierto con película | Pierre Fabre Medicament |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa pan-HER) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Función hepática y vigilancia de efectos gastrointestinales (la literatura señala que causan a menudo la suspensión del tratamiento). Resto: consultar el prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La predicción es coherente con el mecanismo y con la evidencia en HR+/HER2+, respaldada por el ECA de Fase 3 ExteNET y por ensayos de Fase 2 que combinan neratinib con terapia endocrina. La evidencia no alcanza a HR+/HER2-negativo, donde los ensayos fueron retirados o terminados.

**Para avanzar se necesita:**
- Descargar y analizar la ficha técnica de AEMPS (advertencias y contraindicaciones). Es una brecha bloqueante para el cribado de seguridad.
- Obtener datos de mecanismo de acción desde DrugBank.
- Limitar el uso propuesto a HR+/HER2+ y tratar cualquier uso en HER2-negativo como exploratorio.
- Contar con resultados de NCT04886531 y con un plan de manejo de la toxicidad gastrointestinal.

*Este informe es solo para fines de investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

