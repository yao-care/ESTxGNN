---
layout: default
title: Hydroxocobalamin
parent: Solo predicción del modelo (L5)
nav_order: 398
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Hydroxocobalamin: nueva indicación predicha, Várices esofágicas con sangrado (nivel de evidencia L5). Indicación original: Deficiencia de vitamina B12 (según el grafo de conocimiento"
---

# Hydroxocobalamin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Hidroxocobalamina: De Deficiencia de Vitamina B12 a Várices Esofágicas con Sangrado

## Resumen en Una Frase

La hidroxocobalamina es una forma de vitamina B12, utilizada originalmente para tratar la deficiencia de vitamina B12, la anemia perniciosa y la intoxicación por cianuro.
El modelo TxGNN predice que podría ser efectiva para **várices esofágicas con sangrado**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Deficiencia de vitamina B12 (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Várices esofágicas con sangrado |
| Puntaje de Predicción TxGNN | 99.23% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la hidroxocobalamina es una forma inyectable de vitamina B12 cuya eficacia en la deficiencia de B12, la anemia perniciosa y (en su presentación de perfusión) la intoxicación por cianuro es conocida. Con los datos compilados, no es posible establecer un vínculo mecanístico con las várices esofágicas.

La puntuación del modelo (99.23%) es idéntica para las várices con y sin sangrado. Esto sugiere una señal compartida del grafo de conocimiento más que evidencia específica de la indicación.

Existe una hipótesis especulativa basada en farmacología general: la hidroxocobalamina puede unirse al óxido nítrico (NO), un mediador de la vasodilatación esplácnica en la hipertensión portal. Esta hipótesis no procede de los datos compilados y no está validada. El manejo actual de la hemorragia varicosa aguda se basa en fármacos vasoactivos, ligadura endoscópica con bandas y antibióticos, sin papel establecido para la vitamina B12.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 46090 | Megamilbedoce 5.000 microgramos/ml solución inyectable | Solución inyectable | No disponible en los datos compilados |
| 07420001 | Cyanokit 2,5 g polvo para solución para perfusión | Polvo para solución para perfusión | No disponible en los datos compilados |
| 88743 | Hidroxocobalamina Basi 1 mg/ml solución inyectable | Solución inyectable | No disponible en los datos compilados |
| 07420002 | Cyanokit 5 g polvo para solución para perfusión | Polvo para solución para perfusión | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proviene del prospecto): trastorno hipertensivo e hipertensión. Es relevante revisarlo, ya que la hipertensión portal y la situación hemodinámica del paciente con várices requerirían una valoración cuidadosa.
- **Interacciones Farmacológicas**: se identificaron 32 interacciones en total. Las de nivel moderado incluyen trióxido de arsénico, cloranfenicol, yoduro I-131 y yoduro I-123. Otras con nivel no clasificado incluyen omeprazol, lansoprazol, simvastatina, loperamida, prednisolona, ranitidina, ácido acetilsalicílico, budesonida, ácido fólico, valsartán, ramipril, lorazepam, citalopram, paracetamol, mirtazapina y levotiroxina.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo, sin ensayos clínicos, literatura ni vínculo mecanístico demostrado. Además, falta la información de seguridad del prospecto, lo que impide avanzar al cribado de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones).
- Completar los datos del mecanismo de acción desde DrugBank.
- Revisar sistemáticamente la literatura preclínica y clínica sobre vitamina B12/captación de óxido nítrico en hipertensión portal.
- Evaluar la compatibilidad de la vía de administración y la relevancia de la contraindicación por hipertensión señalada en el grafo.
- Valorar si existe justificación para un estudio preclínico antes de cualquier ensayo clínico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

