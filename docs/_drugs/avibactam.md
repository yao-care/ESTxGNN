---
layout: default
title: Avibactam
parent: Solo predicción del modelo (L5)
nav_order: 81
evidence_level: L5
indication_count: 4
monitor_inn: "avibactam"
predicted_indications: ["ureter tuberculosis", "urinary schistosomiasis", "polyclonal hyperviscosity syndrome", "hyperamylasemia"]
last_modified_at: 2026-10-23
description: "Avibactam: nueva indicación predicha, Tuberculosis del uréter (nivel de evidencia L5). Indicación original: Pielonefritis"
---

# Avibactam
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

## Avibactam: De Pielonefritis a Tuberculosis del Uréter
{: .text-alpha }

## Resumen en Una Frase

Avibactam es un inhibidor de beta-lactamasas que no es un antibiótico por sí mismo; se comercializa en combinación con otros antibióticos beta-lactámicos y su indicación original es la pielonefritis.
El modelo TxGNN predice que podría ser efectivo para **tuberculosis del uréter**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.
Se trata, por tanto, de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Pielonefritis (relación registrada en el grafo de conocimiento; los textos de indicación de las autorizaciones locales no están disponibles) |
| Nueva Indicación Predicha | Tuberculosis del uréter |
| Puntaje de Predicción TxGNN | 0,9911 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 2 de 2) |
| Número de Autorizaciones | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento general, avibactam es un inhibidor de beta-lactamasas no beta-lactámico que carece de actividad antibacteriana relevante por sí solo y se administra junto a un antibiótico beta-lactámico para protegerlo de la degradación enzimática.

La relación con la nueva indicación es plausible pero indirecta. Algunos datos sugieren que avibactam puede inhibir la beta-lactamasa BlaC de *Mycobacterium tuberculosis*, lo que en principio podría restaurar la actividad de ciertos beta-lactámicos. La tuberculosis genitourinaria es una manifestación localizada de la misma infección. Este razonamiento es solo preclínico y no está respaldado por estudios incluidos en los datos compilados.

Aunque el puntaje del modelo TxGNN (aprendizaje profundo) es alto (0,9911), no existe ningún estudio que evalúe directamente esta enfermedad, por lo que la predicción debe considerarse una hipótesis.

### Otras predicciones del modelo (de menor interés)

| Enfermedad predicha | Puntaje TxGNN | Valoración |
|------|------|------|
| Esquistosomiasis urinaria | 0,9906 | Vínculo mecanístico débil; la inhibición de beta-lactamasas no tiene un mecanismo establecido frente a helmintos. Probablemente refleja proximidad en la red con enfermedades del tracto urinario. |
| Síndrome de hiperviscosidad policlonal | 0,9901 | Sin vínculo mecanístico plausible; el puntaje proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. |
| Hiperamilasemia | 0,9901 | Es un hallazgo de laboratorio, no una enfermedad tratable con este mecanismo; probable artefacto de la predicción. |

Todas ellas tienen nivel de evidencia L5 y recomendación Hold.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1161109001 | ZAVICEFTA 2 G/0,5 G | Polvo para concentrado para solución para perfusión | No disponible en los datos compilados |
| 1241808001 | EMBLAVEO 1,5 G/0,5 G | Polvo para concentrado para solución para perfusión | No disponible en los datos compilados |

Ambas autorizaciones están vigentes. Corresponden a productos con avibactam en combinación con otros principios activos, por lo que no deben interpretarse como autorizaciones del avibactam como principio activo único.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

No se encontraron interacciones farmacológicas registradas en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo, sin ensayos clínicos ni publicaciones que estudien directamente la tuberculosis del uréter, por lo que el nivel de evidencia es L5. El vínculo mecanístico es solo preclínico, y los datos de seguridad y de mecanismo de acción están incompletos.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), que es un requisito bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Estudios preclínicos que evalúen la inhibición de BlaC de *M. tuberculosis* y la actividad en combinación con beta-lactámicos.
- Revisión sistemática de la literatura sobre inhibidores de beta-lactamasas en tuberculosis, incluida la genitourinaria.
- Evaluar la compatibilidad de vía de administración y la similitud con la indicación original, actualmente pendientes.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

