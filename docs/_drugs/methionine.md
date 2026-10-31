---
layout: default
title: Methionine
parent: Solo predicción del modelo (L5)
nav_order: 511
evidence_level: L5
indication_count: 10
monitor_inn: "methionine"
predicted_indications: ["acne (disease)", "severe nonproliferative diabetic retinopathy", "craniostenosis cataract", "mature cataract", "diabetes mellitus type 2 associated cataract", "nuclear senile cataract", "cortical cataract", "tetanic cataract", "immature cataract", "diabetic cataract"]
last_modified_at: 2026-10-31
description: "Methionine: nueva indicación predicha, Acné (enfermedad) (nivel de evidencia L5). Indicación original: No disponible"
---

# Methionine
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

## Metionina: De Indicación Original no registrada a Acné (enfermedad)
{: .text-alpha }

## Resumen en Una Frase

Metionina es un aminoácido esencial azufrado; en España forma parte de medicamentos con varios principios activos (por ejemplo, soluciones de aminoácidos para nutrición parenteral), sin texto de indicación aprobada disponible para la metionina sola.
El modelo TxGNN predice que podría ser efectivo para **acné**, con **0 ensayos clínicos** y **2 publicaciones** que no estudian la metionina como tratamiento.
Por ello la predicción se considera solo computacional (nivel L5).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (la autorización registrada no incluye texto de indicación) |
| Nueva Indicación Predicha | Acné (enfermedad) |
| Puntaje de Predicción TxGNN | 1,0000 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 50 de 67) |
| Número de Autorizaciones | 67 (vigentes: 50) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la metionina es un aminoácido esencial que participa en el metabolismo del azufre y en la vía de la homocisteína, y en España solo consta en una pomada oftálmica combinada, hoy cancelada.

No hay apoyo mecanístico directo para la metionina en el acné. La literatura recuperada trata de niveles elevados de homocisteína en pacientes tratados con isotretinoína por acné quístico, lo que toca el metabolismo de metionina/homocisteína pero refleja un efecto secundario de otro fármaco, no una justificación terapéutica. El segundo artículo es un caso de mutación de MTHFR con encefalopatía neonatal que no guarda relación con el tratamiento del acné.

El puntaje de TxGNN es muy alto, pero es solo una predicción computacional. No hay estudios que evalúen la metionina en acné.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11277950](https://pubmed.ncbi.nlm.nih.gov/11277950/) | 2001 | Cohorte | Int J Dermatol | Aumento de homocisteína plasmática en pacientes con acné quístico tratados con isotretinoína; no evalúa la metionina como tratamiento |
| [39357918](https://pubmed.ncbi.nlm.nih.gov/39357918/) | 2024 | Reporte de caso | BMJ Case Reports | Neonato con mutación de MTHFR, encefalopatía, pérdida de cabello y acné neonatal; sin relación con tratamiento del acné |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 25908 | Pomada Oculos Epitelizante 3 mg/g + 5,5 mg/g + 5 mg/g (Laboratoires Thea), estado: cancelada | Pomada oftálmica | No consta texto de indicación |

La lista puede considerarse completa (1 autorización). Es un producto de combinación, por lo que no describe la situación regulatoria de la metionina como principio activo único.

## Consideraciones de Seguridad

- **Relaciones de contraindicación registradas en el grafo de conocimiento** (no proceden del prospecto): hipertensión, enfermedad renal (incluida enfermedad renal crónica y terminal), nefrolitiasis, nefrocalcinosis, hipercalcemia, sarcoidosis, diabetes mellitus, cetoacidosis diabética, enfermedad cardíaca y cardiovascular, hiperlipidemia (incluida la familiar), nefropatía aguda por uratos, intoxicación digitálica, fibrilación ventricular, fenilcetonuria y otros trastornos del metabolismo de la fenilalanina.
- **Interacciones farmacológicas** (5 registradas):
  - Carbón activado: moderada.
  - Efedrina, pseudoefedrina, mexiletina y flecainida: leves.
- Un posible problema de seguridad es el aumento de homocisteína por carga de metionina.

Para información de seguridad basada en el prospecto, consultar la ficha técnica.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para acné se basa solo en el modelo: no hay ensayos ni estudios que evalúen la metionina en esta enfermedad, y la literatura disponible es tangencial. Además, la única autorización en España está cancelada.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de la metionina y una hipótesis plausible para el acné.
- Estudios preclínicos o de mecanismo que evalúen directamente la metionina en acné.
- Revisión del prospecto (advertencias y contraindicaciones) y evaluación del riesgo de hiperhomocisteinemia.
- Aclarar la indicación original y la situación regulatoria actual de la metionina en España.

**Nota sobre otras predicciones:** entre las demás indicaciones predichas (retinopatía diabética no proliferativa grave y varios tipos de catarata), la catarata diabética es la que cuenta con la evidencia indirecta más relevante, pero se trata de estudios in vitro u observacionales que no prueban la metionina como tratamiento. Debería plantearse solo como pregunta de investigación mecanística o preclínica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

