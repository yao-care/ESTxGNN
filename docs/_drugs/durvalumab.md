---
layout: default
title: Durvalumab
parent: Solo predicción del modelo (L5)
nav_order: 272
evidence_level: L5
indication_count: 6
monitor_inn: "DURVALUMAB"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
last_modified_at: 2026-11-24
description: "Durvalumab: nueva indicación predicha, Adenocarcinoma del ligamento uterino (uterine ligament adenocarcinoma) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 4 (comercializadas: 4)"
---

# Durvalumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Durvalumab: Adenocarcinoma del ligamento uterino (uterine ligament adenocarcinoma)
{: .text-alpha }

## Resumen en Una Frase

Durvalumab es un anticuerpo inhibidor de PD-L1.
El modelo TxGNN predice que podría ser efectivo para **adenocarcinoma del ligamento uterino**, pero para esta enfermedad hay **0 ensayos clínicos** y **0 publicaciones** que respalden la predicción.
Entre las predicciones del mismo fármaco, la mejor respaldada es el **carcinoma endocervical** (1 ensayo de Fase 1 y 2 publicaciones indirectas).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Adenocarcinoma del ligamento uterino (uterine ligament adenocarcinoma) |
| Puntaje de Predicción TxGNN | 0.9992 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 4 de 4) |
| Número de Autorizaciones | 4 (comercializadas: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Durvalumab (traducción no oficial): «La expresión del ligando 1 de muerte celular programada (PD-L1) puede ser inducida por señales inflamatorias (p. ej., IFN-gamma), y el PD-L1 puede expresarse tanto en las células tumorales como en las células inmunitarias asociadas al tumor en el microentorno tumoral. El PD-L1 bloquea la función y la activación de los linfocitos T mediante su interacción con PD-1 y CD80 (B7.1). […] El durvalumab es un anticuerpo monoclonal humano de tipo inmunoglobulina G1 kappa (IgG1κ) que se une al PD-L1 y bloquea la interacción del PD-L1 con PD-1 y CD80 (B7.1).» Texto original en inglés: "Expression of programmed cell death ligand-1 (PD-L1) can be induced by inflammatory signals (e.g., IFN-gamma) and can be expressed on both tumor cells and tumor-associated immune cells in the tumor microenvironment. PD-L1 blocks T-cell function and activation through interaction with PD-1 and CD80 (B7.1). […] Durvalumab is a human immunoglobulin G1 kappa (IgG1κ) monoclonal antibody that binds to PD-L1 and blocks the interaction of PD-L1 with PD-1 and CD80 (B7.1)." ([DailyMed: Imfinzi (durvalumab) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8baba4ea-2855-42fa-9bd9-5a7548d4cec3), versión del 2026-08-31; consultado el 2026-11-19). Según la información conocida, durvalumab es un inhibidor del punto de control inmunitario PD-L1, y mecanísticamente el bloqueo de esta vía podría ser aplicable a otros adenocarcinomas ginecológicos.

Sin embargo, esta es una extrapolación: no existe ningún ensayo ni publicación en los datos que estudie directamente el adenocarcinoma del ligamento uterino. La puntuación TxGNN (0,999) es solo una salida del modelo y no constituye evidencia clínica. Por ello el nivel de evidencia se mantiene en L5.

Otras predicciones del modelo para este fármaco, todas en el ámbito ginecológico, son: carcinoma endocervical (0.9992), carcinoma adenoide quístico del cuello uterino (0.9992), adenocarcinoma seroso del ligamento uterino (0.9992), adenocarcinoma mucinoso cervical variante de células en anillo de sello (0.9991) y adenocarcinoma mucinoso cervical variante intestinal (0.9991). De ellas, solo el carcinoma endocervical cuenta con algún respaldo (ver abajo; nivel L3 según el análisis previo, pero ver nota en la conclusión).

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para el adenocarcinoma del ligamento uterino.

Como referencia, para la segunda predicción (carcinoma endocervical) se identificó:

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03452332](https://clinicaltrials.gov/study/NCT03452332) | Fase 1 | Completado | 20 | Radioterapia hipofraccionada (SBRT) con durvalumab y tremelimumab en cáncer de cuello uterino, vagina o vulva recurrente o metastásico. Sirve para valorar seguridad y viabilidad; no aporta datos de eficacia. |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para el adenocarcinoma del ligamento uterino.

Como referencia, para el carcinoma endocervical se recuperaron:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37467967](https://pubmed.ncbi.nlm.nih.gov/37467967/) | 2023 | Revisión | Biomedical Journal | Carcinoma neuroendocrino de células pequeñas del cuello uterino: base molecular y avances terapéuticos; los datos publicados se limitan a series y reportes de casos. |
| [42518016](https://pubmed.ncbi.nlm.nih.gov/42518016/) | 2026 | Ensayo clínico no aleatorizado | Oncology and Therapy | Ceralasertib más durvalumab en tumores sólidos avanzados en pacientes chinos (Fase I); no es específico de cuello uterino. |

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 1181322002IP | IMFINZI 50 MG/ML CONCENTRADO PARA SOLUCION PARA PERFUSION | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Astrazeneca Ab | Comercializada |
| 1181322001IP | IMFINZI 50 MG/ML CONCENTRADO PARA SOLUCION PARA PERFUSION | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Astrazeneca Ab | Comercializada |
| 1181322001 | IMFINZI 50 MG/ML CONCENTRADO PARA SOLUCION PARA PERFUSION | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Astrazeneca Ab | Comercializada |
| 1181322002 | IMFINZI 50 MG/ML CONCENTRADO PARA SOLUCION PARA PERFUSION | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Astrazeneca Ab | Comercializada |

Se muestran las 4 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (anticuerpo monoclonal anti-PD-L1) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registraron 81 interacciones. Entre las principales:
  - **Mayor**: adalimumab.
  - **Moderada**: corticoides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida, prednisolona, prednisona, metilprednisolona, deflazacort), roflumilast, alefacept, alemtuzumab, anakinra, vacuna antitetánica y vacuna contra el ántrax.
  - **Menor**: sales de zinc (acetato, gluconato, sulfato, cloruro).

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún ensayo ni publicación que estudie directamente el adenocarcinoma del ligamento uterino; la predicción se basa solo en el modelo (nivel L5). Aunque el carcinoma endocervical tiene un ensayo de Fase 1 con 20 pacientes, este solo aporta información de viabilidad y seguridad, y el nivel debe considerarse con cautela porque no se confirma que el estudio sea específico de esta histología.

**Para avanzar se necesita:**
- Estudios clínicos o preclínicos que evalúen durvalumab directamente en esta enfermedad.
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones), actualmente no disponibles.
- Texto de indicaciones aprobadas de las autorizaciones locales.
- Revisión de seguridad de interacciones, en especial con inmunosupresores como los corticoides y adalimumab.
- Evaluación de la compatibilidad de vía de administración y similitud con la indicación original (pendientes).

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Imfinzi (durvalumab) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8baba4ea-2855-42fa-9bd9-5a7548d4cec3) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

