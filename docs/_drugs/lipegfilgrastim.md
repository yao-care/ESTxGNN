---
layout: default
title: Lipegfilgrastim
parent: Solo predicción del modelo (L5)
nav_order: 474
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Lipegfilgrastim: nueva indicación predicha, Trastorno primario de liberación plaquetaria (primary release disorde… (nivel de evidencia L5). Indicación original: No disponible en los datos compilados …"
monitor_inn: "LIPEGFILGRASTIM"
predicted_indications: ["primary release disorder of platelets", "severe nonproliferative diabetic retinopathy", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "diabetic retinopathy"]
---

# Lipegfilgrastim
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

# Lipegfilgrastim: De Indicación Original No Especificada a Trastorno Primario de Liberación Plaquetaria

## Resumen en Una Frase

Lipegfilgrastim es un análogo pegilado del factor estimulante de colonias de granulocitos (G-CSF), comercializado en España con el nombre Lonquex. En los datos compilados para este informe no consta el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para el **trastorno primario de liberación plaquetaria**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (el texto de indicación de las autorizaciones está vacío) |
| Nueva Indicación Predicha | Trastorno primario de liberación plaquetaria (primary release disorder of platelets) |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, lipegfilgrastim es un análogo pegilado de G-CSF que estimula la proliferación y diferenciación del linaje neutrofílico mediante el receptor de G-CSF.

No se identifica un efecto directo establecido sobre la liberación de gránulos plaquetarios ni sobre la función plaquetaria. El puntaje elevado (0.999) probablemente es un artefacto del grafo de conocimiento, derivado de vecinos compartidos en la red hematológica, y no un mecanismo validado. La relación con la indicación original (similitud) está pendiente de evaluar.

En consecuencia, la plausibilidad biológica de esta predicción es baja y requiere validación antes de cualquier consideración de reposicionamiento.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 113856001 | Lonquex 6 mg solución inyectable | Solución inyectable | No disponible |
| 1130856004 | LONQUEX 6 MG/0,6 ML solución inyectable | Solución inyectable | No disponible |

Ambas autorizaciones corresponden al titular Teva B.V. y están vigentes (monofármaco).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Otras Predicciones Evaluadas

Se evaluaron además otras cuatro indicaciones predichas, todas con nivel de evidencia L5, sin ensayos ni literatura y con recomendación Hold:

| Rango | Indicación Predicha | Puntaje TxGNN | Valoración Mecanística |
|------|------|------|------|
| 2 | Retinopatía diabética no proliferativa grave | 99.91% | Sin mecanismo directo plausible; la movilización de progenitores por G-CSF es especulativa y podría favorecer la neovascularización patológica |
| 3 | Pseudo-enfermedad de von Willebrand | 99.91% | Causada por variantes de ganancia de función de GPIbα; lipegfilgrastim no interactúa con el eje GPIb-VWF |
| 4 | Trombastenia de Glanzmann | 99.91% | Defecto de la integrina αIIbβ3; el agonismo del receptor de G-CSF no lo corrige |
| 5 | Retinopatía diabética | 99.75% | Vínculo especulativo; dirección del efecto incierta (podría empeorar la neovascularización) |

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo, sin ensayos clínicos ni literatura, y el mecanismo conocido de lipegfilgrastim (estimulación del linaje neutrofílico) no se relaciona con la función plaquetaria. El alto puntaje parece reflejar proximidad en la red del grafo y no una base biológica.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), una brecha de datos bloqueante para el cribado de seguridad
- Confirmar la indicación aprobada y el mecanismo de acción detallado del fármaco
- Realizar una revisión sistemática de literatura y de registros de ensayos que busque cualquier señal real en trastornos plaquetarios
- Establecer un vínculo mecanístico plausible, con estudios preclínicos, antes de reconsiderar la decisión
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

