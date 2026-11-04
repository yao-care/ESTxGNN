---
layout: default
title: Elbasvir
parent: Solo predicción del modelo (L5)
nav_order: 281
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-04
monitor_inn: "elbasvir"
predicted_indications: ["hepatitis B virus infection", "hepatitis E virus infection", "hepatitis A virus infection", "hepatitis, viral, animal", "Omsk hemorrhagic fever", "Kyasanur forest disease", "HIV infectious disease", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
description: "Elbasvir: nueva indicación predicha, infección por el virus de la hepatitis B (hepatitis B virus infection) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Elbasvir
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Elbasvir: infección por el virus de la hepatitis B (hepatitis B virus infection)
{: .text-alpha }

## Resumen en Una Frase

Elbasvir es un inhibidor de la proteína NS5A del virus de la hepatitis C, utilizado junto con grazoprevir en el tratamiento de la hepatitis C crónica.
El modelo TxGNN predice que podría ser efectivo para **infección por el virus de la hepatitis B (hepatitis B virus infection)**, pero ningún estudio evalúa elbasvir en hepatitis B, por lo que el nivel de evidencia es **L5** (solo predicción del modelo).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | infección por el virus de la hepatitis B (hepatitis B virus infection) |
| Puntaje de Predicción TxGNN | 0.9971 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Autorizado pero no comercializado (registros: 1) |
| Número de Autorizaciones | 1 (vigentes: 0) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Por la literatura revisada, elbasvir es un inhibidor de la proteína no estructural NS5A del virus de la hepatitis C (VHC), y se utiliza en combinación con grazoprevir, un inhibidor de la proteasa NS3/4A.

El virus de la hepatitis B (VHB) es, como el VHC, un virus con tropismo hepático, y esto probablemente explique la puntuación alta del modelo. Sin embargo, el VHB no tiene un homólogo de NS5A, por lo que no se ha establecido un vínculo mecanístico directo.

En resumen, la predicción debe considerarse una hipótesis. Los ensayos y las publicaciones disponibles se centran en el VHC y no estudian elbasvir en hepatitis B.

## Evidencia de Ensayos Clínicos

Los dos ensayos asociados a esta predicción son estudios en hepatitis C y no evalúan elbasvir en hepatitis B.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02940496](https://clinicaltrials.gov/study/NCT02940496) | Fase 2 | Completado | 15 | Pembrolizumab como segunda línea en carcinoma hepatocelular, con sujetos VHC positivos y negativos; no evalúa elbasvir |
| [NCT02115321](https://clinicaltrials.gov/study/NCT02115321) | Fase 2/3 | Completado | 40 | Grazoprevir + elbasvir en hepatitis C crónica con cirrosis avanzada (Child-Pugh B); solo evidencia en VHC |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [26904396](https://pubmed.ncbi.nlm.nih.gov/26904396/) | 2016 | Revisión | Acta Pharmaceutica Sinica B | Revisión de antivirales de acción directa contra el VHC (proteasa NS3/4A, polimerasa NS5B y NS5A) |
| [25529080](https://pubmed.ncbi.nlm.nih.gov/25529080/) | 2015 | Revisión | Liver International | Revisión general sobre la erradicación del VHC y la curación del VHB; sin datos de elbasvir en VHB |
| [34902265](https://pubmed.ncbi.nlm.nih.gov/34902265/) | 2022 | Cohorte (ensayo fase 4 de un solo brazo) | Antimicrobial Agents and Chemotherapy | Grazoprevir/elbasvir en receptores de trasplante hepático o renal con VHC genotipo 1b |
| [32039536](https://pubmed.ncbi.nlm.nih.gov/32039536/) | 2020 | Estudio de práctica real | Journal of Viral Hepatitis | Seguridad hepática y renal de elbasvir/grazoprevir en pacientes con VHC genotipo 1 |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Revisión | Clinical Pharmacokinetics | Consideraciones farmacocinéticas y farmacodinámicas de los tratamientos para el VHC |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1161119001 | ZEPATIER 50MG/100MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | No disponible en los datos compilados |

## Citotoxicidad

No aplica: elbasvir es un antiviral y no un fármaco antineoplásico, por lo que se omite esta sección.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 15 interacciones. La de mayor gravedad es con **ozanimod** (Mayor). Las demás son de nivel Moderado: metreleptina, betrixabán, dicumarol, lusutrombopag, warfarina, griseofulvina, elagolix, somatrem, somatotropina, alpelisib, aminoglutetimida, binimetinib, ivosidenib y talazoparib.

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ningún estudio evalúa elbasvir en hepatitis B: los ensayos y publicaciones disponibles se limitan al VHC, y el VHB carece de una diana equivalente a NS5A. La predicción se apoya únicamente en el modelo (L5).

**Para avanzar se necesita:**
- Datos de mecanismo de acción de elbasvir y una justificación biológica de su posible actividad frente al VHB
- Estudios preclínicos (in vitro) de actividad antiviral de elbasvir contra el VHB
- Información de seguridad del prospecto (advertencias y contraindicaciones)
- Solo si los estudios preclínicos son favorables, valorar ensayos clínicos específicos en hepatitis B

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

