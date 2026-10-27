---
layout: default
title: Haloperidol
parent: Solo predicción del modelo (L5)
nav_order: 390
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Haloperidol: nueva indicación predicha, Trastorno congénito de glicosilación con fucosilación defectuosa (nivel de evidencia L5). Indicación original: Trastorno psicótico (incluye esquizofrenia, tras…"
monitor_inn: "HALOPERIDOL"
predicted_indications: ["congenital disorder of glycosylation with defective fucosylation", "retinal dystrophy with or without extraocular anomalies", "hydranencephaly (disease)", "myopia X-linked", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "myopia 26, X-linked, female-limited", "syndromic myopia", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "atypical glycine encephalopathy", "manic bipolar affective disorder"]
---

# Haloperidol
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

## Haloperidol: De Trastorno Psicótico a Trastorno Congénito de Glicosilación con Fucosilación Defectuosa
{: .text-alpha }

## Resumen en Una Frase

Haloperidol es un antipsicótico clásico, utilizado originalmente para tratar trastornos psicóticos como la esquizofrenia y el síndrome de Tourette.
El modelo TxGNN predice que podría ser efectivo para el **trastorno congénito de glicosilación con fucosilación defectuosa**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastorno psicótico (incluye esquizofrenia, trastorno esquizoafectivo, trastorno esquizofreniforme y síndrome de Tourette) |
| Nueva Indicación Predicha | Trastorno congénito de glicosilación con fucosilación defectuosa |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Por conocimiento general, haloperidol es un antagonista del receptor de dopamina D2. Su eficacia en psicosis y esquizofrenia está bien establecida, y ese efecto se explica por la reducción de la hiperactividad dopaminérgica.

La nueva indicación es muy distinta de la original. Los trastornos congénitos de glicosilación con fucosilación defectuosa son enfermedades metabólicas hereditarias raras. Se asocian al transporte de GDP-fucosa (por ejemplo, el gen SLC35C1) y a la modificación de proteínas con azúcares. No se identificó ninguna relación mecanística plausible entre el bloqueo de receptores D2 y estas vías.

El puntaje del modelo es muy alto (99.91%), pero es un resultado computacional sin respaldo experimental ni clínico. Por ello, la predicción debe considerarse una hipótesis sin fundamento mecanístico evidente, no una pista terapéutica.

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
| 58355 | Haloperidol Esteve 2 mg/ml solución oral | Solución oral | — |
| 58343 | Haloperidol Esteve 10 mg comprimidos | Comprimido | — |
| 55576 | Haloperidol Prodes 10 mg comprimidos | Comprimido | — |
| 33488 | Haloperidol Prodes 2 mg/ml gotas orales en solución | Gotas orales en solución | — |
| 58345 | Haloperidol Esteve 5 mg/ml solución inyectable | Solución inyectable | — |

Las cinco autorizaciones son de medicamentos de un solo principio activo y están vigentes. El texto de la indicación aprobada no figura en los datos compilados.

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: se registraron unas 100 interacciones. Entre las de nivel **mayor** figuran bupropión, morfina, claritromicina y dolasetrón. Hay además numerosas interacciones de nivel moderado, por ejemplo con famotidina, epinefrina, hidrocortisona, anfotericina B, atropina, loperamida y aprepitant.
- **Condiciones de precaución o contraindicación según la base de conocimiento** (no proceden del prospecto): síndrome de QT largo y torsades de pointes, epilepsia, enfermedades de los ganglios basales y distonías, enfermedad hepática y de la vesícula biliar, hipotiroidismo, deficiencia de potasio, neutropenia, agranulocitosis y leucopenia (incluidas las neutropenias congénitas), hipotensión, carcinoma de mama y síndrome neuroléptico maligno.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para esta indicación es solo computacional (nivel L5), sin ensayos, sin literatura y sin vínculo mecanístico plausible con el mecanismo antidopaminérgico del fármaco. Además, haloperidol tiene un perfil de seguridad exigente (QT, efectos extrapiramidales, numerosas interacciones), lo que no justifica avanzar sin una base científica.

**Para avanzar se necesita:**
- Una hipótesis mecanística que conecte la antagonización de D2 con la vía de fucosilación o transporte de GDP-fucosa
- Estudios preclínicos in vitro o en modelos celulares de la enfermedad
- Datos completos de mecanismo de acción y de advertencias y contraindicaciones del prospecto de la AEMPS
- Evaluación de la viabilidad en una población pediátrica con una enfermedad rara

**Nota:** entre las predicciones secundarias del modelo, el **trastorno afectivo bipolar maníaco** tiene el respaldo más sólido de los datos compilados: 3 ensayos clínicos y múltiples revisiones sistemáticas y metaanálisis, con haloperidol como comparador activo en un ensayo de Fase 3 completado (NCT00129220). Esa indicación ya está respaldada por guías clínicas y su evaluación corresponde a un informe aparte. Otras predicciones, como la distrofia retiniana, solo cuentan con estudios preclínicos en animales, y las relacionadas con la miopía son especulativas y posiblemente desfavorables.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

