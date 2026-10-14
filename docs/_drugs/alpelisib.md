---
layout: default
title: Alpelisib
parent: Solo predicción del modelo (L5)
nav_order: 42
evidence_level: L5
indication_count: 1
---

# Alpelisib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Alpelisib: De Indicación Original No Disponible a Hipertensión Pulmonar

## Resumen en Una Frase

Alpelisib es un inhibidor de PI3K-alfa comercializado en España bajo la marca Piqray (Novartis), aunque los datos compilados no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **hipertensión pulmonar**, pero **no hay ensayos clínicos** y solo hay **1 publicación** (un reporte de caso que describe un evento adverso pulmonar, no un beneficio terapéutico).
La predicción se apoya únicamente en el modelo, por lo que la evidencia real es muy limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (el texto de indicación de las autorizaciones de AEMPS está vacío) |
| Nueva Indicación Predicha | Hipertensión pulmonar |
| Puntaje de Predicción TxGNN | 99.03% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Alpelisib es un inhibidor de PI3K-alfa. Los datos compilados para este informe no incluyen el mecanismo de acción original, por lo que el razonamiento siguiente se basa en conocimiento general de la clase farmacológica y no en los datos suministrados.

La vía PI3K/AKT/mTOR participa en la proliferación del músculo liso vascular pulmonar y en el remodelado vascular característico de la hipertensión pulmonar. Por ello existe un vínculo teórico entre inhibir PI3K y modificar la enfermedad. Sin embargo, no se dispone de la indicación original aprobada en España, así que no es posible analizar con rigor la relación entre esta y la nueva indicación.

Conviene ser cautos: el puntaje del modelo es muy alto (0.990), pero es solo una predicción computacional. La única publicación recuperada describe una enfermedad pulmonar intersticial inducida por alpelisib en una paciente con cáncer de mama avanzado. Esto no respalda un beneficio terapéutico y sugiere una posible preocupación de seguridad pulmonar.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | Reporte de caso | Journal of Oncology Pharmacy Practice | Enfermedad pulmonar intersticial inducida por alpelisib en una paciente con cáncer de mama avanzado; es un evento adverso pulmonar, no evidencia de beneficio en hipertensión pulmonar |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1201455005 | PIQRAY 50 MG y 200 MG comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos |
| 1201455008 | PIQRAY 200 MG comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos |
| 1201455002 | PIQRAY 150 MG comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de PI3K-alfa) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta de interacciones se completó y devolvió 100 registros. Los 20 mostrados son de nivel moderado y se concentran en antidiabéticos y fármacos relacionados con la glucosa: acarbosa, albiglutida, alogliptina, metformina, pioglitazona, acetohexamida, canagliflozina, clorpropamida, dapagliflozina, empagliflozina, ertugliflozina, exenatida, glimepirida, glipizida y dulaglutida. También figuran alosetrón, bupropión, dexametasona, dronabinol y fidaxomicina.
- **Señal pulmonar**: la única publicación recuperada describe enfermedad pulmonar intersticial asociada a alpelisib, relevante para cualquier uso en patología pulmonar.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos y con una única publicación que apunta a un riesgo pulmonar y no a un beneficio. Con esta evidencia no es posible avanzar.

**Para avanzar se necesita:**
- Obtener el prospecto de AEMPS (indicaciones, advertencias y contraindicaciones), cuya ausencia bloquea el cribado de seguridad
- Obtener datos del mecanismo de acción desde DrugBank
- Revisar de forma específica el riesgo de toxicidad pulmonar, incluida la enfermedad pulmonar intersticial
- Buscar estudios preclínicos de inhibición de PI3K en modelos de hipertensión pulmonar
- Evaluar el perfil de interacciones, en especial con antidiabéticos, dado que alpelisib puede afectar la glucemia
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

