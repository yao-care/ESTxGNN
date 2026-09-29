---
layout: default
title: Flecainide
parent: Evidencia moderada (L3-L4)
nav_order: 234
evidence_level: L4
indication_count: 10
---

# Flecainide
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Flecainida: De Arritmias Cardíacas a Accidente Cerebrovascular (Ictus)

## Resumen en Una Frase

Flecainida es un antiarrítmico de clase IC (bloqueante de canales de sodio), utilizado originalmente para controlar arritmias ventriculares y auriculares y taquicardias.
El modelo TxGNN predice que podría ser efectivo para **accidente cerebrovascular (ictus)**, pero la evidencia es solo **indirecta**: se registran **21 ensayos clínicos** y **20 publicaciones**, casi todos sobre fibrilación auricular (FA) y ninguno demuestra un efecto de la flecainida sobre el ictus.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Arritmias ventriculares y auriculares y taquicardias (según la farmacología de referencia; los registros de AEMPS no incluyen texto de indicación) |
| Nueva Indicación Predicha | Accidente cerebrovascular (stroke disorder) |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información conocida, la flecainida es un bloqueante de canales de sodio de clase IC que mantiene el ritmo sinusal en la fibrilación auricular. Su eficacia en arritmias está comprobada, y el vínculo con el ictus sería solo indirecto.

La relación entre ambas indicaciones pasa por la FA. La FA aumenta el riesgo de ictus cardioembólico, y el control temprano del ritmo podría reducirlo. El ensayo EAST-AFNET 4 (NCT01288352, Fase 4, n=2789) apoya el control precoz del ritmo como estrategia. Sin embargo, la flecainida es solo uno de varios fármacos de ese brazo, y no se ha demostrado un efecto preventivo del ictus atribuible a ella sola.

No existe un mecanismo neuroprotector directo. El puntaje alto de TxGNN probablemente refleja la cercanía entre FA e ictus en el grafo de conocimiento y no un mecanismo nuevo. Por eso esta predicción debe leerse como una pregunta de investigación, no como una indicación candidata madura.

## Evidencia de Ensayos Clínicos

Se muestran los 10 más relevantes de 21 registrados. Solo NCT05213104 y NCT07405671 estudian directamente la flecainida, y ninguno tiene ictus como desenlace.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01288352](https://clinicaltrials.gov/study/NCT01288352) | Fase 4 | Completado | 2789 | EAST-AFNET 4: control precoz del ritmo (fármacos antiarrítmicos, incluida flecainida, o ablación) frente a atención habitual; el ictus forma parte del desenlace compuesto. Evidencia indirecta más sólida |
| [NCT05293080](https://clinicaltrials.gov/study/NCT05293080) | Fase 3 | Reclutando | 1746 | EAST-STROKE: control precoz del ritmo en ictus isquémico agudo con FA. Sin resultados aún; estrategia no específica de flecainida |
| [NCT05213104](https://clinicaltrials.gov/study/NCT05213104) | Fase 3 | Activo, sin reclutar | 186 | Flecainida para reducir arritmia auricular tras cierre de foramen oval permeable (población con ictus criptogénico); desenlace sustituto (arritmia) |
| [NCT00911508](https://clinicaltrials.gov/study/NCT00911508) | N/A | Completado | 2204 | CABANA: ablación con catéter frente a fármacos antiarrítmicos (entre ellos flecainida); ictus dentro del desenlace compuesto |
| [NCT01646281](https://clinicaltrials.gov/study/NCT01646281) | Fase 4 | Desconocido | 70 | Vernakalant y flecainida sobre la contractilidad auricular en FA; marcador sustituto del riesgo tromboembólico |
| [NCT06783868](https://clinicaltrials.gov/study/NCT06783868) | N/A | Aún no reclutando | 100 | SAVE STROKE II: ablación de FA frente a medicación tras ictus reciente; la intervención es la ablación |
| [NCT07405671](https://clinicaltrials.gov/study/NCT07405671) | Fase 4 | Reclutando | 988 | Seguridad de flecainida frente a sotalol o amiodarona en FA con enfermedad coronaria estable |
| [NCT00523978](https://clinicaltrials.gov/study/NCT00523978) | Fase 3 | Completado | 245 | STOP AF: crioablación frente a fármaco antiarrítmico (flecainida, propafenona o sotalol) en FA paroxística |
| [NCT05939076](https://clinicaltrials.gov/study/NCT05939076) | Fase 3 | Aún no reclutando | 220 | Crioablación de primera línea frente a antiarrítmicos en FA persistente |
| [NCT06096337](https://clinicaltrials.gov/study/NCT06096337) | N/A | Activo, sin reclutar | 484 | Ablación por campo pulsado frente a antiarrítmicos como primera línea en FA persistente |

## Evidencia de Literatura

Se muestran 10 de 20 publicaciones. Ninguna evalúa la flecainida como tratamiento del ictus.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38702961](https://pubmed.ncbi.nlm.nih.gov/38702961/) | 2024 | ECA (análisis secundario) | Europace | Seguridad y eficacia a largo plazo de los bloqueantes de sodio (flecainida y propafenona) para el control precoz del ritmo en EAST-AFNET 4 |
| [37109225](https://pubmed.ncbi.nlm.nih.gov/37109225/) | 2023 | ECA piloto | J Clin Med | Carvedilol frente a flecainida en extrasístoles ventriculares idiopáticas del tracto de salida; no aborda el ictus |
| [41954064](https://pubmed.ncbi.nlm.nih.gov/41954064/) | 2026 | Cohorte | J Am Heart Assoc | Resultados a largo plazo de los antiarrítmicos de clase 1C en FA; el beneficio cardiovascular frente al control de frecuencia sigue sin estar claro |
| [27159789](https://pubmed.ncbi.nlm.nih.gov/27159789/) | 2016 | Revisión | Nat Rev Dis Primers | Revisión general de la FA y su asociación con mayor riesgo de ictus |
| [25430048](https://pubmed.ncbi.nlm.nih.gov/25430048/) | 2014 | Revisión | BMJ Clin Evidence | FA de inicio agudo; aumenta el riesgo de ictus e insuficiencia cardíaca |
| [39077579](https://pubmed.ncbi.nlm.nih.gov/39077579/) | 2023 | Revisión | Rev Cardiovasc Med | Manejo de la FA en el embarazo y equilibrio entre riesgos de antiarrítmicos y anticoagulantes |
| [8199770](https://pubmed.ncbi.nlm.nih.gov/8199770/) | 1994 | Revisión | Heart Dis Stroke | Valor y peligros de la flecainida; útil en taquicardia supraventricular sin cardiopatía estructural |
| [38551548](https://pubmed.ncbi.nlm.nih.gov/38551548/) | 2024 | Estudio clínico | JACC Clin Electrophysiol | Antiarrítmicos 1C para suprimir extrasístoles ventriculares en miocardiopatía no isquémica con DAI |
| [35114252](https://pubmed.ncbi.nlm.nih.gov/35114252/) | 2022 | Estudio de mecanismo | J Mol Cell Cardiol | Mayor eficacia auricular de la flecainida por diferencias biofísicas de los canales de sodio |
| [40800559](https://pubmed.ncbi.nlm.nih.gov/40800559/) | 2025 | Reporte de caso | Eur Heart J Case Rep | Taquicardia ventricular refractaria asociada a flecainida (proarritmia) |

## Información de Mercado en España

Se listan 5 de las 6 autorizaciones. El registro no incluye texto de indicación aprobada para ninguna de ellas. También constan formas farmacéuticas en comprimido y solución inyectable.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 79337 | Flecainida Apotex 100 mg comprimidos EFG | Comprimido | Sin texto de indicación en el registro |
| 79329 | Flecainida Normon 100 mg comprimidos EFG | Comprimido | Sin texto de indicación en el registro |
| 77173 | Flecainida Aurovitas 100 mg comprimidos EFG | Comprimido | Sin texto de indicación en el registro |
| 78070 | Flecard 100 mg comprimidos EFG | Comprimido | Sin texto de indicación en el registro |
| 57532 | Apocard 100 mg comprimidos | Comprimido | Sin texto de indicación en el registro |

## Consideraciones de Seguridad

No se dispone de advertencias ni contraindicaciones del prospecto de AEMPS. Consultar el prospecto para la información de seguridad completa. Los cinco registros de interacción de la consulta corresponden a dianas farmacológicas (canales Kv), no a interacciones medicamentosas clínicas, por lo que no se listan.

A partir de la evidencia revisada, se señalan estos puntos de cautela para esta indicación:
- **Cardiopatía estructural e infarto previo**: la flecainida está contraindicada en estos casos (estudio CAST), y son frecuentes en pacientes con ictus isquémico.
- **Anticoagulantes orales directos**: se ha documentado una interacción entre estos y ciertos antiarrítmicos (PMID 41152878) que requiere revisión.
- **Proarritmia**: el reporte de caso PMID 40800559 describe taquicardia ventricular refractaria asociada a flecainida.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia es indirecta (L4). Los ensayos relevantes evalúan estrategias de control del ritmo en general, no la flecainida como tratamiento del ictus, y no existe un mecanismo neuroprotector directo. Además, las contraindicaciones en cardiopatía estructural e isquémica afectan a buena parte de la población con ictus. Las otras nueve predicciones (por ejemplo, síndrome del seno enfermo, amiloidosis ABri o sarcoglicanopatía) son solo predicciones del modelo (L5) y también se mantienen en Hold. La del síndrome del seno enfermo es probablemente un falso positivo con riesgo de seguridad.

**Para avanzar se necesita:**
- Revisar la ficha técnica de AEMPS (advertencias y contraindicaciones), actualmente no disponible.
- Obtener los resultados de NCT05213104 (finalización prevista en septiembre de 2026) y de NCT05293080 (EAST-STROKE).
- Analizar el subgrupo de flecainida en EAST-AFNET 4 (PMID 38702961) para valorar eventos cerebrovasculares.
- Seguir NCT07405671 (seguridad de flecainida en FA con enfermedad coronaria estable).
- Definir un plan de seguridad para pacientes con ictus (exclusión de cardiopatía estructural e isquémica y revisión de la interacción con anticoagulantes orales directos).
- Completar los datos del mecanismo de acción desde DrugBank.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

