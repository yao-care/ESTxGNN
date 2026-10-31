---
layout: default
title: Metformin
parent: Solo predicción del modelo (L5)
nav_order: 510
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-31
monitor_inn: "Metformin"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy"]
description: "Metformin: nueva indicación predicha, Classic stiff person syndrome (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Metformin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Metformin: Classic stiff person syndrome
{: .text-alpha }

## Resumen en Una Frase

Metformina es un antidiabético oral utilizado originalmente para el tratamiento de la diabetes mellitus tipo 2.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de la persona rígida clásico**,
pero actualmente **no hay ensayos clínicos ni publicaciones** en los datos compilados que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Classic stiff person syndrome |
| Puntaje de Predicción TxGNN | 0.9945 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 8) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, metformina es un fármaco de uso consolidado en la diabetes tipo 2, y su eficacia en esa indicación está comprobada, pero no existe un vínculo mecanístico claro con la nueva indicación.

El síndrome de la persona rígida es un trastorno neurológico autoinmune, típicamente asociado a anticuerpos anti-GAD65, que afecta a la neurotransmisión GABAérgica. La activación de AMPK y los posibles efectos inmunomoduladores de metformina solo constituyen una conexión especulativa.

El puntaje elevado (0.994) es únicamente una predicción del modelo.

## Otras Indicaciones Predichas

Todas con nivel de evidencia L5 y recomendación Hold, sin ensayos clínicos ni literatura:

| Enfermedad | Puntaje TxGNN | Comentario |
|---|---|---|
| Opsismodisplasia | 0.9940 | Displasia esquelética por mutaciones de INPPL1; posible conexión a nivel de vía PI3K/AKT, puramente hipotética |
| Síndrome de disfunción sensible a tiamina | 0.9940 | Posible vínculo especulativo con transportadores de tiamina; se trata con suplementos de tiamina |
| Lipodistrofia localizada inducida por fármacos | 0.9906 | Racional metabólico plausible pero indirecto; el mecanismo local difiere de la resistencia sistémica a la insulina |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones vigentes (todas de formulación única; ninguna cancelada). El texto de indicación aprobada no figura en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 89159 | Metformina Adair 850 mg EFG | Comprimido recubierto con película | No disponible |
| 84266 | Metformina Juta 850 mg EFG | Comprimido recubierto con película | No disponible |
| 83866 | Metformina Vir 1000 mg EFG | Comprimido recubierto con película | No disponible |
| 72221 | Metformina Viatris 850 mg EFG | Comprimido recubierto con película | No disponible |
| 85976 | Brotmin 1000 mg EFG | Comprimido recubierto con película | No disponible |

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación (según el grafo de conocimiento, no el prospecto)**: insuficiencia hepática, enfermedad hepática, enfermedad renal, pancreatitis, enfermedad de la vesícula biliar, insuficiencia cardíaca congestiva, insuficiencia suprarrenal (adrenocortical), hipopituitarismo y deficiencias hormonales hipofisarias (incluido el síndrome de Sheehan), hipogonadismo hipogonadotrópico (incluido el síndrome de Kallmann), enfermedad del timo y piouréter.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones; entre las mostradas destacan las de nivel **mayor** con **acetazolamida** y **etanol**. Hay además numerosas interacciones moderadas (por ejemplo, dolutegravir, abemaciclib, fenilefrina, ranitidina, formoterol, pseudoefedrina, ketorolaco, nifedipino, epinefrina, ibuprofeno, etinilestradiol, hidrocortisona, salbutamol, hidroclorotiazida y acetohexamida) y algunas menores (acarbosa y corticoides tópicos).

Las advertencias y contraindicaciones del prospecto no están disponibles; consultar el prospecto para la información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y sin un vínculo mecanístico claro entre metformina y el síndrome de la persona rígida.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de metformina para evaluar el vínculo mecanístico
- Revisión de la literatura y búsqueda de ensayos clínicos o estudios preclínicos en síndrome de la persona rígida
- Obtención y análisis del prospecto de la AEMPS (advertencias y contraindicaciones) para el cribado de seguridad
- Evaluación de compatibilidad de vía de administración y de la población diana, considerando las contraindicaciones señaladas y las interacciones mayores
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

