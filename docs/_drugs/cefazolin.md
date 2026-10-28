---
layout: default
title: Cefazolin
parent: Solo predicción del modelo (L5)
nav_order: 154
evidence_level: L5
indication_count: 8
monitor_inn: "Cefazolin"
predicted_indications: ["infectious otitis media", "bronchitis", "middle ear disease", "chronic otitis media", "suppurative otitis media", "otosalpingitis", "non-suppurative otitis media", "allergic otitis media"]
last_modified_at: 2026-10-27
description: "Cefazolin: nueva indicación predicha, Otitis media infecciosa (infectious otitis media) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Cefazolin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Cefazolina: cefalosporina de primera generación (inhibidor de la síntesis de la pared bacteriana) → otitis media infecciosa (infectious otitis media)
{: .text-alpha }

## Resumen en Una Frase

Cefazolina es un antibiótico cefalosporínico de primera generación, de uso parenteral y con actividad frente a bacterias grampositivas.
El modelo TxGNN predice que podría ser efectivo para **otitis media infecciosa (infectious otitis media)**,
pero actualmente **no hay ensayos clínicos** registrados y la evidencia publicada es solo indirecta (2 publicaciones, ninguna con datos directos de eficacia de cefazolina en esta enfermedad).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Otitis media infecciosa (infectious otitis media) |
| Puntaje de Predicción TxGNN | 0,9944 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 13 de 13) |
| Número de Autorizaciones | 13 (vigentes: 13) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Por su clase, cefazolina es una cefalosporina de primera generación que inhibe la síntesis de la pared celular bacteriana y tiene actividad frente a estreptococos y *Staphylococcus aureus* sensible a meticilina.

Estos microorganismos son patógenos plausibles en la otitis media, lo que da un vínculo biológico coherente con la predicción. Sin embargo, la cobertura de patógenos clave de la otitis media (*H. influenzae*, *M. catarrhalis*) es limitada, y la cefazolina parenteral no es una opción habitual de primera línea.

El soporte es débil: las dos publicaciones asociadas son un informe de 2025 sobre terapia empírica ceftazidima-cefazolina en el síndrome de Gradenigo pediátrico (una complicación de la otitis media, no la otitis media en sí) y una revisión de 1986 sobre síndrome de Stevens-Johnson que no es pertinente. Ninguna estudia directamente la enfermedad predicha, por lo que el nivel de evidencia se limita a L5.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Reporte de caso/serie | Ann Otol Rhinol Laryngol | Terapia empírica con ceftazidima-cefazolina en síndrome de Gradenigo pediátrico, complicación de otitis media aguda |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Revisión | Clinical Pharmacy | Manejo del síndrome de Stevens-Johnson; la otitis media se menciona solo como antecedente del caso. No pertinente a esta indicación |

## Información de Mercado en España

Cefazolina está comercializada en España con autorizaciones vigentes de medicamentos de un solo principio activo (todas en polvo para solución inyectable, con o sin disolvente, y para perfusión). El texto de indicación aprobada no figura en los datos locales.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (nivel moderado): kanamicina, neomicina, estreptomicina y ácido picosulfúrico. Se registran además otras interacciones de nivel no clasificado, por ejemplo con anfotericina B, ácido acetilsalicílico, amoxicilina, metformina y morfina.

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (0,9944), pero no hay ensayos clínicos ni estudios que evalúen directamente cefazolina en la otitis media infecciosa. La plausibilidad mecanística es parcial, con cobertura limitada de patógenos habituales y una vía parenteral poco adecuada para esta enfermedad.

**Para avanzar se necesita:**
- Estudios clínicos o revisiones sistemáticas que evalúen cefazolina directamente en otitis media infecciosa
- Datos de sensibilidad de los patógenos actuales de otitis media frente a cefazolina
- Comparación con los tratamientos de primera línea vigentes (p. ej., amoxicilina)
- Datos del mecanismo de acción y de la información de seguridad del prospecto
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

