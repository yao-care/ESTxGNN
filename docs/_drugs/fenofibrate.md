---
layout: default
title: Fenofibrate
parent: Solo predicción del modelo (L5)
nav_order: 330
evidence_level: L5
indication_count: 1
monitor_inn: "Fenofibrate"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-10-29
description: "Fenofibrate: nueva indicación predicha, Deficiencia de la proteína de transferencia de ésteres de colesterol (cholesterol-ester transfer protein deficiency) (nivel de evidencia L5). Indicación origin…"
---

# Fenofibrate
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

## Fenofibrate: Deficiencia de la proteína de transferencia de ésteres de colesterol (cholesterol-ester transfer protein deficiency)
{: .text-alpha }

## Resumen en Una Frase

Fenofibrato es un fármaco hipolipemiante asociado con hipertrigliceridemia e hiperlipidemias familiares.
El modelo TxGNN predice que podría ser efectivo para la **deficiencia de la proteína de transferencia de ésteres de colesterol (CETP)**.
Actualmente no hay ensayos clínicos y solo **3 publicaciones** preclínicas o mecanísticas, ninguna de las cuales estudia directamente esta enfermedad.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Deficiencia de la proteína de transferencia de ésteres de colesterol (cholesterol-ester transfer protein deficiency) |
| Puntaje de Predicción TxGNN | 0.9961 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 14 de 15) |
| Número de Autorizaciones | 15 (vigentes: 14) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información farmacológica conocida, el fenofibrato es un agonista del receptor PPAR-alfa (la actividad reside en su metabolito activo). Esto modifica el metabolismo de los lípidos: reduce triglicéridos y colesterol circulantes y aumenta el HDL, en parte mediante la inducción del gen de la proteína de transferencia de fosfolípidos (PLTP).

La deficiencia de CETP es una condición genética caracterizada por HDL muy elevado y actividad reducida de CETP. La relación con el fenofibrato es solo indirecta: ambos actúan sobre la misma vía de metabolismo de HDL y transferencia de lípidos. Sin embargo, aumentar el HDL en una condición que ya presenta HDL muy alto no tiene una justificación terapéutica clara.

El puntaje alto de TxGNN probablemente refleja la proximidad en la red entre la agonía de PPAR-alfa, el metabolismo lipídico y los genes relacionados con CETP, y no evidencia de beneficio clínico. Un estudio en ratones combina inhibición farmacológica de CETP con agonismo PPAR-alfa, lo que apoya una interacción entre vías, pero no aborda el estado de deficiencia genética.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [20332533](https://pubmed.ncbi.nlm.nih.gov/20332533/) | 2010 | Preclínico (ratones transgénicos) | J Cardiovasc Pharmacol Ther | La inhibición de CETP (torcetrapib) y el agonismo PPAR-alfa (fenofibrato) modifican los perfiles de HDL y LDL en ratones con ApoB100/CETP humanos |
| [11342537](https://pubmed.ncbi.nlm.nih.gov/11342537/) | 2001 | Preclínico (mecanístico) | J Biol Chem | La inducción del gen PLTP explica el agrandamiento de HDL en ratones tratados con fenofibrato |
| [30271349](https://pubmed.ncbi.nlm.nih.gov/30271349/) | 2018 | Preclínico (mecanístico) | Front Physiol | Falta de correlación entre HDL plasmático, colesterol fecal y capacidad de eflujo de colesterol; subraya la importancia de la función del HDL |

## Información de Mercado en España

La lista incluye 5 de las 15 autorizaciones; los textos de indicación aprobada no están disponibles en los registros locales.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 69367 | Fenofibrato Sun 160 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en el registro |
| 63533 | Secalip Supra 160 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en el registro |
| 72705 | Fenofibrato Teva 200 mg cápsulas duras EFG | Cápsula dura | No disponible en el registro |
| 79122 | Fenofibrato Kern Pharma 145 mg comprimidos EFG | Comprimido | No disponible en el registro |
| 60176 | Secalip 200 mg cápsulas | Cápsula dura | No disponible en el registro |

## Consideraciones de Seguridad

- **Contraindicaciones o enfermedades de riesgo recogidas en el grafo de conocimiento** (no proceden del texto del prospecto): insuficiencia y enfermedad hepática, pancreatitis, enfermedad de la vesícula biliar y colelitiasis, miopatía y rabdomiólisis, insuficiencia renal, y alteraciones hematológicas (trombocitopenia, anemia, leucopenia, agranulocitosis y neutropenia).
- **Interacciones farmacológicas**: no se identificaron interacciones con otros fármacos. Los datos farmacológicos solo confirman como diana el receptor PPAR-alfa humano y la proteína de unión a ácidos grasos 1 (en rata).

Consultar el prospecto para la información de seguridad oficial.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ningún estudio citado aborda directamente la deficiencia de CETP; solo hay datos preclínicos de vías relacionadas. Además, no hay un fundamento terapéutico claro para elevar el HDL en una enfermedad que ya cursa con HDL elevado.

**Para avanzar se necesita:**
- Una justificación clínica que identifique un beneficio posible en la deficiencia de CETP
- Estudios o series de casos que evalúen directamente fenofibrato en esta condición
- Datos de mecanismo de acción detallados
- Advertencias y contraindicaciones oficiales de los prospectos de la AEMPS
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

