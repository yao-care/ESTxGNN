---
layout: default
title: Tapentadol
parent: Solo predicción del modelo (L5)
nav_order: 764
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-31
description: "Tapentadol: nueva indicación predicha, Trastorno de migraña (migraine disorder) (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (los textos de indicación de la…"
monitor_inn: "TAPENTADOL"
predicted_indications: ["migraine disorder", "migraine with brainstem aura"]
---

# Tapentadol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Tapentadol: De Indicación No Especificada a Trastorno de Migraña
{: .text-alpha }

## Resumen en Una Frase

Tapentadol es un analgésico opioide que actúa como agonista del receptor mu-opioide e inhibidor de la recaptación de noradrenalina. Los datos compilados para este informe no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **trastorno de migraña**, pero no hay **ningún ensayo clínico** ni **publicaciones** que respalden directamente esta dirección para esa indicación. Las únicas dos publicaciones disponibles se asocian a una indicación relacionada (susceptibilidad a la migraña con o sin aura) y no demuestran eficacia.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Trastorno de migraña (migraine disorder) |
| Puntaje de Predicción TxGNN | 0.9967 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 14) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, tapentadol es un agonista del receptor mu-opioide con inhibición adicional de la recaptación de noradrenalina, lo que le permite modular las vías centrales del dolor. Teóricamente, esto podría ser aplicable a cuadros dolorosos como la migraña.

Sin embargo, la predicción se basa únicamente en una puntuación alta del modelo (0.9967), sin ensayos clínicos ni literatura que la respalden. Además, los opioides no se recomiendan en general para la migraña por el riesgo de cefalea por abuso de medicación, cronificación y dependencia, y su eficacia es inferior a la de triptanes o gepantes.

El otro subtipo predicho (migraña con aura del tronco encefálico, puntuación 0.9957) proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica, sin una justificación mecanística específica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Para la indicación principal (trastorno de migraña) actualmente no hay literatura relacionada disponible. Las dos publicaciones siguientes corresponden a la tercera predicción (susceptibilidad a migraña con o sin aura) y se muestran como contexto:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33689517](https://pubmed.ncbi.nlm.nih.gov/33689517/) | 2021 | Revisión | Expert Opin Pharmacother | Evalúa si los AINE y el paracetamol pueden sustituir a los opioides en el dolor agudo; argumenta a favor de alternativas no opioides, no de eficacia de tapentadol |
| [29760569](https://pubmed.ncbi.nlm.nih.gov/29760569/) | 2018 | Cohorte | Drug Healthc Patient Saf | Uso concomitante de opioides con triptanes o antidepresivos serotoninérgicos en EE. UU.; señala que los opioides no se recomiendan en migraña y advierte del riesgo de síndrome serotoninérgico |

---

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones vigentes (todas de principio activo único). El texto de la indicación aprobada no figura en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 73613 | Yantil 100 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 73243 | Palexia Retard 50 mg | Comprimido de liberación prolongada | No disponible |
| 73630 | Yantil Retard 250 mg | Comprimido de liberación prolongada | No disponible |
| 76794 | Yantil 4 mg/ml solución oral | Solución oral | No disponible |
| 88378 | Tapentadol Teva 100 mg EFG | Comprimido de liberación prolongada | No disponible |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las de nivel **mayor** figuran:
  - Morfina
  - Bupropión
  - Lorcaserina
  - Dietilpropión
  - Fentermina
  - Dolasetrón
  - Palonosetrón

  Entre las de nivel **moderado** figuran naloxona, atropina, hiosciamina, glicopirronio, diciclomina, trospio, eluxadolina, dronabinol, nabilona, epinefrina, ácido picosulfúrico, sulfato de sodio y polietilenglicol con electrolitos.
- **Consideración específica para migraña**: la literatura aportada advierte de un riesgo de síndrome serotoninérgico cuando los opioides se combinan con triptanes o antidepresivos serotoninérgicos (ISRS/IRSN). La inhibición de la recaptación de noradrenalina de tapentadol podría agravar esta preocupación.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en la puntuación del modelo (nivel L5), sin ensayos clínicos ni literatura de eficacia. Además, la literatura disponible desaconseja los opioides en migraña por el riesgo de cefalea por abuso de medicación, dependencia e interacciones serotoninérgicas.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicación aprobada), actualmente ausente
- Completar los datos del mecanismo de acción desde DrugBank
- Buscar evidencia clínica específica de tapentadol en migraña (ensayos o estudios observacionales)
- Comparar con las alternativas de primera línea (triptanes, gepantes, AINE) para justificar cualquier ventaja
- Evaluar el riesgo de cefalea por abuso de medicación y de síndrome serotoninérgico con tratamientos habituales de migraña
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

