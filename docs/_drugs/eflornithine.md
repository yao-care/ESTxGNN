---
layout: default
title: Eflornithine
parent: Solo predicción del modelo (L5)
nav_order: 277
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Eflornithine: nueva indicación predicha, Esotropía (nivel de evidencia L5). Indicación original: Tripanosomiasis africana humana (según el grafo de conocimiento"
monitor_inn: "eflornithine"
predicted_indications: ["esotropia", "neurotrophic keratopathy"]
---

# Eflornithine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Eflornitina: De Tripanosomiasis Africana Humana a Esotropía

## Resumen en Una Frase

Eflornitina es un inhibidor irreversible de la ornitina descarboxilasa, utilizado originalmente para la tripanosomiasis africana humana (enfermedad del sueño) y, en forma tópica, para el hirsutismo facial.
El modelo TxGNN predice que podría ser efectiva para **esotropía**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tripanosomiasis africana humana (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Esotropía |
| Puntaje de Predicción TxGNN | 99,85% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

La eflornitina inhibe de forma irreversible la ornitina descarboxilasa (ODC, gen *ODC1*), enzima limitante de la biosíntesis de poliaminas. Esta acción explica su uso en la tripanosomiasis africana y en el hirsutismo facial (crema tópica). Los datos compilados indican además usos recientes en neuroblastoma de alto riesgo (autorización de la FDA en diciembre de 2023) y una designación huérfana de la EMA en glioma (2016). No se dispone de datos más detallados del mecanismo de acción en los datos compilados para este informe.

La relación entre la indicación original y la esotropía es débil. La esotropía es un trastorno de la alineación ocular causado por factores neuromusculares, refractivos o de visión binocular, y no existe una vía mecanística establecida que conecte la inhibición de la ODC o la depleción de poliaminas con su fisiopatología.

El puntaje tan alto de TxGNN (0,9985) es solo una predicción del modelo, sin ensayos ni literatura de apoyo. El vínculo probablemente sea un artefacto del grafo de conocimiento y no debe considerarse validado biológicamente.

Como referencia, la segunda predicción, **queratopatía neurotrófica** (puntaje 99,38%), tiene una plausibilidad conceptual algo mayor, ya que las poliaminas participan en la proliferación celular y la reparación tisular. Sin embargo, esta enfermedad se debe a una inervación corneal deficiente y pérdida de soporte trófico (p. ej., señalización de NGF), por lo que la depleción de poliaminas probablemente perjudicaría la regeneración epitelial. La dirección del efecto es incierta y tampoco hay evidencia que la respalde (nivel L5, Hold).

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 01173002 | VANIQA 11,5 % CREMA (Almirall S.A.) | Crema | No disponible |
| 01173003 | VANIQA 11,5 % CREMA (Almirall S.A.) | Crema | No disponible |
| 01173001 | VANIQA 11,5 % CREMA (Almirall S.A.) | Crema | No disponible |

Las tres autorizaciones son de medicamentos de un solo principio activo y están vigentes. Todas corresponden a una formulación tópica (crema).

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): exantema y dermatitis.
- **Interacciones farmacológicas**: la consulta se completó y devolvió un único registro, que describe la farmacología del fármaco (diana: ornitina descarboxilasa humana, *ODC1*) y no una interacción con otro medicamento. No se identificaron interacciones clínicas con nivel de gravedad asignado.

Para el resto de la información de seguridad (advertencias y contraindicaciones oficiales), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para esotropía es solo del modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible; probablemente sea un artefacto del grafo de conocimiento. Además, las advertencias y contraindicaciones del prospecto no están disponibles, lo que impide avanzar al cribado de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), que es un bloqueo para la evaluación de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Establecer una hipótesis biológica plausible que vincule la inhibición de la ODC con la esotropía, apoyada por estudios preclínicos.
- Evaluar la compatibilidad de vía de administración (la presentación actual es crema tópica, y está pendiente determinar la vía necesaria para uso oftalmológico).
- Revisar la literatura y los registros de ensayos para detectar cualquier evidencia directa; si no existe, valorar la queratopatía neurotrófica solo tras aclarar la dirección del efecto.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

