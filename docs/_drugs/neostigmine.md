---
layout: default
title: Neostigmine
parent: Solo predicción del modelo (L5)
nav_order: 559
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Neostigmine: nueva indicación predicha, Miastenia gravis con hiperplasia de timo (nivel de evidencia L5). Indicación original: Miastenia gravis (según el grafo de conocimiento"
---

# Neostigmine
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

# Neostigmina: De Miastenia Gravis a Miastenia Gravis con Hiperplasia de Timo

## Resumen en Una Frase

Neostigmina es un inhibidor reversible de la acetilcolinesterasa, utilizado originalmente para el tratamiento de la miastenia gravis y de enfermedades de la unión neuromuscular.
El modelo TxGNN predice que podría ser efectivo para **miastenia gravis con hiperplasia de timo**, pero actualmente **no hay ensayos clínicos ni publicaciones** específicas que respalden esta indicación. Además, se trata de un subtipo de una indicación ya establecida, por lo que no constituye un reposicionamiento genuino.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Miastenia gravis (según el grafo de conocimiento; el texto de indicación de las autorizaciones españolas no está disponible) |
| Nueva Indicación Predicha | Miastenia gravis con hiperplasia de timo |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos. Según la información conocida, neostigmina es un inhibidor reversible de la acetilcolinesterasa (diana: ACHE) que aumenta la acetilcolina en la sinapsis de la unión neuromuscular. Esta es la base de su uso en la miastenia gravis.

La miastenia gravis con hiperplasia de timo es un subtipo de la misma enfermedad, por lo que el puntaje alto del modelo es plausible. Sin embargo, precisamente por ello no representa una oportunidad real de reposicionamiento: la indicación ya está cubierta por el uso conocido del fármaco. No se dispone de ensayos ni literatura específicos para este subtipo.

Entre las demás predicciones, solo la **miastenia gravis neonatal transitoria** (nivel L4, etapa S1, "pregunta de investigación") muestra evidencia algo más consistente, basada en series y reportes de casos. Otras predicciones (hiperesplenismo, síndrome hemolítico urémico atípico, bronquitis, miastenia congénita refractaria a inhibidores de la acetilcolinesterasa) carecen de fundamento mecanístico o presentan conflicto con el mecanismo del fármaco.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación específica.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 4237 | PROSTIGMINE AMPOLLAS (Meda Pharma S.L.) | Solución inyectable | No disponible en los datos compilados |
| 36384 | NEOSTIGMINA BRAUN 0,5 MG/ML (B Braun Medical S.A.) | Solución inyectable | No disponible en los datos compilados |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): epilepsia, úlcera péptica, asma (intrínseco y alérgico), paro cardíaco súbito, enfermedad del sistema de conducción cardíaco, peritonitis, hipertiroidismo (enfermedad de Graves, tirotoxicosis), obstrucción de las vías urinarias y enfermedad de Hirschsprung (incluidos síndromes asociados, como Mowat-Wilson).
- **Interacciones farmacológicas**: solo se registró la interacción farmacológica con su diana, la acetilcolinesterasa (inhibición), sin datos de interacciones con otros fármacos.
- Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción corresponde a un subtipo de una indicación ya conocida, con puntaje alto pero sin ensayos ni literatura específicos (nivel L5). No supone una oportunidad real de reposicionamiento.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS para confirmar las indicaciones autorizadas, advertencias y contraindicaciones
- Confirmar si la miastenia gravis con hiperplasia de timo ya está cubierta por la indicación autorizada
- Completar los datos del mecanismo de acción desde DrugBank
- Si se desea explorar un reposicionamiento real, priorizar la miastenia gravis neonatal transitoria, evaluando dosificación y seguridad neonatal
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

