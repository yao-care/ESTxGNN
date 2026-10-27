---
layout: default
title: Carteolol
parent: Solo predicción del modelo (L5)
nav_order: 149
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Carteolol: nueva indicación predicha, Glaucoma hereditario primario (nivel de evidencia L5). Indicación original: Glaucoma de ángulo abierto e hipertensión ocular (el texto de indicac…"
---

# Carteolol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Carteolol: De Hipertensión Ocular y Glaucoma de Ángulo Abierto a Glaucoma Hereditario Primario
{: .text-alpha }

## Resumen en Una Frase

Carteolol es un betabloqueante no selectivo con actividad simpaticomimética intrínseca, utilizado originalmente para el glaucoma de ángulo abierto y la hipertensión ocular (el grafo de conocimiento también lo asocia con la hipertensión arterial).
El modelo TxGNN predice que podría ser efectivo para **glaucoma hereditario primario**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: se trata solo de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Glaucoma de ángulo abierto e hipertensión ocular (el texto de indicación aprobado no figura en las autorizaciones; se toma de las indicaciones del grafo de conocimiento) |
| Nueva Indicación Predicha | Glaucoma hereditario primario |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Carteolol es un betabloqueante adrenérgico no selectivo con actividad simpaticomimética intrínseca, comercializado en forma oftálmica. Reduce la presión intraocular (PIO) al disminuir la producción de humor acuoso en el cuerpo ciliar. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente consultada; la descripción anterior procede del análisis de la relación mecanística y no ha podido contrastarse con el registro original.

El glaucoma hereditario primario (por ejemplo, el glaucoma congénito primario, con variantes en CYP1B1 o MYOC) también se caracteriza por una PIO elevada. Por ello, reducir la presión mediante betabloqueo es plausible como mecanismo sintomático, dirigido a la presión.

Conviene, sin embargo, ser prudentes: la causa de fondo es del desarrollo o genética (disgenesia de la malla trabecular o del ángulo de la cámara anterior) y carteolol no la corrige. El puntaje tan alto de TxGNN (0.999) probablemente refleja la cercanía en el grafo con las indicaciones aprobadas de glaucoma y es únicamente una predicción computacional.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 71069 | ARTEOPTIC 10 mg/ml Unidosis | Colirio de liberación prolongada | No disponible en los datos compilados |
| 89580 | ARTEOPTIC PF 2% | Colirio en solución de liberación prolongada | No disponible en los datos compilados |
| 71070 | ARTEOPTIC 20 mg/ml Unidosis | Colirio de liberación prolongada | No disponible en los datos compilados |
| 66383 | ARTEOPTIC 1% | Colirio de liberación prolongada | No disponible en los datos compilados |
| 59039 | ELEBLOC 20 mg/ml | Colirio en solución | No disponible en los datos compilados |

Hay una sexta autorización vigente (66366, ARTEOPTIC 2% colirio de liberación prolongada), hasta un total de 6 autorizaciones válidas.

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no el prospecto)**: bronquitis, asma (incluidos asma intrínseco y alérgico), enfisema pulmonar, diabetes mellitus, cetoacidosis diabética, miastenia gravis y enfermedades de la unión neuromuscular, bloqueo auriculoventricular, insuficiencia cardíaca (incluida la congestiva) y anafilaxia.
- **Interacciones Farmacológicas**: se registraron 100 interacciones; entre las 20 primeras reveladas, las de gravedad **mayor** son:
  - Epinefrina
  - Dolasetrón

  Entre las de gravedad moderada figuran corticoides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida), anticolinérgicos (atropina, hiosciamina, metescopolamina, diciclomina), bupropión, cimetidina, canagliflozina, dapagliflozina, clorpropamida y sales de calcio. Las de gravedad menor incluyen ácido acetilsalicílico y óxido de magnesio.

Las advertencias y contraindicaciones del prospecto de la AEMPS no estaban disponibles; consultar el prospecto para la información de seguridad oficial.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y la etiología del glaucoma hereditario primario es del desarrollo o genética, por lo que el efecto de carteolol sería, como máximo, sintomático (reducción de la PIO).

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), un vacío bloqueante para el cribado de seguridad.
- Obtener datos del mecanismo de acción desde DrugBank.
- Buscar literatura y ensayos sobre el uso de betabloqueantes tópicos en glaucoma congénito o juvenil, y su perfil de seguridad en población pediátrica.
- Evaluar la compatibilidad de vías y formulaciones (los productos actuales son colirios) con la población objetivo.
- Valorar la relevancia de las contraindicaciones cardiorrespiratorias en pacientes pediátricos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

