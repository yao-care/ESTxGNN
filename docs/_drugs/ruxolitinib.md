---
layout: default
title: Ruxolitinib
parent: Solo predicción del modelo (L5)
nav_order: 718
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ruxolitinib: nueva indicación predicha, Tumor de células epitelioides perivasculares (PEComa) del cuerpo uter… (nivel de evidencia L5). Indicación original: Neoplasias mieloproliferativas (mielofibro…"
---

# Ruxolitinib
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

# Ruxolitinib: De Mielofibrosis y Policitemia Vera a Neoplasia PEComa Perivascular Epitelioide del Cuerpo Uterino

## Resumen en Una Frase

Ruxolitinib es un inhibidor de JAK1/JAK2 utilizado originalmente en neoplasias mieloproliferativas, como la mielofibrosis primaria y la policitemia vera.
El modelo TxGNN predice que podría ser efectivo para el **tumor de células epitelioides perivasculares (PEComa) del cuerpo uterino**,
pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción concreta: es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Neoplasias mieloproliferativas (mielofibrosis primaria, policitemia vera adquirida), según el grafo de conocimiento; el texto de indicación de las autorizaciones españolas no está disponible |
| Nueva Indicación Predicha | Tumor de células epitelioides perivasculares (PEComa) del cuerpo uterino |
| Puntaje de Predicción TxGNN | 99.73% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, ruxolitinib es un inhibidor de las quinasas JAK1 y JAK2 de la vía JAK-STAT. Su eficacia en neoplasias mieloproliferativas, caracterizadas por una señalización JAK-STAT hiperactiva, está establecida.

Para el PEComa uterino, el vínculo mecanístico es **especulativo**. El PEComa se asocia principalmente con la vía mTOR, y solo se plantea una posible interacción con la señalización JAK-STAT. Los datos compilados no aportan ensayos ni literatura que confirmen esta relación. La puntuación alta del modelo probablemente refleja relaciones del grafo de conocimiento y no evidencia biológica directa.

**Otras predicciones del modelo.** Entre las 10 principales, otras dos tienen algo más de respaldo:
- **Síndrome hemofagocítico asociado a infección (HLH)**: nivel L3, con 20 publicaciones. Incluye estudios clínicos pediátricos, series de casos y modelos murinos que apoyan la inhibición de JAK/STAT en la hiperinflamación mediada por IFN-γ. Es la dirección mejor respaldada, pero no es la de mayor puntaje. Sus estudios deberían evaluarse en un informe específico.
- **Liposarcoma**: nivel L4, con 2 estudios preclínicos sobre JAK-STAT en el liposarcoma mixoide.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 112773015 | JAKAVI 10 MG COMPRIMIDOS | Comprimido | No disponible en los datos |
| 112773017 | JAKAVI 5 MG/ML SOLUCIÓN ORAL | Solución oral | No disponible en los datos |
| 112773011 | JAKAVI 20 MG COMPRIMIDOS | Comprimido | No disponible en los datos |
| 112773008 | JAKAVI 15 MG COMPRIMIDOS | Comprimido | No disponible en los datos |
| 112773005 | JAKAVI 5 MG COMPRIMIDOS | Comprimido | No disponible en los datos |

Existe además una sexta autorización, OPZELURA 15 MG/G CREMA (Incyte Biosciences Distribution B.V.; n.º 1231726001), en forma de crema (formulación tópica). Jakavi pertenece a Novartis Europharm Limited.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de JAK1/JAK2), no citotóxico convencional |
| Riesgo de Mielosupresión | Medio a alto: la trombocitopenia, la anemia y la neutropenia son efectos conocidos de la clase. Consultar el prospecto |
| Clasificación de Emetogenicidad | Baja |
| Items de Monitoreo | Hemograma completo con diferencial, función hepática y renal, perfil lipídico; vigilancia de infecciones |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Las más relevantes de las mostradas son:
  - **Mayores**: claritromicina, cobicistat, deferasirox, deferiprona, ibritumomab tiuxetán, tositumomab (incluido tositumomab I-131) y lexidronam de samario (153Sm).
  - **Moderadas**: dexametasona, rosuvastatina, dexfenfluramina, fenfluramina, sibutramina, troglitazona, palifermina y cloruro de estroncio Sr-89.
  - **Menores**: aprepitant, cimetidina, miconazol y clotrimazol.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para el PEComa uterino se basa únicamente en el modelo (L5), sin ensayos, literatura ni un mecanismo respaldado por los datos. No es posible avanzar con esta indicación en este momento.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) de ruxolitinib a partir de DrugBank.
- Advertencias y contraindicaciones del prospecto de la AEMPS, actualmente sin datos.
- Estudios preclínicos que evalúen la señalización JAK-STAT en PEComa.
- Considerar priorizar la evaluación de HLH, la indicación con mayor evidencia (L3) entre las predicciones, mediante un informe específico.
- Un plan de monitoreo hematológico y de interacciones, en especial con inhibidores potentes de CYP3A4 como la claritromicina.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

