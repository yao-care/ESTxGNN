---
layout: default
title: Tropicamide
parent: Solo predicción del modelo (L5)
nav_order: 831
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Tropicamide: nueva indicación predicha, Síndrome de la cola de caballo (nivel de evidencia L5). Indicación original: Cicloplejia (según el grafo de conocimiento"
monitor_inn: "Tropicamide"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome"]
---

# Tropicamide
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

# Tropicamida: De Cicloplejia a Síndrome de la Cola de Caballo

## Resumen en Una Frase

La tropicamida es un antimuscarínico oftálmico de acción corta, utilizado originalmente para producir cicloplejia y midriasis en exploraciones oculares.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de la cola de caballo**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cicloplejia (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Síndrome de la cola de caballo |
| Puntaje de Predicción TxGNN | 99,53% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

La tropicamida es un antagonista muscarínico. Según los datos farmacológicos compilados, se une a los receptores M2, M3, M4 y M5 (la literatura de clase sugiere cierta preferencia por M4). No se dispone de una descripción detallada del mecanismo de acción en los datos originales, por lo que esta explicación se basa en la farmacología conocida de la clase.

En teoría, la actividad anticolinérgica podría reducir la hiperactividad del detrusor y los síntomas de disfunción vesical asociados al síndrome de la cola de caballo. Sin embargo, esta enfermedad es una urgencia quirúrgica causada por la compresión de raíces nerviosas, y un tratamiento anticolinérgico sintomático no abordaría la causa subyacente.

Además, la tropicamida se presenta como colirio con exposición sistémica mínima, por lo que no está establecida una vía de administración adecuada para este uso. La puntuación alta del modelo (0,995) es solo una predicción computacional.

**Otras predicciones del modelo (todas con nivel L5 y decisión Hold):**

| Indicación predicha | Puntaje TxGNN | Comentario |
|------|------|------|
| Vejiga neurógena (término obsoleto) | 99,13% | El antagonismo muscarínico es un mecanismo validado para la hiperactividad neurógena del detrusor (p. ej., oxibutinina, tolterodina). El término figura como obsoleto en la ontología y debería reasignarse a un concepto vigente (p. ej., hiperactividad neurógena del detrusor) antes de evaluarlo. |
| Síndrome del intestino irritable | 99,12% | Existe un racional por efecto de clase (antiespasmódicos antimuscarínicos como hioscina o diciclomina), pero la formulación oftálmica y la corta duración de acción dificultan la traslación directa. |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 88867 | Minims Tropicamida 10 mg/ml colirio en solución en envase unidosis (Bausch + Lomb Ireland Limited) | Colirio en solución | No disponible en los datos compilados |
| 57050 | Colirofta Tropicamida 10 mg/ml colirio en solución (Alcon Healthcare S.A.) | Colirio en solución | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proceden del prospecto):** hipertensión arterial, glaucoma de ángulo abierto, glaucoma de ángulo cerrado, hipertensión ocular, diabetes mellitus, cetoacidosis diabética, paro cardíaco súbito, enfermedad del sistema de conducción cardíaco, hipertiroidismo, enfermedad de Graves, tirotoxicosis, isquemia miocárdica y enfermedad coronaria.
- **Interacciones farmacológicas:** los datos compilados no muestran interacciones con otros fármacos, sino únicamente la unión a los receptores muscarínicos M2, M3, M4 y M5 (actividad farmacológica esperada).
- **Efectos adversos anticolinérgicos a considerar:** estreñimiento, boca seca y visión borrosa.

Las advertencias y contraindicaciones del prospecto de la AEMPS no estaban disponibles; consultar el prospecto para la información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura. Además, la indicación principal (síndrome de la cola de caballo) es una urgencia quirúrgica que un tratamiento sintomático no resolvería, y el fármaco solo existe en forma de colirio.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), requisito bloqueante para cualquier cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Remapear el término obsoleto "vejiga neurógena" a un concepto vigente y reevaluar esa predicción.
- Realizar una búsqueda sistemática de literatura y ensayos clínicos para las tres indicaciones predichas.
- Evaluar la viabilidad de una vía de administración sistémica o intravesical, dado que solo existe formulación oftálmica.
- Valorar si el síndrome del intestino irritable o la hiperactividad neurógena del detrusor son candidatas más plausibles que el síndrome de la cola de caballo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

