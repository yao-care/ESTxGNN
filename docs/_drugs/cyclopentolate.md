---
layout: default
title: Cyclopentolate
parent: Solo predicción del modelo (L5)
nav_order: 210
evidence_level: L5
indication_count: 3
---

# Cyclopentolate
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Ciclopentolato: De Cicloplejía a Síndrome de la Cola de Caballo

## Resumen en Una Frase

Ciclopentolato es un fármaco anticolinérgico de uso oftálmico, originalmente utilizado para producir cicloplejía (parálisis de la acomodación del ojo).
El modelo TxGNN predice que podría ser efectivo para el **síndrome de la cola de caballo**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cicloplejía |
| Nueva Indicación Predicha | Síndrome de la cola de caballo |
| Puntaje de Predicción TxGNN | 99,54% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la farmacología general, el ciclopentolato es un antagonista muscarínico (anticolinérgico). Su eficacia como cicloplégico en oftalmología está establecida, y mecanísticamente el bloqueo muscarínico podría tener alguna relevancia en trastornos con disfunción neuromuscular de la vejiga o el intestino.

El síndrome de la cola de caballo es una emergencia neurológica compresiva con disfunción vesical, intestinal y motora, cuyo tratamiento definitivo es la descompresión quirúrgica. La única justificación plausible sería el control sintomático de la hiperactividad del detrusor mediante bloqueo muscarínico, un efecto indirecto que no modifica la enfermedad.

Además, el puntaje elevado de TxGNN (0,995) es solo una predicción computacional. El ciclopentolato se comercializa únicamente como colirio, por lo que la exposición sistémica y la vía o formulación adecuadas para este uso no están establecidas.

### Otras predicciones del modelo (para contexto)

| Rango | Enfermedad predicha | Puntaje TxGNN | Nivel | Comentario |
|---|---|---|---|---|
| 2 | Vejiga neurógena (término obsoleto en la ontología) | 99,40% | L5 | Plausibilidad mecanística relativamente buena (antimuscarínicos como oxibutinina y tolterodina), pero el término debe reasignarse a uno vigente (p. ej., hiperactividad neurógena del detrusor). Existen alternativas mejor respaldadas. |
| 3 | Síndrome del intestino irritable | 99,27% | L5 | Vínculo indirecto por efecto de clase (antiespasmódicos). Podría empeorar el estreñimiento y no hay formulación dirigida al tracto digestivo. |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 42117 | Colirofta Ciclopléjico 10 mg/ml colirio en solución | Colirio en solución | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proceden del prospecto)**: hipertensión y trastornos hipertensivos, diabetes mellitus, cetoacidosis diabética, hiperplasia benigna de próstata, enfermedad cardíaca y cardiovascular, enfermedad coronaria, paro cardíaco súbito, enfermedad de la conducción cardíaca, glaucoma de ángulo cerrado, hipertiroidismo, enfermedad de Graves, tirotoxicosis, arteriosclerosis y aterosclerosis, lesión cerebral, enfermedad cerebral y síndrome de Down.
- **Consideraciones adicionales**: para un uso sistémico, preocupan los efectos anticolinérgicos con penetración en el sistema nervioso central (p. ej., confusión y alucinaciones en pacientes susceptibles).
- No se encontraron interacciones farmacológicas registradas en la consulta realizada.

Consultar el prospecto para obtener la información completa de advertencias y contraindicaciones.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos ni publicaciones. Además, la vía de administración actual (oftálmica tópica) no es compatible con la indicación propuesta, y el perfil de contraindicaciones es amplio.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), actualmente un vacío bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción (p. ej., mediante DrugBank).
- Revisar la bibliografía y los registros de ensayos clínicos para ciclopentolato en trastornos neurógenos de vejiga o intestino.
- Reasignar el término obsoleto "vejiga neurógena" a una enfermedad vigente y valorar si es una indicación predicha más plausible.
- Evaluar la compatibilidad de vía y formulación, y comparar con antimuscarínicos de uso establecido.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

