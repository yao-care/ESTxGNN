---
layout: default
title: Aprepitant
parent: Solo predicción del modelo (L5)
nav_order: 63
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Aprepitant: nueva indicación predicha, Síndrome nefrogénico de antidiuresis inapropiada (nivel de evidencia L5). Indicación original: No disponible (los textos de indicación de las autorizaciones est…"
---

# Aprepitant
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

# Aprepitant: De Indicación Original No Disponible a Síndrome Nefrogénico de Antidiuresis Inapropiada

## Resumen en Una Frase

Aprepitant es un antagonista del receptor NK1 comercializado en España en varias presentaciones. En los datos compilados para este informe no consta el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para el **síndrome nefrogénico de antidiuresis inapropiada (NSIAD)**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Síndrome nefrogénico de antidiuresis inapropiada |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 13 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, aprepitant es un antagonista del receptor de neuroquinina 1 (NK1), que bloquea la señalización de la sustancia P. Este mecanismo se utiliza clásicamente en la prevención de náuseas y vómitos, aunque el texto de indicación no figura en los datos de las autorizaciones españolas.

La relación con el NSIAD es solo indirecta. La señalización de sustancia P/NK1 en el sistema nervioso central podría influir en el equilibrio hídrico relacionado con la vasopresina. Sin embargo, el NSIAD se debe a mutaciones activadoras del receptor V2 de vasopresina (AVPR2), una vía que el antagonismo NK1 no actúa directamente.

Por ello, el puntaje tan alto del modelo (99.97%) debe interpretarse con cautela: no hay ensayos, literatura ni relación mecanística directa que lo respalden.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

## Información de Mercado en España

Se listan 5 de las 13 autorizaciones vigentes (todas de principio activo único).

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 03262002 | EMEND 80 mg cápsulas duras | Cápsula dura | No disponible |
| 84275 | Aprepitant Accord 125 mg cápsulas duras EFG | Cápsula dura | No disponible |
| 84706 | Atanto 125 mg cápsulas duras EFG | Cápsula dura | No disponible |
| 85689 | Aprepitant Qilu 80 mg cápsulas duras EFG | Cápsula dura | No disponible |
| 103262011 | EMEND 125 mg polvo para suspensión oral | Polvo para suspensión oral | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones (grafo de conocimiento, no texto del prospecto)**: el grafo de conocimiento asocia aprepitant con insuficiencia hepática (*liver failure*) como contraindicación.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; las primeras 20 revisadas incluyen:
  - **Mayores**: fentanilo, alfentanilo, acalabrutinib.
  - **Moderadas**: paclitaxel, abemaciclib, lidocaína, dihidrocodeína, rabeprazol, nifedipino, ibuprofeno, levonorgestrel, hidrocortisona, albendazol, fluvoxamina, fosamprenavir, fosfenitoína, fostamatinib, gefitinib y abametapir (tópico).
  - **Menores**: dolutegravir.
- Aprepitant presenta numerosas interacciones mediadas por CYP3A4, lo que debe considerarse con inductores o inhibidores potentes.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo computacional (nivel L5), sin ensayos clínicos, sin literatura relevante y sin vínculo mecanístico directo entre el antagonismo NK1 y la vía AVPR2 del NSIAD.

**Para avanzar se necesita:**
- Obtener el prospecto de AEMPS para confirmar indicaciones, advertencias y contraindicaciones (brecha bloqueante para el cribado de seguridad).
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar estudios preclínicos o de mecanismo que justifiquen un vínculo entre NK1/sustancia P y la regulación de la vasopresina o la función del receptor V2.
- Revisar otras predicciones de la lista (p. ej., hipertensión pulmonar y hemorragia subaracnoidea), que tienen un racional biológico débil pero, al igual que esta, carecen de evidencia clínica.
- Evaluar el riesgo de interacciones CYP3A4 y la contraindicación por insuficiencia hepática antes de cualquier uso en una nueva población.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

