---
layout: default
title: Nortriptyline
parent: Evidencia alta (L1-L2)
nav_order: 577
evidence_level: L2
indication_count: 2
last_modified_at: 2026-10-14
monitor_inn: "Nortriptyline"
predicted_indications: ["attention deficit-hyperactivity disorder", "attention deficit hyperactivity disorder, inattentive type"]
description: "Nortriptyline: nueva indicación predicha, Attention deficit-hyperactivity disorder (nivel de evidencia L2). Indicación original: No consta en los datos locales"
---

# Nortriptyline
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **2** 
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

## Nortriptyline: Attention deficit-hyperactivity disorder
{: .text-alpha }

## Resumen en Una Frase

Nortriptilina es un antidepresivo tricíclico, originalmente utilizado para el tratamiento del trastorno de ansiedad, el trastorno neurótico y el trastorno distímico.
El modelo TxGNN predice que podría ser efectivo para el **trastorno por déficit de atención e hiperactividad (TDAH)**,
con **0 ensayos clínicos** registrados y **15 publicaciones** recuperadas, de las cuales solo una parte guarda relación directa con el tema.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Attention deficit-hyperactivity disorder |
| Puntaje de Predicción TxGNN | 0.9942 |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | Comercializado (registros vigentes: 2 de 3) |
| Número de Autorizaciones | 3 (vigentes: 2) |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la farmacología conocida de la clase, la nortriptilina es un antidepresivo tricíclico (amina secundaria) que inhibe principalmente la recaptación de noradrenalina (transportador NET) y, en menor medida, la de serotonina (transportador SERT). Los datos de farmacología recopilados confirman su interacción con NET, SERT y el receptor adrenérgico α1A, así como con canales de potasio Kir.

La ansiedad y la distimia son trastornos neuropsiquiátricos en los que intervienen los sistemas monoaminérgicos. El TDAH comparte esa base: la potenciación noradrenérgica, en particular en la corteza prefrontal, es un mecanismo reconocido para tratar el TDAH (como ocurre con la atomoxetina). Por ello, el vínculo es biológicamente plausible.

Cabe señalar que la puntuación tan alta de TxGNN respalda la predicción, pero no constituye por sí misma evidencia clínica. Además, el MOA original no está disponible, por lo que este razonamiento se apoya en la clase farmacológica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11052409](https://pubmed.ncbi.nlm.nih.gov/11052409/) | 2000 | ECA | J Child Adolesc Psychopharmacol | Estudio controlado de la eficacia y tolerabilidad de nortriptilina en TDAH pediátrico |
| [25238582](https://pubmed.ncbi.nlm.nih.gov/25238582/) | 2014 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Antidepresivos tricíclicos como segunda línea para reducir síntomas de TDAH en niños y adolescentes |
| [15064003](https://pubmed.ncbi.nlm.nih.gov/15064003/) | 2004 | Revisión | Psychiatr Clin North Am | Los tricíclicos, sobre todo los más noradrenérgicos (desipramina, nortriptilina), son alternativas establecidas, aunque limitadas por su estrecho índice terapéutico y toxicidad cardiovascular |
| [8428873](https://pubmed.ncbi.nlm.nih.gov/8428873/) | 1993 | Estudio clínico | J Am Acad Child Adolesc Psychiatry | Nortriptilina en niños con TDAH y trastorno de tics o síndrome de Tourette |
| [8444763](https://pubmed.ncbi.nlm.nih.gov/8444763/) | 1993 | Revisión de historias clínicas | J Am Acad Child Adolesc Psychiatry | Revisión de 58 casos tratados con nortriptilina por TDAH |
| [8444754](https://pubmed.ncbi.nlm.nih.gov/8444754/) | 1993 | Estudio retrospectivo | J Am Acad Child Adolesc Psychiatry | Niveles séricos y efectos electrocardiográficos de nortriptilina en niños y adolescentes |
| [12270803](https://pubmed.ncbi.nlm.nih.gov/12270803/) | 2002 | Revisión | Adolesc Med | Revisión de la psicofarmacología del TDAH en adolescentes, incluyendo nortriptilina |
| [22303520](https://pubmed.ncbi.nlm.nih.gov/22303520/) | 2012 | Guía clínica | Ann Clin Psychiatry | Recomendaciones CANMAT para trastornos del ánimo con TDAH comorbido |
| [22700161](https://pubmed.ncbi.nlm.nih.gov/22700161/) | 2012 | ECA | Pediatr Nephrol | Nortriptilina para la enuresis en niños con TDAH |
| [24345533](https://pubmed.ncbi.nlm.nih.gov/24345533/) | 2014 | Estudio PET | Int J Neuropsychopharmacol | Ocupación del transportador de noradrenalina por nortriptilina en pacientes con depresión |

*Nota: del conjunto recuperado se excluyeron publicaciones no relacionadas con nortriptilina en TDAH (por ejemplo, sobre alprazolam y metilfenidato).*

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 48462 | NORFENAZIN 10 MG COMPRIMIDOS | Comprimido | No disponible |
| 48463 | NORFENAZIN 25 MG COMPRIMIDOS | Comprimido | No disponible |
| 41448 | PAXTIBI 25 MG COMPRIMIDOS RECUBIERTOS | Comprimido recubierto | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no el texto del prospecto)**: síndrome de QT largo (incluida la forma familiar) y torsades de pointes; muerte súbita cardíaca y enfermedad del sistema de conducción cardíaco; infarto de miocardio y trombosis coronaria; ictus, enfermedad cerebrovascular e infarto cerebral; epilepsia; trastorno bipolar en fase maníaca; glaucoma (incluido el de ángulo abierto); hiperplasia benigna de próstata; hipertiroidismo (enfermedad de Graves, tirotoxicosis); insuficiencia hepática; insuficiencia renal y uremia; abuso o dependencia de sustancias; hemoglobinopatía.
- **Interacciones y dianas farmacológicas**: se identificaron 6 interacciones farmacológicas con dianas (receptor α1A, Kir3.2, Kir3.4, Kir4.1, NET y SERT). No se proporcionaron niveles de gravedad para ellas.
- **Seguridad cardiovascular en TDAH**: la literatura señala el estrecho índice terapéutico y la posible toxicidad cardiovascular de los tricíclicos, lo cual coincide con las contraindicaciones cardíacas anteriores. Se dispone además de un estudio sobre efectos electrocardiográficos en población pediátrica.

Las advertencias y contraindicaciones del prospecto de la AEMPS no pudieron obtenerse, por lo que se debe consultar el prospecto para completar la información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ECA pediátrico controlado, una revisión Cochrane y varios estudios clínicos que respaldan la dirección de uso en TDAH, con una puntuación TxGNN muy alta y un mecanismo noradrenérgico plausible. Sin embargo, no hay ensayos registrados y el perfil de seguridad cardiovascular exige precaución.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), un vacío de datos que bloquea el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Evaluar con detalle la eficacia y los riesgos cardiovasculares (ECG, niveles séricos) en las poblaciones objetivo, sobre todo niños y adolescentes.
- Confirmar las indicaciones aprobadas de las tres autorizaciones españolas, cuyo texto está vacío.
- Valorar ensayos clínicos modernos frente a los tratamientos de referencia (estimulantes, atomoxetina).

*Nota: la variante "TDAH, tipo inatento" (puntuación TxGNN 0,9933) no cuenta con ensayos ni literatura propios (nivel L5, decisión Hold); se considera un subtipo de la misma condición y queda cubierta por este análisis.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

