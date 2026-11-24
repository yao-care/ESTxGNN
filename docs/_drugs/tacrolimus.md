---
layout: default
title: Tacrolimus
parent: Evidencia alta (L1-L2)
nav_order: 758
evidence_level: L1
indication_count: 2
last_modified_at: 2026-11-24
description: "Tacrolimus: nueva indicación predicha, Dermatitis seborreica (nivel de evidencia L1). Indicación original: Dermatitis atópica (eccema atópico)"
monitor_inn: "TACROLIMUS"
predicted_indications: ["seborrheic dermatitis", "parapsoriasis"]
---

# Tacrolimus
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **2** 
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

## Tacrolimus: De Dermatitis Atópica a Dermatitis Seborreica
{: .text-alpha }

## Resumen en Una Frase

Tacrolimus es un inhibidor de la calcineurina, utilizado originalmente para el tratamiento de la dermatitis atópica (eccema atópico) y, en sus formulaciones sistémicas, en el contexto del trasplante.
El modelo TxGNN predice que podría ser efectivo para **dermatitis seborreica**, con **2 ensayos clínicos** (uno de Fase 3 completado) y **20 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dermatitis atópica (eccema atópico); los textos de indicación de las autorizaciones españolas no están disponibles en los datos compilados |
| Nueva Indicación Predicha | Dermatitis seborreica |
| Puntaje de Predicción TxGNN | 0,9926 |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 17; revocadas o suspendidas: 3) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Tacrolimus (traducción no oficial): «El tacrolimus se une a una proteína intracelular, FKBP-12. A continuación, se forma un complejo de tacrolimus-FKBP-12, calcio, calmodulina y calcineurina (una enzima intracelular ubicua en los mamíferos) y se inhibe la actividad fosfatasa de la calcineurina.» Texto original en inglés: "Tacrolimus binds to an intracellular protein, FKBP-12. A complex of tacrolimus-FKBP-12, calcium, calmodulin, and calcineurin (an ubiquitous mammalian intracellular enzyme) is then formed and the phosphatase activity of calcineurin inhibited." ([DailyMed: Envarsus Xr (tacrolimus) prescribing information, Veloxis Pharmaceuticals, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=de2315b0-6344-43ac-9aea-3e3b68d828e7), versión del 2025-02-26; consultado el 2026-11-19). Según la información conocida y la literatura compilada, tacrolimus inhibe la calcineurina, lo que suprime la activación de los linfocitos T y la liberación de citocinas proinflamatorias (como IL-2 e IL-4).

La dermatitis seborreica es una enfermedad inflamatoria crónica de la piel, con recaídas frecuentes, que afecta sobre todo a la cara y el cuero cabelludo. Implica una respuesta inflamatoria frente a levaduras del género *Malassezia*. Este componente inflamatorio se solapa con el de la dermatitis atópica, indicación en la que tacrolimus tópico ya está establecido, por lo que el mecanismo antiinflamatorio es plausible en ambas enfermedades.

Además, existen estudios clínicos directos en la indicación predicha, incluido un ensayo de Fase 3 sobre el tratamiento de mantenimiento de la dermatitis seborreica facial grave con pomada de tacrolimus, y revisiones que describen el papel de los inhibidores tópicos de la calcineurina en esta enfermedad.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Fase 3 | Completado | 120 | Pomada de tacrolimus (Protopic®) como tratamiento de mantenimiento de la dermatitis seborreica grave en la cara de adultos, para reducir recaídas y el uso de corticoides tópicos |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Fase 4 | Completado | 104 | Uso proactivo de tacrolimus 0,1% pomada una o dos veces por semana para mantener la remisión de la dermatitis seborreica facial del adulto |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | Estudio clínico | Annals of Dermatology | Terapia de mantenimiento de la dermatitis seborreica facial con tacrolimus 0,1% pomada |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Revisión sistemática | American Journal of Clinical Dermatology | Tratamiento tópico de la dermatitis seborreica facial (antifúngicos, queratolíticos, corticoides) |
| [19222250](https://pubmed.ncbi.nlm.nih.gov/19222250/) | 2009 | Revisión | American Journal of Clinical Dermatology | Los inhibidores tópicos de la calcineurina son una alternativa segura a los corticoides en la dermatitis seborreica |
| [24171300](https://pubmed.ncbi.nlm.nih.gov/24171300/) | 2013 | Ensayo clínico | Annals of Parasitology | Comparación de sertaconazol 2% crema frente a tacrolimus 0,03% crema en 60 pacientes con dermatitis seborreica |
| [31476936](https://pubmed.ncbi.nlm.nih.gov/31476936/) | 2019 | Revisión | Journal of Cutaneous Medicine and Surgery | Uso fuera de indicación de los inhibidores tópicos de la calcineurina en diversas enfermedades dermatológicas |
| [17685874](https://pubmed.ncbi.nlm.nih.gov/17685874/) | 2007 | Revisión | Expert Opinion on Investigational Drugs | Nuevos usos de tacrolimus tópico, con buen perfil de seguridad y mínima absorción sistémica |
| [15461548](https://pubmed.ncbi.nlm.nih.gov/15461548/) | 2004 | Revisión | Expert Opinion on Pharmacotherapy | Tacrolimus pomada en dermatitis atópica y otras enfermedades cutáneas inflamatorias |
| [11770914](https://pubmed.ncbi.nlm.nih.gov/11770914/) | 2001 | Revisión | Seminars in Cutaneous Medicine and Surgery | Experiencias con inmunomoduladores tópicos en psoriasis, dermatitis seborreica y otras enfermedades |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Revisión | Journal of Drugs in Dermatology | Situación actual y perspectivas terapéuticas de la dermatitis seborreica facial |
| [16094289](https://pubmed.ncbi.nlm.nih.gov/16094289/) | 2005 | Observacional | Nihon Ishinkin Gakkai Zasshi | Especies de *Malassezia* en pacientes con dermatitis seborreica y atópica (contexto mecanístico) |

---

## Información de Mercado en España

Los textos de indicación aprobada no figuran en los datos compilados. Se muestran las cinco principales, priorizando las formulaciones tópicas:

<!-- review:begin es-lic-20261105-tacrolimus-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Tacrolimus cuenta con 20 autorizaciones vigentes (todas de monofármaco). Los textos de indicación aprobada no figuran en los datos compilados." Eliminado: el número o el estado de comercialización de las autorizaciones no coincidía con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-tacrolimus-1 -->

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 88081 | TACROLIMUS STADAFARMA 5 MG CAPSULAS DURAS DE LIBERACION PROLONGADA EFG | CÁPSULA DURA DE LIBERACIÓN PROLONGADA | Laboratorio Stada S.L. | Comercializada |
| 02201004 | PROTOPIC 0,1% POMADA | POMADA | Leo Pharma A/S | Comercializada |
| 114935005 | Envarsus 1mg comprimidos de liberacion prolongada | COMPRIMIDO DE LIBERACIÓN MODIFICADA | Chiesi Farmaceutici S.P.A. | Comercializada |
| 07387014 | ADVAGRAF 0,5 MG CAPSULAS DURAS DE LIBERACION PROLONGADA | CÁPSULA DURA DE LIBERACIÓN PROLONGADA | Astellas Pharma Europe B.V. | Comercializada |
| 84631 | CONFEROPORT 3 MG CAPSULAS DURAS DE LIBERACION PROLONGADA EFG | CÁPSULA DURA DE LIBERACIÓN PROLONGADA | Sandoz Farmaceutica S.A. | Comercializada |

Se muestran 5 de al menos 20 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas. Los datos de este informe solo incluyen parte de las autorizaciones.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de precaución (según el grafo de conocimiento, no el prospecto)**: se asocian a tacrolimus enfermedades como hipertensión, síndrome de QT largo y torsades de pointes, insuficiencia hepática, enfermedad renal, hiperglucemia y diabetes, infecciones (herpes simple, herpes zóster, mononucleosis, infección crónica por virus de Epstein-Barr, leucoencefalopatía multifocal progresiva), cáncer y linfomas, epilepsia, delirium y síndrome de leucoencefalopatía posterior. Estas asociaciones proceden mayoritariamente de la exposición sistémica y deben confirmarse en el prospecto.
- **Interacciones farmacológicas** (se identificaron 100 en total; se muestran las principales):
  - Gravedad **mayor**: anfotericina B (y complejo lipídico), loperamida, mesalazina, balsalazida, omeprazol.
  - Gravedad **moderada**: acarbosa, famotidina, rabeprazol, hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida, metformina, pioglitazona, albiglutida, alogliptina, aprepitant, metronidazol.
- **Seguridad a largo plazo en uso tópico**: una revisión sistemática con metaanálisis (2023) analizó el riesgo de cáncer con inhibidores tópicos de la calcineurina. Se recomienda precaución en niños pequeños y evitar la aplicación sobre piel infectada o lesionada.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ensayo de Fase 3 completado (n=120) y un estudio de Fase 4 (n=104) directamente en dermatitis seborreica, además de revisiones que respaldan el uso de inhibidores tópicos de la calcineurina. El mecanismo es coherente con la indicación original y el perfil de seguridad tópico es conocido, aunque las preocupaciones sobre el uso prolongado exigen salvaguardas. Cabe señalar que solo hay un ensayo de Fase 3, por lo que el nivel L1 asignado debe interpretarse con cautela.

**Para avanzar se necesita:**
- Revisar los resultados publicados del ensayo NCT02004860 (eficacia sobre recaídas y reducción del uso de corticoides).
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), así como los textos de indicación de cada autorización.
- Completar los datos del mecanismo de acción desde DrugBank.
- Definir un plan de seguridad para el uso tópico prolongado (riesgo de neoplasias, infecciones cutáneas, poblaciones pediátricas) y confirmar la disponibilidad de la vía tópica para la nueva indicación.
- Verificar que las formulaciones tópicas autorizadas en España (pomada) se ajusten a la localización facial de la dermatitis seborreica.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Tacrolimus cuenta con 20 autorizaciones vigentes (todas de monofármaco)" | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Envarsus Xr (tacrolimus) prescribing information, Veloxis Pharmaceuticals, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=de2315b0-6344-43ac-9aea-3e3b68d828e7) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

