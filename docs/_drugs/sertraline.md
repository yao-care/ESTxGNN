---
layout: default
title: Sertraline
parent: Solo predicción del modelo (L5)
nav_order: 490
evidence_level: L5
indication_count: 8
---

# Sertraline
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

# Sertralina: De Trastorno Depresivo Mayor a Trastorno Esquizoide de la Personalidad

## Resumen en Una Frase

La sertralina es un inhibidor selectivo de la recaptación de serotonina (ISRS), utilizado clínicamente sobre todo para el trastorno depresivo mayor y otros trastornos de ansiedad.
El modelo TxGNN predice que podría ser efectiva para el **trastorno esquizoide de la personalidad**, pero hay **0 ensayos clínicos** y solo **2 publicaciones**, ninguna con relación directa con esta indicación.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastorno depresivo mayor (según el uso clínico descrito en la base farmacológica; los registros de la AEMPS no incluyen texto de indicación) |
| Nueva Indicación Predicha | Trastorno esquizoide de la personalidad |
| Puntaje de Predicción TxGNN | 99,93 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente. Según la información conocida, la sertralina es un ISRS que actúa sobre el transportador de serotonina (SERT, gen SLC6A4). Su eficacia en depresión y ansiedad está comprobada.

Los datos aportados no respaldan un vínculo plausible con los rasgos centrales del trastorno esquizoide de la personalidad, que son el desapego afectivo y el rango emocional restringido. El puntaje alto de TxGNN (0,9993) es solo una predicción del modelo. Además, las cuatro primeras predicciones (trastornos esquizoide, paranoide, esquizotípico e histriónico) comparten exactamente el mismo puntaje, por lo que este valor no permite distinguir entre ellas.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [19794312](https://pubmed.ncbi.nlm.nih.gov/19794312/) | 2009 | Otro (terapia multimodal) | Int Clin Psychopharmacol | Tratamiento combinado (dieta, terapia cognitivo-conductual y sertralina) en 30 pacientes con trastorno por atracón. No guarda relación directa con el trastorno esquizoide. |
| [21163152](https://pubmed.ncbi.nlm.nih.gov/21163152/) | 2010 | Reporte de caso | Dermatol Online J | Caso de lupus eritematoso discoide hipertrófico. No está relacionado con la indicación predicha. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 84732 | Sertralina Cinfa 150 mg comprimidos recubiertos con película | Comprimido recubierto con película |
| 59717 | Besitran 50 mg comprimidos recubiertos con película | Comprimido recubierto con película |
| 65922 | Sertralina Normon 100 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 65997 | Sertralina Cuve 50 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 66116 | Sertralina Qualigen Farma 50 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |

Se muestran 5 de las 20 autorizaciones registradas.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos y la literatura aportada es indirecta o no relacionada. Sin un vínculo mecanístico plausible, la predicción se queda en el nivel L5 (solo predicción del modelo).

**Para avanzar se necesita:**
- Estudios clínicos o de mecanismo específicos en trastorno esquizoide de la personalidad.
- Datos de mecanismo de acción y de advertencias y contraindicaciones del prospecto de la AEMPS.
- Como referencia, entre las predicciones del mismo fármaco, la **agorafobia** (puntaje 99,54 %) tiene nivel L2 y recomendación "Proceed with Guardrails", respaldada por metaanálisis en red y ensayos de sertralina en trastorno de pánico. Sin embargo, podría tratarse de una indicación ya establecida y no de un verdadero reposicionamiento.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

