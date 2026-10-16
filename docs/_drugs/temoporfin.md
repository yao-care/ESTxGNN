---
layout: default
title: Temoporfin
parent: Solo predicción del modelo (L5)
nav_order: 771
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Temoporfin: nueva indicación predicha, Teratoma nasofaríngeo (nivel de evidencia L5). Indicación original: Carcinoma de células escamosas / neoplasia de cabeza y cuello (según…"
---

# Temoporfin
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

# Temoporfina: De Carcinoma de Células Escamosas de Cabeza y Cuello a Teratoma Nasofaríngeo

## Resumen en Una Frase

Temoporfina es un fotosensibilizante utilizado en terapia fotodinámica (TFD), originalmente indicado para el carcinoma de células escamosas y las neoplasias de cabeza y cuello.
El modelo TxGNN predice que podría ser efectivo para **teratoma nasofaríngeo**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta indicación concreta: la predicción se basa únicamente en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Carcinoma de células escamosas / neoplasia de cabeza y cuello (según el grafo de conocimiento; el texto de indicación de las autorizaciones españolas no está disponible) |
| Nueva Indicación Predicha | Teratoma nasofaríngeo |
| Puntaje de Predicción TxGNN | 99.78% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, temoporfina es un fotosensibilizante para terapia fotodinámica: tras su administración y activación con luz de una longitud de onda específica, genera especies reactivas de oxígeno que provocan muerte de las células tumorales. Su eficacia en el cáncer de células escamosas de cabeza y cuello está establecida.

La nasofaringe está anatómicamente próxima a las localizaciones de cabeza y cuello donde se usa temoporfina. Sin embargo, el teratoma es un tumor de células germinales con una biología distinta a la del carcinoma escamoso, y ningún ensayo ni publicación respalda su uso en esta entidad.

Por ello, la puntuación alta del modelo (0.998) no constituye evidencia clínica. Es una hipótesis que requeriría validación preclínica y clínica antes de considerarse seriamente.

### Otras predicciones del modelo (referencia)

| Posición | Enfermedad predicha | Puntaje | Nivel | Comentario |
|------|------|------|------|------|
| 2 | Quiste odontogénico | 99.77% | L5 | Lesión benigna, normalmente de manejo quirúrgico |
| 3 | Neoplasia premaligna | 99.77% | L5 | Biológicamente plausible, pero categoría muy amplia; conviene evaluar entidades específicas (p. ej., displasia oral) |
| 4 | Neoplasia de epiglotis | 99.76% | L5 | Dentro del tracto aerodigestivo superior; plausible, sin evidencia específica |
| 5 | Tumor de testículo y paratestículo | 99.76% | L5 | Sin vínculo anatómico; la administración de luz en profundidad es poco práctica |
| 6 | Neoplasia quística | 99.76% | L4 | Una publicación indirecta sobre TFD adyuvante en tumores paranasales |
| 7 | Neoplasia benigna del suelo de la boca | 99.76% | L5 | Localización plausible; riesgo-beneficio no establecido |
| 8 | Neoplasia benigna de la lengua | 99.76% | L4 | Una publicación indirecta sobre TFD en carcinoma de base de lengua |
| 9 | Neoplasia benigna de hipofaringe | 99.76% | L5 | Adyacente a la indicación aprobada, sin evidencia |
| 10 | Neuroblastoma cervical | 99.76% | L5 | Biología distinta; riesgos pediátricos (fotosensibilidad prolongada) |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Para la indicación principal (teratoma nasofaríngeo) no hay literatura relacionada disponible. Las siguientes publicaciones corresponden a otras predicciones de la lista y aportan solo evidencia indirecta sobre TFD en cabeza y cuello:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [26179387](https://pubmed.ncbi.nlm.nih.gov/26179387/) | 2015 | Serie de casos/cohorte (probable) | World J Surg Oncol | Experiencia preliminar con TFD postoperatoria mediada por temoporfina como tratamiento adyuvante tras cirugía robótica de rescate en carcinoma escamoso recurrente de base de lengua |
| [26072296](https://pubmed.ncbi.nlm.nih.gov/26072296/) | 2015 | Serie clínica (probable) | Photodiagn Photodyn Ther | Viabilidad de la TFD como tratamiento adyuvante a la cirugía en tumores malignos recurrentes de los senos paranasales |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 01197002 | FOSCAN 4 mg/ml solución inyectable | Solución inyectable | No disponible en los datos compilados |
| 01197003 | FOSCAN 1 mg/ml solución inyectable | Solución inyectable | No disponible en los datos compilados |
| 01197005 | FOSCAN 1 mg/ml solución inyectable | Solución inyectable | No disponible en los datos compilados |
| 01197004 | FOSCAN 1 mg/ml solución inyectable | Solución inyectable | No disponible en los datos compilados |

Titular de las autorizaciones: Biolitec Pharma Limited. Las cuatro autorizaciones están vigentes.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Fotosensibilizante para terapia fotodinámica (la citotoxicidad depende de la activación con luz); no es un citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto; es conocida la fotosensibilidad cutánea y ocular prolongada con este tipo de fármacos |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

No se encontraron interacciones farmacológicas registradas en la consulta realizada. Para neuroblastoma cervical (población pediátrica) se señala una preocupación adicional por la fotosensibilidad prolongada.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de teratoma nasofaríngeo se apoya solo en el modelo (nivel L5), sin ensayos ni literatura, y la biología de un tumor de células germinales difiere de la del carcinoma escamoso aprobado. Además, faltan los datos de seguridad del prospecto, lo que impide avanzar al cribado de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), lo cual es un requisito bloqueante.
- Obtener los datos del mecanismo de acción desde DrugBank.
- Obtener el texto de indicación aprobada de las autorizaciones españolas.
- Realizar una revisión sistemática de la literatura sobre TFD con temoporfina en teratoma nasofaríngeo y tumores relacionados.
- Evaluar por separado candidatas más plausibles y específicas (p. ej., neoplasia de epiglotis o displasia/leucoplasia oral) frente a la categoría amplia de neoplasia premaligna.
- Valorar la compatibilidad de la vía de administración y de la entrega de luz para la localización propuesta.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

