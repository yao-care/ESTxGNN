---
layout: default
title: Polatuzumab Vedotin
parent: Solo predicción del modelo (L5)
nav_order: 649
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Polatuzumab Vedotin: nueva indicación predicha, Carcinoma de mama HER2 positivo (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (el texto de indicación de las…"
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

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Polatuzumab vedotina: De Indicación Original No Especificada a Carcinoma de Mama HER2 Positivo

## Resumen en Una Frase

Polatuzumab vedotina es un conjugado anticuerpo-fármaco (ADC) dirigido contra CD79b que se comercializa en España como Polivy; los datos compilados para este informe no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **carcinoma de mama HER2 positivo**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata solo de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (el texto de indicación de las autorizaciones está vacío) |
| Nueva Indicación Predicha | Carcinoma de mama HER2 positivo |
| Puntaje de Predicción TxGNN | 99.34% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, polatuzumab vedotina es un ADC que se une a CD79b, un componente del receptor de células B, y libera monometil auristatina E (MMAE), una carga útil que interrumpe los microtúbulos y provoca citotoxicidad antimitótica.

La relación con la nueva indicación es débil. CD79b no se expresa de forma conocida en las células del carcinoma de mama HER2 positivo, por lo que no existe una justificación directa basada en la diana. El único vínculo concebible es la carga útil: los ADC basados en auristatinas han sido estudiados en tumores sólidos. Sin embargo, sin expresión de CD79b en el tumor, cualquier efecto por muerte de células vecinas (efecto bystander) o captación inespecífica sería especulativo.

El puntaje alto de TxGNN (0.993) probablemente refleja la proximidad en la red de conocimiento con otros ADC y fármacos dirigidos a HER2 (por ejemplo, ADC basados en trastuzumab con cargas útiles de la misma clase), y no biología validada. Debe interpretarse con cautela.

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
| 1191388001 | POLIVY 140 MG polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión | No disponible |
| 1191388002 | POLIVY 30 MG polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión | No disponible |

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
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

