---
layout: default
title: Eptifibatide
parent: Solo predicción del modelo (L5)
nav_order: 299
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Eptifibatide: nueva indicación predicha, Artritis reumatoide (nivel de evidencia L5). Indicación original: Síndrome coronario agudo (según el grafo de conocimiento"
monitor_inn: "Eptifibatide"
predicted_indications: ["rheumatoid arthritis", "sickle cell-hemoglobin d disease syndrome", "hereditary persistence of fetal hemoglobin-sickle cell disease syndrome", "sickle cell-hemoglobin c disease syndrome", "sickle cell-hemoglobin E disease syndrome", "sickle cell-beta-thalassemia disease syndrome", "hemoglobinopathy", "female breast carcinoma", "beta-thalassemia with other manifestations", "partial deletion of the short arm of chromosome 16"]
---

# Eptifibatide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Eptifibatida: De Síndrome Coronario Agudo a Artritis Reumatoide

## Resumen en Una Frase

La eptifibatida es un antiagregante plaquetario utilizado originalmente en el síndrome coronario agudo.
El modelo TxGNN predice que podría ser efectiva para la **artritis reumatoide**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta indicación; se trata solo de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Síndrome coronario agudo (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no vienen informados) |
| Nueva Indicación Predicha | Artritis reumatoide |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados no incluyen una descripción detallada del mecanismo de acción. Aun así, la eptifibatida es un antagonista del receptor GPIIb/IIIa (integrina αIIbβ3) que inhibe la agregación plaquetaria. Por ello se usa en el síndrome coronario agudo, normalmente junto con aspirina y heparina no fraccionada, para prevenir el infarto de miocardio en pacientes de alto riesgo.

La relación con la artritis reumatoide es solo conceptual. La activación plaquetaria contribuye a la inflamación sinovial, por lo que bloquear la función plaquetaria podría tener algún efecto. Sin embargo, la indicación original es cardiovascular y trombótica, y la nueva es una enfermedad autoinmune crónica, de modo que la similitud entre ambas es limitada. El dato de similitud con la indicación original figura como pendiente de análisis.

El puntaje TxGNN es muy alto, pero refleja únicamente una predicción computacional sin respaldo clínico ni bibliográfico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1151065001 | Eptifibatida Accord 0,75 mg/ml solución para perfusión EFG | Solución para perfusión | No especificada en los datos compilados |
| 99109002 | Integrilin 2 mg/ml, solución inyectable | Solución inyectable | No especificada en los datos compilados |
| 1151065002 | Eptifibatida Accord 2 mg/ml solución inyectable EFG | Solución inyectable | No especificada en los datos compilados |
| 99109001 | Integrilin 0,75 mg/ml, solución para perfusión | Solución para perfusión | No especificada en los datos compilados |

Las cuatro autorizaciones son de monofármaco y están vigentes. Los titulares son Accord Healthcare S.L.U. y Glaxosmithkline (Ireland) Limited.

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación (según el grafo de conocimiento, no según el prospecto)**: trombocitopenia, trastornos de la coagulación e insuficiencia renal.
- **Interacciones farmacológicas**: la consulta no identificó interacciones con otros fármacos. El único registro corresponde a la diana farmacológica (integrina αIIbβ3). En la práctica clínica se administra junto con aspirina y heparina, por lo que conviene vigilar el riesgo hemorrágico de la combinación.
- Para advertencias y contraindicaciones oficiales, consultar el prospecto de la AEMPS, ya que no se dispone de ellas en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para la artritis reumatoide solo existe una predicción computacional (nivel L5), sin ensayos ni publicaciones. Además, el riesgo hemorrágico de un antiagregante intravenoso resulta difícil de justificar en una enfermedad crónica sin evidencia previa.

Entre las demás predicciones del modelo, la **hemoglobinopatía (enfermedad de células falciformes)** es la que tiene más respaldo (nivel L2). Cuenta con un ensayo de Fase I/II (NCT00834899, terminado con solo 13 participantes) y tres estudios clínicos publicados (PMID 17916103, 23973010 y 29322543). Se sugiere considerarla como línea prioritaria de investigación frente a la artritis reumatoide.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), que es un dato bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión bibliográfica dirigida sobre plaquetas/GPIIb/IIIa en artritis reumatoide y estudios preclínicos que justifiquen avanzar.
- Evaluar la compatibilidad de la vía de administración (parenteral) con el uso crónico previsto.
- Definir un análisis de riesgo-beneficio frente al riesgo hemorrágico en esta población.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

