---
layout: default
title: Palbociclib
parent: 僅模型預測 (L5)
nav_order: 208
evidence_level: L5
indication_count: 4
---

# Palbociclib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Palbociclib: De Cáncer de Mama a Artritis Reumatoide

## Resumen en Una Frase

Palbociclib es un inhibidor selectivo de CDK4/6 utilizado internacionalmente para el cáncer de mama HR+/HER2- avanzado, aunque actualmente no está comercializado en España. El modelo TxGNN predice que podría ser efectivo para la **Artritis Reumatoide**, con **1 reporte de caso y 3 estudios mecanicistas/de revisión** que respaldan esta dirección, pero **sin ensayos clínicos controlados** hasta la fecha.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de mama HR+/HER2- (según contexto de la literatura; sin ficha técnica oficial disponible) |
| Nueva Indicación Predicha | Artritis Reumatoide |
| Puntaje de Predicción TxGNN | 99.36% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en ficha técnica oficial (dato pendiente de DrugBank/TFDA). Según la información disponible en la literatura, palbociclib es un inhibidor selectivo de las quinasas dependientes de ciclina 4 y 6 (CDK4/6), perteneciente a la clase de terapias dirigidas oncológicas, cuya eficacia en el cáncer de mama HR+/HER2- avanzado está ampliamente comprobada en la práctica clínica internacional.

La conexión mecanística con la artritis reumatoide se apoya en evidencia preclínica: un estudio en modelos murinos de artritis identificó una hiperplasia sinovial dependiente de CDK6 (independiente de CDK4) como vía clave en la proliferación de fibroblastos sinoviales inducida por TNF-α, sugiriendo que la inhibición de CDK4/6 podría frenar directamente esta proliferación patológica. Un segundo estudio preclínico mostró que la inhibición del ciclo celular combinada con bloqueo de citoquinas mejora los efectos antiartríticos sin aumentar la inmunosupresión.

A nivel clínico, existe únicamente un reporte de caso de una paciente con cáncer de mama y artritis reumatoide preexistente cuya artritis mejoró tras iniciar palbociclib, y un estudio de cohorte/revisión sobre enfermedades autoinmunes en pacientes tratadas con inhibidores de CDK4/6. El mecanismo es biológicamente plausible, pero la evidencia en humanos es todavía anecdótica y no controlada.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33587021](https://pubmed.ncbi.nlm.nih.gov/33587021/) | 2021 | Reporte de Caso | Mod Rheumatol Case Rep | Mejoría de artritis reumatoide en una paciente con cáncer de mama tratada con palbociclib |
| [40504547](https://pubmed.ncbi.nlm.nih.gov/40504547/) | 2025 | Revisión/Cohorte | The Oncologist | Prevalencia de enfermedades autoinmunes preexistentes/emergentes en pacientes con cáncer de mama HR+/HER2- tratadas con inhibidores de CDK4/6 |
| [25165034](https://pubmed.ncbi.nlm.nih.gov/25165034/) | 2016 | Preclínico (mecanístico) | Ann Rheum Dis | Inhibición del ciclo celular combinada con bloqueo de citoquinas mejora efectos antiartríticos en modelos animales de AR, sin aumentar inmunosupresión |
| [39940918](https://pubmed.ncbi.nlm.nih.gov/39940918/) | 2025 | Preclínico (mecanístico) | Int J Mol Sci | Hiperplasia sinovial dependiente de CDK6 (no de CDK4) en ratones artríticos; palbociclib explorado como opción terapéutica para AR, con mielosupresión reportada en estudios preclínicos |

---

## Citotoxicidad

*Palbociclib es una terapia oncológica dirigida (inhibidor de CDK4/6), por lo que se incluye esta sección.*

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de CDK4/6), no es citotóxico convencional |
| Riesgo de Mielosupresión | Alto — la literatura documenta directamente "mielosupresión inducida por palbociclib" en estudios preclínicos, y la supresión de médula ósea es un evento adverso frecuente y bien caracterizado de esta clase |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma completo (riesgo de neutropenia/mielosupresión) |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad (advertencias, contraindicaciones e interacciones farmacológicas no disponibles actualmente — DG001, bloqueante).

**Señal adicional detectada durante la revisión de evidencia:** varios estudios de farmacovigilancia (FAERS) y de farmacoepidemiología del mundo real, identificados al evaluar otra indicación candidata (enfermedad trombótica), asocian a los inhibidores de CDK4/6 —incluido palbociclib— con eventos tromboembólicos como evento adverso ([PMID 39123221](https://pubmed.ncbi.nlm.nih.gov/39123221/), [PMID 39083396](https://pubmed.ncbi.nlm.nih.gov/39083396/), [PMID 36794339](https://pubmed.ncbi.nlm.nih.gov/36794339/), [PMID 35300061](https://pubmed.ncbi.nlm.nih.gov/35300061/)). Esto no respalda la reposición hacia enfermedad trombótica, pero es relevante como señal de seguridad a monitorizar en cualquier uso futuro del fármaco.

---

## Otras Indicaciones Predichas Evaluadas

Además de la artritis reumatoide, el pipeline de evidencia evaluó tres candidatos adicionales, todos con recomendación **Hold**:

- **Hipertiroidismo** (score 99.44%, L5): sin ensayos ni literatura; sin base mecanicista conocida.
- **Enfermedad Trombótica** (score 99.32%, L4): señal invertida — la evidencia disponible describe eventos trombóticos como *reacción adversa* de los inhibidores de CDK4/6, no como indicación terapéutica.
- **Resistencia a la Hormona Tiroidea por mutación en el receptor beta** (score 99.30%, L5): enfermedad monogénica rara sin relación mecanística conocida ni evidencia de respaldo.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La hipótesis mecanística para artritis reumatoide es biológicamente plausible (hiperplasia sinovial dependiente de CDK6) pero la evidencia en humanos se limita a un reporte de caso, sin ningún ensayo clínico registrado (nivel L4, etapa S1 — "Research Question"). Además, el fármaco no está comercializado en España y faltan datos regulatorios básicos de seguridad (DG001, bloqueante para la evaluación S1).

**Para avanzar se necesita:**
- Obtener la ficha técnica oficial (advertencias, contraindicaciones, MOA formal) — actualmente bloqueante (DG001/DG002)
- Diseñar un estudio piloto (Fase 1/2) en artritis reumatoide refractaria, con vigilancia hematológica como criterio primario de seguridad
- Incorporar la señal de riesgo tromboembólico de clase como criterio de exclusión/monitorización en cualquier protocolo
- Definir la vía regulatoria de importación/autorización en España, dado el estado actual "no comercializado"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

