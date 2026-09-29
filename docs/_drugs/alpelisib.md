---
layout: default
title: Alpelisib
parent: Solo predicción del modelo (L5)
nav_order: 32
evidence_level: L5
indication_count: 1
---

# Alpelisib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Alpelisib: De Cáncer de Mama HR+/HER2- Avanzado a Hipertensión Pulmonar

## Resumen en Una Frase

Alpelisib es un inhibidor selectivo de PI3Kα, comercializado en España como Piqray y utilizado en cáncer de mama avanzado HR+/HER2-.
El modelo TxGNN predice que podría ser efectivo para **hipertensión pulmonar**, pero **ningún ensayo clínico** lo respalda y las **2 publicaciones** encontradas apuntan más bien a posibles riesgos (toxicidad pulmonar y cardíaca).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos de autorización de la AEMPS (el texto de indicación está vacío). El contexto de los ensayos y del producto apunta a cáncer de mama avanzado HR+/HER2- |
| Nueva Indicación Predicha | Hipertensión pulmonar |
| Puntaje de Predicción TxGNN | 99,03% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, alpelisib es un inhibidor selectivo de la isoforma alfa de la PI3K (PI3Kα). Su eficacia se ha estudiado en cáncer de mama avanzado HR+/HER2-, y mecanísticamente podría ser aplicable a la hipertensión pulmonar.

La vía PI3K/Akt participa en la proliferación de las células musculares lisas de las arterias pulmonares y en el remodelado vascular, procesos centrales de la hipertensión pulmonar. Esto ofrece una base plausible, pero **no demostrada**, para la predicción.

Conviene interpretar el puntaje con cautela. El 99,03% es solo una predicción computacional, y ningún estudio clínico ni preclínico de los datos analizados prueba alpelisib en hipertensión pulmonar. Además, la literatura disponible sugiere posible daño: enfermedad pulmonar intersticial y señales de atrofia cardíaca con la inhibición de PI3Kα. Como faltan las indicaciones originales y el MOA en DrugBank, no fue posible contrastar este razonamiento con la ficha técnica.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06705504](https://clinicaltrials.gov/study/NCT06705504) | N/A | Completado | 435 | Estudio retrospectivo no intervencionista (REASSURE) en cáncer de mama avanzado HR+/HER2- tratado con ribociclib o alpelisib. No estudia hipertensión pulmonar; probable coincidencia de palabras clave (relevancia C) |

Este ensayo no aporta evidencia a favor de la nueva indicación.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | Reporte de caso | J Oncol Pharm Pract | Enfermedad pulmonar intersticial inducida por alpelisib en una paciente con cáncer de mama avanzado. Señal de toxicidad pulmonar |
| [31039672](https://pubmed.ncbi.nlm.nih.gov/31039672/) | 2019 | Estudio preclínico (animal) | J Am Heart Assoc | La inhibición de PI3Kα con doxorrubicina produjo atrofia biventricular, remodelado y disfunción del ventrículo derecho. Señal de riesgo cardíaco |

Ninguna publicación evalúa alpelisib como tratamiento de la hipertensión pulmonar. Ambas describen posibles efectos adversos.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1201455005 | PIQRAY 50 mg y 200 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos de la autorización |
| 1201455008 | PIQRAY 200 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos de la autorización |
| 1201455002 | PIQRAY 150 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos de la autorización |

Titular de las tres autorizaciones: Novartis Europharm Limited.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor selectivo de PI3Kα) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

Los datos de seguridad de la AEMPS (advertencias y contraindicaciones) no están disponibles y no se encontraron interacciones farmacológicas registradas. Consultar el prospecto para información de seguridad.

La literatura revisada señala dos aspectos a vigilar si se explorara esta nueva indicación:
- **Toxicidad pulmonar**: un caso de enfermedad pulmonar intersticial asociada a alpelisib.
- **Riesgo cardíaco**: en un modelo animal, la inhibición de PI3Kα se asoció con disfunción del ventrículo derecho, órgano especialmente relevante en la hipertensión pulmonar.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos ni estudios que evalúen alpelisib en hipertensión pulmonar. Las señales de seguridad disponibles, pulmonares y del ventrículo derecho, apuntan en sentido contrario a un beneficio.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), que es un vacío bloqueante para el cribado de seguridad.
- Obtener el mecanismo de acción desde DrugBank.
- Estudios preclínicos que evalúen la inhibición de PI3Kα en modelos de hipertensión pulmonar, prestando atención a la función del ventrículo derecho.
- Una revisión de la biología de PI3K en la vasculatura pulmonar para confirmar si la inhibición sería beneficiosa o perjudicial.

*Este informe es solo para fines de investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

