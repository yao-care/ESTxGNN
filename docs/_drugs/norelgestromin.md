---
layout: default
title: Norelgestromin
parent: Solo predicción del modelo (L5)
nav_order: 572
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Norelgestromin: nueva indicación predicha, Amenorrea (nivel de evidencia L5). Indicación original: No disponible en los datos de la autorización (el parche se comercial…"
monitor_inn: "norelgestromin"
predicted_indications: ["amenorrhea (disease)"]
---

# Norelgestromin
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

## Norelgestromina: De Anticoncepción Transdérmica a Amenorrea
{: .text-alpha }

## Resumen en Una Frase

Norelgestromina es el metabolito progestágeno activo de la norgestimato y se administra en un parche transdérmico anticonceptivo junto con etinilestradiol.
El modelo TxGNN predice que podría ser efectiva para **amenorrea**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de la autorización (el parche se comercializa como anticonceptivo transdérmico) |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 0,9951 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 10 de 13) |
| Número de Autorizaciones | 13 (vigentes: 10) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, norelgestromina es el metabolito progestágeno activo de norgestimato y forma parte de un parche anticonceptivo combinado con etinilestradiol. Su actividad progestágena (agonismo del receptor de progesterona, supresión de la liberación de gonadotropinas y de la ovulación, estabilización del endometrio) es biológicamente plausible para tratar algunas formas de amenorrea, por ejemplo la secundaria a un desequilibrio estroprogestágeno, en la que se usa la retirada del progestágeno para inducir sangrado.

La relación con la indicación original es hormonal: ambas situaciones dependen del eje hipotálamo-hipófiso-ovárico y del control del endometrio. Sin embargo, este vínculo se infiere por clase farmacológica y por la predicción del modelo TxGNN (aprendizaje profundo) (puntaje 0,9951), no por datos específicos del fármaco.

Conviene ser prudente: el parche anticonceptivo puede causar amenorrea o sangrado irregular como efecto adverso. Por ello la dirección del efecto no está clara, y la predicción podría reflejar esa asociación y no un beneficio terapéutico real.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 13 autorizaciones vigentes (todas del parche transdérmico EVRA, sin cancelaciones).

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 02223001 | EVRA 203 microgramos/24 horas + 33,9 microgramos/24 horas parche transdérmico | Parche transdérmico | No disponible en los datos compilados |
| 02223001IP | EVRA 203 microgramos/24 horas + 33,9 microgramos/24 horas parche transdérmico | Parche transdérmico | No disponible en los datos compilados |
| 02223002 | EVRA 203 microgramos/24 horas + 33,9 microgramos/24 horas parche transdérmico | Parche transdérmico | No disponible en los datos compilados |
| 02223003 | EVRA 203 microgramos/24 horas + 33,9 microgramos/24 horas parche transdérmico | Parche transdérmico | No disponible en los datos compilados |
| 02223002IP | EVRA 203 microgramos/24 horas + 33,9 microgramos/24 horas parche transdérmico | Parche transdérmico | No disponible en los datos compilados |

Titulares: Gedeon Richter Plc. y Janssen-Cilag International N.V.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad del grafo, no texto del prospecto): hipertensión, epilepsia, trastornos de ansiedad y neuróticos, distimia, porfirias, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, hiperglucemia, diabetes mellitus y cetoacidosis diabética, lupus eritematoso sistémico, asma, hipertrigliceridemia, hiperlipidemia (incluida la familiar), carcinoma de mama femenino, tromboflebitis, migraña, enfermedad coronaria, piouréter y pérdida visual funcional.
- **Interacciones farmacológicas**: 1 interacción de nivel **Mayor** registrada, con **sugammadex**.

Para el resto de advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se sustenta únicamente en el modelo (nivel L5), sin ensayos ni literatura. Además, el parche puede provocar amenorrea como efecto adverso, por lo que la dirección del efecto es incierta, y el perfil de contraindicaciones es amplio.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicación aprobada), un vacío bloqueante para el cribado de seguridad.
- Datos del mecanismo de acción desde DrugBank.
- Revisión de literatura y de registros de ensayos sobre progestágenos en amenorrea, aclarando si el efecto es terapéutico o adverso.
- Evaluar la compatibilidad de la vía transdérmica con la indicación propuesta y su similitud con la indicación original.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

