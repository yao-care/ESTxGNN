---
layout: default
title: Tolcapone
parent: Solo predicción del modelo (L5)
nav_order: 803
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tolcapone: nueva indicación predicha, Encefalitis subaguda de Rasmussen (nivel de evidencia L5). Indicación original: Enfermedad de Parkinson (según el grafo de conocimiento"
monitor_inn: "Tolcapone"
predicted_indications: ["Rasmussen subacute encephalitis", "myelitis", "PLA2G6-associated neurodegeneration", "transaldolase deficiency", "fructose-1,6-bisphosphatase deficiency", "Lewy body dementia", "X-linked intellectual disability-ataxia-apraxia syndrome", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "X-linked intellectual disability-cerebellar hypoplasia syndrome"]
---

# Tolcapone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Tolcapona: De Enfermedad de Parkinson a Encefalitis Subaguda de Rasmussen

## Resumen en Una Frase

Tolcapona es un inhibidor de la catecol-O-metiltransferasa (COMT), utilizado originalmente como tratamiento complementario de la enfermedad de Parkinson.
El modelo TxGNN predice que podría ser efectivo para la **encefalitis subaguda de Rasmussen**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción basada en el grafo de conocimiento.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Parkinson (según el grafo de conocimiento; el texto de indicación de las autorizaciones españolas no está disponible) |
| Nueva Indicación Predicha | Encefalitis subaguda de Rasmussen |
| Puntaje de Predicción TxGNN | 99,93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, tolcapona es un inhibidor de la COMT (enzima codificada por el gen *COMT*), que se utiliza como terapia complementaria en la enfermedad de Parkinson. Al inhibir la degradación periférica de la levodopa, prolonga su efecto dopaminérgico.

La encefalitis de Rasmussen es una encefalitis crónica inmunomediada, impulsada por linfocitos T. La COMT no tiene un papel inmunomodulador establecido, por lo que **no se aprecia un mecanismo plausible** que vincule el fármaco con esta enfermedad. La puntuación elevada del modelo refleja probablemente la proximidad en la red del grafo, no una relación biológica demostrada.

Por tanto, esta predicción debe considerarse altamente especulativa y requeriría evidencia preclínica básica antes de cualquier consideración clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la encefalitis subaguda de Rasmussen.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 97044003 | TASMAR 100 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |
| 97044006 | TASMAR 200 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |

Ambas autorizaciones están vigentes y corresponden a monofármacos del titular Viatris Healthcare Limited.

---

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no texto del prospecto)**: enfermedad hepática, enfermedad de la vesícula biliar, melanoma, trastornos hipotensivos, rabdomiólisis, fascitis nodular, discinesia tardía y discinesia lingual-facial-bucal.
- **Interacciones Farmacológicas**: la consulta se completó y solo registró la interacción farmacológica con su diana, la catecol-O-metiltransferasa (COMT), sin interacciones medicamentosas clínicas con nivel de gravedad asignado.
- **Hepatotoxicidad**: el análisis de la predicción señala que tolcapona tiene una advertencia de recuadro negro por hepatotoxicidad, relevante si se considerara en enfermedades con afectación hepática.

Para el detalle de advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5), sin ensayos ni literatura, y no existe un vínculo mecanístico plausible entre la inhibición de la COMT y una encefalitis inmunomediada. Además, el perfil de hepatotoxicidad añade una preocupación de seguridad.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA) del fármaco.
- Evidencia preclínica que justifique un papel de la inhibición de la COMT en la encefalitis de Rasmussen.
- Revisión del prospecto de AEMPS (advertencias y contraindicaciones), actualmente no disponible en los datos compilados.
- Evaluación del riesgo hepático antes de cualquier estudio clínico.

**Nota sobre otras predicciones:** entre las demás candidatas, la **demencia con cuerpos de Lewy** (puntaje 99,64%, nivel L4) es la que cuenta con cierto respaldo, una publicación preclínica de 2024 (PMID [39259788](https://pubmed.ncbi.nlm.nih.gov/39259788/)) en organoides corticales derivados de iPSC, aunque no se pudo confirmar el papel específico de la tolcapona. Se considera una pregunta de investigación, con cautela por la sensibilidad a agentes dopaminérgicos y el riesgo de psicosis. La predicción "parálisis agitante juvenil de Hunt" es en esencia un solapamiento de nomenclatura con la indicación ya existente, no un reposicionamiento novedoso.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

