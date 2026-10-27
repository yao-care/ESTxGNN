---
layout: default
title: Eptinezumab
parent: Evidencia moderada (L3-L4)
nav_order: 300
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-14
description: "Eptinezumab: nueva indicación predicha, Migraña con aura del tronco encefálico (nivel de evidencia L4). Indicación original: Trastorno de migraña (según las indicaciones del grafo de conocimiento"
---

# Eptinezumab
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **1** 
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

## Eptinezumab: De Migraña a Migraña con Aura del Tronco Encefálico
{: .text-alpha }

## Resumen en Una Frase

Eptinezumab es un anticuerpo monoclonal anti-CGRP, originalmente utilizado para la prevención de la migraña.
El modelo TxGNN predice que podría ser efectivo para **migraña con aura del tronco encefálico**,
pero actualmente no hay ensayos clínicos registrados y solo se dispone de **10 publicaciones**, en su mayoría indirectas, que respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastorno de migraña (según las indicaciones del grafo de conocimiento; el texto de indicación autorizado no está disponible) |
| Nueva Indicación Predicha | Migraña con aura del tronco encefálico |
| Puntaje de Predicción TxGNN | 99,94% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Según la información conocida, eptinezumab es un anticuerpo monoclonal dirigido contra el péptido relacionado con el gen de la calcitonina (CGRP), ya comercializado para la prevención de la migraña, y mecanísticamente podría ser aplicable a la migraña con aura del tronco encefálico.

La migraña con aura del tronco encefálico es un subtipo clínico de la migraña, por lo que la participación de la vía del CGRP es biológicamente plausible. El alto puntaje de TxGNN (0,9994) es coherente con este solapamiento entre la indicación original y la nueva.

Sin embargo, la evidencia es en gran parte indirecta. El análisis post hoc de eptinezumab en pacientes con aura autorreportada (PROMISE-1 y PROMISE-2) apoya la eficacia en una población más amplia con aura, pero no es específico del aura de tronco encefálico. Los mecanismos propios del aura (por ejemplo, la depresión cortical propagada) podrían depender solo parcialmente del CGRP. Además, los datos de provocación con PACAP38 sugieren que algunas vías de ataque de migraña son independientes del CGRP, lo que podría limitar el beneficio en algunos pacientes.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40229719](https://pubmed.ncbi.nlm.nih.gov/40229719/) | 2025 | ECA | J Headache Pain | Los ataques de migraña inducidos por PACAP38 son independientes de la señalización de CGRP; podría limitar el beneficio de los anti-CGRP en algunos pacientes |
| [35302389](https://pubmed.ncbi.nlm.nih.gov/35302389/) | 2022 | Análisis post hoc de ECA | Cephalalgia | Eficacia y seguridad de eptinezumab en pacientes con migraña y aura autorreportada (PROMISE-1 y PROMISE-2) |
| [40341526](https://pubmed.ncbi.nlm.nih.gov/40341526/) | 2025 | Serie de casos/observacional | Headache | Dos casos de trastornos genéticos con migraña como rasgo clave que respondieron al tratamiento antagonista de CGRP |
| [30725283](https://pubmed.ncbi.nlm.nih.gov/30725283/) | 2019 | Revisión | Handb Exp Pharmacol | Papel del CGRP en la migraña |
| [33550872](https://pubmed.ncbi.nlm.nih.gov/33550872/) | 2021 | Revisión | Pain Manag | Revisión de los nuevos tratamientos de la migraña (incluye eptinezumab) y rimegepant como tratamiento agudo |
| [32699706](https://pubmed.ncbi.nlm.nih.gov/32699706/) | 2020 | Revisión | Cureus | Antagonistas de CGRP en migraña episódica y crónica |
| [35268319](https://pubmed.ncbi.nlm.nih.gov/35268319/) | 2022 | Casos y revisión | J Clin Med | Posible utilidad de los anticuerpos anti-CGRP en el aura migrañosa |
| [42090640](https://pubmed.ncbi.nlm.nih.gov/42090640/) | 2026 | Cohorte (seguridad) | Neurology | Riesgo de glaucoma asociado al uso de inhibidores de CGRP en migraña |
| [42390441](https://pubmed.ncbi.nlm.nih.gov/42390441/) | 2026 | Cohorte (seguridad) | Cephalalgia | Riesgo cerebrovascular con anticuerpos anti-CGRP frente a onabotulinumtoxinA en migraña |
| [40191903](https://pubmed.ncbi.nlm.nih.gov/40191903/) | 2025 | Reporte de caso | Rev Neurol | Manejo del efecto de desgaste con eptinezumab en un caso de migraña crónica refractaria a dos anticuerpos CGRP subcutáneos |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1211599001 | VYEPTI 100 MG concentrado para solución para perfusión | Concentrado y disolvente para solución para perfusión | No disponible en los datos compilados |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es biológicamente plausible y el puntaje del modelo es muy alto, pero la evidencia es de nivel L4: no hay ensayos clínicos específicos para migraña con aura del tronco encefálico y la literatura es mayoritariamente indirecta. Además, faltan datos de seguridad del prospecto, lo que impide avanzar al cribado de seguridad.

**Para avanzar se necesita:**
- Obtener advertencias y contraindicaciones del prospecto de AEMPS (descargar y analizar el PDF).
- Obtener datos del mecanismo de acción desde DrugBank.
- Evidencia específica en aura del tronco encefálico (series de casos, análisis de subgrupos o ensayos dedicados).
- Evaluar el impacto de las vías independientes de CGRP (p. ej., PACAP38) sobre la respuesta esperada.
- Revisar las señales de seguridad recientes (glaucoma y riesgo cerebrovascular) en esta población.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

