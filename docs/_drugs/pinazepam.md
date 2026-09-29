---
layout: default
title: Pinazepam
parent: Solo predicción del modelo (L5)
nav_order: 426
evidence_level: L5
indication_count: 7
---

# Pinazepam
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Pinazepam: De Indicación Original No Disponible a Insomnio

## Resumen en Una Frase

Pinazepam es una benzodiazepina comercializada en España como DUNA, pero los datos recibidos no incluyen su indicación original aprobada.
El modelo TxGNN predice que podría ser efectivo para **Insomnio**,
pero solo hay **1 ensayo clínico** (no relevante, porque no evalúa pinazepam ni ningún hipnótico) y **ninguna publicación** que respalden esta dirección. Por ahora es una predicción del modelo sin evidencia propia.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (los textos de indicación de las autorizaciones de AEMPS están vacíos) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.95% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, pinazepam es una benzodiazepina 1,4 que se metaboliza a N-desmetildiazepam (nordazepam), un modulador alostérico positivo del receptor GABA-A con efecto ansiolítico. Los estudios farmacocinéticos y de metabolismo incluidos respaldan esta conversión.

El insomnio es una indicación frecuente en la clase de las benzodiazepinas, por su acción sedante-hipnótica a través de GABA-A. Por eso el vínculo mecanístico es plausible. Sin embargo, la revisión de 1984 sobre pinazepam señala que tiene un efecto hipnótico particularmente bajo y poca alteración de la coordinación motora, lo que matiza esta hipótesis.

En los datos no hay ningún estudio de pinazepam en insomnio. El puntaje alto de TxGNN es solo una predicción y no sustituye a la evidencia clínica.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04151485](https://clinicaltrials.gov/study/NCT04151485) | No aplicable | Desconocido | 177 | ECA de un programa psicológico mente-cuerpo para fertilidad (versión húngara) en mujeres en reproducción asistida. No evalúa pinazepam ni ningún hipnótico; relevancia baja (grado C). |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para insomnio.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 53885 | DUNA 5 mg cápsulas duras | Cápsula dura |
| 53886 | DUNA 10 mg cápsulas duras | Cápsula dura |
| 53884 | DUNA 2,5 mg cápsulas duras | Cápsula dura |

Las tres autorizaciones pertenecen a Meiji Pharma Spain S.A. Los datos recibidos no incluyen el texto de la indicación aprobada.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como nota de clase, las benzodiazepinas tienen riesgo propio de abuso y dependencia. Esto debe tenerse en cuenta en cualquier uso nuevo. No se encontraron interacciones farmacológicas registradas para pinazepam en la consulta realizada.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación de insomnio tiene nivel de evidencia L5: solo hay predicción del modelo, y el único ensayo vinculado es una intervención conductual sin relación con pinazepam. Además, faltan los datos de seguridad del prospecto de AEMPS, por lo que no se puede avanzar al cribado de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias, contraindicaciones e indicación aprobada).
- Obtener el mecanismo de acción desde DrugBank.
- Buscar estudios clínicos de pinazepam o de su metabolito N-desmetildiazepam en insomnio.
- Evaluar el riesgo de abuso y dependencia antes de cualquier ampliación de uso.
- Como referencia, la predicción de **ansiedad** (rank 6) tiene más respaldo (nivel L4, con una revisión farmacológica de 1984). Podría ser una línea de investigación más sólida que insomnio.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

