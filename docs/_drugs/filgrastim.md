---
layout: default
title: Filgrastim
parent: Solo predicción del modelo (L5)
nav_order: 336
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
monitor_inn: "FILGRASTIM"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "Scott syndrome", "hemorrhagic disorder due to a constitutional thrombocytopenia", "bleeding diathesis due to a collagen receptor defect", "C1 inhibitor deficiency", "serpinopathy with toxic serpin polymerization", "fetal and neonatal alloimmune thrombocytopenia", "platelet-type bleeding disorder"]
description: "Filgrastim: nueva indicación predicha, Trastorno de liberación primaria de las plaquetas (primary release disorder of platelets) (nivel de evidencia L5). Indicación original: No consta en los datos l…"
---

# Filgrastim
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

## Filgrastim: Trastorno de liberación primaria de las plaquetas (primary release disorder of platelets)
{: .text-alpha }

## Resumen en Una Frase

Filgrastim es un factor estimulante de colonias de granulocitos (G-CSF), utilizado originalmente en neutropenias crónicas y congénitas (neutropenia constitucional, neutropenia congénita grave, hematopoyesis cíclica y neutropenia crónica familiar).
El modelo TxGNN predice que podría ser efectivo para el **trastorno de liberación primaria de las plaquetas**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción directamente; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Trastorno de liberación primaria de las plaquetas (primary release disorder of platelets) |
| Puntaje de Predicción TxGNN | 1.0000 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 12) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados en las fuentes compiladas. Según la información conocida, filgrastim es un G-CSF recombinante que actúa sobre el receptor de G-CSF en el linaje granulocítico, estimulando la proliferación y maduración de neutrófilos. Su eficacia en las neutropenias congénitas y crónicas está bien establecida.

La relación entre la indicación original y la nueva es débil. Los trastornos de liberación plaquetaria afectan a la función de las plaquetas (secreción de gránulos), no al número de neutrófilos, y no se ha identificado un vínculo mecanístico establecido con la señalización de G-CSF. El puntaje alto proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica o clínica.

Las otras indicaciones predichas con mayor puntaje (pseudo-enfermedad de von Willebrand, trombastenia de Glanzmann, síndrome de Scott, entre otras) presentan el mismo patrón: sin ensayos, sin literatura y sin mecanismo plausible. Por ello, esta predicción debe considerarse generadora de hipótesis y no una recomendación terapéutica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para el trastorno de liberación primaria de las plaquetas.

Como referencia, la predicción de rango 10 ("trastorno hemorrágico de tipo plaquetario") tiene 7 ensayos asociados, todos de relevancia indirecta (trasplante de progenitores hematopoyéticos en neoplasias hematológicas, donde G-CSF es un componente de apoyo). No evalúan filgrastim en trastornos plaquetarios y no se consideran evidencia para la predicción principal.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se registran 20 autorizaciones vigentes (todas monofármaco). Las principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 08495003 | ZARZIO 30 MU/0,5 ml | Solución inyectable y para perfusión en jeringa precargada | No disponible |
| 110631007 | NIVESTIM 48 MU/0,5 ml | Solución inyectable y para perfusión | No disponible |
| 114946004 | Accofil 48 MU/0,5 ml | Solución inyectable y para perfusión en jeringa precargada | No disponible |
| 08444006 | RATIOGRASTIM 48 MU/0,8 ml | Solución inyectable y para perfusión en jeringa precargada | No disponible |
| 64314 | NEUPOGEN 30 MU (0,6 mg/ml) | Solución inyectable en jeringa precargada | No disponible |

Las 20 autorizaciones corresponden a las marcas Zarzio, Nivestim, Accofil, Ratiograstim y Neupogen (biosimilares y originador).

## Citotoxicidad

No aplica: filgrastim es un factor de crecimiento hematopoyético, no un fármaco antineoplásico citotóxico.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; las primeras listadas son de nivel moderado. Ejemplos: ibritumomab tiuxetán, tositumomab (incluido I-131), iobenguano (I-131), fludesoxiglucosa (18F), levamisol, trimetrexato, mercaptopurina, abemaciclib, paclitaxel, acalabrutinib, aldesleukina, alemtuzumab, altretamina, trióxido de arsénico, asparaginasa, avapritinib, azacitidina, belantamab mafodotina y bendamustina. Se debe revisar el conjunto completo antes de cualquier uso.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos ni literatura, y no existe un vínculo mecanístico plausible entre la señalización de G-CSF y la función plaquetaria. No hay base para avanzar.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consulta a DrugBank) y análisis de plausibilidad biológica con la función plaquetaria
- Revisión sistemática de literatura preclínica o clínica sobre G-CSF en trastornos plaquetarios
- Obtención y análisis del prospecto de la AEMPS (advertencias y contraindicaciones), necesario para cualquier evaluación de seguridad
- Texto de indicaciones aprobadas de las autorizaciones españolas
- Evaluación de compatibilidad de vía de administración y similitud con la indicación original (pendientes)
- Valorar otras predicciones del listado con mayor racionalidad biológica, por ejemplo en trombocitopenias constitucionales, si se dispone de evidencia directa
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

