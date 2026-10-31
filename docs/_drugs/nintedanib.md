---
layout: default
title: Nintedanib
parent: Solo predicción del modelo (L5)
nav_order: 568
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-31
monitor_inn: "NINTEDANIB"
predicted_indications: ["dermatofibrosarcoma protuberans", "liposarcoma", "ovarian myxoid liposarcoma"]
description: "Nintedanib: nueva indicación predicha, Dermatofibrosarcoma protuberans (nivel de evidencia L5). Indicación original: No consta en los datos locales"
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
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 17) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos compilada. Según la información conocida, nintedanib es un inhibidor multidiana de tirosina quinasas que bloquea PDGFR-alfa/beta, FGFR1-3 y VEGFR1-3. Su eficacia en cáncer de pulmón no microcítico y fibrosis pulmonar idiopática está reconocida, y mecanísticamente podría ser aplicable al DFSP.

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
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

