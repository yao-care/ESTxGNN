---
layout: default
title: Entecavir
parent: Evidencia moderada (L3-L4)
nav_order: 292
evidence_level: L4
indication_count: 9
last_modified_at: 2026-10-31
monitor_inn: "ENTECAVIR"
predicted_indications: ["chronic hepatitis C virus infection", "HIV infectious disease", "hepatitis C virus infection", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "hepatitis, viral, animal", "hepatitis E virus infection", "hepatitis A virus infection"]
description: "Entecavir: nueva indicación predicha, Infección crónica por el virus de la hepatitis C (chronic hepatitis C virus infection) (nivel de evidencia L4). Indicación original: No consta en los datos local…"
---

# Entecavir
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **9** 
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

## Entecavir: Infección crónica por el virus de la hepatitis C (chronic hepatitis C virus infection)
{: .text-alpha }

## Resumen en Una Frase

Entecavir es un análogo nucleósido de la guanosina, utilizado originalmente para tratar la **infección crónica por el virus de la hepatitis B (VHB)**.
El modelo TxGNN predice que podría ser efectivo para la **infección crónica por el virus de la hepatitis C (VHC)**, pero solo respaldan esta dirección **2 ensayos clínicos** y **20 publicaciones**, y ninguno demuestra que entecavir trate el VHC.
Los estudios identificados se refieren a la coinfección VHC/VHB, en la que entecavir actúa sobre el componente del VHB.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Infección crónica por el virus de la hepatitis C (chronic hepatitis C virus infection) |
| Puntaje de Predicción TxGNN | 0.9998 |
| Nivel de Evidencia | L4 (solo evidencia indirecta; ningún estudio real en VHC) |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 12) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, entecavir es un análogo nucleósido de la guanosina que, una vez fosforilado a su forma trifosfato activa, inhibe la ADN polimerasa del VHB. Su eficacia en la hepatitis B crónica está bien establecida y respaldada por guías clínicas como la EASL 2017.

La hepatitis B y la hepatitis C son ambas infecciones virales crónicas del hígado, con riesgo de cirrosis y carcinoma hepatocelular, y con frecuencia coexisten en el mismo paciente. Es probable que esta cercanía clínica y de red de enfermedades explique el puntaje tan alto del modelo.

**Sin embargo, mecanísticamente la predicción es débil.** El VHC es un virus ARN que se replica mediante la ARN polimerasa dependiente de ARN (NS5B), y entecavir no tiene actividad antiviral conocida contra él. Los ensayos identificados evalúan entecavir u otros análogos nucleósidos para prevenir la reactivación del VHB durante el tratamiento del VHC con antivirales de acción directa. No evalúan el tratamiento del VHC con entecavir. La señal del modelo parece reflejar la proximidad en la red de conocimiento y no una actividad antiviral directa.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Fase 2/3 | Completado | 23 | Antivirales de acción directa en pacientes coinfectados VHC/VHB; estudia la incidencia y los factores de riesgo de reactivación del VHB durante el tratamiento del VHC. No evalúa entecavir como tratamiento del VHC. |
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | N/A | Desconocido | 60 | Aleatorizado, abierto, de tres brazos: profilaxis con análogos nucleós(t)idos (12 vs. 24 semanas) frente a la reactivación del VHB en coinfectados VHC/VHB que reciben antivirales de acción directa. Aborda el VHB, no el VHC. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34864158](https://pubmed.ncbi.nlm.nih.gov/34864158/) | 2022 | Ensayo aleatorizado | Clin Gastroenterol Hepatol | Entecavir previene la reactivación del VHB durante el tratamiento con antivirales de acción directa en la doble infección VHC/VHB. |
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Cohorte | Viruses | Cohorte de 66 pacientes con hepatitis B crónica y anti-VHC positivos; analiza la reactivación del VHC durante el tratamiento antiviral contra el VHB. |
| [35108715](https://pubmed.ncbi.nlm.nih.gov/35108715/) | 2022 | Estudio observacional | Dig Dis | Incidencia y evolución clínica de la reactivación del VHB en pacientes tratados con antivirales de acción directa contra el VHC. |
| [28230928](https://pubmed.ncbi.nlm.nih.gov/28230928/) | 2017 | Estudio observacional | J Gastroenterol Hepatol | Riesgo de reactivación del VHB durante el tratamiento del VHC con antivirales de acción directa. |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Revisión | Expert Opin Pharmacother | Avances en el tratamiento de la coinfección VHB/VHC, que conlleva alto riesgo de cirrosis y carcinoma hepatocelular. |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Revisión | Minerva Gastroenterol Dietol | Antivirales para hepatitis B y C (entre ellos entecavir) y sus efectos sobre la función renal. |
| [35327336](https://pubmed.ncbi.nlm.nih.gov/35327336/) | 2022 | Revisión | Biomedicines | Terapia de la hepatitis viral crónica; los análogos nucleós(t)idos han mejorado de forma importante la evolución de la hepatitis B. |
| [32173307](https://pubmed.ncbi.nlm.nih.gov/32173307/) | 2020 | Revisión | Clin Res Hepatol Gastroenterol | Manejo actual y futuro de las hepatitis B y C en niños. |
| [24868325](https://pubmed.ncbi.nlm.nih.gov/24868325/) | 2014 | Revisión | World J Hepatol | Manejo de hepatitis B y C antes y después del trasplante hepático y renal; entecavir y tenofovir mejoran el pronóstico en la hepatitis B. |
| [38450508](https://pubmed.ncbi.nlm.nih.gov/38450508/) | 2024 | Revisión | Rev Esp Enferm Dig | Hepatología en hemofilia; la aprobación de entecavir y tenofovir contra el VHB y de los antivirales de acción directa contra el VHC permitió tratamientos realmente eficaces. |

---

## Información de Mercado en España

Entecavir tiene 20 autorizaciones vigentes (todas de medicamentos con un solo principio activo, ninguna cancelada). Se listan las 5 principales.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 06343003 | BARACLUDE 0,5 mg comprimidos recubiertos con película | Comprimido recubierto con película | No consignada en los datos disponibles |
| 06343004 | BARACLUDE 1 mg comprimidos recubiertos con película | Comprimido recubierto con película | No consignada en los datos disponibles |
| 06343005 | BARACLUDE 0,05 mg/ml solución oral | Solución oral | No consignada en los datos disponibles |
| 82136 | ENTECAVIR STADA 0,5 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No consignada en los datos disponibles |
| 84926 | ENTECAVIR SUN 0,5 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No consignada en los datos disponibles |

---

## Consideraciones de Seguridad

- **Contraindicaciones o condiciones de riesgo (según el grafo de conocimiento, no el prospecto):** insuficiencia renal, hígado graso, esteatohepatitis no alcohólica y acidosis láctica.
- **Interacciones farmacológicas:** se identificaron 44 interacciones; las 20 detalladas son todas de nivel **moderado**. Las principales son:
  - Antiácidos y antagonistas H2: famotidina, ranitidina y cimetidina.
  - Metformina.
  - Anfotericina B (formulaciones convencional, lipídica, liposomal y de sulfato de colesterilo).
  - Antibióticos: amoxicilina, vancomicina, kanamicina, neomicina, levofloxacino y polimixina B.
  - Salicilatos y derivados: mesalazina, balsalazida, olsalazina y sulfasalazina.
  - Orlistat.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La alta puntuación del modelo (0,9998) no está respaldada por evidencia directa. Los dos ensayos y la literatura tratan la coinfección VHC/VHB, donde entecavir actúa sobre el VHB, y no existe plausibilidad mecanística contra el VHC. Además, el VHC ya dispone de antivirales de acción directa muy eficaces.

**Para avanzar se necesita:**
- Datos de actividad antiviral de entecavir contra el VHC (estudios in vitro o preclínicos), que hoy no existen en los datos compilados.
- Datos detallados del mecanismo de acción (MOA) del fármaco.
- Los textos de indicación y las advertencias y contraindicaciones del prospecto oficial de la AEMPS.
- Si el interés real es la coinfección VHC/VHB, reformular la pregunta como "prevención de la reactivación del VHB durante el tratamiento del VHC", donde ya existe un ensayo aleatorizado (PMID 34864158), y evaluarla como una indicación distinta.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

