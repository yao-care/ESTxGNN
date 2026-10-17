---
layout: default
title: Deanol
parent: Solo predicción del modelo (L5)
nav_order: 227
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Deanol: nueva indicación predicha, Insomnio (nivel de evidencia L5). Indicación original: No disponible en la autorización de la AEMPS"
monitor_inn: "deanol"
predicted_indications: ["insomnia (disease)"]
---

# Deanol
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

# Deanol: De Indicación No Registrada a Insomnio

## Resumen en Una Frase

Deanol (DMAE) es un fármaco comercializado en España como solución oral (DENUBIL), cuya indicación aprobada no figura en los datos compilados para este informe.
El modelo TxGNN predice que podría ser efectivo para **Insomnio**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: el único apoyo es la predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en la autorización de la AEMPS |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.87% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información general conocida, el deanol se describe como un precursor de la colina, lo que en teoría podría influir en la señalización colinérgica y, con ello, en la arquitectura del sueño. Esta es una hipótesis basada en conocimiento general y no está respaldada por los datos compilados para este informe.

Tampoco se puede establecer una relación entre la indicación original y la nueva, ya que la autorización española no incluye texto de indicación. Además, no está claro si la modulación colinérgica ayudaría o empeoraría el insomnio.

Por lo tanto, la razonabilidad de la predicción descansa únicamente en el alto puntaje del grafo de conocimiento (0.9987). No hay un vínculo mecanístico verificable.

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
| 49691 | DENUBIL 250 mg/180 mg SOLUCIÓN ORAL (Pierre Fabre Ibérica S.A.) | Solución oral | No especificada en los datos disponibles |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas para este fármaco en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5), sin ensayos clínicos, literatura ni mecanismo de acción documentado. Además, faltan los datos de seguridad del prospecto, lo que impide avanzar al cribado de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS para obtener advertencias y contraindicaciones, y confirmar la indicación aprobada.
- Obtener el mecanismo de acción desde DrugBank y analizar su vínculo con el insomnio, incluyendo si la modulación colinérgica podría empeorar el sueño.
- Buscar ensayos clínicos y literatura sobre deanol en trastornos del sueño.
- Evaluar la compatibilidad de la vía de administración (actualmente solo solución oral) con la nueva indicación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

