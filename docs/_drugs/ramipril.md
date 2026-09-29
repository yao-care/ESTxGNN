---
layout: default
title: Ramipril
parent: Solo predicción del modelo (L5)
nav_order: 454
evidence_level: L5
indication_count: 10
---

# Ramipril
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

# Ramipril: De Inhibidor de la ECA a Hipertensión Pulmonar por Enfermedad Pulmonar o Hipoxia

## Resumen en Una Frase

Ramipril es un inhibidor de la enzima convertidora de angiotensina (ECA) que está comercializado en España en forma de comprimidos.
El modelo TxGNN predice que podría ser efectivo para **hipertensión pulmonar por enfermedad pulmonar y/o hipoxia**, pero actualmente hay **0 ensayos clínicos** y **20 publicaciones** que no evalúan ramipril en esta enfermedad, así que la predicción se apoya solo en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Hipertensión pulmonar por enfermedad pulmonar y/o hipoxia |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Ramipril pertenece a la clase de los inhibidores de la ECA, que bloquean la formación de angiotensina II. Los textos de indicación de las autorizaciones españolas tampoco están disponibles, por lo que no se puede citar una indicación original.

Mecanísticamente, la inhibición de la ECA podría influir en el tono vascular pulmonar y en la remodelación de los vasos a través del sistema renina-angiotensina. Esa es la única base de la predicción.

Esta plausibilidad es débil. Las 20 publicaciones recuperadas tratan de biología general de la hipoxia (cerebro, cáncer, inmunidad, altitud) y ninguna estudia ramipril ni otro inhibidor de la ECA en hipertensión pulmonar. El puntaje alto del modelo no está respaldado por evidencia clínica ni específica del fármaco.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Las publicaciones recuperadas son casi todas revisiones generales sobre hipoxia. Ninguna evalúa ramipril. Se listan las 10 más cercanas al tema respiratorio o de la hipoxia.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Revisión | Respiratory Care Clinics of North America | Describe los cuatro mecanismos básicos de la hipoxemia (bajo oxígeno ambiental, hipoventilación, desajuste ventilación-perfusión y cortocircuito derecha-izquierda). |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Revisión | Journal of Cellular Biochemistry | Explica cómo las células y los tejidos responden a la hipoxia, incluida su relación con enfermedades vasculares, inflamatorias y el cáncer. |
| [24557798](https://pubmed.ncbi.nlm.nih.gov/24557798/) | 2014 | Revisión | Journal of Applied Physiology | Revisión general sobre hipoxia (sin resumen disponible). |
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Revisión | Ageing Research Reviews | Analiza el efecto de la hipoxia sobre el envejecimiento cerebral y las enfermedades neurodegenerativas. |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Revisión | Metabolic Brain Disease | Evidencia clínica y mecanismos moleculares del deterioro cognitivo causado por hipoxia. |
| [31961750](https://pubmed.ncbi.nlm.nih.gov/31961750/) | 2020 | Sin clasificar | Annual Review of Immunology | Papel de la hipoxia en la inmunidad innata y la inflamación. |
| [28219680](https://pubmed.ncbi.nlm.nih.gov/28219680/) | 2017 | Sin clasificar | Experimental Cell Research | Regulación de la represión transcripcional en hipoxia mediada por HIF. |
| [40815459](https://pubmed.ncbi.nlm.nih.gov/40815459/) | 2025 | Revisión | Revista Médica del IMSS | Hipoxia hipobárica por altitud y adaptación de las poblaciones de altura. |
| [9446167](https://pubmed.ncbi.nlm.nih.gov/9446167/) | 1997 | Sin clasificar | Revue Médicale de Liège | Trabajo sobre el síndrome hepatopulmonar (sin resumen disponible). |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Revisión | Clinical Oncology | Modificación terapéutica de la hipoxia tumoral y su relación con la resistencia a la radioterapia. |

## Información de Mercado en España

Ramipril tiene 20 autorizaciones en España. Se muestran las 5 principales.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 67880 | Ramipril Aristo 2,5 mg comprimidos EFG | Comprimido |
| 73549 | Ramipril Tecnigen 2,5 mg comprimidos EFG | Comprimido |
| 65104 | Acovil 10 mg comprimidos | Comprimido |
| 73787 | Ramipril Combix 10 mg comprimidos EFG | Comprimido |
| 76966 | Ramipril Alter 10 mg comprimidos EFG | Comprimido |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje muy alto (99.93%), pero es solo del modelo (nivel L5). No hay ensayos clínicos, y la literatura recuperada no evalúa ramipril ni los inhibidores de la ECA en hipertensión pulmonar.

**Para avanzar se necesita:**
- Búsqueda dirigida de estudios preclínicos o clínicos de inhibidores de la ECA en hipertensión pulmonar (por ejemplo, ramipril y modelos de hipertensión pulmonar por hipoxia).
- Datos de mecanismo de acción desde DrugBank, para analizar el vínculo mecanístico.
- Advertencias y contraindicaciones de la ficha técnica de la AEMPS, necesarias antes de cualquier evaluación de seguridad.
- Como referencia, entre las demás predicciones del modelo, la oclusión de arteria cerebral tiene más apoyo (nivel L4, con estudios preclínicos y un estudio humano pequeño). Podría ser una hipótesis más prometedora para explorar.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

