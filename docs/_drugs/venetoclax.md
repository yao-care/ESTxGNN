---
layout: default
title: Venetoclax
parent: Solo predicción del modelo (L5)
nav_order: 842
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-28
monitor_inn: "VENETOCLAX"
predicted_indications: ["Hodgkins lymphoma", "chronic myelogenous leukemia, BCR-ABL1 positive", "Ewing sarcoma", "follicular lymphoma", "metastatic neoplasm", "malignant spiradenoma"]
description: "Venetoclax: nueva indicación predicha, Hodgkins lymphoma (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Venetoclax
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Venetoclax: Hodgkins lymphoma
{: .text-alpha }

## Resumen en Una Frase

Venetoclax es un inhibidor oral de la proteína BCL-2. En la base de conocimiento del modelo figura asociado a la leucemia linfoblástica aguda y al síndrome de Richter.
El modelo TxGNN predice que podría ser efectivo para la **leucemia linfocítica crónica/linfoma linfocítico pequeño (LLC/LLP) de origen pregerminal (IGHV no mutado)**.
Esta predicción cuenta con **0 ensayos clínicos** y **1 publicación** (una revisión sobre biología del receptor de células B), por lo que la evidencia directa es muy limitada.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Hodgkins lymphoma |
| Puntaje de Predicción TxGNN | 0.9951 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 5 de 5) |
| Número de Autorizaciones | 5 (vigentes: 5) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Venetoclax actúa inhibiendo BCL-2, una proteína que impide la muerte celular programada (apoptosis). Las células de LLC dependen mucho de BCL-2 para sobrevivir, por lo que bloquearla restablece la apoptosis en las células tumorales. En los datos compilados para este informe no consta una descripción detallada del mecanismo de acción del fármaco. Esta explicación se basa en el conocimiento general de la clase y en la justificación mecanística asociada a la predicción.

La nueva indicación predicha no es una enfermedad distinta. Es un subtipo molecular de la LLC/LLP, el de IGHV no mutado, que suele tener peor pronóstico. Venetoclax ya está aprobado para la LLC/LLP mediante inhibición de BCL-2, de modo que este subtipo queda cubierto por la indicación de LLC existente.

Para este subtipo no hay ensayos listados. La única publicación analiza la estructura y función del receptor de células B tumoral, lo que da un apoyo solo indirecto.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para este subtipo específico.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35158929](https://pubmed.ncbi.nlm.nih.gov/35158929/) | 2022 | Revisión | Cancers | Analiza el receptor de células B (BCR) en la LLC. Distingue dos grandes subgrupos: IGHV no mutado (origen pregerminal, peor pronóstico) e IGHV mutado (origen postgerminal, mejor pronóstico). Resume lo que el estudio del BCR tumoral aporta a la biología y la clínica. No evalúa venetoclax directamente. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 161138005 | VENCLYXTO 100 mg comprimidos recubiertos con película | Comprimido recubierto con película |
| 161138007IP1 | VENCLYXTO 100 mg comprimidos recubiertos con película | Comprimido recubierto con película |
| 161138004 | VENCLYXTO 50 mg comprimidos recubiertos con película | Comprimido recubierto con película |
| 161138002 | VENCLYXTO 10 mg comprimidos recubiertos con película | Comprimido recubierto con película |
| 161138007IP | VENCLYXTO 100 mg comprimidos recubiertos con película | Comprimido recubierto con película |

Las cinco autorizaciones están vigentes y corresponden a monofármaco, titular Abbvie Deutschland GmbH & Co.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor selectivo de BCL-2), no citotóxico convencional |
| Riesgo de Mielosupresión | Medio a alto. La literatura compilada señala el síndrome de lisis tumoral y la mielosupresión como los efectos adversos más frecuentes en enfermedades linfoides. Confirmar en el prospecto. |
| Clasificación de Emetogenicidad | Baja a moderada (estimación general para un agente oral dirigido; confirmar en el prospecto) |
| Items de Monitoreo | Hemograma con diferencial, función renal y hepática, electrolitos y ácido úrico (riesgo de lisis tumoral), signos de infección |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta de interacciones identificó 100 en total. Entre las principales de nivel **Mayor** figuran:
  - Aprepitant
  - Dexametasona
  - Claritromicina
  - Eliglustat
  - Rolapitant
  - Fidaxomicina
  - Cobicistat
  - Deferiprona
  - Samario (153Sm) lexidronam

  Hay además interacciones de nivel **Moderado** con alvimopán, loperamida, cimetidina, naldemedina, metreleptina, miconazol, rifaximina, clotrimazol, troglitazona y deferasirox. Naloxegol figura con nivel **Menor**.
- La literatura compilada indica que los antifúngicos azólicos potentes, como posaconazol, inhiben CYP3A y requieren ajuste de dosis de venetoclax.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El subtipo ya está cubierto por la indicación aprobada de LLC/LLP, así que no constituye un reposicionamiento real. Además, no hay ensayos ni literatura específica para este subtipo (solo una revisión indirecta sobre biología del BCR), por lo que el respaldo se limita a la predicción del modelo (nivel L4).

**Para avanzar se necesita:**
- Confirmar con el prospecto de la AEMPS el texto exacto de las indicaciones aprobadas y verificar que incluye la LLC/LLP sin restricción por estado de IGHV.
- Obtener las advertencias y contraindicaciones del prospecto, que no están disponibles en los datos compilados.
- Completar los datos del mecanismo de acción (por ejemplo, desde DrugBank).
- Buscar datos de eficacia estratificados por estado de IGHV en los ensayos de LLC ya existentes, como el MURANO.
- Si se busca un reposicionamiento genuino, centrar el análisis en las indicaciones con más respaldo del listado: leucemia mieloide (L1), leucemia mieloide crónica BCR-ABL1 positiva y linfoma folicular (ambas L2).
- Establecer un plan de monitoreo de seguridad: lisis tumoral, mielosupresión e interacciones con inhibidores de CYP3A.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

