---
layout: default
title: Albutrepenonacog Alfa
parent: Solo predicción del modelo (L5)
nav_order: 30
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Albutrepenonacog Alfa: nueva indicación predicha, Enfermedad pseudo-von Willebrand (nivel de evidencia L5). Indicación original: Hemofilia (según el grafo de conocimiento"
monitor_inn: "ALBUTREPENONACOG ALFA"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia"]
---

# Albutrepenonacog Alfa
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Albutrepenonacog alfa: De Hemofilia a Enfermedad de von Willebrand Pseudo (pseudo-von Willebrand)

## Resumen en Una Frase

Albutrepenonacog alfa es un factor IX de coagulación recombinante fusionado a albúmina, utilizado originalmente para el tratamiento de la hemofilia.
El modelo TxGNN predice que podría ser efectivo para la **enfermedad pseudo-von Willebrand**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hemofilia (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Enfermedad pseudo-von Willebrand |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado. Según la información conocida, albutrepenonacog alfa es un factor IX recombinante fusionado a albúmina (rFIX-FP), que apoya la vía intrínseca de la coagulación. Su eficacia en la hemofilia, donde falta factor IX, es la base de su uso original.

La enfermedad pseudo-von Willebrand es un trastorno de tipo plaquetario causado por una mutación de ganancia de función en GP1BA, que aumenta la afinidad de las plaquetas por el factor von Willebrand (VWF). Su fenotipo hemorrágico se debe a la disfunción plaquetaria y del VWF, no a un déficit de factor IX.

Por ello, el vínculo mecanístico directo es débil. El puntaje TxGNN, muy alto, proviene de una predicción basada en el grafo y no está respaldado por evidencia clínica ni bibliográfica. Esta predicción debe considerarse una hipótesis exploratoria.

### Otras indicaciones predichas (para contexto)

| Rango | Enfermedad | Puntaje TxGNN | Comentario mecanístico |
|------|------|------|------|
| 2 | Trastorno primario de liberación plaquetaria | 99.94% | El defecto de secreción plaquetaria no se corrige con factor IX; un beneficio por mayor generación de trombina sería puramente teórico. |
| 3 | Trombastenia de Glanzmann | 99.92% | El defecto es la ausencia de integrina αIIbβ3; el tratamiento estándar es transfusión de plaquetas o FVIIa recombinante. |
| 4 | Síndrome de Scott | 99.63% | Existe una conexión conceptual (FIXa actúa en el complejo tenasa), pero el defecto está en la superficie de membrana (TMEM16F/ANO6), no en la cantidad de FIX. |
| 5 | Diátesis hemorrágica por defecto del receptor de colágeno | 99.28% | Defecto plaquetario previo a la cascada de coagulación, sin justificación mecanística para el FIX. |
| 6 | Trastorno hemorrágico por trombocitopenia constitucional | 99.26% | El sangrado se debe a la falta de plaquetas; no hay mecanismo plausible de beneficio con FIX. |

Todas estas predicciones tienen nivel de evidencia L5 y recomendación Hold.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1161095001 | IDELVION 250 UI polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable | No disponible en los datos compilados |
| 1161095002 | IDELVION 500 UI polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable | No disponible en los datos compilados |
| 1161095003 | IDELVION 1000 UI polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable | No disponible en los datos compilados |
| 1161095004 | IDELVION 2000 UI polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable | No disponible en los datos compilados |
| 1161095009 | IDELVION 3.500 UI polvo y disolvente para solución inyectable | Polvo y solución para solución inyectable | No disponible en los datos compilados |

Las cinco autorizaciones corresponden a presentaciones de un solo principio activo, están vigentes y pertenecen a CSL Behring GmbH.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el puntaje del modelo (nivel L5), sin ensayos clínicos ni publicaciones. Además, la fisiopatología de la enfermedad pseudo-von Willebrand es plaquetaria y del VWF, no un déficit de factor IX, por lo que el fundamento mecanístico es débil.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS para completar advertencias y contraindicaciones (es un requisito previo para cualquier evaluación de seguridad).
- Obtener datos del mecanismo de acción desde DrugBank.
- Realizar una revisión sistemática de la literatura y de registros de ensayos sobre factor IX en trastornos hemorrágicos plaquetarios.
- Evaluar estudios preclínicos o de mecanismo (por ejemplo, generación de trombina en modelos de disfunción plaquetaria) antes de plantear un estudio clínico.
- Valorar si las alternativas ya establecidas (transfusión de plaquetas, FVIIa recombinante, antifibrinolíticos) hacen innecesaria esta vía.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

