---
layout: default
title: Buserelin
parent: Solo predicción del modelo (L5)
nav_order: 127
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Buserelin: nueva indicación predicha, Hipertricosis (nivel de evidencia L4). Indicación original: Cáncer de próstata (según la información farmacológica compilada"
monitor_inn: "buserelin"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality"]
---

# Buserelin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Buserelina: De Cáncer de Próstata a Hipertricosis
{: .text-alpha }

## Resumen en Una Frase

Buserelina es un agonista de la hormona liberadora de gonadotropinas (GnRH), utilizado originalmente para el tratamiento del cáncer de próstata.
El modelo TxGNN predice que podría ser efectivo para **hipertricosis**, pero actualmente no hay ensayos clínicos y solo hay **1 publicación** (un reporte de caso sobre síndrome de Cantú) que no describe el uso de buserelina para esta indicación, por lo que la evidencia es muy limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de próstata (según la información farmacológica compilada; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Hipertricosis |
| Puntaje de Predicción TxGNN | 0,9975 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 2 de 4) |
| Número de Autorizaciones | 4 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Buserelina es un agonista del receptor de GnRH (GNRHR). Su uso continuado suprime el eje hipofisario-gonadal y reduce los niveles de esteroides sexuales, lo que explica su utilidad en el cáncer de próstata hormonodependiente. No se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe; la descripción anterior se basa en la clase farmacológica conocida.

La relación entre la indicación original y la nueva es débil. La hipertricosis no depende clásicamente de los andrógenos gonadales (a diferencia del hirsutismo), por lo que la supresión de esteroides sexuales no ofrece una justificación mecanística clara. La única publicación recuperada trata del síndrome de Cantú (hipertricosis con anomalías cardíacas y esqueléticas) e hipopituitarismo, y no describe tratamiento con buserelina.

En consecuencia, la puntuación elevada de TxGNN es únicamente una predicción computacional, sin respaldo clínico. Otras predicciones del modelo (hipertricosis congénita universal tipo Ambras, síndromes malformativos con componente dental o periodontal, síndromes con malformación de Dandy-Walker y anomalías genéticas aisladas del tallo piloso) tampoco tienen evidencia ni plausibilidad mecanística.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31743099](https://pubmed.ncbi.nlm.nih.gov/31743099/) | 2019 | Reporte de caso | Endocrinology, Diabetes & Metabolism Case Reports | Caso de síndrome de Cantú (hipertricosis, anomalías cardíacas y esqueléticas) con deficiencias hormonales hipofisarias múltiples; sugiere incluir monitoreo endocrino. No evalúa buserelina. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 62477 | SUPREFACT DEPOT 9,45 mg IMPLANTE | Implante | No disponible |
| 57037 | SUPREFACT 100 microgramos/PULSACIÓN SOLUCIÓN PARA PULVERIZACIÓN NASAL | Solución para pulverización nasal | No disponible |
| 60980 | SUPREFACT DEPOT 6,3 mg IMPLANTE EN JERINGA PRECARGADA | Implante | No disponible |
| 57011 | SUPREFACT 1 mg/ml SOLUCIÓN INYECTABLE | Solución inyectable | No disponible |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de ensayos clínicos y de respaldo mecanístico; la única publicación es un reporte de caso que no involucra buserelina. La puntuación de TxGNN por sí sola no es suficiente para avanzar.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas)
- Complementar los datos del mecanismo de acción desde DrugBank
- Establecer una hipótesis mecanística plausible entre la supresión del eje GnRH y la hipertricosis
- Realizar una revisión sistemática de la literatura sobre agonistas de GnRH en trastornos del crecimiento del vello
- Evaluar la compatibilidad de las vías de administración (implante, nasal, inyectable) con la nueva indicación
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

