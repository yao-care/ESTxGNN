---
layout: default
title: Rasagiline
parent: Solo predicción del modelo (L5)
nav_order: 684
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-31
description: "Rasagiline: nueva indicación predicha, Neurodegeneración asociada a PLA2G6 (nivel de evidencia L5). Indicación original: Enfermedad de Parkinson (y síndromes parkinsonianos relacionados)"
monitor_inn: "Rasagiline"
predicted_indications: ["PLA2G6-associated neurodegeneration", "Rasmussen subacute encephalitis", "myelitis", "paralysis agitans, juvenile, of Hunt", "transaldolase deficiency", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis"]
---

# Rasagiline
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Rasagilina: De Enfermedad de Parkinson a Neurodegeneración Asociada a PLA2G6
{: .text-alpha }

## Resumen en Una Frase

Rasagilina es un inhibidor selectivo e irreversible de la monoaminooxidasa B (MAO-B), utilizado originalmente en el tratamiento de la enfermedad de Parkinson y de varios síndromes parkinsonianos.
El modelo TxGNN predice que podría ser efectivo para la **neurodegeneración asociada a PLA2G6**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Parkinson (y síndromes parkinsonianos relacionados) |
| Nueva Indicación Predicha | Neurodegeneración asociada a PLA2G6 |
| Puntaje de Predicción TxGNN | 0.9971 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 13) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Rasagilina inhibe de forma selectiva e irreversible la MAO-B, según los datos farmacológicos compilados para este informe (diana: MAOB). Se utiliza como monoterapia en fases iniciales de la enfermedad de Parkinson y como terapia adyuvante a levodopa en fases avanzadas. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada; lo anterior se basa solo en la diana farmacológica y el uso clínico conocido.

La neurodegeneración asociada a PLA2G6 (que incluye la distrofia neuroaxonal infantil y la distonía-parkinsonismo PARK14) comparte rasgos parkinsonianos y patología dopaminérgica/de alfa-sinucleína con la enfermedad de Parkinson. Por ello, rasagilina podría ofrecer apoyo dopaminérgico sintomático o cierta neuroprotección mediante la reducción del estrés oxidativo.

Conviene ser prudentes: el vínculo se apoya únicamente en el puntaje elevado de TxGNN y en el solapamiento fenotípico con las indicaciones parkinsonianas originales. No hay ensayos ni literatura que lo corroboren.

### Otras predicciones del modelo (todas de nivel L5)

| Enfermedad predicha | Puntaje TxGNN | Comentario |
|------|------|------|
| Encefalitis subaguda de Rasmussen | 0.9956 | Enfermedad inmunomediada; no hay vínculo mecanístico evidente con la inhibición de MAO-B |
| Mielitis | 0.9932 | Grupo heterogéneo de causas; vínculo especulativo |
| Parálisis agitante juvenil de Hunt | 0.9925 | Término histórico de parkinsonismo juvenil; probablemente solapa con la indicación existente, no es una novedad real; seguridad y eficacia pediátricas no establecidas |
| Deficiencia de transaldolasa | 0.9919 | Error congénito de la vía de las pentosas fosfato; mecanismo no evidente |
| Polimicrogiria perisilviana con hipoplasia cerebelosa y artrogriposis | 0.9901 | Malformación del neurodesarrollo; improbable que un inhibidor de MAO-B postnatal tenga efecto |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Hay 20 autorizaciones vigentes, todas de medicamentos con un solo principio activo (comprimidos). Se muestran las 5 principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 04304004IP3 | AZILECT 1 MG COMPRIMIDOS | Comprimido | No disponible en los datos |
| 04304004IP5 | AZILECT 1 mg COMPRIMIDOS | Comprimido | No disponible en los datos |
| 04304004IP1 | AZILECT 1 MG COMPRIMIDOS | Comprimido | No disponible en los datos |
| 81248 | DEVOLINA 1 MG COMPRIMIDOS EFG | Comprimido | No disponible en los datos |
| 80582 | RASAGILINA BLUEFISH 1 MG COMPRIMIDOS EFG | Comprimido | No disponible en los datos |

---

## Consideraciones de Seguridad

- **Contraindicaciones/condiciones de precaución según el grafo de conocimiento** (no proceden del prospecto): hipertensión, atrofia multisistémica, síndrome de taquicardia postural ortostática, hipotensión ortostática, discinesia inducida por fármacos, epilepsia, trastorno bipolar, trastorno afectivo mayor, enfermedad hepática, enfermedad de la vesícula biliar, melanoma, feocromocitoma, paraganglioma simpático y varios cánceres (duodeno, intestino delgado, corazón, glándula suprarrenal).
- **Interacciones farmacológicas**: solo se registró la interacción farmacológica con su diana, la monoaminooxidasa B (MAOB); no hay datos de interacciones con otros fármacos.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para la neurodegeneración asociada a PLA2G6 es solo computacional (nivel L5), sin ensayos clínicos ni literatura, y con un mecanismo de acción sin documentar. Aunque la plausibilidad biológica es razonable por el solapamiento parkinsoniano, no hay base suficiente para avanzar.

**Para avanzar se necesita:**
- Obtener los datos del mecanismo de acción (por ejemplo, desde DrugBank) para analizar el vínculo mecanístico.
- Descargar y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), requisito previo para la evaluación de seguridad.
- Revisión sistemática de literatura preclínica y clínica sobre inhibidores de MAO-B en PLAN/PARK14.
- Estudios preclínicos (modelos de PLA2G6) que respalden la hipótesis.
- Evaluar la seguridad y eficacia en población pediátrica, dada la aparición temprana de la enfermedad.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

