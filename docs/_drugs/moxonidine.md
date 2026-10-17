---
layout: default
title: Moxonidine
parent: Solo predicción del modelo (L5)
nav_order: 545
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Moxonidine: nueva indicación predicha, Hipotricosis simple del cuero cabelludo (nivel de evidencia L5). Indicación original: Hipertensión (esencial)"
monitor_inn: "Moxonidine"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "malignant hypertensive renal disease", "primary hereditary glaucoma"]
---

# Moxonidine
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

# Moxonidina: De Hipertensión a Hipotricosis Simple del Cuero Cabelludo

## Resumen en Una Frase

Moxonidina es un antihipertensivo de acción central, utilizado originalmente para el tratamiento de la hipertensión.
El modelo TxGNN predice que podría ser efectivo para **hipotricosis simple del cuero cabelludo**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión (esencial) |
| Nueva Indicación Predicha | Hipotricosis simple del cuero cabelludo |
| Puntaje de Predicción TxGNN | 99,95% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado en los datos compilados para este informe. Según la información conocida, moxonidina es un agonista de los receptores de imidazolina I1 y de los adrenoceptores alfa-2 de acción central, que reduce el tono simpático y, con ello, la presión arterial. Los datos farmacológicos confirman su unión a los adrenoceptores α2A, α2B y α2C.

La hipotricosis simple es un trastorno genético del folículo piloso (por ejemplo, variantes en CDSN, APCDD1 o RPL21). No se conoce ninguna vía que conecte el flujo simpático o los receptores de imidazolina con estos genes. **Por tanto, no se ha establecido un vínculo mecanístico plausible.**

El puntaje elevado de TxGNN refleja una predicción basada en la estructura del grafo de conocimiento, probablemente por proximidad en la red con otros nodos de enfermedades capilares, y no una base biológica demostrada. La predicción debe interpretarse con cautela.

### Otras predicciones del modelo (todas de nivel L5, sin ensayos clínicos)

| Posición | Indicación predicha | Puntaje TxGNN | Comentario |
|------|------|------|------|
| 2 | Hipotricosis congénita con milia | 99,94% | Sin vínculo mecanístico plausible |
| 3 | Alopecia areata difusa | 99,91% | Trastorno autoinmune (JAK/STAT, IFN-γ); sin acción inmunomoduladora conocida de moxonidina |
| 4 | Alopecia | 99,90% | La única publicación asociada no evalúa el fármaco |
| 5 | Enfermedad renal hipertensiva maligna | 99,67% | Cercana a la indicación aprobada, pero sin datos; una urgencia hipertensiva no es un buen escenario para un fármaco oral de acción central |
| 6 | Hipertensión renovascular maligna | 99,67% | Adyacente a la indicación actual; sin evidencia |
| 7 | Hipertensión pulmonar por enfermedad pulmonar o hipoxia | 99,66% | Mecanismo no relacionado con el objetivo del fármaco |
| 8 | Hipertensión pulmonar de mecanismo multifactorial poco claro | 99,66% | Probable asociación por la etiqueta "hipertensión" |
| 9 | Síndrome de Braddock | 99,62% | Enfermedad ultrarrara; no evaluable |
| 10 | Glaucoma hereditario primario | 99,54% | Candidato no cardiovascular biológicamente más plausible (clase de agonistas α2 como brimonidina), pero sin datos oculares |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para hipotricosis simple del cuero cabelludo.

Cabe señalar que para la predicción de "alopecia" (posición 4) se recuperó una publicación ([PMID 40007390](https://pubmed.ncbi.nlm.nih.gov/40007390/), 2024, *Georgian Medical News*, reporte de caso) sobre el síndrome de Graham-Little-Piccardi-Lasseur, una variante del liquen plano pilar. No evalúa moxonidina y no aporta evidencia clínica del fármaco; probablemente se recuperó por coincidencia de palabras clave.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 61158 | MOXON 0,4 mg comprimidos recubiertos con película | Comprimido recubierto | Hipertensión (según la base de conocimiento; el texto de indicación no está disponible) |
| 61157 | MOXON 0,3 mg comprimidos recubiertos con película | Comprimido recubierto | Hipertensión (según la base de conocimiento; el texto de indicación no está disponible) |
| 61156 | MOXON 0,2 mg comprimidos recubiertos con película | Comprimido recubierto | Hipertensión (según la base de conocimiento; el texto de indicación no está disponible) |

Las tres autorizaciones están vigentes, son de monofármaco y su titular es Viatris Healthcare Limited.

## Consideraciones de Seguridad

- **Interacciones farmacológicas / farmacología:** la consulta se completó y devolvió 3 registros, todos de farmacología (no interacciones con otros medicamentos): moxonidina actúa sobre los adrenoceptores α2A, α2B y α2C humanos. No se identificaron interacciones con otros fármacos.

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo (nivel L5): no hay ensayos clínicos ni literatura sobre moxonidina en hipotricosis, y no existe un vínculo mecanístico plausible con un trastorno genético del folículo piloso.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) del fármaco y análisis de su posible relación con la biología del folículo piloso.
- Advertencias y contraindicaciones del prospecto de la AEMPS, que son necesarias para cualquier evaluación de seguridad.
- Evidencia preclínica (modelos de folículo piloso) que justifique cualquier estudio posterior.
- Evaluación de compatibilidad de vía de administración (los productos disponibles son solo orales; una indicación capilar probablemente requeriría otra vía).
- Priorizar, en caso de querer explorar alguna de las otras predicciones, las de mayor plausibilidad biológica, como el glaucoma hereditario primario, aunque también carecen de datos clínicos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

