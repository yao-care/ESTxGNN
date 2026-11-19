---
layout: default
title: Esketamine
parent: Solo predicción del modelo (L5)
nav_order: 307
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-05
monitor_inn: "Esketamine"
predicted_indications: ["agoraphobia", "benign paroxysmal torticollis of infancy"]
description: "Esketamine: nueva indicación predicha, Agorafobia (agoraphobia) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 1 (comercializadas: 1)"
---

# Esketamine
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

## Esketamine: Agorafobia (agoraphobia)
{: .text-alpha }

## Resumen en Una Frase

Esketamina está registrada en el grafo de conocimiento TxGNN con indicaciones originales de trastorno de ansiedad, trastorno neurótico y trastorno distímico.
El modelo TxGNN predice que podría ser efectiva para **agorafobia**, pero actualmente **no hay ensayos clínicos ni publicaciones** en los datos compilados que respalden esta dirección; se trata solo de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Agorafobia (agoraphobia) |
| Puntaje de Predicción TxGNN | 0.9957 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Esketamine (traducción no oficial): «La esketamina, el S-enantiómero de la ketamina racémica, es un antagonista no selectivo y no competitivo del receptor de N -metil- D -aspartato (NMDA), un receptor ionotrópico de glutamato. Se desconoce el mecanismo por el cual la esketamina ejerce su efecto antidepresivo.» Texto original en inglés: "Esketamine, the S-enantiomer of racemic ketamine, is a non-selective, non-competitive antagonist of the N -methyl- D -aspartate (NMDA) receptor, an ionotropic glutamate receptor. The mechanism by which esketamine exerts its antidepressant effect is unknown." ([DailyMed: Spravato (esketamine hydrochloride) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d81a6a79-a74a-44b7-822c-0dfa3036eaed), versión del 2026-09-22; consultado el 2026-11-19). Según la información conocida, esketamina es el enantiómero S de la ketamina y su farmacología general se asocia con el antagonismo del receptor NMDA y la modulación glutamatérgica. Esto es conocimiento general y no está confirmado por los datos compilados.

La agorafobia es un trastorno relacionado con la ansiedad. El puntaje proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. Hipotéticamente, la modulación glutamatérgica podría influir en los circuitos del miedo y la evitación.

Este vínculo es hipotético y no está verificado. No hay ensayos ni literatura que lo respalden, por lo que la predicción debe tratarse como una pregunta de investigación.

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
| 1191410001 | SPRAVATO 28 MG SOLUCIÓN PARA PULVERIZACIÓN NASAL (Janssen-Cilag International N.V.) | Solución para pulverización nasal | No disponible en los datos compilados |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): enfermedad vascular y malformación/hemangioma arteriovenoso.
- **Interacciones farmacológicas**: se identificaron 70 interacciones (fuente: DDInter). Entre las de nivel **Mayor** figuran dietilpropión, fentermina, fenfluramina, mazindol y cafeína. Entre las de nivel **Moderado** figuran morfina (incluida la liposomal), opio, loperamida, difenoxina, difenoxilato, dronabinol, nabilona, metoclopramida, escopolamina y corticoides/efedrina nasales (beclometasona, budesonida, triamcinolona, dexametasona, efedrina).

El prospecto de AEMPS (advertencias y contraindicaciones) no estaba disponible en los datos compilados; consultarlo para la información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el puntaje del modelo (L5), sin ensayos clínicos ni literatura. Aunque la agorafobia es plausible por su cercanía con los trastornos de ansiedad, el vínculo mecanístico no está verificado y la revisión de seguridad no puede completarse sin el prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), ya que su ausencia bloquea el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una búsqueda sistemática de ensayos y literatura sobre esketamina en agorafobia y trastornos de ansiedad.
- Evaluar el perfil de seguridad de la vía nasal y las interacciones de nivel mayor en esta población.

---

### Nota sobre la segunda predicción

La segunda predicción del modelo, **tortícolis paroxística benigna de la infancia** (puntaje 0.9949, nivel L5), no se recomienda: es un trastorno pediátrico benigno y autolimitado, sin vínculo mecanístico evidente con esketamina, y el uso de un anestésico disociativo en lactantes plantea preocupaciones de seguridad. El puntaje proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. Decisión: **Hold**.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Spravato (esketamine hydrochloride) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d81a6a79-a74a-44b7-822c-0dfa3036eaed) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

