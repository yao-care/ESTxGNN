---
layout: default
title: Volanesorsen
parent: Solo predicción del modelo (L5)
nav_order: 857
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Volanesorsen: nueva indicación predicha, Anemia megaloblástica (nivel de evidencia L5). Indicación original: No disponible en los datos de la licencia AEMPS (el texto de indicaci…"
monitor_inn: "VOLANESORSEN"
predicted_indications: ["megaloblastic anemia (disease)", "sclerosing cholangitis", "sickle cell disease and related diseases", "sickle cell-hemoglobin d disease syndrome", "sickle cell-beta-thalassemia disease syndrome", "sickle cell-hemoglobin c disease syndrome", "hereditary persistence of fetal hemoglobin-sickle cell disease syndrome", "sickle cell-hemoglobin E disease syndrome", "meningococcal infection", "paroxysmal nocturnal hemoglobinuria"]
---

# Volanesorsen
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

## Volanesorsen: De Hipertrigliceridemia (indicación no registrada en los datos) a Anemia Megaloblástica
{: .text-alpha }

## Resumen en Una Frase

Volanesorsen es un oligonucleótido antisentido dirigido al ARNm de APOC3, que reduce los triglicéridos. Los datos compilados para este informe no incluyen el texto de su indicación aprobada en España.
El modelo TxGNN predice que podría ser efectivo para **anemia megaloblástica**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: la predicción es únicamente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de la licencia AEMPS (el texto de indicación está vacío) |
| Nueva Indicación Predicha | Anemia megaloblástica |
| Puntaje de Predicción TxGNN | 99,997% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, volanesorsen es un oligonucleótido antisentido que se une al ARNm de APOC3 y reduce la producción de apolipoproteína C-III, lo que disminuye los triglicéridos plasmáticos.

La anemia megaloblástica surge por deficiencia de vitamina B12 o folato, que altera la síntesis de ADN en las células hematopoyéticas. No se identifica un vínculo mecanístico entre la inhibición de APOC3 y esta enfermedad. El puntaje TxGNN muy alto (0,99997) refleja una predicción del grafo de conocimiento, no evidencia independiente.

Por ello, la plausibilidad biológica es baja con los datos disponibles, y cualquier conexión (por ejemplo, vías lipídicas o inflamatorias) sería hipotética.

**Otras predicciones del modelo (todas L5, sin ensayos ni literatura):** colangitis esclerosante (99,993%), enfermedad de células falciformes y sus subtipos (≈99,992%), infección meningocócica (99,988%) y hemoglobinuria paroxística nocturna (99,988%). Los subtipos de células falciformes probablemente reflejan un agrupamiento en la ontología y no evidencia independiente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1191360 | WAYLIVRA 285 MG solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada | No disponible en los datos |

## Consideraciones de Seguridad

- **Contraindicaciones (según grafo de conocimiento, no según prospecto):** el grafo de conocimiento asocia el fármaco con contraindicación en **trombocitopenia**. Esto debe verificarse con el prospecto oficial.

Para el resto de la información de seguridad (advertencias, interacciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y sin vínculo mecanístico plausible entre la inhibición de APOC3 y la anemia megaloblástica. Además, el grafo de conocimiento señala trombocitopenia como contraindicación, lo que añade preocupación en enfermedades hematológicas.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), requisito bloqueante para cualquier evaluación de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Confirmar la indicación aprobada en España.
- Realizar una búsqueda sistemática de literatura y ensayos que justifique un vínculo biológico.
- Evaluar el riesgo de trombocitopenia en la población objetivo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

