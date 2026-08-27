---
layout: default
title: Latanoprost
parent: 僅模型預測 (L5)
nav_order: 160
evidence_level: L5
indication_count: 10
---

# Latanoprost
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Latanoprost: De Glaucoma a Glaucoma Hereditario Primario

## Resumen en Una Frase

Latanoprost es un análogo de prostaglandina F2α utilizado habitualmente para reducir la presión intraocular en glaucoma e hipertensión ocular. El modelo TxGNN predice que podría ser efectivo para **Glaucoma Hereditario Primario**, con **1 ensayo clínico de Fase 2 completado** que actualmente respalda esta dirección, aunque sin literatura adicional disponible.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Reducción de la presión intraocular (glaucoma / hipertensión ocular) |
| Nueva Indicación Predicha | Glaucoma Hereditario Primario |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Taiwán | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

El dato estructurado de mecanismo de acción no está disponible en DrugBank para este candidato. Sin embargo, según la justificación mecanística asociada a esta predicción, Latanoprost es un análogo de prostaglandina F2α que activa los receptores FP, incrementando el flujo de salida uveoescleral del humor acuoso — el mecanismo estándar de los fármacos reductores de la presión intraocular (PIO).

El Glaucoma Hereditario Primario, aunque corresponde a un subgrupo genético específico, comparte el mismo núcleo fisiopatológico que el glaucoma común: presión intraocular elevada que daña el nervio óptico. Por ello, el mecanismo de acción de Latanoprost resulta directamente aplicable a esta nueva indicación.

La relación entre la indicación original (control de la PIO) y la nueva indicación predicha es, por tanto, prácticamente directa y no constituye una extrapolación novedosa, lo cual está respaldado por un ensayo clínico de Fase 2 ya completado en una población de glaucoma primario pediátrico.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Fase 2 | Completado | 37 | Evaluó el efecto hipotensor ocular de latanoprost y dorzolamida en pacientes con Glaucoma Pediátrico Primario (PG) refractario a cirugía; también se evaluó la seguridad. |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Taiwán

Actualmente no hay autorizaciones de comercialización registradas para Latanoprost en Taiwán (estado: no comercializado, 0 autorizaciones).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ensayo clínico de Fase 2 ya completado que respalda la eficacia de latanoprost en una población de glaucoma primario, junto con una alta plausibilidad mecanística (mismo objetivo terapéutico: control de la PIO). Sin embargo, la evidencia se limita a un solo ensayo con tamaño de muestra modesto (n=37) y sin literatura adicional que la respalde.

**Para avanzar se necesita:**
- Warnings/contraindicaciones del prospecto TFDA (brecha DG001, prioridad *Blocking* — impide la evaluación de seguridad S1)
- Datos detallados del mecanismo de acción desde DrugBank (brecha DG002, prioridad Alta)
- Estudios clínicos adicionales específicos para el subgrupo de glaucoma hereditario
- Datos de interacciones farmacológicas (DDI), actualmente no encontrados
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

