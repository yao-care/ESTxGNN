---
layout: default
title: Moxonidine
parent: Solo predicción del modelo (L5)
nav_order: 368
evidence_level: L5
indication_count: 10
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

# Moxonidina: De Hipertensión Arterial a Hipotricosis Simple del Cuero Cabelludo

## Resumen en Una Frase

Moxonidina es un antihipertensivo de acción central, comercializado en España como MOXON. El modelo TxGNN predice que podría ser efectivo para **hipotricosis simple del cuero cabelludo**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial (según la información farmacológica del fármaco; el texto de indicación autorizado por la AEMPS no figura en los datos recibidos) |
| Nueva Indicación Predicha | Hipotricosis simple del cuero cabelludo |
| Puntaje de Predicción TxGNN | 99,95% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información farmacológica disponible, moxonidina es un agonista central de receptores de imidazolina I1 y alfa-2 adrenérgicos (actúa sobre ADRA2A, ADRA2B y ADRA2C). Reduce la salida simpática y se utiliza como antihipertensivo.

**No se ha establecido un vínculo mecanístico directo** con la nueva indicación. El puntaje elevado (0,9995) probablemente refleja que, en el grafo de conocimiento, moxonidina comparte un "vecindario antihipertensivo" con minoxidil. Minoxidil sí se relaciona con la pérdida de cabello, pero actúa como vasodilatador abridor de canales de potasio, un mecanismo distinto al de moxonidina. Por tanto, la asociación parece deberse a la cercanía en el grafo y no a una razón biológica demostrada.

Sin ensayos ni literatura que sustenten la hipótesis, esta predicción debe considerarse una señal del modelo y no un candidato con respaldo clínico.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 61158 | MOXON 0,4 mg comprimidos recubiertos con película | Comprimido recubierto | No especificada en los datos disponibles |
| 61157 | MOXON 0,3 mg comprimidos recubiertos con película | Comprimido recubierto | No especificada en los datos disponibles |
| 61156 | MOXON 0,2 mg comprimidos recubiertos con película | Comprimido recubierto | No especificada en los datos disponibles |

Titular de las tres autorizaciones: Viatris Healthcare Limited. La única vía disponible es oral (comprimido).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- No existen ensayos clínicos ni literatura que vinculen moxonidina con hipotricosis del cuero cabelludo (nivel L5, etapa S0).
- El puntaje alto del modelo parece originarse en la similitud de grafo con minoxidil, no en un mecanismo compatible.
- No se ha revisado la ficha técnica de la AEMPS, por lo que no se puede completar el cribado de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar la ficha técnica de la AEMPS (advertencias y contraindicaciones), que es un vacío de datos bloqueante.
- Obtener los datos del mecanismo de acción desde DrugBank.
- Buscar estudios preclínicos (folículo piloso, receptores alfa-2 o imidazolina) que justifiquen una hipótesis mecanística.
- Evaluar si un fármaco sistémico que baja la presión arterial es viable para una condición capilar, considerando el perfil de riesgo-beneficio y la posible necesidad de una vía tópica.

**Otras predicciones del mismo fármaco:** malignant hypertensive renal disease, malignant renovascular hypertension y primary hereditary glaucoma quedaron marcadas como "Research Question" por tener cierta plausibilidad biológica. Sin embargo, tampoco cuentan con ensayos ni literatura, y las dos primeras podrían solaparse con el uso antihipertensivo ya existente.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

