---
layout: default
title: Acitretin
parent: Evidencia moderada (L3-L4)
nav_order: 21
evidence_level: L3
indication_count: 4
---

# Acitretin
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **4** 
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

# Acitretina: De Indicación No Especificada en la Ficha Regulatoria a Acné

## Resumen en Una Frase

Acitretina es un retinoide oral de segunda generación comercializado en España; los datos compilados no incluyen el texto de su indicación aprobada (en la práctica clínica se usa sobre todo en psoriasis y trastornos de queratinización, según la literatura revisada).
El modelo TxGNN predice que podría ser efectivo para **acné (enfermedad)**, con **1 ensayo clínico** y **18 publicaciones** relacionados, aunque la evidencia más sólida se refiere a la hidradenitis supurativa (acné inverso) y no al acné vulgar.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Acné (enfermedad) |
| Puntaje de Prediccion TxGNN | 99.94% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | ✓ Comercializado |
| Numero de Autorizaciones | 4 |
| Decision Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Acitretina es un retinoide oral de segunda generación que modula la diferenciación y proliferación de los queratinocitos y tiene efectos antiinflamatorios. Actualmente no se dispone de datos detallados del mecanismo de acción en las fuentes compiladas, pero esta descripción general de clase es coherente con la literatura revisada.

Los retinoides reducen la actividad de las glándulas sebáceas y la hiperqueratinización folicular, procesos centrales en la patogenia del acné. Sin embargo, el retinoide de referencia para el acné noduloquístico es la isotretinoína, no la acitretina. La señal más fuerte en los datos corresponde al acné inverso / hidradenitis supurativa (HS), una enfermedad de oclusión folicular distinta del acné vulgar.

El puntaje TxGNN de 0.999 probablemente refleja la pertenencia a la clase de los retinoides y la ontología compartida de enfermedades foliculares, más que evidencia directa en acné vulgar. La predicción debe interpretarse como una pregunta de investigación.

---

## Evidencia de Ensayos Clínicos

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT07708480](https://clinicaltrials.gov/study/NCT07708480) | Fase 4 | Completado | 70 | ECA que compara apremilast (30 mg dos veces al día) con acitretina (25 mg) durante 12 semanas en hidradenitis supurativa moderada-grave; variable principal: puntuación IHS4. No se dispone de resultados. Evidencia indirecta para acné vulgar. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [25640693](https://pubmed.ncbi.nlm.nih.gov/25640693/) | 2015 | Guía clínica | J Eur Acad Dermatol Venereol | Guía europea S1 para el tratamiento de la hidradenitis supurativa/acné inverso |
| [20874789](https://pubmed.ncbi.nlm.nih.gov/20874789/) | 2011 | Serie clínica | Br J Dermatol | Resultados a largo plazo de acitretina en hidradenitis supurativa |
| [12080949](https://pubmed.ncbi.nlm.nih.gov/12080949/) | 2002 | Reporte de caso | Cutis | Acné noduloquístico e hidradenitis supurativa tratados con acitretina |
| [28476075](https://pubmed.ncbi.nlm.nih.gov/28476075/) | 2017 | Revisión sistemática | Cochrane Database Syst Rev | Fármacos para el lupus eritematoso discoide |
| [40888828](https://pubmed.ncbi.nlm.nih.gov/40888828/) | 2025 | Revisión sistemática | Am J Clin Dermatol | Diferencias étnicas en la pustulosis palmoplantar |
| [41692081](https://pubmed.ncbi.nlm.nih.gov/41692081/) | 2026 | Revisión | Clin Dermatol | Vitamina A y retinoides en dermatología |
| [29234829](https://pubmed.ncbi.nlm.nih.gov/29234829/) | 2018 | Revisión | Hautarzt | Tratamiento farmacológico del acné inverso |
| [9074840](https://pubmed.ncbi.nlm.nih.gov/9074840/) | 1997 | Revisión | Drugs | Uso actual y potencial futuro de los retinoides en dermatología |
| [8573927](https://pubmed.ncbi.nlm.nih.gov/8573927/) | 1995 | Revisión | Dermatology | Retinoides y actividad de la glándula sebácea |
| [11586072](https://pubmed.ncbi.nlm.nih.gov/11586072/) | 2001 | Revisión | Skin Pharmacol Appl Skin Physiol | Indicaciones dermatológicas futuras de los retinoides |

---

## Información de Mercado en España

| Numero de Autorizacion | Nombre del Producto | Forma Farmaceutica | Indicacion Aprobada |
|---------|------|------|-----------|
| 60303 | NEOTIGASON 10 MG CAPSULAS DURAS | Cápsula dura | No disponible |
| 74726 | ACITRETINA IFC 25 mg CAPSULAS DURAS EFG | Cápsula dura | No disponible |
| 60302 | NEOTIGASON 25 MG CAPSULAS DURAS | Cápsula dura | No disponible |
| 74727 | ACITRETINA IFC 10 mg CAPSULAS DURAS EFG | Cápsula dura | No disponible |

---

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento TxGNN, no el prospecto):** insuficiencia hepática, daño hepático inducido por fármacos, pancreatitis, diabetes mellitus, cetoacidosis diabética, hipertrigliceridemia, hipoalfalipoproteinemia, obesidad, trastornos de ansiedad, trastornos neuróticos, trastorno distímico, abuso/dependencia de sustancias, pseudotumor cerebral, hipertensión intracraneal, trastornos de la visión, ceguera, ceguera nocturna (incluida la ceguera nocturna congénita estacionaria y la enfermedad de Oguchi) e hiperostosis.
- **Interacciones Farmacológicas:** se identificaron 113 interacciones. Las principales de nivel **Mayor** son doxiciclina, minociclina, tetraciclina y vitamina A. De nivel **Moderado**: sulfonilureas (acetohexamida, clorpropamida, glimepirida, glipizida, gliburida, tolazamida, tolbutamida) y naltrexona. Con nivel desconocido figuran, entre otros, omeprazol, pantoprazol, lansoprazol, simvastatina, rosuvastatina, morfina, vancomicina y triamcinolona.
- **Teratogenicidad:** la literatura y el análisis de los datos señalan a la acitretina como un potente teratógeno, contraindicado en el embarazo. Además, se destacan los riesgos de toxicidad hepática y ósea.

Consultar el prospecto para información de seguridad completa, ya que no se dispuso del texto de advertencias y contraindicaciones de la AEMPS.

---

## Conclusión y Próximos Pasos

**Decision: Hold**

**Justificación:**
La evidencia es de nivel L3 y se centra en la hidradenitis supurativa, no en el acné vulgar; el único ensayo (Fase 4) no tiene resultados disponibles. La isotretinoína es el retinoide de referencia en acné, y el perfil de seguridad de la acitretina (teratogenicidad, hepatotoxicidad) exige cautela.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), actualmente pendiente y bloqueante para el cribado de seguridad.
- Datos del mecanismo de acción desde DrugBank.
- Definir si la indicación objetivo es acné vulgar o hidradenitis supurativa, y obtener los resultados del ensayo NCT07708480.
- Evidencia comparativa frente a la isotretinoína en acné.
- Plan de gestión de riesgos (prevención del embarazo, monitorización hepática y lipídica).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

