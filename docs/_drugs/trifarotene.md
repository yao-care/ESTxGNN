---
layout: default
title: Trifarotene
parent: Solo predicción del modelo (L5)
nav_order: 826
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Trifarotene: nueva indicación predicha, Zinc plasmático elevado (nivel de evidencia L5). Indicación original: Acné (según las relaciones de indicación del grafo de conocimiento"
---

# Trifarotene
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Trifaroteno: De Acné a Zinc Plasmático Elevado

## Resumen en Una Frase

Trifaroteno es un retinoide tópico, originalmente utilizado para el tratamiento del acné.
El modelo TxGNN predice que podría ser efectivo para **zinc plasmático elevado**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Acné (según las relaciones de indicación del grafo de conocimiento; el texto de indicación de la autorización de la AEMPS no está disponible) |
| Nueva Indicación Predicha | Zinc plasmático elevado |
| Puntaje de Predicción TxGNN | 99,40% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, el trifaroteno es un agonista selectivo del receptor del ácido retinoico gamma (RAR-γ) de aplicación tópica, y su eficacia en el acné está respaldada por ensayos de Fase 3. Los datos farmacológicos también lo vinculan con los receptores RAR-α, RAR-β y RAR-γ.

**No se identifica un vínculo mecanístico creíble** con la nueva indicación. El zinc plasmático elevado es un hallazgo metabólico o de laboratorio sistémico (por ejemplo, asociado a suplementación, insuficiencia renal o artefactos del ensayo) y no se conoce dependencia de la señalización por RAR-γ. Además, el trifaroteno presenta una alta inestabilidad metabólica y, aplicado por vía tópica, una exposición sistémica limitada, lo que reduce aún más la plausibilidad de un efecto sobre el zinc plasmático.

El puntaje alto de TxGNN (99,40%) es solo una predicción basada en el modelo y no cuenta con respaldo clínico ni bibliográfico.

**Otra predicción del modelo (rango 2):** el síndrome de artritis piogénica-pioderma gangrenoso-acné (PAPA), con un puntaje de 99,32%, también con nivel de evidencia L5 y recomendación Hold. El vínculo es indirecto y especulativo: el componente de acné cutáneo coincide fenotípicamente con la indicación original, y el RAR-γ podría modular la diferenciación de queratinocitos y la inflamación folicular. Sin embargo, no abordaría la patología subyacente de activación del inflamasoma (mutaciones en PSTPIP1, inflamación dependiente de IL-1), ni la artritis ni el pioderma gangrenoso, cuyo tratamiento estándar se dirige a las vías de IL-1 y TNF.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 85017 | AKLIEF 50 microgramos/g crema | Crema | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** la consulta se completó y devolvió 3 registros, todos de tipo farmacológico (sin nivel de gravedad asignado), correspondientes a la unión del trifaroteno a los receptores del ácido retinoico RAR-α, RAR-β y RAR-γ. No son interacciones medicamentosas clínicas con otros fármacos. Los datos indican que, por su alta inestabilidad metabólica, la exposición sistémica con uso tópico sería limitada.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para zinc plasmático elevado se basa únicamente en el modelo (L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible con la agonista RAR-γ tópica, con exposición sistémica baja. La alternativa del síndrome PAPA tampoco tiene respaldo y solo podría abordar de forma teórica el componente de acné.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicación aprobada), un vacío de datos bloqueante para el cribado de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Una hipótesis biológica que explique cómo la señalización por RAR podría influir en el zinc plasmático, y datos de exposición sistémica que la sustenten
- Búsqueda de estudios preclínicos o de series de casos antes de reconsiderar cualquiera de las dos indicaciones predichas
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

