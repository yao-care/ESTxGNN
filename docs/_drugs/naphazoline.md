---
layout: default
title: Naphazoline
parent: Solo predicción del modelo (L5)
nav_order: 551
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Naphazoline: nueva indicación predicha, Hipotricosis simple del cuero cabelludo (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (los textos de indicación de la…"
monitor_inn: "naphazoline"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "primary hereditary glaucoma", "hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "open-angle glaucoma", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature"]
---

# Naphazoline
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Naphazolina: De Indicación Original no Especificada a Hipotricosis Simple del Cuero Cabelludo
{: .text-alpha }

## Resumen en Una Frase

Naphazolina es un vasoconstrictor agonista alfa-adrenérgico que se comercializa en España en forma de spray nasal, colirios y solución cutánea; en las fichas de autorización disponibles no consta un texto de indicación aprobada. El modelo TxGNN predice que podría ser efectivo para **hipotricosis simple del cuero cabelludo**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción, por lo que se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos). La información farmacológica la describe como vasoconstrictor que reduce el enrojecimiento ocular |
| Nueva Indicación Predicha | Hipotricosis simple del cuero cabelludo |
| Puntaje de Predicción TxGNN | 0,9983 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 5 de 7) |
| Número de Autorizaciones | 7 (vigentes: 5) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos de fármacos. Según la información farmacológica compilada, la naphazolina se une a los receptores adrenérgicos α1A, α2A y α2C (humanos), y es un vasoconstrictor que estrecha los vasos sanguíneos inflamados; se usa como descongestionante nasal y para aliviar el enrojecimiento ocular.

**La predicción no resulta mecanísticamente razonable.** La hipotricosis simple es un trastorno hereditario de origen genético (p. ej., CDSN, APCDD1), y no existe un vínculo farmacológico plausible con la agonista alfa-adrenérgica. Si acaso, la vasoconstricción de los vasos del cuero cabelludo podría ser contraproducente para la perfusión folicular. El puntaje alto proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni una señal farmacológica real.

Otras predicciones del modelo siguen el mismo patrón: congénita hipotricosis con milia, alopecia areata difusa, alopecia, hipertricosis y síndromes malformativos. Todas tienen nivel L5 y ninguna cuenta con ensayos clínicos. Es llamativo que se prediga tanto hipotricosis/alopecia como hipertricosis (fenotipo opuesto), lo que sugiere una señal inespecífica. La única predicción con una justificación de clase débil es la de glaucoma (los agonistas alfa, como la brimonidina, modulan la dinámica del humor acuoso), aunque la naphazolina carece de datos y presenta riesgos de seguridad en esa población.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 21032 | VASOCONSTRICTOR PENSA | Solución para pulverización nasal | No especificada |
| 81752 | OPTIALERG 5 MG/ML + 0,25 MG/ML colirio en solución | Colirio en solución | No especificada |
| 19763 | ALERGOFTAL 0,25 mg/ml + 5 mg/ml colirio en solución | Colirio en solución | No especificada |
| 56489 | OJOSBEL gotas oculares, 0,30 mg/0,08 ml | Colirio en solución | No especificada |
| 22414 | COLIROFTA ANESTESICO 5 MG/ML + 0,5 MG/ML | Colirio en solución | No especificada |

Se muestran 5 de las 7 autorizaciones vigentes (las otras dos son CENTILUX 0,25 mg/ml colirio y Epistaxol solución cutánea).

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad del grafo, no texto del prospecto): hipertensión, hiperglucemia, diabetes mellitus, cetoacidosis diabética, glaucoma de ángulo cerrado, enfermedad cardiovascular, cardiopatía, hipertiroidismo, enfermedad de Graves, tirotoxicosis, infecciones oculares y conjuntivitis.
- **Interacciones y dianas farmacológicas**: interacción con los receptores adrenérgicos α1A (ADRA1A), α2A (ADRA2A) y α2C (ADRA2C) en humanos, y con TAAR4P en ratón.
- **Relevancia para el glaucoma**: los simpaticomiméticos descongestionantes conllevan una advertencia de riesgo de cierre angular en pacientes predispuestos, por lo que los problemas de seguridad superan el beneficio especulativo en esa indicación.

No se dispone de advertencias ni contraindicaciones extraídas del prospecto; consultar el prospecto para confirmar la información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo computacional (L5), sin ensayos clínicos ni literatura de apoyo, y no existe un mecanismo plausible que vincule un vasoconstrictor alfa-adrenérgico con la hipotricosis hereditaria. Además, el perfil de seguridad cardiovascular y ocular no favorece su uso en nuevas indicaciones.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y una hipótesis biológica que conecte la agonista alfa-adrenérgica con la fisiología del folículo piloso
- Estudios preclínicos (modelos de folículo o animales) que respalden algún efecto sobre el crecimiento del cabello
- Obtención y análisis del prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas)
- Evaluación de compatibilidad de la vía de administración (las formas actuales son nasal, ocular y cutánea)
- Búsqueda de literatura específica, ya que actualmente no hay estudios relevantes
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

