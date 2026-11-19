---
layout: default
title: Selpercatinib
parent: Solo predicción del modelo (L5)
nav_order: 730
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-05
description: "Selpercatinib: nueva indicación predicha, Hipertensión pulmonar (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (los textos de indicación de la…"
monitor_inn: "SELPERCATINIB"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "migraine with brainstem aura"]
---

# Selpercatinib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Selpercatinib: De Indicación Original No Especificada a Hipertensión Pulmonar
{: .text-alpha }

## Resumen en Una Frase

Selpercatinib es un inhibidor selectivo de la quinasa RET, comercializado en España con el nombre Retsevmo. Los datos compilados para este informe no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **hipertensión pulmonar**, pero actualmente hay **0 ensayos clínicos** y **ninguna publicación que estudie esta indicación** (las 3 publicaciones recuperadas tratan sobre cánceres con alteraciones de RET y perfiles de eventos adversos).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Hipertensión pulmonar |
| Puntaje de Predicción TxGNN | 0.9918 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 2 de 4; autorizadas no comercializadas: 2) |
| Número de Autorizaciones | 4 (comercializadas: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Selpercatinib (traducción no oficial): «El selpercatinib es un inhibidor de cinasas. El selpercatinib inhibió el RET de tipo silvestre y múltiples isoformas mutadas de RET, así como VEGFR1 y VEGFR3, con valores de CI 50 que oscilaron entre 0,92 nM y 67,8 nM. En otros ensayos enzimáticos, el selpercatinib también inhibió FGFR 1, 2 y 3 a concentraciones más altas que aún eran alcanzables clínicamente.» Texto original en inglés: "Selpercatinib is a kinase inhibitor. Selpercatinib inhibited wild-type RET and multiple mutated RET isoforms as well as VEGFR1 and VEGFR3 with IC 50 values ranging from 0.92 nM to 67.8 nM. In other enzyme assays, selpercatinib also inhibited FGFR 1, 2, and 3 at higher concentrations that were still clinically achievable." ([DailyMed: Retevmo (selpercatinib) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7fa848ba-a59c-4144-9f52-64d090f4d828), versión del 2026-09-11; consultado el 2026-11-19). Según la información conocida, selpercatinib es un inhibidor selectivo de la quinasa RET, y las publicaciones recuperadas lo sitúan en el tratamiento de cánceres con alteraciones de RET (cáncer de pulmón no microcítico con fusión de RET y carcinoma medular de tiroides).

El puntaje de TxGNN es muy alto (0.9918), proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. Un posible vínculo hipotético sería la modulación de la señalización de receptores tirosina quinasa implicada en la remodelación vascular pulmonar, pero ningún dato respalda directamente esta idea.

Ninguna de las publicaciones recuperadas estudia la hipertensión pulmonar como indicación terapéutica. Cualquier señal de hipertensión pulmonar en el estudio de farmacovigilancia sería una observación de seguridad, no terapéutica. Por tanto, el vínculo mecanístico no está respaldado.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Las siguientes publicaciones fueron recuperadas, pero ninguna evalúa la hipertensión pulmonar como indicación:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34178121](https://pubmed.ncbi.nlm.nih.gov/34178121/) | 2021 | Cohorte retrospectiva | Therapeutic Advances in Medical Oncology | Análisis retrospectivo (SIREN) de selpercatinib en cáncer de pulmón no microcítico con fusión de RET, tratado mediante un programa de acceso |
| [39372206](https://pubmed.ncbi.nlm.nih.gov/39372206/) | 2024 | Estudio de farmacovigilancia | Frontiers in Pharmacology | Comparación de los eventos adversos de pralsetinib y selpercatinib con datos reales del sistema FAERS |
| [41918669](https://pubmed.ncbi.nlm.nih.gov/41918669/) | 2026 | Reporte de caso | Cureus | Carcinoma medular de tiroides metastásico en MEN 2B con mutación RET M918T: desafíos del manejo a largo plazo y la terapia dirigida |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1201527016 | RETSEVMO 80 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 1201527001 | RETSEVMO 40 mg cápsulas duras | Cápsula dura | No disponible |
| 1201527002 | RETSEVMO 80 mg cápsulas duras | Cápsula dura | No disponible |
| 1201527013 | RETSEVMO 40 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor selectivo de quinasa RET) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: La consulta identificó 100 interacciones. Entre las principales:
  - **Gravedad Mayor**: famotidina, ranitidina, rabeprazol, omeprazol, dexlansoprazol y cimetidina (fármacos que reducen la acidez gástrica), aprepitant, dexametasona, claritromicina y óxido de magnesio.
  - **Gravedad Moderada**: hidrocortisona, triamcinolona, betametasona, budesonida, pioglitazona, loperamida, bisacodilo, polietilenglicol 3350 con electrolitos y saxagliptina.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura que respalden el uso en hipertensión pulmonar. El vínculo mecanístico no está respaldado por los datos disponibles.

**Para avanzar se necesita:**
- Obtener el texto de las indicaciones aprobadas y las advertencias y contraindicaciones del prospecto de la AEMPS
- Obtener datos del mecanismo de acción (MOA) desde DrugBank
- Estudios preclínicos que evalúen la inhibición de RET en modelos de hipertensión pulmonar
- Revisar si la señal de hipertensión pulmonar en los datos de farmacovigilancia corresponde a un riesgo de seguridad
- Evaluar el riesgo de las interacciones de gravedad mayor, especialmente con fármacos que reducen la acidez gástrica

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Retevmo (selpercatinib) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7fa848ba-a59c-4144-9f52-64d090f4d828) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

