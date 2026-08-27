---
layout: default
title: Lenograstim
parent: 僅模型預測 (L5)
nav_order: 161
evidence_level: L5
indication_count: 4
---

# Lenograstim
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Lenograstim: De Neutropenia (uso conocido) a Trastorno Primario de Liberación Plaquetaria

## Resumen en Una Frase

Lenograstim es la forma recombinante del factor estimulante de colonias de granulocitos (G-CSF), farmacológicamente empleada para estimular la producción de neutrófilos y movilizar células madre hematopoyéticas; el Evidence Pack no contiene una indicación regulatoria original confirmada para este fármaco. El modelo TxGNN predice que podría ser efectivo para el **trastorno primario de liberación plaquetaria** (primary release disorder of platelets), con una puntuación de **99,91%**, pero los **13 ensayos clínicos** identificados corresponden a trasplante hematopoyético y no abordan directamente esta indicación, y no hay literatura de respaldo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en la fuente (fármaco no comercializado; ver mecanismo de acción conocido más abajo) |
| Nueva Indicación Predicha | Trastorno Primario de Liberación Plaquetaria (primary release disorder of platelets) |
| Puntaje de Predicción TxGNN | 99,91% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Lenograstim es G-CSF recombinante: se une al receptor G-CSFR y activa la vía JAK-STAT para estimular la proliferación y diferenciación de precursores granulocíticos en la médula ósea, además de movilizar células madre hematopoyéticas hacia la sangre periférica. No se dispone de una indicación regulatoria original confirmada en esta fuente, pero clínicamente esta clase de fármacos se emplea de forma conocida para neutropenia y movilización de progenitores para trasplante.

El trastorno primario de liberación plaquetaria (p. ej., enfermedades del pool de almacenamiento plaquetario) es un defecto en la secreción de los gránulos densos o alfa de las plaquetas — un proceso biológico distinto de la generación de granulocitos. No existe una superposición mecanística conocida entre la vía G-CSFR/JAK-STAT y los mecanismos de secreción de gránulos plaquetarios.

Según el propio análisis incluido en el Evidence Pack, la puntuación alta de TxGNN probablemente refleja un efecto de agrupamiento en el grafo de conocimiento en torno a nodos de "enfermedades hematológicas", más que una conexión farmacológica real. Los 13 ensayos clínicos recuperados corresponden a trasplante de células madre hematopoyéticas —donde lenograstim se usa como apoyo para movilización o injerto—, no al tratamiento del trastorno plaquetario en sí, y todos fueron clasificados como de baja relevancia (grado C) o quedaron pendientes de evaluación. La plausibilidad mecanística de esta predicción es, por tanto, actualmente baja.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04047628](https://clinicaltrials.gov/study/NCT04047628) | Fase 3 | Reclutando | 156 | AHSCT autólogo vs. mejor terapia disponible en esclerosis múltiple recidivante resistente a tratamiento; no relacionado con trastornos plaquetarios (grado C). |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Fase 2 | Reclutando | 358 | Profilaxis de GVHD post-trasplante con ciclofosfamida en neoplasias hematológicas; enfoque en GVHD, no en función plaquetaria (grado C). |
| [NCT05436418](https://clinicaltrials.gov/study/NCT05436418) | Fase 1/2 | Reclutando | 260 | Dosis mínima eficaz de ciclofosfamida post-trasplante para profilaxis de GVHD (grado C). |
| [NCT00245037](https://clinicaltrials.gov/study/NCT00245037) | Fase 1/2 | Completado | 147 | Trasplante alogénico no mieloablativo con busulfán/fludarabina/ICT en neoplasias hematológicas (grado C). |
| [NCT01335932](https://clinicaltrials.gov/study/NCT01335932) | Fase 2 | Completado | 160 | Ganciclovir/valganciclovir para prevención de reactivación de CMV en fallo respiratorio agudo; sin relación con el trastorno plaquetario (grado C). |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Fase 2 | Completado | 60 | Trasplante alogénico/singénico de células madre en sarcomas pediátricos de alto riesgo (grado C). |
| [NCT00923364](https://clinicaltrials.gov/study/NCT00923364) | Fase 2 | Completado | 19 | Trasplante de intensidad reducida en pacientes con mutaciones GATA2 (relevancia pendiente de evaluar). |
| [NCT01503918](https://clinicaltrials.gov/study/NCT01503918) | Fase 2 | Completado | 124 | Profilaxis antiviral para reactivación de CMV en cuidados críticos (relevancia pendiente de evaluar). |
| [NCT00076752](https://clinicaltrials.gov/study/NCT00076752) | Fase 2 | Completado | 9 | Linfodepleción intensificada seguida de trasplante autólogo en lupus eritematoso sistémico grave (grado C). |
| [NCT00281879](https://clinicaltrials.gov/study/NCT00281879) | Fase 2 | Terminado | 200 | Trasplante de donante no emparentado para neoplasias hematológicas; ensayo terminado, sin relación directa (grado C). |

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. La revisión inicial de seguridad (advertencias TFDA/AEMPS, contraindicaciones e interacciones) está actualmente bloqueada por falta de datos fuente — es un vacío de datos de severidad *Blocking* que impide avanzar a la evaluación de seguridad S1.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia clínica disponible (13 ensayos) es toda de trasplante hematopoyético y ha sido calificada como de relevancia baja o pendiente respecto al trastorno primario de liberación plaquetaria; no hay literatura de respaldo, y el propio análisis mecanístico del Evidence Pack indica que la puntuación de TxGNN probablemente es un artefacto de agrupamiento en el grafo de conocimiento más que una señal farmacológica real. Los otros tres candidatos predichos (Glanzmann thrombasthenia, pseudo-von Willebrand disease, retinopatía diabética no proliferativa grave) están en nivel de evidencia L5, sin ningún ensayo clínico ni literatura registrados, y en el caso de la retinopatía diabética el propio análisis señala un riesgo teórico de empeorar la enfermedad en lugar de un beneficio.

**Para avanzar se necesita:**
- Resolver el vacío de datos bloqueante (DG001): obtener y analizar el prospecto TFDA/AEMPS de lenograstim para completar la evaluación de seguridad S1.
- Confirmar el mecanismo de acción (DG002) vía API de DrugBank para validar o descartar la plausibilidad mecanística frente al trastorno plaquetario.
- Buscar evidencia preclínica o mecanística específica que vincule la señalización G-CSF/JAK-STAT con la secreción de gránulos plaquetarios, dado que ningún ensayo o publicación actual la aborda directamente.
- Confirmar la indicación original regulatoria del fármaco, ausente en esta fuente.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

