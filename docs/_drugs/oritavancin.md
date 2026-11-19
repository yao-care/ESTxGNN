---
layout: default
title: Oritavancin
parent: Solo predicción del modelo (L5)
nav_order: 591
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-05
monitor_inn: "oritavancin"
predicted_indications: ["Bacteroidaceae infectious disease", "ophthalmic herpes zoster", "Mycoplasma pneumoniae pneumonia"]
description: "Oritavancin: nueva indicación predicha, Enfermedad infecciosa por Bacteroidaceae (Bacteroidaceae infectious disease) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 2 (comercializadas: 2)"
---

# Oritavancin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Oritavancin: Enfermedad infecciosa por Bacteroidaceae (Bacteroidaceae infectious disease)
{: .text-alpha }

## Resumen en Una Frase

Oritavancina es un lipoglucopéptido antibacteriano, originalmente utilizado para el tratamiento de infecciones de la piel de origen bacteriano.
El modelo TxGNN predice que podría ser efectivo para **enfermedad infecciosa por Bacteroidaceae**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Enfermedad infecciosa por Bacteroidaceae (Bacteroidaceae infectious disease) |
| Puntaje de Predicción TxGNN | 0.9948 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 2 de 2) |
| Número de Autorizaciones | 2 (comercializadas: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Oritavancina es un lipoglucopéptido que inhibe la síntesis de la pared celular bacteriana (transglicosilación y transpeptidación) y altera la integridad de la membrana. Su espectro comercializado es el de bacterias Gram-positivas, lo que explica su uso en infecciones cutáneas bacterianas.

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Oritavancin (traducción no oficial): «La oritavancina es un fármaco antibacteriano. […] La oritavancina tiene tres mecanismos de acción: (i) inhibición de la etapa de transglucosilación (polimerización) de la biosíntesis de la pared celular mediante la unión al péptido troncal de los precursores del peptidoglucano; (ii) inhibición de la etapa de transpeptidación (entrecruzamiento) de la biosíntesis de la pared celular mediante la unión a los segmentos peptídicos de enlace de la pared celular; y (iii) alteración de la integridad de la membrana bacteriana, lo que provoca despolarización, permeabilización y muerte celular. Estos múltiples mecanismos contribuyen a la actividad bactericida dependiente de la concentración de la oritavancina.» Texto original en inglés: "Oritavancin is an antibacterial drug. […] Oritavancin has three mechanisms of action: (i) inhibition of the transglycosylation (polymerization) step of cell wall biosynthesis by binding to the stem peptide of peptidoglycan precursors; (ii) inhibition of the transpeptidation (crosslinking) step of cell wall biosynthesis by binding to the peptide bridging segments of the cell wall; and (iii) disruption of bacterial membrane integrity, leading to depolarization, permeabilization, and cell death. These multiple mechanisms contribute to the concentration-dependent bactericidal activity of oritavancin." ([DailyMed: Orbactiv (oritavancin) prescribing information, Melinta Therapeutics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ff09a726-9f9b-4e30-b509-396781293220), versión del 2026-09-15; consultado el 2026-11-19). Con la información conocida, la relación entre la indicación original y la nueva es **débil**: Bacteroidaceae son anaerobios Gram-negativos con una membrana externa que los glucopéptidos, en general, no logran atravesar.

Por tanto, el puntaje alto de TxGNN (0,9948) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni una justificación farmacológica sólida. Sin ensayos ni literatura, esta predicción requiere mucha cautela.

**Otras predicciones del modelo (todas con nivel L5 y decisión Hold):**

| Indicación predicha | Puntaje TxGNN | Comentario |
|------|------|------|
| Herpes zóster oftálmico | 0,9903 | Oritavancina es antibacteriana, sin actividad antiviral conocida; el tratamiento antiviral estándar sigue siendo el adecuado. |
| Neumonía por *Mycoplasma pneumoniae* | 0,9901 | *Mycoplasma* carece de pared celular, por lo que no se espera actividad de un inhibidor de la síntesis de peptidoglucano. |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 115989001 | TENKASI 400 MG polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión | No disponible en los datos compilados |
| 115989002 | TENKASI 1200 MG polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión | No disponible en los datos compilados |

Titular de ambas autorizaciones: Menarini International Operations Luxembourg S.A. (vigentes, de tipo monofármaco).

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 38 interacciones en total; a continuación se resumen las principales de las 20 detalladas en los datos compilados:
  - **Mayor**: heparina.
  - **Moderada**: warfarina, ticagrelor, cobicistat, fostamatinib, hidrocodona, praziquantel, etinilestradiol, nitisinona, picosulfato, macimorelina, elagolix, osilodrostat, abemaciclib, acalabrutinib, alpelisib, brigatinib, cabozantinib, crizotinib.
  - **Menor**: bortezomib.

Para advertencias y contraindicaciones, consultar el prospecto; los datos de la ficha técnica de la AEMPS no estaban disponibles para este informe.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y el mecanismo de oritavancina (espectro Gram-positivo) no encaja bien con bacterias Gram-negativas anaerobias como Bacteroidaceae. Las otras dos predicciones tampoco tienen respaldo mecanístico.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto/ficha técnica de la AEMPS (advertencias, contraindicaciones e indicaciones autorizadas), lo cual es un requisito bloqueante para cualquier evaluación de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Estudios in vitro de sensibilidad (CMI) frente a especies de Bacteroidaceae que confirmen o descarten actividad.
- Revisión sistemática de la literatura sobre glucopéptidos y lipoglucopéptidos frente a anaerobios Gram-negativos.
- Valorar la compatibilidad de la vía de administración (solo disponible en perfusión intravenosa) con la nueva indicación.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Orbactiv (oritavancin) prescribing information, Melinta Therapeutics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ff09a726-9f9b-4e30-b509-396781293220) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

