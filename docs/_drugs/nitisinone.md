---
layout: default
title: Nitisinone
parent: Solo predicción del modelo (L5)
nav_order: 570
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Nitisinone: nueva indicación predicha, Acidosis tubular renal (nivel de evidencia L5). Indicación original: Tirosinemia"
monitor_inn: "nitisinone"
predicted_indications: ["renal tubular acidosis", "galactosemia", "serpinopathy with toxic serpin polymerization", "C1 inhibitor deficiency", "glycogen storage disease", "adult polyglucosan body disease", "glycogen storage disease due to glucose-6-phosphatase deficiency", "Griscelli syndrome", "granulomatous disease, chronic, X-linked", "ermine phenotype"]
---

# Nitisinone
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

## Nitisinona: De Tirosinemia a Acidosis Tubular Renal
{: .text-alpha }

## Resumen en Una Frase

Nitisinona es un inhibidor de la enzima 4-hidroxifenilpiruvato dioxigenasa (HPPD), utilizado originalmente para el tratamiento de la tirosinemia.
El modelo TxGNN predice que podría ser efectivo para la **acidosis tubular renal**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tirosinemia |
| Nueva Indicación Predicha | Acidosis tubular renal |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 12 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción registrada en la base de datos. Según la información conocida, nitisinona inhibe la enzima HPPD en la vía de degradación de la tirosina, lo que evita la acumulación de metabolitos tóxicos como la succinilacetona en la tirosinemia hereditaria tipo 1.

En esta enfermedad, la disfunción tubular renal (tubulopatía proximal tipo Fanconi) es una manifestación reconocida, y nitisinona previene su progresión al bloquear la formación de dichos metabolitos. Por ello existe un vínculo mecanístico **indirecto** con la tubulopatía asociada a la tirosinemia.

Este vínculo no equivale a un efecto sobre la acidosis tubular renal primaria. La puntuación TxGNN tan alta es solo una predicción computacional, sin respaldo de ensayos ni literatura en los datos disponibles, y debe interpretarse con cautela.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal (acidosis tubular renal).

---

## Información de Mercado en España

Se listan 5 de las 12 autorizaciones vigentes (todas son monofármaco y están en estado válido):

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1171217001 | NITISINONE MDK 2 MG CAPSULAS DURAS | Cápsula dura | No disponible en los datos |
| 04303003 | ORFADIN 10 mg CAPSULAS DURAS | Cápsula dura | No disponible en los datos |
| 85156 | NITISINONA DIPHARMA 2 MG CAPSULAS DURAS EFG | Cápsula dura | No disponible en los datos |
| 104303005 | ORFADIN 4 mg/ml SUSPENSION ORAL | Suspensión oral | No disponible en los datos |
| 83467 | NITISINONA DIPHARMA 10 MG CAPSULAS DURAS EFG | Cápsula dura | No disponible en los datos |

---

## Consideraciones de Seguridad

- **Enfermedades con contraindicación según el grafo de conocimiento** (no proviene del prospecto): enfermedad renal, piouréter, trombocitopenia, leucopenia, hipofosfatemia y tirosinemia. Esta información debe verificarse con el prospecto oficial.
- **Interacciones farmacológicas**: se identificaron 201 interacciones en total. Entre las principales (mayoría de nivel moderado):
  - Abametapir (tópico), abiraterona, isotretinoína, nifedipino, ibuprofeno
  - Aldesleucina, pioglitazona, amiodarona, amlodipino, amobarbital
  - Apalutamida, aprepitant, atazanavir, avatrombopag, baricitinib
  - Dexametasona, bexaroteno, bicalutamida, jengibre
  - Armodafinilo (nivel menor)

Consultar el prospecto para las advertencias y contraindicaciones oficiales.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y el vínculo mecanístico con la acidosis tubular renal primaria es indirecto. Otras indicaciones predichas, como galactosemia y enfermedad por almacenamiento de glucógeno, solo cuentan con revisiones que las mencionan en contextos de diagnóstico diferencial (nivel L4) y tampoco respaldan un efecto terapéutico.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA)
- Advertencias y contraindicaciones oficiales del prospecto de la AEMPS
- Texto de las indicaciones aprobadas de cada autorización
- Revisión sistemática de la literatura sobre nitisinona y tubulopatías renales
- Estudios preclínicos o series de casos que evalúen el efecto de nitisinona en la acidosis tubular renal primaria
- Revisión de la compatibilidad de vías de administración y similitud con la indicación original
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

