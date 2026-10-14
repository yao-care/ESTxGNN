---
layout: default
title: Eculizumab
parent: Solo predicción del modelo (L5)
nav_order: 275
evidence_level: L5
indication_count: 10
---

# Eculizumab
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

# Eculizumab: De Hemoglobinuria Paroxística Nocturna a Hematopoyesis Cíclica

## Resumen en Una Frase

Eculizumab es un anticuerpo monoclonal inhibidor del complemento C5, utilizado originalmente para el tratamiento de la hemoglobinuria paroxística nocturna y la neuromielitis óptica.
El modelo TxGNN predice que podría ser efectivo para **hematopoyesis cíclica**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden directamente esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hemoglobinuria paroxística nocturna y neuromielitis óptica (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Hematopoyesis cíclica |
| Puntaje de Predicción TxGNN | 99,97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, eculizumab es un inhibidor del componente C5 del complemento, que bloquea la vía terminal del complemento. Su eficacia en enfermedades mediadas por complemento, como la hemoglobinuria paroxística nocturna, está establecida.

Sin embargo, la relación mecanística con la nueva indicación **no está respaldada** por los datos. La hematopoyesis cíclica (neutropenia cíclica) se asocia típicamente a mutaciones en *ELANE* que alteran la regulación de los precursores de neutrófilos, y no a una patología mediada por el complemento. El puntaje elevado de TxGNN (99,97%) es una predicción basada únicamente en el grafo de conocimiento y debe interpretarse con cautela.

Otras predicciones del modelo con puntajes similares (neutropenias congénitas graves por deficiencia de JAGN1, CXCR2 o CSF3R, neutropenia idiopática del adulto, entre otras) tampoco cuentan con evidencia clínica ni mecanismo plausible de inhibición de C5.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para hematopoyesis cíclica.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1231727001 | BEKEMV 300 mg concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos compilados |
| 07393001 | SOLIRIS 300 mg concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos compilados |
| 1231735001 | EPYSQLI 300 mg concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 4 interacciones de nivel menor con distintas formulaciones de inmunoglobulina G humana (intravenosa, subcutánea, intramuscular, e intravenosa y subcutánea).

Para advertencias y contraindicaciones, consultar el prospecto. Como dato general, la inhibición del complemento aumenta el riesgo de infecciones graves, en particular meningocócicas, algo especialmente relevante en pacientes con inmunodeficiencia de base.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya exclusivamente en el puntaje del modelo (nivel L5), sin ensayos clínicos, sin literatura directamente relevante y sin un vínculo mecanístico plausible entre la inhibición de C5 y la hematopoyesis cíclica.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción y un análisis mecanístico que justifique el papel del complemento en esta enfermedad
- Estudios preclínicos o de mecanismo que muestren una implicación del complemento en la hematopoyesis cíclica
- Revisión del prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas)
- Evaluación del perfil de riesgo-beneficio, en especial el riesgo de infecciones por la inhibición del complemento
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

