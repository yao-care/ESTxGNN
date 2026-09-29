---
layout: default
title: Diltiazem
parent: Solo predicción del modelo (L5)
nav_order: 178
evidence_level: L5
indication_count: 1
---

# Diltiazem
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

# Diltiazem: De Indicación Original No Registrada a Susceptibilidad Obsoleta al Ictus Isquémico

## Resumen en Una Frase

Diltiazem es un bloqueador de canales de calcio no dihidropiridínico comercializado en España. Los datos suministrados no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **"susceptibilidad obsoleta al ictus isquémico"**, un término que la ontología marca como obsoleto.
Actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de autorización |
| Nueva Indicación Predicha | Susceptibilidad obsoleta al ictus isquémico (término obsoleto) |
| Puntaje de Predicción TxGNN | 99.08% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información suministrada. Diltiazem es un bloqueador de canales de calcio no dihidropiridínico, con efectos vasodilatadores y reductores de la presión arterial. Esto es farmacología de contexto y no evidencia de los datos aportados. Mecanísticamente, esos efectos podrían relacionarse con el riesgo cerebrovascular.

El único respaldo de esta predicción es la puntuación elevada del grafo de conocimiento TxGNN (0.991). No hay ensayos ni literatura que la confirmen, y no se ha podido evaluar la similitud con la indicación original.

Hay además una advertencia importante: el término de enfermedad está marcado como **obsoleto** en su ontología. Es un nodo en desuso y no una indicación clínica definida, por lo que la puntuación alta podría deberse a artefactos del grafo. Antes de seguir evaluando, conviene asignarlo a un concepto vigente relacionado con el ictus.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Hay 20 autorizaciones en total. Se muestran las 5 principales. El texto de indicación aprobada no figura en los datos, por lo que no se incluye.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 60006 | LACEROL RETARD 120 mg cápsulas duras de liberación prolongada | Cápsula dura de liberación prolongada | Lacer S.A. |
| 11456610496 | TILKER cápsulas | Cápsula dura de liberación prolongada | Lavipharm S.A. |
| 60089 | DOCLIS RETARD 120 mg cápsulas duras de liberación prolongada | Cápsula dura de liberación prolongada | Laboratorios Bial S.A. |
| 60214 | ANGIODROX 300 mg cápsulas duras de liberación prolongada | Cápsula dura de liberación prolongada | Viatris Healthcare Limited |
| 59776 | DINISOR RETARD 180 mg comprimidos de liberación modificada | Comprimido de liberación modificada | Pfizer S.L. |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en la puntuación del modelo (nivel L5), sin ensayos ni literatura. Además, la enfermedad predicha es un término obsoleto que no representa una indicación clínica definida.

**Para avanzar se necesita:**
- Asignar el término obsoleto a un concepto vigente de ictus isquémico o de riesgo cerebrovascular, y repetir la evaluación con ese concepto.
- Obtener el prospecto de la AEMPS para conocer las indicaciones aprobadas, advertencias y contraindicaciones.
- Completar los datos de mecanismo de acción desde DrugBank.
- Buscar ensayos clínicos y literatura sobre diltiazem en ictus isquémico con el concepto ya asignado.
- Evaluar la compatibilidad de vías de administración, hoy pendiente.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

