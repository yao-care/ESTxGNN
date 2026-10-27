---
layout: default
title: Dapoxetine
parent: Evidencia moderada (L3-L4)
nav_order: 221
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-14
description: "Dapoxetine: nueva indicación predicha, Trastorno de migraña (nivel de evidencia L4). Indicación original: Eyaculación precoz (indicación del grafo de conocimiento"
monitor_inn: "Dapoxetine"
predicted_indications: ["migraine disorder", "dysthymic disorder", "migraine with brainstem aura"]
---

# Dapoxetine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **3** 
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

## Dapoxetina: De Eyaculación Precoz a Trastorno de Migraña
{: .text-alpha }

## Resumen en Una Frase

Dapoxetina es un inhibidor selectivo de la recaptación de serotonina (ISRS) de acción corta, utilizado originalmente para el tratamiento de la eyaculación precoz.
El modelo TxGNN predice que podría ser efectivo para **trastorno de migraña**, pero actualmente no hay ensayos clínicos registrados y solo se dispone de **2 publicaciones** de apoyo indirecto (una revisión sobre usos off-label de ISRS y un estudio de cohorte sobre dapoxetina en eyaculación precoz).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Eyaculación precoz (indicación del grafo de conocimiento; el texto autorizado en España no está disponible) |
| Nueva Indicación Predicha | Trastorno de migraña |
| Puntaje de Predicción TxGNN | 99.34% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, dapoxetina es un ISRS de acción corta que inhibe el transportador de serotonina (SERT, gen SLC6A4). Su eficacia en la eyaculación precoz está respaldada por su uso clínico, y mecanísticamente podría ser aplicable a la migraña por la vía serotoninérgica.

La señalización de la serotonina (5-HT) participa en la activación trigeminovascular y en la depresión cortical propagada, y los triptanes actúan sobre los receptores 5-HT1B/1D. Esto hace biológicamente plausible la hipótesis de modulación serotoninérgica en la migraña.

Sin embargo, como clase, los ISRS han mostrado una eficacia profiláctica limitada e inconsistente en migraña. El vínculo para dapoxetina se basa en inferencia a nivel de clase y en el alto puntaje de TxGNN, y el mecanismo no está verificado de forma independiente.

### Otras predicciones del modelo

| Posición | Indicación predicha | Puntaje TxGNN | Nivel de Evidencia | Recomendación |
|------|------|------|------|------|
| 2 | Trastorno distímico | 99.14% | L5 | Hold |
| 3 | Migraña con aura de tronco encefálico | 99.11% | L5 | Hold |

La distimia es coherente a nivel de clase (los ISRS tratan trastornos depresivos), pero dapoxetina tiene vida media corta y está pensada para uso a demanda, sin evidencia en condiciones depresivas crónicas. La migraña con aura de tronco encefálico es un subtipo raro, y la predicción probablemente se deriva de su relación con la categoría general de migraña.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33998993](https://pubmed.ncbi.nlm.nih.gov/33998993/) | 2022 | Revisión | Current Neuropharmacology | Revisión del estado actual de los usos off-label de los ISRS en distintas indicaciones, entre ellas la migraña |
| [23504864](https://pubmed.ncbi.nlm.nih.gov/23504864/) | 2013 | Cohorte | Urologia | Cumplimiento del tratamiento con dapoxetina en pacientes con eyaculación precoz; no aborda migraña |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 70875 | PRILIGY 60 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 70874 | PRILIGY 30 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta se completó y registró una interacción de tipo farmacológico con el transportador de serotonina (SERT, SLC6A4), que es la diana principal de dapoxetina como ISRS. No se trata de una interacción con otro fármaco y no tiene nivel de gravedad asignado.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para migraña (L4) se apoya únicamente en el puntaje del modelo y en inferencia a nivel de clase, sin ensayos clínicos ni estudios específicos de dapoxetina en migraña. Además, la eficacia profiláctica de los ISRS en migraña es limitada e inconsistente.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) de dapoxetina
- Advertencias y contraindicaciones del prospecto de la AEMPS, necesarias para el cribado de seguridad
- Estudios preclínicos o de mecanismo que respalden el uso de dapoxetina en migraña
- Evaluación de si el perfil de dosis a demanda es compatible con una indicación profiláctica o aguda en migraña
- Texto de la indicación autorizada en España para las dos autorizaciones vigentes
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

