---
layout: default
title: Zuclopenthixol
parent: Solo predicción del modelo (L5)
nav_order: 869
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Zuclopenthixol: nueva indicación predicha, Distrofia retiniana con o sin anomalías extraoculares (nivel de evidencia L5). Indicación original: Esquizofrenia (según las relaciones de indicación del gr…"
monitor_inn: "zuclopenthixol"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "hydranencephaly (disease)", "congenital disorder of glycosylation with defective fucosylation", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "myopia X-linked", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "syndromic myopia", "myopia 26, X-linked, female-limited", "atypical glycine encephalopathy"]
---

# Zuclopenthixol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Zuclopentixol: De Esquizofrenia a Distrofia Retiniana (con o sin anomalías extraoculares)
{: .text-alpha }

## Resumen en Una Frase

Zuclopentixol es un antipsicótico utilizado originalmente para el tratamiento de la esquizofrenia.
El modelo TxGNN predice que podría ser efectivo para **distrofia retiniana con o sin anomalías extraoculares**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Esquizofrenia (según las relaciones de indicación del grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Distrofia retiniana con o sin anomalías extraoculares |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información general conocida, zuclopentixol es un antipsicótico tipo tioxanteno que se considera antagonista de los receptores dopaminérgicos D1/D2. Este punto no está confirmado en los datos disponibles y debe verificarse. Su eficacia en esquizofrenia está establecida, pero no existe un vínculo mecanístico demostrado con la nueva indicación.

Las distrofias retinianas son, en su mayoría, enfermedades monogénicas, estructurales o degenerativas. No hay una justificación plausible por la cual el antagonismo de receptores dopaminérgicos modifique su curso. El alto puntaje de TxGNN (0.99994) refleja una predicción basada en el grafo de conocimiento, sin respaldo clínico ni bibliográfico.

Por ello, esta predicción debe considerarse una hipótesis de bajo respaldo. La similitud con la indicación original queda pendiente de análisis, y la compatibilidad de vías de administración tampoco ha sido evaluada.

### Otras predicciones del modelo (todas con nivel L5, sin ensayos ni literatura)

| Rango | Enfermedad predicha | Puntaje TxGNN | Comentario |
|---|---|---|---|
| 2 | Hidranencefalia | 99.99% | Malformación cerebral congénita estructural; sin papel plausible para un antagonista dopaminérgico |
| 3 | Trastorno congénito de la glicosilación con fucosilación defectuosa | 99.99% | Trastorno metabólico de la biosíntesis de glicanos; sin acción conocida del fármaco |
| 4 | Enfermedad de Charcot-Marie-Tooth desmielinizante tipo 1G | 99.99% | Neuropatía hereditaria; sin vía conocida hacia la mielina |
| 5 | Miopía ligada al X | 99.99% | La dopamina retiniana interviene en el crecimiento ocular, pero un antagonista se esperaría en sentido opuesto; hipótesis especulativa |
| 6 | Polimicrogiria perisilviana con hipoplasia cerebelosa y artrogriposis | 99.99% | Malformación del desarrollo; sin papel corrector plausible |
| 7 | Miopía sindrómica | 99.99% | Un antagonista D2 no se espera beneficioso y podría ser contraproducente |
| 8 | Miopía 26 ligada al X, limitada a mujeres | 99.99% | Misma salvedad que otras miopías; forma monogénica |
| 9 | Encefalopatía atípica por glicina | 99.99% | Error innato del metabolismo; los antipsicóticos pueden reducir el umbral convulsivo |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 6816281CIP | CLOPIXOL DEPOT 200 MG/ML SOLUCIÓN INYECTABLE | Solución inyectable | No disponible en los datos compilados |
| 60873 | CLOPIXOL 25 mg COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | No disponible en los datos compilados |
| 60875 | CLOPIXOL ACUFASE 50 mg/ml SOLUCIÓN INYECTABLE | Solución inyectable | No disponible en los datos compilados |
| 60872 | CLOPIXOL 10 mg COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | No disponible en los datos compilados |
| 6816281C | CLOPIXOL DEPOT 200 MG/ML SOLUCIÓN INYECTABLE | Solución inyectable | No disponible en los datos compilados |

Se muestran 5 de las 8 autorizaciones vigentes (todas de medicamento único, ninguna cancelada). Las otras tres corresponden a gotas orales 20 mg/ml (60871) y a otras presentaciones de Clopixol Depot (60874 y BE104736).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Nota: no se dispone de datos de advertencias ni contraindicaciones del prospecto en los datos compilados, y la consulta de interacciones farmacológicas no devolvió resultados. Como antipsicótico, el fármaco puede reducir el umbral convulsivo, lo que sería relevante en caso de explorar indicaciones neurológicas como la encefalopatía atípica por glicina.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el puntaje del modelo (nivel L5), sin ensayos clínicos, sin literatura y sin un vínculo mecanístico plausible entre el antagonismo dopaminérgico y las distrofias retinianas. Además, faltan datos de seguridad del prospecto, lo que impide avanzar al cribado de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), un vacío de datos bloqueante
- Confirmar el mecanismo de acción del fármaco mediante DrugBank
- Realizar una revisión sistemática de la literatura sobre dopamina y distrofias retinianas
- Evaluar la similitud con la indicación original y la compatibilidad de vías de administración
- Reconsiderar la priorización frente a otras candidatas con respaldo clínico o mecanístico
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

