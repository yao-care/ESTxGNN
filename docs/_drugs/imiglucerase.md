---
layout: default
title: Imiglucerase
parent: Evidencia moderada (L3-L4)
nav_order: 408
evidence_level: L4
indication_count: 5
last_modified_at: 2026-10-14
description: "Imiglucerase: nueva indicación predicha, Síndrome de Hurler (nivel de evidencia L4). Indicación original: Enfermedad de Gaucher (según el grafo de conocimiento"
monitor_inn: "imiglucerase"
predicted_indications: ["Hurler syndrome", "Scheie syndrome", "benign neoplasm of adrenal gland", "autosomal ichthyosis syndrome with fatal disease course", "cholesteryl ester storage disease"]
---

# Imiglucerase
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **5** 
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

# Imiglucerasa: De Enfermedad de Gaucher a Síndrome de Hurler

## Resumen en Una Frase

Imiglucerasa es una enzima recombinante (glucocerebrosidasa) utilizada originalmente como terapia de reemplazo enzimático para la enfermedad de Gaucher.
El modelo TxGNN predice que podría ser efectivo para **Síndrome de Hurler**, pero actualmente no hay **ningún ensayo clínico** y solo hay **1 publicación** (una revisión general sobre terapias de reemplazo enzimático en enfermedades de depósito lisosomal) que respalda esta dirección de forma indirecta.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Gaucher (según el grafo de conocimiento; el texto de indicación de la autorización está vacío) |
| Nueva Indicación Predicha | Síndrome de Hurler |
| Puntaje de Predicción TxGNN | 99,52% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción detallado del fármaco. Según la información conocida, imiglucerasa es una glucocerebrosidasa (beta-glucosidasa) recombinante que hidroliza la glucosilceramida, sustrato que se acumula en la enfermedad de Gaucher.

El síndrome de Hurler (MPS I) está causado por la deficiencia de alfa-L-iduronidasa, lo que produce acumulación de glucosaminoglucanos (dermatán y heparán sulfato). Ambas enfermedades comparten el paradigma de depósito lisosomal y de tratamiento con reemplazo enzimático, pero la enzima y el sustrato son distintos.

Por ello, **la predicción no tiene un fundamento mecanístico directo**. El puntaje elevado probablemente refleja la proximidad en la red dentro de la clase de enfermedades de depósito lisosomal, y no un vínculo real a nivel de sustrato. Además, ya existe un tratamiento específico aprobado (laronidasa). Se ha descrito acumulación secundaria de glucoesfingolípidos en las MPS, pero eso no justifica el uso de imiglucerasa.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Revisión | La Revue de médecine interne | Revisión general de las terapias de reemplazo enzimático en enfermedades de depósito lisosomal (de la alglucerasa a la imiglucerasa en Gaucher, y agalsidasa en Fabry). No aporta datos específicos de imiglucerasa en síndrome de Hurler |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 97053003 | CEREZYME 400 UNIDADES POLVO PARA CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Concentrado para solución para perfusión | No disponible en el registro |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificó 1 interacción de nivel moderado con **miglustat** (fuente: DDInter).

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos y la única publicación es una revisión general sin datos específicos de imiglucerasa en síndrome de Hurler. El mecanismo no respalda la predicción (enzima y sustrato distintos) y ya existe una terapia enzimática específica aprobada (laronidasa).

**Para avanzar se necesita:**
- Datos del mecanismo de acción detallado y evidencia de un vínculo a nivel de sustrato con la MPS I
- Estudios preclínicos que demuestren algún efecto de imiglucerasa en modelos de MPS I
- Obtención y análisis del prospecto de la AEMPS (advertencias y contraindicaciones) para completar el cribado de seguridad
- Comparación con la terapia aprobada (laronidasa) que justifique un posible valor añadido

---

**Nota sobre otras predicciones:** las demás indicaciones predichas (síndrome de Scheie, neoplasia benigna de glándula suprarrenal, síndrome de ictiosis autosómica con curso fatal y enfermedad por depósito de ésteres de colesterol) tampoco cuentan con ensayos clínicos y tienen niveles de evidencia L4–L5, por lo que también se recomienda **Hold**.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

