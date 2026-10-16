---
layout: default
title: Vismodegib
parent: Solo predicción del modelo (L5)
nav_order: 854
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Vismodegib: nueva indicación predicha, Meduloblastoma con nodularidad extensa (nivel de evidencia L5). Indicación original: Carcinoma cutáneo (carcinoma basocelular). El texto de indicación de…"
monitor_inn: "VISMODEGIB"
predicted_indications: ["medulloblastoma with extensive nodularity", "xeroderma pigmentosum", "annular epidermolytic ichthyosis", "epidermolysis bullosa simplex with mottled pigmentation", "prostate cancer/brain cancer susceptibility", "Brenner tumor", "cutaneous adenocystic carcinoma", "prostate leiomyoma", "skin cancer", "benign neoplasm of sweat gland"]
---

# Vismodegib
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

# Vismodegib: De Carcinoma Cutáneo a Meduloblastoma con Nodularidad Extensa

## Resumen en Una Frase

Vismodegib es un inhibidor de la vía Hedgehog (bloquea la proteína Smoothened, SMO), utilizado originalmente para tratar el carcinoma basocelular y otros carcinomas cutáneos.
El modelo TxGNN predice que podría ser efectivo para **meduloblastoma con nodularidad extensa**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Carcinoma cutáneo (carcinoma basocelular). El texto de indicación de la autorización española no está disponible, por lo que se toma de las indicaciones originales del grafo de conocimiento |
| Nueva Indicación Predicha | Meduloblastoma con nodularidad extensa |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

El meduloblastoma con nodularidad extensa suele asociarse al subgrupo molecular SHH. En este subgrupo la activación de la vía Hedgehog, por mutaciones en PTCH1 o SUFU, impulsa el desarrollo del tumor. Vismodegib inhibe SMO, un componente central de esta vía, por lo que existe plausibilidad mecanística, sobre todo en la enfermedad dirigida por PTCH1 o SMO.

La indicación original (carcinoma basocelular) comparte con esta nueva indicación la dependencia de la señalización Hedgehog. Por eso el modelo establece la conexión, y el puntaje es muy alto (99.93%).

Hay limitaciones importantes:
- Los tumores con mutaciones en SUFU actúan por debajo de SMO y se espera que sean resistentes al fármaco.
- El uso pediátrico preocupa por el riesgo de cierre prematuro de las placas de crecimiento.
- No se dispone de datos detallados sobre el mecanismo de acción en las fuentes compiladas, y no hay estudios que respalden esta indicación concreta.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 113848001 | ERIVEDGE 150 MG CÁPSULAS DURAS (Roche Registration GmbH) | Cápsula dura | No disponible en los datos compilados |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de la vía Hedgehog / SMO) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto. Los datos compilados señalan como puntos a vigilar la toxicidad embriofetal, los espasmos musculares, la alopecia, la disgeusia y la pérdida de peso |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registran 56 interacciones. Las 20 disponibles para esta revisión son de gravedad **menor**, salvo una **moderada**:
  - **Moderada**: claritromicina.
  - **Menor**: antiácidos y reductores de acidez gástrica, entre ellos famotidina, ranitidina, cimetidina, nizatidina, omeprazol, esomeprazol, lansoprazol, dexlansoprazol, pantoprazol, rabeprazol, hidróxido de aluminio, carbonato de calcio, óxido, carbonato e hidróxido de magnesio, magaldrato, citrato de sodio y bicarbonato de sodio.
- **Consideraciones específicas de esta indicación**:
  - Posible cierre prematuro de las placas de crecimiento en población pediátrica, relevante porque el meduloblastoma es frecuente en niños.
  - Resistencia esperada en tumores con mutaciones en SUFU.
  - Toxicidad embriofetal (teratogenicidad).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto y una base mecanística plausible en el subgrupo SHH, pero no hay ensayos clínicos ni literatura específica (nivel L5). Además, existen riesgos propios de la indicación: la resistencia en tumores con mutaciones en SUFU y la preocupación por el crecimiento óseo en niños.

**Para avanzar se necesita:**
- Estudios preclínicos o clínicos que evalúen vismodegib en meduloblastoma del subgrupo SHH, con selección por genotipo (PTCH1/SMO frente a SUFU).
- Datos detallados del mecanismo de acción y las advertencias y contraindicaciones del prospecto de la AEMPS.
- Una evaluación de seguridad en población pediátrica, en especial sobre el crecimiento óseo.
- Un plan de prevención del riesgo embriofetal y de gestión de las interacciones farmacológicas.

**Nota de contexto:** en los datos compilados, otras indicaciones predichas para este fármaco cuentan con más respaldo. El "cáncer de piel" corresponde esencialmente al uso ya aprobado (nivel L1, Proceed with Guardrails). La xeroderma pigmentosum tiene dos reportes de caso del uso de vismodegib para carcinomas basocelulares asociados (nivel L4).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

