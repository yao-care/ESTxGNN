---
layout: default
title: Hydromorphone
parent: Solo predicción del modelo (L5)
nav_order: 396
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-28
monitor_inn: "hydromorphone"
predicted_indications: ["pharyngitis", "allergic urticaria", "nasal cavity disease", "acute laryngopharyngitis", "headache disorder", "trigeminal autonomic cephalalgia"]
description: "Hydromorphone: nueva indicación predicha, Faringitis (pharyngitis) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Hydromorphone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Hydromorphone: Faringitis (pharyngitis)
{: .text-alpha }

## Resumen en Una Frase

La hidromorfona es un opioide agonista mu, originalmente asociado en la base de conocimiento del modelo a indicaciones como el resfriado común y la nasofaringitis, y comercializado en España como analgésico opioide en múltiples formulaciones.
El modelo TxGNN predice que podría ser efectiva para **faringitis**, pero solo con **3 ensayos clínicos** de dolor posoperatorio tras amigdalectomía (evidencia indirecta) y **ninguna publicación** directamente relacionada.
La puntuación alta del modelo no está respaldada por evidencia clínica directa.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Faringitis (pharyngitis) |
| Puntaje de Predicción TxGNN | 0.9981 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 7 de 13) |
| Número de Autorizaciones | 13 (vigentes: 7) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, la hidromorfona es un agonista del receptor opioide mu con acción analgésica central y propiedades antitusivas.

La relación con la indicación original (resfriado común, nasofaringitis) es de tipo sintomático: ambas son afecciones de las vías respiratorias altas en las que el dolor o la tos podrían aliviarse con un opioide. Es probable que el puntaje del modelo TxGNN (aprendizaje profundo) refleje similitudes que el modelo aprendió entre enfermedades relacionadas y no un efecto terapéutico real ni evidencia biológica.

Mecanísticamente, la hidromorfona no tiene acción antiinfecciosa ni antiinflamatoria sobre la faringitis. Cualquier utilidad se limitaría al alivio sintomático del dolor, con un perfil de riesgo (depresión respiratoria, dependencia) poco favorable para una afección habitualmente leve y autolimitada. Los tres ensayos disponibles estudian dolor posquirúrgico tras amigdalectomía, no faringitis.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04230681](https://clinicaltrials.gov/study/NCT04230681) | Fase 1 temprana | Completado | 189 | Hidromorfona vs fentanilo para el control del dolor tras amigdalectomía en niños. Evidencia indirecta (dolor perioperatorio) |
| [NCT05244226](https://clinicaltrials.gov/study/NCT05244226) | Fase 2 | Completado | 66 | Opioides de acción corta (fentanilo/hidromorfona) vs metadona de acción prolongada tras amigdalectomía pediátrica. Fármaco evaluado: metadona; relevancia baja |
| [NCT06576830](https://clinicaltrials.gov/study/NCT06576830) | Fase 4 | En reclutamiento | 440 | Metadona intraoperatoria en dosis única vs opioides de acción corta en amigdalectomía pediátrica. Relevancia baja |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para faringitis.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 79784 | EDUNIX 8 mg comprimidos de liberación prolongada | Comprimido de liberación prolongada | No disponible |
| 68019 | JURNISTA 16 mg comprimidos de liberación prolongada | Comprimido de liberación prolongada | No disponible |
| 79783 | EDUNIX 4 mg comprimidos de liberación prolongada | Comprimido de liberación prolongada | No disponible |
| 86201 | EDUNIX 2,6 mg cápsulas duras EFG | Cápsula dura | No disponible |
| 90236 | EDUNIX 2,6 mg/ml solución oral | Solución oral | No disponible |

Se muestran 5 de las 13 autorizaciones vigentes (todas de monofármaco, ninguna cancelada).

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no el texto del prospecto)**: insuficiencia hepática y renal, epilepsia, insuficiencia respiratoria, insuficiencia suprarrenal (incluida la enfermedad de Addison), hipotiroidismo, enfermedad inflamatoria intestinal y colitis ulcerosa, hiperplasia prostática benigna, trastornos hipotensivos, paro cardíaco súbito, enfermedad de la conducción cardíaca, enfermedad de la vesícula biliar, estreñimiento, y trastornos por uso de sustancias o dependencia de fármacos.
- **Interacciones farmacológicas**: se identificaron 207 interacciones. Entre las de nivel **Mayor** figuran alvimopán, bupropión, morfina y naltrexona. Entre las de nivel **Moderado** destacan anticolinérgicos (atropina, hioscina, glicopirronio, diciclomina, trospio), loperamida, naloxona, cimetidina, eluxadolina y cannabinoides (dronabinol, nabilona).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe evidencia directa en faringitis: los ensayos son de dolor posquirúrgico y no hay publicaciones relacionadas. El mecanismo opioide no actúa sobre la causa de la faringitis y el riesgo de depresión respiratoria y dependencia desaconseja su uso. La predicción del modelo no está respaldada clínicamente.

**Para avanzar se necesita:**
- Ensayos clínicos que evalúen directamente la hidromorfona en faringitis o dolor faríngeo no quirúrgico
- Datos detallados del mecanismo de acción
- Advertencias y contraindicaciones del prospecto de la AEMPS, así como los textos de indicación aprobada
- Análisis de la relación riesgo-beneficio frente a alternativas no opioides
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

