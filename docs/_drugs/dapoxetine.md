---
layout: default
title: Dapoxetine
parent: Solo predicción del modelo (L5)
nav_order: 156
evidence_level: L5
indication_count: 3
---

# Dapoxetine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Dapoxetina: De Eyaculación Precoz a Migraña

## Resumen en Una Frase

Dapoxetina es un inhibidor selectivo de la recaptación de serotonina (ISRS) de acción corta, utilizado originalmente para el tratamiento de la eyaculación precoz.
El modelo TxGNN predice que podría ser efectivo para **migraña (trastorno de migraña)**, pero actualmente hay **0 ensayos clínicos** y solo **2 publicaciones** de relación indirecta, por lo que la predicción sigue siendo una hipótesis de investigación.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Eyaculación precoz (según la farmacología de referencia; los registros de AEMPS no incluyen el texto de indicación) |
| Nueva Indicación Predicha | Trastorno de migraña |
| Puntaje de Predicción TxGNN | 99.34% |
| Nivel de Evidencia | L4 (solo evidencia indirecta a nivel de clase de fármaco) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Dapoxetina actúa como inhibidor selectivo de la recaptación de serotonina, con el transportador SERT (gen *SLC6A4*) como diana. No se dispone de datos detallados del mecanismo de acción en DrugBank. La descripción anterior procede de la ficha farmacológica. Su perfil es de absorción rápida y vida media corta, diseñado para uso a demanda.

La relación con la migraña es indirecta y se da a nivel de clase: la modulación serotoninérgica es biológicamente plausible en la migraña, y los ISRS se han explorado como usos fuera de indicación. Sin embargo, la evidencia de los ISRS en la profilaxis de la migraña es débil e inconsistente, y no hay datos que muestren que dapoxetina en particular haya sido estudiada en migraña.

Además, su perfil a demanda y de vida media corta encaja mal con un uso profiláctico continuo. El puntaje alto de TxGNN (0.993) es únicamente una predicción computacional, y el razonamiento mecanístico es una inferencia, no una confirmación.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33998993](https://pubmed.ncbi.nlm.nih.gov/33998993/) | 2022 | Revisión | Current Neuropharmacology | Revisión de los usos fuera de indicación de los ISRS, incluida la migraña. Evidencia a nivel de clase, no específica de dapoxetina |
| [23504864](https://pubmed.ncbi.nlm.nih.gov/23504864/) | 2013 | Cohorte | Urologia | Cumplimiento del tratamiento con dapoxetina en pacientes con eyaculación precoz. No aborda la migraña |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 70875 | PRILIGY 60 mg comprimidos recubiertos con película | Comprimido recubierto con película | Phoenix Labs Unlimited Company |
| 70874 | PRILIGY 30 mg comprimidos recubiertos con película | Comprimido recubierto con película | Phoenix Labs Unlimited Company |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos y la literatura disponible es indirecta (una revisión general de ISRS y un estudio sobre eyaculación precoz). El perfil farmacocinético a demanda no encaja con la profilaxis de la migraña, así que el puntaje de TxGNN no basta por sí solo para avanzar.

Las otras dos predicciones, **trastorno distímico** (99.14%) y **migraña con aura de tronco encefálico** (99.11%), tampoco tienen ensayos ni literatura específica (nivel L5), y también quedan en Hold.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de AEMPS (advertencias y contraindicaciones), un dato que bloquea el cribado de seguridad.
- Completar el mecanismo de acción desde DrugBank.
- Buscar estudios específicos de dapoxetina en migraña y valorar la evidencia de ISRS en profilaxis migrañosa, con especial atención a la compatibilidad con una pauta a demanda.
- Definir si la migraña es realmente una pregunta de investigación prioritaria frente a otros candidatos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

