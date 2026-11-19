---
layout: default
title: Empagliflozin
parent: Solo predicción del modelo (L5)
nav_order: 287
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-20
monitor_inn: "Empagliflozin"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia"]
description: "Empagliflozin: nueva indicación predicha, Focal stiff limb syndrome (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 8 (comercializadas: 2; autorizadas no comercializadas: 6)"
---

# Empagliflozin
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

## Empagliflozin: Focal stiff limb syndrome
{: .text-alpha }

## Resumen en Una Frase

Empagliflozina es un inhibidor del cotransportador sodio-glucosa tipo 2 (SGLT2), utilizado originalmente para el tratamiento de la diabetes mellitus tipo 2.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de rigidez focal de extremidad**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Focal stiff limb syndrome |
| Puntaje de Predicción TxGNN | 0.9906 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 2 de 8; autorizadas no comercializadas: 6) |
| Número de Autorizaciones | 8 (comercializadas: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Empagliflozin (traducción no oficial): «La empagliflozina es un inhibidor del SGLT2, el transportador predominante responsable de la reabsorción de la glucosa desde el filtrado glomerular de vuelta a la circulación. Al inhibir el SGLT2, la empagliflozina reduce la reabsorción renal de la glucosa filtrada y disminuye el umbral renal de glucosa, con lo que aumenta la excreción urinaria de glucosa.» Texto original en inglés: "Empagliflozin is an inhibitor of SGLT2, the predominant transporter responsible for reabsorption of glucose from the glomerular filtrate back into the circulation. By inhibiting SGLT2, empagliflozin reduces renal reabsorption of filtered glucose and lowers the renal threshold for glucose, and thereby increases urinary glucose excretion." ([DailyMed: Jardiance (empagliflozin) prescribing information, Boehringer Ingelheim Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=faf3dd6a-9cd0-39c2-0d2e-232cb3f67565), versión del 2026-11-10; consultado el 2026-11-19). Según la información conocida, empagliflozina inhibe el cotransportador SGLT2 renal (y, con menor afinidad, SGLT1), lo que favorece la excreción urinaria de glucosa y reduce la glucemia. Su eficacia en la diabetes mellitus tipo 2 está comprobada.

Hay que ser claros: **no existe un vínculo mecanístico establecido** con la nueva indicación. El síndrome de rigidez focal de extremidad es un trastorno neurológico raro, probablemente autoinmune, dentro del espectro de la persona rígida, asociado a una menor inhibición GABAérgica (por ejemplo, anticuerpos anti-GAD65 o anti-anfifisina). La inhibición de SGLT2 no tiene un efecto conocido sobre esta vía.

La puntuación elevada de TxGNN (0.9903) probablemente refleja la proximidad en la red del conocimiento con la diabetes y la autoinmunidad (los anti-GAD65 se asocian tanto a la diabetes tipo 1 como al síndrome de la persona rígida). Esto es una asociación indirecta y no una justificación de eficacia.

Otras predicciones del modelo con puntuaciones similares (síndrome clásico de la persona rígida, 0.9906, y opsismodisplasia, 0.9903) tampoco cuentan con vínculo mecanístico ni evidencia clínica en los datos compilados.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 114930014 | JARDIANCE 10 MG comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |
| 114930005 | JARDIANCE 25 MG comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |
| 89672 | GLUSOD 10 MG comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos compilados |
| 89671 | GLUSOD 25 MG comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos compilados |
| 91044 | EMPAGLIFLOZINA KERN PHARMA 10 MG comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos compilados |

Hay 8 autorizaciones vigentes en total, todas de monofármaco; aquí se muestran 5.

## Consideraciones de Seguridad

- **Interacciones farmacológicas / farmacología de dianas**: la consulta se completó con 2 resultados, ambos de tipo farmacológico (sin nivel de gravedad asignado): interacción con los cotransportadores sodio-glucosa tipo 1 (SGLT1, gen SLC5A1) y tipo 2 (SGLT2, gen SLC5A2). Son las dianas farmacológicas de empagliflozina y no interacciones con otros fármacos.

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no hay vínculo mecanístico plausible entre la inhibición de SGLT2 y la fisiopatología GABAérgica/autoinmune del síndrome de rigidez focal. La puntuación alta no basta para avanzar.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y un análisis mecanístico que justifique la relación con la vía GABAérgica o autoinmune
- Estudios preclínicos o series de casos que sugieran algún beneficio en síndromes de la persona rígida
- Revisión de las advertencias y contraindicaciones del prospecto de la AEMPS, aún no incorporadas
- Textos de indicación aprobada de las autorizaciones españolas
- Evaluación de la compatibilidad de vía de administración y de la similitud con la indicación original (pendientes)
- Evaluación de seguridad específica en la población objetivo

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Jardiance (empagliflozin) prescribing information, Boehringer Ingelheim Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=faf3dd6a-9cd0-39c2-0d2e-232cb3f67565) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

