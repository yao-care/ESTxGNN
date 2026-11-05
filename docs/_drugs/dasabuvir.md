---
layout: default
title: Dasabuvir
parent: Solo predicción del modelo (L5)
nav_order: 224
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-05
monitor_inn: "DASABUVIR"
predicted_indications: ["hepatitis B virus infection", "hepatitis E virus infection", "hepatitis A virus infection", "hepatitis, viral, animal", "Omsk hemorrhagic fever"]
description: "Dasabuvir: nueva indicación predicha, infección por el virus de la hepatitis B (hepatitis B virus infection) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Dasabuvir
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Dasabuvir: infección por el virus de la hepatitis B (hepatitis B virus infection)
{: .text-alpha }

## Resumen en Una Frase

Dasabuvir es un inhibidor no nucleosídico de la ARN polimerasa NS5B del virus de la hepatitis C, utilizado dentro de regímenes antivirales de acción directa.
El modelo TxGNN predice que podría ser efectivo para **infección por el virus de la hepatitis B (hepatitis B virus infection)**, pero el nivel de evidencia es **L5**: ningún estudio evalúa dasabuvir como tratamiento de la hepatitis B. Los 2 ensayos clínicos y las publicaciones disponibles tratan la hepatitis C o describen el riesgo de reactivación del VHB.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | infección por el virus de la hepatitis B (hepatitis B virus infection) |
| Puntaje de Predicción TxGNN | 0.9937 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado (registros anulados: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 0) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Dasabuvir inhibe la ARN polimerasa dependiente de ARN NS5B del VHC mediante un mecanismo no nucleosídico. No se dispone de datos detallados adicionales sobre el mecanismo de acción en los datos compilados para este informe.

El VHB se replica mediante una transcriptasa inversa (ADN polimerasa), por lo que no existe homología directa con la diana de dasabuvir. Los ensayos que incluyen a pacientes coinfectados por VHC/VHB tratan el VHC y no demuestran actividad contra el VHB.

El puntaje alto del modelo probablemente refleja la proximidad en la red de relaciones biológicas de las hepatitis virales, y no un mecanismo antiviral directo. Además, la literatura señala un riesgo de reactivación del VHB durante el tratamiento con antivirales de acción directa en pacientes coinfectados, lo que es una preocupación de seguridad y no un beneficio terapéutico.

## Evidencia de Ensayos Clínicos

Los siguientes ensayos incluyen población coinfectada, pero ninguno evalúa a dasabuvir como tratamiento de la hepatitis B.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Fase 2/3 | Completado | 23 | Antivirales de acción directa en coinfección VHC/VHB; evalúa incidencia y factores de reactivación del VHB. El objetivo terapéutico es el VHC |
| [NCT02219477](https://clinicaltrials.gov/study/NCT02219477) | Fase 3 | Completado | 36 | Ombitasvir/paritaprevir/ritonavir + dasabuvir con ribavirina en hepatitis C con cirrosis descompensada; seguridad y RVS12, sin evidencia de efecto anti-VHB |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29397016](https://pubmed.ncbi.nlm.nih.gov/29397016/) | 2018 | Cohorte | Journal of Viral Hepatitis | Riesgo de reactivación del VHB en pacientes coinfectados VHB/VHC con cirrosis compensada tratados con ombitasvir, paritaprevir/r + dasabuvir + ribavirina |
| [28416221](https://pubmed.ncbi.nlm.nih.gov/28416221/) | 2017 | ECA | The Lancet Gastroenterology & Hepatology | Régimen de 8 semanas con ombitasvir, paritaprevir, ritonavir y dasabuvir en hepatitis C genotipo 1b sin cirrosis (ensayo de fase 3b de un solo brazo) |
| [28762541](https://pubmed.ncbi.nlm.nih.gov/28762541/) | 2018 | Cohorte | Journal of Gastroenterology and Hepatology | Efectividad y seguridad en la vida real del régimen PrOD en hepatitis C genotipo 1b en Taiwán |
| [25529080](https://pubmed.ncbi.nlm.nih.gov/25529080/) | 2015 | Revisión | Liver International | Revisión sobre la erradicación del VHC y la curación del VHB |

## Información de Mercado en Espana

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 114983001 | EXVIERA 250 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | No disponible en los datos compilados |

La única autorización registrada figura como cancelada.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificó 1 interacción de nivel moderado, con abiraterona.
- **Riesgo de reactivación del VHB**: la literatura señala reactivación del virus de la hepatitis B durante el tratamiento con antivirales de acción directa en pacientes coinfectados.

Para el resto de la información de seguridad, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ningún estudio evalúa dasabuvir como tratamiento de la hepatitis B; los estudios disponibles tratan la hepatitis C y señalan un riesgo de reactivación del VHB. El mecanismo (inhibidor de la polimerasa NS5B del VHC) no tiene una diana homóloga en el VHB, por lo que la predicción se apoya solo en el modelo (nivel L5).

**Para avanzar se necesita:**
- Validación in vitro de actividad anti-VHB de dasabuvir
- Datos detallados del mecanismo de acción y de su posible interacción con la replicación del VHB
- Evaluación de seguridad sobre la reactivación del VHB en pacientes coinfectados
- Información de advertencias y contraindicaciones del prospecto

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

