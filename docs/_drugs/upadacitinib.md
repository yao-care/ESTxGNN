---
layout: default
title: Upadacitinib
parent: Solo predicción del modelo (L5)
nav_order: 834
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Upadacitinib: nueva indicación predicha, Síndrome de microftalmia colobomatosa con displasia rizomélica (nivel de evidencia L5). Indicación original: Artritis reumatoide (según el grafo de conocimien…"
monitor_inn: "UPADACITINIB"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
---

# Upadacitinib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Upadacitinib: De Artritis Reumatoide a Síndrome de Microftalmia Colobomatosa con Displasia Rizomélica

## Resumen en Una Frase

Upadacitinib es un inhibidor selectivo de JAK1, originalmente utilizado para el tratamiento de la artritis reumatoide.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de microftalmia colobomatosa con displasia rizomélica**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Artritis reumatoide (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Síndrome de microftalmia colobomatosa con displasia rizomélica |
| Puntaje de Predicción TxGNN | 99,61% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, upadacitinib es un inhibidor selectivo de JAK1 que se emplea en enfermedades inflamatorias de base inmunitaria, y su eficacia en artritis reumatoide está establecida.

Sin embargo, **los datos disponibles no respaldan un vínculo mecanístico** con la nueva indicación. Este síndrome es un trastorno del desarrollo extremadamente raro, con malformaciones oculares y esqueléticas, y en general no está impulsado por inflamación mediada por la vía JAK-STAT. El puntaje del modelo es muy alto (0,996), pero es una predicción derivada del modelo; es probable que refleje un artefacto de proximidad en la red del grafo más que una base biológica real.

Como segunda predicción, el modelo propone el **síndrome de braquidactilia-sindactilia** (puntaje 99,58%), también una malformación congénita de origen genético y del desarrollo, sin respuesta esperable a la inmunomodulación en pacientes posnatales. Tampoco cuenta con evidencia clínica ni bibliográfica y recibe la misma recomendación de Hold.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1191404001 | RINVOQ 15 mg comprimidos de liberación prolongada | Comprimido de liberación prolongada | No disponible en los datos compilados |
| 1191404010 | RINVOQ 45 mg comprimidos de liberación prolongada | Comprimido de liberación prolongada | No disponible en los datos compilados |
| 1191404006 | RINVOQ 30 mg comprimidos de liberación prolongada | Comprimido de liberación prolongada | No disponible en los datos compilados |

Titular: Abbvie Deutschland GmbH & Co. KG.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; a continuación se muestran las principales de la muestra consultada.
  - **Gravedad mayor**: corticoides (hidrocortisona, triamcinolona, dexametasona, beclometasona, betametasona, budesonida, prednisona, prednisolona), claritromicina, cobicistat, deferiprona e iobenguano (I-131).
  - **Gravedad moderada**: aprepitant, cimetidina, miconazol y deferasirox.
  - **Gravedad menor**: sales de zinc (sulfato, acetato, gluconato).

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y carece de plausibilidad biológica: ambos síndromes predichos son malformaciones congénitas del desarrollo sin un componente inflamatorio mediado por JAK1 que justifique el tratamiento.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) de upadacitinib y un análisis de su posible relación con la fisiopatología del síndrome.
- Revisión de la ficha técnica de AEMPS (advertencias y contraindicaciones), actualmente no disponible.
- Evidencia preclínica o biológica que vincule la vía JAK1-STAT con el síndrome predicho.
- Una revisión sistemática de la literatura y de registros de ensayos que confirme la ausencia de estudios.
- Considerar priorizar otras indicaciones predichas con mayor plausibilidad mecanística.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

