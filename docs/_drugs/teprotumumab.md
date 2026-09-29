---
layout: default
title: Teprotumumab
parent: Solo predicción del modelo (L5)
nav_order: 519
evidence_level: L5
indication_count: 10
---

# Teprotumumab
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

# Teprotumumab: De Indicación Original No Registrada a Monosomía X

## Resumen en Una Frase

Teprotumumab es un anticuerpo monoclonal que inhibe el receptor del factor de crecimiento similar a la insulina tipo 1 (IGF-1R). Está comercializado en España como Tepezza, pero el Evidence Pack no incluye el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **monosomía X**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (el texto de indicación aprobada está vacío en el registro) |
| Nueva Indicación Predicha | Monosomía X |
| Puntaje de Predicción TxGNN | 99.79% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Teprotumumab es un inhibidor de IGF-1R. No hay datos detallados de mecanismo de acción en DrugBank para este registro, pero el análisis mecanístico disponible identifica esta clase de inhibición como su característica principal.

**En este caso la predicción es poco razonable desde el punto de vista biológico.** No se ha establecido un vínculo directo entre la inhibición de IGF-1R y el fenotipo de dosificación del cromosoma X. Además, la señalización de IGF-1 favorece el crecimiento en el síndrome de Turner, que suele tratarse con hormona de crecimiento (actúa vía IGF-1). Bloquear IGF-1R podría por tanto ser contraproducente y plantear un problema de seguridad, no un beneficio.

El puntaje alto (99.79%) probablemente refleja un artefacto del grafo de conocimiento y no una señal real. Las otras nueve predicciones del conjunto (várices esofágicas con y sin sangrado, disgenesia gonadal mixta, trastorno mitocondrial de la fosforilación oxidativa por anomalías del ADN nuclear, síndrome de Turner por anomalías estructurales del X, monosomía X en mosaico, trastorno del desarrollo sexual por cromosomas sexuales, enfermedad varicosa y anomalía del número de cromosomas X) también son solo predicción, sin ensayos ni literatura. Varias de ellas están correlacionadas entre sí (grupo de cromosomas sexuales y grupo de várices), por lo que no son señales independientes.

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
| 1251941001 | TEPEZZA 500 MG (Amgen Europe B.V.) | Polvo para concentrado para solución para perfusión | No disponible en el registro |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas para este fármaco.

Como señal de precaución derivada del análisis mecanístico: en síndrome de Turner y cuadros relacionados, el bloqueo de IGF-1R podría oponerse al efecto de la hormona de crecimiento.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Todas las predicciones son de nivel L5 (solo modelo), sin ensayos clínicos ni literatura, y no existe un mecanismo plausible que las respalde. Además, en la principal predicción hay una posible preocupación de seguridad por antagonismo del eje IGF-1.

**Para avanzar se necesita:**
- Obtener el prospecto de AEMPS (advertencias y contraindicaciones) y la indicación aprobada
- Completar los datos de mecanismo de acción desde DrugBank
- Buscar evidencia preclínica o clínica que vincule la inhibición de IGF-1R con la monosomía X. Sin ella, no se recomienda avanzar
- Evaluar de forma explícita el riesgo de antagonizar el tratamiento con hormona de crecimiento en síndrome de Turner

*Estos resultados son solo para investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

