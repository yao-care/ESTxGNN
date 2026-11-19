---
layout: default
title: Iohexol
parent: Solo predicción del modelo (L5)
nav_order: 427
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-20
description: "Iohexol: nueva indicación predicha, Insomnio (nivel de evidencia L5). Indicación original: No disponible en los datos de autorización compilados (el texto de in…"
monitor_inn: "IOHEXOL"
predicted_indications: ["insomnia (disease)", "anxiety"]
---

# Iohexol
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

## Iohexol: De Medio de Contraste Radiológico a Insomnio
{: .text-alpha }

## Resumen en Una Frase

Iohexol es un medio de contraste yodado, no iónico e hidrosoluble, utilizado en técnicas de diagnóstico por imagen con rayos X.
El modelo TxGNN predice que podría ser efectivo para **insomnio**, pero no existe ningún ensayo clínico ni publicación que respalde esta dirección (**0 ensayos clínicos** y **0 publicaciones**).
La predicción carece de plausibilidad biológica y debe considerarse un probable artefacto del modelo TxGNN (aprendizaje profundo).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de autorización compilados (el texto de indicación está vacío); el producto se emplea como medio de contraste radiológico |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 0,9987 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 3 de 3) |
| Número de Autorizaciones | 3 (comercializadas: 3) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Iohexol (traducción no oficial): «Los átomos de yodo del iohexol atenúan los rayos X en proporción directa a la concentración de iohexol. Dado que la concentración varía con el tiempo, el iohexol proporciona un contraste de imagen dependiente del tiempo que puede ayudar a visualizar las estructuras corporales.» Texto original en inglés: "The iodine atoms in iohexol provide attenuation of X-rays in direct proportion to the concentration of iohexol. Since concentration changes over time, iohexol provides time-dependent image contrast which may assist in visualizing body structures." ([DailyMed: Omnipaque (iohexol) prescribing information, Medical Purchasing Solutions, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=508c42eb-f5e5-44f1-e063-6294a90a4d1f), versión del 2026-04-28; consultado el 2026-11-19). Según la información conocida, iohexol es un medio de contraste yodado, no iónico e hidrosoluble, que actúa por atenuación de los rayos X y es farmacológicamente inerte.

No se identifica un vínculo mecanístico con el insomnio. Iohexol no tiene actividad conocida sobre las vías que regulan el sueño (GABAérgica, orexinérgica, melatoninérgica o monoaminérgica). La relación con su uso original (diagnóstico por imagen) tampoco se traslada a un efecto terapéutico sobre el sueño.

El puntaje TxGNN muy alto (0,9987) probablemente refleja artefactos del modelo TxGNN (aprendizaje profundo), como las 100 interacciones farmacológicas registradas, más que una relación biológica real.

> **Nota sobre la segunda predicción (ansiedad, puntaje 0,9925):** tampoco se sustenta un mecanismo terapéutico. Las cuatro publicaciones recuperadas mencionan la ansiedad solo de forma incidental (contexto procedimental o efectos adversos), no como objetivo de tratamiento.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para insomnio.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 62019 | OMNIPAQUE 350 mg Iodo/ml solución inyectable | Solución inyectable | No disponible en los datos compilados |
| 62017 | OMNIPAQUE 240 mg Iodo/ml solución inyectable | Solución inyectable | No disponible en los datos compilados |
| 62018 | OMNIPAQUE 300 mg Iodo/ml solución inyectable | Solución inyectable | No disponible en los datos compilados |

Titular: GE Healthcare Bio-Sciences, S.A.U.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registran 100 interacciones. Entre las de gravedad mayor figuran:
  - Corticoides: hidrocortisona, dexametasona, betametasona, triamcinolona
  - Metformina
  - Anfotericina B (incluida la formulación de complejo lipídico)
  - Antibióticos: vancomicina, kanamicina, neomicina, levofloxacino
  - Bupropión, morfina, metoclopramida
  - Mesalazina y balsalazida
  - Fentermina, dietilpropión, dronabinol
  
  Con gravedad moderada se registra manitol.

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo computacional (nivel L5): no hay ensayos ni literatura, y la farmacología de iohexol, un agente de contraste inerte, no ofrece un mecanismo plausible sobre el sueño. El puntaje proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y de las indicaciones aprobadas (ficha técnica de la AEMPS)
- Advertencias y contraindicaciones del prospecto, para completar el cribado de seguridad
- Una hipótesis mecanística y evidencia preclínica que justifiquen el insomnio antes de reconsiderar la candidatura
- Valorar si el sistema debe filtrar predicciones de agentes de diagnóstico farmacológicamente inertes

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Omnipaque (iohexol) prescribing information, Medical Purchasing Solutions, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=508c42eb-f5e5-44f1-e063-6294a90a4d1f) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

