---
layout: default
title: Aflibercept
parent: Solo predicción del modelo (L5)
nav_order: 26
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Aflibercept: nueva indicación predicha, Esotropía (nivel de evidencia L5). Indicación original: Degeneración macular, edema macular diabético…"
monitor_inn: "AFLIBERCEPT"
predicted_indications: ["esotropia"]
---

# Aflibercept
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Aflibercept: De Degeneración Macular a Esotropía

## Resumen en Una Frase

Aflibercept es una proteína de fusión anti-VEGF originalmente utilizada para el tratamiento de enfermedades vasculares de la retina (degeneración macular, edema macular diabético, oclusión de la arteria retiniana) y de la metástasis de cáncer de colon.
El modelo TxGNN predice que podría ser efectivo para **esotropía**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Degeneración macular, edema macular diabético, oclusión de la arteria retiniana y metástasis de cáncer de colon (según el grafo de conocimiento; el texto de indicación de las autorizaciones españolas no está disponible) |
| Nueva Indicación Predicha | Esotropía |
| Puntaje de Predicción TxGNN | 99.38% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Aflibercept actúa como una "trampa" de factores de crecimiento: se une a VEGF-A, VEGF-B y al factor de crecimiento placentario (PlGF), reduciendo la neovascularización y la permeabilidad vascular. Por ello se emplea en enfermedades neovasculares y edematosas de la retina. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe; la descripción anterior corresponde al conocimiento farmacológico general del fármaco.

La relación entre las indicaciones originales y la nueva es débil. La esotropía es un trastorno de la alineación ocular causado principalmente por factores neuromusculares, refractivos, acomodativos o sensoriales, y no por angiogénesis o hiperpermeabilidad vascular. No se ha establecido un vínculo mecanístico directo entre la inhibición de VEGF y la esotropía.

Una posible asociación indirecta es que la esotropía o el estrabismo aparezcan de forma secundaria en ojos con enfermedad retiniana (por ejemplo, retinopatía del prematuro, donde se usan agentes anti-VEGF). Esta relación es confusa e indirecta, y no respalda el uso de aflibercept como tratamiento de la esotropía. El puntaje alto (0.994) refleja solo una predicción basada en grafos.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones vigentes (todas de producto único, ninguna cancelada). El texto de indicación aprobada no figura en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 112797001 | EYLEA 40 mg/ml solución inyectable en jeringa precargada | Solución inyectable |
| 112797004 | EYLEA 114,3 mg/ml solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada |
| 112814001 | ZALTRAP 25 mg/ml concentrado para solución para perfusión | Concentrado para solución para perfusión |
| 1241895001 | EYDENZELT 40 mg/ml solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada |
| 1241865002 | OPUVIZ 40 mg/ml solución inyectable en vial | Solución inyectable |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 78 interacciones. Entre las de nivel **Mayor** figuran deferiprona, samario (153Sm) lexidronam, adalimumab, baricitinib, certolizumab pegol, cladribina y clozapina. Entre las de nivel **Moderado** figuran estroncio-89 cloruro, roflumilast, cloranfenicol, zidovudina, alefacept, alemtuzumab, anakinra, azatioprina y canakinumab, además de algunas vacunas (antitetánica, ántrax, cólera viva).

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible entre la inhibición de VEGF y la esotropía. Los datos de seguridad del prospecto tampoco están disponibles.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank
- Prospecto de AEMPS con advertencias y contraindicaciones (brecha bloqueante para el cribado de seguridad)
- Revisión de literatura sobre anti-VEGF y estrabismo/esotropía (incluida la retinopatía del prematuro) para aclarar si existe una señal real o solo confusión
- Evidencia preclínica o clínica que sustente un mecanismo plausible
- Evaluación de compatibilidad de vía de administración (la vía intravítrea no está confirmada para esta indicación)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

