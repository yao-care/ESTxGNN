---
layout: default
title: Durvalumab
parent: Solo predicción del modelo (L5)
nav_order: 272
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Durvalumab: nueva indicación predicha, Carcinoma urotelial de la uretra prostática (nivel de evidencia L5). Indicación original: Carcinoma de células transicionales (carcinoma urotelial)"
monitor_inn: "DURVALUMAB"
predicted_indications: ["prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma", "infiltrating bladder urothelial carcinoma sarcomatoid variant", "renal pelvis papillary urothelial carcinoma", "uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
---

# Durvalumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Durvalumab: De Carcinoma de Células Transicionales a Carcinoma Urotelial de la Uretra Prostática

## Resumen en Una Frase

Durvalumab es un anticuerpo monoclonal dirigido contra PD-L1, originalmente utilizado para el tratamiento del carcinoma de células transicionales (carcinoma urotelial).
El modelo TxGNN predice que podría ser efectivo para el **carcinoma urotelial de la uretra prostática**, pero para esta indicación concreta **no hay ensayos clínicos ni publicaciones** que la respalden; es una predicción basada únicamente en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Carcinoma de células transicionales (carcinoma urotelial) |
| Nueva Indicación Predicha | Carcinoma urotelial de la uretra prostática |
| Puntaje de Predicción TxGNN | 99,98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

> Nota: los textos de indicación aprobada en las autorizaciones españolas no están disponibles en los datos compilados; la indicación original procede de las relaciones de indicación del grafo de conocimiento de TxGNN.

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, durvalumab es un inhibidor del punto de control inmunitario que bloquea PD-L1, su eficacia en el carcinoma urotelial ha sido establecida, y mecanísticamente podría ser aplicable a otros tumores uroteliales.

El carcinoma urotelial de la uretra prostática pertenece a la misma familia histológica que la indicación original (carcinoma de células transicionales). Por ello, el bloqueo de PD-L1 es biológicamente plausible por analogía.

No obstante, no se aportaron ensayos ni literatura para esta localización concreta, por lo que la predicción sigue siendo una hipótesis sin respaldo clínico directo.

### Otras predicciones del modelo (para contexto)

Los datos compilados incluyen otras indicaciones predichas con algo más de evidencia que la seleccionada como principal:

| Indicación predicha | Puntaje TxGNN | Nivel | Ensayos | Publicaciones |
|------|------|------|------|------|
| Carcinoma urotelial sarcomatoide de la variante infiltrante de vejiga | 99,98% | L2 | 2 | 0 |
| Carcinoma sarcomatoide de células transicionales de la pelvis renal | 99,98% | L3 | 1 | 0 |
| Carcinoma endocervical | 99,91% | L3 | 1 | 2 |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para el carcinoma urotelial de la uretra prostática.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1181322002IP | IMFINZI 50 mg/ml concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos |
| 1181322001IP | IMFINZI 50 mg/ml concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos |
| 1181322001 | IMFINZI 50 mg/ml concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos |
| 1181322002 | IMFINZI 50 mg/ml concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos |

Titular: AstraZeneca AB. Las cuatro autorizaciones están vigentes y corresponden a monofármaco.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (inhibidor de punto de control inmunitario anti-PD-L1) |
| Riesgo de Mielosupresión | Bajo en comparación con la quimioterapia citotóxica; consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Baja |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto (en general: función hepática, renal, tiroidea y hemograma) |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 81 interacciones en total. Entre las principales:
  - **Mayor**: adalimumab.
  - **Moderadas**: corticoides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida, prednisolona, prednisona, metilprednisolona, deflazacort), roflumilast, alefacept, alemtuzumab, anakinra, vacuna antitetánica (toxoide inactivado) y vacuna contra el ántrax.
  - **Menores**: sales de zinc (acetato, gluconato, sulfato, cloruro).

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación seleccionada solo cuenta con la predicción del modelo (L5), sin ensayos ni literatura específicos. Aunque la plausibilidad biológica es alta por pertenecer a la misma familia urotelial, no es suficiente para avanzar.

**Para avanzar se necesita:**
- Datos de mecanismo de acción (MOA) y del prospecto de la AEMPS (advertencias y contraindicaciones), actualmente ausentes.
- Revisión sistemática de literatura y de registros de ensayos específica para el carcinoma urotelial de la uretra prostática.
- Valorar priorizar la variante sarcomatoide infiltrante de vejiga (L2, aunque con un ensayo de fase 2 terminado con solo 7 pacientes) y los tumores uroteliales del tracto superior, donde existe al menos un ensayo piloto de durvalumab más tremelimumab.
- Evaluar el uso en combinación (con tremelimumab o quimioterapia), dado que los ensayos disponibles no son de monoterapia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

