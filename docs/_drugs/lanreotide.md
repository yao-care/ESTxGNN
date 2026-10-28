---
layout: default
title: Lanreotide
parent: Solo predicción del modelo (L5)
nav_order: 450
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
monitor_inn: "Lanreotide"
predicted_indications: ["hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "Ambras type hypertrichosis universalis congenita"]
description: "Lanreotide: nueva indicación predicha, Hipertricosis (hypertrichosis (disease)) (hypertrichosis (disease)) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Lanreotide
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

## Lanreotide: Hipertricosis (hypertrichosis (disease)) (hypertrichosis (disease))
{: .text-alpha }

## Resumen en Una Frase

Lanreotida es un análogo de la somatostatina, utilizado originalmente para el tratamiento de la acromegalia (también asociada a hiperpituitarismo y gigantismo hipofisario).
El modelo TxGNN predice que podría ser efectivo para **hipertricosis**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Hipertricosis (hypertrichosis (disease)) (hypertrichosis (disease)) |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 6 de 10) |
| Número de Autorizaciones | 10 (vigentes: 6) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Según la información conocida, lanreotida es un análogo peptídico de la somatostatina que actúa sobre los receptores de somatostatina SST2, SST3 y SST5 (según los datos farmacológicos compilados). Mediante este mecanismo suprime la secreción de hormona del crecimiento (GH) y, de forma secundaria, de IGF-1, lo que explica su eficacia en acromegalia.

La relación con la hipertricosis es indirecta: la señalización de IGF-1 puede influir en la biología del folículo piloso, por lo que un vínculo es plausible en teoría. Sin embargo, la hipertricosis es clínicamente heterogénea (formas congénitas, inducidas por fármacos y adquiridas) y no existe evidencia que conecte la inhibición de GH/IGF-1 con su tratamiento.

Por lo tanto, este vínculo debe considerarse especulativo y sin verificar. La puntuación alta del modelo refleja una predicción del modelo TxGNN (aprendizaje profundo), no una validación clínica.

Otras predicciones del modelo (todas con evidencia L5 y recomendación Hold) son: síndrome de malformación con componente dental/periodontal (0.9996), síndrome con malformación de Dandy-Walker (0.9996), anomalía genética aislada del tallo piloso (0.9996) e hipertricosis universal congénita tipo Ambras (0.9996). Para ellas, el vínculo mecanístico es aún más débil o no creíble.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 64838 | Somatulina Autogel 90 mg | Solución inyectable en jeringa precargada | No disponible |
| 86176 | Myrelez 60 mg EFG | Solución inyectable en jeringa precargada | No disponible |
| 90113 | Lanreotida Sun 90 mg EFG | Solución inyectable en jeringa precargada | No disponible |
| 90111 | Lanreotida Sun 120 mg EFG | Solución inyectable en jeringa precargada | No disponible |
| 60914 | Somatulina 30 mg | Polvo y disolvente para suspensión inyectable de liberación prolongada | No disponible |

Se muestran 5 de las 10 autorizaciones vigentes (todas de principio activo único, ninguna cancelada).

## Consideraciones de Seguridad

- **Contraindicaciones / condiciones de precaución (según el grafo de conocimiento, no texto del prospecto)**: enfermedad hepática, enfermedad de la vesícula biliar (colelitiasis, colecistolitiasis, coledocolitiasis), hiperglucemia, hipoglucemia, hipotiroidismo (incluido mixedema e hipotiroidismo congénito), insuficiencia renal y trastornos hipertensivos (hipertensión).
- **Interacciones farmacológicas**: los datos compilados describen únicamente la farmacología de unión a receptores (SST2, SST3 y SST5); no se identificaron interacciones con otros fármacos con nivel de gravedad asignado.

Consultar el prospecto para la información de seguridad completa, ya que las advertencias y contraindicaciones oficiales no están disponibles.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (L5), sin ensayos clínicos ni literatura, y el vínculo mecanístico con la hipertricosis es especulativo.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas).
- Confirmar el mecanismo de acción en DrugBank para un análisis mecanístico más sólido.
- Realizar una revisión de literatura preclínica sobre somatostatina/GH/IGF-1 y biología del folículo piloso.
- Evaluar la compatibilidad de la vía de administración (pendiente) y definir la subpoblación de hipertricosis (adquirida vs. congénita) más plausible.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

