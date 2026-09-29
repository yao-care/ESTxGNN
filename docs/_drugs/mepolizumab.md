---
layout: default
title: Mepolizumab
parent: Evidencia moderada (L3-L4)
nav_order: 342
evidence_level: L4
indication_count: 5
---

# Mepolizumab
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **5** 
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

# Mepolizumab: De Anticuerpo Anti-IL-5 a Trombocitopenia por Destrucción Inmune

## Resumen en Una Frase

Mepolizumab es un anticuerpo monoclonal anti-IL-5 que reduce los eosinófilos y se comercializa en España como Nucala. El Evidence Pack no incluye su indicación original aprobada.
El modelo TxGNN predice que podría ser efectivo para **trombocitopenia por destrucción inmune**, pero la evidencia es muy limitada: **0 ensayos clínicos** y **1 publicación** (un reporte de caso indirecto).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de AEMPS del Evidence Pack |
| Nueva Indicación Predicha | Trombocitopenia por destrucción inmune |
| Puntaje de Predicción TxGNN | 99.66% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según el conocimiento general, mepolizumab bloquea la interleucina-5 (IL-5), la principal señal para la maduración y supervivencia de los eosinófilos, y por eso reduce su número en sangre y tejidos.

El vínculo con la trombocitopenia inmune es indirecto. La única publicación asociada describe un síndrome hipereosinofílico resistente a esteroides que se resolvió con mepolizumab, junto con una mejoría de una microangiopatía trombótica mixta. Esto sugiere una posible vía mediada por eosinófilos hacia las citopenias inmunes, pero no demuestra un efecto directo sobre la trombocitopenia inmune en general.

El puntaje de TxGNN (0.997) es solo una predicción computacional. No hay ensayos clínicos que la respalden, y la similitud con la indicación original no ha sido evaluada.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28648630](https://pubmed.ncbi.nlm.nih.gov/28648630/) | 2018 | Reporte de caso (inferido del título) | Blood Cells, Molecules & Diseases | Un diátesis inmune hipereosinofílica resistente a esteroides se resolvió con mepolizumab, con mejoría de una microangiopatía trombótica mixta en el contexto de síndrome hemolítico urémico atípico. No trata directamente la trombocitopenia inmune. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 1151043003 | NUCALA 100 MG solución inyectable en pluma precargada | Solución inyectable en pluma precargada |
| 1151043009 | NUCALA 40 MG solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada |
| 1151043005 | NUCALA 100 MG solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada |
| 1151043001 | NUCALA 100 MG polvo para solución inyectable | Polvo para solución inyectable |

Titular de las cuatro autorizaciones: Glaxosmithkline Trading Services Limited. El texto de indicación aprobada no figura en los datos recibidos.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos y la única publicación es un reporte de caso sobre síndrome hipereosinofílico, no sobre trombocitopenia inmune. La predicción se apoya solo en el modelo, con un vínculo mecanístico indirecto. Además, faltan los datos de seguridad del prospecto de AEMPS, una brecha que bloquea el cribado de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones) para completar el cribado de seguridad.
- Confirmar la indicación original aprobada y los datos de mecanismo de acción (por ejemplo, consultando la API de DrugBank).
- Buscar evidencia clínica específica en trombocitopenia inmune (series de casos, estudios observacionales o ensayos).
- Evaluar si existe un subgrupo de pacientes con eosinofilia asociada, donde el bloqueo de IL-5 tenga una justificación biológica más sólida.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

