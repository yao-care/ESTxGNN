---
layout: default
title: Cladribine
parent: Solo predicción del modelo (L5)
nav_order: 186
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-24
monitor_inn: "Cladribine"
predicted_indications: ["parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "embryonal extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "rhabdomyosarcoma (disease)", "liver sarcoma"]
description: "Cladribine: nueva indicación predicha, Parameningeal embryonal rhabdomyosarcoma (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 5 (comercializadas: 4; autorizadas no comercializadas: 1)"
---

# Cladribine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

## Cladribine: Parameningeal embryonal rhabdomyosarcoma
{: .text-alpha }

## Resumen en Una Frase

Cladribina es un análogo de nucleósidos de purina, utilizado originalmente para el tratamiento de la leucemia de células pilosas y de la esclerosis múltiple remitente-recurrente.
El modelo TxGNN predice que podría ser efectivo para el **rabdomiosarcoma embrionario parameníngeo**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Parameningeal embryonal rhabdomyosarcoma |
| Puntaje de Predicción TxGNN | 0.9977 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 4 de 5; autorizadas no comercializadas: 1) |
| Número de Autorizaciones | 5 (comercializadas: 4) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Cladribine (traducción no oficial): «El mecanismo por el cual la cladribina ejerce sus efectos terapéuticos en los pacientes con esclerosis múltiple no se ha dilucidado por completo, pero se cree que implica efectos citotóxicos sobre los linfocitos B y T mediante la alteración de la síntesis del ADN, lo que da lugar a una depleción de linfocitos.» Texto original en inglés: "The mechanism by which cladribine exerts its therapeutic effects in patients with multiple sclerosis has not been fully elucidated but is thought to involve cytotoxic effects on B and T lymphocytes through impairment of DNA synthesis, resulting in depletion of lymphocytes." ([DailyMed: Mavenclad (cladribine) prescribing information, EMD Serono, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9c75e30a-a410-40f1-b653-04d532bd9144), versión del 2026-05-27; consultado el 2026-11-19). Según la información conocida, cladribina es un análogo de nucleósidos de purina resistente a la adenosina desaminasa; provoca roturas de cadenas de ADN y apoptosis, principalmente en linfocitos y monocitos con alta actividad de desoxicitidina cinasa. Esto explica su eficacia en neoplasias hematológicas linfoides y en la esclerosis múltiple (donde actúa sobre poblaciones linfocitarias).

La relación con el rabdomiosarcoma embrionario parameníngeo es **débil y no está establecida**. Se trata de un tumor sólido de origen mesenquimal, muy distinto de las neoplasias linfoides. No hay evidencia en los datos de que la citotoxicidad de este análogo de purina sea relevante para este tumor.

Además, las siete predicciones principales (seis variantes de rabdomiosarcoma, incluido el término general, y un sarcoma hepático) probablemente reflejan una misma señal repetida, y no hallazgos independientes. El puntaje elevado (0.9977) proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. Por ello, debe interpretarse con cautela.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal (rabdomiosarcoma embrionario parameníngeo).

Como referencia, en la séptima predicción (sarcoma hepático) solo se recuperó un artículo, que no respalda esa indicación:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15241520](https://pubmed.ncbi.nlm.nih.gov/15241520/) | 2004 | Reporte de caso | Der Hautarzt | Terapia exitosa con cladribina en mastocitosis sistémica latente (smoldering); se trata de una neoplasia hematológica de mastocitos, no de un sarcoma hepático |

---

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 61380 | LEUSTATIN 1 MG/ML SOLUCION PARA PERFUSION | SOLUCIÓN INYECTABLE | Atnahs Pharma Netherlands Bv. | Comercializada |
| 04275001 | LITAK 2 mg/ml SOLUCION INYECTABLE | SOLUCIÓN INYECTABLE | Lipomed Gmbh | Comercializada |
| 1171212001 | MAVENCLAD 10 MG COMPRIMIDOS | COMPRIMIDO | Merck Europe B.V. | Comercializada |
| 04275002 | LITAK 2 mg/ml SOLUCION INYECTABLE | SOLUCIÓN INYECTABLE | Lipomed Gmbh | Comercializada |
| 90544 | LEUSTATIN 2 MG/ML SOLUCION INYECTABLE | SOLUCIÓN INYECTABLE | Atnahs Pharma Netherlands Bv. | Autorizada, no comercializada |

Se muestran las 5 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (análogo de nucleósidos de purina) |
| Riesgo de Mielosupresión | Alto, según las contraindicaciones del grafo de conocimiento (neutropenia, trombocitopenia, agranulocitosis, anemia) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma completo con diferencial, función renal y hepática, ácido úrico; vigilancia de signos de neuropatía periférica |
| Protección en Manejo | Las presentaciones inyectables deben manejarse según las regulaciones para fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no texto de prospecto)**: enfermedad renal, piouréter, trombocitopenia, hiperuricemia, neutropenia, agranulocitosis, enfermedad del sistema nervioso periférico, neuropatía periférica, anemia y anemia macrocítica.
- **Interacciones Farmacológicas** (100 interacciones registradas; se muestran las principales):
  - **Mayor**: corticosteroides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida, prednisolona, prednisona), deferiprona, y radiofármacos/anticuerpos radiomarcados (ibritumomab tiuxetán, iobenguano I-131, tositumomab, samario-153 lexidronam, cloruro de estroncio-89).
  - **Moderada**: palifermina, dipiridamol, cilostazol, eltrombopag.
  - **Desconocida**: ácido acetilsalicílico.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y el vínculo mecanístico entre un análogo de purina y un sarcoma embrionario sólido no está establecido. El perfil de mielosupresión de cladribina añade cautela.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) y análisis de su relevancia en rabdomiosarcoma.
- Estudios preclínicos (líneas celulares, modelos in vivo) que muestren actividad en rabdomiosarcoma.
- Revisión de la ficha técnica de la AEMPS (advertencias y contraindicaciones oficiales), pendiente de obtener.
- Textos de indicación aprobada de las autorizaciones españolas.
- Evaluación de la compatibilidad de vía de administración y de la población pediátrica objetivo.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Mavenclad (cladribine) prescribing information, EMD Serono, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9c75e30a-a410-40f1-b653-04d532bd9144) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

