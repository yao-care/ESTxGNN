---
layout: default
title: Carboplatin
parent: Solo predicción del modelo (L5)
nav_order: 147
evidence_level: L5
indication_count: 9
monitor_inn: "carboplatin"
predicted_indications: ["rectum mucinous adenocarcinoma", "colon mucinous adenocarcinoma", "adult germ cell tumor", "cervical mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma", "endometrial mucinous adenocarcinoma", "villoglandular endometrial endometrioid adenocarcinoma", "endometrial mixed adenocarcinoma", "extrahepatic bile duct mucinous adenocarcinoma"]
last_modified_at: 2026-11-20
description: "Carboplatin: nueva indicación predicha, Adenocarcinoma mucinoso de recto (rectum mucinous adenocarcinoma) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 6 (comercializadas: 5)"
---

# Carboplatin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Carboplatino: antineoplásico derivado del platino → adenocarcinoma mucinoso de recto (rectum mucinous adenocarcinoma)
{: .text-alpha }

## Resumen en Una Frase

Carboplatino es un fármaco antineoplásico del grupo de los compuestos de platino, utilizado en quimioterapia de tumores sólidos. El modelo TxGNN predice que podría ser efectivo para el **adenocarcinoma mucinoso de recto (rectum mucinous adenocarcinoma)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección. Se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Adenocarcinoma mucinoso de recto (rectum mucinous adenocarcinoma) |
| Puntaje de Predicción TxGNN | 0,9928 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 5 de 6; revocadas o suspendidas: 1) |
| Número de Autorizaciones | 6 (comercializadas: 5) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Carboplatin (traducción no oficial): «El carboplatino es un fármaco a base de platino que se une al ADN y forma entrecruzamientos del ADN. Estos entrecruzamientos inhiben la replicación y la transcripción del ADN y desencadenan procesos citotóxicos que conducen a la muerte celular.» Texto original en inglés: "Carboplatin is a platinum-based drug that binds to DNA and forms DNA cross-links. These crosslinks inhibit DNA replication and transcription and trigger cytotoxic processes that lead to cell death." ([DailyMed: Kyxata (carboplatin) prescribing information, AVYXA Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f91c48da-68d1-4aa7-89b8-d84a3e8b629b), versión del 2026-11-09; consultado el 2026-11-19). Por conocimiento general de la clase, carboplatino es un compuesto de platino que daña el ADN de las células tumorales mediante enlaces cruzados, lo que impide su división y favorece su muerte.

Ese mecanismo es, en principio, aplicable a tumores de origen epitelial como los adenocarcinomas del tubo digestivo. Esto explica por qué el modelo asigna un puntaje alto a esta indicación.

Sin embargo, el vínculo es especulativo. No existen ensayos ni literatura que muestren actividad de carboplatino en este tumor. Además, la histología mucinosa se considera en general menos sensible a la quimioterapia, lo que reduce la plausibilidad de beneficio.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (compuesto de platino) |
| Riesgo de Mielosupresión | Alto (la mielosupresión, en especial trombocitopenia y neutropenia, es la toxicidad limitante de dosis en la clase) |
| Clasificación de Emetogenicidad | Media a alta, según la dosis |
| Items de Monitoreo | Hemograma con diferencial, función renal, función hepática, electrolitos; vigilancia de neuropatía periférica y audición |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos. Consultar las advertencias y precauciones del prospecto. |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registran 488 interacciones en total. Entre las de nivel moderado destacan:
  - los inhibidores de la bomba de protones (omeprazol, esomeprazol, lansoprazol, dexlansoprazol, pantoprazol, rabeprazol);
  - los aminoglucósidos (kanamicina, neomicina, estreptomicina);
  - la vancomicina;
  - el metronidazol y el tinidazol;
  - las estatinas (rosuvastatina, simvastatina).

  La interacción con levofloxacino es de nivel menor.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (0,9928), sin ensayos clínicos ni literatura que estudien esta enfermedad. La histología mucinosa suele responder peor a la quimioterapia, por lo que no hay base suficiente para avanzar.

**Para avanzar se necesita:**
- Revisión sistemática de la literatura sobre quimioterapia con platino en adenocarcinoma mucinoso colorrectal.
- Datos preclínicos o series de casos que muestren actividad de carboplatino en esta histología.
- Datos del mecanismo de acción y de las advertencias y contraindicaciones del prospecto.
- Evaluación de seguridad en la población objetivo, dada la mielosupresión esperada.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Kyxata (carboplatin) prescribing information, AVYXA Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f91c48da-68d1-4aa7-89b8-d84a3e8b629b) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

