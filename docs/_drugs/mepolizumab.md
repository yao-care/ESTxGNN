---
layout: default
title: Mepolizumab
parent: Solo predicción del modelo (L5)
nav_order: 504
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
monitor_inn: "MEPOLIZUMAB"
predicted_indications: ["thrombocytopenia due to immune destruction", "primary release disorder of platelets", "pseudo-von Willebrand disease", "autoimmune thrombocytopenic", "Glanzmann thrombasthenia"]
description: "Mepolizumab: nueva indicación predicha, Trombocitopenia por destrucción inmune (thrombocytopenia due to immune destruction) (nivel de evidencia L5). Indicación original: No consta en los datos locale"
---

# Mepolizumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Mepolizumab: Trombocitopenia por destrucción inmune (thrombocytopenia due to immune destruction)
{: .text-alpha }

## Resumen en Una Frase

Mepolizumab es un anticuerpo monoclonal anti-IL-5, originalmente utilizado en enfermedades eosinofílicas como la neumonía eosinofílica y la eosinofilia pulmonar.
El modelo TxGNN predice que podría ser efectivo para **trombocitopenia por destrucción inmune**,
pero actualmente solo cuenta con **0 ensayos clínicos** y **1 publicación** (un reporte de caso) que respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Trombocitopenia por destrucción inmune (thrombocytopenia due to immune destruction) |
| Puntaje de Predicción TxGNN | 0.9966 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 3 de 4) |
| Número de Autorizaciones | 4 (vigentes: 3) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Mepolizumab es un anticuerpo monoclonal que bloquea la interleucina-5 (IL-5) y, con ello, reduce los eosinófilos. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada; esta descripción se basa en el conocimiento general de la clase del fármaco.

La relación con la nueva indicación es limitada. Un vínculo plausible solo existiría en el subgrupo de pacientes en que una desregulación inmune impulsada por eosinófilos (por ejemplo, síndrome hipereosinofílico con diátesis inmune resistente a esteroides) contribuya a la destrucción de plaquetas. No hay evidencia de que el bloqueo de IL-5 actúe sobre los mecanismos centrales de la trombocitopenia inmune primaria (aclaramiento plaquetario mediado por autoanticuerpos y receptores Fc, y alteración de la megacariopoyesis).

El puntaje TxGNN muy alto (0.9966) es una predicción computacional y no sustituye a los datos clínicos. Las otras indicaciones predichas (trastorno primario de liberación plaquetaria, pseudo-enfermedad de von Willebrand, trombocitopenia autoinmune y trombastenia de Glanzmann) tienen aún menos respaldo mecanístico; la entrada "trombocitopenia autoinmune" se solapa conceptualmente con la analizada aquí y debería reconciliarse para no duplicar la evaluación de evidencia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28648630](https://pubmed.ncbi.nlm.nih.gov/28648630/) | 2018 | Reporte de caso | Blood Cells, Molecules & Diseases | Resolución de una diátesis inmune hipereosinofílica resistente a esteroides con mepolizumab, con mejoría concomitante de una microangiopatía trombótica mixta (contexto de síndrome hemolítico urémico atípico) |

Se trata de un único reporte de caso en un contexto distinto a la trombocitopenia inmune primaria, por lo que constituye evidencia indirecta y de bajo nivel.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1151043003 | NUCALA 100 MG solución inyectable en pluma precargada | Solución inyectable en pluma precargada | No disponible |
| 1151043009 | NUCALA 40 MG solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada | No disponible |
| 1151043005 | NUCALA 100 MG solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada | No disponible |
| 1151043001 | NUCALA 100 MG polvo para solución inyectable | Polvo para solución inyectable | No disponible |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en un puntaje computacional y en un único reporte de caso en un contexto distinto; no hay ensayos clínicos y el vínculo mecanístico con la trombocitopenia inmune primaria no está respaldado.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de AEMPS (advertencias y contraindicaciones), requisito previo para el cribado de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Evaluar si existe un subgrupo con inmunodesregulación mediada por eosinófilos donde el bloqueo de IL-5 sea biológicamente relevante
- Reconciliar las entradas "trombocitopenia por destrucción inmune" y "trombocitopenia autoinmune" para evitar duplicidad
- Buscar estudios observacionales o ensayos que justifiquen avanzar a una fase de evaluación posterior
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

