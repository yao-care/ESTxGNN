---
layout: default
title: Rabeprazole
parent: Solo predicción del modelo (L5)
nav_order: 676
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Rabeprazole: nueva indicación predicha, Mastocitosis sistémica latente (smouldering) (nivel de evidencia L5). Indicación original: Enfermedad ulcerosa péptica y reflujo gastroesofágico (según las ind…"
---

# Rabeprazole
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Rabeprazol: De Enfermedad Ulcerosa Péptica a Mastocitosis Sistémica Latente (Smouldering)

## Resumen en Una Frase

Rabeprazol es un inhibidor de la bomba de protones, utilizado originalmente para el tratamiento de la enfermedad ulcerosa péptica y el reflujo gastroesofágico.
El modelo TxGNN predice que podría ser efectivo para **mastocitosis sistémica latente (smouldering)**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad ulcerosa péptica y reflujo gastroesofágico (según las indicaciones del grafo de conocimiento; los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Mastocitosis sistémica latente (smouldering) |
| Puntaje de Predicción TxGNN | 99.44% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, rabeprazol pertenece a la clase de los inhibidores de la bomba de protones, su eficacia en patologías de hipersecreción ácida está establecida, y mecanísticamente podría ser aplicable de forma limitada a la mastocitosis sistémica.

Entre las indicaciones originales registradas figuran la mastocitosis, la mastocitosis sistémica y el síndrome de Zollinger-Ellison. Esto probablemente explica el puntaje alto del modelo: la nueva indicación está muy próxima a estas enfermedades en el grafo de conocimiento.

Conviene ser claro sobre el alcance: el vínculo es indirecto y se basa solo en la predicción. En la mastocitosis, los mediadores de los mastocitos pueden provocar hipersecreción ácida gástrica, y el rabeprazol aportaría control sintomático de la acidez. No actúa sobre la enfermedad clonal de mastocitos (por ejemplo, la proliferación impulsada por KIT D816V), por lo que no hay un mecanismo modificador de la enfermedad respaldado.

Una segunda predicción (rango 2), la mastocitosis linfadenopática con eosinofilia (puntaje 99.35%), sigue la misma lógica de proximidad en el grafo y tampoco cuenta con evidencia. No hay indicios de que la inhibición de la bomba de protones afecte la linfadenopatía, la eosinofilia ni la biología clonal de los mastocitos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones vigentes (todas de medicamentos de un solo principio activo). Los textos de indicación aprobada no estaban disponibles en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 76934 | Rabeprazol Mabo 10 mg comprimidos gastrorresistentes EFG | Comprimido gastrorresistente | No disponible |
| 034216186 | Pariet 20 mg comprimidos gastrorresistentes | Comprimido gastrorresistente | No disponible |
| 62461 | Pariet 10 mg comprimidos gastrorresistentes | Comprimido gastrorresistente | No disponible |
| 72744 | Rabeprazol Cinfa 20 mg comprimidos gastrorresistentes EFG | Comprimido gastrorresistente | No disponible |
| 73505 | Rabeprazol Sandoz 10 mg comprimidos gastrorresistentes EFG | Comprimido gastrorresistente | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proviene del texto del prospecto): enfermedad hepática, enfermedad de la vesícula biliar, osteoporosis, osteoporosis posmenopáusica y fractura ósea.
- **Interacciones farmacológicas**: se identificaron 100 interacciones en total; se muestran las de mayor gravedad entre las primeras 20 revisadas:
  - **Mayor**: acalabrutinib, atazanavir.
  - **Moderada**: por ejemplo, amikacina, anfotericina B (y sus formulaciones), anfetamina, apalutamida, aprepitant, armodafinilo, bosutinib, bendroflumetiazida.
  - **Menor**: ácido acetilsalicílico, axitinib.

No se dispone de advertencias principales ni de contraindicaciones extraídas del prospecto. Consultar el prospecto para esta información.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción alcanza un puntaje alto (99.44%), pero se basa solo en la proximidad en el grafo de conocimiento (nivel L5), sin ensayos clínicos ni literatura. El rabeprazol solo aportaría control sintomático de la hipersecreción ácida y no tiene un efecto demostrado sobre la enfermedad clonal de mastocitos.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) del rabeprazol.
- Advertencias y contraindicaciones del prospecto de la AEMPS (hoy es un bloqueo para el cribado de seguridad).
- Revisión de la literatura y de registros de ensayos sobre inhibidores de la bomba de protones en mastocitosis sistémica.
- Aclarar si el beneficio buscado es solo sintomático (control de la acidez) o si se pretende un efecto sobre la enfermedad.
- Evaluar las interacciones de gravedad mayor (acalabrutinib, atazanavir) y las contraindicaciones del grafo (enfermedad hepática, osteoporosis) en la población con mastocitosis.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

