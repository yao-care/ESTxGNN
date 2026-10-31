---
layout: default
title: Finasteride
parent: Solo predicción del modelo (L5)
nav_order: 337
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-31
monitor_inn: "Finasteride"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly"]
description: "Finasteride: nueva indicación predicha, Ambras type hypertrichosis universalis congenita (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Finasteride
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Finasteride: Ambras type hypertrichosis universalis congenita
{: .text-alpha }

## Resumen en Una Frase

Finasterida es un inhibidor de la 5-alfa-reductasa tipo II, utilizado originalmente para el tratamiento de la hiperplasia prostática benigna.
El modelo TxGNN predice que podría ser efectivo para **hipertricosis**, aunque la evidencia es muy limitada: **0 ensayos clínicos** y **4 publicaciones** indirectas (revisiones narrativas y un artículo metodológico) respaldan esta dirección.

*Nota: la predicción con mayor puntaje del modelo es "hipertricosis universalis congénita tipo Ambras" (0,9999), pero carece de cualquier evidencia. Se presenta la segunda predicción, la hipertricosis, por ser la que cuenta con alguna literatura relacionada, y se comenta la primera en el apartado de mecanismo.*

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Ambras type hypertrichosis universalis congenita |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 (hipertricosis); L5 (Ambras) |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 9) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, finasterida inhibe la 5-alfa-reductasa tipo II (gen SRD5A2), enzima que convierte la testosterona en dihidrotestosterona (DHT). Su eficacia en la hiperplasia prostática benigna está comprobada y se emplea también en la alopecia androgenética masculina.

La relación con la nueva indicación es solo parcial. La supresión de DHT tiene fundamento en trastornos del cabello dependientes de andrógenos, como el hirsutismo y la alopecia androgenética. Sin embargo, la hipertricosis es típicamente independiente de andrógenos (congénita, inducida por fármacos o paraneoplásica), por lo que el ajuste mecanístico es limitado.

Para la predicción de mayor puntaje (síndrome de Ambras), la conexión es aún más débil: se asocia a reordenamientos genómicos que afectan la regulación de TRPS1 y no es principalmente androgénica. El puntaje elevado proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni un mecanismo plausible demostrado. Además, la finasterida está contraindicada en el embarazo por el riesgo de anomalías genitales en fetos masculinos, lo que limita cualquier uso en cuadros congénitos o pediátricos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [12223963](https://pubmed.ncbi.nlm.nih.gov/12223963/) | 2002 | Revisión | Annales de dermatologie et de vénéréologie | Distingue hipertricosis (zonas no dependientes de andrógenos) de hirsutismo; en adultos suele ser iatrogénica, metabólica, nutricional o paraneoplásica |
| [10330884](https://pubmed.ncbi.nlm.nih.gov/10330884/) | 1999 | Revisión | Therapeutische Umschau | Revisa opciones terapéuticas para alopecia androgenética e hirsutismo; no aporta datos de finasterida en hipertricosis |
| [12942187](https://pubmed.ncbi.nlm.nih.gov/12942187/) | 2003 | Revisión | Der Hautarzt | Menciona finasterida para la alopecia masculina y láser para hipertricosis e hirsutismo |
| [12444520](https://pubmed.ncbi.nlm.nih.gov/12444520/) | 2002 | Artículo metodológico | Der Hautarzt | Describe TrichoScan, herramienta de análisis digital del cabello; no es un estudio de eficacia |

Ninguna publicación es un estudio controlado de finasterida en hipertricosis; la evidencia es indirecta.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 71064 | Finasterida Normon 1 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos |
| 68168 | Finasterida Tecnigen 5 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos |
| 76704 | Finasterida Cinfa 1 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos |
| 74134 | Capikern 1 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos |
| 86827 | Alocare 2,275 mg/ml solución para pulverización cutánea | Solución para pulverización cutánea | No disponible en los datos |

Existen 20 autorizaciones vigentes, todas de medicamentos de un solo principio activo. Se observan presentaciones de 1 mg y de 5 mg, además de una formulación tópica (Alocare, solución cutánea).

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no el prospecto)**: enfermedad hepática y enfermedad de la vesícula biliar.
- **Interacciones Farmacológicas**: la consulta no identificó interacciones con otros fármacos; solo consta la diana farmacológica, la esteroide 5-alfa-reductasa tipo 2 (SRD5A2).
- **Embarazo**: la finasterida conlleva riesgo de anomalías genitales externas en fetos masculinos.

Consultar el prospecto para el resto de la información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Las predicciones tienen puntajes muy altos, pero provienen solo del modelo TxGNN (aprendizaje profundo) y pueden reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. Para hipertricosis la evidencia es indirecta (revisiones narrativas antiguas, nivel L4) y para las demás indicaciones no existe ninguna (L5). Además, el mecanismo androgénico no es plausible en cuadros mayoritariamente independientes de andrógenos.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y análisis mecanístico formal frente a la hipertricosis
- Advertencias y contraindicaciones del prospecto de la AEMPS
- Revisión de la literatura específica sobre finasterida en hipertricosis y trastornos del tallo piloso (casos, series o estudios controlados)
- Evaluación de la compatibilidad de vías de administración (oral vs. tópica)
- Evaluación de seguridad en poblaciones específicas (embarazo, mujeres en edad fértil, población pediátrica)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

