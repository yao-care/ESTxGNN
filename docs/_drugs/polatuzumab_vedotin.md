---
layout: default
title: Polatuzumab Vedotin
parent: Solo predicción del modelo (L5)
nav_order: 649
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Polatuzumab Vedotin: nueva indicación predicha, Carcinoma de mama HER2 positivo (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (el texto de indicación de las…"
monitor_inn: "polatuzumab vedotin"
predicted_indications: ["HER2 positive breast carcinoma"]
---

# Polatuzumab Vedotin
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

## Polatuzumab vedotina: De Indicación Original No Especificada a Carcinoma de Mama HER2 Positivo
{: .text-alpha }

## Resumen en Una Frase

Polatuzumab vedotina es un conjugado anticuerpo-fármaco (ADC) dirigido contra CD79b que se comercializa en España como Polivy; los datos compilados para este informe no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **carcinoma de mama HER2 positivo**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata solo de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (el texto de indicación de las autorizaciones está vacío) |
| Nueva Indicación Predicha | Carcinoma de mama HER2 positivo |
| Puntaje de Predicción TxGNN | 0.9934 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 2 de 2) |
| Número de Autorizaciones | 2 (comercializadas: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Polatuzumab Vedotin (traducción no oficial): «El polatuzumab vedotina-piiq es un conjugado anticuerpo-fármaco dirigido contra CD79b con actividad contra los linfocitos B en división. La molécula pequeña, MMAE, es un agente antimitótico unido covalentemente al anticuerpo mediante un enlazador escindible. El anticuerpo monoclonal se une a CD79b, una proteína de superficie específica de los linfocitos B que es un componente del receptor de linfocitos B.» Texto original en inglés: "Polatuzumab vedotin-piiq is a CD79b-directed antibody-drug conjugate with activity against dividing B cells. The small molecule, MMAE, is an anti-mitotic agent covalently attached to the antibody via a cleavable linker. The monoclonal antibody binds to CD79b, a B-cell specific surface protein, which is a component of the B-cell receptor." ([DailyMed: Polivy (polatuzumab vedotin) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=20a16ab2-f338-4abb-9dcd-254bd949a2bc), versión del 2026-08-24; consultado el 2026-11-19). Según la información conocida, polatuzumab vedotina es un ADC que se une a CD79b, un componente del receptor de células B, y libera monometil auristatina E (MMAE), una carga útil que interrumpe los microtúbulos y provoca citotoxicidad antimitótica.

La relación con la nueva indicación es débil. CD79b no se expresa de forma conocida en las células del carcinoma de mama HER2 positivo, por lo que no existe una justificación directa basada en la diana. El único vínculo concebible es la carga útil: los ADC basados en auristatinas han sido estudiados en tumores sólidos. Sin embargo, sin expresión de CD79b en el tumor, cualquier efecto por muerte de células vecinas (efecto bystander) o captación inespecífica sería especulativo.

El puntaje alto de TxGNN (0.9934) probablemente refleja la proximidad en la red de conocimiento con otros ADC y fármacos dirigidos a HER2 (por ejemplo, ADC basados en trastuzumab con cargas útiles de la misma clase), y no biología validada. Debe interpretarse con cautela.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 1191388001 | POLIVY 140 MG POLVO PARA CONCENTRADO PARA SOLUCION PARA PERFUSION | POLVO PARA CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Roche Registration Gmbh | Comercializada |
| 1191388002 | POLIVY 30 MG POLVO PARA CONCENTRADO PARA SOLUCION PARA PERFUSION | POLVO PARA CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Roche Registration Gmbh | Comercializada |

Se muestran las 2 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

Titular: Roche Registration GmbH. Ambas autorizaciones están vigentes.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Conjugado anticuerpo-fármaco con carga útil citotóxica (MMAE, inhibidor de microtúbulos) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto (en general, hemograma y funciones hepática y renal) |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto; por su carga útil citotóxica, se recomienda seguir las normas de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registraron 131 interacciones. Entre las principales:
  - **Gravedad mayor**: claritromicina, cobicistat, deferiprona, lexidronam de samario (153Sm).
  - **Gravedad moderada** (ejemplos): aprepitant, cimetidina, naltrexona, metronidazol, miconazol, rosuvastatina, simvastatina, tinidazol, clotrimazol, cloruro de estroncio Sr-89, ticagrelor, cloroquina, disulfiram, secnidazol, hidroxicloroquina, benznidazol.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y sin una justificación mecanística directa, ya que CD79b no se asocia con el carcinoma de mama HER2 positivo. Además, faltan datos clave de la ficha técnica y del mecanismo de acción.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicación aprobada), un vacío bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Verificar la expresión de CD79b en carcinoma de mama HER2 positivo mediante estudios preclínicos.
- Buscar evidencia de ADC con MMAE en tumores sólidos y comparar con alternativas dirigidas a HER2 ya establecidas.
- Evaluar la compatibilidad de vías de administración y la similitud con la indicación original.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Polivy (polatuzumab vedotin) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=20a16ab2-f338-4abb-9dcd-254bd949a2bc) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

