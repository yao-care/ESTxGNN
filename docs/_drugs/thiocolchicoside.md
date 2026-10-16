---
layout: default
title: Thiocolchicoside
parent: Solo predicción del modelo (L5)
nav_order: 790
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Thiocolchicoside: nueva indicación predicha, Insomnio (nivel de evidencia L5). Indicación original: No disponible en los datos de la autorización"
monitor_inn: "thiocolchicoside"
predicted_indications: ["insomnia (disease)", "alcohol withdrawal delirium"]
---

# Thiocolchicoside
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

# Tiocolchicósido: De Indicación Original No Especificada a Insomnio

## Resumen en Una Frase

Tiocolchicósido es un derivado semisintético de la colchicósida con efecto miorrelajante, comercializado en España en comprimidos (ADALGUR 500 mg/2 mg). No se dispone de un texto de indicación aprobada en los datos compilados para este informe.
El modelo TxGNN predice que podría ser efectivo para **insomnio**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, y la plausibilidad farmacológica es cuestionable.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de la autorización |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99,89% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos de mecanismo de acción del registro original no están disponibles. Según la información farmacológica conocida, el tiocolchicósido es un derivado semisintético de la colchicósida con efecto miorrelajante. Actúa como antagonista competitivo de los receptores GABA-A y también inhibe los receptores de glicina.

La relación con el insomnio es indirecta: la modulación de GABA-A es central en la farmacología de los hipnóticos sedantes, lo que explica la conexión en el grafo de conocimiento. Sin embargo, el tiocolchicósido **antagoniza** el receptor GABA-A, la dirección opuesta a la de los hipnóticos clásicos (benzodiazepinas, fármacos Z), que lo potencian. Además, tiene actividad proconvulsivante a dosis altas.

Por tanto, el puntaje alto del modelo (99,89%) no está respaldado por la dirección farmacológica conocida. Al faltar los datos de mecanismo original, este vínculo no puede verificarse más.

### Segunda predicción: delirium por abstinencia alcohólica

El modelo también predice **delirium por abstinencia alcohólica** (puntaje 99,21%, nivel L5, decisión Hold). La abstinencia alcohólica implica una reducción de la inhibición GABAérgica y una hiperexcitabilidad glutamatérgica, y su tratamiento se basa en moduladores positivos de GABA-A. Dado que el tiocolchicósido es antagonista de GABA-A y proconvulsivante, podría **empeorar** el riesgo de convulsiones. Esto representa una preocupación de seguridad, no evidencia a favor.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 46534 | ADALGUR 500 mg/2 mg COMPRIMIDOS | Comprimido | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: no se encontraron interacciones registradas en la consulta realizada.
- **Riesgo derivado del mecanismo (según la evaluación farmacológica)**: actividad proconvulsivante a dosis altas por antagonismo de GABA-A. Esto es especialmente relevante en contextos de hiperexcitabilidad del SNC, como la abstinencia alcohólica.

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ambas predicciones son solo del modelo (L5), sin ensayos ni literatura, y el sentido del mecanismo conocido (antagonismo de GABA-A) es contrario al efecto terapéutico esperado en insomnio y abstinencia alcohólica. En esta última existe además un riesgo de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), actualmente un vacío bloqueante para el cribado de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Confirmar la indicación aprobada de la autorización 46534
- Realizar una revisión de literatura y estudios preclínicos que justifiquen cualquier efecto sobre el sueño
- Descartar el uso en abstinencia alcohólica salvo que nueva evidencia demuestre seguridad
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

