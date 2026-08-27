---
layout: default
title: Alprazolam
parent: 僅模型預測 (L5)
nav_order: 20
evidence_level: L5
indication_count: 3
---

# Alprazolam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Alprazolam: De Trastorno de Panico y Ansiedad a Insomnio

---

## Resumen en Una Frase

Alprazolam es una benzodiazepina cuyo uso clinico establecido, documentado ampliamente en la literatura incluida en este paquete de evidencia, es el tratamiento del trastorno de panico y la ansiedad generalizada (con o sin agorafobia). El modelo TxGNN predice que podria ser efectivo tambien para **Insomnio**, con **7 ensayos clinicos** y **18 publicaciones** que actualmente rodean esta direccion, aunque gran parte de esa evidencia es indirecta o corresponde a otros farmacos de la misma clase.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Trastorno de panico y ansiedad generalizada (uso clinico ampliamente documentado en la literatura; no existe ficha tecnica registrada en Espana dentro de este informe) |
| Nueva Indicacion Predicha | Insomnio |
| Puntaje de Prediccion TxGNN | 99.81% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Espana | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Proceed with Guardrails |

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de una ficha de mecanismo de accion (MOA) formal en DrugBank para este candidato. Sin embargo, la informacion clinica y farmacologica recogida en el paquete de evidencia describe que alprazolam es una triazolobenzodiazepina de alta potencia que actua sobre el sitio de union de benzodiazepinas del receptor GABA-A, potenciando la neurotransmision inhibitoria mediada por GABA. Esta accion produce efectos sedante-hipnoticos, ansioliticos y relajantes musculares, propiedades farmacologicas compartidas por toda la clase de las benzodiazepinas.

Su indicacion original —el tratamiento del trastorno de panico y la ansiedad generalizada, con frecuencia asociado a agorafobia— comparte con el insomnio una base fisiopatologica comun: la hiperactivacion del sistema nervioso central y la desregulacion del eje GABAergico. Es habitual que los pacientes con trastornos de ansiedad presenten insomnio comorbido, y viceversa, lo que hace plausible que un farmaco ansiolitico eficaz module tambien la arquitectura del sueno.

No obstante, alprazolam no actua de forma selectiva sobre la subunidad GABA-A α1, la mas relacionada con la regulacion del sueño (a diferencia de hipnoticos especificos como zolpidem o zopiclona). Por ello, su efecto sedante viene acompañado de mayor riesgo de sedacion residual diurna, tolerancia, dependencia y sintomas de abstinencia, lo que explica que no sea un tratamiento de primera linea recomendado por las guias clinicas para el insomnio, incluso si mecanisticamente resulta plausible.

---

## Evidencia de Ensayos Clinicos

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00266409](https://clinicaltrials.gov/study/NCT00266409) | Fase 4 | Completado | 418 | Ensayo abierto multicentrico con Niravam® (alprazolam) que compara el tiempo de respuesta de los sintomas de ansiedad al anadir un ISRS/IRSN frente a ISRS/IRSN solo, en TAG o trastorno de panico; relevancia moderada, titulo truncado no confirma intervencion exacta. |
| [NCT01584440](https://clinicaltrials.gov/study/NCT01584440) | Fase 2 | Completado | 220 | Estudio doble ciego controlado con placebo de AVP-923 (dextrometorfano/quinidina) para agitacion en Alzheimer; no evalua alprazolam directamente, relevancia indirecta. |
| [NCT04572750](https://clinicaltrials.gov/study/NCT04572750) | No aplica | Completado | 170 | Intervencion electronica de autogestion para promover el cese de benzodiazepinas (incluye alprazolam); explora la direccion opuesta (deshabituacion, no tratamiento del insomnio). |
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | No aplica | Desconocido | 1400 | Cohorte prospectiva taiwanesa sobre riesgo-beneficio de hipnoticos en poblacion geriatrica; puede incluir datos reales de uso de alprazolam en insomnio, pero es observacional y su estado actual es incierto. |
| [NCT03327506](https://clinicaltrials.gov/study/NCT03327506) | Fase 4 | Desconocido | 128 | Compara hipnosis frente a premedicacion con alprazolam para la ansiedad perioperatoria en cirugia ginecologica; relevancia baja para insomnio. |
| [NCT01893632](https://clinicaltrials.gov/study/NCT01893632) | Fase 2 | Terminado | 2 | Evalua gabapentina (no alprazolam) para la dependencia de benzodiazepinas; terminado prematuramente por dificultad de reclutamiento. |
| [NCT01146600](https://clinicaltrials.gov/study/NCT01146600) | Fase 2 | Completado | 26 | Evalua claritromicina (no alprazolam) para la hipersomnia; no relacionado con la hipotesis de reposicionamiento. |

---

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33403184](https://pubmed.ncbi.nlm.nih.gov/33403184/) | 2020 | Estudio comparativo/cohorte | Cureus | Comparacion de alprazolam frente a melatonina para trastornos del sueno en pacientes en hemodialisis. |
| [39183410](https://pubmed.ncbi.nlm.nih.gov/39183410/) | 2024 | ECA | Medicine | Terapia integrativa (moxibustion del meridiano Du + acupuntura auricular) frente a alprazolam (grupo control) en pacientes con cardiopatia coronaria e insomnio. |
| [37801512](https://pubmed.ncbi.nlm.nih.gov/37801512/) | 2023 | Estudio mecanistico/preclinico | Aging | La administracion repetida de alprazolam en ratones causa disfuncion mitocondrial y deterioro de la consolidacion de memoria dependiente del hipocampo; relevante para la seguridad del uso cronico. |
| [37984023](https://pubmed.ncbi.nlm.nih.gov/37984023/) | 2024 | Revision | Value in Health Regional Issues | Analisis de tendencias y carga economica del uso de benzodiazepinas, incluyendo el insomnio como indicacion frecuente, mediante un modelo predictivo a 10 anos. |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Meta-analisis | Acta Pharmaceutica | Revision sistematica de terapias tranquilizantes (incluidas benzodiazepinas) en pacientes geriatricos con enfermedades cronicas. |
| [25532388](https://pubmed.ncbi.nlm.nih.gov/25532388/) | 2014 | Estudio transversal (real-world) | China J. Chinese Materia Medica | Analisis de comorbilidades y patrones de uso de medicamentos (MTC y occidental) en pacientes con insomnio en 20 hospitales chinos. |
| [38363887](https://pubmed.ncbi.nlm.nih.gov/38363887/) | 2024 | Cohorte transversal | Medicine | Estudio transversal sobre el insomnio en supervivientes de COVID-19 y sus factores asociados. |
| [35041261](https://pubmed.ncbi.nlm.nih.gov/35041261/) | 2022 | ECA | Brain and Behavior | Efectos de eszopiclona (farmaco de referencia, no alprazolam) sobre la calidad del sueno y la funcion cognitiva en ancianos con Alzheimer y trastorno del sueno. |
| [35493764](https://pubmed.ncbi.nlm.nih.gov/35493764/) | 2022 | Cohorte | JHEP Reports | La deprescripcion de zolpidem (no alprazolam) reduce caidas y fracturas en pacientes con cirrosis; referencia indirecta sobre el manejo de hipnosedantes en poblaciones vulnerables. |
| [39295670](https://pubmed.ncbi.nlm.nih.gov/39295670/) | 2024 | Reporte de caso | Cureus | Tratamiento homeopatico individualizado en un paciente con insomnio persistente y trastorno de ansiedad generalizada comorbido; evidencia de muy bajo nivel. |

---

## Informacion de Mercado en Espana

Segun los datos disponibles, alprazolam **no se encuentra actualmente comercializado en Espana** (0 autorizaciones registradas). No hay informacion de producto, forma farmaceutica ni indicacion aprobada que resumir en este momento.

---

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

---

## Conclusion y Proximos Pasos

**Decision: Proceed with Guardrails**

**Justificacion:**
- La evidencia disponible para insomnio corresponde a nivel L2 (respaldo mecanistico solido de la clase de benzodiazepinas y algunos estudios clinicos relacionados), pero la mayoria de los ensayos y publicaciones son indirectos, corresponden a otros farmacos, o exploran la direccion opuesta (deshabituacion). El perfil de riesgo (sedacion residual, tolerancia, dependencia) impide una recomendacion "Go" sin controles adicionales.

**Para avanzar se necesita:**
- Ficha tecnica/prospecto con advertencias y contraindicaciones (actualmente bloqueante para la evaluacion inicial de seguridad S1)
- Datos formales de mecanismo de accion (MOA) desde DrugBank
- Confirmacion de disponibilidad y estado regulatorio de alprazolam en Espana
- Evaluacion especifica del riesgo de dependencia y sedacion residual en un uso prolongado orientado al insomnio, dado que no es tratamiento de primera linea segun las guias clinicas actuales
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

