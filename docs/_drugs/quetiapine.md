---
layout: default
title: Quetiapine
parent: Solo predicción del modelo (L5)
nav_order: 674
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "Quetiapine"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "congenital disorder of glycosylation with defective fucosylation", "hydranencephaly (disease)", "distal 17p13.3 microdeletion syndrome", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "myopia X-linked", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "trichotillomania", "syndromic myopia", "myopia 26, X-linked, female-limited"]
description: "Quetiapine: nueva indicación predicha, Distrofia retiniana con o sin anomalías extraoculares (retinal dystrophy with or without extraocular anomalies) (nivel de evidencia L5). Indicación original: No…"
---

# Quetiapine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Quetiapine: Distrofia retiniana con o sin anomalías extraoculares (retinal dystrophy with or without extraocular anomalies)
{: .text-alpha }

> **Nota sobre la selección de la indicación:** la primera predicción del modelo (rank 1, retinopatía distrófica) carece por completo de ensayos clínicos y literatura. La única predicción con alguna evidencia publicada es **tricotilomanía** (rank 8), que se analiza en detalle en las secciones de evidencia como alternativa de interés.

## Resumen en Una Frase

Quetiapina es un antipsicótico atípico utilizado originalmente para el tratamiento de la esquizofrenia y el trastorno bipolar.
El modelo TxGNN predice que podría ser efectivo para **distrofia retiniana con o sin anomalías extraoculares**, pero sin ningún ensayo clínico ni publicación que lo respalde (nivel de evidencia L5).
La predicción con más respaldo documental es **tricotilomanía**, con **0 ensayos clínicos** y **6 publicaciones** (casos clínicos y revisiones).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Distrofia retiniana con o sin anomalías extraoculares (retinal dystrophy with or without extraocular anomalies) |
| Puntaje de Predicción TxGNN | 0.9957 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 9; autorizadas no comercializadas: 5; revocadas o suspendidas: 6) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

**Referencia alternativa (tricotilomanía, rank 8):** puntaje TxGNN 0.9938, nivel de evidencia L4, recomendación "pregunta de investigación".

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Quetiapine (traducción no oficial): «El mecanismo de acción de la quetiapina en las indicaciones enumeradas no está claro. Sin embargo, la eficacia de la quetiapina en estas indicaciones podría estar mediada por una combinación de antagonismo de los receptores de dopamina de tipo 2 (D 2 ) y de serotonina de tipo 2A (5HT 2A ).» Texto original en inglés: "The mechanism of action of quetiapine in the listed indications is unclear. However, the efficacy of quetiapine in these indications could be mediated through a combination of dopamine type 2 (D 2 ) and serotonin type 2A (5HT 2A ) antagonism." ([DailyMed: Quetiapine Extended Release (quetiapine) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6953175c-78ec-442c-b91d-97dfb57db933), versión del 2026-10-08; consultado el 2026-11-19). Según la información conocida, quetiapina es un antipsicótico atípico con eficacia comprobada en esquizofrenia y trastorno bipolar. Los datos farmacológicos compilados indican afinidad por los receptores serotoninérgicos (5-HT1A, 5-HT1D, 5-HT1E, 5-HT1F, 5-HT2A), el receptor dopaminérgico D2, el receptor histamínico H1 y el transportador de noradrenalina (NET).

Para la distrofia retiniana no se identificó ningún vínculo mecanístico con los datos disponibles. Es un trastorno hereditario de la retina y no hay estudios que relacionen la quetiapina con esta enfermedad. El puntaje alto del modelo (0.9957) es una predicción computacional sin respaldo clínico, por lo que debe interpretarse con mucha cautela.

En el caso de la tricotilomanía, el vínculo es plausible pero no confirmado: se trata de un trastorno del espectro obsesivo-compulsivo con conductas repetitivas centradas en el cuerpo, y los antipsicóticos atípicos con actividad serotoninérgica y dopaminérgica se han usado como aumento en cuadros de ese espectro. Esta inferencia proviene de conocimiento general de la clase farmacológica, no de los datos compilados.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados, ni para distrofia retiniana ni para tricotilomanía.

## Evidencia de Literatura

Para la indicación principal (distrofia retiniana) actualmente no hay literatura relacionada disponible. Para la alternativa **tricotilomanía** se identificaron las siguientes publicaciones:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [12405081](https://pubmed.ncbi.nlm.nih.gov/12405081/) | 2002 | Revisión y caso clínico | Psychiatry | Revisión de la tricotilomanía y caso de una veterana de 33 años con respuesta favorable a quetiapina |
| [38797877](https://pubmed.ncbi.nlm.nih.gov/38797877/) | 2025 | Revisión | Int J Dermatol | Revisión del tratamiento farmacológico de la tricotilomanía; no existen guías y la patogenia es desconocida |
| [19142421](https://pubmed.ncbi.nlm.nih.gov/19142421/) | 2008 | Caso clínico | Rev Bras Psiquiatr | Quetiapina para el tratamiento de la tricotilomanía (sin resumen disponible) |
| [11212595](https://pubmed.ncbi.nlm.nih.gov/11212595/) | 2001 | Caso clínico y revisión | J Psychiatry Neurosci | Quetiapina exacerbó síntomas obsesivo-compulsivos en un paciente con TOC y tricotilomanía (señal contraria) |
| [20833945](https://pubmed.ncbi.nlm.nih.gov/20833945/) | 2010 | Caso clínico y revisión | Psychosomatics | Tratamiento del síndrome de Rapunzel recurrente y tricotilomanía |
| [27840761](https://pubmed.ncbi.nlm.nih.gov/27840761/) | 2016 | Caso clínico | Case Rep Psychiatry | Tricotilomanía como manifestación de demencia; no evalúa directamente quetiapina |

## Información de Mercado en España

Los textos de indicación aprobada no están disponibles en los datos compilados. Principales autorizaciones:

<!-- review:begin es-lic-20261105-quetiapine-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Se registran 20 autorizaciones vigentes (todas monofármaco, ninguna cancelada). Los textos de indicación aprobada no están disponibles en los datos compilados." Eliminado: afirmaba que el medicamento no está autorizado o comercializado en España, o que sus autorizaciones están revocadas o suspendidas, lo que no coincide con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-quetiapine-1 -->

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 83355 | QUETIAPINA ALTER 300 MG COMPRIMIDOS DE LIBERACION PROLONGADA EFG | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Laboratorios Alter S.A. | Comercializada |
| 70202 | QUETIAPINA STADA 300 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Laboratorio Stada S.L. | Comercializada |
| 73984 | QUETIAPINA COMBIX 200 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Laboratorios Combix S.L.U. | Comercializada |
| 73831 | QUETIAPINA PENSA 100 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Towa Pharmaceutical S.A. | Comercializada |
| 72883 | QUETIAPINA CINFA 200 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Laboratorios Cinfa S.A. | Comercializada |
| 71557 | QUETIAPINA NORMON 300 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Laboratorios Normon S.A. | Comercializada |
| 79677 | QUETIAPINA STADA 150 MG COMPRIMIDOS DE LIBERACION PROLONGADA EFG | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Laboratorio Stada S.L. | Comercializada |
| 84519 | QUDIX PROLONG 200 MG COMPRIMIDOS DE LIBERACION PROLONGADA EFG | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Adamed Laboratorios S.L.U. | Comercializada |
| 85768 | QUETIAPINA PENSA 150 MG COMPRIMIDOS DE LIBERACION PROLONGADA EFG | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Towa Pharmaceutical S.A. | Comercializada |
| 80241 | QUETIAPINA TARBIS 50 MG COMPRIMIDOS DE LIBERACION PROLONGADA EFG | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Tarbis Farma S.L. | Autorizada, no comercializada |

Se muestran 10 de al menos 20 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas. Los datos de este informe solo incluyen parte de las autorizaciones.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo (según el grafo de conocimiento, no el prospecto):** síndrome de QT largo (incluido el familiar) y torsades de pointes; hipotensión ortostática, hipertensión y atrofia multisistémica; epilepsia; neutropenia y agranulocitosis; diabetes mellitus, cetoacidosis diabética e hiperglucemia; hiperlipidemia e hipertrigliceridemia; obesidad; hipotiroidismo; enfermedad hepática y de vesícula biliar; infarto de miocardio; carcinoma de mama femenino; deficiencia de potasio; y trastornos de los ganglios basales (distonía focal de mano, blefaroespasmo).
- **Interacciones farmacológicas:** los datos compilados describen únicamente afinidad por dianas (receptores 5-HT1A/1D/1E/1F/2A, D2, H1 y NET), no interacciones con otros fármacos específicos.

Las advertencias y contraindicaciones oficiales del prospecto de la AEMPS no están disponibles; consultar el prospecto para la información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de distrofia retiniana se basa únicamente en el modelo (L5), sin ensayos, literatura ni vínculo mecanístico identificable. La alternativa de tricotilomanía (L4) solo cuenta con casos clínicos y revisiones, incluido un reporte de empeoramiento de síntomas obsesivo-compulsivos, por lo que tampoco justifica avanzar sin más estudios.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas).
- Completar los datos del mecanismo de acción desde DrugBank.
- Para distrofia retiniana: estudios preclínicos o de mecanismo que justifiquen cualquier vínculo biológico.
- Para tricotilomanía: ensayos clínicos controlados y una revisión sistemática que aclare la señal contradictoria.
- Evaluar el perfil de riesgo cardiometabólico y hematológico (QT, glucosa, lípidos, neutropenia) en la población objetivo.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Se registran 20 autorizaciones vigentes (todas monofármaco, ninguna cancelada)" | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Quetiapine Extended Release (quetiapine) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6953175c-78ec-442c-b91d-97dfb57db933) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

