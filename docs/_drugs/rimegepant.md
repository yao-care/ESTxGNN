---
layout: default
title: Rimegepant
parent: Solo predicción del modelo (L5)
nav_order: 468
evidence_level: L5
indication_count: 6
---

# Rimegepant
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Rimegepant: De Migraña a Migraña con Aura del Tronco Encefálico

## Resumen en Una Frase

Rimegepant es un antagonista del receptor del péptido relacionado con el gen de la calcitonina (CGRP), utilizado para el tratamiento agudo y preventivo de la migraña en adultos.
El modelo TxGNN predice que podría ser efectivo para la **migraña con aura del tronco encefálico**, un subtipo de migraña.
Actualmente hay **0 ensayos clínicos** y **14 publicaciones** sobre rimegepant en migraña en general, pero **ninguna específica de este subtipo**.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Migraña (tratamiento agudo y preventivo, según la literatura; el registro local no incluye el texto de indicación) |
| Nueva Indicación Predicha | Migraña con aura del tronco encefálico |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L4 (evidencia indirecta, sin estudios del subtipo) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la literatura revisada, rimegepant es un antagonista selectivo del receptor de CGRP, de molécula pequeña y administración oral. Su eficacia en migraña, con o sin aura, se ha demostrado en ensayos de Fase 3. En la UE se comercializa como Vydura.

La migraña con aura del tronco encefálico es un subtipo de migraña. Si la vía del CGRP participa en la fisiopatología de la migraña en general, es plausible que el bloqueo de su receptor también beneficie a este subtipo. Esa es la base mecanística de la predicción.

Hay una limitación importante: los estudios disponibles (Fase 3 y 4, revisiones, estudios farmacocinéticos) evalúan la migraña en general. Ninguno de los títulos revisados presenta un análisis específico del aura del tronco encefálico, así que la evidencia es indirecta. La seguridad en este subtipo, en particular los aspectos vasculares, tampoco está documentada.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Todas las publicaciones tratan la migraña en general. Ninguna analiza específicamente la migraña con aura del tronco encefálico.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36739335](https://pubmed.ncbi.nlm.nih.gov/36739335/) | 2023 | Revisión | CNS Drugs | Revisión del uso agudo y preventivo de rimegepant en migraña. Los ensayos pivotales de Fase 3 lo muestran más eficaz que el placebo. |
| [35790906](https://pubmed.ncbi.nlm.nih.gov/35790906/) | 2022 | Metaanálisis en red | J Headache Pain | Compara la eficacia relativa de lasmiditán frente a rimegepant y ubrogepant en el tratamiento agudo de la migraña. |
| [41366286](https://pubmed.ncbi.nlm.nih.gov/41366286/) | 2025 | Estudio de Fase 4 abierto | J Headache Pain | Estudio de 24 semanas sobre la seguridad y tolerabilidad de 75 mg al día en la prevención de la migraña episódica. |
| [41066271](https://pubmed.ncbi.nlm.nih.gov/41066271/) | 2025 | Fase 3 abierto | Cephalalgia | Seguridad y efectividad a largo plazo de rimegepant 75 mg ODT en adultos chinos con migraña aguda. |
| [36808268](https://pubmed.ncbi.nlm.nih.gov/36808268/) | 2023 | ECA de Fase 1 | Clin Pharmacol Drug Dev | Farmacocinética y seguridad de dosis únicas y múltiples en adultos chinos sanos, controlado con placebo. |
| [41574090](https://pubmed.ncbi.nlm.nih.gov/41574090/) | 2026 | Estudio prospectivo longitudinal | Brain Commun | Evalúa con angiografía por resonancia magnética el efecto de rimegepant sobre las arterias cerebrales y extracerebrales durante las crisis. Se propone como alternativa no vasoconstrictora. |
| [38307667](https://pubmed.ncbi.nlm.nih.gov/38307667/) | 2024 | Revisión | Handb Clin Neurol | Revisión de los gepantes. Recoge la preocupación por hepatotoxicidad que detuvo el desarrollo de la primera generación. |
| [32270407](https://pubmed.ncbi.nlm.nih.gov/32270407/) | 2020 | Revisión | Drugs | Primera aprobación de rimegepant ODT para el tratamiento agudo de la migraña. |
| [41652664](https://pubmed.ncbi.nlm.nih.gov/41652664/) | 2026 | Cohorte retrospectiva | Headache | Tolerabilidad y efectividad del uso fuera de indicación en adolescentes con migraña aguda. |
| [33550872](https://pubmed.ncbi.nlm.nih.gov/33550872/) | 2021 | Revisión | Pain Manag | Revisión de los nuevos tratamientos agudos de la migraña, entre ellos rimegepant. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1221645002 | VYDURA 75 MG LIOFILIZADO ORAL (Pfizer Europe Ma Eeig) | Liofilizado oral | No consta en el registro local |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como nota de la literatura, el estudio de angiografía por resonancia magnética (PMID 41574090) analiza los efectos vasculares de rimegepant durante las crisis. Estos aspectos deberían valorarse específicamente en el subtipo de aura del tronco encefálico.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje de TxGNN es muy alto y la vía del CGRP es plausible para este subtipo. Sin embargo, no hay ensayos ni publicaciones específicas de migraña con aura del tronco encefálico, y la evidencia es indirecta (L4). Además, falta la información de seguridad de la ficha técnica de la AEMPS, lo que impide avanzar al cribado de seguridad. Por ahora la predicción es una pregunta de investigación.

**Para avanzar se necesita:**
- Descargar y analizar la ficha técnica de la AEMPS (advertencias y contraindicaciones), que es el punto bloqueante.
- Obtener datos del mecanismo de acción desde DrugBank.
- Buscar estudios o análisis por subgrupos de migraña con aura del tronco encefálico.
- Evaluar la seguridad vascular en este subtipo.
- Confirmar la indicación aprobada en el registro español.

Las otras cinco predicciones del modelo (atrofodermia vermiculada, uleritema ofriógenes, deficiencia de cofactor II de la heparina, deficiencia de antitrombina tipo 2 y exceso de factor V con trombosis espontánea) no tienen ensayos, literatura ni vínculo mecanístico identificado. Su decisión es Hold.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

