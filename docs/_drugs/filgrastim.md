---
layout: default
title: Filgrastim
parent: 僅模型預測 (L5)
nav_order: 120
evidence_level: L5
indication_count: 10
---

# Filgrastim
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

# Filgrastim: De Neutropenia a Trastorno Primario de Liberación Plaquetaria

## Resumen en Una Frase

Filgrastim es un G-CSF (factor estimulante de colonias de granulocitos) recombinante, de uso internacionalmente establecido para el tratamiento y prevención de la neutropenia. El modelo TxGNN predice que podría ser efectivo para **trastorno primario de liberación plaquetaria (primary release disorder of platelets)**, pero la evidencia recopilada —14 ensayos clínicos y 1 publicación— corresponde en su totalidad a estudios de trasplante de células madre hematopoyéticas donde filgrastim se usa como agente movilizador de soporte, no como tratamiento dirigido a este trastorno.

> **Nota sobre datos de origen:** España no comercializa actualmente filgrastim bajo este expediente (0 autorizaciones registradas), por lo que no existe un texto de indicación aprobado localmente que citar; la indicación original arriba mencionada corresponde al uso internacional conocido del principio activo, no a una ficha técnica española verificada en este Evidence Pack.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Neutropenia (uso internacional establecido como G-CSF recombinante); sin ficha técnica española disponible en este pack |
| Nueva Indicación Predicha | Trastorno primario de liberación plaquetaria (primary release disorder of platelets) |
| Puntaje de Predicción TxGNN | 99,9976% (rank #146 entre las predicciones del modelo) |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de filgrastim en este Evidence Pack (dato marcado como bloqueante de alta severidad). Según la información conocida, filgrastim es un G-CSF recombinante que actúa sobre el receptor de G-CSF en los precursores mieloides, promoviendo la proliferación y diferenciación de precursores neutrofílicos, y movilizando células madre hematopoyéticas (HSC) hacia la sangre periférica.

El trastorno primario de liberación plaquetaria es una alteración de la función de los gránulos densos/alfa de las plaquetas, cuya vía fisiopatológica corresponde al eje de la trombopoyetina (TPO) y a la maquinaria de secreción plaquetaria — no a la vía del G-CSF. No existe conexión molecular conocida entre la estimulación de neutrófilos por G-CSF y la función secretora de las plaquetas.

En consecuencia, la puntuación elevada de TxGNN probablemente refleja proximidad en el espacio de embeddings del modelo (ambos contextos comparten el dominio "hematología / cuidado de soporte en trasplante de células madre") más que una relación mecanística real. Esta valoración es coherente con la evidencia clínica disponible: ningún ensayo identificado trata directamente este trastorno con filgrastim.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04047628](https://clinicaltrials.gov/study/NCT04047628) | Fase 3 | Reclutando | 156 | Trasplante autólogo de HSC vs. mejor terapia disponible en esclerosis múltiple recidivante resistente; filgrastim como soporte de movilización, no como tratamiento del trastorno plaquetario |
| [NCT02646098](https://clinicaltrials.gov/study/NCT02646098) | Fase 2 | Completado | 64 | Selección CD34+ vs. no selección en trasplante autólogo para linfoma de células del manto/DLBCL; sin relación con liberación plaquetaria |
| [NCT00245037](https://clinicaltrials.gov/study/NCT00245037) | Fase 1/2 | Completado | 147 | Trasplante alogénico no mieloablativo para neoplasias hematológicas con busulfán/fludarabina/ICT |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Fase 2 | Completado | 60 | Trasplante alogénico/singénico en sarcomas pediátricos de alto riesgo |
| [NCT00076752](https://clinicaltrials.gov/study/NCT00076752) | Fase 2 | Completado | 9 | Trasplante autólogo de HSC tras linfodepleción intensiva en lupus eritematoso sistémico grave |
| [NCT00923364](https://clinicaltrials.gov/study/NCT00923364) | Fase 2 | Completado | 19 | Trasplante de intensidad reducida en pacientes con mutaciones GATA2 |
| [NCT01503918](https://clinicaltrials.gov/study/NCT01503918) | Fase 2 | Completado | 124 | Profilaxis antiviral para reactivación de CMV en pacientes críticos inmunocompetentes; sin relación con plaquetas |
| [NCT01335932](https://clinicaltrials.gov/study/NCT01335932) | Fase 2 | Completado | 160 | Ganciclovir/valganciclovir para prevención de reactivación de CMV en lesión pulmonar aguda; sin relación con el trastorno plaquetario |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Fase 2 | Reclutando | 358 | Profilaxis de enfermedad de injerto contra huésped post-trasplante con ciclofosfamida en donante no emparentado |
| [NCT05436418](https://clinicaltrials.gov/study/NCT05436418) | Fase 1/2 | Reclutando | 260 | Dosis mínima eficaz de ciclofosfamida post-trasplante combinada con sirolimus/micofenolato para profilaxis de EICH |

**Nota:** Los ensayos evaluados como grado "C" de relevancia (p. ej. NCT02646098) fueron valorados explícitamente como no relacionados con el trastorno plaquetario; el resto permanece pendiente de evaluación de relevancia. Ninguno de los 14 ensayos identificados constituye un estudio terapéutico dirigido a este trastorno — filgrastim aparece únicamente como agente de movilización/soporte en el contexto de trasplante de células madre.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29770133](https://pubmed.ncbi.nlm.nih.gov/29770133/) | 2018 | Revisión/Observacional | Frontiers in Immunology | La movilización de células madre de sangre periférica en donantes sanos mediante G-CSF causa movilización preferencial de subpoblaciones linfocitarias; no aborda la liberación plaquetaria |

---

## Información de Mercado en España

Filgrastim no está comercializado en España bajo este expediente (0 autorizaciones registradas en el pack de evidencia). No hay información de producto, forma farmacéutica ni indicación aprobada localmente disponible para citar.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se identificaron advertencias, contraindicaciones ni interacciones farmacológicas documentadas en las fuentes consultadas (TFDA, DDI); la ficha técnica de seguridad (DG001) está marcada como dato bloqueante pendiente.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe vínculo mecanístico conocido ni evidencia clínica directa que respalde el uso de filgrastim en el trastorno primario de liberación plaquetaria: los 14 ensayos identificados son estudios de trasplante de células madre donde filgrastim actúa como movilizador de soporte, y la única publicación relacionada tampoco aborda la función plaquetaria. El propio análisis mecanístico del pack de evidencia señala que la puntuación TxGNN probablemente es un artefacto de proximidad en el espacio de embeddings, no una señal biológica real.

**Para avanzar se necesita:**
- Ficha técnica/prospecto de TFDA con advertencias y contraindicaciones (dato bloqueante, DG001)
- Datos de mecanismo de acción (MOA) verificados vía DrugBank (DG002)
- Estudios preclínicos o mecanísticos que evalúen directamente el efecto de G-CSF sobre la secreción de gránulos plaquetarios
- Evaluación de si existe justificación para el registro/comercialización de filgrastim en España, dado que actualmente no está en el mercado
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

