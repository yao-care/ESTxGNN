---
layout: default
title: Galantamine
parent: Solo predicción del modelo (L5)
nav_order: 252
evidence_level: L5
indication_count: 9
---

# Galantamine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

# Galantamina: De Enfermedad de Alzheimer a Trastornos del Movimiento Psicógenos

## Resumen en Una Frase

Galantamina es un inhibidor de la acetilcolinesterasa que se usa para el Alzheimer leve a moderado.
El modelo TxGNN predice que podría ser efectiva para **trastornos del movimiento psicógenos**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Alzheimer leve a moderada (según datos farmacológicos; los textos de indicación de AEMPS no están disponibles) |
| Nueva Indicación Predicha | Trastornos del movimiento psicógenos |
| Puntaje de Predicción TxGNN | 99,90% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Galantamina inhibe la acetilcolinesterasa (ACHE) y además modula de forma alostérica el receptor nicotínico de acetilcolina α7. Con ello aumenta la señalización colinérgica y mejora el rendimiento cognitivo en el Alzheimer y otros trastornos neurodegenerativos.

La relación entre la indicación original y la nueva es débil. Los trastornos del movimiento psicógenos son trastornos funcionales, y no hay un mecanismo colinérgico documentado que explique un posible beneficio. El puntaje alto de TxGNN (99,90%) refleja únicamente la similitud dentro del grafo de conocimiento, no evidencia real.

Por lo tanto, la predicción debe considerarse una hipótesis sin respaldo mecanístico ni clínico por ahora.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 74331 | GALNORA 24 mg cápsulas duras de liberación prolongada EFG | Cápsula dura de liberación prolongada |
| 66652 | REMINYL 24 mg cápsulas duras de liberación prolongada | Cápsula dura de liberación prolongada |
| 74688 | GALANTAMINA VIATRIS 24 mg cápsulas duras de liberación prolongada EFG | Cápsula dura de liberación prolongada |
| 74351 | GALANTAMINA KERN PHARMA 8 mg cápsulas duras de liberación prolongada EFG | Cápsula dura de liberación prolongada |
| 77472 | GALANTAMINA TEVA-RATIO 16 mg cápsulas duras de liberación prolongada EFG | Cápsula dura de liberación prolongada |

Existen 20 autorizaciones en total; la tabla muestra las 5 principales. También hay una presentación de solución oral.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos, sin literatura y sin un mecanismo plausible. No hay base para avanzar con esta indicación.

**Para avanzar se necesita:**
- Obtener del prospecto de AEMPS las advertencias y contraindicaciones (actualmente sin datos), un paso bloqueante para cualquier evaluación de seguridad.
- Priorizar otra predicción del mismo farmaco: la **discinesia lingual-facial-bucal** (discinesia tardía, puesto 7, nivel L2). Cuenta con un ECA cruzado de galantamina (PMID 17388711), revisiones Cochrane y un metaanálisis. Antes de avanzar, hay que verificar los resultados reales de esos estudios, ya que las revisiones suelen concluir que la evidencia de los agentes colinérgicos es insuficiente.
- Vigilar la señal de seguridad de la revisión sistemática de 2025 (PMID 40224553), que asocia los inhibidores de la acetilcolinesterasa con trastornos del movimiento.
- Si se quiere reconsiderar la indicación psicógena, generar primero una justificación mecanística y datos preclínicos o clínicos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

