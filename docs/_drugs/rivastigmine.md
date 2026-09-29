---
layout: default
title: Rivastigmine
parent: Evidencia moderada (L3-L4)
nav_order: 473
evidence_level: L4
indication_count: 1
---

# Rivastigmine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **1** 
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

# Rivastigmina: De Enfermedad de Alzheimer a Glaucoma

## Resumen en Una Frase

Rivastigmina es un inhibidor de la colinesterasa utilizado en el tratamiento de la enfermedad de Alzheimer (según los datos farmacológicos de la ficha; las autorizaciones españolas no incluyen el texto de indicación).
El modelo TxGNN predice que podría ser efectivo para **glaucoma**,
pero por ahora no hay **ningún ensayo clínico** registrado. Solo hay **3 publicaciones**, todas preclínicas, de revisión o *in silico*.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Alzheimer (según datos farmacológicos; sin texto de indicación en las autorizaciones) |
| Nueva Indicación Predicha | Glaucoma |
| Puntaje de Predicción TxGNN | 99.27% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Rivastigmina inhibe la acetilcolinesterasa (AChE, gen *ACHE*) y la butirilcolinesterasa (BChE, gen *BCHE*). Al frenar la degradación de la acetilcolina, aumenta el tono colinérgico. Además de la enfermedad de Alzheimer, los datos farmacológicos mencionan su posible utilidad en el deterioro cognitivo vascular y en la marcha de pacientes con Parkinson. No hay una descripción detallada del mecanismo de acción en el registro de origen, así que este razonamiento se basa en la clase del fármaco y en sus dianas conocidas.

En el segmento anterior del ojo, más acetilcolina podría provocar contracción del músculo ciliar y aumentar la salida de humor acuoso por la malla trabecular. Es el mismo principio de los mióticos clásicos, como la pilocarpina y la fisostigmina. Por eso la hipótesis es mecanísticamente plausible: la presión intraocular (PIO) elevada es el principal factor de riesgo modificable del glaucoma.

Esta conexión está respaldada solo por evidencia preclínica. Un estudio en conejos mostró que la rivastigmina tópica reduce la PIO. El puntaje TxGNN de 0.993 es una predicción del modelo y no constituye evidencia clínica. No hay datos en humanos sobre reducción de PIO, protección del nervio óptico ni seguridad ocular.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10673128](https://pubmed.ncbi.nlm.nih.gov/10673128/) | 2000 | Estudio preclínico en animales (conejo) | J Ocul Pharmacol Ther | La rivastigmina tópica, un inhibidor selectivo de la AChE, reduce la presión intraocular en conejos normotensos. |
| [27967267](https://pubmed.ncbi.nlm.nih.gov/27967267/) | 2017 | Revisión (literatura de patentes) | Expert Opin Ther Pat | Revisa inhibidores y reactivadores de la AChE. Indica que la inhibición leve de la AChE tiene relevancia terapéutica en Alzheimer, miastenia gravis y glaucoma. |
| [39130374](https://pubmed.ncbi.nlm.nih.gov/39130374/) | 2024 | Genética de sistemas / modelado molecular (*in silico*) | Front Mol Biosci | Analiza los agentes colinérgicos para reducir la PIO y señala que los agonistas M3 aprobados tienen efectos adversos colinérgicos sistémicos que limitan su uso. |

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones. El registro no incluye el texto de indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 98092005 | PROMETAX 3 mg CÁPSULAS DURAS | Cápsula dura |
| 76269 | RIVASTIGMINA VIR 4.5 MG CÁPSULAS DURAS EFG | Cápsula dura |
| 98066025 | EXELON 9,5 mg/24 H PARCHE TRANSDÉRMICO | Parche transdérmico |
| 09599015 | RIVASTIGMINA SANDOZ 6 mg CÁPSULAS DURAS EFG | Cápsula dura |
| 98066010 | EXELON 6 mg CÁPSULAS DURAS | Cápsula dura |

Las formas farmacéuticas registradas son cápsula dura, parche transdérmico y solución oral. No consta ninguna presentación oftálmica.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

No hay datos en humanos sobre la seguridad ocular de la rivastigmina tópica.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia es de nivel L4: un estudio preclínico en conejos y un análisis *in silico*, sin ensayos clínicos ni datos en humanos. La plausibilidad mecanística es buena, pero el puntaje TxGNN por sí solo no basta para avanzar. Por ahora es una pregunta de investigación.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), un vacío bloqueante para el cribado de seguridad
- Confirmar el mecanismo de acción en DrugBank
- Estudios preclínicos adicionales (otras especies, modelos de glaucoma, neuroprotección del nervio óptico)
- Evaluar la compatibilidad de la vía de administración, ya que no existe formulación oftálmica y las formas actuales son oral y transdérmica
- Datos de tolerabilidad y seguridad ocular de una formulación tópica antes de plantear un ensayo clínico en humanos
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

