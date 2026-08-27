---
layout: default
title: Baricitinib
parent: 僅模型預測 (L5)
nav_order: 34
evidence_level: L5
indication_count: 2
---

# Baricitinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Baricitinib: De Indicación Original No Documentada a Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## Resumen en Una Frase

No se dispone en los datos actuales de las indicaciones originales aprobadas de Baricitinib (DB11817), aunque su mecanismo de acción es de inhibidor de JAK1/JAK2. El modelo TxGNN predice que podría ser efectivo para **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, un síndrome de malformación congénita del desarrollo, pero actualmente **no existe ningún ensayo clínico ni publicación** que respalde esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos (sin licencias ni indicaciones registradas en el Evidence Pack) |
| Nueva Indicación Predicha | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados sobre el mecanismo de acción de Baricitinib en este Evidence Pack (data gap de severidad alta). Según la información disponible en el propio análisis de la predicción, Baricitinib es un inhibidor de JAK1/JAK2, una clase farmacológica cuyo mecanismo actúa sobre la señalización de citoquinas en enfermedades inflamatorias y autoinmunes.

La indicación predicha —un síndrome congénito de malformación del desarrollo (coloboma/microftalmía asociado a displasia esquelética rizomélica)— tiene una etiología asociada típicamente a genes del desarrollo embrionario (p. ej. genes ciliares o de morfogénesis ósea), no a vías inflamatorias ni a la señalización JAK-STAT. El propio análisis mecanístico incluido en el Evidence Pack concluye que **no existe una hipótesis de conexión mecanística creíble** entre el fármaco y esta indicación, y señala que la predicción es probablemente ruido o sobreajuste del modelo de embeddings de TxGNN en nodos de enfermedades raras.

Se observa el mismo patrón en la segunda indicación predicha (brachydactyly-syndactyly syndrome, score 99.94%, L5): otra malformación esquelética congénita sin vínculo mecanístico plausible con la inhibición de JAK, sin ensayos clínicos ni literatura de respaldo. Ambas predicciones refuerzan la conclusión de que, en su estado actual, este par fármaco-indicación no cuenta con base biológica ni evidencia empírica suficiente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Baricitinib no está actualmente comercializado en España según los datos disponibles, y no hay autorizaciones registradas en el Evidence Pack.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
A pesar del puntaje numérico elevado de TxGNN (99.94%), la evidencia es de nivel L5 (solo predicción del modelo, sin estudios reales), no existen ensayos clínicos ni literatura de respaldo, y el propio análisis mecanístico incluido en el paquete de evidencia indica que la conexión biológica entre Baricitinib y esta indicación es implausible y probablemente producto de ruido del modelo.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) de Baricitinib desde DrugBank (actualmente data gap de severidad alta)
- Ficha técnica/prospecto de la AEMPS con advertencias y contraindicaciones (actualmente data gap bloqueante para la evaluación inicial de seguridad, S1)
- Revalidación de la hipótesis mecanística antes de considerar cualquier búsqueda dirigida de evidencia clínica o preclínica
- Dado el patrón repetido en ambas indicaciones predichas (L5, sin evidencia, sin plausibilidad mecanística), se recomienda tratar este candidato como de baja prioridad hasta que surjan nuevas señales
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

