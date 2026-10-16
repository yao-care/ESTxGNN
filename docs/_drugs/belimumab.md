---
layout: default
title: Belimumab
parent: Solo predicción del modelo (L5)
nav_order: 90
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Belimumab: nueva indicación predicha, Trastorno primario de liberación plaquetaria (nivel de evidencia L5). Indicación original: Lupus eritematoso sistémico (el texto de indicación aprobado no está…"
monitor_inn: "BELIMUMAB"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "fetal and neonatal alloimmune thrombocytopenia", "severe nonproliferative diabetic retinopathy", "autosomal dominant macrothrombocytopenia"]
---

# Belimumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Belimumab: De Lupus Eritematoso Sistémico a Trastorno Primario de Liberación Plaquetaria

## Resumen en Una Frase

Belimumab es un anticuerpo monoclonal originalmente utilizado para el tratamiento del lupus eritematoso sistémico (incluido el lupus eritematoso sistémico pediátrico).
El modelo TxGNN predice que podría ser efectivo para el **trastorno primario de liberación plaquetaria**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Lupus eritematoso sistémico (el texto de indicación aprobado no está disponible en las autorizaciones; se toma de las indicaciones originales del grafo de conocimiento) |
| Nueva Indicación Predicha | Trastorno primario de liberación plaquetaria |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, belimumab es un inhibidor de BLyS (BAFF) que reduce la supervivencia de los linfocitos B y la producción de autoanticuerpos, y su eficacia en el lupus eritematoso sistémico, una enfermedad autoinmune mediada por linfocitos B, está establecida.

Sin embargo, los trastornos primarios de liberación plaquetaria son defectos de la función plaquetaria (anomalías de la secreción de gránulos), de origen hereditario o adquirido, y no se deben principalmente a la actividad de los linfocitos B ni a autoanticuerpos. No se ha establecido un vínculo mecanístico plausible. El alto puntaje de TxGNN parece reflejar una predicción basada en la red del grafo de conocimiento, sin respaldo clínico ni bibliográfico.

Otras predicciones del modelo (todas con nivel L5 y recomendación Hold):

| Enfermedad predicha | Puntaje TxGNN | Valoración mecanística |
|------|------|------|
| Pseudo-enfermedad de von Willebrand | 99.96% | Defecto genético de gananancia de función de GPIbα; sin justificación para inhibir BLyS |
| Trombastenia de Glanzmann | 99.88% | Déficit hereditario de la integrina αIIbβ3; solo un vínculo especulativo con aloanticuerpos tras transfusiones |
| Trombocitopenia aloinmune fetal y neonatal | 99.59% | La más plausible biológicamente (aloanticuerpos maternos anti-HPA-1a); pero belimumab no depleciona eficazmente las células plasmáticas establecidas, hay pocos datos de seguridad en el embarazo y el desarrollo actual se centra en el bloqueo de FcRn y la inmunoglobulina hiperinmune anti-HPA-1a |
| Retinopatía diabética no proliferativa grave | 99.05% | Enfermedad microvascular sin papel establecido de BAFF/BLyS |
| Macrotrombocitopenia autosómica dominante | 99.04% | Defecto hereditario de producción plaquetaria o citoesqueleto; no autoinmune |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 11700001 | BENLYSTA 120 mg polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión | No disponible en los datos compilados |
| 11700002 | BENLYSTA 400 mg polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión | No disponible en los datos compilados |
| 111700004 | BENLYSTA 200 mg solución inyectable en pluma precargada | Solución inyectable en pluma precargada | No disponible en los datos compilados |

Titular de las tres autorizaciones: Glaxosmithkline (Ireland) Limited.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 69 interacciones en total; a continuación se listan las principales de las 20 detalladas en los datos compilados:
  - **Mayor**: adalimumab, baricitinib, certolizumab pegol, vacuna BCG (cepa Tice, viva).
  - **Moderada**: roflumilast, anakinra, alefacept, alemtuzumab, azatioprina, canakinumab, vacunas (toxoide tetánico, ántrax, adenovirus tipo 4, cólera viva), *Candida albicans*, *Bifidobacterium longum infantis*.
  - **Menor**: sales de zinc (acetato, gluconato, sulfato, cloruro).

  En conjunto, las interacciones relevantes se relacionan con inmunosupresión adicional (otros biológicos e inmunosupresores) y con vacunas vivas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Las seis predicciones son únicamente del modelo (L5), sin ensayos clínicos ni publicaciones, y para la indicación principal no existe un vínculo mecanístico plausible con la inhibición de BLyS. La predicción más defendible biológicamente es la trombocitopenia aloinmune fetal y neonatal, pero sigue siendo hipotética.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), cuya ausencia impide el cribado de seguridad.
- Completar los datos del mecanismo de acción del fármaco (por ejemplo, consultando DrugBank).
- Revisión sistemática de literatura y de registros de ensayos para las indicaciones predichas.
- Si se desea priorizar una línea, valorar estudios preclínicos o de mecanismo en trombocitopenia aloinmune fetal y neonatal, considerando la seguridad en el embarazo y las alternativas actuales (bloqueo de FcRn, inmunoglobulina hiperinmune anti-HPA-1a).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

