---
layout: default
title: Elbasvir
parent: Evidencia moderada (L3-L4)
nav_order: 281
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Elbasvir: nueva indicación predicha, Infección por el virus de la hepatitis B (nivel de evidencia L4). Indicación original: Infección crónica por el virus de la hepatitis C (según el grafo de c…"
---

# Elbasvir
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

# Elbasvir: De Infección por el Virus de la Hepatitis C a Infección por el Virus de la Hepatitis B

## Resumen en Una Frase

Elbasvir es un inhibidor de la proteína NS5A del virus de la hepatitis C, utilizado originalmente para el tratamiento de la infección crónica por hepatitis C (en combinación con grazoprevir).
El modelo TxGNN predice que podría ser efectivo para **infección por el virus de la hepatitis B**, pero los **2 ensayos clínicos** y las publicaciones asociadas son en realidad estudios sobre hepatitis C, por lo que la evidencia directa para esta nueva indicación es prácticamente inexistente.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección crónica por el virus de la hepatitis C (según el grafo de conocimiento; el texto de indicación autorizado no está disponible) |
| Nueva Indicación Predicha | Infección por el virus de la hepatitis B |
| Puntaje de Predicción TxGNN | 99.71% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, elbasvir es un inhibidor de la proteína NS5A del VHC y se utiliza combinado con grazoprevir (inhibidor de la proteasa NS3/4A). Su eficacia en hepatitis C está bien establecida.

La relación con la hepatitis B es débil mecanísticamente: el VHB no tiene un homólogo de NS5A, por lo que no existe un vínculo mecanístico directo. El puntaje alto del modelo probablemente refleja características compartidas en la red de virus hepatotropos (ambos infectan el hígado y se tratan con antivirales), y no una actividad antiviral demostrada contra el VHB.

Por ello, esta predicción debe considerarse una hipótesis generada por el modelo y no una indicación respaldada por evidencia.

**Otras predicciones del modelo (todas con nivel L4-L5):**
- **Hepatitis E** (99.66%): la única con una señal mecanística plausible. Un estudio in vitro de 2026 (PMID 42347219) indica que elbasvir inhibe la internalización del VHE y, combinado con ribavirina, logra supresión viral sostenida. Es evidencia preclínica, sin ensayos clínicos.
- **Hepatitis A** (99.65%): los 40 ensayos listados son de hepatitis C y no aportan evidencia para VHA, aunque algunos sean de Fase 3.
- **Infección por VIH** (99.61%): los ensayos son de pacientes coinfectados VIH/VHC tratados por la hepatitis C, no por el VIH. El elevado número de ensayos es un artefacto de la coinfección.
- **Hepatitis viral animal, fiebre hemorrágica de Omsk, enfermedad del bosque de Kyasanur, síndrome de inmunodeficiencia adquirida felina, infección por virus de inmunodeficiencia símica y un trastorno del neurodesarrollo raro:** solo predicción del modelo, sin evidencia que los respalde o con vínculos mecanísticos no plausibles.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02115321](https://clinicaltrials.gov/study/NCT02115321) | Fase 2/3 | Completado | 40 | Grazoprevir + elbasvir en hepatitis C crónica con cirrosis avanzada e insuficiencia hepática Child-Pugh B. Solo evidencia en VHC, sin criterio de valoración para VHB |
| [NCT02940496](https://clinicaltrials.gov/study/NCT02940496) | Fase 2 | Completado | 15 | Pembrolizumab en carcinoma hepatocelular avanzado, en pacientes VHC positivos y negativos. No evalúa elbasvir ni VHB |

Ninguno de estos ensayos evalúa elbasvir en hepatitis B.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [25529080](https://pubmed.ncbi.nlm.nih.gov/25529080/) | 2015 | Revisión | Liver International | Revisión general sobre la erradicación del VHC y la curación del VHB; no evalúa elbasvir en VHB |
| [26904396](https://pubmed.ncbi.nlm.nih.gov/26904396/) | 2016 | Revisión | Acta Pharmaceutica Sinica B | Revisión de antivirales de acción directa contra el VHC |
| [34902265](https://pubmed.ncbi.nlm.nih.gov/34902265/) | 2022 | Cohorte (Fase 4, un solo brazo) | Antimicrobial Agents and Chemotherapy | Grazoprevir/elbasvir en receptores de trasplante hepático o renal con VHC genotipo 1b |
| [32039536](https://pubmed.ncbi.nlm.nih.gov/32039536/) | 2020 | Estudio de mundo real | Journal of Viral Hepatitis | Experiencia en Taiwán con elbasvir/grazoprevir, centrada en efectos adversos hepáticos y renales |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Revisión | Clinical Pharmacokinetics | Consideraciones farmacocinéticas y farmacodinámicas de la terapia de hepatitis C |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) | 2025 | Estudio retrospectivo | Klinicka Mikrobiologie a Infekcni Lekarstvi | Tratamiento antiviral de hepatitis B y C en niños en Ostrava |

La literatura se centra en la hepatitis C. No se identificaron estudios de elbasvir en hepatitis B.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1161119001 | ZEPATIER 50MG/100MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | No disponible en los datos compilados |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** se identificaron 15 interacciones, 14 de nivel moderado y 1 de nivel mayor. La de nivel **mayor** es con **ozanimod**. Entre las de nivel moderado destacan **warfarina**, **dicumarol**, **betrixabán** (anticoagulantes), **lusutrombopag**, **griseofulvina**, **elagolix**, **alpelisib**, **aminoglutetimida**, **binimetinib**, **ivosidenib**, **talazoparib**, **metreleptina**, **somatrem** y **somatotropina**.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para hepatitis B se basa solo en el modelo: no hay vínculo mecanístico (el VHB carece de NS5A) y los ensayos y publicaciones son de hepatitis C. Entre las indicaciones predichas, la hepatitis E es la que tiene una hipótesis más plausible, aunque solo con evidencia in vitro.

**Para avanzar se necesita:**
- Estudios in vitro de actividad de elbasvir frente al VHB
- Priorizar la validación preclínica adicional en hepatitis E (PMID 42347219), incluyendo modelos in vivo
- Datos del mecanismo de acción detallado
- Texto de indicaciones y advertencias/contraindicaciones del prospecto de la AEMPS
- Evaluación de las interacciones, en particular con ozanimod, antes de cualquier ensayo
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

