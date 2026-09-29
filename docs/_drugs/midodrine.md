---
layout: default
title: Midodrine
parent: Solo predicción del modelo (L5)
nav_order: 354
evidence_level: L5
indication_count: 10
---

# Midodrine
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

# Midodrina: De Indicación No Registrada a Prionopatía Variablemente Sensible a Proteasas

## Resumen en Una Frase

La midodrina es un profármaco cuyo metabolito activo, la desglimidodrina, es un agonista alfa-1 adrenérgico periférico. En la ficha de la AEMPS analizada no consta el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectiva para **prionopatía variablemente sensible a proteasas**, pero hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción, por lo que es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de la AEMPS |
| Nueva Indicación Predicha | Prionopatía variablemente sensible a proteasas |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados de mecanismo de acción en DrugBank. Según la información conocida, la midodrina se convierte por hidrólisis enzimática en desglimidodrina, que estimula selectivamente los receptores alfa-1 periféricos. Esto produce vasoconstricción arterial y venosa y aumenta la presión arterial.

Este mecanismo **no tiene una relación plausible** con la prionopatía variablemente sensible a proteasas, una enfermedad neurodegenerativa por mal plegamiento de la proteína priónica. El agonismo alfa-1 periférico no actúa sobre el plegamiento proteico ni sobre la neurodegeneración, y la desglimidodrina apenas atraviesa la barrera hematoencefálica. El puntaje alto del modelo debe leerse como una señal computacional, no como un indicio biológico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 65058 | GUTRON 5 mg COMPRIMIDOS (Cheplapharm Arzneimittel GmbH) | Comprimido | No disponible |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas en la consulta realizada.

## Otras Predicciones Relevantes del Mismo Paquete

- **Trastorno hipotensivo (posición 4, puntaje 99.90%)**: es la única predicción con evidencia sustancial, con 9 ensayos clínicos y 19 publicaciones. Incluye estudios directos de midodrina en hipotensión posterior a anestesia espinal (NCT05548985, completado, n=58), hipotensión intradialítica (NCT03431194, completado, n=80) e insuficiencia cardíaca con hipotensión (NCT06405555, en reclutamiento). Estos datos respaldan el uso ya establecido del fármaco, así que es más una indicación en ficha técnica que un reposicionamiento real.
- **Discrepancia de nivel**: el paquete le asigna L1 (Proceed with Guardrails), pero solo hay un ensayo de Fase 3 completado (NCT02307565, n=19). Con la regla de niveles, el nivel correspondería más bien a L2 y conviene revisarlo.
- **Salvaguardas señaladas**: hipertensión en decúbito supino (advertencia destacada), bradicardia refleja, retención urinaria y precaución en insuficiencia cardíaca y renal.
- **TDAH (posiciones 3 y 5)**: solo hay un vínculo noradrenérgico especulativo. El único ensayo (NCT05159687) evalúa atomoxetina en síncope vasovagal, no midodrina.
- **Bloqueo y enfermedad del nodo sinoauricular (posiciones 6 y 10)**: no aportan beneficio esperado, y la bradicardia refleja de la midodrina es un riesgo.
- **Restantes (posiciones 2, 7, 8 y 9)**: sin evidencia ni vínculo mecanístico.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de prionopatía se basa solo en el modelo, sin ensayos, literatura ni vínculo mecanístico plausible.

**Para avanzar se necesita:**
- Descartar esta indicación como candidata prioritaria, salvo que aparezca evidencia preclínica.
- Descargar y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicación aprobada).
- Completar los datos de mecanismo de acción desde DrugBank.
- Revisar el nivel de evidencia de la indicación de hipotensión, hoy L1, según las reglas de niveles.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

