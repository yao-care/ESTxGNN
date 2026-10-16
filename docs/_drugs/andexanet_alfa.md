---
layout: default
title: Andexanet Alfa
parent: Solo predicción del modelo (L5)
nav_order: 58
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Andexanet Alfa: nueva indicación predicha, Trombastenia de Glanzmann (nivel de evidencia L5). Indicación original: No disponible en los datos de autorización de la AEMPS (texto de indi…"
monitor_inn: "ANDEXANET ALFA"
predicted_indications: ["Glanzmann thrombasthenia", "primary release disorder of platelets", "pseudo-von Willebrand disease", "hemophilia"]
---

# Andexanet Alfa
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Andexanet alfa: De Reversión de Anticoagulantes Inhibidores del FXa a Trombastenia de Glanzmann

## Resumen en Una Frase

Andexanet alfa es una proteína recombinante, señuelo del factor Xa catalíticamente inactivo, comercializada en España como ONDEXXYA para revertir el efecto de los inhibidores del factor Xa.
El modelo TxGNN predice que podría ser efectivo para **trombastenia de Glanzmann**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.
Su puntaje alto parece reflejar cercanía en la red de conocimiento de trastornos hemorrágicos, no un vínculo biológico real.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de autorización de la AEMPS (texto de indicación vacío) |
| Nueva Indicación Predicha | Trombastenia de Glanzmann |
| Puntaje de Predicción TxGNN | 99,77% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos consultada. Según la información conocida, andexanet alfa es un señuelo recombinante del factor Xa, catalíticamente inactivo, que une y secuestra los inhibidores del FXa (y la actividad de FXa asociada a TFPI). Su uso conocido es la reversión de la anticoagulación.

La trombastenia de Glanzmann se debe a la deficiencia o disfunción de la integrina plaquetaria αIIbβ3 (GPIIb/IIIa), que impide la agregación plaquetaria. Ambos mecanismos no guardan relación: un agente de reversión de inhibidores del FXa no tiene una acción plausible sobre una agregación plaquetaria defectuosa.

En consecuencia, la predicción parece un artefacto computacional derivado de la proximidad entre enfermedades hemostáticas en el grafo de conocimiento. **No se identificó una justificación mecanística sólida.**

---

## Otras Indicaciones Predichas (Contexto)

| Rango | Enfermedad | Puntaje TxGNN | Nivel de Evidencia | Recomendación | Comentario |
|---|---|---|---|---|---|
| 1 | Trombastenia de Glanzmann | 99,77% | L5 | Hold | Sin relación mecanística; sin estudios |
| 2 | Trastorno primario de liberación plaquetaria | 99,76% | L5 | Hold | Andexanet no modula la secreción plaquetaria; sin estudios |
| 3 | Pseudoenfermedad de von Willebrand | 99,65% | L5 | Hold | No actúa sobre el eje GPIb-VWF; sin estudios |
| 4 | Hemofilia | 99,10% | L4 | Hold | Solo literatura indirecta (reversión de anticoagulantes e interferencia en pruebas de laboratorio) |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Para la trombastenia de Glanzmann (indicación principal) actualmente no hay literatura relacionada disponible.

A modo de contexto, para la cuarta predicción (hemofilia) se identificaron publicaciones solo indirectamente relacionadas, que tratan sobre reversión de anticoagulantes o interferencia analítica, **no** sobre el uso de andexanet para tratar la hemofilia:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38620086](https://pubmed.ncbi.nlm.nih.gov/38620086/) | 2024 | Cohorte | Circulation | Subanálisis de ANNEXA-4: eficacia y seguridad de andexanet alfa en hemorragia gastrointestinal aguda con inhibidores del FXa |
| [31962376](https://pubmed.ncbi.nlm.nih.gov/31962376/) | 2020 | Estudio comparativo de laboratorio | Haemophilia | Andexanet alfa y DOAC Stop reducen la interferencia de rivaroxabán en las pruebas de FVIII y FIX |
| [33742436](https://pubmed.ncbi.nlm.nih.gov/33742436/) | 2021 | Guía/Recomendación | Thromb Haemost | Actualización de las recomendaciones del ICSH para la medición de laboratorio de anticoagulantes orales directos |
| [42033142](https://pubmed.ncbi.nlm.nih.gov/42033142/) | 2026 | Declaración de posición | Br J Haematol | Posición de la Sociedad Británica de Hematología sobre el uso de andexanet alfa |
| [36819179](https://pubmed.ncbi.nlm.nih.gov/36819179/) | 2023 | Revisión | EJHaem | Revisión de protocolos hospitalarios locales del Reino Unido para andexanet alfa |
| [30309890](https://pubmed.ncbi.nlm.nih.gov/30309890/) | 2018 | Revisión | Blood | Reversión de agentes anti-FXa y necesidades no cubiertas en pacientes con trauma |
| [31298165](https://pubmed.ncbi.nlm.nih.gov/31298165/) | 2019 | Revisión | Curr Pharm Des | Nuevos agentes hemostáticos y consideraciones anestésicas perioperatorias |
| [26519420](https://pubmed.ncbi.nlm.nih.gov/26519420/) | 2016 | Revisión | Drug Saf | Estrategias de reversión de los NOAC: estado de desarrollo y perspectivas |
| [27254626](https://pubmed.ncbi.nlm.nih.gov/27254626/) | 2016 | Revisión | Dtsch Med Wochenschr | Novedades en trastornos de la coagulación en cuidados intensivos |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1181345001 | ONDEXXYA 200 MG polvo para solución para perfusión (Astrazeneca AB) | Polvo para solución para perfusión | No disponible en los datos compilados |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como nota de contexto procedente del análisis de la literatura: andexanet alfa conlleva riesgo trombótico y podría interferir teóricamente con TFPI, por lo que su uso en una población con tendencia hemorrágica requeriría una evaluación de seguridad cuidadosa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para trombastenia de Glanzmann se basa únicamente en el modelo (nivel L5), sin ensayos ni publicaciones, y el mecanismo de acción de andexanet alfa (neutralización de inhibidores del FXa) no guarda relación con el defecto plaquetario de esta enfermedad. Lo mismo ocurre con las demás indicaciones predichas.

**Para avanzar se necesita:**
- Obtener los datos de advertencias y contraindicaciones del prospecto de la AEMPS (descargar y analizar el PDF).
- Obtener los datos detallados del mecanismo de acción desde DrugBank.
- Disponer de evidencia preclínica que respalde un vínculo biológico con la agregación plaquetaria, antes de considerar cualquier estudio clínico.
- Realizar una evaluación del riesgo trombótico si se explorase su uso en poblaciones con trastornos hemorrágicos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

