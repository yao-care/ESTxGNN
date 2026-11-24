---
layout: default
title: Meropenem
parent: Solo predicción del modelo (L5)
nav_order: 507
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-24
monitor_inn: "MEROPENEM"
predicted_indications: ["bacterial arthritis", "epiglottitis", "laryngitis", "paratyphoid fever", "Lyme disease", "gonococcal urethritis", "Ureaplasma urethritis"]
description: "Meropenem: nueva indicación predicha, artritis bacteriana (bacterial arthritis) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: al menos 20"
---

# Meropenem
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

## Meropenem: artritis bacteriana (bacterial arthritis)
{: .text-alpha }

## Resumen en Una Frase

Meropenem es un antibiótico carbapenémico de amplio espectro, utilizado en infecciones bacterianas graves.
El modelo TxGNN predice que podría ser efectivo para **artritis bacteriana (bacterial arthritis)**, pero actualmente no hay ensayos clínicos registrados y solo hay **20 publicaciones** recuperadas, casi todas informes de casos, estudios de sensibilidad o farmacocinética, sin estudios que evalúen directamente la eficacia de meropenem en esta enfermedad.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | artritis bacteriana (bacterial arthritis) |
| Puntaje de Predicción TxGNN | 0.9992 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 6; autorizadas no comercializadas: 7; revocadas o suspendidas: 7) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Meropenem (traducción no oficial): «El meropenem es un fármaco antibacteriano. […] La actividad bactericida del meropenem se debe a la inhibición de la síntesis de la pared celular. El meropenem penetra la pared celular de la mayoría de las bacterias grampositivas y gramnegativas para unirse a sus dianas, las proteínas de unión a penicilina (PBP).» Texto original en inglés: "Meropenem is an antibacterial drug. […] The bactericidal activity of meropenem results from the inhibition of cell wall synthesis. Meropenem penetrates the cell wall of most gram-positive and gram-negative bacteria to bind penicillin-binding-protein (PBP) targets." ([DailyMed: meropenem prescribing information, Civica, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b0075b72-c3cc-f844-e053-2a95a90a417f), versión del 2026-11-02; consultado el 2026-11-19). Según la información conocida, meropenem es un carbapenem que inhibe la síntesis de la pared celular bacteriana al unirse a las proteínas fijadoras de penicilina, con actividad frente a bacterias Gram-negativas y Gram-positivas sensibles.

Las infecciones de huesos y articulaciones están causadas por bacterias que pueden ser sensibles a este tipo de antibiótico. Por ello, desde el punto de vista mecanístico, la predicción es biológicamente plausible.

Sin embargo, la literatura recuperada consiste sobre todo en estudios farmacocinéticos, informes de casos (por ejemplo, artritis séptica por *Klebsiella pneumoniae* productora de BLEE tratada con meropenem y amikacina), cohortes retrospectivas de melioidosis osteoarticular y trabajos que no son pertinentes (como un modelo murino de espondiloartritis). Ninguno estudia directamente la eficacia de meropenem en artritis bacteriana, por lo que el nivel de evidencia se limita a L5.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Revisión | Int J Antimicrob Agents | Uso fuera de indicación frente a recomendaciones formales de antibióticos en infecciones por bacterias multirresistentes |
| [35146367](https://pubmed.ncbi.nlm.nih.gov/35146367/) | 2021 | Cohorte retrospectiva | Le Infezioni in Medicina | Caracterización de pacientes con melioidosis osteoarticular |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Cohorte | Clin Lab | Distribución de patógenos y resistencia en infecciones óseas y articulares en niños pequeños |
| [39489417](https://pubmed.ncbi.nlm.nih.gov/39489417/) | 2024 | Revisión retrospectiva | Indian J Med Microbiol | 22 casos de melioidosis musculoesquelética; todos los aislados sensibles a meropenem |
| [39681779](https://pubmed.ncbi.nlm.nih.gov/39681779/) | 2025 | Estudio farmacocinético | Clin Pharmacokinet | Farmacocinética poblacional de meropenem en adultos y dosificación óptima |
| [17433752](https://pubmed.ncbi.nlm.nih.gov/17433752/) | 2007 | Informe de casos | Joint Bone Spine | Dos casos de artritis séptica por *Klebsiella pneumoniae* BLEE tratados con meropenem y amikacina más lavado artroscópico |
| [39380073](https://pubmed.ncbi.nlm.nih.gov/39380073/) | 2024 | Informe de caso | J Med Case Rep | Melioidosis diseminada con artritis séptica, mal diagnosticada inicialmente |
| [37713001](https://pubmed.ncbi.nlm.nih.gov/37713001/) | 2024 | Antibiograma | Eur J Orthop Surg Traumatol | Antibiograma para tratamiento empírico de infecciones ortopédicas no espinales |
| [33857030](https://pubmed.ncbi.nlm.nih.gov/33857030/) | 2021 | Estudio in vitro | J Bone Joint Surg Am | Estabilidad térmica y elución de meropenem y otros antibióticos en cemento óseo PMMA |
| [38375100](https://pubmed.ncbi.nlm.nih.gov/38375100/) | 2024 | Informe de caso | Infect Drug Resist | Meningitis supurativa con artritis por *Streptococcus suis* |

## Información de Mercado en España

Meropenem figura como comercializado en España, con 6 autorizaciones vigentes y 7 canceladas entre los registros disponibles; la lista puede ser parcial.

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 74304 | MEROPENEM AUROVIT 1000 MG POLVO PARA SOLUCION INYECTABLE Y PARA PERFUSION EFG | POLVO PARA SOLUCIÓN INYECTABLE Y PARA PERFUSIÓN | Eugia Pharma (Malta) Limited | Comercializada |
| 89435 | MEROPENEM AUROVIT 2.000 MG POLVO PARA SOLUCION PARA PERFUSION | POLVO PARA SOLUCIÓN PARA PERFUSIÓN | Eugia Pharma (Malta) Limited | Comercializada |
| 74303 | MEROPENEM AUROVIT 500 MG POLVO PARA SOLUCION INYECTABLE Y PARA PERFUSION EFG | POLVO PARA SOLUCIÓN INYECTABLE Y PARA PERFUSIÓN | Eugia Pharma (Malta) Limited | Comercializada |
| 83989 | ARCHIFAR 500 MG POLVO PARA SOLUCION INYECTABLE Y PARA PERFUSION EFG | POLVO PARA SOLUCIÓN INYECTABLE Y PARA PERFUSIÓN | Medochemie Iberia S.A. | Comercializada |
| 72610 | MEROPENEM KABI 500 mg POLVO PARA SOLUCION INYECTABLE Y PARA PERFUSION EFG | POLVO PARA SOLUCIÓN INYECTABLE Y PARA PERFUSIÓN | Fresenius Kabi España, S.A.U. | Comercializada |
| 89569 | MEROPENEM LDP LABORATORIOS TORLAN 500 MG POLVO PARA SOLUCIÓN INYECTABLE Y PARA PERFUSIÓN EFG | POLVO PARA SOLUCIÓN INYECTABLE Y PARA PERFUSIÓN | Ldp Laboratorios Torlan S.A. | Comercializada |
| 88903 | MEROPENEM VENUS PHARMA 2000 MG POLVO PARA SOLUCION INYECTABLE Y PARA PERFUSION | POLVO PARA SOLUCIÓN INYECTABLE Y PARA PERFUSIÓN | Venus Pharma Gmbh | Autorizada, no comercializada |
| 88341 | MEROPENEM STERISCIENCE 500 MG POLVO PARA SOLUCION INYECTABLE Y PARA PERFUSION EFG | POLVO PARA SOLUCIÓN INYECTABLE Y PARA PERFUSIÓN | Steriscience B.V. | Autorizada, no comercializada |
| 90807 | MEROPENEM QILU 2 G POLVO PARA SOLUCION INYECTABLE Y PARA PERFUSION | POLVO PARA SOLUCIÓN INYECTABLE Y PARA PERFUSIÓN | Qilu Pharma Spain S.L. | Autorizada, no comercializada |
| 88901 | MEROPENEM VENUS PHARMA 500 MG POLVO PARA SOLUCION INYECTABLE Y PARA PERFUSION EFG | POLVO PARA SOLUCIÓN INYECTABLE Y PARA PERFUSIÓN | Venus Pharma Gmbh | Autorizada, no comercializada |

Se muestran 10 de al menos 20 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas. Los datos de este informe solo incluyen parte de las autorizaciones.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registran 14 interacciones. Las de nivel mayor son con bupropión, iohexol e iopamidol. Las de nivel moderado incluyen ácido picosulfúrico, polietilenglicol con electrolitos, nitisinona, sulfato de sodio, lindano, etinilestradiol, alpelisib, encorafenib, ácido micofenólico, pemetrexed y teriflunomida.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La puntuación del modelo es alta, pero no hay ensayos clínicos y la literatura no evalúa directamente la eficacia de meropenem en artritis bacteriana (solo informes de casos, estudios de sensibilidad y farmacocinética). La evidencia se limita a la predicción del modelo.

**Para avanzar se necesita:**
- Estudios clínicos o series comparativas que evalúen meropenem en artritis séptica y otras infecciones osteoarticulares.
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones) para el cribado de seguridad.
- Evaluación del papel de meropenem frente a los tratamientos habituales, considerando la política de uso prudente de carbapenémicos.
- Datos de dosificación y penetración en hueso y articulación.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: meropenem prescribing information, Civica, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b0075b72-c3cc-f844-e053-2a95a90a417f) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

