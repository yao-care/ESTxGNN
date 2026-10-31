---
layout: default
title: Temozolomide
parent: Solo predicción del modelo (L5)
nav_order: 772
evidence_level: L5
indication_count: 1
monitor_inn: "Temozolomide"
predicted_indications: ["cauda equina neoplasm"]
last_modified_at: 2026-10-31
description: "Temozolomide: nueva indicación predicha, Neoplasia de la cauda equina (cauda equina neoplasm) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Temozolomide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Temozolomide: Neoplasia de la cauda equina (cauda equina neoplasm)
{: .text-alpha }

## Resumen en Una Frase

Temozolomida es un agente alquilante oral, utilizado originalmente según el grafo de conocimiento para el astrocitoma anaplásico, el astrocitoma (excluido el glioblastoma) y el glioblastoma cerebral.
El modelo TxGNN predice que podría ser efectivo para **neoplasia de la cauda equina**, pero hasta ahora solo hay **0 ensayos clínicos** y **3 publicaciones** (todas informes de caso, solo una de ellas con relación directa con la predicción).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Neoplasia de la cauda equina (cauda equina neoplasm) |
| Puntaje de Prediccion TxGNN | 0.9930 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 2) |
| Número de Autorizaciones | al menos 20 |
| Decision Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento farmacológico general, temozolomida es un agente alquilante oral que metila el ADN (O6-guanina, N7-guanina, N3-adenina), lo que produce lesiones citotóxicas y apoptosis. La sensibilidad es mayor en tumores con el promotor de MGMT metilado, por su menor capacidad de reparación.

Sus relaciones registradas en el grafo de conocimiento corresponden a gliomas del sistema nervioso central. La neoplasia de la cauda equina incluye tumores neuroepiteliales, como el ependimoma mixopapilar, de modo que la penetración en el sistema nervioso central y la actividad en gliomas ofrecen una justificación mecanística plausible.

Esta relación es una hipótesis. No se dispone de datos de estado de MGMT ni de otros biomarcadores predictivos para esta indicación.

**Nivel de evidencia L5:** el único estudio con relación directa es un informe de caso de ependimoma mixopapilar espinal recurrente. Aunque describe una respuesta notable, es un caso aislado y no sustenta un nivel superior. Los otros dos informes tratan de otras enfermedades (carcinoma NUT nasal y criptococosis en un paciente con glioma pontino).

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29270703](https://pubmed.ncbi.nlm.nih.gov/29270703/) | 2018 | Informe de caso | European Spine Journal | Eficacia notable de temozolomida en un ependimoma mixopapilar espinal recurrente con diseminación en el líquido cefalorraquídeo; incluye revisión de la literatura |
| [42760727](https://pubmed.ncbi.nlm.nih.gov/42760727/) | 2026 | Informe de caso | Medicine | Carcinoma NUT nasal con respuestas repetidas a tratamiento multimodal con radioterapia; relación indirecta con la indicación predicha |
| [18706663](https://pubmed.ncbi.nlm.nih.gov/18706663/) | 2009 | Informe de caso | Neuro-Chirurgie | Criptococosis neuromeníngea atípica en un niño tratado por glioma pontino; no estudia la eficacia en la indicación predicha |

## Información de Mercado en España

Se muestran 5 de las al menos 20 autorizaciones registradas (la lista puede ser parcial). Los datos disponibles no incluyen texto de indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 110615031 | Temozolomida Accord 140 mg cápsulas duras EFG | Cápsula dura | Sin texto de indicación disponible |
| 111697021 | Temozolomida SUN 180 mg cápsulas duras EFG | Cápsula dura | Sin texto de indicación disponible |
| 98096023 | Temodal 2,5 mg/ml polvo para solución para perfusión | Polvo para solución para perfusión | Sin texto de indicación disponible |
| 11697001 | Temozolomida SUN 5 mg cápsulas duras EFG | Cápsula dura | Sin texto de indicación disponible |
| 09606005 | Temozolomida Teva 100 mg cápsulas duras EFG | Cápsula dura | Sin texto de indicación disponible |


## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (agente alquilante, clase de las imidazotetrazinas) |
| Riesgo de Mielosupresión | Medio a alto. El grafo de conocimiento registra relaciones de contraindicación con neutropenia, trombocitopenia, pancitopenia y anemia aplásica |
| Clasificación de Emetogenicidad | Media |
| Items de Monitoreo | Hemograma completo con fórmula leucocitaria, función hepática y renal. Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

- **Contraindicaciones registradas en el grafo de conocimiento** (no proceden del texto del prospecto): insuficiencia hepática, trombocitopenia, neutropenia, agranulocitosis, anemia, anemia macrocítica, neumocistosis, pancitopenia, linfopenia, síndrome mielodisplásico, anemia aplásica idiopática y anemia aplásica.
- **Interacciones farmacológicas:** se identificaron 100 interacciones. Entre las listadas, naltrexona es de nivel moderado y levofloxacino de nivel menor. El resto (por ejemplo calcitriol, pantoprazol, doxiciclina, morfina, metformina, omeprazol, prednisona) tiene nivel desconocido.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en un informe de caso directamente relevante y en un razonamiento mecanístico general, sin ensayos clínicos, por lo que corresponde a un nivel L5. Además, falta la información de seguridad del prospecto, que es un requisito previo.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones)
- Completar los datos del mecanismo de acción
- Revisión sistemática de la literatura sobre temozolomida en ependimoma mixopapilar y otros tumores de la cauda equina
- Datos de estado de MGMT y otros biomarcadores en estos tumores
- Series de casos o estudios prospectivos que evalúen eficacia y tolerabilidad en esta indicación
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

