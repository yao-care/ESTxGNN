---
layout: default
title: Modafinil
parent: Evidencia moderada (L3-L4)
nav_order: 539
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-14
description: "Modafinil: nueva indicación predicha, Insomnio (nivel de evidencia L4). Indicación original: Narcolepsia (según las indicaciones del grafo de conocimiento"
monitor_inn: "modafinil"
predicted_indications: ["insomnia (disease)"]
---

# Modafinil
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **1** 
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

# Modafinilo: De Narcolepsia a Insomnio

## Resumen en Una Frase

Modafinilo es un fármaco promotor de la vigilia, utilizado originalmente para tratar la narcolepsia (con y sin cataplejía) y otros trastornos asociados a somnolencia excesiva.
El modelo TxGNN predice que podría ser efectivo para **Insomnio**, aunque solo **2 ensayos clínicos** (uno terminado con 2 participantes y otro completado con 40) y publicaciones mayormente indirectas respaldan esta dirección, por lo que la evidencia es débil.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Narcolepsia (según las indicaciones del grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.85% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 7 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento general, modafinilo es un agente promotor de la vigilia que se entiende que actúa mediante la inhibición del transportador de dopamina y efectos sobre los circuitos que favorecen la vigilia. Su eficacia en la narcolepsia y en la somnolencia excesiva está bien establecida.

Sin embargo, la predicción resulta **mecanísticamente poco intuitiva**. El insomnio se caracteriza por dificultad para iniciar o mantener el sueño, mientras que modafinilo busca reducir la somnolencia diurna. El puntaje alto de TxGNN (0.998) probablemente refleja la proximidad en la red de conocimiento con trastornos del sueño y la vigilia como la narcolepsia, más que un vínculo terapéutico real.

La evidencia disponible se refiere sobre todo a alteraciones del sueño/vigilia y somnolencia diurna en contextos comórbidos (adultos mayores, enfermedad de Parkinson, trastornos neurológicos, trastorno por trabajo a turnos), y no al insomnio en sí. Un posible uso sería el de mejorar el funcionamiento diurno en personas con insomnio, algo que debe verificarse.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00124384](https://clinicaltrials.gov/study/NCT00124384) | Fase 4 | Completado | 40 | Efectos de modafinilo, solo o con terapia cognitivo-conductual para el insomnio (TCC-I), sobre el funcionamiento diurno y la gravedad del insomnio primario. No se reportan resultados; relevancia moderada (B). |
| [NCT00626210](https://clinicaltrials.gov/study/NCT00626210) | Fase 4 | Terminado | 2 | Alteraciones del sueño/vigilia en adultos mayores. Terminado con solo 2 participantes; no permite extraer datos de eficacia ni seguridad (relevancia C). |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [24312590](https://pubmed.ncbi.nlm.nih.gov/24312590/) | 2013 | Revisión sistemática/Metaanálisis | PloS one | Eficacia y seguridad de modafinilo sobre la fatiga y la somnolencia diurna asociadas a trastornos neurológicos; resultados previos inconsistentes. |
| [27010071](https://pubmed.ncbi.nlm.nih.gov/27010071/) | 2016 | Revisión sistemática/Metaanálisis | Parkinsonism & Related Disorders | Intervenciones farmacológicas para la somnolencia y los trastornos del sueño en Parkinson; pocos ensayos realizados. |
| [18729534](https://pubmed.ncbi.nlm.nih.gov/18729534/) | 2008 | Revisión | Drugs | Revisión basada en evidencia de usos aprobados y en investigación de modafinilo, a partir de ensayos aleatorizados controlados con placebo. |
| [22021174](https://pubmed.ncbi.nlm.nih.gov/22021174/) | 2011 | Revisión | Movement Disorders | Revisión de la MDS sobre tratamientos de síntomas no motores del Parkinson. |
| [39535843](https://pubmed.ncbi.nlm.nih.gov/39535843/) | 2024 | Revisión | Expert Opinion on Pharmacotherapy | Manejo farmacológico y no farmacológico de las alteraciones del sueño en Parkinson. |
| [24272458](https://pubmed.ncbi.nlm.nih.gov/24272458/) | 2014 | Revisión | Neurotherapeutics | Tratamiento de los trastornos del sueño en Parkinson; los tratamientos óptimos para el insomnio aún no están determinados. |
| [17181377](https://pubmed.ncbi.nlm.nih.gov/17181377/) | 2006 | Revisión | Drugs | Carga y manejo del trastorno del sueño por trabajo a turnos. |
| [21904092](https://pubmed.ncbi.nlm.nih.gov/21904092/) | 2011 | Revisión | Postgraduate Medicine | Teorías y terapias emergentes para el trastorno por trabajo a turnos (somnolencia o insomnio). |
| [24138359](https://pubmed.ncbi.nlm.nih.gov/24138359/) | 2013 | Revisión | Medical Journal of Australia | Pérdida de sueño y alteración circadiana en el trabajo a turnos: carga para la salud y manejo. |
| [17060310](https://pubmed.ncbi.nlm.nih.gov/17060310/) | 2006 | Serie de casos | American Journal of Hospice & Palliative Care | Modafinilo reduce la fatiga en la enfermedad de Charcot-Marie-Tooth tipo 1A. |

Ninguna de estas publicaciones demuestra beneficio de modafinilo en el insomnio como tal.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 80929 | MODAFINILO TARBIS 100 mg COMPRIMIDOS EFG | Comprimido | No disponible en los datos compilados |
| 75919 | MODAFINILO AUROVITAS 100 MG COMPRIMIDOS EFG | Comprimido | No disponible en los datos compilados |
| 72187 | MODAFINILO MYLAN 100 mg COMPRIMIDOS EFG | Comprimido | No disponible en los datos compilados |
| 61540 | MODIODAL 100 mg COMPRIMIDOS | Comprimido | No disponible en los datos compilados |
| 84141 | MODAFINILO ARISTO 100 MG COMPRIMIDOS EFG | Comprimido | No disponible en los datos compilados |

Hay 7 autorizaciones vigentes en total (todas de principio activo único); se muestran las 5 principales.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): hipertensión, insuficiencia hepática, trastornos de ansiedad, trastornos psicóticos y otros trastornos mentales (esquizoafectivo, esquizofreniforme, distimia, neurótico), abuso/dependencia de sustancias, síndrome coronario agudo, infarto de miocardio, isquemia miocárdica, enfermedad arterial coronaria, prolapso de la válvula mitral y síndrome de taquicardia postural ortostática.
- **Interacciones farmacológicas**: se identificaron 249 interacciones. Entre las de nivel moderado figuran omeprazol, esomeprazol, rabeprazol, dexametasona, eliglustat, linagliptina y cisaprida. Entre las de nivel menor: hidrocortisona, pioglitazona, aprepitant, cimetidina, claritromicina y otras.

No se dispone de advertencias ni contraindicaciones del prospecto; consultar el prospecto de la AEMPS para la información de seguridad oficial.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia se limita a nivel L4: solo hay un ensayo de Fase 4 completado (n=40, sin resultados reportados) y otro terminado con 2 participantes. Además, el mecanismo de un fármaco promotor de la vigilia es contrario al objetivo terapéutico del insomnio, y el puntaje alto de TxGNN probablemente refleja proximidad con la narcolepsia.

**Para avanzar se necesita:**
- Obtener y analizar los resultados de NCT00124384 y verificar su población y criterios de valoración.
- Datos del mecanismo de acción (MOA) desde DrugBank para analizar el vínculo mecanístico.
- Advertencias y contraindicaciones del prospecto de la AEMPS (necesarias antes del cribado de seguridad), dado el perfil cardiovascular y psiquiátrico señalado.
- Definir si la hipótesis es tratar el insomnio o mejorar el funcionamiento diurno en pacientes con insomnio, y evaluarla en ensayos controlados.
- Revisar el riesgo de interacciones en una población que a menudo recibe varios fármacos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

