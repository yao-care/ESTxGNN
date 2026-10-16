---
layout: default
title: Milrinone
parent: Solo predicción del modelo (L5)
nav_order: 530
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Milrinone: nueva indicación predicha, Alopecia (nivel de evidencia L5). Indicación original: Insuficiencia cardiaca congestiva (según datos farmacológicos"
monitor_inn: "milrinone"
predicted_indications: ["alopecia", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "headache disorder", "congestive heart failure", "migraine disorder", "migraine with brainstem aura", "trigeminal autonomic cephalalgia", "acute pulmonary heart disease"]
---

# Milrinone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Milrinona: De Insuficiencia Cardiaca Congestiva a Alopecia

## Resumen en Una Frase

Milrinona es un inhibidor de la fosfodiesterasa 3 (PDE3) que se utiliza por vía inyectable para la insuficiencia cardiaca congestiva descompensada.
El modelo TxGNN predice que podría ser efectiva para **alopecia**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Insuficiencia cardiaca congestiva (según datos farmacológicos; el texto de indicación de la autorización de AEMPS no está disponible) |
| Nueva Indicación Predicha | Alopecia |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Milrinona inhibe la fosfodiesterasa 3 (PDE3), lo que eleva el AMP cíclico (AMPc). En el corazón esto produce un efecto inotrópico positivo, y en los vasos sanguíneos produce vasodilatación periférica. Por eso se la clasifica como "inodilatador". Los datos farmacológicos también la asocian con PDE2A, PDE3A, PDE3B y PDE5A.

Un vínculo con el cabello es concebible, pero especulativo. La señalización por AMPc y el flujo sanguíneo perifolicular podrían influir en la biología del folículo piloso, de forma parecida a lo que se discute con el minoxidil, otro vasodilatador. Sin embargo, no existe ningún estudio clínico ni publicación que respalde este uso de milrinona.

El puntaje alto (99.91%) probablemente refleja cercanía en el grafo de conocimiento con otros nodos relacionados con la pérdida de cabello y no biología real. Las demás predicciones del mismo grupo (hipotricosis simple del cuero cabelludo, hipotricosis congénita con milia y alopecia areata difusa) tampoco cuentan con evidencia. En la alopecia areata, además, las vías más relevantes son JAK y PDE4, no PDE3.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 58849 | COROTROPE 1 mg/ml SOLUCIÓN INYECTABLE (Sanofi Aventis S.A.) | Solución inyectable | No especificada en los datos disponibles |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas por el grafo de conocimiento** (relaciones fármaco-enfermedad del grafo de conocimiento, no texto del prospecto): enfermedad renal, piouréter, trastornos hipotensivos, infarto de miocardio, trombosis coronaria, hemoglobinopatía, paro cardiaco súbito, enfermedad del sistema de conducción cardiaco, estenosis de la válvula pulmonar y miocardiopatía hipertrófica (incluida la familiar).
- **Interacciones farmacológicas** (9 registros en total, 5 de nivel moderado): amifostina, diatrizoato, anagrelida, ozanimod y procarbazina. Los otros 4 registros corresponden a dianas farmacológicas (PDE2A, PDE3A, PDE3B y PDE5A) y no a interacciones con otros fármacos.

Para el resto de la información de seguridad, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para alopecia se basa únicamente en el modelo (L5), sin ensayos clínicos ni literatura, y el mecanismo propuesto es especulativo. Además, el perfil de seguridad de milrinona (hipotensión, arritmias, necesidad de monitorización hospitalaria) es poco compatible con un uso en una condición no mortal como la alopecia.

**Para avanzar se necesita:**
- Estudios preclínicos que evalúen el efecto de la inhibición de PDE3 sobre el folículo piloso (modelos celulares o animales).
- Una evaluación de la viabilidad de una vía de administración tópica, ya que la vía inyectable no resulta adecuada para esta indicación.
- Datos de seguridad del prospecto de AEMPS (advertencias y contraindicaciones oficiales).
- Una comparación con alternativas ya establecidas (minoxidil, inhibidores de JAK).

**Nota:** Entre las demás predicciones para milrinona, **insuficiencia cardiaca congestiva** y **enfermedad cardiaca pulmonar aguda** tienen evidencia de nivel L2 (decisión "Proceed with Guardrails"). Ambas se sitúan dentro del ámbito cardiovascular donde el fármaco ya se usa. La predicción para **trastorno de cefalea** (L4) se apoya solo en informes de casos de síndrome de vasoconstricción cerebral reversible (SVCR), no en cefaleas primarias.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

