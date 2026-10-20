---
layout: default
title: Epinastine
parent: Solo predicción del modelo (L5)
nav_order: 295
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Epinastine: nueva indicación predicha, Conjuntivitis rosácea (nivel de evidencia L5). Indicación original: Conjuntivitis atópica…"
monitor_inn: "Epinastine"
predicted_indications: ["rosacea conjunctivitis", "allergic urticaria"]
---

# Epinastine
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

# Epinastina: De Conjuntivitis Atópica a Conjuntivitis Rosácea

## Resumen en Una Frase

Epinastina es un antihistamínico antagonista del receptor H1, utilizado originalmente en el tratamiento de la conjuntivitis alérgica (atópica, papilar y vernal).
El modelo TxGNN predice que podría ser efectivo para **conjuntivitis rosácea**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección específica; se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Conjuntivitis atópica, papilar y vernal (según el grafo de conocimiento; la ficha de AEMPS no incluye texto de indicación) |
| Nueva Indicación Predicha | Conjuntivitis rosácea |
| Puntaje de Predicción TxGNN | 99,57% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Epinastina es un antagonista tópico del receptor H1 de histamina con actividad estabilizadora de mastocitos. Ya está comercializada en forma de colirio para conjuntivitis alérgica, vernal y papilar. Actualmente no se dispone de datos detallados sobre el mecanismo de acción dentro de los datos compilados para este informe, pero la farmacología conocida del fármaco apunta a la inhibición de la histamina y de la liberación de mediadores desde los mastocitos.

La conjuntivitis rosácea (rosácea ocular) se debe principalmente a disfunción de las glándulas de Meibomio, inflamación del borde palpebral y factores microbianos o de *Demodex*, más que a una alergia clásica mediada por IgE. Por ello, el mecanismo antihistamínico y de estabilización de mastocitos ofrece solo un vínculo plausible y parcial, probablemente limitado al componente inflamatorio o al picor asociado.

El puntaje tan alto del modelo (99,57%) probablemente refleja la proximidad en la red de conocimiento con otras indicaciones de conjuntivitis, y no está respaldado por evidencia clínica ni bibliográfica. Debe interpretarse con cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 65574 | RELESTAT 0,5 mg/ml colirio en solución (Abbvie Spain, S.L.U.) | Colirio en solución | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: la consulta se completó sin interacciones fármaco-fármaco clínicamente catalogadas. Solo consta el dato farmacológico de que epinastina actúa sobre el receptor H1 (gen HRH1) en humanos.

Consultar el prospecto para el resto de la información de seguridad (advertencias y contraindicaciones).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y el mecanismo antihistamínico solo explica parcialmente la fisiopatología de la rosácea ocular, que es principalmente de origen meibomiano e inflamatorio.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA).
- Revisión sistemática de la literatura sobre antihistamínicos tópicos o estabilizadores de mastocitos en rosácea ocular.
- Obtener y analizar el prospecto de AEMPS (advertencias, contraindicaciones e indicación autorizada).
- Evaluación de la compatibilidad de vía de administración y de la similitud con la indicación original.
- Estudios preclínicos o piloto que justifiquen un ensayo clínico exploratorio.

---

### Nota sobre la segunda predicción (urticaria alérgica)

El segundo candidato, **urticaria alérgica** (puntaje TxGNN 99,28%), tiene una evidencia indirecta algo mayor (nivel L4, recomendación "Research Question"). La literatura disponible consiste en revisiones y estudios farmacodinámicos de supresión de roncha y eritema inducidos por histamina (por ejemplo, un ensayo cruzado doble ciego en voluntarios sanos, PMID [10442525](https://pubmed.ncbi.nlm.nih.gov/10442525/)), pero no hay ensayos clínicos registrados ni un ECA específico en urticaria. Además, la autorización española corresponde únicamente a un colirio oftálmico, por lo que habría que verificar la formulación oral y su estado regulatorio antes de cualquier decisión.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

