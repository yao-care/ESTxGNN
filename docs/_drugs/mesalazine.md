---
layout: default
title: Mesalazine
parent: Solo predicción del modelo (L5)
nav_order: 345
evidence_level: L5
indication_count: 7
---

# Mesalazine
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

# Mesalazina: De Colitis Ulcerosa a Hipotricosis Congénita con Distrofia Macular Juvenil

## Resumen en Una Frase

La mesalazina (5-ASA) es un antiinflamatorio que se usa originalmente para tratar la colitis ulcerosa y prevenir sus recaídas.
El modelo TxGNN predice que podría ser efectiva para la **hipotricosis congénita con distrofia macular juvenil**, una enfermedad hereditaria rara.
Actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción, que se apoya únicamente en el puntaje del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Colitis ulcerosa (según información farmacológica; el texto de indicación de las autorizaciones de la AEMPS no está disponible) |
| Nueva Indicación Predicha | Hipotricosis congénita con distrofia macular juvenil |
| Puntaje de Predicción TxGNN | 99.65% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, la mesalazina ejerce acción antiinflamatoria mediante inhibición de las vías de COX/LOX, agonismo de PPAR-gamma y modulación de NF-κB. Su eficacia en colitis ulcerosa y otras enfermedades inflamatorias intestinales está bien establecida.

En este caso, sin embargo, **no se identificó un vínculo mecanístico**. La hipotricosis congénita con distrofia macular juvenil es un trastorno hereditario raro relacionado con mutaciones en CDH3. Su patología no guarda relación conocida con las vías antiinflamatorias de la mesalazina.

Por ello, el puntaje del modelo (0.996) es el único respaldo de esta predicción. Debe tratarse como una señal computacional sin sustento biológico ni clínico verificado.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 62670 | PENTASA 1g granulado de liberación prolongada | Granulado de liberación modificada |
| 74791 | SALOFALK 3 g granulado de liberación prolongada | Granulado de liberación modificada |
| 61335 | CLAVERSAL espuma rectal | Espuma rectal |
| 65771 | SALOFALK 500 mg granulado de liberación prolongada | Granulado de liberación modificada |
| 037734011IP | MEZAVANT 1200 mg comprimidos de liberación prolongada gastrorresistentes | Comprimido de liberación prolongada |

Se muestran 5 de las 20 autorizaciones. También existen otras formas, como supositorios, suspensión rectal y comprimidos gastrorresistentes.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: Solo hay un registro farmacológico, la mesalazina con el receptor PPAR-gamma (PPARG). Es una interacción con una diana biológica, no una interacción clínica entre fármacos, y no indica un nivel de riesgo.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción solo cuenta con el puntaje de TxGNN (evidencia L5), sin ensayos, sin literatura y sin vínculo mecanístico plausible con una enfermedad hereditaria de origen no inflamatorio.

Entre las otras indicaciones predichas, la **osteoartritis** es la única con respaldo preclínico (evidencia L4, recomendación "Research Question"). Un estudio de 2024 en *Nature Communications* (PMID 38310093) describe que el 5-ASA suprime la osteoartritis a través del eje OSCAR-PPARγ. Es la línea con más fundamento biológico de este candidato, aunque aún no cuenta con ensayos clínicos.

**Para avanzar se necesita:**
- Un vínculo mecanístico documentado entre la mesalazina y la vía de CDH3, o una razón biológica alternativa.
- Datos detallados del mecanismo de acción (MOA) desde DrugBank.
- Advertencias y contraindicaciones del prospecto de la AEMPS.
- Priorizar la osteoartritis: replicación preclínica y revisión de seguridad y viabilidad antes de cualquier estudio clínico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

