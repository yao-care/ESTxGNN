---
layout: default
title: Iohexol
parent: Solo predicción del modelo (L5)
nav_order: 427
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
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

# Iohexol: De Medio de Contraste Radiológico a Insomnio

## Resumen en Una Frase

Iohexol es un medio de contraste yodado, no iónico e hidrosoluble, utilizado en técnicas de diagnóstico por imagen con rayos X.
El modelo TxGNN predice que podría ser efectivo para **insomnio**, pero no existe ningún ensayo clínico ni publicación que respalde esta dirección (**0 ensayos clínicos** y **0 publicaciones**).
La predicción carece de plausibilidad biológica y debe considerarse un probable artefacto del grafo de conocimiento.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de autorización compilados (el texto de indicación está vacío); el producto se emplea como medio de contraste radiológico |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99,87% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado. Según la información conocida, iohexol es un medio de contraste yodado, no iónico e hidrosoluble, que actúa por atenuación de los rayos X y es farmacológicamente inerte.

No se identifica un vínculo mecanístico con el insomnio. Iohexol no tiene actividad conocida sobre las vías que regulan el sueño (GABAérgica, orexinérgica, melatoninérgica o monoaminérgica). La relación con su uso original (diagnóstico por imagen) tampoco se traslada a un efecto terapéutico sobre el sueño.

El puntaje TxGNN muy alto (0,9987) probablemente refleja artefactos del grafo de conocimiento, como las 100 interacciones farmacológicas registradas, más que una relación biológica real.

> **Nota sobre la segunda predicción (ansiedad, puntaje 99,25%):** tampoco se sustenta un mecanismo terapéutico. Las cuatro publicaciones recuperadas mencionan la ansiedad solo de forma incidental (contexto procedimental o efectos adversos), no como objetivo de tratamiento.

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
La predicción es solo computacional (nivel L5): no hay ensayos ni literatura, y la farmacología de iohexol, un agente de contraste inerte, no ofrece un mecanismo plausible sobre el sueño. El puntaje elevado parece un artefacto del grafo.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y de las indicaciones aprobadas (ficha técnica de la AEMPS)
- Advertencias y contraindicaciones del prospecto, para completar el cribado de seguridad
- Una hipótesis mecanística y evidencia preclínica que justifiquen el insomnio antes de reconsiderar la candidatura
- Valorar si el sistema debe filtrar predicciones de agentes de diagnóstico farmacológicamente inertes
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

