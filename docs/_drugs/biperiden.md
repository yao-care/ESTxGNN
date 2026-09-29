---
layout: default
title: Biperiden
parent: Solo predicción del modelo (L5)
nav_order: 77
evidence_level: L5
indication_count: 10
---

# Biperiden
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

# Biperideno: De Síndrome Parkinsoniano a Encefalitis Subaguda de Rasmussen

## Resumen en Una Frase

Biperideno es un anticolinérgico muscarínico comercializado en España (Akineton), utilizado para aliviar la rigidez muscular, el temblor y la sialorrea en el síndrome parkinsoniano.
El modelo TxGNN predice que podría ser efectivo para la **encefalitis subaguda de Rasmussen**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción: es solo una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Las autorizaciones de la AEMPS no incluyen texto de indicación; según farmacología (GtoPdb), síndrome parkinsoniano |
| Nueva Indicación Predicha | Encefalitis subaguda de Rasmussen |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información farmacológica disponible, biperideno actúa sobre los receptores muscarínicos M1, M2, M3, M4 y M5 (genes CHRM1 a CHRM5), con preferencia conocida por M1. Su eficacia en el síndrome parkinsoniano proviene del bloqueo colinérgico central.

**Este caso es débil mecanísticamente.** La encefalitis de Rasmussen es un proceso inmunomediado, dirigido por linfocitos T, y no se identifica un vínculo plausible con el bloqueo muscarínico. La relación con la indicación original es tenue. Es probable que el puntaje alto (99.94%) refleje cercanía en el grafo de conocimiento y no una relación biológica real.

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
| 28994 | AKINETON 5MG/ML SOLUCIÓN INYECTABLE | Solución inyectable | No especificada en los datos recibidos |
| 26692 | AKINETON 2 mg COMPRIMIDOS | Comprimido | No especificada en los datos recibidos |
| 51224 | AKINETON RETARD 4 MG COMPRIMIDOS DE LIBERACIÓN PROLONGADA | Comprimido de liberación prolongada | No especificada en los datos recibidos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como nota general basada en conocimiento farmacológico (no proviene de los datos recibidos), el bloqueo muscarínico central puede afectar la cognición, un aspecto a considerar en cualquier población neurológica.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos, literatura ni un vínculo mecanístico plausible (nivel L5). Además, faltan datos de seguridad de la AEMPS, lo que impide avanzar al cribado de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), que actualmente bloquea el cribado de seguridad
- Obtener el mecanismo de acción desde DrugBank
- Buscar literatura específica sobre biperideno y encefalitis de Rasmussen para confirmar que no hay evidencia previa
- Considerar priorizar otras predicciones del mismo fármaco. La más coherente biológicamente es el **parkinsonismo juvenil de Hunt** (puntaje 99.73%, también L5), por su similitud con el uso clásico de biperideno, aunque sigue sin evidencia directa en los datos recibidos.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

