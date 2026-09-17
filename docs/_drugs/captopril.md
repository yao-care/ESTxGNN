---
layout: default
title: Captopril
parent: Evidencia moderada (L3-L4)
nav_order: 58
evidence_level: L4
indication_count: 4
---

# Captopril
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **4** 
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

# Captopril: De Hipertensión Arterial a Enfermedad Renal Hipertensiva Maligna

## Resumen en Una Frase

Captopril es un inhibidor de la enzima convertidora de angiotensina (IECA), utilizado originalmente en el tratamiento de la hipertensión arterial. El modelo TxGNN predice que podría ser efectivo para **Enfermedad Renal Hipertensiva Maligna**, con **1 publicación** que actualmente respalda esta dirección de forma indirecta, sin ensayos clínicos registrados.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Hipertensión arterial (clase IECA; no hay texto de indicación de licencia disponible en España) |
| Nueva Indicacion Predicha | Enfermedad Renal Hipertensiva Maligna |
| Puntaje de Prediccion TxGNN | 99.28% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Espana | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción (MOA) desde la fuente estructurada (DrugBank). Según la información conocida de forma general, captopril es un inhibidor de la enzima convertidora de angiotensina (IECA) que bloquea el sistema renina-angiotensina-aldosterona (RAAS), mecanismo bien establecido en su indicación original de hipertensión arterial.

La hipertensión renal maligna es, por definición, un estado de hiperactivación marcada del eje renina-angiotensina; por tanto, existe una relación mecanicista directa y plausible entre la indicación original de captopril y esta nueva indicación predicha por TxGNN.

Sin embargo, la única evidencia bibliográfica disponible para esta indicación específica es un reporte de caso sobre gammagrafía renal con captopril (uso diagnóstico, no terapéutico) que resultó ser un falso positivo causado por un carcinoma de células renales, no por hipertensión renina-dependiente real. Esta evidencia respalda solo indirectamente la hipótesis mecanicista, sin constituir evidencia de eficacia terapéutica. Cabe destacar que la indicación relacionada "malignant renovascular hypertension" (mismo puntaje TxGNN) cuenta con una base de literatura considerablemente más sólida (20 publicaciones, incluyendo revisiones y series de casos clínicos), lo que refuerza la plausibilidad general del mecanismo IECA en hipertensión renina-dependiente grave.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28902735](https://pubmed.ncbi.nlm.nih.gov/28902735/) | 2017 | Reporte de Caso | Clinical Nuclear Medicine | Gammagrafía renal con captopril positiva sin estenosis de arteria renal; la causa real fue un carcinoma de células renales cromófobo. La hipertensión renina-dependiente se resolvió tras nefrectomía. Evidencia diagnóstica, no terapéutica. |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusion y Proximos Pasos

**Decisión: Hold**

**Justificación:**
El único dato bibliográfico disponible para esta indicación es un reporte de caso de uso diagnóstico (no terapéutico), y no existen ensayos clínicos registrados. Aunque el mecanismo IECA es plausible para hipertensión renina-dependiente grave, la evidencia actual (nivel L4) es insuficiente para avanzar más allá de la fase de pregunta de investigación.

**Para avanzar se necesita:**
- Prospecto/ficha técnica de la agencia reguladora con advertencias y contraindicaciones (actualmente ausente — gap bloqueante, DG001)
- Datos detallados del mecanismo de acción desde DrugBank (gap de alta prioridad, DG002)
- Estudios terapéuticos (no solo diagnósticos) que evalúen captopril en enfermedad renal hipertensiva maligna
- Evaluar en paralelo la indicación relacionada "malignant renovascular hypertension" (mismo puntaje TxGNN, nivel L3, recomendación "Proceed with Guardrails"), que cuenta con una base de evidencia bibliográfica considerablemente más robusta
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

