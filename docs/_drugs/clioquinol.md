---
layout: default
title: Clioquinol
parent: Solo predicción del modelo (L5)
nav_order: 190
evidence_level: L5
indication_count: 2
monitor_inn: "clioquinol"
predicted_indications: ["ectothrix infectious disease", "endothrix infectious disease"]
last_modified_at: 2026-10-28
description: "Clioquinol: nueva indicación predicha, Ectothrix infectious disease (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Clioquinol
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

## Clioquinol: Ectothrix infectious disease
{: .text-alpha }

## Resumen en Una Frase

Clioquinol es un fármaco de uso tópico cuyas relaciones registradas en el grafo de conocimiento incluyen la tiña del pie, la tiña corporal, la tiña en general y la dermatofitosis de la ingle y la zona perianal.
El modelo TxGNN predice que podría ser efectivo para la **enfermedad infecciosa ectotrix**, con una puntuación muy alta (0,9926), pero es solo una salida del modelo.
Actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Ectothrix infectious disease |
| Puntaje de Predicción TxGNN | 0.9926 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 3 de 3) |
| Número de Autorizaciones | 3 (vigentes: 3) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción de clioquinol. Según la información conocida, clioquinol es un antiinfeccioso tópico con relaciones registradas en el grafo de conocimiento con dermatofitosis superficiales. Su actividad antifúngica se atribuye con frecuencia a la quelación de iones metálicos (cobre, zinc, hierro), pero esto no está confirmado en los datos disponibles.

La infección ectotrix es una dermatofitosis del pelo en la que las artroconidias se sitúan en el exterior del tallo piloso. Pertenece a la misma clase de enfermedad que las tiñas registradas, por lo que el vínculo es biológicamente coherente. Es probable que la predicción refleje la proximidad en la red a esas relaciones.

Sin embargo, las infecciones del tallo piloso y del folículo suelen requerir tratamiento sistémico, porque los agentes tópicos penetran mal. Por ello, extrapolar desde la tiña de la superficie cutánea es incierto. Tampoco se aportaron estudios que respalden la predicción.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 54860 | MENADERM OTOLOGICO 0,25 mg/10 mg/ml gotas óticas en solución | Gotas óticas en solución | No consta texto de indicación |
| 52444 | MENADERM CLIO 0,25 mg/30 mg/g crema | Crema | No consta texto de indicación |
| 51784 | CUATROCREM crema | Crema | No consta texto de indicación |

## Consideraciones de Seguridad

- **Contraindicaciones registradas en el grafo de conocimiento** (no proceden del texto del prospecto): insuficiencia suprarrenal, enfermedad de Addison, atrofia cutánea, telangiectasia, enfermedad capilar, telangiectasia hemorrágica hereditaria, enfermedad vascular periférica, claudicación vascular intermitente y enfermedad arterial periférica.
- No se encontraron interacciones farmacológicas registradas.

Para el resto de la información de seguridad, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo, sin ensayos clínicos ni publicaciones sobre esta enfermedad (nivel L5). Además, la ubicación del hongo en el pelo hace dudosa la eficacia de un fármaco tópico.

**Para avanzar se necesita:**
- Obtener y analizar los prospectos de AEMPS (advertencias y contraindicaciones), ya que su ausencia impide el cribado de seguridad.
- Obtener datos del mecanismo de acción desde DrugBank.
- Realizar una búsqueda bibliográfica específica sobre clioquinol en tinea capitis (ectotrix/endotrix) y estudios de penetración en el folículo piloso.
- Estudios preclínicos o clínicos que evalúen la eficacia frente a dermatofitos del pelo y su viabilidad por vía tópica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

