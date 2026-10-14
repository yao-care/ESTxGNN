---
layout: default
title: Agomelatine
parent: Solo predicción del modelo (L5)
nav_order: 27
evidence_level: L5
indication_count: 10
---

# Agomelatine
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

# Agomelatina: De Trastorno Depresivo Mayor a Tortícolis Paroxística Benigna de la Infancia

## Resumen en Una Frase

Agomelatina es un antidepresivo con acción melatoninérgica (agonista MT1/MT2) y antagonista serotoninérgico 5-HT2C, utilizado originalmente para el tratamiento de la depresión unipolar, la depresión endógena, el trastorno depresivo mayor y los trastornos de ansiedad.
El modelo TxGNN predice que podría ser efectivo para **tortícolis paroxística benigna de la infancia**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Depresión unipolar / trastorno depresivo mayor (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Tortícolis paroxística benigna de la infancia |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la literatura revisada para este informe, agomelatina actúa como agonista de los receptores melatoninérgicos MT1 y MT2 y como antagonista del receptor serotoninérgico 5-HT2C. Esto puede normalizar los ritmos circadianos, mejorar el sueño de ondas lentas y aumentar la liberación de dopamina y noradrenalina en la corteza prefrontal. Los datos farmacológicos compilados confirman además su unión a los receptores 5-HT2A, 5-HT2B, 5-HT2C, MT1 y MT2. No se dispone de datos detallados de mecanismo de acción en la fuente principal de fármacos, por lo que esta descripción procede de la literatura y no ha podido contrastarse.

La tortícolis paroxística benigna de la infancia es un trastorno episódico neurológico, relacionado con el espectro migrañoso. El vínculo con la indicación original es plausible, pero no está demostrado: la modulación melatoninérgica y 5-HT2C podría ser relevante para fenómenos neurológicos episódicos. La similitud con la indicación original no ha sido evaluada.

El puntaje del modelo (99.96%) es una predicción basada en el grafo de conocimiento y no sustituye a la evidencia clínica. Hay que ser especialmente prudente porque se trata de una población pediátrica, mientras que agomelatina está autorizada en adultos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se han compilado 20 autorizaciones vigentes (todas de monofármaco, ninguna cancelada). Los textos de indicación aprobada no estaban disponibles en los datos. Se listan las 5 principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 08499003 | VALDOXAN 25 mg comprimidos recubiertos con película (Servier) | Comprimido recubierto con película | No disponible en los datos |
| 08498003 | THYMANAX 25 mg comprimidos recubiertos con película (Servier Ireland) | Comprimido recubierto con película | No disponible en los datos |
| 83546 | AGOMELATINA STADA 25 mg EFG | Comprimido recubierto con película | No disponible en los datos |
| 83360 | AGOMELATINA RATIOPHARM 25 mg EFG | Comprimido recubierto con película | No disponible en los datos |
| 83440 | AGLONEX 25 mg EFG (Accord Healthcare) | Comprimido recubierto con película | No disponible en los datos |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas / Farmacología de dianas**: los datos compilados no incluyen interacciones con otros fármacos, sino la unión de agomelatina a sus dianas: receptores 5-HT2A, 5-HT2B, 5-HT2C, MT1 y MT2.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún ensayo clínico ni publicación para esta indicación; el puntaje alto de TxGNN es una predicción basada en grafos y no puede contrastarse con el mecanismo de acción por falta de datos. Además, la población diana es pediátrica.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA)
- Prospecto de AEMPS con advertencias y contraindicaciones, necesario antes de cualquier evaluación de seguridad
- Revisión sistemática de la literatura sobre melatonina/5-HT2C en tortícolis paroxística benigna y migraña pediátrica
- Evaluación de la seguridad y la justificación de uso en población pediátrica
- Evidencia preclínica o clínica específica que respalde el vínculo mecanístico

### Otras indicaciones predichas (contexto)

Para otras indicaciones del ranking, la evidencia es más sólida pero indirecta y en su mayoría solapa con las indicaciones ya aprobadas:

| Indicación | Puntaje TxGNN | Nivel de Evidencia | Observación |
|------|------|------|------|
| Melancolía | 99.88% | L4 | Metaanálisis en red de antidepresivos, no específicos del subtipo melancólico |
| Depresión neurótica | 99.88% | L4 | Mismo conjunto de literatura, evidencia indirecta |
| Trastorno distímico | 99.86% | L4 | Metaanálisis de ECA de antidepresivos en distimia, no específico de agomelatina |

Estas indicaciones son las más prometedoras para una futura investigación, aunque constituyen sobre todo una extensión de la indicación depresiva ya aprobada y no un reposicionamiento genuino.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

