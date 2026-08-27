---
layout: default
title: Interferon Gamma-1B
parent: 僅模型預測 (L5)
nav_order: 149
evidence_level: L5
indication_count: 10
---

# Interferon Gamma-1B
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

# Interferon Gamma-1b: De Enfermedad Granulomatosa Crónica a Cardiopatía (Heart Disease)

## Resumen en Una Frase

Interferon gamma-1b es una citoquina inmunomoduladora, aprobada originalmente para la enfermedad granulomatosa crónica y la osteopetrosis maligna grave. El modelo TxGNN predice que podría ser efectivo para **Heart Disease (Cardiopatía)**, con una puntuación del **99.99%**, pero el análisis de los **50 ensayos clínicos** y **5 publicaciones** asociados a esta predicción muestra que ninguno evalúa realmente el fármaco como tratamiento de cardiopatía: la señal parece derivar de una cercanía indirecta con el concepto de "inflamación" en el grafo de conocimiento.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad granulomatosa crónica (CGD) / osteopetrosis maligna grave (según mecanismo conocido; sin confirmación por licencias AEMPS) |
| Nueva Indicación Predicha | Heart Disease (Cardiopatía) |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción (MOA) verificados para este informe (dato pendiente de consulta en DrugBank). Según la información contextual disponible en el evidence pack, interferon gamma-1b actúa potenciando la función oxidativa bactericida de los fagocitos (mecanismo relevante en CGD) y participa en la regulación de la densidad ósea (relevante en osteopetrosis maligna grave).

La cardiopatía no comparte una vía fisiopatológica establecida con estas dos indicaciones aprobadas. Al revisar los ensayos y la literatura recuperados para esta predicción, la mayoría corresponde a comorbilidades o complicaciones cardíacas en pacientes con la enfermedad de base del fármaco —por ejemplo, un caso de pericarditis constrictiva por Aspergillus en una niña con CGD, o un caso de endocarditis protésica tras cirugía cardíaca— y no a ensayos que evalúen el fármaco como tratamiento de la cardiopatía en sí.

La puntuación alta de TxGNN (99.99%) probablemente refleja una cercanía indirecta en el grafo de conocimiento a través de nodos relacionados con "inflamación" o "sistema inmune", más que una señal causal real. Por este motivo, el nivel de evidencia se clasifica como L5 (predicción de modelo sin respaldo clínico directo).

## Evidencia de Ensayos Clínicos

De los 50 ensayos recuperados para "heart disease", los 10 evaluados explícitamente por el equipo revisor fueron todos calificados como grado C (no relacionados / ruido de grafo de conocimiento):

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03652519](https://clinicaltrials.gov/study/NCT03652519) | NA | Completado | 72 | Ejercicio aeróbico en esclerosis múltiple; no evalúa IFN-gamma-1b, comparte solo el concepto de "inflamación" |
| [NCT04356248](https://clinicaltrials.gov/study/NCT04356248) | NA | Completado | 106 | Entrenamiento de alta intensidad vs. estándar en esclerosis múltiple; sin relación con el fármaco |
| [NCT03672812](https://clinicaltrials.gov/study/NCT03672812) | Fase 3 | Completado | 50 | Evalúa liraglutide en donantes con muerte cerebral, no IFN-gamma-1b |
| [NCT07099911](https://clinicaltrials.gov/study/NCT07099911) | NA | Reclutando | 20 | Estimulación neuromuscular para control de glucosa en lesión medular; sin relación con el fármaco ni con cardiopatía |
| [NCT05650333](https://clinicaltrials.gov/study/NCT05650333) | Fase 1 | Completado | 15 | Estudio PK/PD de ritlecitinib en alopecia areata pediátrica; fármaco distinto |
| [NCT05027958](https://clinicaltrials.gov/study/NCT05027958) | Fase temprana 1 | Completado | 17 | Respuesta inmune pulmonar a antígenos micobacterianos; no evalúa eficacia en cardiopatía |
| [NCT02489383](https://clinicaltrials.gov/study/NCT02489383) | NA | Desconocido | 60 | Entrenamiento aeróbico continuo vs. interválico en asma; sin relación con el fármaco |
| [NCT00974142](https://clinicaltrials.gov/study/NCT00974142) | Fase 1/2 | Completado | 43 | Ciclosporina oral en EPOC avanzada; fármaco distinto al evaluado |
| [NCT03904277](https://clinicaltrials.gov/study/NCT03904277) | N/A | Completado | 28 | Estudio sobre tamaño del foramen oval permeable; no es ensayo de intervención farmacológica |
| [NCT02799095](https://clinicaltrials.gov/study/NCT02799095) | Fase 1/2 | Completado | 243 | ALKS 4230 en tumores sólidos avanzados; fármaco distinto |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37180421](https://pubmed.ncbi.nlm.nih.gov/37180421/) | 2022 | Revisión | Therapeutic advances in rare disease | Revisión sistemática de intervenciones en ataxia de Friedreich; no evalúa cardiopatía |
| [31020218](https://pubmed.ncbi.nlm.nih.gov/31020218/) | 2018 | Reporte de caso | European heart journal. Case reports | Endocarditis infecciosa protésica por Mycobacterium chimaera tras cirugía cardíaca; no evalúa el fármaco |
| [29456196](https://pubmed.ncbi.nlm.nih.gov/29456196/) | 2018 | Reporte de caso | Journal of cystic fibrosis | Mejora respiratoria con interferón-gamma en fibrosis quística con infección fúngica; no relacionado con cardiopatía |
| [21131468](https://pubmed.ncbi.nlm.nih.gov/21131468/) | 2011 | Validación metodológica | Am J Respir Crit Care Med | Validación del test de caminata de 6 minutos en fibrosis pulmonar idiopática; no evalúa el fármaco directamente |
| [28990950](https://pubmed.ncbi.nlm.nih.gov/28990950/) | 2017 | Reporte de caso | Turk Kardiyoloji Dernegi Arsivi | Niña con enfermedad granulomatosa crónica que desarrolló pericarditis constrictiva por Aspergillus; complicación de la enfermedad de base, no evidencia de eficacia en cardiopatía |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad (no hay advertencias, contraindicaciones ni interacciones registradas en las fuentes consultadas).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- La puntuación TxGNN del 99.99% no está respaldada por evidencia clínica real: los ensayos y publicaciones recuperados corresponden a comorbilidades o complicaciones cardíacas de las enfermedades ya aprobadas para el fármaco (CGD, fibrosis pulmonar/quística), no a tratamiento de cardiopatía en sí.
- Faltan datos críticos que bloquean incluso la evaluación de seguridad inicial (S1): advertencias/contraindicaciones del prospecto (brecha bloqueante DG001) y mecanismo de acción verificado (DG002).

**Para avanzar se necesita:**
- Obtener las advertencias y contraindicaciones del prospecto oficial (fuente TFDA/AEMPS) — bloqueante para pasar a S1
- Confirmar el mecanismo de acción vía consulta directa a la API de DrugBank
- Redefinir la búsqueda con subtipos específicos de cardiopatía (p. ej. insuficiencia cardíaca, miocarditis) en lugar del término amplio "heart disease", ya que la amplitud del término explica en parte el ruido observado
- Evaluar la relevancia real de la señal TxGNN mediante revisión mecanística experta, dado que el propio análisis de evidencia sugiere una asociación indirecta vía nodos de "inflamación" más que una relación causal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

