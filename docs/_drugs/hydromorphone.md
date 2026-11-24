---
layout: default
title: Hydromorphone
parent: Solo predicción del modelo (L5)
nav_order: 396
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
monitor_inn: "hydromorphone"
predicted_indications: ["pharyngitis", "allergic urticaria", "nasal cavity disease", "acute laryngopharyngitis", "headache disorder", "trigeminal autonomic cephalalgia"]
description: "Hydromorphone: nueva indicación predicha, Faringitis (pharyngitis) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 13 (comercializadas: 7)"
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
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 7 de 13; revocadas o suspendidas: 6) |
| Número de Autorizaciones | 13 (comercializadas: 7) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Hydromorphone (traducción no oficial): «La hidromorfona es un agonista opioide completo y es relativamente selectiva para el receptor opioide mu, aunque puede unirse a otros receptores opioides a dosis más altas. La principal acción terapéutica de la hidromorfona es la analgesia.» Texto original en inglés: "Hydromorphone is a full opioid agonist and is relatively selective for the mu-opioid receptor, although it can bind to other opioid receptors at higher doses. The principal therapeutic action of hydromorphone is analgesia." ([DailyMed: Dilaudid (hydromorphone hydrochloride) prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9eebd88a-5632-460f-b7b6-26c8a180540d), versión del 2026-07-15; consultado el 2026-11-19). Según la información conocida, la hidromorfona es un agonista del receptor opioide mu con acción analgésica central y propiedades antitusivas.

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

<!-- review:begin es-lic-20261105-hydromorphone-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Se muestran 5 de las 13 autorizaciones vigentes (todas de monofármaco, ninguna cancelada)." Eliminado: afirmaba que el medicamento no está autorizado o comercializado en España, o que sus autorizaciones están revocadas o suspendidas, lo que no coincide con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en España. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-hydromorphone-1 -->

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 79784 | EDUNIX 8 MG COMPRIMIDOS DE LIBERACION PROLONGADA | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Aristo Pharma Gmbh | Comercializada |
| 79783 | EDUNIX 4 MG COMPRIMIDOS DE LIBERACION PROLONGADA | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Aristo Pharma Gmbh | Comercializada |
| 86201 | EDUNIX 2,6 MG CAPSULAS DURAS EFG | CÁPSULA DURA | Aristo Pharma Gmbh | Comercializada |
| 90236 | EDUNIX 2,6 MG/ML SOLUCION ORAL | SOLUCIÓN ORAL | Aristo Pharma Gmbh | Comercializada |
| 86200 | EDUNIX 1,3 MG CAPSULAS DURAS EFG | CÁPSULA DURA | Aristo Pharma Gmbh | Comercializada |
| 79781 | EDUNIX 16 MG COMPRIMIDOS DE LIBERACION PROLONGADA | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Aristo Pharma Gmbh | Comercializada |
| 79782 | EDUNIX 32 MG COMPRIMIDOS DE LIBERACION PROLONGADA | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Aristo Pharma Gmbh | Comercializada |
| 68019 | JURNISTA 16 mg COMPRIMIDOS DE LIBERACION PROLONGADA | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Janssen Cilag S.A. | Revocada |
| 69710 | JURNISTA 4 mg COMPRIMIDOS DE LIBERACION PROLONGADA | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Janssen Cilag S.A. | Revocada |
| 68018 | JURNISTA 8 mg COMPRIMIDOS DE LIBERACION PROLONGADA | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Janssen Cilag S.A. | Revocada |

Se muestran 10 de 13 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

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

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | Eliminado: "Se muestran 5 de las 13 autorizaciones vigentes (todas de monofármaco, ninguna cancelada)" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Dilaudid (hydromorphone hydrochloride) prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9eebd88a-5632-460f-b7b6-26c8a180540d) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

