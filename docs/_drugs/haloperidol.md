---
layout: default
title: Haloperidol
parent: Solo predicción del modelo (L5)
nav_order: 264
evidence_level: L5
indication_count: 10
---

# Haloperidol
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

# Haloperidol: De Antipsicótico a Trastorno Congénito de la Glicosilación con Fucosilación Defectuosa

## Resumen en Una Frase

Haloperidol es un antagonista del receptor de dopamina D2, un fármaco antipsicótico comercializado en España.
El modelo TxGNN predice que podría ser efectivo para el **trastorno congénito de la glicosilación con fucosilación defectuosa**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Trastorno congénito de la glicosilación con fucosilación defectuosa |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L5 (solo predicción del modelo) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados en el paquete de evidencia. Según la información conocida, haloperidol actúa bloqueando los receptores de dopamina D2, y ese es el fundamento de su efecto antipsicótico.

En este caso no se identifica una relación plausible entre ese mecanismo y la enfermedad predicha. El trastorno se debe a un defecto en la fucosilación, una etapa de la biosíntesis de glicanos, y el bloqueo dopaminérgico no tiene un vínculo conocido con esa vía.

El puntaje alto del modelo (99.91%) proviene de patrones en el grafo de conocimiento, sin ensayos ni literatura que lo respalden. Debe considerarse una hipótesis sin validar.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 58355 | HALOPERIDOL ESTEVE 2 mg/ml SOLUCION ORAL | Solución oral |
| 58343 | HALOPERIDOL ESTEVE 10 mg COMPRIMIDOS | Comprimido |
| 55576 | HALOPERIDOL PRODES 10 mg COMPRIMIDOS | Comprimido |
| 33488 | HALOPERIDOL PRODES 2mg/ml GOTAS ORALES EN SOLUCION | Gotas orales en solución |
| 58345 | HALOPERIDOL ESTEVE 5 mg/ml SOLUCION INYECTABLE | Solución inyectable |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos clínicos, sin literatura y sin un mecanismo plausible. No hay base para avanzar en esta indicación.

**Para avanzar se necesita:**
- Evidencia preclínica o de mecanismo que conecte la vía dopaminérgica con la fucosilación defectuosa
- Datos de seguridad y contraindicaciones del prospecto de la AEMPS, actualmente no disponibles
- Datos de mecanismo de acción y de indicaciones aprobadas en España, actualmente no disponibles

**Nota sobre otras predicciones:** el paquete incluye otras nueve indicaciones predichas. La de **trastorno bipolar maníaco** (puesto 10, puntaje 99.83%) es la única con evidencia sólida: 4 ensayos de Fase 3 completados con haloperidol como comparador o brazo de tratamiento, y un metaanálisis en red. Esa evidencia (L1, Proceed with Guardrails) probablemente refleja un uso ya establecido más que un reposicionamiento nuevo. Conviene evaluarla en un informe aparte, verificando su estado de aprobación en España y considerando el riesgo de síntomas extrapiramidales.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

