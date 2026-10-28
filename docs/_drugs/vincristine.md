---
layout: default
title: Vincristine
parent: Solo predicción del modelo (L5)
nav_order: 850
evidence_level: L5
indication_count: 2
monitor_inn: "Vincristine"
predicted_indications: ["vertebral anomalies and variable endocrine and T-cell dysfunction", "retroperitoneal neoplasm"]
last_modified_at: 2026-10-28
description: "Vincristine: nueva indicación predicha, Anomalías vertebrales con disfunción endocrina y de linfocitos T variable (nivel de evidencia L5). Indicación original: Leucemia linfoblástica aguda"
---

# Vincristine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Vincristina: De Leucemia Linfoblástica Aguda a Anomalías Vertebrales con Disfunción Endocrina y de Linfocitos T Variable
{: .text-alpha }

## Resumen en Una Frase

La vincristina es un alcaloide de la vinca que se usa como antineoplásico. Según el grafo de conocimiento, sus usos registrados incluyen la leucemia linfoblástica aguda y varios linfomas.
El modelo TxGNN predice que podría ser efectiva para **anomalías vertebrales con disfunción endocrina y de linfocitos T variable**, un síndrome congénito raro.
Actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, por lo que se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Leucemia linfoblástica aguda (relación registrada en el grafo de conocimiento; los textos de las autorizaciones españolas disponibles no incluyen indicación) |
| Nueva Indicación Predicha | Anomalías vertebrales con disfunción endocrina y de linfocitos T variable |
| Puntaje de Predicción TxGNN | 0,9924 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 1 de 2) |
| Número de Autorizaciones | 2 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción. Sí consta que la vincristina actúa sobre la tubulina beta de clase I (gen *TUBB*). Es conocido que los alcaloides de la vinca inhiben la polimerización de los microtúbulos y detienen las células en mitosis. Esta actividad antimitótica explica su uso en cánceres hematológicos y tumores de proliferación rápida.

Entre las relaciones registradas en el grafo de conocimiento figuran la leucemia linfoblástica aguda de células T precursoras, linfomas y la histiocitosis de células de Langerhans. Esto sugiere un vínculo con enfermedades del sistema linfoide, pero el puntaje proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

Sin embargo, no se identifica un vínculo mecanístico claro con un síndrome congénito de anomalías vertebrales y disfunción endocrina y de linfocitos T. La acción antimitótica general de la vincristina no tiene una relevancia evidente para esta enfermedad. El puntaje alto del modelo TxGNN (aprendizaje profundo), sin ningún estudio que lo respalde, debe interpretarse con mucha cautela, ya que puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 62378 (vigente) | VINCRISTINA PFIZER 1 mg/ml SOLUCIÓN INYECTABLE EFG | Solución inyectable | No consta en los datos compilados |
| 71117 (cancelada) | VINCRISTINA TEVA 1 mg/ml SOLUCIÓN INYECTABLE EFG | Solución inyectable | No consta en los datos compilados |

Ambas autorizaciones corresponden a medicamentos con vincristina como único principio activo.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (alcaloide de la vinca, antimitótico que actúa sobre la tubulina) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto. En general es menor que en otros citotóxicos; el grafo de conocimiento registra la leucopenia como relación de contraindicación |
| Clasificación de Emetogenicidad | Baja (según la categoría general del fármaco) |
| Ítems de Monitoreo | Hemograma con diferencial, función hepática (bilirrubina), función renal y exploración neurológica periférica |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

- **Contraindicaciones registradas en el grafo de conocimiento** (relaciones del grafo, no texto del prospecto): insuficiencia hepática, colestasis (incluidas las formas intrahepáticas familiares), hiperbilirrubinemia y síndrome de Gilbert, leucopenia, neuropatía periférica y enfermedades neuromusculares (incluida la enfermedad de Charcot-Marie-Tooth), nefropatía aguda por uratos, y enfermedades infecciosas, incluidas las infecciones fúngicas y la dermatofitosis.
- **Interacciones farmacológicas**: no se identificaron interacciones con otros fármacos. El único registro es la unión a su diana farmacológica, la tubulina beta de clase I, que no es una interacción entre fármacos.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún ensayo clínico ni publicación sobre esta indicación (nivel L5), y no se identifica un vínculo mecanístico plausible. El puntaje alto de TxGNN no basta por sí solo para justificar avanzar.

**Para avanzar se necesita:**
- Una hipótesis mecanística que conecte la inhibición de microtúbulos con la fisiopatología de este síndrome
- Estudios preclínicos o series de casos que apoyen la dirección propuesta
- Los textos de indicación y las advertencias del prospecto de AEMPS
- Datos detallados del mecanismo de acción (MOA)
- Una evaluación de seguridad, dado el perfil citotóxico y neurotóxico del fármaco en una población probablemente pediátrica
- Revisar otras predicciones del modelo para la vincristina con más literatura. Un ejemplo es la neoplasia retroperitoneal, cuya evidencia disponible consiste en series y casos de regímenes combinados
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

