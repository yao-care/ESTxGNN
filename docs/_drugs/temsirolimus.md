---
layout: default
title: Temsirolimus
parent: Evidencia moderada (L3-L4)
nav_order: 515
evidence_level: L3
indication_count: 3
---

# Temsirolimus
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **3** 
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

# Temsirolimus: Hacia una Nueva Indicación en Liposarcoma

## Resumen en Una Frase

Temsirolimus es un inhibidor de mTOR que está autorizado y comercializado en España en forma de solución para perfusión. El registro no recoge su indicación original.
El modelo TxGNN predice que podría ser efectivo para **liposarcoma**, con **5 ensayos clínicos** (solo uno prueba temsirolimus en sarcomas de forma directa y sin restringirse a población pediátrica) y **1 publicación** (una revisión) que respaldan esta dirección de forma indirecta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Liposarcoma |
| Puntaje de Predicción TxGNN | 99.54% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Temsirolimus es un inhibidor de mTOR. El registro no incluye una descripción detallada de su mecanismo de acción, pero este es el mecanismo establecido del fármaco. La vía PI3K/AKT/mTOR está activa en muchos sarcomas de tejidos blandos, incluido el liposarcoma. Bloquearla podría frenar el crecimiento tumoral, algo que los modelos en ratón ya han mostrado con la inhibición de mTOR.

El liposarcoma desdiferenciado también depende de la amplificación de CDK4/MDM2. Por eso varios ensayos combinan un inhibidor de mTOR con un inhibidor de CDK4/6, como el ensayo con ribociclib y everolimus. El puntaje alto de TxGNN (0.995) es coherente con esta biología, pero sigue siendo una predicción y no una prueba clínica.

El registro no incluye indicaciones originales del fármaco, por lo que no se puede analizar su relación con la nueva indicación. TxGNN también predice, con puntajes similares, dos entidades muy raras: liposarcoma mixoide de ovario (99.47%) y sarcoma de vulva (99.09%). Para ambas no hay ensayos ni literatura, así que tienen nivel L5 y la recomendación es Hold.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Fase 1/2 | Completado | 24 | Temsirolimus (Torisel) más doxorrubicina liposomal en sarcoma recurrente de tejidos blandos y hueso. Busca una dosis segura y valora la eficacia. Es el más directo, pero pequeño y no específico de liposarcoma. |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Fase 2 | Completado | 46 | Cixutumumab más temsirolimus en tumores sólidos pediátricos recurrentes o refractarios, incluido sarcoma. El liposarcoma es raro en esta población. |
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Fase 2 | Completado | 70 | Sirolimus más ciclofosfamida en liposarcoma mixoide y condrosarcoma metastásicos o irresecables. Es otro inhibidor de mTOR, por lo que aporta evidencia de clase. |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Fase 2 | Completado | 216 | Ridaforolimus (inhibidor de mTOR) en sarcoma avanzado. Respalda la lógica de clase, pero no es evidencia directa de temsirolimus. |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Fase 2 | Activo, sin reclutar | 48 | Ribociclib más everolimus en liposarcoma desdiferenciado y leiomiosarcoma avanzados. Se dirige a la enfermedad correcta, pero con everolimus. |

El registro no incluye resultados de eficacia de estos ensayos, así que la tabla resume solo sus diseños.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Revisión | Bulletin du cancer | Revisión de tratamientos dirigidos en sarcomas y tumores raros del tejido conectivo. Los agrupa en seis subgrupos según sus alteraciones moleculares. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 86058 | Temsirolimus Accord 30 mg (Accord Healthcare S.L.U.) | Concentrado y disolvente para solución para perfusión |
| 07424001 | Torisel 30 mg (Pfizer Europe Ma Eeig) | Concentrado y disolvente para solución para perfusión |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de mTOR) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto y seguir la normativa local de manejo de antineoplásicos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. El registro no contiene advertencias ni contraindicaciones, y no se encontraron interacciones farmacológicas.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia es sobre todo indirecta: hay pocos datos con temsirolimus y el resto procede de otros inhibidores de mTOR. Además, faltan los datos de seguridad de la ficha técnica de la AEMPS, lo que bloquea el cribado de seguridad.

**Para avanzar se necesita:**
- Obtener advertencias y contraindicaciones del prospecto de la AEMPS.
- Revisar los resultados y el desglose por subtipo de NCT00949325, el ensayo más directo.
- Completar los datos de mecanismo de acción (MOA) e indicaciones originales.
- Buscar estudios específicos de liposarcoma con temsirolimus, preferiblemente de Fase 2/3.
- Evaluar la compatibilidad de la vía de administración y la relación con la indicación original, hoy pendientes.

*Los resultados son solo de referencia para la investigación y no constituyen consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

