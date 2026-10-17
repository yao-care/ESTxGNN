---
layout: default
title: Apraclonidine
parent: Solo predicción del modelo (L5)
nav_order: 62
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Apraclonidine: nueva indicación predicha, Glaucoma hereditario primario (nivel de evidencia L5). Indicación original: Glaucoma de ángulo abierto (según el grafo de conocimiento…"
---

# Apraclonidine
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

# Apraclonidina: De Glaucoma de Ángulo Abierto a Glaucoma Hereditario Primario

## Resumen en Una Frase

Apraclonidina es un agonista alfa-2 adrenérgico de uso oftálmico, originalmente utilizado para el tratamiento del glaucoma de ángulo abierto.
El modelo TxGNN predice que podría ser efectivo para **glaucoma hereditario primario**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Glaucoma de ángulo abierto (según el grafo de conocimiento, ya que los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Glaucoma hereditario primario |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Apraclonidina es un agonista alfa-2 adrenérgico (con actividad alfa-1 débil) que reduce la presión intraocular (PIO) al disminuir la producción de humor acuoso. Los datos compilados confirman su unión a los receptores adrenérgicos α2A (ADRA2A) y α2C (ADRA2C). Actualmente no se dispone de datos detallados oficiales sobre el mecanismo de acción; la descripción anterior procede del análisis de plausibilidad mecanística.

El glaucoma de ángulo abierto y el glaucoma hereditario primario (por ejemplo, formas congénitas o juveniles) comparten la elevación de la PIO como principal factor modificable de la enfermedad. Es probable que esta superposición explique el puntaje alto del modelo (0.9988) en el grafo de conocimiento.

Sin embargo, es una predicción puramente computacional, sin evidencia directa en glaucoma hereditario o congénito. Además, existe una preocupación importante en población pediátrica, la más afectada por el glaucoma congénito primario: los agonistas alfa-2 (como la brimonidina y, por efecto de clase, la apraclonidina) conllevan riesgo de depresión del sistema nervioso central, apnea, bradicardia, hipotensión y somnolencia en lactantes y niños pequeños. A esto se suman la taquifilaxia y la alta tasa de reacciones alérgicas oculares con el uso prolongado, que limitan el tratamiento crónico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 60634 | IOPIMAX 5 mg/ml colirio en solución | Colirio en solución | No disponible en los datos compilados |
| 61225 | IOPIMAX 10 mg/ml colirio en solución | Colirio en solución | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): hipertensión y trastornos hipertensivos, trombocitopenia y púrpura trombocitopénica, anemia de Diamond-Blackfan, anemia aplásica hereditaria, neutropenia, agranulocitosis, trastornos de la coagulación, hiperlipidemia (incluida la familiar), colestasis (incluidas las formas intrahepáticas recurrentes y familiares), úlcera péptica activa, hemorragia intracerebral, leucemia, déficit de ácido ascórbico y escorbuto.
- **Interacciones farmacológicas / farmacología**: se registran interacciones con los receptores α2A-adrenérgico (ADRA2A) y α2C-adrenérgico (ADRA2C), coherentes con su acción como agonista alfa-2. No se han identificado interacciones con otros fármacos.
- **Población pediátrica**: riesgo de depresión del SNC, apnea, bradicardia, hipotensión y somnolencia (efecto de clase de los agonistas alfa-2), relevante para el glaucoma congénito.
- **Uso prolongado**: taquifilaxia y elevada frecuencia de reacciones alérgicas oculares.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y el riesgo de seguridad en población pediátrica, la principal afectada por el glaucoma hereditario, es significativo.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de la AEMPS (advertencias y contraindicaciones oficiales).
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión bibliográfica específica sobre apraclonidina en glaucoma congénito/juvenil.
- Evaluar la seguridad pediátrica y la viabilidad del uso crónico dada la taquifilaxia y las reacciones alérgicas.
- Confirmar los textos de indicación aprobada de las dos autorizaciones españolas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

