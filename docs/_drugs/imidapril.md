---
layout: default
title: Imidapril
parent: Solo predicción del modelo (L5)
nav_order: 274
evidence_level: L5
indication_count: 5
---

# Imidapril
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Imidapril: De Hipertensión Arterial a Hipertensión Pulmonar por Enfermedad Pulmonar y/o Hipoxia

## Resumen en Una Frase

Imidapril es un inhibidor de la enzima convertidora de angiotensina (IECA), una clase de fármacos que se usa para tratar la hipertensión arterial.
El modelo TxGNN predice que podría ser efectivo para la **hipertensión pulmonar por enfermedad pulmonar y/o hipoxia**,
pero **no hay ensayos clínicos** y las **20 publicaciones** recuperadas tratan de la hipoxia en general, sin mencionar imidapril.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en las autorizaciones de la AEMPS (el campo está vacío). Por su clase (IECA), se asume hipertensión arterial |
| Nueva Indicación Predicha | Hipertensión pulmonar por enfermedad pulmonar y/o hipoxia |
| Puntaje de Predicción TxGNN | 99,78 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 12 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Por su clase, imidapril inhibe la ACE, lo que reduce la angiotensina II y la vasoconstricción mediada por el sistema renina-angiotensina-aldosterona (SRAA). Su uso en hipertensión arterial sistémica es la base de su perfil terapéutico.

La conexión con la nueva indicación es plausible pero débil. El SRAA podría intervenir en la vasoconstricción y el remodelado vascular pulmonar inducidos por hipoxia. Sin embargo, ninguna evidencia aportada une imidapril con esta enfermedad. El puntaje de 99,78 % es solo una predicción basada en grafos de conocimiento y no constituye evidencia clínica.

Además, hay argumentos en contra. Los IECA no tienen beneficio establecido en la hipertensión pulmonar del grupo 3, y la vasodilatación sistémica podría empeorar el equilibrio ventilación-perfusión. La segunda predicción (hipertensión pulmonar de mecanismo multifactorial poco claro) tiene exactamente el mismo puntaje. Esto sugiere que ambas comparten vecindad en el grafo y no que existan evidencias independientes.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Se recuperaron 20 publicaciones, ninguna de las cuales estudia imidapril ni el tratamiento de la hipertensión pulmonar. Todas son revisiones o investigación básica sobre hipoxia en general, y su relevancia sigue pendiente de evaluación. Se muestran las 10 más relevantes, priorizando revisiones.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Revisión | Ageing Research Reviews | Hipoxia y envejecimiento cerebral: efectos neurodegenerativos frente a posibles efectos neuroprotectores |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Revisión | Metabolic Brain Disease | Deterioro cognitivo por hipoxia aguda y crónica: evidencia clínica y mecanismos moleculares |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Revisión | Journal of Cellular Biochemistry | Respuesta celular a la hipoxia y su papel en enfermedad vascular, inflamación y cáncer |
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Revisión | Respiratory Care Clinics of North America | Mecanismos básicos de la hipoxemia (incluido el desajuste ventilación-perfusión) |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Revisión | Clinical Oncology | Modificación terapéutica de la hipoxia tumoral y su relación con la resistencia a radioterapia |
| [31706510](https://pubmed.ncbi.nlm.nih.gov/31706510/) | 2019 | Revisión | Trends in Cancer | Desubiquitinasas, factores inducibles por hipoxia (HIF) y cáncer |
| [40815459](https://pubmed.ncbi.nlm.nih.gov/40815459/) | 2025 | Revisión | Revista Médica del IMSS | Hipoxia hipobárica y adaptación en habitantes de altitud |
| [40347693](https://pubmed.ncbi.nlm.nih.gov/40347693/) | 2025 | Revisión | Redox Biology | Papel de la hipoxia en la esclerosis múltiple |
| [24557798](https://pubmed.ncbi.nlm.nih.gov/24557798/) | 2014 | Revisión | Journal of Applied Physiology | Revisión general sobre hipoxia (sin resumen disponible) |
| [37328448](https://pubmed.ncbi.nlm.nih.gov/37328448/) | 2023 | Investigación básica | Advanced Science | Modificación de ARNm (ac4C) y adicción a la glucólisis en cáncer gástrico bajo hipoxia |

## Información de Mercado en España

Imidapril figura con 12 autorizaciones. Se muestran las 5 principales; el texto de indicación aprobada no está disponible en los registros.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 83139 | IMIDAPRIL QUALIGEN 5 MG COMPRIMIDOS EFG | Comprimido | Neuraxpharm Spain S.L. |
| 63425 | HIPERTENE 5 mg COMPRIMIDOS | Comprimido | Laboratorios Bial S.A. |
| 83141 | IMIDAPRIL QUALIGEN 20 MG COMPRIMIDOS EFG | Comprimido | Neuraxpharm Spain S.L. |
| 83177 | IMIDAPRIL ASIBILAN 20 MG COMPRIMIDOS EFG | Comprimido | Neuraxpharm Pharmaceuticals S.L. |
| 83179 | IMIDAPRIL DARI PHARMA 20 MG COMPRIMIDOS EFG | Comprimido | Dari Pharma S.L. |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se dispone de advertencias, contraindicaciones ni interacciones farmacológicas registradas.

Del análisis del mecanismo de las predicciones se desprenden dos precauciones de clase:
- **Hipertensión pulmonar por hipoxia**: la vasodilatación sistémica podría empeorar el equilibrio ventilación-perfusión.
- **Hipertensión renovascular**: los IECA pueden causar lesión renal aguda en estenosis bilateral de la arteria renal o en riñón único. También hay que vigilar la función renal, el potasio y el volumen.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (nivel L5): no hay ensayos clínicos y ninguna publicación vincula imidapril con la hipertensión pulmonar. Además, existe una razón fisiopatológica de cautela, porque los IECA no tienen beneficio establecido en la hipertensión pulmonar del grupo 3.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), que es un requisito bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una búsqueda bibliográfica dirigida a imidapril o IECA en hipertensión pulmonar, con estudios preclínicos o de mecanismo como mínimo.
- Valorar las otras predicciones, más coherentes con la clase farmacológica: la enfermedad renal hipertensiva maligna y la hipertensión renovascular maligna (ambas con puntaje de 99,76 %, nivel L5, "pregunta de investigación"). Estas exigirían un diseño que priorice la seguridad renal.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

