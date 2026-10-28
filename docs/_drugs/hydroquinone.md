---
layout: default
title: Hydroquinone
parent: Solo predicción del modelo (L5)
nav_order: 397
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
description: "Hydroquinone: nueva indicación predicha, Queratosis seborreica (nivel de evidencia L4). Indicación original: No disponible en los datos compilados (los textos de indicación de la…"
monitor_inn: "hydroquinone"
predicted_indications: ["seborrheic keratosis", "vulvar inverted follicular keratosis", "exanthem (disease)", "lichen disease"]
---

# Hydroquinone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Hidroquinona: De Indicación Original No Especificada a Queratosis Seborreica
{: .text-alpha }

## Resumen en Una Frase

La hidroquinona es un agente despigmentante de uso tópico, comercializado en España en cremas y geles para trastornos de la hiperpigmentación. Los datos compiladas para este informe no incluyen el texto de indicación aprobada.
El modelo TxGNN predice que podría ser efectiva para **queratosis seborreica**, pero la evidencia directa es mínima: **ningún ensayo clínico** y **1 publicación** indirecta (un estudio observacional sobre trastornos pigmentarios faciales).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Queratosis seborreica |
| Puntaje de Predicción TxGNN | 0,9973 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 5 de 7) |
| Número de Autorizaciones | 7 (vigentes: 5) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, la hidroquinona inhibe la tirosinasa y reduce la síntesis de melanina, por lo que se utiliza para aclarar lesiones hiperpigmentadas como el melasma.

La queratosis seborreica es una proliferación epidérmica benigna con pigmentación variable. Mecanísticamente, la hidroquinona podría aclarar el pigmento de estas lesiones, pero el beneficio se limitaría a un efecto cosmético: no actúa sobre el crecimiento de los queratinocitos, que es la base de la lesión.

El único artículo vinculado es un estudio observacional prospectivo de tratamiento combinado en trastornos pigmentarios faciales; es evidencia indirecta y no evalúa específicamente la hidroquinona en la queratosis seborreica. El puntaje elevado de TxGNN es una predicción computacional que no está respaldada por datos clínicos directos.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para queratosis seborreica.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33046430](https://pubmed.ncbi.nlm.nih.gov/33046430/) | 2021 | Estudio de cohorte (observacional prospectivo) | J Plast Reconstr Aesthet Surg | Algoritmo de tratamiento combinado para trastornos pigmentarios faciales en pacientes asiáticos; la mayoría presenta varios trastornos a la vez. No evalúa la hidroquinona de forma específica en queratosis seborreica. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 63945 | NADONA 20 mg/g CREMA | Crema | No disponible |
| 63695 | SOLUMELAN 20 mg/g GEL | Gel | No disponible |
| 66899 | LICOFORTE 40 mg/g GEL | Gel | No disponible |
| 81390 | HQUIN 40 MG/G CREMA | Crema | No disponible |
| 63558 | LICOSTRATA 20 mg/g GEL | Gel | No disponible |

Hay 7 autorizaciones vigentes en total, todas de monofármaco; aquí se muestran las 5 principales.

---

## Consideraciones de Seguridad

- **Posibles enfermedades contraindicadas según el grafo de conocimiento** (relaciones fármaco-enfermedad de TxGNN, no texto del prospecto): quemadura solar, insuficiencia suprarrenal, enfermedad de Addison, atrofia cutánea, telangiectasia, enfermedad capilar, telangiectasia hemorrágica hereditaria, enfermedad vascular periférica, claudicación vascular intermitente, enfermedad arterial periférica, eccema atópico y dermatitis.
- **Interacciones farmacológicas**: no se encontraron interacciones registradas.
- Consideraciones adicionales señaladas en el análisis: el uso de hidroquinona durante el embarazo requiere precaución, y aplicar un agente potencialmente irritante sobre mucosa vulvar plantea preocupaciones de seguridad.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya en un puntaje computacional alto, pero solo hay un estudio observacional indirecto y ningún ensayo clínico. El beneficio, de existir, sería meramente cosmético y no tratamiento de la lesión subyacente.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), pues su ausencia impide el cribado de seguridad.
- Obtener datos del mecanismo de acción desde DrugBank.
- Evidencia clínica directa (estudios de hidroquinona tópica en queratosis seborreica).
- Evaluar si la lesión justifica un tratamiento despigmentante frente a las opciones habituales (observación, crioterapia, curetaje).
- Valorar los riesgos de seguridad frente a las contraindicaciones señaladas por el grafo de conocimiento.

---

### Otras indicaciones predichas (para referencia)

| Indicación | Puntaje TxGNN | Nivel | Observación |
|------|------|------|------|
| Queratosis folicular invertida vulvar | 0,9964 | L5 | Sin ensayos ni literatura; sin justificación mecanística clara y con preocupaciones de seguridad en mucosa vulvar. |
| Exantema | 0,9942 | L4 | Un ensayo de Fase 4 (NCT02138539) sobre un sistema despigmentante herbal, sin relación directa; sin mecanismo plausible. |
| Enfermedad liquenoide | 0,9907 | L4 | Solo una revisión y un caso clínico; la hidroquinona podría ayudar únicamente con la hiperpigmentación postinflamatoria, no con la inflamación subyacente. |
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

