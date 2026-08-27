---
layout: default
title: Sotalol
parent: 僅模型預測 (L5)
nav_order: 264
evidence_level: L5
indication_count: 7
---

# Sotalol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Sotalol: De Arritmia Cardíaca a Prevención de Ictus Asociado a Fibrilación Auricular

## Resumen en Una Frase

Sotalol es un antiarrítmico de Clase III con actividad betabloqueante, utilizado clínicamente en el control del ritmo en arritmias ventriculares y fibrilación auricular (FA). El modelo TxGNN predice una asociación con **"stroke disorder"** (ictus), que el análisis mecanístico identifica como una relación indirecta vía control de FA más que un efecto antitrombótico directo, respaldada por **22 ensayos clínicos** y **20 publicaciones**.

> **Nota de alcance:** el Evidence Pack contiene 7 indicaciones predichas por TxGNN. Solo la indicación de rango 4 ("stroke disorder") cuenta con evidencia clínica real; las otras 6 (rango 1, 2, 3, 5, 6, 7) carecen de ensayos/literatura o presentan una relación mecanística de riesgo (no terapéutica). Por eso este informe se centra en la indicación de rango 4 y resume el resto al final.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Arritmia cardíaca (antiarrítmico Clase III / betabloqueante) — texto regulatorio detallado no disponible por ausencia de comercialización en España |
| Nueva Indicación Predicha | Ictus ("stroke disorder"), en el contexto mecanístico de prevención de ictus asociado a fibrilación auricular |
| Puntaje de Predicción TxGNN | 99.44% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

No se dispone de datos estructurados de mecanismo de acción (MOA) de DrugBank para sotalol en este Evidence Pack (brecha de datos identificada como severidad "High"). Según la información disponible en la literatura recogida, sotalol es "un betabloqueante único que prolonga la repolarización" (PMID 1281807), es decir, combina bloqueo beta-adrenérgico no selectivo con propiedades de Clase III (inhibición de corrientes de potasio, prolongación del intervalo QT).

La etiqueta predicha "stroke disorder" no corresponde a un mecanismo antitrombótico directo. Según el razonamiento mecanístico del propio análisis, la asociación real es indirecta: sotalol se usa para mantener el ritmo sinusal en fibrilación auricular (control de ritmo), y la FA no controlada es un factor de riesgo mayor de ictus embólico. Por tanto, el efecto sobre el riesgo de ictus sería consecuencia de controlar la arritmia subyacente, no de una acción farmacológica nueva sobre la coagulación o la circulación cerebral.

Esto se confirma con el ensayo CSP #399 (NCT00007605, Fase 3, n=706), que evaluó directamente si sotalol y amiodarona son seguros y eficaces para mantener el ritmo sinusal en FA, población en la que el ictus es un desenlace clínico central. En conjunto, la evidencia respalda que esta "nueva indicación" es en realidad una extensión ya reconocida clínicamente del uso de sotalol en FA (label-adjacent), no una hipótesis de reposicionamiento completamente nueva.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00007605](https://clinicaltrials.gov/study/NCT00007605) | Fase 3 | Completado | 706 | CSP #399: evalúa si amiodarona y sotalol son seguros y eficaces para mantener el ritmo sinusal en FA, frente a las dudas de seguridad sobre quinidina. Evidencia directa de mayor calidad. |
| [NCT05279833](https://clinicaltrials.gov/study/NCT05279833) | No aplica | Completado | 87.810 | Revisión sistemática/meta-análisis en red comparando dronedarona vs. sotalol en seguridad y eficacia en FA. |
| [NCT02389218](https://clinicaltrials.gov/study/NCT02389218) | Fase 4 | Completado | 13 | Comparación de crioablación con balón vs. terapia médica estandarizada (puede incluir sotalol) en FA persistente reciente. |
| [NCT00911508](https://clinicaltrials.gov/study/NCT00911508) | No aplica | Completado | 2.204 | CABANA: ablación por catéter vs. fármacos antiarrítmicos (control de frecuencia o ritmo) en FA. |
| [NCT02145546](https://clinicaltrials.gov/study/NCT02145546) | Fase 4 | Desconocido | 600 | Evalúa amiodarona, sotalol y propafenona en el manejo a largo plazo de FA en pacientes con síndrome del seno enfermo. |
| [NCT00523978](https://clinicaltrials.gov/study/NCT00523978) | Fase 3 | Completado | 245 | STOP AF: crioablación vs. fármaco antiarrítmico de estudio (flecainida, propafenona o sotalol) en FA paroxística refractaria. |
| [NCT07405671](https://clinicaltrials.gov/study/NCT07405671) | Fase 4 | Aún no recluta | 988 | Compara flecainida frente al estándar de cuidado (sotalol o amiodarona) en FA con enfermedad coronaria estable. |
| [NCT01856075](https://clinicaltrials.gov/study/NCT01856075) | No aplica | Completado | 1.015 | Estudio observacional internacional de efectividad relativa de dronedarona vs. otros antiarrítmicos en la práctica clínica real. |
| [NCT06322017](https://clinicaltrials.gov/study/NCT06322017) | No aplica | Reclutando | 294 | Aislamiento precoz de venas pulmonares vs. tratamiento habitual (incluye control de ritmo farmacológico) en mayores de 75 años con FA. |
| [NCT02830360](https://clinicaltrials.gov/study/NCT02830360) | Fase 4 | Completado | 416 | VANISH2: ablación por catéter vs. fármacos antiarrítmicos en taquicardia ventricular sostenida sobre cardiopatía estructural. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37485722](https://pubmed.ncbi.nlm.nih.gov/37485722/) | 2023 | Cohorte | Circ Arrhythm Electrophysiol | Comparación retrospectiva head-to-head de dronedarona vs. sotalol en veteranos con FA sin tratamiento previo; sotalol requiere monitorización de QT y proarritmia. |
| [29954667](https://pubmed.ncbi.nlm.nih.gov/29954667/) | 2019 | Cohorte | Int J Cardiol | Eficacia y efectos adversos de sotalol en adultos con cardiopatía congénita, alternativa a amiodarona por su perfil de toxicidad. |
| [1281807](https://pubmed.ncbi.nlm.nih.gov/1281807/) | 1992 | ECA | Int J Cardiol | Sotalol en 626 pacientes con arritmia ventricular compleja; supresión de la arritmia en 50-60% de los intentos de tratamiento. |
| [9576159](https://pubmed.ncbi.nlm.nih.gov/9576159/) | 1998 | ECA | Am J Cardiol | Ensayo aleatorizado doble ciego (n=70): amiodarona en dosis baja vs. sotalol para supresión de FA sintomática recurrente. |
| [8346725](https://pubmed.ncbi.nlm.nih.gov/8346725/) | 1993 | Estudio observacional | Am J Cardiol | Efectos hemodinámicos del sotalol oral durante titulación de dosis en pacientes con arritmia ventricular y cardiopatía estructural. |
| [7509121](https://pubmed.ncbi.nlm.nih.gov/7509121/) | 1994 | Estudio observacional | Am J Cardiol | La respuesta a sotalol predice la respuesta a amiodarona mediante estimulación ventricular programada en taquicardia ventricular sostenida. |
| [25428811](https://pubmed.ncbi.nlm.nih.gov/25428811/) | 2015 | Análisis farmacoeconómico | Kardiol Pol | Coste-efectividad de dronedarona vs. amiodarona, propafenona y sotalol en FA (datos para Serbia). |
| [28496906](https://pubmed.ncbi.nlm.nih.gov/28496906/) | 2013 | Cohorte | J Atr Fibrillation | Cohorte retrospectiva (n=10.455) de riesgo cardiovascular, ictus, insuficiencia cardíaca y daño hepático con dronedarona vs. amiodarona y otros antiarrítmicos. |
| [38011245](https://pubmed.ncbi.nlm.nih.gov/38011245/) | 2023 | Revisión | Circulation | Manejo contemporáneo de la FA en miocardiopatía hipertrófica, incluyendo estrategias de control de ritmo y riesgo de ictus. |
| [37777295](https://pubmed.ncbi.nlm.nih.gov/37777295/) | 2023 | Guía/Revisión | Am J Cardiol | Recomendaciones de guías ACC/AHA/HRS y ESC sobre selección de fármacos antiarrítmicos en FA. |

---

## Consideraciones de Seguridad

No hay datos estructurados de advertencias, contraindicaciones o interacciones (DDI) en las fuentes regulatorias consultadas (TFDA/ficha técnica). Sin embargo, la literatura y el análisis mecanístico del propio Evidence Pack señalan riesgos relevantes a vigilar:

- **Bradicardia grave en síndrome del seno enfermo:** sotalol está considerado de uso arriesgado o contraindicado sin protección de marcapasos en pacientes con síndrome del seno enfermo, por su acción cronotrópica negativa combinada (betabloqueo + Clase III).
- **Riesgo torsadogénico con antipsicóticos:** el bloqueo beta-adrenérgico de sotalol puede potenciar el efecto torsadogénico de antipsicóticos que prolongan el QT, como risperidona (PMID 39179332).
- **Bradicardia sintomática con litio:** se ha descrito la necesidad de marcapasos permanente para mantener terapia con litio en un paciente maníaco que desarrolló bradicardia sintomática con sotalol (PMID 10958269).
- **Monitorización de QT:** a diferencia de otros antiarrítmicos (p. ej. dronedarona), sotalol requiere monitorización inicial de la prolongación del QT y del riesgo proarrítmico (PMID 37485722).

---

## Otras Predicciones Evaluadas (Sin Evidencia Suficiente)

| Indicación | Puntaje TxGNN | Nivel de Evidencia | Motivo de "Hold" |
|------|------|------|------|
| Síndrome del seno enfermo tipo 2 | 99.76% | L5 | Relación de riesgo, no terapéutica: sotalol puede inducir bradicardia grave en esta población sin protección de marcapasos. |
| Síndrome de Wildervanck | 99.65% | L5 | Sin vínculo mecanístico conocido con canales iónicos cardíacos ni arritmia; sin evidencia. |
| Sarcoglicanopatía | 99.64% | L5 | Hipótesis puramente mecanística (miocardiopatía asociada); sin ensayos ni literatura de respaldo. |
| Trastorno bipolar, episodio maníaco | 99.43% | L4 | La literatura disponible describe riesgos de interacción (QT, bradicardia), no eficacia antimaníaca. |
| Macrocefalia con facies dismórfica y retraso psicomotor | 99.42% | L5 | Síndrome neurodesarrollo sin relación conocida con el mecanismo de sotalol; sin evidencia. |
| Susceptibilidad a ictus isquémico (obsoleto) | 99.23% | L5 | Término de ontología de enfermedad marcado como obsoleto; señal de ruido del grafo de conocimiento. |

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La única indicación predicha con evidencia real (rango 4, "stroke disorder") alcanza nivel L1 gracias a un ECA de Fase 3 (CSP #399, n=706) y amplia literatura de apoyo, pero corresponde a una extensión ya conocida del uso de sotalol en control de ritmo de FA, no a un mecanismo antitrombótico nuevo. Las otras 6 indicaciones predichas por TxGNN carecen de evidencia clínica o presentan relaciones de riesgo, no terapéuticas, y deben mantenerse en "Hold".

**Para avanzar se necesita:**
- Obtener el prospecto/ficha técnica de TFDA (brecha bloqueante DG001) para completar la evaluación de seguridad S1.
- Obtener datos estructurados de MOA desde DrugBank (brecha DG002) para robustecer el análisis mecanístico.
- Clarificar si la propuesta regulatoria se centra en "control de ritmo en FA con reducción de riesgo de ictus" en vez de "tratamiento de ictus", dado que la etiqueta original de TxGNN puede inducir a error.
- Confirmar plan de monitorización de QT y riesgo proarrítmico antes de cualquier uso clínico ampliado.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

