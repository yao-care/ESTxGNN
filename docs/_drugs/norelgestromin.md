---
layout: default
title: Norelgestromin
parent: Solo predicción del modelo (L5)
nav_order: 572
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
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
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 9 de 13; autorizadas no comercializadas: 4) |
| Número de Autorizaciones | 13 (comercializadas: 9) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para norelgestromin and ethinyl estradiol (combinación que contiene Norelgestromin) (traducción no oficial): «El NGMN es el progestágeno activo principalmente responsable de la actividad progestacional que se produce en las mujeres tras la aplicación del sistema transdérmico de norelgestromina y etinilestradiol.» Texto original en inglés: "NGMN is the active progestin largely responsible for the progestational activity that occurs in women following application of norelgestromin and ethinyl estradiol transdermal system." ([DailyMed: norelgestromin and ethinyl estradiol prescribing information, Zydus Pharmaceuticals USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=10fa1458-c8ed-4197-922a-1ba7271d2b02), versión del 2026-04-16; consultado el 2026-11-19). Según la información conocida, norelgestromina es el metabolito progestágeno activo de norgestimato y forma parte de un parche anticonceptivo combinado con etinilestradiol. Su actividad progestágena (agonismo del receptor de progesterona, supresión de la liberación de gonadotropinas y de la ovulación, estabilización del endometrio) es biológicamente plausible para tratar algunas formas de amenorrea, por ejemplo la secundaria a un desequilibrio estroprogestágeno, en la que se usa la retirada del progestágeno para inducir sangrado.

La relación con la indicación original es hormonal: ambas situaciones dependen del eje hipotálamo-hipófiso-ovárico y del control del endometrio. Sin embargo, este vínculo se infiere por clase farmacológica y por la predicción del modelo TxGNN (aprendizaje profundo) (puntaje 0,9951), no por datos específicos del fármaco.

Conviene ser prudente: el parche anticonceptivo puede causar amenorrea o sangrado irregular como efecto adverso. Por ello la dirección del efecto no está clara, y la predicción podría reflejar esa asociación y no un beneficio terapéutico real.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 13 autorizaciones vigentes (todas del parche transdérmico EVRA, sin cancelaciones).

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 02223001 | EVRA 203 MICROGRAMOS/24 HORAS + 33,9 MICROGRAMOS/24 HORAS PARCHE TRANSDERMICO | PARCHE TRANSDÉRMICO | Gedeon Richter Plc. | Comercializada |
| 02223001IP4 | EVRA 203 MICROGRAMOS/24 HORAS + 33,9 MICROGRAMOS/24 HORAS PARCHE TRANSDERMICO | PARCHE TRANSDÉRMICO | Janssen-Cilag International N.V | Comercializada |
| 02223002IP2 | EVRA 203 MICROGRAMOS/24 HORAS + 33,9 MICROGRAMOS/24 HORAS PARCHE TRANSDERMICO | PARCHE TRANSDÉRMICO | Janssen-Cilag International N.V | Comercializada |
| 02223001IP1 | EVRA 203 MICROGRAMOS/24 hORAS + 33,9 MICROGRAMOS/24 HORAS PARCHE TRANSDERMICO | PARCHE TRANSDÉRMICO | Janssen-Cilag International N.V | Comercializada |
| 02223001IP2 | EVRA 203 MICROGRAMOS/24 HORAS + 33,9 MICROGRAMOS/24 HORAS PARCHE TRANSDERMICO | PARCHE TRANSDÉRMICO | Janssen-Cilag International N.V | Comercializada |

Se muestran 5 de 13 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

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

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: norelgestromin and ethinyl estradiol prescribing information, Zydus Pharmaceuticals USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=10fa1458-c8ed-4197-922a-1ba7271d2b02) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

