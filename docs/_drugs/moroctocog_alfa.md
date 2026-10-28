---
layout: default
title: Moroctocog Alfa
parent: Solo predicción del modelo (L5)
nav_order: 542
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
monitor_inn: "MOROCTOCOG ALFA"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "acquired coagulation factor deficiency", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "flood factor deficiency"]
description: "Moroctocog Alfa: nueva indicación predicha, Trastorno de liberación primaria de las plaquetas (primary release disorder of platelets) (nivel de evidencia L5). Indicación original: No consta en los da…"
---

# Moroctocog Alfa
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Moroctocog Alfa: Trastorno de liberación primaria de las plaquetas (primary release disorder of platelets)
{: .text-alpha }

## Resumen en Una Frase

Moroctocog alfa es un factor VIII de coagulación recombinante con deleción del dominio B, utilizado originalmente para el tratamiento de la hemofilia.
El modelo TxGNN predice que podría ser efectivo para el **trastorno de liberación primaria de las plaquetas**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Trastorno de liberación primaria de las plaquetas (primary release disorder of platelets) |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 5 de 9) |
| Número de Autorizaciones | 9 (vigentes: 5) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Moroctocog alfa es un factor VIII (FVIII) recombinante con deleción del dominio B que repone el FVIII deficiente en la vía intrínseca de la coagulación. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en las fuentes consultadas, pero su función como sustituto del FVIII en la hemofilia está bien establecida.

Los trastornos de liberación primaria de las plaquetas se deben a un defecto en la secreción de los gránulos plaquetarios, no a una deficiencia de FVIII. Por ello, el vínculo mecanístico directo es débil. El puntaje tan alto (0,9997) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no una base biológica demostrada.

**Otras predicciones del modelo (todas con nivel L5 y decisión Hold):**

| Enfermedad predicha | Puntaje TxGNN | Plausibilidad mecanística |
|------|------|------|
| Enfermedad de von Willebrand pseudo (tipo plaquetario) | 0,9997 | Vínculo indirecto: el FVIII se estabiliza con el VWF y puede verse afectado secundariamente. El tratamiento habitual es transfusión de plaquetas o desmopresina. |
| Trombastenia de Glanzmann | 0,9996 | Débil: el defecto está en la integrina αIIbβ3 y el FVIII es normal. |
| Deficiencia adquirida de factores de coagulación | 0,9988 | La más plausible: la hemofilia A adquirida es una deficiencia de FVIII. Sin embargo, los autoanticuerpos inhibidores neutralizan el FVIII y se emplean agentes de bypass e inmunosupresión. La categoría es amplia y heterogénea. |
| Síndrome de Scott | 0,9986 | Débil: el defecto está en la exposición de fosfatidilserina (TMEM16F/ANO6). |
| Diátesis hemorrágica por defecto del receptor de colágeno | 0,9973 | Sin vínculo directo: defecto plaquetario independiente del FVIII. |
| Trastorno hemorrágico por trombocitopenia constitucional | 0,9972 | Sin vínculo: afecta al número o producción de plaquetas. |
| "Flood factor deficiency" | 0,9911 | Término poco claro, posible artefacto de la ontología; debe verificarse. |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 99103003 | REFACTO AF 1000 UI | Polvo y disolvente para solución inyectable | No disponible |
| 99103002 | REFACTO AF 500 UI | Polvo y disolvente para solución inyectable | No disponible |
| 99103007 | REFACTO AF 1000 UI | Polvo y disolvente para solución inyectable en jeringa precargada | No disponible |
| 99103008 | REFACTO AF 2000 UI | Polvo y disolvente para solución inyectable en jeringa precargada | No disponible |
| 99103004 | REFACTO AF 2000 UI | Polvo y disolvente para solución inyectable | No disponible |

Se muestran 5 de las 9 autorizaciones vigentes, todas de Pfizer Europe MA EEIG.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Todas las indicaciones predichas se apoyan únicamente en el puntaje del modelo (nivel L5), sin ensayos ni literatura, y para la mayoría el mecanismo no es coherente con una terapia de reposición de FVIII.

**Para avanzar se necesita:**
- Obtener el prospecto de AEMPS (advertencias y contraindicaciones), pues es un vacío de información que impide la evaluación de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Priorizar la revisión de la deficiencia adquirida de factores de coagulación (hemofilia A adquirida), la candidata más plausible, mediante búsqueda sistemática de literatura y ensayos.
- Verificar la definición del término "flood factor deficiency" en la ontología de origen.
- Completar el análisis de similitud con la indicación original y de compatibilidad de vía de administración.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

