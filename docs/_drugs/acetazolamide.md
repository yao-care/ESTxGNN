---
layout: default
title: Acetazolamide
parent: Solo predicción del modelo (L5)
nav_order: 15
evidence_level: L5
indication_count: 10
---

# Acetazolamide
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

# Acetazolamida: De Glaucoma, Epilepsia y Edema a Hipertermia Maligna Inducida por el Ejercicio

## Resumen en Una Frase

Acetazolamida es un inhibidor de la anhidrasa carbónica, utilizado originalmente para el glaucoma, la epilepsia y el edema.
El modelo TxGNN predice que podría ser efectiva para **hipertermia maligna inducida por el ejercicio**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en la autorización de AEMPS (texto vacío). Según los datos farmacológicos: glaucoma, epilepsia y edema |
| Nueva Indicación Predicha | Hipertermia maligna inducida por el ejercicio |
| Puntaje de Predicción TxGNN | 99,95% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos farmacológicos indican que la acetazolamida inhibe la anhidrasa carbónica (CA1, CA4, CA7, CA12 y CA14 en humanos). Este mecanismo explica su efecto diurético, la reducción de la presión intraocular y su posible acción antiepiléptica. El campo de mecanismo de acción de DrugBank no está completado, por lo que esta descripción se basa solo en las dianas farmacológicas registradas.

Con los datos disponibles **no se puede sostener un vínculo mecanístico** entre esa inhibición y la hipertermia maligna inducida por el ejercicio. El puntaje alto (99,95%) proviene únicamente de las relaciones del grafo de conocimiento del modelo. No hay ensayos ni literatura que lo corroboren, y la similitud con las indicaciones originales no ha sido evaluada.

Por eso esta predicción debe leerse como una hipótesis de partida, no como una señal terapéutica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 24408 | EDEMOX 250 mg COMPRIMIDOS (Chiesi España S.A.U.) | Comprimido | No especificada en los datos recibidos |

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: la consulta se completó, pero las 6 entradas registradas son dianas farmacológicas (anhidrasas carbónicas CA1, CA4, CA7, CA12, CA13 de ratón y CA14), no interacciones clínicas con otros medicamentos. No hay datos de niveles de gravedad.
- **Señales de otras predicciones del mismo modelo** (no de esta indicación):
  - Se han descrito casos de íleo adinámico inducido por acetazolamida.
  - En cirrosis podría aumentar el riesgo de encefalopatía hepática.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos clínicos ni publicaciones (nivel L5), y no existe un mecanismo plausible documentado con los datos disponibles. El puntaje alto de TxGNN por sí solo no basta para avanzar.

**Para avanzar se necesita:**
- Una revisión de literatura dirigida sobre anhidrasa carbónica e hipertermia maligna o fisiopatología muscular asociada al ejercicio.
- El mecanismo de acción completo desde DrugBank.
- El texto del prospecto de AEMPS (advertencias y contraindicaciones), que es un requisito previo para cualquier cribado de seguridad.
- La evaluación de la similitud entre la indicación predicha y las indicaciones originales.
- Como alternativa, priorizar la predicción de **cardiomiopatía** (rango 7): tiene 3 ensayos de fase 4/NA en curso, aunque en insuficiencia cardíaca aguda y no en cardiomiopatía específicamente, y aún sin resultados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

