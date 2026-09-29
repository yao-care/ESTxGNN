---
layout: default
title: Vancomycin
parent: Solo predicción del modelo (L5)
nav_order: 554
evidence_level: L5
indication_count: 10
---

# Vancomycin
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

# Vancomicina: De Infecciones por Bacterias Gram-positivas a Esclerodermia Difusa

## Resumen en Una Frase

La vancomicina es un antibiótico glucopéptido activo frente a bacterias Gram-positivas, y en España se comercializa en forma de perfusión intravenosa y cápsulas.
El modelo TxGNN predice que podría ser efectiva para **esclerodermia difusa**, pero solo hay **0 ensayos clínicos** y **1 publicación** (un reporte de caso en el que la vancomicina es un dato incidental).
La predicción carece de respaldo real y no se identifica ningún mecanismo plausible.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los textos de AEMPS recibidos; por su clase farmacológica, infecciones por bacterias Gram-positivas |
| Nueva Indicación Predicha | Esclerodermia difusa |
| Puntaje de Predicción TxGNN | 99,92 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 10 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, la vancomicina es un antibiótico glucopéptido con actividad frente a bacterias Gram-positivas, y no se le conoce acción inmunomoduladora ni antifibrótica.

**Esta predicción no tiene un vínculo mecanístico plausible.** La esclerodermia difusa (esclerosis sistémica) es una enfermedad autoinmune y fibrosante, y la vancomicina no actúa sobre esos procesos. El puntaje alto de TxGNN (99,92 %) es solo una predicción del modelo. No implica eficacia.

La única publicación recuperada describe un caso de eritrodermia con sepsis y eosinofilia. La vancomicina aparece allí de forma incidental, sin relación con el tratamiento de la esclerodermia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Reporte de caso | The American Journal of Case Reports | Varón de 56 años con exantema descamativo difuso (eritrodermia), sepsis y eosinofilia. No aporta evidencia de eficacia de la vancomicina en esclerodermia. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 73785 | Vancomicina Pfizer 1000 mg | Polvo para concentrado para solución para perfusión |
| 90304 | Vangozyr 250 mg cápsulas duras | Cápsula dura |
| 73784 | Vancomicina Pfizer 500 mg | Polvo para concentrado para solución para perfusión |
| 85651 | Vancomicina Normon 1000 mg | Polvo para concentrado para solución para perfusión |
| 67283 | Vancomicina Sala 1.000 mg | Polvo para solución inyectable |

Se muestran 5 de las 10 autorizaciones. Los textos de indicación aprobada no están disponibles en los datos recibidos.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en la consulta realizada.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos, la única publicación es un reporte de caso sin relación causal y no existe un mecanismo plausible. La vancomicina no tiene acción antifibrótica ni inmunomoduladora conocida, por lo que el puntaje de TxGNN no basta para avanzar.

**Para avanzar se necesita:**
- Obtener el prospecto de AEMPS (advertencias, contraindicaciones e indicaciones aprobadas) para poder realizar el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Justificar un mecanismo biológico entre la vancomicina y la esclerosis sistémica. Sin él, no se recomienda ninguna investigación adicional para esta indicación.
- Entre las demás predicciones del modelo, solo la neumonía estreptocócica (puesto 9) tiene un mecanismo plausible (inhibición de la síntesis de pared celular en Gram-positivos). Es probable que se trate de un uso ya cercano a la indicación autorizada o a las guías, no de un reposicionamiento real. Conviene revisar primero la indicación original.

*Los resultados son solo para investigación y no constituyen consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

