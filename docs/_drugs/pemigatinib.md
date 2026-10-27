---
layout: default
title: Pemigatinib
parent: Solo predicción del modelo (L5)
nav_order: 620
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Pemigatinib: nueva indicación predicha, Neoplasia endocrina múltiple (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (el texto de indicación de las…"
monitor_inn: "PEMIGATINIB"
predicted_indications: ["multiple endocrine neoplasia", "amenorrhea (disease)", "HER2 positive breast carcinoma", "cytomegalovirus infection", "malignant catarrh", "infectious bovine rhinotracheitis", "amyotrophic lateral sclerosis", "amyotrohpic lateral sclerosis type 22", "amyotrophic lateral sclerosis, susceptibility to", "axial spondylometaphyseal dysplasia"]
---

# Pemigatinib
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

## Pemigatinib: De Indicación Original No Disponible a Neoplasia Endocrina Múltiple
{: .text-alpha }

## Resumen en Una Frase

Pemigatinib es un inhibidor selectivo de los receptores FGFR1-3 que se comercializa en España con tres autorizaciones vigentes; los datos compilados para este informe no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **neoplasia endocrina múltiple**, con un puntaje muy alto (99,71%).
Sin embargo, actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (el texto de indicación de las autorizaciones está vacío) |
| Nueva Indicación Predicha | Neoplasia endocrina múltiple |
| Puntaje de Predicción TxGNN | 99,71% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Pemigatinib es un inhibidor selectivo de la tirosina quinasa de FGFR1, FGFR2 y FGFR3. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados; la descripción anterior procede del conocimiento general sobre el fármaco y de la valoración mecanística asociada a la predicción.

Algunos tumores endocrinos presentan implicación de la vía FGFR, lo que ofrece una plausibilidad biológica muy general. No obstante, los síndromes de neoplasia endocrina múltiple suelen estar impulsados por alteraciones en genes como MEN1 o RET, y los datos disponibles no respaldan un vínculo directo entre la inhibición de FGFR y estas enfermedades.

Por tanto, el puntaje elevado del modelo debe interpretarse con cautela: es una predicción basada en el grafo de conocimiento, sin ensayos ni literatura que la sustenten, y la similitud con la indicación original no pudo evaluarse.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal (neoplasia endocrina múltiple).

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1211535001 | PEMAZYRE 4,5 mg comprimidos | Comprimido | No disponible |
| 1211535005 | PEMAZYRE 13,5 mg comprimidos | Comprimido | No disponible |
| 1211535003 | PEMAZYRE 9 mg comprimidos | Comprimido | No disponible |

Titular: Incyte Biosciences Distribution B.V.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de quinasa FGFR) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto (en general, fósforo sérico, función hepática y renal, hemograma) |
| Protección en Manejo | Consultar el prospecto y la normativa local de manejo de medicamentos antineoplásicos |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 50 interacciones en total. Entre las listadas, las de nivel **mayor** son:
  - Aprepitant
  - Dexametasona
  - Claritromicina
  - Cobicistat
  - Lumacaftor
  - Cloranfenicol
  - Eritromicina
  - Ketoconazol
  - Fluconazol

  Las de nivel **moderado** incluyen cimetidina, metreleptina, clotrimazol, fenilbutirato de glicerol, troglitazona, deferasirox, ivacaftor, zafirlukast, griseofulvina, elagolix y osilodrostat. Muchas de ellas son inhibidores o inductores del metabolismo enzimático, por lo que conviene revisar la medicación concomitante.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto, pero carece de ensayos clínicos y literatura (nivel L5) y no existe un vínculo mecanístico respaldado con los síndromes de neoplasia endocrina múltiple. Además, faltan datos de indicación aprobada y de seguridad de la ficha técnica.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha técnica de AEMPS (indicación aprobada, advertencias y contraindicaciones)
- Completar los datos del mecanismo de acción desde DrugBank
- Revisar literatura preclínica sobre FGFR en tumores endocrinos y síndromes MEN
- Valorar si existen candidatas con mayor respaldo entre las otras predicciones; por ejemplo, el carcinoma de mama HER2 positivo cuenta con plausibilidad indirecta (FGFR1 y resistencia terapéutica), aunque solo con una revisión general (nivel L4)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

