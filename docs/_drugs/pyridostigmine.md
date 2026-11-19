---
layout: default
title: Pyridostigmine
parent: Solo predicción del modelo (L5)
nav_order: 673
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-05
monitor_inn: "Pyridostigmine"
predicted_indications: ["autoimmune disease of peripheral nervous system", "disease of receptor activity", "hypersplenism (disease)", "atypical hemolytic-uremic syndrome with B factor anomaly"]
description: "Pyridostigmine: nueva indicación predicha, Autoimmune disease of peripheral nervous system (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 2 (comercializadas: 1)"
---

# Pyridostigmine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Pyridostigmine: Autoimmune disease of peripheral nervous system
{: .text-alpha }

## Resumen en Una Frase

La piridostigmina es un inhibidor reversible de la acetilcolinesterasa, utilizado originalmente para el tratamiento sintomático de la miastenia gravis y de otras enfermedades de la unión neuromuscular.
El modelo TxGNN predice que podría ser efectivo para **miastenia gravis con hiperplasia tímica**, aunque se trata de un subtipo de la indicación ya conocida y no de un reposicionamiento propiamente dicho.
Actualmente no hay **ensayos clínicos** registrados y solo **3 publicaciones** relacionadas, ninguna de las cuales evalúa directamente la eficacia de la piridostigmina en esta indicación.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Autoimmune disease of peripheral nervous system |
| Puntaje de Predicción TxGNN | 0.9975 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 2; revocadas o suspendidas: 1) |
| Número de Autorizaciones | 2 (comercializadas: 1) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Pyridostigmine (traducción no oficial): «La solución oral de bromuro de piridostigmina inhibe la destrucción de la acetilcolina por la colinesterasa y, de este modo, permite una transmisión más libre de los impulsos nerviosos a través de la unión neuromuscular. La piridostigmina es un análogo de la neostigmina (Prostigmine TM ), pero difiere de ella en ciertos aspectos clínicamente significativos; por ejemplo, la piridostigmina se caracteriza por una duración de acción más prolongada y menos efectos secundarios gastrointestinales.» Texto original en inglés: "Pyridostigmine bromide oral solution inhibits the destruction of acetylcholine by cholinesterase and thereby permits freer transmission of nerve impulses across the neuromuscular junction. Pyridostigmine is an analog of neostigmine (Prostigmine TM ), but differs from it in certain clinically significant respects; for example, pyridostigmine is characterized by a longer duration of action and fewer gastrointestinal side effects." ([DailyMed: Pryidostigmine Bromide (pyridostigmine bromide) prescribing information, Rising Pharma Holdings, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=beda905e-005a-439d-ac74-92db4e269780), versión del 2022-09-07; consultado el 2026-11-19). Según la información conocida, la piridostigmina es un inhibidor reversible de la acetilcolinesterasa. Al impedir la degradación de la acetilcolina, aumenta su disponibilidad en la unión neuromuscular. Los datos farmacológicos compilados confirman como dianas la acetilcolinesterasa (ACHE) y la butirilcolinesterasa (BCHE).

La miastenia gravis con hiperplasia tímica es un subtipo de la miastenia gravis, enfermedad autoinmune en la que los anticuerpos reducen la transmisión neuromuscular. El alivio sintomático que ofrece la piridostigmina no depende de la patología del timo, por lo que la predicción es mecanísticamente coherente. Sin embargo, como se trata de un subtipo de la enfermedad ya tratada, no constituye un reposicionamiento genuino.

La literatura recuperada describe características de la enfermedad y resultados de la timectomía, pero no la eficacia de la piridostigmina en este subgrupo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34225443](https://pubmed.ncbi.nlm.nih.gov/34225443/) | 2021 | Revisión (estudio genómico/epigenético) | Molecular Medicine Reports | Aspectos genómicos, fenotípicos y epigenéticos de la miastenia gravis, su autoinmunidad y el manejo del peso |
| [25683765](https://pubmed.ncbi.nlm.nih.gov/25683765/) | 2015 | Cohorte | Journal of Neurology | Resultados a 2 años de la timectomía en 39 pacientes con miastenia gravis de inicio tardío no timomatosa |
| [18053719](https://pubmed.ncbi.nlm.nih.gov/18053719/) | 2008 | Reporte de caso | Neuromuscular Disorders | Síndrome de cabeza caída en una paciente con miastenia gravis MuSK positiva e hiperplasia tímica |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 84453 | ZEDEPTINE 12 MG/ML SOLUCIÓN ORAL EFG | Solución oral | No disponible en los datos compilados |
| 23524 | MESTINON 60 MG COMPRIMIDOS | Comprimido | No disponible en los datos compilados |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): enfermedad renal, piouréter, asma (incluidos el asma intrínseco y el alérgico) y obstrucción de las vías urinarias.
- **Interacciones farmacológicas**: la consulta se completó y devolvió 2 registros, ambos de tipo farmacológico (dianas y no interacciones con otros fármacos): acetilcolinesterasa (ACHE) y butirilcolinesterasa (BCHE). No se identificaron interacciones con otros medicamentos con nivel de gravedad asignado.

Consultar el prospecto para información completa sobre advertencias y contraindicaciones.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La piridostigmina es un tratamiento sintomático ya establecido y comercializado en España para la miastenia gravis, y el subtipo con hiperplasia tímica comparte la misma fisiopatología de la unión neuromuscular. Sin embargo, no hay ensayos clínicos específicos y la literatura recuperada no evalúa la eficacia del fármaco en este subgrupo, por lo que la evidencia se limita a L3.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones autorizadas), ya que actualmente esta información no está disponible.
- Completar los datos detallados del mecanismo de acción (MOA) desde fuentes como DrugBank.
- Buscar estudios que evalúen directamente la respuesta a la piridostigmina en miastenia gravis con hiperplasia tímica.
- Verificar las contraindicaciones señaladas por el grafo de conocimiento (enfermedad renal, asma, obstrucción urinaria) frente al prospecto oficial.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Pryidostigmine Bromide (pyridostigmine bromide) prescribing information, Rising Pharma Holdings, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=beda905e-005a-439d-ac74-92db4e269780) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

