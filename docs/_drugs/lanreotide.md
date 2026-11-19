---
layout: default
title: Lanreotide
parent: Solo predicción del modelo (L5)
nav_order: 450
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-20
monitor_inn: "Lanreotide"
predicted_indications: ["hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "Ambras type hypertrichosis universalis congenita"]
description: "Lanreotide: nueva indicación predicha, Hipertricosis (hypertrichosis (disease)) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 10 (comercializadas: 6; autorizadas no comercializadas: 3)"
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

## Lanreotide: Hipertricosis (hypertrichosis (disease))
{: .text-alpha }

## Resumen en Una Frase

Lanreotida es un análogo de la somatostatina, utilizado originalmente para el tratamiento de la acromegalia (también asociada a hiperpituitarismo y gigantismo hipofisario).
El modelo TxGNN predice que podría ser efectivo para **hipertricosis**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Hipertricosis (hypertrichosis (disease)) |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 6 de 10; autorizadas no comercializadas: 3; revocadas o suspendidas: 1) |
| Número de Autorizaciones | 10 (comercializadas: 6) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Lanreotide (traducción no oficial): «La lanreotida, el componente activo de SOMATULINE DEPOT, es un análogo octapeptídico de la somatostatina natural. Se cree que el mecanismo de acción de la lanreotida es similar al de la somatostatina natural.» Texto original en inglés: "Lanreotide, the active component of SOMATULINE DEPOT is an octapeptide analog of natural somatostatin. The mechanism of action of lanreotide is believed to be similar to that of natural somatostatin." ([DailyMed: Somatuline Depot (lanreotide acetate) prescribing information, Ipsen Biopharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6e4a41fd-a753-4362-87ee-8cc56ed3660d), versión del 2024-10-11; consultado el 2026-11-19). Según la información conocida, lanreotida es un análogo peptídico de la somatostatina que actúa sobre los receptores de somatostatina SST2, SST3 y SST5 (según los datos farmacológicos compilados). Mediante este mecanismo suprime la secreción de hormona del crecimiento (GH) y, de forma secundaria, de IGF-1, lo que explica su eficacia en acromegalia.

La relación con la hipertricosis es indirecta: la señalización de IGF-1 puede influir en la biología del folículo piloso, por lo que un vínculo es plausible en teoría. Sin embargo, la hipertricosis es clínicamente heterogénea (formas congénitas, inducidas por fármacos y adquiridas) y no existe evidencia que conecte la inhibición de GH/IGF-1 con su tratamiento.

Por lo tanto, este vínculo debe considerarse especulativo y sin verificar. La puntuación alta del modelo refleja una predicción del modelo TxGNN (aprendizaje profundo), no una validación clínica.

Otras predicciones del modelo (todas con evidencia L5 y recomendación Hold) son: síndrome de malformación con componente dental/periodontal (0.9996), síndrome con malformación de Dandy-Walker (0.9996), anomalía genética aislada del tallo piloso (0.9996) e hipertricosis universal congénita tipo Ambras (0.9996). Para ellas, el vínculo mecanístico es aún más débil o no creíble.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

<!-- review:begin es-lic-20261105-lanreotide-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Se muestran 5 de las 10 autorizaciones vigentes (todas de principio activo único, ninguna cancelada)." Eliminado: afirmaba que el medicamento no está autorizado o comercializado en España, o que sus autorizaciones están revocadas o suspendidas, lo que no coincide con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 10 autorizaciones (comercializadas: 6); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en España. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-lanreotide-1 -->

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 64838 | Somatulina Autogel 90 mg | Solución inyectable en jeringa precargada | No disponible |
| 86176 | Myrelez 60 mg EFG | Solución inyectable en jeringa precargada | No disponible |
| 90113 | Lanreotida Sun 90 mg EFG | Solución inyectable en jeringa precargada | No disponible |
| 90111 | Lanreotida Sun 120 mg EFG | Solución inyectable en jeringa precargada | No disponible |
| 60914 | Somatulina 30 mg | Polvo y disolvente para suspensión inyectable de liberación prolongada | No disponible |

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

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Se muestran 5 de las 10 autorizaciones vigentes (todas de principio activo único, ninguna cancelada)" | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Somatuline Depot (lanreotide acetate) prescribing information, Ipsen Biopharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6e4a41fd-a753-4362-87ee-8cc56ed3660d) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

