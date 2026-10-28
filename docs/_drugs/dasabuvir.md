---
layout: default
title: Dasabuvir
parent: Evidencia moderada (L3-L4)
nav_order: 224
evidence_level: L3
indication_count: 5
last_modified_at: 2026-10-28
description: "Dasabuvir: nueva indicación predicha, Infección por virus de la hepatitis B (nivel de evidencia L3). Indicación original: Infección crónica por virus de la hepatitis C (según la base de conoc…"
monitor_inn: "DASABUVIR"
predicted_indications: ["hepatitis B virus infection", "hepatitis E virus infection", "hepatitis A virus infection", "hepatitis, viral, animal", "Omsk hemorrhagic fever"]
---

# Dasabuvir
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **5** 
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

## Dasabuvir: De Infección por Virus de la Hepatitis C a Infección por Virus de la Hepatitis B
{: .text-alpha }

## Resumen en Una Frase

Dasabuvir es un inhibidor no nucleosídico de la polimerasa NS5B del virus de la hepatitis C (VHC), utilizado originalmente para el tratamiento de la infección crónica por VHC.
El modelo TxGNN predice que podría ser efectivo para la **infección por el virus de la hepatitis B (VHB)**, pero los **2 ensayos clínicos** y las publicaciones disponibles se refieren a pacientes coinfectados y al tratamiento del VHC, sin demostrar actividad anti-VHB.
La evidencia real es limitada y la predicción se apoya sobre todo en la proximidad en la red biológica del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección crónica por virus de la hepatitis C (según la base de conocimiento del modelo; el texto de indicación autorizado no está disponible) |
| Nueva Indicación Predicha | Infección por virus de la hepatitis B |
| Puntaje de Predicción TxGNN | 0.9937 |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | No comercializado (registros anulados: 1 de 1) |
| Número de Autorizaciones | 1 (vigentes: 0) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, dasabuvir es un inhibidor no nucleosídico de la ARN polimerasa dependiente de ARN NS5B del VHC y se emplea dentro de un régimen combinado con ombitasvir, paritaprevir y ritonavir. Su eficacia en la hepatitis C está bien documentada en numerosos ensayos de fase 3.

La hepatitis C y la hepatitis B son ambas infecciones virales hepáticas, y es frecuente que coexistan en un mismo paciente. Sin embargo, el VHB se replica mediante transcripción inversa (ADN polimerasa), por lo que **no existe homología directa con la diana de dasabuvir**. La puntuación alta del modelo probablemente refleja la proximidad en la red de conocimiento por biología hepática compartida, y no un mecanismo antiviral directo.

Los ensayos y la literatura sobre pacientes coinfectados VHC/VHB muestran seguridad y eficacia frente al VHC, pero no actividad anti-VHB. Además, se ha señalado el riesgo de **reactivación del VHB** durante el tratamiento con antivirales de acción directa, lo que constituye una preocupación de seguridad y no un beneficio terapéutico.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Fase 2/3 | Completado | 23 | Estudio prospectivo sobre incidencia y factores de reactivación del VHB durante el tratamiento antiviral directo del VHC en coinfectados VHC/VHB. El objetivo terapéutico es el VHC. |
| [NCT02219477](https://clinicaltrials.gov/study/NCT02219477) | Fase 3 | Completado | 36 | Ombitasvir/paritaprevir/ritonavir + dasabuvir con ribavirina en VHC genotipo 1 con cirrosis descompensada (TURQUOISE-CPB). Datos de seguridad y RVS12 para VHC; sin evidencia de efecto anti-VHB. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28416221](https://pubmed.ncbi.nlm.nih.gov/28416221/) | 2017 | ECA (fase 3b, un solo brazo) | Lancet Gastroenterol Hepatol | Régimen de 8 semanas de ombitasvir/paritaprevir/ritonavir + dasabuvir sin ribavirina en VHC genotipo 1b sin cirrosis (GARNET). |
| [29397016](https://pubmed.ncbi.nlm.nih.gov/29397016/) | 2018 | Cohorte | J Viral Hepat | Riesgo de reactivación del VHB en pacientes coinfectados VHB/VHC con cirrosis compensada tratados con el régimen que incluye dasabuvir. |
| [28762541](https://pubmed.ncbi.nlm.nih.gov/28762541/) | 2018 | Cohorte | J Gastroenterol Hepatol | Efectividad y seguridad en el mundo real del régimen PrOD en VHC genotipo 1b en Taiwán. |
| [25529080](https://pubmed.ncbi.nlm.nih.gov/25529080/) | 2015 | Revisión | Liver Int | Hacia la erradicación del VHC y la curación del VHB. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 114983001 | EXVIERA 250 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | No disponible en los datos compilados |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificó 1 interacción de nivel moderado, con **abiraterona** (fuente: DDInter).
- **Reactivación del VHB**: la literatura señala riesgo de reactivación del VHB durante el tratamiento con antivirales de acción directa en pacientes coinfectados, un aspecto relevante para esta indicación predicha.

Para el resto de la información de seguridad, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Los ensayos disponibles se centran en el tratamiento del VHC en pacientes coinfectados y no demuestran actividad anti-VHB. Además, no hay homología entre la diana de dasabuvir (NS5B del VHC) y la polimerasa del VHB, por lo que la predicción responde más a proximidad en la red que a un mecanismo plausible.

**Para avanzar se necesita:**
- Validación in vitro de actividad anti-VHB (cultivos celulares, replicación del VHB).
- Datos detallados del mecanismo de acción y análisis de la relación mecanística con el VHB.
- Revisión del prospecto de la AEMPS para advertencias y contraindicaciones.
- Evaluación del riesgo de reactivación del VHB en pacientes coinfectados.

---

### Otras indicaciones predichas (referencia breve)

| Indicación | Puntaje TxGNN | Nivel de Evidencia | Recomendación | Comentario |
|---|---|---|---|---|
| Infección por virus de la hepatitis E | 0.9907 | L5 | Hold | Solo predicción; sin ensayos ni literatura. Su polimerasa es estructuralmente distinta de NS5B. |
| Infección por virus de la hepatitis A | 0.9905 | L4 | Hold | Los ensayos listados son estudios de VHC, asociados por artefactos de coincidencia de términos; no respaldan actividad frente al VHA. |
| Hepatitis viral animal | 0.9905 | L4 | Hold | Solo evidencia estructural preclínica indirecta (NS5B de hepacivirus equinos); término demasiado inespecífico. |
| Fiebre hemorrágica de Omsk | 0.9903 | L5 | Hold | Solo predicción; el sitio alostérico de dasabuvir está poco conservado entre flavivirus. |
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

