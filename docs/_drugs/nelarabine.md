---
layout: default
title: Nelarabine
parent: Solo predicción del modelo (L5)
nav_order: 558
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Nelarabine: nueva indicación predicha, Esclerosis múltiple remitente-recurrente (nivel de evidencia L5). Indicación original: Leucemia linfoblástica aguda / leucemia de células T / linfoma linfob…"
monitor_inn: "Nelarabine"
predicted_indications: ["relapsing-remitting multiple sclerosis"]
---

# Nelarabine
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

## Nelarabina: De Leucemia Linfoblástica Aguda a Esclerosis Múltiple Remitente-Recurrente
{: .text-alpha }

## Resumen en Una Frase

Nelarabina es un análogo de nucleósidos de purina, utilizado originalmente para el tratamiento de la leucemia linfoblástica aguda de células T y del linfoma linfoblástico T.
El modelo TxGNN predice que podría ser efectivo para **esclerosis múltiple remitente-recurrente**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Leucemia linfoblástica aguda / leucemia de células T / linfoma linfoblástico T (según el grafo de conocimiento; el texto de indicación de la autorización en España no está disponible) |
| Nueva Indicación Predicha | Esclerosis múltiple remitente-recurrente |
| Puntaje de Predicción TxGNN | 99.43% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Según la información conocida, la nelarabina es un profármaco de ara-G, un análogo de la desoxiguanosina que se convierte en ara-GTP y se incorpora al ADN, causando citotoxicidad preferente en los linfocitos T. Su eficacia en neoplasias linfoides de células T es el motivo de su uso original.

La relación con la nueva indicación es teórica: se considera que la esclerosis múltiple remitente-recurrente implica actividad de linfocitos T autorreactivos, y fármacos que depletan linfocitos (como la cladribina, otro análogo de nucleósidos de purina) son eficaces en esta enfermedad. Por tanto, mecanísticamente podría ser aplicable.

Esta vinculación se infiere por la clase del fármaco y **no está respaldada por datos específicos de nelarabina**. Además, existe una contradicción de seguridad importante: la nelarabina tiene una toxicidad neurológica grave conocida (somnolencia, confusión, convulsiones, ataxia, neuropatía periférica, desmielinización y parálisis ascendente tipo Guillain-Barré), lo cual es especialmente problemático en una enfermedad desmielinizante del sistema nervioso central. El puntaje elevado de TxGNN es solo una predicción del modelo, sin corroboración clínica ni bibliográfica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 07403001 | ATRIANCE 5 MG/ML SOLUCIÓN PARA PERFUSIÓN (Sandoz Pharmaceuticals D.D.) | Solución para perfusión | No disponible en los datos compilados |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (análogo de nucleósidos de purina / antimetabolito) |
| Riesgo de Mielosupresión | Alto (las contraindicaciones del grafo de conocimiento incluyen neutropenia, trombocitopenia y anemia como condiciones de riesgo) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma completo (con diferencial y plaquetas), función hepática y renal, bilirrubina, y vigilancia neurológica estrecha |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

- **Condiciones de riesgo según el grafo de conocimiento** (no proceden del texto del prospecto): insuficiencia hepática, epilepsia, trombocitopenia, neutropenia, agranulocitosis, enfermedades del sistema nervioso periférico, neuropatía periférica, anemia (incluida la macrocítica), hiperbilirrubinemia (incluidos el síndrome de Gilbert y las formas hereditarias), insuficiencia renal, discapacidad de aprendizaje, discapacidad intelectual, enfermedades desmielinizantes y polirradiculoneuropatía desmielinizante inflamatoria.
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Entre las principales de nivel **mayor** figuran bupropión, deferiprona, iopamidol, iohexol y lexidronam de samario (153Sm). Entre las de nivel **moderado** figuran metronidazol, tinidazol, secnidazol, benznidazol, rosuvastatina, simvastatina, cloroquina, hidroxicloroquina, disulfiram, palifermina, lindano, cloruro de estroncio Sr-89, ácido picosulfúrico, polietilenglicol (3350 con electrolitos) y sulfato de sodio.
- Para advertencias y contraindicaciones formales, consultar el prospecto.

Cabe destacar la coincidencia entre las condiciones de riesgo (enfermedades desmielinizantes, neuropatías, epilepsia) y la toxicidad neurológica de la nelarabina, que choca directamente con la nueva indicación propuesta.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y el perfil de neurotoxicidad grave y desmielinización de la nelarabina es contrario a su uso en una enfermedad desmielinizante como la esclerosis múltiple.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), actualmente un vacío de datos bloqueante para el cribado de seguridad
- Datos detallados del mecanismo de acción (por ejemplo, desde DrugBank)
- Estudios preclínicos que evalúen la relevancia mecanística en modelos de esclerosis múltiple
- Evaluación del balance beneficio-riesgo neurológico frente a alternativas de depleción linfocitaria ya aprobadas (como cladribina)
- Revisión sistemática de la literatura para identificar cualquier evidencia indirecta
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

