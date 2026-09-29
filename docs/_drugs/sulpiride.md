---
layout: default
title: Sulpiride
parent: Solo predicción del modelo (L5)
nav_order: 506
evidence_level: L5
indication_count: 9
---

# Sulpiride
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

# Sulpirida: De Esquizofrenia a Distrofia Retiniana con o sin Anomalías Extraoculares

## Resumen en Una Frase

La sulpirida es un antipsicótico benzamida antagonista de los receptores de dopamina D2/D3, utilizado en esquizofrenia, depresión, ansiedad y trastornos de conducta en niños.
El modelo TxGNN predice que podría ser efectiva para la **distrofia retiniana con o sin anomalías extraoculares**, pero **no hay ensayos clínicos** y las **16 publicaciones** halladas son artículos generales sobre anomalías oculares que no mencionan la sulpirida, por lo que no constituyen evidencia del fármaco.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Esquizofrenia, depresión y ansiedad (según la ficha farmacológica; los textos de indicación de las autorizaciones de la AEMPS no están disponibles) |
| Nueva Indicación Predicha | Distrofia retiniana con o sin anomalías extraoculares |
| Puntaje de Predicción TxGNN | 99.95% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

La sulpirida es un antagonista selectivo de los receptores de dopamina D2 y D3 (genes DRD2 y DRD3), con baja afinidad por el receptor D4. La ficha farmacológica también registra interacción con las anhidrasas carbónicas 1, 7 y 12. No se dispone de una descripción detallada del mecanismo de acción en DrugBank.

La relación con la nueva indicación es débil. La dopamina participa en la señalización retiniana, lo que ofrece un puente biológico muy laxo. Sin embargo, las distrofias retinianas hereditarias se deben a defectos génicos específicos de los fotorreceptores o del epitelio pigmentario retiniano, y no se ha establecido ningún mecanismo dopaminérgico que aporte beneficio.

El puntaje de 99.95% proviene únicamente del grafo de conocimiento de TxGNN. Las publicaciones asociadas coinciden con el término de la enfermedad, pero no tratan sobre el fármaco. Por eso esta predicción debe considerarse una hipótesis sin respaldo experimental.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Ninguna de estas publicaciones menciona la sulpirida. Son resultados por coincidencia de palabras clave con la enfermedad y no evidencia del fármaco.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Revisión | Seminars in Neurology | Enfoque sistemático para evaluar la diplopía y su diagnóstico diferencial |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Revisión | Pediatric Radiology | Diagnóstico diferencial y hallazgos de imagen de lesiones oculares pediátricas congénitas y del desarrollo |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Revisión | Taiwan Journal of Ophthalmology | Anomalías congénitas de la forma del cristalino |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Revisión | Klinische Monatsblätter für Augenheilkunde | Ptosis congénita y sus asociaciones con errores refractivos |
| [31359131](https://pubmed.ncbi.nlm.nih.gov/31359131/) | 2019 | Sin clasificar | Human Genetics | Arquitectura genética de los defectos del desarrollo ocular asociados a la vía del ácido retinoico |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Sin clasificar | International Journal of Molecular Sciences | Anomalías del nervio óptico y de la retina en la fibrosis congénita de los músculos extraoculares |
| [39582415](https://pubmed.ncbi.nlm.nih.gov/39582415/) | 2024 | Cohorte | Birth Defects Research | Prevalencia de anomalías oculares congénitas en 15 países europeos (estudio Medikeye) |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Sin clasificar | American Journal of Ophthalmology | Patogenia y tratamiento de la maculopatía asociada a anomalías cavitarias del disco óptico |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Reporte de caso | Optometry and Vision Science | Divergencia sinérgica en un paciente con fibrosis congénita de los músculos extraoculares |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Reporte de caso | American Journal of Ophthalmology | Dos casos de criptoftalmía unilateral |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 51836 | PSICOCEN 50 mg CÁPSULAS | Cápsula dura | Especialidades Farmacéuticas Centrum S.A. |
| 48557 | DOGMATIL 50 mg/ml SOLUCIÓN INYECTABLE | Solución inyectable | Neuraxpharm Spain S.L. |
| 48558 | DOGMATIL FUERTE 200 mg COMPRIMIDOS | Comprimido | Neuraxpharm Spain S.L.U. |
| 73195 | SULPIRIDA KERN PHARMA 50 mg CÁPSULAS EFG | Cápsula dura | Kern Pharma S.L. |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el grafo de TxGNN, sin ensayos clínicos ni literatura que mencione la sulpirida (nivel L5). El mecanismo dopaminérgico no explica un beneficio en distrofias retinianas de origen genético. Las otras 8 indicaciones predichas (hidranencefalia, polimicrogiria, Charcot-Marie-Tooth 1G, miopías, entre otras) también están en L5 y Hold, y varias no tienen vínculo mecanístico plausible.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de la AEMPS (advertencias y contraindicaciones), pendiente y bloqueante para cualquier evaluación de seguridad
- Confirmar la indicación aprobada en cada autorización española, hoy ausente en los datos
- Datos preclínicos que muestren un efecto de la sulpirida sobre la biología de los fotorreceptores o del epitelio pigmentario retiniano
- Una revisión de literatura específica que busque sulpirida o antagonistas D2 junto con distrofia retiniana
- Un análisis de seguridad en población pediátrica y oftalmológica, incluidos los efectos extrapiramidales
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

