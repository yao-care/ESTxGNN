---
layout: default
title: Vildagliptin
parent: Solo predicción del modelo (L5)
nav_order: 847
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-31
monitor_inn: "Vildagliptin"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
description: "Vildagliptin: nueva indicación predicha, Classic stiff person syndrome (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Vildagliptin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Vildagliptin: Classic stiff person syndrome
{: .text-alpha }

## Resumen en Una Frase

Vildagliptina es un inhibidor de la dipeptidil peptidasa 4 (DPP-4), utilizado originalmente para el tratamiento de la diabetes mellitus tipo 2.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de la persona rígida clásica**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Classic stiff person syndrome |
| Puntaje de Predicción TxGNN | 0.9988 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 16) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Vildagliptina inhibe la enzima DPP-4, que degrada las hormonas incretinas GLP-1 y GIP. Al elevar sus niveles, favorece la secreción de insulina dependiente de glucosa y reduce la secreción de glucagón. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción. Sí muestran que el fármaco actúa sobre DPP-4 y también sobre DPP-8, DPP-9 y TRPV4.

Con los datos disponibles **no se puede sostener un vínculo mecanístico** con el síndrome de la persona rígida. Esta enfermedad es un trastorno neurológico de origen autoinmune (con frecuencia asociado a anticuerpos anti-GAD), y la inhibición de DPP-4 no tiene un papel establecido en ella. El puntaje alto del modelo probablemente refleja la cercanía en la red de conocimiento entre diabetes y enfermedades autoinmunes, no evidencia independiente.

El cuadro es similar para el síndrome de la extremidad rígida focal, que obtiene exactamente el mismo puntaje. La similitud con la indicación original queda pendiente de evaluación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones vigentes (todas de principio activo único). Los textos de indicación aprobada no figuran en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 07414003 | Galvus 50 mg comprimidos | Comprimido | Novartis Europharm Limited |
| 08485003 | Jalra 50 mg comprimidos | Comprimido | Novartis Europharm Limited |
| 08486003 | Xiliarx 50 mg comprimidos | Comprimido | Novartis Europharm Limited |
| 86670 | Vildagliptina Vir 50 mg comprimidos EFG | Comprimido | Industria Química y Farmacéutica Vir S.A. |
| 84925 | Vildagliptina Tecnigen 50 mg cápsulas duras EFG | Cápsula dura | Tecnimede España Industria Farmacéutica S.A. |

## Consideraciones de Seguridad

- **Dianas farmacológicas identificadas:** DPP-4, DPP-8, DPP-9 y TRPV4. Son datos de farmacología, no interacciones con otros fármacos con nivel de gravedad establecido.

Consultar el prospecto para información sobre advertencias y contraindicaciones.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura, y sin un mecanismo plausible que conecte la inhibición de DPP-4 con el síndrome de la persona rígida.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA) y una hipótesis biológica que vincule DPP-4/incretinas con la fisiopatología autoinmune y neurológica de esta enfermedad
- Estudios preclínicos o series de casos que sugieran algún efecto en este síndrome
- Información de seguridad del prospecto de la AEMPS (advertencias y contraindicaciones)
- Revisar otros candidatos de la misma lista de predicciones con más respaldo. Por ejemplo, la diabetes mellitus tipo 1 (nivel L2) cuenta con ensayos de fase 2/3 y un ECA publicado de rapamicina más vildagliptina. Aun así, ese uso sigue siendo una pregunta de investigación y no una indicación establecida.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

