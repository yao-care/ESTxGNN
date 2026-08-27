---
layout: default
title: Moroctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 188
evidence_level: L5
indication_count: 8
---

# Moroctocog Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

Usando el Evidence Pack proporcionado, seleccioné como indicación a evaluar **"Deficiencia Adquirida de Factor de Coagulación"** (rank 4) en lugar de la predicción con mayor score bruto (rank 1). El propio Evidence Pack marca las predicciones rank 1, 2, 3, 5, 6, 7 y 8 como `evidence_level: L5` / `recommendation: Hold`, con razonamientos que dicen explícitamente "sin sustento mecanístico real" (p. ej. ensayos con `relevance.grade: C` que no coinciden con la enfermedad). La rank 4 es la única con evidencia sustantiva (`L2`, ensayos Grade B, `decision_stage: S2`). Presentar la rank 1 como indicación principal habría producido un informe internamente contradictorio.

---

# Moroctocog Alfa: De Reposición de Factor VIII (Hemofilia A) a Deficiencia Adquirida de Factor de Coagulación

## Resumen en Una Frase

Moroctocog alfa es un Factor VIII de coagulación recombinante con dominio B eliminado, utilizado como terapia de reposición en hemofilia A. Entre las ocho indicaciones propuestas por TxGNN, la única con respaldo real es **Deficiencia Adquirida de Factor de Coagulación** (esencialmente hemofilia A adquirida por autoanticuerpos anti-FVIII), con **13 ensayos clínicos** y **4 publicaciones** identificados; el resto de predicciones del modelo carecen de vínculo mecanístico verificable.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No registrada en el Evidence Pack; descriptivamente, el fármaco actúa como terapia de reposición de Factor VIII en hemofilia A congénita |
| Nueva Indicación Predicha | Deficiencia Adquirida de Factor de Coagulación |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

## Por qué es Razonable esta Predicción?

El campo formal de mecanismo de acción no está disponible en este Evidence Pack, pero la propia evidencia recopilada describe a moroctocog alfa como Factor VIII recombinante humano con dominio B eliminado ("B-domain deleted rFVIII"), cuya función es reponer directamente el factor de coagulación deficiente.

La Deficiencia Adquirida de Factor de Coagulación corresponde mayoritariamente a hemofilia A adquirida (AHA), causada por autoanticuerpos que neutralizan el Factor VIII endógeno. Mecanísticamente, esto es el mismo objetivo terapéutico que la hemofilia A congénita —reposición de FVIII— por lo que la predicción de TxGNN tiene una base biológica coherente, a diferencia de las otras siete predicciones del mismo lote (p. ej. trastornos de liberación plaquetaria, enfermedad de pseudo-von Willebrand, trombastenia de Glanzmann, síndrome de Scott), donde la evidencia del propio pack indica ausencia de relación mecanística real.

Existe, sin embargo, una limitación importante señalada en el propio análisis: en la práctica clínica, la AHA suele tratarse preferentemente con FVIII porcino (p. ej. Obizur) o agentes bypass, porque los mismos autoanticuerpos que causan la enfermedad pueden neutralizar también un FVIII de secuencia humana como moroctocog alfa. Esto no invalida el mecanismo, pero sí limita su papel a un uso de segunda línea o guiado por el título de inhibidor del paciente.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06550882](https://clinicaltrials.gov/study/NCT06550882) | N/A | Reclutando | 9 | Vigilancia post-comercialización de OBIZUR (FVIII porcino recombinante) en hemofilia A adquirida, Corea del Sur |
| [NCT02610127](https://clinicaltrials.gov/study/NCT02610127) | N/A | Completado | 53 | Evaluación de seguridad no intervencionista post-comercialización de Obizur en episodios hemorrágicos por AHA |
| [NCT01178294](https://clinicaltrials.gov/study/NCT01178294) | Fase 2/3 | Completado | 29 | Eficacia y seguridad de FVIII porcino recombinante (OBI-1) en AHA por autoanticuerpos anti-FVIII |
| [NCT04580407](https://clinicaltrials.gov/study/NCT04580407) | Fase 2/3 | Completado | 5 | FVIII porcino recombinante con dominio B eliminado (TAK-672) en episodios hemorrágicos graves por AHA en Japón |
| [NCT00306670](https://clinicaltrials.gov/study/NCT00306670) | Fase 2/3 | Terminado | 2 | Rituximab vs. ciclofosfamida oral para suprimir autoanticuerpos anti-FVIII en AHA |
| [NCT02453542](https://clinicaltrials.gov/study/NCT02453542) | N/A | Reclutando | 20 | Métodos hemostáticos globales para medir efecto de agentes bypass en hemofilia con inhibidores |
| [NCT01856751](https://clinicaltrials.gov/study/NCT01856751) | N/A | Desconocido | 80 | Uso de TGA y TEM para evaluar eficacia de APCC/rFVIIa en hemofilia adquirida y hemofilia A con inhibidores |
| [NCT03199794](https://clinicaltrials.gov/study/NCT03199794) | N/A | Completado | 50 | Estudio no intervencionista de seguridad y efectividad de Obizur en práctica clínica real |
| [NCT04398628](https://clinicaltrials.gov/study/NCT04398628) | N/A | Reclutando | 3000 | Registro de historia natural ATHN Transcends, incluye trastornos hematológicos no neoplásicos como AHA |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [25765796](https://pubmed.ncbi.nlm.nih.gov/25765796/) | 2015 | Revisión | Rinsho Ketsueki | Revisión de inhibidores adquiridos de factores de coagulación, mayoritariamente autoanticuerpos anti-FVIII |
| [25525118](https://pubmed.ncbi.nlm.nih.gov/25525118/) | 2015 | Cohorte (registro GTH-AH) | Blood | Factores pronósticos de remisión y supervivencia en hemofilia A adquirida bajo tratamiento inmunosupresor |
| [26517066](https://pubmed.ncbi.nlm.nih.gov/26517066/) | 2015 | Reporte de caso | Blood Coagul Fibrinolysis | Caso de AHA con desarrollo posterior de linfoma no-Hodgkin |
| [14161416](https://pubmed.ncbi.nlm.nih.gov/14161416/) | 1964 | Revisión histórica | Blood | Implicaciones clínicas de anomalías adquiridas de la coagulación |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No hay datos de advertencias, contraindicaciones ni interacciones farmacológicas disponibles en este Evidence Pack; la obtención del etiquetado de seguridad es un requisito bloqueante antes de cualquier evaluación S1.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El mecanismo de reposición de FVIII de moroctocog alfa tiene coherencia biológica directa con la deficiencia adquirida de factor de coagulación, respaldado por ensayos Fase 2/3 completados con moléculas de FVIII recombinante estructuralmente análogas (OBI-1, TAK-672) y series post-comercialización de Obizur. Sin embargo, el fármaco no está comercializado en España, no existe evidencia clínica del compuesto específico en esta indicación, y el riesgo de neutralización por los mismos autoanticuerpos que definen la enfermedad limita su posicionamiento a segunda línea o poblaciones seleccionadas.

**Para avanzar se necesita:**
- Obtener el etiquetado de seguridad (advertencias/contraindicaciones) de la agencia reguladora — actualmente bloqueante para la evaluación de seguridad
- Confirmar el mecanismo de acción y perfil de inmunogenicidad vía DrugBank
- Evaluar el estado de inhibidores anti-FVIII como criterio de selección de pacientes antes de posicionar moroctocog alfa frente a alternativas porcinas o agentes bypass
- Descartar formalmente las siete predicciones restantes del mismo lote TxGNN, dado que su propia evidencia interna no sustenta un vínculo mecanístico real
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

