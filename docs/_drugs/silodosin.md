---
layout: default
title: Silodosin
parent: Solo predicción del modelo (L5)
nav_order: 491
evidence_level: L5
indication_count: 6
---

# Silodosin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Silodosina: De Hiperplasia Prostática Benigna a Hipertricosis Universal Congénita tipo Ambras

## Resumen en Una Frase

La silodosina es un antagonista selectivo de los receptores adrenérgicos alfa-1A, utilizado para mejorar el flujo urinario en la hiperplasia prostática benigna (HPB).
El modelo TxGNN predice que podría ser efectiva para la **hipertricosis universal congénita tipo Ambras**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hiperplasia prostática benigna (según datos de farmacología; los textos de indicación de AEMPS no están disponibles) |
| Nueva Indicación Predicha | Hipertricosis universal congénita tipo Ambras |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente principal. Según la información farmacológica conocida, la silodosina se une a los receptores adrenérgicos alfa-1A (ADRA1A), y también aparece asociada a los subtipos alfa-1B y alfa-1D. Su eficacia en la HPB está comprobada, pero mecanísticamente no se identifica una vía que la conecte con la nueva indicación.

El síndrome de Ambras es un trastorno congénito raro, vinculado a reordenamientos genómicos en 8q22 que alteran la regulación de TRPS1. No existe una vía conocida que conecte el bloqueo alfa-1A con este mecanismo. El puntaje muy alto de TxGNN (0.9999) refleja solo proximidad en el grafo de conocimiento, no evidencia clínica.

Por tanto, esta predicción **no está respaldada mecanísticamente** con los datos actuales. Debe considerarse una hipótesis generada por el modelo y no una candidata con fundamento farmacológico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

> Nota: la tercera predicción (síndrome malformativo con componente odontal/periodontal) recuperó 20 publicaciones sobre periodontitis en general. Ninguna menciona la silodosina ni el antagonismo alfa-1, por lo que no cuentan como evidencia específica del fármaco.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 84053 | Silodosina Stada 8 mg cápsulas duras EFG | Cápsula dura |
| 85271 | Xilapro 4 mg cápsulas duras EFG | Cápsula dura |
| 85272 | Xilapro 8 mg cápsulas duras EFG | Cápsula dura |
| 84377 | Sidarso 8 mg cápsulas duras EFG | Cápsula dura |
| 84498 | Silodosina Aurobindo 8 mg cápsulas duras EFG | Cápsula dura |

Se muestran 5 de las 20 autorizaciones. Los textos de indicación aprobada no están disponibles en los datos recibidos.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en la proximidad en el grafo de conocimiento (nivel L5). No hay ensayos, literatura específica ni vínculo mecanístico plausible entre el bloqueo alfa-1A y el síndrome de Ambras. Las otras cinco indicaciones predichas también quedan en L5 y Hold.

**Para avanzar se necesita:**
- Obtener el mecanismo de acción detallado (por ejemplo, consultando la API de DrugBank).
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones) para poder iniciar el cribado de seguridad.
- Aclarar la dirección del efecto en las predicciones relacionadas con el vello (tratamiento frente a efecto adverso).
- Buscar estudios preclínicos o de mecanismo que vinculen la señalización adrenérgica con el folículo piloso o con la regulación de TRPS1.
- Realizar una búsqueda bibliográfica específica de silodosina más la enfermedad, en lugar de una búsqueda solo por palabra clave de la enfermedad.

*Los resultados son solo de referencia para investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

