---
layout: default
title: Gilteritinib
parent: Solo predicción del modelo (L5)
nav_order: 257
evidence_level: L5
indication_count: 1
---

# Gilteritinib
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

# Gilteritinib: De Leucemia Mieloide Aguda con Mutación FLT3 a Poliomielitis Bulbar

## Resumen en Una Frase

Gilteritinib es un inhibidor de quinasas FLT3/AXL que se utiliza en la leucemia mieloide aguda (LMA) con mutación FLT3 en recaída o refractaria.
El modelo TxGNN predice que podría ser efectivo para **poliomielitis bulbar**, pero **no hay ningún ensayo clínico ni publicación** que respalde esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Leucemia mieloide aguda con mutación FLT3, en recaída o refractaria (el registro de la AEMPS no incluye el texto de indicación; se toma del análisis de mecanismo) |
| Nueva Indicación Predicha | Poliomielitis bulbar |
| Puntaje de Predicción TxGNN | 99.10% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, gilteritinib es un inhibidor de quinasas dirigido a FLT3 y AXL. Su eficacia se ha comprobado en la LMA con mutación FLT3, pero no en enfermedades infecciosas.

La poliomielitis bulbar es una infección por poliovirus (un enterovirus) que afecta a las neuronas motoras del tronco encefálico. AXL se ha relacionado con la entrada viral o la evasión inmunitaria en otros virus, pero **no hay evidencia de que esto aplique al poliovirus**. Por eso no se identifica un vínculo mecanístico establecido entre la indicación original y la nueva.

El puntaje de 0.991 proviene únicamente de la predicción del grafo de conocimiento y no está respaldado por datos reales. Además, la polio se previene con vacunas. Los riesgos de mielosupresión y prolongación del intervalo QT de gilteritinib serían una preocupación de seguridad en una infección neurológica aguda.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 1191399001 | XOSPATA 40 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | Astellas Pharma Europe B.V. |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de quinasas FLT3/AXL) |
| Riesgo de Mielosupresión | Presente, según el análisis del caso; no hay datos cuantitativos. Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma y electrocardiograma (riesgo de prolongación del QT); para otros parámetros, consultar el prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

No hay datos estructurados de advertencias, contraindicaciones ni interacciones farmacológicas en el Evidence Pack. Se han señalado los riesgos de mielosupresión y prolongación del QT.

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos ni publicaciones, y no existe un vínculo mecanístico plausible con el poliovirus. El perfil de riesgo del fármaco tampoco favorece su uso en una infección aguda prevenible con vacuna.

**Para avanzar se necesita:**
- Datos de mecanismo de acción (MOA) desde DrugBank
- Advertencias y contraindicaciones del prospecto de la AEMPS
- Evidencia preclínica que relacione la inhibición de AXL/FLT3 con la replicación o entrada del poliovirus
- Una evaluación de seguridad específica para una población con infección neurológica aguda
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

