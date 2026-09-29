---
layout: default
title: Cabozantinib
parent: Solo predicción del modelo (L5)
nav_order: 93
evidence_level: L5
indication_count: 10
---

# Cabozantinib
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

# Cabozantinib: De Indicación Original No Registrada a Liposarcoma

## Resumen en Una Frase

Cabozantinib es un inhibidor multicinasa de uso oncológico, comercializado en España como Cometriq y Cabometyx. Los datos recibidos no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **liposarcoma**, con **1 ensayo clínico** (Fase 2, en curso, sin resultados) y **1 publicación** (Fase 1, en sarcomas de extremidades) que respaldan esta dirección de forma indirecta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No registrada (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Liposarcoma |
| Puntaje de Predicción TxGNN | 99.83% |
| Nivel de Evidencia | L5 (criterio estricto; ver nota abajo) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Hold |

> **Nota sobre el nivel de evidencia:** el Evidence Pack asigna L2, pero según las reglas de este informe L2 exige un ECA de Fase 2/3 **completado**. El único ensayo disponible sigue activo, sin resultados, y no es específico de liposarcoma. La publicación es un estudio de Fase 1 de seguridad. Por eso se clasifica como L5.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la farmacología general, cabozantinib es un inhibidor multicinasa que actúa sobre VEGFR2, MET, AXL, RET y KIT. Su eficacia en tumores sólidos está comprobada en otras indicaciones oncológicas, y mecanísticamente podría ser aplicable al liposarcoma.

La angiogénesis dependiente de VEGFR y la señalización MET/AXL son impulsores plausibles en el sarcoma de partes blandas. El liposarcoma es uno de sus subtipos. La publicación disponible indica que cabozantinib muestra actividad en varios subtipos de sarcoma de partes blandas.

Esta relación es una hipótesis. El puntaje TxGNN de 0.998 es solo una predicción del modelo. No hay evidencia clínica específica de liposarcoma, y el ensayo de Fase 2 incluye sarcoma de partes blandas en general.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT05836571](https://clinicaltrials.gov/study/NCT05836571) | Fase 2 | Activo, sin reclutamiento | 66 | Ensayo aleatorizado que compara ipilimumab + nivolumab solos frente a su combinación con cabozantinib en sarcoma de partes blandas avanzado. La población no es específica de liposarcoma y no hay resultados publicados. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41770651](https://pubmed.ncbi.nlm.nih.gov/41770651/) | 2026 | Ensayo Fase 1 | American Journal of Clinical Oncology | Evalúa la seguridad de cabozantinib neoadyuvante con radioterapia concurrente en sarcomas de partes blandas de extremidades. Esa combinación se había limitado por el riesgo de fístula o perforación. |

---

## Información de Mercado en España

Se muestran 5 de las 6 autorizaciones registradas.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 113890004 | Cometriq 20mg cápsulas duras | Cápsula dura | No registrada |
| 113890005 | Cometriq 20mg+80mg cápsulas duras | Cápsula dura | No registrada |
| 113890006 | Cometriq 20mg+80mg cápsulas duras | Cápsula dura | No registrada |
| 1161136002 | Cabometyx 20 mg comprimidos recubiertos con película | Comprimido recubierto con película | No registrada |
| 1161136006 | Cabometyx 60 mg comprimidos recubiertos con película | Comprimido recubierto con película | No registrada |

---

## Citotoxicidad

Los datos recibidos no incluyen información de toxicidad de DrugBank. Lo siguiente se basa en la clasificación farmacológica general y debe confirmarse en el prospecto.

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina cinasa multidiana) |
| Riesgo de Mielosupresión | Bajo a medio; consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Baja |
| Items de Monitoreo | Hemograma, función hepática y renal, electrolitos, presión arterial, proteinuria y función tiroidea |
| Protección en Manejo | Consultar las regulaciones locales de manejo de medicamentos peligrosos y el prospecto |

---

## Consideraciones de Seguridad

- **Riesgo de fístula o perforación con radioterapia concurrente:** la publicación de Fase 1 señala que esta preocupación ha limitado el uso combinado de cabozantinib con radioterapia en sarcomas.

Para el resto de la información de seguridad, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de liposarcoma se apoya en un solo ensayo de Fase 2 en curso y sin resultados, con población de sarcoma de partes blandas en general, y en un estudio de Fase 1 de seguridad. No hay ningún estudio completado con eficacia específica en liposarcoma, por lo que la evidencia sigue en el nivel de hipótesis.

**Para avanzar se necesita:**
- Resultados del ensayo NCT05836571, idealmente con análisis por subtipo histológico (liposarcoma).
- Estudios o series de casos específicos de liposarcoma, incluyendo los subtipos bien diferenciado, desdiferenciado y mixoide.
- Datos del mecanismo de acción desde DrugBank.
- Prospecto de la AEMPS con advertencias, contraindicaciones y el texto de la indicación aprobada.
- Consulta de interacciones farmacológicas, ya que la búsqueda no devolvió resultados y podría ser una laguna de datos.

**Contexto adicional:** en este mismo Evidence Pack, la predicción de **carcinoma renal** tiene evidencia mucho más sólida (varios ECA de Fase 3, nivel L1, decisión Proceed with Guardrails). Si el objetivo es priorizar candidatos, conviene evaluarla por separado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

