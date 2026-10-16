---
layout: default
title: Ofatumumab
parent: Evidencia alta (L1-L2)
nav_order: 582
evidence_level: L2
indication_count: 8
last_modified_at: 2026-10-14
description: "Ofatumumab: nueva indicación predicha, Linfoma folicular (nivel de evidencia L2). Indicación original: Leucemia linfoblástica/linfocítica aguda y síndrome de Richter"
monitor_inn: "OFATUMUMAB"
predicted_indications: ["chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation", "pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma", "follicular lymphoma", "leukemia, lymphocytic, susceptibility to", "chronic lymphocytic leukemia/small lymphocytic lymphoma", "metastatic neoplasm", "malignant spiradenoma", "Langerhans cell histiocytosis"]
---

# Ofatumumab
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **8** 
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

# Ofatumumab: De Leucemia Linfoblástica Aguda a Linfoma Folicular

## Resumen en Una Frase

Ofatumumab es un anticuerpo monoclonal anti-CD20, cuyas indicaciones de partida en el grafo de conocimiento son la leucemia linfoblástica/linfocítica aguda y el síndrome de Richter.
El modelo TxGNN predice que podría ser efectivo para **linfoma folicular**, con **11 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección (incluidos varios ensayos de fase 2, uno de ellos aleatorizado y publicado).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Leucemia linfoblástica/linfocítica aguda y síndrome de Richter (según el grafo de conocimiento; el registro de la AEMPS no incluye texto de indicación) |
| Nueva Indicación Predicha | Linfoma folicular |
| Puntaje de Predicción TxGNN | 99,70% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, ofatumumab es un anticuerpo monoclonal humano dirigido contra CD20, una proteína de la superficie de los linfocitos B. Se une a un epítopo distinto del de rituximab y destruye las células B mediante citotoxicidad dependiente del complemento y citotoxicidad celular dependiente de anticuerpos.

Las indicaciones originales (leucemia linfoblástica/linfocítica y síndrome de Richter) y el linfoma folicular son neoplasias de linfocitos B. Las células del linfoma folicular expresan CD20, por lo que el mecanismo anti-CD20 es directamente aplicable.

La plausibilidad clínica se apoya en varios estudios de fase 2, incluidos estudios aleatorizados, y en datos publicados de eficacia en enfermedad refractaria a rituximab. No se identificó ningún ECA de fase 3 completado que evalúe ofatumumab como brazo experimental en linfoma folicular, por lo que el nivel se mantiene en L2.

Otras predicciones del modelo (subtipos moleculares de LLC/LLP, LLC/LLP en general, neoplasia metastásica, espiradenoma maligno, histiocitosis de células de Langerhans) no se desarrollan aquí. El puntaje alto de varias de ellas parece reflejar la proximidad en la ontología con indicaciones ya existentes, y no una evidencia específica.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01286272](https://clinicaltrials.gov/study/NCT01286272) | Fase 2 | Completado | 135 | Ensayo aleatorizado de ofatumumab + bendamustina con o sin bortezomib en linfoma folicular sin tratamiento previo |
| [NCT00494780](https://clinicaltrials.gov/study/NCT00494780) | Fase 2 | Completado | 59 | Dos dosis de ofatumumab + CHOP en linfoma folicular sin tratamiento previo |
| [NCT00394836](https://clinicaltrials.gov/study/NCT00394836) | Fase 2 | Completado | 116 | Brazo único de ofatumumab en linfoma folicular refractario a rituximab |
| [NCT01077518](https://clinicaltrials.gov/study/NCT01077518) | Fase 3 | Terminado | 346 | Ofatumumab + bendamustina frente a bendamustina sola en linfoma indolente no respondedor a rituximab |
| [NCT02710643](https://clinicaltrials.gov/study/NCT02710643) | Fase 2 | Completado | 110 | Estudio MIRO: radioterapia local con o sin ofatumumab según base molecular en linfoma folicular estadio I/II (efecto de ofatumumab confundido por el diseño combinado) |
| [NCT01190449](https://clinicaltrials.gov/study/NCT01190449) | Fase 2 | Completado | 51 | Ofatumumab en monoterapia en linfoma folicular sin tratamiento previo |
| [NCT00823719](https://clinicaltrials.gov/study/NCT00823719) | Fase 2 | Completado | 61 | Ofatumumab con quimioterapia ICE o DHAP en linfoma agresivo en recaída/refractario antes de trasplante autólogo (brazo único) |
| [NCT01239394](https://clinicaltrials.gov/study/NCT01239394) | Fase 2 | Completado | 43 | Tratamiento inicial de linfoma de células B indolente (población mixta) |
| [NCT00742144](https://clinicaltrials.gov/study/NCT00742144) | Fase 1 | Completado | 6 | Seguridad y farmacocinética en pacientes japoneses con linfoma folicular o LLC |
| [NCT01119794](https://clinicaltrials.gov/study/NCT01119794) | Fase 2 | Terminado | 10 | Ofatumumab + bortezomib en linfoma no Hodgkin de bajo grado en recaída/refractario; muestra muy pequeña |

Otros ensayos (NCT01397591, NCT01263418) se terminaron de forma anticipada o se retiraron, y no aportan datos de eficacia.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31174236](https://pubmed.ncbi.nlm.nih.gov/31174236/) | 2019 | ECA (fase 2) | Cancer | CALGB 50904: ofatumumab + bendamustina con o sin bortezomib en linfoma folicular de alto riesgo sin tratamiento previo |
| [22389254](https://pubmed.ncbi.nlm.nih.gov/22389254/) | 2012 | Fase 2 multicéntrico | Blood | Monoterapia con ofatumumab en linfoma folicular refractario a rituximab (n=116) |
| [22409295](https://pubmed.ncbi.nlm.nih.gov/22409295/) | 2012 | Ensayo fase 2 | Br J Haematol | Ofatumumab + CHOP (dos dosis) en linfoma folicular sin tratamiento previo (n=59) |
| [30723894](https://pubmed.ncbi.nlm.nih.gov/30723894/) | 2019 | Fase 2 multicéntrico | Br J Haematol | CALGB 50901: ofatumumab en monoterapia en linfoma folicular sin tratamiento previo |
| [38937025](https://pubmed.ncbi.nlm.nih.gov/38937025/) | 2024 | Estudio clínico fase 2 | Lancet Haematol | FIL MIRO: radioterapia local e inmunoterapia guiada por enfermedad residual medible en linfoma folicular precoz |
| [18390837](https://pubmed.ncbi.nlm.nih.gov/18390837/) | 2008 | Fase 1/2 | Blood | Primer uso clínico de ofatumumab en linfoma folicular en recaída/refractario |
| [26043777](https://pubmed.ncbi.nlm.nih.gov/26043777/) | 2015 | Revisión | Expert Opin Biol Ther | Actividad de ofatumumab en linfomas no Hodgkin de células B |
| [29934061](https://pubmed.ncbi.nlm.nih.gov/29934061/) | 2018 | Revisión basada en evidencia | Clin Lymphoma Myeloma Leuk | Regímenes con anti-CD20 en LLC, LBDCG o linfoma folicular en recaída/refractario |
| [35663281](https://pubmed.ncbi.nlm.nih.gov/35663281/) | 2022 | Revisión | Leuk Res Rep | Inmunoterapia en linfoma no Hodgkin indolente |
| [32933335](https://pubmed.ncbi.nlm.nih.gov/32933335/) | 2021 | Revisión | Expert Opin Biol Ther | Tratamiento anti-CD20 en neoplasias de células B: situación actual y perspectivas |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 121532003 | KESIMPTA 20 mg solución inyectable en pluma precargada (Novartis Europharm Limited) | Solución inyectable en pluma precargada | No disponible en el registro |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (anticuerpo monoclonal anti-CD20) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registraron 80 interacciones. Entre las de gravedad mayor figuran deferiprona, samario (153Sm) lexidronam, adalimumab, baricitinib, certolizumab pegol, cladribina y clozapina. Entre las de gravedad moderada figuran estroncio-89, roflumilast, cloranfenicol, zidovudina, alemtuzumab, anakinra, azatioprina, canakinumab y varias vacunas (toxoide tetánico, ántrax, cólera vivo). En general, destacan los fármacos inmunosupresores o mielosupresores y las vacunas, por lo que conviene revisar la medicación concomitante.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen varios ensayos de fase 2, incluidos aleatorizados y publicados (CALGB 50904 y el estudio en enfermedad refractaria a rituximab), que respaldan la actividad de ofatumumab en linfoma folicular a través de un mecanismo anti-CD20 directamente aplicable. No hay un ECA de fase 3 completado en esta indicación, por lo que el nivel es L2.

**Para avanzar se necesita:**
- Confirmar los datos de advertencias y contraindicaciones a partir del prospecto de la AEMPS, que no estaban disponibles.
- Obtener los datos detallados del mecanismo de acción desde DrugBank.
- Aclarar el estado y resultados del ensayo de fase 3 NCT01077518 (terminado, ofatumumab + bendamustina).
- Verificar que la presentación comercializada en España (Kesimpta, pluma precargada de 20 mg) no corresponde a la formulación intravenosa usada en los ensayos oncológicos, por lo que habría que evaluar la compatibilidad de vía y dosis.
- Plan de monitoreo de seguridad (infecciones, reactivación de hepatitis B, vacunaciones) y revisión de las interacciones farmacológicas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

