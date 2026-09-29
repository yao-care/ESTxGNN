---
layout: default
title: Paliperidone
parent: Solo predicción del modelo (L5)
nav_order: 403
evidence_level: L5
indication_count: 10
---

# Paliperidone
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

# Paliperidona: De Esquizofrenia a Distrofia Retiniana con o sin Anomalías Extraoculares

## Resumen en Una Frase

Paliperidona es un antipsicótico (metabolito activo de la risperidona) que se comercializa en España, principalmente en formulaciones inyectables de liberación prolongada y en comprimidos, para la esquizofrenia.
El modelo TxGNN predice que podría ser efectivo para **distrofia retiniana con o sin anomalías extraoculares**, pero hay **0 ensayos clínicos** y las **16 publicaciones** recuperadas no mencionan la paliperidona. Se trata de una predicción sin respaldo real.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Esquizofrenia (inferida del mecanismo y de la predicción n.º 10; los textos de autorización no incluyen indicación) |
| Nueva Indicación Predicha | Distrofia retiniana con o sin anomalías extraoculares |
| Puntaje de Predicción TxGNN | 99,92 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Paliperidona es un antagonista de los receptores dopaminérgicos D2 y serotoninérgicos 5-HT2A. Este es el mecanismo central de la acción antipsicótica en la esquizofrenia. La base de datos no aporta una descripción detallada del mecanismo, así que esta información procede del análisis de la predicción.

**En este caso no se ha podido establecer un vínculo mecanístico plausible.** No se documenta ninguna vía retiniana o extraocular relacionada con el antagonismo D2/5-HT2A. El puntaje TxGNN es muy alto (0,999), pero proviene únicamente de las relaciones del grafo de conocimiento.

La literatura recuperada trata sobre anomalías oculares y extraoculares en general (diplopía, ptosis, oftalmoplejía, enfermedad orbitaria). Ningún artículo menciona la paliperidona, por lo que parece que se asociaron solo por términos de la enfermedad. No hay evidencia que permita relacionar la indicación original con esta nueva indicación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

No hay ECA. La tabla muestra 10 de las 16 publicaciones recuperadas, priorizando revisiones. Ninguna estudia la paliperidona ni una intervención farmacológica para distrofia retiniana; todas describen condiciones oculares o extraoculares en general.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Revisión | Seminars in Neurology | Enfoque sistemático de la historia y la exploración en pacientes con diplopía |
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Revisión | Seminars in Ultrasound, CT, and MR | Infecciones orbitarias, su etiología (sobre todo sinusitis) y signos clínicos |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Revisión | Klinische Monatsblätter für Augenheilkunde | Ptosis congénita, formas simples y complicadas, y asociaciones con errores de refracción |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Revisión | Taiwan Journal of Ophthalmology | Anomalías congénitas del tamaño, la forma y la posición del cristalino |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Revisión | Pediatric Radiology | Diagnóstico diferencial e imagen de patologías oculares pediátricas |
| [10192514](https://pubmed.ncbi.nlm.nih.gov/10192514/) | 1999 | Revisión | Progress in Retinal and Eye Research | Propioceptores de los músculos extraoculares y su papel en la percepción espacial visual |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Revisión | Journal of Binocular Vision and Ocular Motility | Oftalmoplejía y trastornos congénitos de la disinervación craneal |
| [30747268](https://pubmed.ncbi.nlm.nih.gov/30747268/) | 2019 | Cohorte | Neuroradiology | Características neurorradiológicas y clínicas de la oftalmoplejía |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Reporte de caso | American Journal of Ophthalmology | Dos pacientes con criptoftalmía unilateral |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Reporte de caso | Journal of Neuro-Ophthalmology | Sincinesia troclear-oculomotora congénita en un niño de 6 años |

## Información de Mercado en España

La base de datos registra 20 autorizaciones; se muestran las 5 principales. Los textos de indicación aprobada figuran vacíos, por lo que se omiten.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 11672002 | XEPLION 50 mg suspensión inyectable de liberación prolongada | Suspensión inyectable en jeringa precargada |
| 89540 | Paliperidona Stada 100 mg suspensión inyectable de liberación prolongada en jeringa precargada EFG | Suspensión inyectable de liberación prolongada en jeringa precargada |
| 86055 | Paliperidona Teva 75 mg suspensión inyectable de liberación prolongada EFG | Suspensión inyectable de liberación prolongada |
| 83086 | Parnido 6 mg comprimidos de liberación prolongada EFG | Comprimido de liberación prolongada |
| 86054 | Paliperidona Teva 50 mg suspensión inyectable de liberación prolongada EFG | Suspensión inyectable de liberación prolongada |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (nivel L5): no hay ensayos clínicos, la literatura no menciona la paliperidona y no existe un vínculo mecanístico plausible entre el antagonismo D2/5-HT2A y la distrofia retiniana.

**Para avanzar se necesita:**
- Evidencia preclínica o mecanística que conecte la paliperidona con vías retinianas
- Estudios que involucren directamente a la paliperidona en distrofias retinianas
- Datos de seguridad del prospecto de la AEMPS (advertencias y contraindicaciones), que faltan actualmente
- Los textos de indicación aprobada de las autorizaciones y una descripción detallada del mecanismo de acción

**Nota:** entre las demás predicciones, la n.º 10 (esquizofrenia resistente al tratamiento) tiene 4 ensayos de Fase 4 (uno terminado con 5 participantes) y nivel L3. Es más una indicación cercana a la ya aprobada que un reposicionamiento, y habría que evaluarla en un informe aparte.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

