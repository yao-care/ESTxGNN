---
layout: default
title: Miglustat
parent: Solo predicción del modelo (L5)
nav_order: 356
evidence_level: L5
indication_count: 10
---

# Miglustat
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

# Miglustat: De Enfermedad de Gaucher tipo 1 a Síndrome de ictiosis autosómica con curso mortal

## Resumen en Una Frase

Miglustat es un inhibidor de la glucosilceramida sintasa. Según la literatura del expediente (PMID 12808890), se desarrolló para la enfermedad de Gaucher tipo 1, porque los datos de AEMPS no incluyen el texto de indicación.
El modelo TxGNN predice como primera opción el **síndrome de ictiosis autosómica con curso mortal**, pero **sin ningún ensayo clínico ni publicación** que lo respalde (solo predicción del modelo).
Entre las 10 predicciones, solo la **enfermedad de Tay-Sachs** (posición 7) tiene evidencia real: **5 ensayos clínicos** y **20 publicaciones**.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de AEMPS (los 5 textos de indicación están vacíos). La literatura la sitúa en la enfermedad de Gaucher tipo 1 |
| Nueva Indicación Predicha | Síndrome de ictiosis autosómica con curso mortal |
| Puntaje de Predicción TxGNN | 99,83 % |
| Nivel de Evidencia | L5 (para la indicación predicha en primer lugar) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 7 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Miglustat inhibe la glucosilceramida sintasa, la enzima que inicia la síntesis de la mayoría de los glucoesfingolípidos. Por eso podría alterar el equilibrio de ceramidas y glucoesfingolípidos en la epidermis. Esta es la única base para la predicción de ictiosis, y el propio expediente la califica de **especulativa**.

La relación con la indicación original es débil. La ictiosis autosómica es un trastorno de la barrera cutánea, mientras que la enfermedad de Gaucher es un trastorno lisosomal por acumulación de glucosilceramida. No se encontró ningún ensayo ni publicación que una miglustat con esta enfermedad.

Otras predicciones tienen un vínculo más plausible, pero también sin evidencia clínica. Es el caso de las esfingolipidosis como la enfermedad de Krabbe, la leucodistrofia metacromática y la deficiencia de prosaposina. En varias predicciones el vínculo es inexistente o dudoso (deficiencia de lipasa ácida lisosomal, adenoma suprarrenal benigno, ictiosis ligada al X). Estas últimas parecen artefactos del grafo de conocimiento.

## Evidencia de Ensayos Clínicos y Literatura (predicción principal)

Actualmente no hay ensayos clínicos ni literatura relacionados con el síndrome de ictiosis autosómica con curso mortal.

## Predicción con Mayor Respaldo: Enfermedad de Tay-Sachs

**Puntaje TxGNN:** 99,75 % · **Nivel de evidencia:** L2 · **Estado:** pregunta de investigación

**Mecanismo.** Miglustat reduce la síntesis de los precursores del gangliósido GM2 (terapia de reducción de sustrato). Este es un fundamento directo para la deficiencia de HexA, y el fármaco atraviesa la barrera hematoencefálica. La evidencia clínica es mixta. Un ensayo aleatorizado de 12 meses en Tay-Sachs de inicio tardío no mostró un beneficio neurológico claro. En la forma infantil, los datos se limitan a estudios pequeños, abiertos o farmacocinéticos.

### Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03822013](https://clinicaltrials.gov/study/NCT03822013) | Fase 3 | Terminado | 30 | Efectos de miglustat sobre síntomas neurológicos y sistémicos en las formas infantiles de Sandhoff y Tay-Sachs. La terminación limita la interpretación |
| [NCT00672022](https://clinicaltrials.gov/study/NCT00672022) | Fase 3 | Completado | 10 | Farmacocinética, seguridad y tolerabilidad en GM2 de inicio infantil. No es un ensayo de eficacia |
| [NCT00418847](https://clinicaltrials.gov/study/NCT00418847) | Fase 2 | Completado | 5 | Farmacocinética y tolerabilidad en GM2 juvenil. Muestra muy pequeña |
| [NCT02030015](https://clinicaltrials.gov/study/NCT02030015) | Fase 4 | Terminado | 16 | Régimen Syner-G: miglustat más dieta cetogénica en gangliosidosis. El efecto propio de miglustat queda confundido |
| [NCT07399704](https://clinicaltrials.gov/study/NCT07399704) | Fase 2 | Reclutando | 21 | Estudio abierto a largo plazo de nizubaglustat (otro fármaco) en GM2 y Niemann-Pick C. Solo sirve como contexto |

### Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [19346952](https://pubmed.ncbi.nlm.nih.gov/19346952/) | 2009 | ECA | Genetics in Medicine | Estudio aleatorizado de 12 meses (más 24 de extensión) sobre seguridad y eficacia de miglustat en Tay-Sachs de inicio tardío |
| [37209042](https://pubmed.ncbi.nlm.nih.gov/37209042/) | 2023 | Revisión sistemática | European Journal of Neurology | Evalúa eficacia y seguridad de miglustat en GM2, ante resultados previos inconsistentes |
| [16434676](https://pubmed.ncbi.nlm.nih.gov/16434676/) | 2006 | Serie de casos | Neurology | En 2 pacientes infantiles no detuvo el deterioro neurológico. Hubo niveles significativos en LCR y se previno la macrocefalia |
| [16151419](https://pubmed.ncbi.nlm.nih.gov/16151419/) | 2005 | Reporte de caso | Bone Marrow Transplantation | Trasplante alogénico de médula seguido de terapia de reducción de sustrato en un niño con Tay-Sachs subagudo |
| [32867370](https://pubmed.ncbi.nlm.nih.gov/32867370/) | 2020 | Revisión | Int J Mol Sci | Características clínicas, fisiopatología y terapias actuales de las gangliosidosis GM2 |
| [30524313](https://pubmed.ncbi.nlm.nih.gov/30524313/) | 2018 | Revisión | Frontiers in Physiology | Nuevos enfoques terapéuticos para Tay-Sachs |
| [28476546](https://pubmed.ncbi.nlm.nih.gov/28476546/) | 2017 | Cohorte de historia natural | Mol Genet Metab | Cronología clínica de las gangliosidosis infantiles. Señala que miglustat está limitado por efectos gastrointestinales |
| [12808890](https://pubmed.ncbi.nlm.nih.gov/12808890/) | 2003 | Perfil de fármaco | Curr Opin Investig Drugs | Miglustat aprobado en la UE para Gaucher y en desarrollo para Tay-Sachs, Fabry y Niemann-Pick C |

## Información de Mercado en España

Hay 7 autorizaciones en total. Se muestran 5 (los datos de AEMPS no incluyen el texto de indicación aprobada).

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1171176001 | YARGESA 100 MG CÁPSULAS DURAS EFG | Cápsula dura | No disponible |
| 90992 | MIGLUSTAT WAYMADE 100 MG CÁPSULAS EFG | Cápsula dura | No disponible |
| 02238001 | ZAVESCA 100 MG CÁPSULAS DURAS | Cápsula dura | No disponible |
| 1231737001 | OPFOLDA 65 MG CÁPSULAS DURAS | Cápsula dura | No disponible |
| 78987 | MIGLUSTAT ACCORD 100 MG CÁPSULAS DURAS EFG | Cápsula dura | No disponible |

## Consideraciones de Seguridad

Consultar el prospecto para la información de advertencias y contraindicaciones, que no está disponible en el expediente. No se encontraron interacciones farmacológicas registradas.

El perfil conocido por la indicación comercializada incluye efectos gastrointestinales, pérdida de peso, temblor y neuropatía.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- La indicación predicha en primer lugar (ictiosis autosómica) solo tiene el puntaje del modelo, sin ensayos ni literatura y con un vínculo mecanístico especulativo.
- Tay-Sachs es la única predicción con evidencia real (L2), pero los resultados son mixtos y los ensayos son pequeños o terminados. Se justifica como pregunta de investigación, no como recomendación de tratamiento.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), un vacío bloqueante para el cribado de seguridad.
- Obtener los textos de indicación aprobada de cada autorización.
- Completar los datos de mecanismo de acción desde DrugBank.
- Para Tay-Sachs, revisar en detalle la revisión sistemática (PMID 37209042) y las razones de terminación de NCT03822013 y NCT02030015.
- Decidir si se prioriza Tay-Sachs sobre la predicción de mayor puntaje, dado que esta última carece de evidencia.

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

