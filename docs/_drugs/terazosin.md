---
layout: default
title: Terazosin
parent: Solo predicción del modelo (L5)
nav_order: 779
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
monitor_inn: "terazosin"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "migraine disorder", "migraine with brainstem aura", "Raynaud disease", "Ambras type hypertrichosis universalis congenita", "manic bipolar affective disorder", "kyphoscoliotic heart disease"]
description: "Terazosin: nueva indicación predicha, Hipotricosis simple del cuero cabelludo (hypotrichosis simplex of the scalp) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Terazosin
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

## Terazosin: Hipotricosis simple del cuero cabelludo (hypotrichosis simplex of the scalp)
{: .text-alpha }

## Resumen en Una Frase

Terazosina es un bloqueador alfa-1 adrenérgico, utilizado originalmente para el tratamiento de la hipertensión arterial y la hiperplasia prostática benigna.
El modelo TxGNN predice que podría ser efectivo para **hipotricosis simple del cuero cabelludo**, pero **no existen ensayos clínicos ni publicaciones** que respalden esta predicción (solo la puntuación del modelo).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Hipotricosis simple del cuero cabelludo (hypotrichosis simplex of the scalp) |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 11 de 17) |
| Número de Autorizaciones | 17 (vigentes: 11) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, terazosina es un antagonista selectivo de los receptores alfa-1 adrenérgicos, que produce vasodilatación y relajación del músculo liso del cuello vesical y la próstata. Su eficacia en hipertensión e hiperplasia prostática benigna está bien establecida.

Para la hipotricosis simple del cuero cabelludo, un trastorno genético del folículo piloso, **no se identifica un vínculo mecanístico plausible** con el bloqueo alfa-1. La puntuación elevada proviene del modelo TxGNN (aprendizaje profundo) y probablemente refleja similitudes que el modelo aprendió entre enfermedades relacionadas con el cabello, no evidencia biológica ni un mecanismo validado.

Cabe señalar que otras predicciones del mismo modelo para terazosina tienen más respaldo: **migraña** (nivel L3, un estudio clínico pequeño de 1994 y una revisión de 1997) y **fenómeno/enfermedad de Raynaud** (nivel L3, un estudio pequeño de 1997, con plausibilidad biológica por la vasoconstricción alfa-adrenérgica). Estas podrían ser candidatas más sólidas como preguntas de investigación, aunque la evidencia sigue siendo limitada y antigua.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 17 autorizaciones vigentes (todas de principio activo único). El texto de indicación aprobada no está disponible en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 69087 | Terazosina Cinfa 5 mg comprimidos EFG | Comprimido | No disponible |
| 69086 | Terazosina Cinfa 2 mg comprimidos EFG | Comprimido | No disponible |
| 63476 | Sutif 5 mg comprimidos | Comprimido | No disponible |
| 63980 | Terazosina Alter 5 mg comprimidos EFG | Comprimido | No disponible |
| 63458 | Zayasel 1 mg/ml solución oral EFG | Solución oral | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proviene del prospecto): atrofia multisistémica, síndrome de taquicardia postural ortostática, hipotensión ortostática, priapismo y síndrome de iris flácido intraoperatorio.
- **Interacciones Farmacológicas**: se registraron 137 interacciones. Las principales de nivel moderado incluyen corticoesteroides (hidrocortisona, dexametasona, betametasona, prednisona, prednisolona, triamcinolona, budesonida), bupropión, morfina (incluida la liposomal), opio, inhibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina, ertugliflozina), dronabinol y nabilona. Para calcitriol, pantoprazol y glimepirida el nivel no está determinado.
- Para advertencias y contraindicaciones del prospecto, consultar el prospecto autorizado por la AEMPS.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en la puntuación del modelo (nivel L5), sin ensayos ni literatura, y no existe un vínculo mecanístico plausible entre el bloqueo alfa-1 y la hipotricosis simple del cuero cabelludo, por lo que probablemente sea un artefacto del modelo TxGNN (aprendizaje profundo).

**Para avanzar se necesita:**
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones) de la AEMPS
- Evidencia preclínica que respalde un papel del bloqueo alfa-1 en el folículo piloso
- Valorar priorizar otras indicaciones predichas con mayor respaldo (migraña y enfermedad de Raynaud), mediante ensayos aleatorizados con potencia adecuada y evaluando el riesgo de hipotensión ortostática
- Evaluar la viabilidad de una vía de administración adecuada (por ejemplo, tópica), ya que la compatibilidad de vía aún no se ha determinado
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

