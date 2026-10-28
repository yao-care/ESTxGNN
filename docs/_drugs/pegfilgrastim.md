---
layout: default
title: Pegfilgrastim
parent: Solo predicción del modelo (L5)
nav_order: 616
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Pegfilgrastim: nueva indicación predicha, Retinopatía diabética no proliferativa grave (nivel de evidencia L5). Indicación original: No disponible en los datos de las autorizaciones de AEMPS"
monitor_inn: "PEGFILGRASTIM"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy"]
---

# Pegfilgrastim
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

## Pegfilgrastim: De Neutropenia (indicación no registrada en los datos) a Retinopatía Diabética No Proliferativa Grave
{: .text-alpha }

## Resumen en Una Frase

Pegfilgrastim es un análogo pegilado del factor estimulante de colonias de granulocitos (G-CSF) que se comercializa en España para estimular la producción de neutrófilos; los datos compilados para este informe no incluyen el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **retinopatía diabética no proliferativa grave**, con una puntuación muy alta (0,9989).
Actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, por lo que se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de las autorizaciones de AEMPS |
| Nueva Indicación Predicha | Retinopatía diabética no proliferativa grave |
| Puntaje de Predicción TxGNN | 0,9989 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 6 de 10) |
| Número de Autorizaciones | 10 (vigentes: 6) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, pegfilgrastim es una forma pegilada de G-CSF que estimula la producción y la liberación de neutrófilos desde la médula ósea, y su uso establecido está relacionado con la reducción de la neutropenia.

Mecanísticamente, podría plantearse una relación con la retinopatía diabética a través de los efectos del G-CSF sobre las células progenitoras derivadas de la médula ósea, la reparación vascular o las vías inflamatorias de la microvasculatura retiniana. Sin embargo, esta es solo una hipótesis sin respaldo en los datos disponibles.

Además, la dirección del efecto es incierta: la movilización de neutrófilos también podría empeorar la inflamación y el daño vascular de la retina. La predicción de la retinopatía diabética (puntuación 0,9973) es una indicación más amplia que se solapa con la forma grave, por lo que ambas predicciones no constituyen evidencia independiente.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1181329002 | FULPHILA 6 mg solución inyectable en jeringa precargada | Solución inyectable | No disponible |
| 02227004 | NEULASTA 6 mg solución inyectable | Solución inyectable en jeringa precargada | No disponible |
| 1181327001 | ZIEXTENZO 6 mg solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada | No disponible |
| 02227003 | NEULASTA 6 mg solución inyectable en pluma precargada | Solución inyectable en pluma precargada | No disponible |
| 1181313001 | PELGRAZ 6 mg solución inyectable en jeringa precargada | Solución inyectable | No disponible |

Se muestran 5 de las 10 autorizaciones vigentes (todas de principio activo único). Otros productos autorizados: Neulasta (jeringa), Pelmeg, Pelgraz (inyector precargado), Stimufend y Nyvepria.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; las principales mostradas son de nivel moderado, entre ellas:
  - Paclitaxel
  - Mercaptopurina
  - Abemaciclib
  - Acalabrutinib
  - Aldesleukina
  - Alemtuzumab
  - Azacitidina
  - Trióxido de arsénico
  - Ibritumomab tiuxetán
  - Levamisol

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única base de esta predicción es la puntuación del modelo TxGNN (nivel de evidencia L5), sin ensayos clínicos ni literatura, y con una dirección de efecto incierta (posible beneficio o daño). Además, faltan datos clave de seguridad y de mecanismo de acción.

**Para avanzar se necesita:**
- Obtener el prospecto de AEMPS (advertencias, contraindicaciones e indicación aprobada), ya que su ausencia bloquea el cribado de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Revisión sistemática de la literatura preclínica sobre G-CSF y retinopatía diabética para establecer la dirección del efecto
- Evaluar la seguridad en pacientes diabéticos con enfermedad retiniana
- Analizar la compatibilidad de la vía de administración (inyectable) con la indicación propuesta
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

