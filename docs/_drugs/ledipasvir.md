---
layout: default
title: Ledipasvir
parent: Evidencia alta (L1-L2)
nav_order: 457
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-14
description: "Ledipasvir: nueva indicación predicha, Infección por virus de la hepatitis B (nivel de evidencia L5). Indicación original: Infección crónica por el virus de la hepatitis C (según la base de co…"
monitor_inn: "ledipasvir"
predicted_indications: ["hepatitis B virus infection", "hepatitis E virus infection", "hepatitis, viral, animal", "hepatitis A virus infection", "Omsk hemorrhagic fever", "Kyasanur forest disease", "chronic hepatitis B virus infection", "HIV infectious disease", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection"]
---

# Ledipasvir
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **10** 
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

## Ledipasvir: De Infección por Hepatitis C a Infección por Virus de la Hepatitis B
{: .text-alpha }

## Resumen en Una Frase

Ledipasvir es un inhibidor de la proteína NS5A del virus de la hepatitis C, comercializado en combinación con sofosbuvir (Harvoni) para el tratamiento de la infección crónica por hepatitis C.
El modelo TxGNN predice que podría ser efectivo para la **infección por virus de la hepatitis B**, pero la evidencia es limitada: **5 ensayos clínicos** (solo uno evalúa directamente la hepatitis B, es de fase 2, de un solo brazo y con 21 participantes) y **20 publicaciones**, muchas de las cuales describen sobre todo el riesgo de reactivación del VHB durante el tratamiento de la hepatitis C.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección crónica por el virus de la hepatitis C (según la base de conocimiento del modelo; el texto de indicación autorizado no está disponible) |
| Nueva Indicación Predicha | Infección por virus de la hepatitis B |
| Puntaje de Predicción TxGNN | 0.9991 |
| Nivel de Evidencia | L2 (un ensayo de fase 2/3 completado, aunque centrado en coinfección VHC/VHB; el único estudio dirigido a VHB es de fase 2 de un solo brazo) |
| Estado de Mercado en España | Comercializado (registros vigentes: 1 de 1) |
| Número de Autorizaciones | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, ledipasvir actúa sobre la proteína NS5A del VHC y se administra junto con sofosbuvir (inhibidor de la polimerasa NS5B). Su eficacia en la hepatitis C está bien establecida.

Mecanísticamente, el vínculo con la hepatitis B es débil. NS5A no tiene homólogo conocido en el VHB, por lo que cualquier efecto sobre el VHB sería probablemente indirecto, por ejemplo a través de la supresión del VHC en pacientes coinfectados. El puntaje alto del modelo probablemente refleja la proximidad en la red de conocimiento entre fármacos de hepatitis virales, y no una actividad antiviral directa contra el VHB.

Un estudio de fase 2 sugiere una reducción modesta del HBsAg en pacientes con monoinfección por VHB, lo que genera una hipótesis de investigación. Sin embargo, varios estudios describen reactivación del VHB tras el tratamiento de la hepatitis C con antivirales de acción directa, lo que apunta más a un problema de seguridad que a un beneficio terapéutico.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Fase 2 | Completado | 21 | Ledipasvir/sofosbuvir durante 12 semanas en personas con infección por VHB; estudio abierto de un solo brazo, evalúa el descenso de HBsAg y ADN del VHB (relevancia directa, pero pequeño) |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Fase 2/3 | Completado | 23 | Antivirales de acción directa en coinfección crónica VHC/VHB; evalúa la incidencia y los factores de reactivación del VHB |
| [NCT02836925](https://clinicaltrials.gov/study/NCT02836925) | Fase 2 | Completado | 40 | Régimen sin interferón con ledipasvir/sofosbuvir en linfomas B indolentes asociados a VHC; datos específicos de VHB inciertos |
| [NCT03261349](https://clinicaltrials.gov/study/NCT03261349) | Fase 2 | Desconocido | 21 | Harvoni en linfoma no Hodgkin de células B asociado a VHC; relevancia para VHB poco clara |
| [NCT02768961](https://clinicaltrials.gov/study/NCT02768961) | Fase 4 | Completado | 64 | Programa de cribado y eliminación de hepatitis C en prisiones de Cantabria; no está diseñado para evaluar eficacia en VHB |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | Ensayo fase 2 abierto | J Med Virol | Ledipasvir/sofosbuvir 12 semanas en monoinfección por VHB; evalúa descenso de HBsAg y ADN del VHB |
| [29174546](https://pubmed.ncbi.nlm.nih.gov/29174546/) | 2018 | Estudio prospectivo | Gastroenterology | Eficacia y riesgos de ledipasvir/sofosbuvir para VHC en pacientes coinfectados con VHB |
| [34864948](https://pubmed.ncbi.nlm.nih.gov/34864948/) | 2022 | Cohorte | Clin Infect Dis | Reactivación del VHB durante el tratamiento y 108 semanas de seguimiento en Taiwán |
| [27367295](https://pubmed.ncbi.nlm.nih.gov/27367295/) | 2016 | Estudio piloto | Antivir Ther | Ledipasvir/sofosbuvir para suprimir el VHC en pacientes coinfectados con VHB |
| [29334502](https://pubmed.ncbi.nlm.nih.gov/29334502/) | 2018 | Cohorte | J Clin Gastroenterol | Riesgo de reactivación del VHB con ledipasvir/sofosbuvir |
| [33523503](https://pubmed.ncbi.nlm.nih.gov/33523503/) | 2021 | Cohorte | J Viral Hepat | Reactivación del VHB en pacientes con cáncer tratados con antivirales de acción directa |
| [28585404](https://pubmed.ncbi.nlm.nih.gov/28585404/) | 2017 | Cohorte | Hepatol Res | Frecuencia y factores asociados a la reactivación del VHB en una cohorte japonesa |
| [28249574](https://pubmed.ncbi.nlm.nih.gov/28249574/) | 2017 | Reporte de caso | BMC Infect Dis | Reactivación de infección oculta por VHB en paciente VIH/VHC tratado con sofosbuvir/ledipasvir |
| [25529080](https://pubmed.ncbi.nlm.nih.gov/25529080/) | 2015 | Revisión | Liver Int | Hacia la erradicación del VHC y la curación del VHB |
| [37254310](https://pubmed.ncbi.nlm.nih.gov/37254310/) | 2024 | Estudio in silico | J Biomol Struct Dyn | Cribado molecular de compuestos antivirales frente a la proteína HBx |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 114958001 | HARVONI 90 MG/400 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Reactivación del VHB**: múltiples cohortes y reportes de caso (Taiwán, Japón, EE. UU., Italia) describen reactivación del virus de la hepatitis B durante o tras el tratamiento de la hepatitis C con antivirales de acción directa, incluido ledipasvir/sofosbuvir. Es el principal riesgo de seguridad en la población objetivo.
- **Interacciones farmacológicas**: se identificaron 65 interacciones; las principales de nivel moderado incluyen:
  - Antiácidos: hidróxido de aluminio, carbonato de calcio, magaldrato, carbonato, hidróxido y óxido de magnesio.
  - Antagonistas H2: cimetidina, famotidina, nizatidina.
  - Inhibidores de la bomba de protones: omeprazol, esomeprazol, lansoprazol, dexlansoprazol, pantoprazol.
  - Otros: eliglustat, linagliptina, loperamida, naldemedina.
  - De nivel leve: fidaxomicina y naloxegol.
- En pacientes VIH/VHC, las interacciones con antirretrovirales (en especial regímenes con tenofovir) son un aspecto práctico relevante.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El único estudio dirigido directamente a la hepatitis B es una prueba piloto de fase 2 de un solo brazo con 21 participantes. No existe un mecanismo directo plausible, ya que la inhibición de NS5A no actúa sobre la replicación del VHB, y la literatura destaca la reactivación del VHB como riesgo. El puntaje alto de TxGNN probablemente refleja proximidad en la red entre fármacos de hepatitis virales.

**Para avanzar se necesita:**
- Revisar con prioridad la seguridad (reactivación y brotes de VHB) antes de plantear cualquier pregunta de eficacia.
- Obtener el prospecto de la AEMPS con advertencias y contraindicaciones, hoy no disponible en los datos compilados.
- Obtener datos del mecanismo de acción (p. ej., desde DrugBank) para analizar el vínculo mecanístico.
- Estudios controlados y de mayor tamaño en monoinfección por VHB que confirmen o descarten el efecto sobre el HBsAg.
- Confirmar el texto de la indicación autorizada en España.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

