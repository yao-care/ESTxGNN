---
layout: default
title: Asenapine
parent: Solo predicción del modelo (L5)
nav_order: 49
evidence_level: L5
indication_count: 10
---

# Asenapine
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

# Asenapina: De Esquizofrenia y Trastorno Bipolar a Distrofia Retiniana con o sin Anomalías Extraoculares

## Resumen en Una Frase

La asenapina es un antipsicótico atípico sublingual, utilizado para tratar la esquizofrenia y los episodios maníacos del trastorno bipolar.
El modelo TxGNN predice que podría ser efectiva para la **distrofia retiniana con o sin anomalías extraoculares**,
pero actualmente hay **0 ensayos clínicos** y **15 publicaciones**, y ninguna de ellas trata sobre asenapina.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Esquizofrenia y trastorno bipolar (según la información farmacológica; el registro de autorizaciones no incluye texto de indicación) |
| Nueva Indicación Predicha | Distrofia retiniana con o sin anomalías extraoculares |
| Puntaje de Predicción TxGNN | 99.77% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco. Según la información farmacológica disponible, la asenapina se une a varios receptores: serotonina (5-HT1A, 5-HT1B, 5-HT1D, 5-HT1E, 5-HT2A), dopamina D2 e histamina H1. Este perfil es coherente con su uso en psicosis y manía.

**Esta predicción no tiene respaldo mecanístico creíble.** El puntaje alto (99.77%) proviene únicamente del grafo de conocimiento. No se identificó ningún vínculo entre el perfil de receptores de la asenapina y la biología de las distrofias retinianas. Las 15 publicaciones recuperadas tratan temas generales de oftalmología y neuro-oftalmología (diplopía, ptosis, infecciones orbitarias, oftalmoplejía). Sus títulos no mencionan la asenapina y parecen coincidencias de palabras clave sobre la enfermedad, no evidencia sobre el fármaco.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Ninguna de estas publicaciones estudia la asenapina. Se listan solo como referencia de lo recuperado.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Revisión | Seminars in Neurology | Enfoque sistemático para evaluar la diplopía y su diagnóstico diferencial |
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Revisión | Seminars in Ultrasound, CT, and MR | Infecciones orbitarias: causas (sobre todo sinusitis), estadios de celulitis y signos clínicos |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Revisión | Klinische Monatsblätter für Augenheilkunde | Ptosis congénita: formas simple y complicada, y asociación con errores de refracción |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Revisión | Taiwan Journal of Ophthalmology | Anomalías congénitas de la forma del cristalino |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Revisión | Pediatric Radiology | Diagnóstico diferencial y hallazgos de imagen de lesiones oculares pediátricas |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Revisión | Journal of Binocular Vision and Ocular Motility | Oftalmoplejía y trastornos congénitos de la disinervación craneal |
| [31359131](https://pubmed.ncbi.nlm.nih.gov/31359131/) | 2019 | Revisión | Human Genetics | Arquitectura genética de los defectos oculares del desarrollo asociados al ácido retinoico |
| [37408430](https://pubmed.ncbi.nlm.nih.gov/37408430/) | 2023 | Revisión | Zhonghua Yan Ke Za Zhi | Avances sobre la estructura e inervación de los músculos extraoculares |
| [30747268](https://pubmed.ncbi.nlm.nih.gov/30747268/) | 2019 | Cohorte/Imagen | Neuroradiology | Características neurorradiológicas y clínicas de la oftalmoplejía |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Reporte de caso | American Journal of Ophthalmology | Dos pacientes con criptoftalmía unilateral |

## Información de Mercado en España

Se muestran 5 de las 8 autorizaciones. El registro no incluye el texto de la indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 10640005IP2 | SYCREST 10 MG comprimidos sublinguales | Comprimido sublingual | Organon N.V. |
| 10640002IP2 | SYCREST 5 MG comprimidos sublinguales | Comprimido sublingual | Organon N.V. |
| 10640002 | SYCREST 5 MG comprimidos sublinguales | Comprimido sublingual | Organon N.V. |
| 10640005IP3 | SYCREST 10 MG comprimidos sublinguales | Comprimido sublingual | Organon N.V. |
| 10640005IP | SYCREST 10 MG comprimidos sublinguales | Comprimido sublingual | Organon N.V. |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo TxGNN, sin ensayos clínicos ni literatura sobre asenapina, y no existe un vínculo mecanístico plausible con la distrofia retiniana. Con un nivel de evidencia L5 no se recomienda avanzar.

**Para avanzar se necesita:**
- Estudios preclínicos o de mecanismo que conecten los receptores de la asenapina con la biología retiniana
- Descargar el prospecto de la AEMPS para completar las advertencias y contraindicaciones, y poder hacer el cribado de seguridad
- Datos detallados del mecanismo de acción (MOA) desde DrugBank
- Confirmar la indicación original, ya que el campo está vacío en las fuentes

**Nota:** entre las 10 predicciones del modelo, la única con evidencia real es *trastorno afectivo mayor* (rango 10). Tiene 4 ensayos de Fase 3 completados (incluido NCT01244815, n=404), pero corresponde a una indicación ya aprobada (manía en trastorno bipolar I), por lo que no es reposicionamiento. Su recomendación es Proceed with Guardrails, con verificación de la indicación y la población (adulta o pediátrica) y vigilancia de efectos metabólicos, extrapiramidales y de sedación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

