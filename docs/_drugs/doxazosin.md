---
layout: default
title: Doxazosin
parent: Evidencia moderada (L3-L4)
nav_order: 263
evidence_level: L4
indication_count: 2
last_modified_at: 2026-10-31
monitor_inn: "Doxazosin"
predicted_indications: ["migraine disorder", "migraine with brainstem aura"]
description: "Doxazosin: nueva indicación predicha, Trastorno de migraña (migraine disorder) (nivel de evidencia L4). Indicación original: No consta en los datos locales"
---

# Doxazosin
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **2** 
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

## Doxazosin: Trastorno de migraña (migraine disorder)
{: .text-alpha }

## Resumen en Una Frase

Doxazosina es un antagonista selectivo de los receptores adrenérgicos alfa-1, utilizado originalmente para tratar la hipertensión y la hiperplasia prostática benigna.
El modelo TxGNN predice que podría ser efectivo para **migraña (trastorno de migraña)**,
pero actualmente solo cuenta con **0 ensayos clínicos** y **1 publicación** (una revisión/discusión de 1997 con 10 pacientes) que respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Trastorno de migraña (migraine disorder) |
| Puntaje de Predicción TxGNN | 0.9920 |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 14) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, doxazosina es un antagonista selectivo de los receptores adrenérgicos alfa-1. Los datos de farmacología confirman su unión a los receptores α1A, α1B y α1D (genes ADRA1A, ADRA1B y ADRA1D). Su eficacia en hipertensión y en hiperplasia prostática benigna está bien establecida.

La señalización adrenérgica modula el tono vascular cerebral y las vías noradrenérgicas centrales, que podrían intervenir en la fisiopatología de la migraña. Esto ofrece un vínculo biológicamente plausible, pero no demostrado. Este razonamiento se infiere de la farmacología conocida del fármaco, no de datos de mecanismo aportados directamente.

El puntaje de 0,9920 es una predicción computacional y no constituye evidencia clínica. Además, el modelo predice también "migraña con aura del tronco encefálico" (0,9919), un subtipo de migraña sin ensayos ni literatura propios; esa predicción hereda la hipótesis general de migraña y debería abordarse dentro de la misma pregunta de investigación, no por separado.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9074296](https://pubmed.ncbi.nlm.nih.gov/9074296/) | 1997 | Revisión / discusión | Headache | Diez pacientes con migraña en una consulta de neurología general recibieron terazosina o doxazosina. Nueve de diez presentaron menor frecuencia o gravedad de las migrañas, pero 5 abandonaron el tratamiento por efectos secundarios. No se notificaron reacciones adversas graves. |

Se trata de una serie de casos pequeña y sin control, con valor limitado como evidencia.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 75010 | Doxazosina Neo Viatris 4 mg comprimidos de liberación prolongada EFG | Comprimido de liberación prolongada | No disponible |
| 70679 | Doxazosina Neo Aurovitas Spain 4 mg comprimidos de liberación prolongada EFG | Comprimido de liberación prolongada | No disponible |
| 62930 | Progandol Neo 8 mg comprimidos de liberación modificada | Comprimido de liberación modificada | No disponible |
| 58861 | Progandol 4 mg comprimidos | Comprimido | No disponible |
| 3400937625784 | Carduran Neo 8 mg comprimidos de liberación modificada | Comprimido de liberación prolongada | No disponible |

Se muestran 5 de las 20 autorizaciones vigentes (todas de medicamento monocomponente, ninguna cancelada).

---

## Consideraciones de Seguridad

- **Contraindicaciones asociadas (según el grafo de conocimiento, no según el prospecto)**: atrofia multisistémica, síndrome de taquicardia postural ortostática, hipotensión ortostática, insuficiencia hepática, enfermedad hepática, enfermedad de la vesícula biliar, trastornos hipotensivos, estenosis pilórica, priapismo, síndrome del iris flácido intraoperatorio y obstrucción intestinal.
- **Interacciones Farmacológicas**: la consulta se completó con 3 registros, que corresponden a la unión a los receptores adrenérgicos α1A, α1B y α1D (interacciones farmacológicas con dianas), no a interacciones con otros medicamentos. En una población migrañosa no hipertensa, el efecto hipotensor del fármaco debe considerarse con especial atención.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en un puntaje del modelo y en una serie de 10 casos de 1997 sin control, sin ensayos clínicos registrados (nivel L4). Además, 5 de los 10 pacientes abandonaron el tratamiento por efectos secundarios, y el efecto hipotensor es una preocupación en pacientes no hipertensos. Se mantiene como pregunta de investigación.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank para fortalecer el vínculo mecanístico.
- Advertencias y contraindicaciones del prospecto de la AEMPS (actualmente sin datos), requisito previo para cualquier cribado de seguridad.
- Revisión sistemática de la literatura sobre bloqueadores alfa-1 en profilaxis de migraña.
- Estudios preclínicos o un ensayo piloto controlado, con evaluación del riesgo de hipotensión en población normotensa.
- Tratar la migraña con aura del tronco encefálico dentro de la misma pregunta de investigación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

