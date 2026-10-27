---
layout: default
title: Fostamatinib
parent: Solo predicción del modelo (L5)
nav_order: 361
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Fostamatinib: nueva indicación predicha, Trombocitopenia autosómica con plaquetas normales (nivel de evidencia L5). Indicación original: Trombocitopenia por destrucción inmune"
monitor_inn: "FOSTAMATINIB"
predicted_indications: ["autosomal thrombocytopenia with normal platelets", "non-syndromic esophageal malformation"]
---

# Fostamatinib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Fostamatinib: De Trombocitopenia por Destrucción Inmune a Trombocitopenia Autosómica con Plaquetas Normales
{: .text-alpha }

## Resumen en Una Frase

Fostamatinib es un inhibidor de la tirosina quinasa SYK, originalmente utilizado para el tratamiento de la trombocitopenia por destrucción inmune.
El modelo TxGNN predice que podría ser efectivo para **trombocitopenia autosómica con plaquetas normales**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trombocitopenia por destrucción inmune |
| Nueva Indicación Predicha | Trombocitopenia autosómica con plaquetas normales |
| Puntaje de Predicción TxGNN | 99.45% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos compilada. Según la información conocida, fostamatinib es un inhibidor de SYK cuyo metabolito activo (R406) reduce la destrucción de plaquetas mediada por anticuerpos en los macrófagos, lo que explica su eficacia en la trombocitopenia inmune.

La nueva indicación predicha es una trombocitopenia hereditaria (autosómica), cuyo origen no es la destrucción inmune de plaquetas. Por ello, el vínculo mecanístico es débil. El puntaje elevado del modelo (99.45%) probablemente refleja la cercanía en la red de conocimiento con el fenotipo de trombocitopenia, más que un mecanismo patogénico compartido.

En conclusión, la predicción debe considerarse con cautela: no hay estudios que respalden un vínculo real y la similitud entre ambas indicaciones está pendiente de evaluar.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1191405002 | TAVLESSE 150 MG comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |
| 1191405001 | TAVLESSE 100 MG comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |

Ambas autorizaciones son de Instituto Grifols S.A., vigentes y de principio activo único.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las principales:
  - **Mayor**: claritromicina.
  - **Moderadas**: inhibidores de la bomba de protones y antiácidos (rabeprazol, omeprazol, dexlansoprazol, cimetidina), corticoides (hidrocortisona, betametasona, budesonida, triamcinolona, dexametasona), aprepitant, alosetrón, alvimopán, dolasetrón, dronabinol, eliglustat, empagliflozina, loperamida, pioglitazona y morfina.

Para advertencias y contraindicaciones, consultar el prospecto. Para el uso en una condición del desarrollo o hereditaria, el análisis previo señala posibles preocupaciones como hipertensión, hepatotoxicidad y toxicidad embrio-fetal.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos ni literatura, y el mecanismo de acción de fostamatinib (frenar la destrucción inmune de plaquetas) no se corresponde con una trombocitopenia hereditaria. No hay base suficiente para avanzar.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA), por ejemplo desde DrugBank
- Revisión de advertencias y contraindicaciones del prospecto de AEMPS
- Evidencia preclínica o clínica que vincule la inhibición de SYK con la trombocitopenia autosómica
- Evaluación del perfil de seguridad (hipertensión, hepatotoxicidad, toxicidad embrio-fetal) en la población objetivo
- Análisis de similitud con la indicación original y de compatibilidad de vía de administración
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

