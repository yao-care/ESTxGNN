---
layout: default
title: Epinastine
parent: Solo predicción del modelo (L5)
nav_order: 295
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "Epinastine"
predicted_indications: ["rosacea conjunctivitis", "allergic urticaria"]
description: "Epinastine: nueva indicación predicha, Conjuntivitis rosácea (rosacea conjunctivitis) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 1 (comercializadas: 0)"
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

## Epinastine: Conjuntivitis rosácea (rosacea conjunctivitis)
{: .text-alpha }

## Resumen en Una Frase

Epinastina es un antihistamínico antagonista del receptor H1, utilizado originalmente en el tratamiento de la conjuntivitis alérgica (atópica, papilar y vernal).
El modelo TxGNN predice que podría ser efectivo para **conjuntivitis rosácea**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección específica; se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Conjuntivitis rosácea (rosacea conjunctivitis) |
| Puntaje de Predicción TxGNN | 0.9957 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado (registros anulados: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 0) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Epinastina es un antagonista tópico del receptor H1 de histamina con actividad estabilizadora de mastocitos. Se presenta en forma de colirio para conjuntivitis alérgica, vernal y papilar, pero actualmente no está comercializada en este país (solo constan registros cancelados). Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Epinastine (traducción no oficial): «La epinastina es un antagonista directo del receptor H 1, de acción tópica, y un inhibidor de la liberación de histamina desde el mastocito. La epinastina es selectiva para el receptor H 1 de la histamina y tiene afinidad por el receptor H 2 de la histamina.» Texto original en inglés: "Epinastine is a topically active, direct H 1 -receptor antagonist and an inhibitor of the release of histamine from the mast cell. Epinastine is selective for the histamine H 1 -receptor and has affinity for the histamine H 2 -receptor." ([DailyMed: epinastine hydrochloride prescribing information, Somerset Therapeutics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0d4ee45c-e58f-4b7c-b389-898f5c27f54d), versión del 2025-03-22; consultado el 2026-11-19).

La conjuntivitis rosácea (rosácea ocular) se debe principalmente a disfunción de las glándulas de Meibomio, inflamación del borde palpebral y factores microbianos o de *Demodex*, más que a una alergia clásica mediada por IgE. Por ello, el mecanismo antihistamínico y de estabilización de mastocitos ofrece solo un vínculo plausible y parcial, probablemente limitado al componente inflamatorio o al picor asociado.

El puntaje tan alto del modelo (0,9957) probablemente refleja la proximidad en la red de conocimiento con otras indicaciones de conjuntivitis, y no está respaldado por evidencia clínica ni bibliográfica. Debe interpretarse con cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 65574 | RELESTAT 0,5 mg/ml COLIRIO EN SOLUCION | COLIRIO EN SOLUCIÓN | Abbvie Spain, S.L.U. | Revocada |

Se muestra la única autorización con este principio activo en los datos de CIMA (AEMPS).

<!-- licenses:end -->

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

El segundo candidato, **urticaria alérgica** (puntaje TxGNN 0,9928), tiene una evidencia indirecta algo mayor (nivel L4, recomendación "Research Question"). La literatura disponible consiste en revisiones y estudios farmacodinámicos de supresión de roncha y eritema inducidos por histamina (por ejemplo, un ensayo cruzado doble ciego en voluntarios sanos, PMID [10442525](https://pubmed.ncbi.nlm.nih.gov/10442525/)), pero no hay ensayos clínicos registrados ni un ECA específico en urticaria. Además, la autorización española corresponde únicamente a un colirio oftálmico, por lo que habría que verificar la formulación oral y su estado regulatorio antes de cualquier decisión.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: epinastine hydrochloride prescribing information, Somerset Therapeutics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0d4ee45c-e58f-4b7c-b389-898f5c27f54d) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

