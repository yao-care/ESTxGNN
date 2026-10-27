---
layout: default
title: Raltitrexed
parent: Solo predicción del modelo (L5)
nav_order: 679
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Raltitrexed: nueva indicación predicha, Colangitis esclerosante (nivel de evidencia L5). Indicación original: No disponible en la ficha de autorización de la AEMPS (el uso clínico…"
monitor_inn: "RALTITREXED"
predicted_indications: ["sclerosing cholangitis", "myelodysplastic syndrome", "sickle cell-hemoglobin E disease syndrome", "sickle cell-beta-thalassemia disease syndrome", "sickle cell-hemoglobin c disease syndrome", "hereditary persistence of fetal hemoglobin-sickle cell disease syndrome", "sickle cell-hemoglobin d disease syndrome", "unclassified myelodysplastic syndrome", "refractory cytopenia of childhood", "partial deletion of the long arm of chromosome 5"]
---

# Raltitrexed
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Raltitrexed: De Indicación Original No Especificada a Colangitis Esclerosante
{: .text-alpha }

## Resumen en Una Frase

Raltitrexed es un inhibidor de la timidilato sintasa (antifolato) que se utiliza en oncología, en concreto en cáncer colorrectal y mesotelioma maligno.
El modelo TxGNN predice que podría ser efectivo para **colangitis esclerosante**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en la ficha de autorización de la AEMPS (el uso clínico conocido es cáncer colorrectal y mesotelioma maligno) |
| Nueva Indicación Predicha | Colangitis esclerosante |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco. Según la información conocida, raltitrexed inhibe la timidilato sintasa (TYMS), enzima clave en la síntesis de ADN, y bloquea así la proliferación de células que se dividen rápidamente. Su eficacia se ha utilizado en cáncer colorrectal y mesotelioma maligno.

Con los datos compilados, **no se identifica un vínculo mecanístico plausible** entre la inhibición de la timidilato sintasa y la patología colestásica, inmunomediada y fibroinflamatoria de la colangitis esclerosante. El puntaje elevado del modelo parece reflejar asociaciones del grafo de conocimiento y no evidencia específica del fármaco. Además, la elevación de transaminasas asociada al fármaco es una preocupación en una enfermedad hepatobiliar.

**Otras predicciones del modelo** (todas con nivel L5, sin ensayos ni literatura, decisión Hold):

| Enfermedad predicha | Puntaje TxGNN | Comentario |
|------|------|------|
| Síndrome mielodisplásico | 99.97% | Racional teórico como antimetabolito, pero la mielosupresión es una preocupación importante en pacientes con citopenias |
| Síndrome mielodisplásico no clasificado | 99.96% | Mismo racional y misma preocupación de seguridad |
| Síndromes de células falciformes (Hb E, beta-talasemia, Hb C, Hb D, persistencia hereditaria de Hb fetal) | 99.96% | Racional especulativo de inducción de hemoglobina fetal, análogo a la hidroxiurea; probablemente refleja agrupación por clase de enfermedad |
| Citopenia refractaria de la infancia | 99.96% | Un antifolato mielosupresor es mecanísticamente contraproducente |
| Deleción parcial del brazo largo del cromosoma 5 | 99.95% | Sin vínculo con la inhibición de la timidilato sintasa; el tratamiento establecido en del(5q) es lenalidomida |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 61452 | TOMUDEX 2 MG POLVO PARA SOLUCIÓN PARA PERFUSIÓN (Hospira Invicta S.A.) | Polvo para solución para perfusión | No especificada en los datos compilados |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antimetabolito, antifolato, inhibidor de la timidilato sintasa) |
| Riesgo de Mielosupresión | Alto (se describen neutropenia, anemia y trombocitopenia) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma completo, función hepática (transaminasas) y función renal |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta se completó y solo registra la interacción farmacológica con su diana, la timidilato sintasa (TYMS), sin nivel de gravedad asignado. No se identificaron interacciones con otros fármacos.
- **Preocupaciones identificadas en el análisis**: elevación de transaminasas (relevante en enfermedad hepatobiliar) y mielosupresión (relevante en síndromes mielodisplásicos y hemoglobinopatías).

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible. Además, el perfil de hepatotoxicidad y mielosupresión del fármaco es desfavorable para las indicaciones predichas.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), imprescindible para el cribado de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Confirmar la indicación aprobada en la autorización de la AEMPS
- Evidencia preclínica o clínica que respalde un vínculo entre la inhibición de la timidilato sintasa y la colangitis esclerosante
- Evaluar la compatibilidad de la vía de administración (actualmente solo perfusión intravenosa)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

