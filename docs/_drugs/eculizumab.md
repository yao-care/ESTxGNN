---
layout: default
title: Eculizumab
parent: Solo predicción del modelo (L5)
nav_order: 191
evidence_level: L5
indication_count: 10
---

# Eculizumab
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

# Eculizumab: De Inhibidor del Complemento C5 a Hematopoyesis Cíclica

## Resumen en Una Frase

Eculizumab es un anticuerpo monoclonal inhibidor del complemento C5. El registro de origen no incluye su indicación original, pero la literatura recuperada lo asocia con la hemoglobinuria paroxística nocturna, el síndrome hemolítico urémico atípico y la miastenia gravis.
El modelo TxGNN predice que podría ser efectivo para **hematopoyesis cíclica** (neutropenia cíclica), pero hay **0 ensayos clínicos** y **0 publicaciones** específicas que respalden esta predicción.
Es una predicción basada solo en el modelo, sin un vínculo mecanístico plausible.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Hematopoyesis cíclica |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información conocida, eculizumab es un inhibidor del componente C5 del complemento. Su eficacia se ha documentado en enfermedades mediadas por complemento, como la hemoglobinuria paroxística nocturna, el síndrome hemolítico urémico atípico y la miastenia gravis.

Aplicado a la hematopoyesis cíclica, el análisis no encuentra un vínculo mecanístico evidente. La neutropenia cíclica se debe a mutaciones en *ELANE* y no a la activación del complemento. El alto puntaje del modelo (99.97%) refleja probablemente la proximidad en la red del grafo de conocimiento y no una relación biológica real.

Por ello, la predicción debe considerarse una hipótesis sin respaldo mecanístico ni clínico. Lo mismo ocurre con las otras nueve indicaciones predichas, todas neutropenias congénitas o síndromes relacionados, en nivel L5.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 07393001 | SOLIRIS 300 mg concentrado para solución para perfusión | Concentrado para solución para perfusión | Alexion Europe SAS |
| 1231727001 | BEKEMV 300 mg concentrado para solución para perfusión | Concentrado para solución para perfusión | Amgen Technology (Ireland) Unlimited Company |
| 1231735001 | EPYSQLI 300 mg concentrado para solución para perfusión | Concentrado para solución para perfusión | Samsung Bioepis NL B.V. |

## Consideraciones de Seguridad

- **Advertencia importante**: eculizumab conlleva una advertencia de recuadro por infección meningocócica. Esto es especialmente relevante en pacientes neutropénicos o con inmunodeficiencia, en quienes la inhibición del complemento sumaría riesgo de infección.

No se dispone de datos de contraindicaciones ni de interacciones farmacológicas. Consultar el prospecto para el resto de la información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos clínicos ni literatura específica, y no existe un vínculo mecanístico plausible entre la inhibición de C5 y la neutropenia cíclica. Además, el riesgo de infección meningocócica es una preocupación de seguridad en pacientes neutropénicos.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), un bloqueo para el cribado de seguridad.
- Completar los datos de mecanismo de acción desde DrugBank.
- Registrar la indicación original autorizada, hoy vacía en las tres autorizaciones.
- Encontrar evidencia preclínica o mecanística que vincule la vía del complemento con la hematopoyesis cíclica.
- Si aparece evidencia, evaluar el riesgo-beneficio de la inhibición del complemento en pacientes neutropénicos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

