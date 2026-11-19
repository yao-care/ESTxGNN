---
layout: default
title: Neostigmine
parent: Solo predicción del modelo (L5)
nav_order: 559
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-20
monitor_inn: "Neostigmine"
predicted_indications: ["autoimmune disease of peripheral nervous system", "disease of receptor activity", "hypersplenism (disease)", "atypical hemolytic-uremic syndrome with B factor anomaly", "bronchitis", "fetal akinesia deformation sequence", "myasthenia, congenital, refractory to acetylcholinesterase inhibitors"]
description: "Neostigmine: nueva indicación predicha, Autoimmune disease of peripheral nervous system (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 2 (comercializadas: 1)"
---

# Neostigmine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

## Neostigmine: Autoimmune disease of peripheral nervous system
{: .text-alpha }

## Resumen en Una Frase

Neostigmina es un inhibidor reversible de la acetilcolinesterasa, utilizado originalmente para el tratamiento de la miastenia gravis y de enfermedades de la unión neuromuscular.
El modelo TxGNN predice que podría ser efectivo para **miastenia gravis con hiperplasia de timo**, pero actualmente **no hay ensayos clínicos ni publicaciones** específicas que respalden esta indicación. Además, se trata de un subtipo de una indicación ya establecida, por lo que no constituye un reposicionamiento genuino.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Autoimmune disease of peripheral nervous system |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 2; revocadas o suspendidas: 1) |
| Número de Autorizaciones | 2 (comercializadas: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Neostigmine (traducción no oficial): «El metilsulfato de neostigmina es un inhibidor competitivo de la colinesterasa. Al reducir la degradación de la acetilcolina, el metilsulfato de neostigmina induce un aumento de la acetilcolina en la hendidura sináptica, que compite por el mismo sitio de unión que los bloqueantes neuromusculares no despolarizantes, y revierte el bloqueo neuromuscular.» Texto original en inglés: "Neostigmine methylsulfate is a competitive cholinesterase inhibitor. By reducing the breakdown of acetylcholine, neostigmine methylsulfate induces an increase in acetylcholine in the synaptic cleft which competes for the same binding site as nondepolarizing neuromuscular blocking agents, and reverses the neuromuscular blockade." ([DailyMed: neostigmine prescribing information, Medical Purchasing Solutions, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=95fb1b3d-be9a-fdb4-e053-2a95a90a5e90), versión del 2023-05-15; consultado el 2026-11-19). Según la información conocida, neostigmina es un inhibidor reversible de la acetilcolinesterasa (diana: ACHE) que aumenta la acetilcolina en la sinapsis de la unión neuromuscular. Esta es la base de su uso en la miastenia gravis.

La miastenia gravis con hiperplasia de timo es un subtipo de la misma enfermedad, por lo que el puntaje alto del modelo es plausible. Sin embargo, precisamente por ello no representa una oportunidad real de reposicionamiento: la indicación ya está cubierta por el uso conocido del fármaco. No se dispone de ensayos ni literatura específicos para este subtipo.

Entre las demás predicciones, solo la **miastenia gravis neonatal transitoria** (nivel L4, etapa S1, "pregunta de investigación") muestra evidencia algo más consistente, basada en series y reportes de casos. Otras predicciones (hiperesplenismo, síndrome hemolítico urémico atípico, bronquitis, miastenia congénita refractaria a inhibidores de la acetilcolinesterasa) carecen de fundamento mecanístico o presentan conflicto con el mecanismo del fármaco.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación específica.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 4237 | PROSTIGMINE AMPOLLAS (Meda Pharma S.L.) | Solución inyectable | No disponible en los datos compilados |
| 36384 | NEOSTIGMINA BRAUN 0,5 MG/ML (B Braun Medical S.A.) | Solución inyectable | No disponible en los datos compilados |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): epilepsia, úlcera péptica, asma (intrínseco y alérgico), paro cardíaco súbito, enfermedad del sistema de conducción cardíaco, peritonitis, hipertiroidismo (enfermedad de Graves, tirotoxicosis), obstrucción de las vías urinarias y enfermedad de Hirschsprung (incluidos síndromes asociados, como Mowat-Wilson).
- **Interacciones farmacológicas**: solo se registró la interacción farmacológica con su diana, la acetilcolinesterasa (inhibición), sin datos de interacciones con otros fármacos.
- Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción corresponde a un subtipo de una indicación ya conocida, con puntaje alto pero sin ensayos ni literatura específicos (nivel L5). No supone una oportunidad real de reposicionamiento.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS para confirmar las indicaciones autorizadas, advertencias y contraindicaciones
- Confirmar si la miastenia gravis con hiperplasia de timo ya está cubierta por la indicación autorizada
- Completar los datos del mecanismo de acción desde DrugBank
- Si se desea explorar un reposicionamiento real, priorizar la miastenia gravis neonatal transitoria, evaluando dosificación y seguridad neonatal

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: neostigmine prescribing information, Medical Purchasing Solutions, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=95fb1b3d-be9a-fdb4-e053-2a95a90a5e90) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

