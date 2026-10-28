---
layout: default
title: Tripelennamine
parent: Solo predicción del modelo (L5)
nav_order: 829
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
monitor_inn: "tripelennamine"
predicted_indications: ["nasal cavity disease", "recalcitrant atopic dermatitis"]
description: "Tripelennamine: nueva indicación predicha, Nasal cavity disease (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Tripelennamine
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

## Tripelennamine: Nasal cavity disease
{: .text-alpha }

## Resumen en Una Frase

Tripelennamina es un antihistamínico H1 de primera generación, utilizado originalmente para cuadros alérgicos como la rinitis alérgica, la urticaria y el angioedema.
pero actualmente solo cuenta con **0 ensayos clínicos** y **1 publicación** (un informe de experiencia clínica de 1954 sobre un preparado combinado) que respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Nasal cavity disease |
| Puntaje de Predicción TxGNN | 0.9959 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 1 de 2) |
| Número de Autorizaciones | 2 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, tripelennamina es un antihistamínico H1 de primera generación. Su eficacia en cuadros alérgicos como la urticaria, el angioedema y la rinitis alérgica forma parte de sus usos conocidos, y mecanísticamente podría ser aplicable a la urticaria alérgica.

La urticaria alérgica es un subtipo de la urticaria, que ya figura entre las indicaciones originales. Está mediada por la liberación de histamina desde los mastocitos, por lo que el bloqueo del receptor H1 es plausible. Se trata, en gran medida, de una extensión dentro de la indicación existente y no de un reposicionamiento genuino.

La única publicación disponible es de 1954 y describe un preparado antialérgico combinado, por lo que no es posible aislar la contribución de tripelennamina por sí sola.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [13195608](https://pubmed.ncbi.nlm.nih.gov/13195608/) | 1954 | Informe de experiencia clínica (no controlado) | Schweizerische medizinische Wochenschrift | Experiencias con un nuevo preparado antialérgico combinado; no permite aislar el efecto de tripelennamina y no incluye resumen disponible |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 58666 | AZARON STICK 20 MG/G BARRA CUTÁNEA | Barra cutánea | No disponible en los datos compilados |
| 88786 | RELEPOST 20 MG/G BARRA CUTANEA | Barra cutánea | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no el prospecto)**: hipertensión arterial, úlcera péptica, hiperplasia prostática benigna, hipertensión ocular, glaucoma de ángulo cerrado, hipertiroidismo (enfermedad de Graves, tirotoxicosis) y obstrucción del cuello vesical.
- **Interacciones Farmacológicas**: se identificaron 261 interacciones en total. Entre las principales:
  - **Mayores**: cloruro de potasio y citrato de potasio.
  - **Moderadas**: fármacos anticolinérgicos (atropina, escopolamina, hiosciamina, glicopirronio, diciclomina, trospio, propantelina, clidinio, metescopolamina, mepenzolato), opioides (morfina, loperamida, opio, eluxadolina), cannabinoides (dronabinol, nabilona) y metoclopramida.

Para las advertencias del prospecto, consultar el prospecto oficial.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es mecanísticamente plausible, pero está muy próxima a una indicación ya conocida y se apoya solo en una publicación de 1954 sobre un preparado combinado, sin ensayos clínicos. Además, la práctica actual favorece los antihistamínicos de segunda generación, por lo que un fármaco sedante y anticolinérgico no ofrece una ventaja clara.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), una carencia que bloquea el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Obtener estudios controlados con tripelennamina sola en urticaria alérgica.
- Evaluar la compatibilidad de la vía de administración: la presentación española es una barra cutánea y no se ha confirmado su adecuación.

### Otras predicciones evaluadas (todas en Hold)

| Indicación Predicha | Puntaje TxGNN | Nivel de Evidencia | Comentario |
|------|------|------|------|
| Enfermedad de la cavidad nasal | 0,9959 | L5 | Categoría demasiado inespecífica; solapa con la rinitis ya indicada |
| Dermatitis atópica refractaria | 0,9911 | L5 | Poco probable que responda al bloqueo H1; existen biológicos e inhibidores JAK |
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

