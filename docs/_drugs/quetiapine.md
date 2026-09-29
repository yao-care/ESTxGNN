---
layout: default
title: Quetiapine
parent: Solo predicción del modelo (L5)
nav_order: 448
evidence_level: L5
indication_count: 10
---

# Quetiapine
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

# Quetiapina: De Esquizofrenia y Trastornos del Estado de Ánimo a Distrofia Retiniana con o sin Anomalías Extraoculares

## Resumen en Una Frase

La quetiapina es un antipsicótico atípico, utilizado originalmente para la esquizofrenia, el trastorno bipolar y el trastorno depresivo mayor.
El modelo TxGNN predice que podría ser efectiva para la **distrofia retiniana con o sin anomalías extraoculares**, pero **no hay ensayos clínicos** y las **15 publicaciones** recuperadas no respaldan esta dirección (se trata de literatura general sobre patología ocular).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Esquizofrenia, trastorno bipolar I y trastorno depresivo mayor (fuente: ficha farmacológica; los textos de indicación de las autorizaciones españolas están vacíos) |
| Nueva Indicación Predicha | Distrofia retiniana con o sin anomalías extraoculares |
| Puntaje de Predicción TxGNN | 99,57 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente principal. Según la información farmacológica conocida, la quetiapina actúa sobre receptores de serotonina (5-HT1A, 5-HT1D, 5-HT1E, 5-HT1F, 5-HT2A), dopamina D2, histamina H1 y el transportador de noradrenalina (NET). Su efecto antipsicótico se atribuye principalmente al antagonismo D2/5-HT2A.

**No se ha establecido un vínculo mecanístico** entre estas vías y la degeneración retiniana. El puntaje alto proviene únicamente del modelo de grafos. Además, la toxicidad retiniana figura como una preocupación de seguridad asociada a la quetiapina, no como una señal terapéutica.

La relación entre la indicación original (psiquiátrica) y la nueva (distrofia hereditaria de la retina) es débil. Por tanto, esta predicción debe considerarse un resultado computacional sin respaldo biológico o clínico actual.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Ninguna de las publicaciones recuperadas evalúa la quetiapina en distrofia retiniana. Tratan sobre patología ocular y extraocular en general, y su relevancia está pendiente de revisión.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Revisión | Seminars in Neurology | Enfoque sistemático de la diplopía; sin relación con quetiapina |
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Revisión | Seminars in Ultrasound, CT, and MR | Infecciones orbitarias y su diagnóstico por imagen |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Revisión | Klinische Monatsblätter für Augenheilkunde | Ptosis congénita y sus formas complicadas |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Revisión | Taiwan Journal of Ophthalmology | Anomalías congénitas de la forma del cristalino |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Revisión | Pediatric Radiology | Diagnóstico diferencial por imagen de lesiones oculares pediátricas |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Revisión | Journal of Binocular Vision and Ocular Motility | Oftalmoplejía y trastornos congénitos de disinervación craneal |
| [10192514](https://pubmed.ncbi.nlm.nih.gov/10192514/) | 1999 | Revisión | Progress in Retinal and Eye Research | Propioceptores de los músculos extraoculares |
| [31359131](https://pubmed.ncbi.nlm.nih.gov/31359131/) | 2019 | Revisión | Human Genetics | Arquitectura genética de defectos oculares del desarrollo por señalización del ácido retinoico |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Reporte de caso | American Journal of Ophthalmology | Dos casos de criptoftalmía unilateral |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Otro | Optometry and Vision Science | Divergencia sinérgica en fibrosis congénita de músculos extraoculares |

## Información de Mercado en España

Los textos de indicación aprobada de estas autorizaciones no están disponibles en los datos recibidos.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 80241 | Quetiapina Tarbis 50 mg comprimidos de liberación prolongada EFG | Comprimido de liberación prolongada | Tarbis Farma S.L. |
| 83355 | Quetiapina Alter 300 mg comprimidos de liberación prolongada EFG | Comprimido de liberación prolongada | Laboratorios Alter S.A. |
| 80242 | Quetiapina Tarbis 150 mg comprimidos de liberación prolongada EFG | Comprimido de liberación prolongada | Tarbis Farma S.L. |
| 70202 | Quetiapina Stada 300 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Laboratorio Stada S.L. |
| 74447 | Quetiapina Aristo 300 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Aristo Pharma GmbH |

## Consideraciones de Seguridad

- **Toxicidad retiniana**: se ha descrito como una preocupación de seguridad de la quetiapina. Es especialmente relevante al plantear su uso en enfermedades de la retina.
- **Interacciones farmacológicas**: las 8 entradas de la consulta corresponden a dianas farmacológicas (receptores y transportadores), no a interacciones con otros medicamentos. No se dispone de datos de interacciones farmacológicas clínicas.

Consultar el prospecto para el resto de la información de seguridad (advertencias y contraindicaciones).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo computacional (nivel L5), sin ensayos clínicos, sin literatura pertinente y sin vínculo mecanístico plausible. Además, la toxicidad retiniana es una preocupación de seguridad conocida de la quetiapina.

**Para avanzar se necesita:**
- Un vínculo mecanístico plausible entre las dianas de la quetiapina y las vías de la distrofia retiniana, con estudios preclínicos que lo respalden
- Advertencias y contraindicaciones del prospecto de la AEMPS (dato bloqueante para el cribado de seguridad)
- Datos de mecanismo de acción desde DrugBank
- Considerar priorizar otras predicciones de la lista con más respaldo. En particular, la **tricotilomanía** (rank 8, puntaje 99,38 %, nivel L4) cuenta con reportes de caso y revisiones específicos de quetiapina, aunque sin ensayos controlados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

