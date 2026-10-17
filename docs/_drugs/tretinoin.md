---
layout: default
title: Tretinoin
parent: Solo predicción del modelo (L5)
nav_order: 822
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tretinoin: nueva indicación predicha, Nodulosis reumatoide (nivel de evidencia L5). Indicación original: Acné, leucemia promielocítica aguda…"
monitor_inn: "Tretinoin"
predicted_indications: ["rheumatoid nodulosis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis", "juvenile idiopathic arthritis", "juvenile chronic polyarthritis", "spondyloarthropathy, susceptibility to", "juvenile arthritis due to defect in LACC1", "osteoarthritis", "pseudoachondroplasia", "acromesomelic dysplasia, Hunter-Thompson type", "Quinquaud's folliculitis decalvans"]
---

# Tretinoin
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

# Tretinoína: De Acné a Nodulosis Reumatoide

## Resumen en Una Frase

La tretinoína (ácido retinoico todo-trans) es un retinoide utilizado originalmente para el tratamiento del acné, la leucemia promielocítica aguda, la queratosis adquirida y la queratodermia palmoplantar.
El modelo TxGNN predice que podría ser efectiva para la **nodulosis reumatoide**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden directamente esta dirección: se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Acné, leucemia promielocítica aguda, queratosis adquirida y queratodermia palmoplantar (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Nodulosis reumatoide |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción original del fármaco. Según la información conocida, la tretinoína es un retinoide que actúa como ligando de los receptores del ácido retinoico (RAR-α, RAR-β y RAR-γ), y además interactúa con otros receptores nucleares como PPAR-β/δ, RORB, NR2C2 (receptor testicular 4) y NR2E1 (TLX). Se utiliza como agente diferenciador en la leucemia promielocítica aguda y para normalizar la queratinización en trastornos cutáneos como el acné.

La relación entre las indicaciones originales (dermatológicas y hematológicas) y la nodulosis reumatoide es indirecta. Un vínculo plausible, pero no verificado, sería la modulación retinoide de la señalización inmunitaria e inflamatoria (por ejemplo, efectos sobre la diferenciación de los linfocitos T y la producción de citocinas). Esta hipótesis es especulativa para los nódulos reumatoides en particular.

Conviene destacar que las demás predicciones de mayor puntaje (artritis idiopática juvenil y sus variantes, espondiloartropatía, osteoartritis, displasias esqueléticas) tampoco cuentan con evidencia clínica. Todas reflejan probablemente la proximidad en la red del grafo de conocimiento y no una base farmacológica establecida. Entre las predicciones del listado, la foliculitis decalvante de Quinquaud (rango 10) parece mecanísticamente más verosímil por la acción dermatológica de la tretinoína, aunque tampoco está verificada.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la nodulosis reumatoide.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 65396 | VESANOID 10 mg CÁPSULAS BLANDAS | Cápsula blanda | No disponible en los datos compilados |
| 52751 | NEOCARE 4 mg/g CREMA | Crema | No disponible en los datos compilados |
| 60140 | RETIRIDES 0,25 MG/G CREMA | Crema | No disponible en los datos compilados |
| 60142 | RETIRIDES 1 MG/G CREMA | Crema | No disponible en los datos compilados |
| 60141 | RETIRIDES 0,5 MG/G CREMA | Crema | No disponible en los datos compilados |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Agente diferenciador (retinoide) usado en leucemia promielocítica aguda; no es un citotóxico convencional clásico |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad del grafo, no texto de prospecto): quemadura solar, trastornos de ansiedad y neuróticos, trastorno distímico, enfermedad renal, pioureter, pancreatitis, enfermedad hepática, enfermedad de la vesícula biliar, insuficiencia cardíaca congestiva, insuficiencia suprarrenal y enfermedad de Addison, enfermedad de Crohn y enfermedad inflamatoria intestinal, eccema/dermatitis atópica, osteoporosis (incluida la posmenopáusica), trastornos psicóticos y mentales (esquizofreniforme, esquizoafectivo), micosis fungoide y linfomas cutáneos de células T relacionados, diabetes mellitus y cetoacidosis diabética.
- **Interacciones farmacológicas**: se identificaron 7 interacciones de tipo farmacológico con receptores diana (RAR-α, RAR-β, RAR-γ, PPAR-β/δ, RORB, NR2C2 y NR2E1). Son relaciones de unión a receptores, sin nivel de gravedad clínica asignado.
- **Consideraciones específicas de las predicciones**: el uso pediátrico de tretinoína sistémica (relevante para las predicciones de artritis juvenil) plantearía preocupaciones de seguridad (teratogenicidad, toxicidad ósea y mucocutánea). En displasias esqueléticas, los retinoides pueden alterar el desarrollo esquelético.

Las advertencias principales del prospecto de la AEMPS no están disponibles; consultar el prospecto para la información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje de TxGNN es alto (99.84%), pero no existe ningún ensayo clínico ni publicación que respalde el uso de tretinoína en la nodulosis reumatoide (nivel L5). Además, el mecanismo de acción original y los datos de seguridad del prospecto no están disponibles, y el perfil de contraindicaciones del grafo es amplio.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), un requisito previo para cualquier evaluación de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión sistemática de la literatura sobre retinoides en nodulosis reumatoide y artritis inflamatoria.
- Establecer estudios preclínicos que respalden el vínculo mecanístico (por ejemplo, equilibrio Th17/Treg).
- Evaluar si otras predicciones, como la foliculitis decalvante, ofrecen una hipótesis más sólida y mejor alineada con la vía tópica ya comercializada.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

