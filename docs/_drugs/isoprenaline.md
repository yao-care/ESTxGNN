---
layout: default
title: Isoprenaline
parent: Solo predicción del modelo (L5)
nav_order: 433
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
monitor_inn: "Isoprenaline"
predicted_indications: ["nasal cavity disease", "headache disorder", "pharyngitis", "acute laryngopharyngitis", "trigeminal autonomic cephalalgia", "bronchial disease", "endobronchial leiomyoma", "allergic urticaria", "endobronchial lipoma", "bronchus adenoma"]
description: "Isoprenaline: nueva indicación predicha, Enfermedad de la cavidad nasal (nasal cavity disease) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Isoprenaline
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

## Isoprenaline: Enfermedad de la cavidad nasal (nasal cavity disease)
{: .text-alpha }

## Resumen en Una Frase

Isoprenalina es un agonista beta-adrenérgico no selectivo, originalmente utilizado en el tratamiento del resfriado común, la nasofaringitis, la parada cardíaca y el bloqueo auriculoventricular.
El modelo TxGNN predice que podría ser efectivo para **enfermedad de la cavidad nasal**,
pero actualmente **no hay ensayos clínicos** y solo **1 publicación** (un reporte de caso no relacionado terapéuticamente) respalda esta dirección: es una predicción basada únicamente en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Enfermedad de la cavidad nasal (nasal cavity disease) |
| Puntaje de Predicción TxGNN | 0.9995 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 2 de 2) |
| Número de Autorizaciones | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Según la información conocida, la isoprenalina es un agonista beta-adrenérgico no selectivo que activa los receptores β1, β2 y β3, con aumento del AMP cíclico. Sus efectos clásicos son cardioestimulación (β1) y broncodilatación/vasodilatación (β2).

La relación con la nueva indicación es débil. Un efecto descongestionante o sobre la mucosa mediado por receptores beta es concebible, pero no hay datos que lo respalden. La única publicación recuperada trata de taquicardia ventricular perioperatoria y espasmo coronario, y no tiene relación con la enfermedad nasal. El puntaje alto proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

Por tanto, esta predicción debe considerarse una hipótesis del modelo, sin una justificación mecanística sólida.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [14711196](https://pubmed.ncbi.nlm.nih.gov/14711196/) | 2003 | Reporte de caso | Japanese Heart Journal | Varón japonés de 26 años con taquicardia ventricular perioperatoria tras la instilación nasal de epinefrina; se halló espasmo coronario. No aporta evidencia terapéutica sobre enfermedad nasal. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 89777 | LABRYCOR 0,2 mg/ml concentrado para solución para perfusión EFG | Concentrado para solución para perfusión | No disponible |
| 47131 | ALEUDRINA 0,2 mg/ml solución inyectable | Solución inyectable | No disponible |

## Consideraciones de Seguridad

- **Enfermedades con contraindicación según el grafo de conocimiento** (no proviene del texto del prospecto): hipertensión, diabetes mellitus, cetoacidosis diabética, enfermedad coronaria, infarto de miocardio, trombosis coronaria, hemoglobinopatía, hipertiroidismo, enfermedad de Graves y tirotoxicosis.
- **Farmacología**: actúa sobre los receptores β1 (ADRB1), β2 (ADRB2) y β3 (ADRB3) humanos. No se identificaron interacciones con otros fármacos.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para enfermedad de la cavidad nasal se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura terapéutica pertinente. Además, los antecedentes cardiovasculares y metabólicos de contraindicación y las formas farmacéuticas disponibles en España (perfusión e inyectable) no son adecuadas para un uso nasal.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y un fundamento biológico específico para la mucosa nasal.
- Revisión sistemática de literatura preclínica o clínica sobre isoprenalina y enfermedad nasal.
- Evaluación de la compatibilidad de la vía de administración (formulación nasal o tópica) frente a las presentaciones actuales.
- Extracción de las advertencias, contraindicaciones e indicaciones aprobadas de los prospectos de la AEMPS.

**Nota sobre otras predicciones:** entre las demás indicaciones predichas, **enfermedad bronquial** (puntaje 0.9977, nivel L4) es la que cuenta con más respaldo, con 19 publicaciones, principalmente revisiones de la clase de agonistas β2 y estudios históricos de isoprenalina en asma. Se trata más de un uso histórico ya establecido que de un reposicionamiento novedoso, y la evidencia es indirecta. Esta alternativa merece una evaluación específica por separado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

