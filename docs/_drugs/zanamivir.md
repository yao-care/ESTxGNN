---
layout: default
title: Zanamivir
parent: Solo predicción del modelo (L5)
nav_order: 863
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Zanamivir: nueva indicación predicha, Pielonefritis (nivel de evidencia L5). Indicación original: Gripe (influenza)"
monitor_inn: "ZANAMIVIR"
predicted_indications: ["pyelonephritis", "disorder of tyrosine metabolism"]
---

# Zanamivir
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

# Zanamivir: De Gripe a Pielonefritis

## Resumen en Una Frase

Zanamivir es un inhibidor de la neuraminidasa viral, utilizado originalmente para el tratamiento de la gripe (influenza).
El modelo TxGNN predice que podría ser efectivo para **pielonefritis**, pero no existe ningún ensayo clínico ni publicación que respalde esta dirección (**0 ensayos clínicos** y **0 publicaciones**), por lo que la predicción debe considerarse con mucha cautela.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Gripe (influenza) |
| Nueva Indicación Predicha | Pielonefritis |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, zanamivir es un inhibidor de la neuraminidasa viral con actividad frente a los virus de la gripe A y B, y su uso está establecido en la gripe (por vía inhalada o intravenosa).

Sin embargo, el análisis no identifica un vínculo mecanístico creíble con la pielonefritis. Esta es una infección del riñón de origen predominantemente bacteriano (habitualmente *E. coli*), por lo que un antiviral inhibidor de la neuraminidasa no tiene una diana o vía de acción establecida en este contexto.

El puntaje TxGNN es muy alto (99.84%), pero es únicamente una predicción del grafo de conocimiento, sin respaldo de ensayos ni literatura. Probablemente refleja proximidad en la red a través de nodos genéricos relacionados con infecciones, por lo que debe tratarse como un probable falso positivo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para pielonefritis.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1181349001 | DECTOVA 10 mg/ml solución para perfusión | Solución para perfusión | No disponible en los datos compilados |
| 62712 | RELENZA 5 mg/dosis polvo para inhalación (unidosis) | Polvo para inhalación | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Enfermedades con contraindicación según el grafo de conocimiento** (no proviene del texto del prospecto): epilepsia, enfermedad pulmonar obstructiva crónica (EPOC), EPOC grave de inicio temprano, enfermedad bronquial y delirio.
- **Interacciones Farmacológicas**: se identificaron 8 interacciones potenciales.
  - Insulina humana (inhalada, de acción rápida): nivel **moderado**.
  - Claritromicina, loratadina, montelukast, ketotifeno, fexofenadina, ibuprofeno y diclofenaco: nivel de gravedad no determinado.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura que la respalden, y no existe un vínculo mecanístico plausible entre un antiviral inhibidor de la neuraminidasa y una infección renal bacteriana. Se considera un probable falso positivo.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) del fármaco.
- Evidencia preclínica o clínica que sustente una actividad en pielonefritis (actualmente inexistente).
- Texto de indicaciones, advertencias y contraindicaciones del prospecto de la AEMPS, para completar la evaluación de seguridad.
- Análisis de compatibilidad de vía de administración y exposición sistémica/renal.

---

**Nota sobre la segunda predicción (trastorno del metabolismo de la tirosina; puntaje TxGNN 99.02%, nivel L5, decisión Hold):** no se identifica ningún vínculo mecanístico, ya que zanamivir no interactúa con las enzimas del catabolismo de la tirosina. Las tres publicaciones recuperadas tratan sobre resistencia antiviral y la neuraminidasa de la gripe, sin relación con esta indicación; probablemente aparecieron por la notación de mutaciones con aminoácidos (por ejemplo, H274Y, N294S). No aportan evidencia clínica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

