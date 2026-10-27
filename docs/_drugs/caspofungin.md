---
layout: default
title: Caspofungin
parent: Solo predicción del modelo (L5)
nav_order: 151
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Caspofungin: nueva indicación predicha, Anomalía de la secreción de gastrina (nivel de evidencia L5). Indicación original: Candidiasis esofágica y candidemia (según las relaciones de indicació…"
monitor_inn: "caspofungin"
predicted_indications: ["gastrin secretion abnormality"]
---

# Caspofungin
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

## Caspofungina: De Candidiasis Esofágica y Candidemia a Anomalía de la Secreción de Gastrina
{: .text-alpha }

## Resumen en Una Frase

Caspofungina es un antifúngico de la clase de las equinocandinas, utilizado originalmente para el tratamiento de la candidiasis esofágica y la candidemia.
El modelo TxGNN predice que podría ser efectivo para la **anomalía de la secreción de gastrina**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Candidiasis esofágica y candidemia (según las relaciones de indicación del grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Anomalía de la secreción de gastrina |
| Puntaje de Predicción TxGNN | 99,44% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la farmacología conocida de la clase, caspofungina es una equinocandina que inhibe la beta-(1,3)-D-glucano sintasa de la pared celular de los hongos. Su eficacia en la candidiasis esofágica y la candidemia es la base de su uso clínico.

Sin embargo, **no se identifica un vínculo mecanístico** con la nueva indicación. Las células de mamífero carecen de la diana de las equinocandinas, y no se conoce ninguna vía que conecte este mecanismo con la regulación de la gastrina, la función de las células G o la secreción de ácido gástrico. El puntaje elevado (0,994) proviene exclusivamente de patrones del grafo de conocimiento, sin respaldo biológico, ensayo clínico ni publicación.

Además, caspofungina se administra por vía intravenosa y tiene una biodisponibilidad oral limitada, lo que restringiría cualquier uso dirigido al tracto gastrointestinal. La compatibilidad de vías de administración con la nueva indicación está pendiente de evaluar.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones vigentes (todas de medicamento con un solo principio activo; ninguna cancelada).

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 01196001 | CANCIDAS 50 mg | Polvo para concentrado para solución para perfusión | No disponible en los datos |
| 85533 | Caspofungina Stadafarma 70 mg EFG | Polvo para concentrado para solución para perfusión | No disponible en los datos |
| 89229 | Caspofungina Tillomed 50 mg EFG | Polvo para concentrado para solución para perfusión | No disponible en los datos |
| 83627 | Fornega 50 mg EFG | Polvo para concentrado para solución para perfusión | No disponible en los datos |
| 81703 | Caspofungina Mylan 50 mg EFG | Polvo para concentrado para solución para perfusión | No disponible en los datos |

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación en el grafo de conocimiento** (no proviene del texto del prospecto): enfermedad hepática, enfermedad de la vesícula biliar y deficiencia de potasio.
- **Interacciones farmacológicas**: se registraron 81 interacciones. Las principales son:
  - **Mayor**: dexametasona.
  - **Moderada**: naltrexona.
  - **Nivel no clasificado**: calcitriol, pantoprazol, doxiciclina, morfina, omeprazol, lansoprazol, vancomicina, sucralfato, lactulosa, prednisona, simvastatina, nistatina, epinefrina, anfotericina B, hidrocortisona, manitol, cloruro de potasio y prednisolona, entre otros.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5): no hay ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible entre la inhibición de la glucano sintasa fúngica y la secreción de gastrina. La vía intravenosa y las numerosas interacciones farmacológicas añaden más obstáculos.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), pendiente para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Identificar estudios preclínicos o de mecanismo que conecten caspofungina con la fisiología de la gastrina.
- Evaluar la compatibilidad de la vía de administración con la nueva indicación.
- Revisar con detalle la relevancia clínica de las interacciones, en especial con dexametasona.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

