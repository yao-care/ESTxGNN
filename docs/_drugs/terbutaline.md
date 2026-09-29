---
layout: default
title: Terbutaline
parent: Evidencia alta (L1-L2)
nav_order: 520
evidence_level: L1
indication_count: 3
---

# Terbutaline
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **3** 
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

# Terbutalina: De Broncoespasmo Reversible a Enfermedad Pulmonar Obstructiva

## Resumen en Una Frase

La terbutalina es un agonista beta-2 adrenérgico que ya se usa como broncodilatador en el broncoespasmo asociado a asma, bronquitis y enfisema. El modelo TxGNN predice que podría ser efectiva para la **enfermedad pulmonar obstructiva**, con **48 ensayos clínicos** y **20 publicaciones** asociados. Es más una confirmación de un uso ya establecido que un reposicionamiento genuino.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Prevención y reversión del broncoespasmo en enfermedad obstructiva reversible de las vías respiratorias (según datos farmacológicos; el registro de la AEMPS no incluye texto de indicación) |
| Nueva Indicación Predicha | Enfermedad pulmonar obstructiva (obstructive lung disease) |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

La terbutalina es un agonista selectivo de los receptores beta-2 adrenérgicos (ADRB2), con actividad también sobre ADRB1. Al activar el receptor beta-2 aumenta el AMPc en el músculo liso de las vías respiratorias. Esto lo relaja y produce broncodilatación. No hay un campo de mecanismo de acción en DrugBank, pero este mecanismo está bien establecido y coincide con los datos farmacológicos disponibles.

La obstrucción reversible del flujo aéreo en asma y EPOC es justamente la diana de este mecanismo. Además, el fármaco ya está comercializado en España como broncodilatador. La predicción del modelo se acerca más a confirmar un uso existente que a proponer una indicación nueva. El campo de indicaciones originales del Evidence Pack está vacío, por lo que no se puede medir una "distancia" formal entre indicación original y nueva.

El uso regular y prolongado de agonistas beta puede afectar la respuesta de las vías respiratorias (véase PMID 8882073).

---

## Evidencia de Ensayos Clínicos

Se identificaron 48 ensayos. Se listan los 10 más relevantes. La mayoría de los ensayos de Fase 3 usan la terbutalina como medicación de rescate en el brazo comparador, no como intervención evaluada.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06626620](https://clinicaltrials.gov/study/NCT06626620) | Fase 3 | Completado | 120 | ECA de sulfato de magnesio intravenoso vs. terbutalina en exacerbación aguda de asma pediátrica. Evidencia directa (grado A) |
| [NCT02149199](https://clinicaltrials.gov/study/NCT02149199) | Fase 3 | Completado | 3850 | Symbicort a demanda vs. terbutalina a demanda vs. budesonida + terbutalina en asma leve |
| [NCT01096017](https://clinicaltrials.gov/study/NCT01096017) | Fase 3 | Completado | 24 | Eficacia relativa de terbutalina Turbuhaler 0,4 mg vs. salbutamol pMDI en asma en pacientes japoneses |
| [NCT02322788](https://clinicaltrials.gov/study/NCT02322788) | Fase 3 | Completado | 95 | Bricanyl Turbuhaler M3 vs. M2: protección frente a la broncoconstricción por metacolina en asma |
| [NCT00750568](https://clinicaltrials.gov/study/NCT00750568) | N/A | Desconocido | 36 | Farmacocinética y farmacodinamia de terbutalina en infusión intravenosa continua en estado asmático pediátrico |
| [NCT00839800](https://clinicaltrials.gov/study/NCT00839800) | Fase 3 | Completado | 2091 | Symbicort SMART vs. Symbicort + terbutalina a demanda en asma (grado B, evidencia indirecta) |
| [NCT02224157](https://clinicaltrials.gov/study/NCT02224157) | Fase 3 | Completado | 4215 | Symbicort a demanda vs. budesonida dos veces al día + terbutalina a demanda en asma (grado B) |
| [NCT00252863](https://clinicaltrials.gov/study/NCT00252863) | Fase 3 | Completado | 1600 | Symbicort SMART vs. mejor práctica convencional en asma persistente (grado B) |
| [NCT00849095](https://clinicaltrials.gov/study/NCT00849095) | Fase 3 | Completado | 860 | Budesonida/formoterol a demanda vs. regular + terbutalina a demanda en asma leve-moderada |
| [NCT01944033](https://clinicaltrials.gov/study/NCT01944033) | Fase 3 | Completado | 250 | β2-agonista solo vs. bromuro de ipratropio + β2-agonista en exacerbación de EPOC |

---

## Evidencia de Literatura

Se identificaron 20 publicaciones. Se listan las 10 más relevantes, con prioridad para los ECA.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30156361](https://pubmed.ncbi.nlm.nih.gov/30156361/) | 2019 | ECA | Acad Emerg Med | Terbutalina nebulizada con ipratropio vs. terbutalina sola en exacerbación de EPOC que requiere ventilación no invasiva |
| [10384064](https://pubmed.ncbi.nlm.nih.gov/10384064/) | 1999 | ECA | Lung | Efecto de una dosis de terbutalina (Turbuhaler) sobre función pulmonar y capacidad de ejercicio en EPOC |
| [3073804](https://pubmed.ncbi.nlm.nih.gov/3073804/) | 1988 | ECA | Br J Dis Chest | Terbutalina oral aumentó la fuerza diafragmática frente a placebo en EPOC (10 pacientes) |
| [6988343](https://pubmed.ncbi.nlm.nih.gov/6988343/) | 1980 | ECA | Int J Clin Pharmacol Ther Toxicol | Comparación de clenbuterol y terbutalina orales en enfermedad pulmonar obstructiva crónica |
| [36227333](https://pubmed.ncbi.nlm.nih.gov/36227333/) | 2023 | Revisión sistemática | Naunyn-Schmiedebergs Arch Pharmacol | Farmacocinética clínica de la terbutalina en humanos |
| [33065789](https://pubmed.ncbi.nlm.nih.gov/33065789/) | 2020 | Estudio clínico | Ann Palliat Med | N-acetilcisteína combinada con terbutalina en ancianos con EPOC |
| [1615190](https://pubmed.ncbi.nlm.nih.gov/1615190/) | 1992 | Estudio clínico (doble ciego, cruzado) | Respir Med | Terbutalina inhalada sobre FEV1, FVC, disnea y distancia de marcha en EPOC |
| [2031046](https://pubmed.ncbi.nlm.nih.gov/2031046/) | 1991 | Estudio clínico (cruzado) | Pneumologie | Terbutalina nebulizada con presión espiratoria positiva en EPOC |
| [8882073](https://pubmed.ncbi.nlm.nih.gov/8882073/) | 1996 | Estudio clínico | Thorax | Efectos de suspender la terbutalina sobre la obstrucción y la reactividad de las vías respiratorias en EPOC |
| [6107217](https://pubmed.ncbi.nlm.nih.gov/6107217/) | 1980 | Estudio clínico | Chest | Interacción entre betabloqueantes y terbutalina oral en EPOC con cardiopatía isquémica o hipertensión |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 52616 | TERBASMIN 0,3 mg/ml solución oral (Laboratorios Ern S.A.) | Solución oral | Texto de indicación no disponible en el registro |
| 58859 | TERBASMIN TURBUHALER 500 microgramos/inhalación (Laboratorio Lailan S.A.) | Polvo para inhalación | Texto de indicación no disponible en el registro |

---

## Consideraciones de Seguridad

No se dispone de advertencias ni contraindicaciones extraídas del prospecto de la AEMPS. Según el análisis del modelo, las precauciones principales son:

- **Efectos adversos a vigilar**: taquicardia, temblor e hipopotasemia.
- **Precaución**: pacientes con enfermedad cardiovascular.
- **Interacciones**: el estudio PMID 6107217 evaluó la interacción entre betabloqueantes y terbutalina oral. Los betabloqueantes pueden antagonizar el efecto broncodilatador.

Consultar el prospecto para la información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay múltiples ensayos de Fase 3 completados y ECA publicados que respaldan el efecto broncodilatador de la terbutalina en asma y EPOC, y el fármaco ya está comercializado. Sin embargo, la mayoría de los ensayos de Fase 3 usan la terbutalina como rescate en el brazo comparador, no como intervención evaluada. Solo un ensayo (NCT06626620) la evalúa directamente. El nivel L1 debe leerse con esta salvedad.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones autorizadas), que hoy es un vacío bloqueante.
- Confirmar las indicaciones originales autorizadas, para aclarar si "enfermedad pulmonar obstructiva" supone realmente algo nuevo.
- Definir un plan de monitoreo cardiovascular y de potasio en poblaciones de riesgo.

**Otras predicciones del modelo (no recomendadas por ahora, decisión Hold):**
- **Malformación respiratoria** (puntaje 99.52%, nivel L4): la evidencia es indirecta. El puntaje probablemente refleja una asociación amplia con enfermedades respiratorias, no un mecanismo específico.
- **Síndrome de Rienhoff** (puntaje 99.38%, nivel L5): no hay ensayos ni literatura. Solo es una predicción del grafo de conocimiento y requiere revisión mecanística independiente.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

