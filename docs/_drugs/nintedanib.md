---
layout: default
title: Nintedanib
parent: Solo predicción del modelo (L5)
nav_order: 568
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-20
monitor_inn: "NINTEDANIB"
predicted_indications: ["dermatofibrosarcoma protuberans", "liposarcoma", "ovarian myxoid liposarcoma"]
description: "Nintedanib: nueva indicación predicha, Dermatofibrosarcoma protuberans (nivel de evidencia L5). En España, autorizaciones de la AEMPS: al menos 20"
---

# Nintedanib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Nintedanib: Dermatofibrosarcoma protuberans
{: .text-alpha }

## Resumen en Una Frase

Nintedanib es un inhibidor de tirosina quinasas de múltiples dianas, utilizado originalmente para el cáncer de pulmón no microcítico y la fibrosis pulmonar idiopática.
El modelo TxGNN predice que podría ser efectivo para **dermatofibrosarcoma protuberans (DFSP)**,
pero actualmente solo hay **0 ensayos clínicos** y **1 publicación** (una revisión indirecta sobre inhibidores de PDGFR) que respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Dermatofibrosarcoma protuberans |
| Puntaje de Predicción TxGNN | 0.9915 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 17; autorizadas no comercializadas: 3) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Nintedanib (traducción no oficial): «El nintedanib es una molécula pequeña que inhibe múltiples receptores tirosina cinasa (RTK) y tirosina cinasas no receptoras (nRTK). El nintedanib inhibe los siguientes RTK: receptor del factor de crecimiento derivado de plaquetas (PDGFR) α y β, receptor del factor de crecimiento de fibroblastos (FGFR) 1-3, receptor del factor de crecimiento endotelial vascular (VEGFR) 1-3, receptor del factor estimulante de colonias 1 (CSF1R) y tirosina cinasa 3 similar a Fms (FLT-3).» Texto original en inglés: "Nintedanib is a small molecule that inhibits multiple receptor tyrosine kinases (RTKs) and non-receptor tyrosine kinases (nRTKs). Nintedanib inhibits the following RTKs: platelet-derived growth factor receptor (PDGFR) α and β, fibroblast growth factor receptor (FGFR) 1-3, vascular endothelial growth factor receptor (VEGFR) 1-3, colony stimulating factor 1 receptor (CSF1R), and Fms-like tyrosine kinase-3 (FLT-3)." ([DailyMed: Nintedanib Capsules, 100 Mg And 150 Mg (nintedanib) prescribing information, EXELAN PHARMACEUTICALS INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=60d8104e-cb6c-4f4f-8159-95ed57346ffa), versión del 2026-04-21; consultado el 2026-11-19). Según la información conocida, nintedanib es un inhibidor multidiana de tirosina quinasas que bloquea PDGFR-alfa/beta, FGFR1-3 y VEGFR1-3. Su eficacia en cáncer de pulmón no microcítico y fibrosis pulmonar idiopática está reconocida, y mecanísticamente podría ser aplicable al DFSP.

El DFSP está impulsado por la fusión génica COL1A1-PDGFB, que provoca una activación constitutiva de la señalización de PDGFR-beta. Dado que nintedanib inhibe esta vía, existe una justificación mecanística plausible. La conexión con las indicaciones originales radica en las vías compartidas de crecimiento y angiogénesis (PDGFR/VEGFR/FGFR), implicadas tanto en el crecimiento tumoral como en la fibrosis.

Conviene ser prudente: la única literatura disponible es una revisión de 2018 sobre inhibidores de PDGFR de molécula pequeña (como imatinib), que constituye evidencia indirecta de clase. No hay demostración de que nintedanib se haya probado en DFSP. Además, imatinib es el comparador establecido dirigido a PDGFR, lo que fija un listón alto para cualquier nuevo agente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Revisión | Pharmacological Research | Revisión del papel de los inhibidores de molécula pequeña de PDGFR en trastornos neoplásicos; evidencia indirecta para la clase de inhibidores de PDGFR, no específica de nintedanib |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 114979004 | OFEV 150 mg cápsulas blandas | Cápsula blanda | No disponible |
| 114979002 | OFEV 100 mg cápsulas blandas | Cápsula blanda | No disponible |
| 114954004 | VARGATEF 150 mg cápsulas blandas | Cápsula blanda | No disponible |
| 114954003 | VARGATEF 100 mg cápsulas blandas | Cápsula blanda | No disponible |
| 89430 | Nintedanib Teva 100 mg cápsulas blandas EFG | Cápsula blanda | No disponible |

Se muestran 5 de las 20 autorizaciones vigentes (todas de medicamentos con un único principio activo, ninguna cancelada); el resto corresponde a genéricos de otros titulares.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasas múltiples) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto (típicamente función hepática y hemograma) |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las principales:
  - **Mayor**: dexametasona.
  - **Moderadas**: ácido acetilsalicílico, claritromicina, naltrexona, rolapitant, cobicistat, y varios antitrombóticos/anticoagulantes (abciximab, alteplasa, antitrombina III, apixabán, dipiridamol, betrixabán, bivalirudina, cangrelor, caplacizumab, cilostazol, clopidogrel, dalteparina, defibrótido, desirudina), lo que sugiere vigilar el riesgo hemorrágico.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (0,9915) y una base mecanística plausible (PDGFR-beta en DFSP), pero la evidencia es solo indirecta (una revisión de clase), sin ensayos clínicos y con imatinib como comparador establecido. Es una pregunta de investigación más que una candidata lista para avanzar.

**Para avanzar se necesita:**
- Datos de estudios preclínicos de nintedanib en modelos de DFSP (líneas celulares con fusión COL1A1-PDGFB).
- Datos detallados del mecanismo de acción (MOA) y comparación con imatinib.
- Advertencias y contraindicaciones del prospecto de la AEMPS (actualmente sin datos).
- Evaluación de seguridad, en particular del riesgo hemorrágico y de las interacciones identificadas.

**Otras predicciones (evidencia solo de modelo, nivel L5, decisión Hold):** liposarcoma (0.9913) y liposarcoma mixoide de ovario (0.9912). No hay ensayos ni literatura, y la relación mecanística con las dianas de nintedanib no es específica.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Nintedanib Capsules, 100 Mg And 150 Mg (nintedanib) prescribing information, EXELAN PHARMACEUTICALS INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=60d8104e-cb6c-4f4f-8159-95ed57346ffa) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

