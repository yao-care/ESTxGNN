---
layout: default
title: Insulin Detemir
parent: Evidencia alta (L1-L2)
nav_order: 281
evidence_level: L1
indication_count: 10
---

# Insulin Detemir
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **10** 
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

# Insulina detemir: De Indicación Original No Registrada a Diabetes Mellitus Tipo 1

## Resumen en Una Frase

La insulina detemir (Levemir) es una insulina basal de acción prolongada, comercializada en España por Novo Nordisk. El registro de AEMPS de este paquete de evidencia no incluye el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectiva para la **diabetes mellitus tipo 1**, con **50 ensayos clínicos** y **19 publicaciones** que respaldan esta dirección.
Esta predicción coincide con un uso ya comercializado, por lo que en la práctica no es un reposicionamiento.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Diabetes mellitus tipo 1 |
| Puntaje de Predicción TxGNN | 99.77% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank para este paquete. Según la literatura recuperada, la insulina detemir es un análogo soluble de la insulina humana, acilado con un ácido graso de 14 carbonos. Tras la inyección subcutánea se une de forma reversible a la albúmina, lo que produce una absorción lenta y un efecto metabólico prolongado de hasta 24 horas. Actúa sobre el receptor de insulina y sustituye la insulina basal endógena que falta.

En la diabetes tipo 1 el páncreas deja de producir insulina, y el tratamiento de base es reponerla. Por eso la predicción es mecanísticamente coherente: la insulina detemir cumple esa función como insulina basal dentro de un régimen basal-bolo. Se trata de un uso comercializado, no de un hallazgo nuevo. La ausencia de indicación original en el registro es una laguna de datos, no una señal de que el uso sea nuevo.

---

## Evidencia de Ensayos Clínicos

Se identificaron 50 ensayos; se muestran los 10 más relevantes para diabetes tipo 1.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00595374](https://clinicaltrials.gov/study/NCT00595374) | Fase 3 | Completado | 114 | Detemir + aspart frente a NPH + aspart en adultos con DM1: eficacia y seguridad en el control glucémico |
| [NCT00312104](https://clinicaltrials.gov/study/NCT00312104) | Fase 3 | Completado | 325 | Detemir dos veces al día frente a glargina una vez al día, ambas con aspart, en DM1 |
| [NCT01697657](https://clinicaltrials.gov/study/NCT01697657) | Fase 3 | Completado | 131 | Cruzado: frecuencia de hipoglucemias con detemir frente a NPH en DM1 bien controlada |
| [NCT00271284](https://clinicaltrials.gov/study/NCT00271284) | Fase 3 | Completado | 88 | Cruzado: variabilidad de la glucemia en ayunas con glargina o detemir, combinadas con glulisina, en DM1 |
| [NCT01513473](https://clinicaltrials.gov/study/NCT01513473) | Fase 3 | Completado | 350 | Degludec frente a detemir en niños y adolescentes con DM1 (detemir como comparador) |
| [NCT00605137](https://clinicaltrials.gov/study/NCT00605137) | Fase 3 | Completado | 83 | Seguridad de detemir frente a NPH en niños con DM1 (Japón) |
| [NCT01831765](https://clinicaltrials.gov/study/NCT01831765) | Fase 3 | Completado | 1290 | FIAsp frente a aspart, ambas con detemir como insulina basal de fondo en adultos con DM1 |
| [NCT01461616](https://clinicaltrials.gov/study/NCT01461616) | Fase 3 | Completado | 19 | Triple cruzado NPH, detemir y glargina: efecto sobre IGFBP-1 e IGF-I en DM1 |
| [NCT00542399](https://clinicaltrials.gov/study/NCT00542399) | Fase 4 | Completado | 50 | Detemir una frente a dos veces al día en niños y adolescentes con DM1 |
| [NCT00704574](https://clinicaltrials.gov/study/NCT00704574) | N/A | Completado | 159 | Estudio observacional (PREDICTIVE Youth): reacciones adversas graves con detemir en menores con DM1 |

**Nota:** en varios de estos ensayos la detemir es solo el comparador o la insulina basal de fondo (NCT01831765, NCT01513473). Por eso respaldan su uso y seguridad, pero no siempre miden su eficacia de forma directa.

---

## Evidencia de Literatura

Se recuperaron 19 publicaciones; se muestran 10 (ECA y metaanálisis primero, luego revisiones).

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | ECA | Lancet Diabetes Endocrinol | Estudio EXPECT: degludec frente a detemir, ambas con aspart, en embarazadas con DM1 (no inferioridad) |
| [21878861](https://pubmed.ncbi.nlm.nih.gov/21878861/) | 2011 | Revisión sistemática y metaanálisis | Pol Arch Med Wewn | Compara detemir con NPH en DM1; los beneficios de la detemir no fueron confirmados por todos los estudios |
| [33662147](https://pubmed.ncbi.nlm.nih.gov/33662147/) | 2021 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Análogos de insulina de acción (ultra)prolongada en DM1: beneficio sobre complicaciones e hipoglucemia |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Metaanálisis en red | Value Health | Eficacia y seguridad relativas de las pautas de insulina basal en adultos con DM1 |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | Revisión sistemática y metaanálisis | Clin Ther | Degludec frente a otras insulinas basales (glargina, detemir) en DM1 y DM2 |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Revisión | Lancet Diabetes Endocrinol | Manejo de la DM1 en el embarazo: estilo de vida, tratamiento farmacológico y tecnologías |
| [17326333](https://pubmed.ncbi.nlm.nih.gov/17326333/) | 2006 | Revisión | Vasc Health Risk Manag | La detemir se une a la albúmina, con perfil farmacocinético menos variable; puede reducir el riesgo de hipoglucemia, sobre todo nocturna |
| [15516157](https://pubmed.ncbi.nlm.nih.gov/15516157/) | 2004 | Revisión | Drugs | Efecto más predecible y consistente que NPH, con menor variabilidad intraindividual, hasta 24 horas |
| [20539842](https://pubmed.ncbi.nlm.nih.gov/20539842/) | 2010 | Revisión | Vasc Health Risk Manag | La detemir es una opción eficaz en DM1 y DM2, con menor tasa de hipoglucemias |
| [23243636](https://pubmed.ncbi.nlm.nih.gov/23243636/) | 2012 | Revisión | Drugs Today (Barc) | Análogos de insulina en DM1 de niños y adolescentes; la detemir es uno de los dos análogos de acción prolongada aprobados |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 04278005 | LEVEMIR FLEXPEN 100 U/ML SOLUCION INYECTABLE EN UNA PLUMA PRECARGADA | Solución inyectable en pluma precargada | Novo Nordisk A/S |
| 04278008 | LEVEMIR INNOLET 100 U/ML SOLUCION INYECTABLE EN UNA PLUMA PRECARGADA | Solución inyectable en pluma precargada | Novo Nordisk A/S |

El registro no incluye el texto de la indicación aprobada.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en las fuentes consultadas.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay varios ensayos de Fase 3 completados en diabetes tipo 1 (frente a NPH, glargina y degludec), además de metaanálisis y revisiones, lo que cumple el criterio de nivel L1. Los guardarraíles son necesarios porque en varios ensayos la detemir actúa solo como comparador o tratamiento de fondo, y porque faltan los datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), pendiente para el cribado de seguridad.
- Confirmar la indicación aprobada de Levemir en España y consultar el mecanismo de acción en DrugBank.
- Definir los guardarraíles clínicos: riesgo de hipoglucemia, dosificación individualizada y rotación de sitios de inyección.
- Ejecutar una revisión formal de la literatura que priorice los ECA con detemir como brazo de estudio, no como comparador.

**Otras predicciones del modelo:** las nueve restantes (por ejemplo, ooforitis autoinmune, síndrome de la persona rígida, lipodistrofias) están en nivel L5 y se recomiendan como Hold. La agenesia pancreática se marca como pregunta de investigación: la reposición de insulina es coherente, pero no hay evidencia recuperada. La lipodistrofia localizada inducida por fármacos es una señal de seguridad de las insulinas inyectadas, no un objetivo terapéutico.

---

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

