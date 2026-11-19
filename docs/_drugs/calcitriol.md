---
layout: default
title: Calcitriol
parent: Solo predicción del modelo (L5)
nav_order: 135
evidence_level: L5
indication_count: 5
monitor_inn: "CALCITRIOL"
predicted_indications: ["obsolete vitamin D deficiency", "renal tubular acidosis", "acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "hereditary hypophosphatemic rickets"]
last_modified_at: 2026-11-20
description: "Calcitriol: nueva indicación predicha, Deficiencia de vitamina D obsoleta (obsolete vitamin D deficiency) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 4 (comercializadas: 3)"
---

# Calcitriol
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

## Calcitriol: análogo activo de la vitamina D → deficiencia de vitamina D obsoleta (obsolete vitamin D deficiency)
{: .text-alpha }

## Resumen en Una Frase

Calcitriol es la forma activa de la vitamina D, utilizada en trastornos del metabolismo del calcio y del fósforo.
El modelo TxGNN predice que podría ser efectivo para **deficiencia de vitamina D obsoleta (obsolete vitamin D deficiency)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden directamente esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Deficiencia de vitamina D obsoleta (obsolete vitamin D deficiency) |
| Puntaje de Predicción TxGNN | 0,9996 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 3 de 4; revocadas o suspendidas: 1) |
| Número de Autorizaciones | 4 (comercializadas: 3) |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Calcitriol (traducción no oficial): «La síntesis endógena y el catabolismo del calcitriol, así como los mecanismos de control fisiológico que afectan a estos procesos, desempeñan un papel fundamental en la regulación de la concentración sérica de calcitriol. La producción diaria fisiológica es normalmente de 0.5 a 1.0 mcg y es algo mayor durante los períodos de aumento de la síntesis ósea (p. ej., crecimiento o embarazo).» Texto original en inglés: "Endogenous synthesis and catabolism of calcitriol, as well as physiological control mechanisms affecting these processes, play a critical role regulating the serum level of calcitriol. Physiological daily production is normally 0.5 to 1.0 mcg and is somewhat higher during periods of increased bone synthesis (eg, growth or pregnancy)." ([DailyMed: calcitriol prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=45f78bbe-4bbc-404d-a061-ead3db50908e), versión del 2026-10-15; consultado el 2026-11-19). Según la información conocida, calcitriol es el metabolito activo de la vitamina D (1,25-dihidroxivitamina D3), por lo que existe un vínculo biológico plausible con los estados de deficiencia de esta vitamina.

Sin embargo, la entrada de la enfermedad está marcada como obsoleta en la ontología, y no se recuperó ningún ensayo ni publicación. El puntaje elevado es solo una predicción del modelo y probablemente refleja cercanía entre términos, no evidencia clínica nueva. Además, en la deficiencia nutricional se usa habitualmente la vitamina D nativa (colecalciferol o ergocalciferol) y no el metabolito activo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 55973 | ROCALTROL 0,25 mcg cápsulas blandas | Cápsula blanda | No registrada en los datos locales |
| 68934 | Calcitriol Kern Pharma 1 microgramo/ml solución inyectable EFG | Solución inyectable | No registrada en los datos locales |
| 55974 | ROCALTROL 0,50 mcg cápsulas blandas | Cápsula blanda | No registrada en los datos locales |
| 64527 | SILKIS 3 microgramos/g pomada | Pomada | No registrada en los datos locales |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las principales:
  - Mayor gravedad: colecalciferol, burosumab, calcifediol.
  - Gravedad moderada: fosfenitoína, carbamazepina, barbitúricos (amobarbital, butalbital, butabarbital), diuréticos tiazídicos (hidroclorotiazida, bendroflumetiazida, clortalidona), resinas de unión a ácidos biliares (colestiramina, colesevelam, colestipol), digoxina, digitoxina, hidróxido de aluminio y calcipotriol tópico.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de ensayos clínicos y literatura, la enfermedad está marcada como obsoleta y la vitamina D nativa es la opción habitual en la deficiencia nutricional. No hay base suficiente para avanzar.

**Para avanzar se necesita:**
- Aclarar qué entidad clínica vigente corresponde a la enfermedad obsoleta
- Revisión de la literatura sobre calcitriol frente a vitamina D nativa en déficit de vitamina D
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones)
- Plan de monitorización de calcio y fósforo y de las interacciones farmacológicas de mayor gravedad

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: calcitriol prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=45f78bbe-4bbc-404d-a061-ead3db50908e) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

