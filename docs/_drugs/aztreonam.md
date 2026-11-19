---
layout: default
title: Aztreonam
parent: Solo predicción del modelo (L5)
nav_order: 85
evidence_level: L5
indication_count: 10
monitor_inn: "AZTREONAM"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "gonococcal urethritis", "Ureaplasma urethritis", "blood group incompatibility", "premalignant hematological system disease", "epiglottitis", "monoclonal gammopathy", "xanthogranulomatous pyelonephritis"]
last_modified_at: 2026-11-20
description: "Aztreonam: nueva indicación predicha, hiperamilasemia (hyperamylasemia) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 2 (comercializadas: 2)"
---

# Aztreonam
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Aztreonam: monobactámico antibacteriano (inhibidor de la síntesis de pared celular) → hiperamilasemia (hyperamylasemia)
{: .text-alpha }

## Resumen en Una Frase

Aztreonam es un antibiótico monobactámico activo frente a bacterias gramnegativas, comercializado en España en formas inyectable e inhalada.
El modelo TxGNN predice que podría ser efectivo para **hiperamilasemia (hyperamylasemia)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | hiperamilasemia (hyperamylasemia) |
| Puntaje de Predicción TxGNN | 0,9973 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 2 de 2) |
| Número de Autorizaciones | 2 (comercializadas: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Aztreonam (traducción no oficial): «Aztreonam es un agente bactericida que actúa mediante la inhibición de la síntesis de la pared celular bacteriana. Aztreonam tiene actividad en presencia de algunas betalactamasas, tanto penicilinasas como cefalosporinasas, de bacterias gramnegativas y grampositivas.» Texto original en inglés: "Aztreonam is a bactericidal agent that acts by inhibition of bacterial cell wall synthesis. Aztreonam has activity in the presence of some beta-lactamases, both penicillinases and cephalosporinases, of Gram-negative and Gram-positive bacteria." ([DailyMed: aztreonam prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d4500795-3b07-4a7d-b432-73cafbb3dbc6), versión del 2024-06-03; consultado el 2026-11-19). Según la información conocida, aztreonam es un monobactámico que inhibe la síntesis de la pared celular bacteriana al unirse a la proteína fijadora de penicilina 3 (PBP3) en bacterias gramnegativas.

La hiperamilasemia es un hallazgo de laboratorio (elevación de amilasa en sangre) que suele tener causas no infecciosas, pancreáticas o salivales. No se identifica un vínculo mecanístico plausible entre la acción antibacteriana de aztreonam y esta condición.

Por tanto, el puntaje elevado (0,9973) refleja una predicción basada en el modelo, sin datos clínicos que la sustenten. Debe interpretarse con mucha cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 09543002 | CAYSTON 75 mg polvo y disolvente para solución para inhalación por nebulizador | Polvo para solución para inhalación por nebulizador | No registrada en los datos locales |
| 57781 | AZACTAM 1 g polvo para solución inyectable | Polvo para solución inyectable | No registrada en los datos locales |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se han identificado 27 interacciones en total. Las de nivel moderado incluyen ácido picosulfúrico, dicumarol y warfarina (posible efecto sobre la anticoagulación; se recomienda vigilancia). Otras interacciones registradas, sin nivel de gravedad clasificado, incluyen vancomicina, amikacina, anfotericina B, tacrolimus, heparina, metronidazol y fluconazol, entre otros.

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de ensayos clínicos, literatura y vínculo mecanístico plausible; el puntaje alto del modelo no es suficiente por sí solo para avanzar.

**Para avanzar se necesita:**
- Una hipótesis biológica que explique cómo un antibacteriano podría influir en la hiperamilasemia
- Datos de mecanismo de acción detallados
- Revisión del prospecto (advertencias y contraindicaciones) de las autorizaciones españolas
- Estudios preclínicos o clínicos que evalúen directamente esta indicación antes de cualquier consideración de desarrollo

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: aztreonam prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d4500795-3b07-4a7d-b432-73cafbb3dbc6) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

