---
layout: default
title: Salicylamide
parent: Evidencia moderada (L3-L4)
nav_order: 723
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Salicylamide: nueva indicación predicha, Faringitis (nivel de evidencia L4). Indicación original: Cefalea (trastorno de cefalea, según el grafo de conocimiento"
monitor_inn: "salicylamide"
predicted_indications: ["pharyngitis", "nasal cavity disease", "acute laryngopharyngitis", "trigeminal autonomic cephalalgia", "common cold", "allergic urticaria", "lung disease", "massive neonatal aspiration syndrome", "respiratory syncytial virus bronchiolitis", "hantavirus infectious disease"]
---

# Salicylamide
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Salicilamida: De Cefalea a Faringitis

## Resumen en Una Frase

La salicilamida es un analgésico y antipirético que originalmente se utiliza para el tratamiento de la cefalea (trastorno de cefalea).
El modelo TxGNN predice que podría ser efectiva para **faringitis**,
con **0 ensayos clínicos** y **1 publicación** (un informe clínico histórico de 1953) que respaldan actualmente esta dirección, por lo que la evidencia es muy limitada.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cefalea (trastorno de cefalea, según el grafo de conocimiento; el texto de indicación de la autorización no está disponible) |
| Nueva Indicación Predicha | Faringitis |
| Puntaje de Predicción TxGNN | 99,98% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la salicilamida es un derivado salicílico con actividad analgésica y antipirética. Su eficacia en la cefalea se considera establecida por su uso histórico, y mecanísticamente podría ser aplicable a la faringitis.

La relación entre ambas indicaciones es sintomática: el dolor y la fiebre asociados a la faringitis podrían aliviarse con un analgésico-antipirético. Se trataría de un alivio de síntomas, no de una modificación de la enfermedad ni de un efecto antiinfeccioso. La única publicación disponible (1953) describe el uso de salicilamida en combinación con p-aminobenzoato de sodio en la amigdalitis catarral infantil, por lo que no es posible aislar el efecto propio de la salicilamida.

El puntaje TxGNN es muy alto, pero es solo una predicción computacional y no sustituye a la evidencia clínica. Otras indicaciones predichas (resfriado común, laringofaringitis aguda) siguen la misma lógica sintomática y tampoco cuentan con ensayos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [13060598](https://pubmed.ncbi.nlm.nih.gov/13060598/) | 1953 | Informe clínico histórico (terapia combinada) | Gazzetta medica italiana | Tratamiento de la amigdalitis catarral en la infancia con salicilamida asociada a p-aminobenzoato de sodio; no se dispone de resumen y el efecto individual no puede separarse |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 47802 | YENDOL GRANULADO PARA SUSPENSIÓN ORAL | Granulado para suspensión oral | No disponible en los datos compilados |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como referencia adicional, el grafo de conocimiento (no el texto del prospecto) asocia la salicilamida con posibles contraindicaciones en enfermedades como: insuficiencia hepática y enfermedad hepática, enfermedad renal, úlcera péptica, gastritis, enfermedad inflamatoria intestinal, trombocitopenia, trastornos de la coagulación y hemofilia, anemias, hipertensión, hipotiroidismo, diabetes, gota, epilepsia, EPOC y colitis por *Clostridium difficile*. Esta lista no procede del prospecto y debe verificarse con la ficha técnica oficial.

No se encontraron interacciones farmacológicas en los datos compilados.

Un hallazgo relevante en la literatura de otras indicaciones predichas: varios artículos (1975-1985) indican que la salicilamida se ha estudiado como analgésico alternativo en pacientes con asma sensible a la aspirina, al parecer por su débil efecto sobre la síntesis de prostaglandinas. Aun así, requiere precaución en pacientes alérgicos o con asma, y el uso en lactantes y neonatos exige especial cautela.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única evidencia para faringitis es un informe clínico de 1953 con terapia combinada, sin ensayos clínicos, y el beneficio esperado sería únicamente sintomático. La predicción del modelo no es suficiente por sí sola para avanzar.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), actualmente sin datos
- Obtener datos del mecanismo de acción desde DrugBank
- Confirmar la indicación aprobada en la autorización española (el texto está vacío)
- Estudios clínicos modernos que aíslen el efecto de la salicilamida en el dolor faríngeo
- Evaluar la comparación frente a analgésicos ya establecidos (paracetamol, AINE)
- Valorar con cautela la indicación alternativa de "pulmón/asma sensible a analgésicos" como pregunta de investigación (la única con etapa S1), centrada en seguridad y no en tratamiento de la enfermedad
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

