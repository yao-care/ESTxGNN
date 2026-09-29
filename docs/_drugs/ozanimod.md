---
layout: default
title: Ozanimod
parent: Evidencia moderada (L3-L4)
nav_order: 400
evidence_level: L4
indication_count: 1
---

# Ozanimod
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **1** 
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

# Ozanimod: De Esclerosis Múltiple Recurrente a Esclerosis Múltiple Recurrente Progresiva

## Resumen en Una Frase

Ozanimod es un modulador de los receptores de esfingosina-1-fosfato (S1P), utilizado en esclerosis múltiple recurrente. Los datos suministrados no incluyen la indicación original, así que este dato procede del conocimiento de clase.
El modelo TxGNN predice que podría ser efectivo para **esclerosis múltiple recurrente progresiva**, pero la evidencia directa es escasa: hay **8 ensayos clínicos** asociados (solo **1** de Fase 3 con valor indirecto) y **ninguna publicación** disponible.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Esclerosis múltiple recurrente progresiva |
| Puntaje de Predicción TxGNN | 99,34 % |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según el conocimiento de clase, ozanimod modula los receptores S1P 1 y 5. Retiene los linfocitos en los ganglios linfáticos y reduce la entrada de linfocitos autorreactivos al sistema nervioso central. Este es el mecanismo que respalda su uso en esclerosis múltiple (EM) recurrente.

"EM recurrente progresiva" es una etiqueta antigua. La clasificación actual la considera EM progresiva con brotes superpuestos. Por eso, el beneficio esperable vendría solo del componente inflamatorio (menos brotes), no de un efecto sobre la progresión sin brotes.

El puntaje alto de TxGNN (0,993) es una predicción computacional y **no cuenta como evidencia clínica**.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02576717](https://clinicaltrials.gov/study/NCT02576717) | Fase 3 | Completado | 2494 | Ensayo aleatorizado, doble ciego, con control activo, de RPC1063 (ozanimod) en EM recurrente. Es la única evidencia aleatorizada del conjunto y es indirecta para este fenotipo. |
| [NCT06396039](https://clinicaltrials.gov/study/NCT06396039) | Fase 4 | Activo, no recluta | 84 | Estudio abierto de un solo brazo sobre efectividad y seguridad de ozanimod oral en adultos chinos con EM recurrente. No tiene comparador. |
| [NCT05605782](https://clinicaltrials.gov/study/NCT05605782) | N/A | Activo, no recluta | 9000 | ORION: estudio observacional poscomercialización de seguridad a largo plazo de ozanimod. No aporta datos de eficacia. |
| [NCT05828901](https://clinicaltrials.gov/study/NCT05828901) | N/A | Reclutando | 60 | Estudio observacional de actividad de la enfermedad y riesgo de rebote con moduladores S1P. Es de clase, no específico de ozanimod. |
| [NCT03535298](https://clinicaltrials.gov/study/NCT03535298) | Fase 4 | Activo, no recluta | 800 | DELIVER-MS: compara estrategias de tratamiento temprano intensivo y escalonado. No se confirma que ozanimod sea un brazo. Vínculo débil. |
| [NCT03500328](https://clinicaltrials.gov/study/NCT03500328) | N/A | Activo, no recluta | 900 | TREAT-MS: compara terapia temprana agresiva y escalonada. Vínculo débil con ozanimod. |
| [NCT04676204](https://clinicaltrials.gov/study/NCT04676204) | N/A | Inscripción por invitación | 323 | STATURE: estudio observacional de carga del tratamiento y adherencia a DMT orales, entre ellos ozanimod. No evalúa eficacia. |

Se excluyó NCT05688436, un registro de embarazo de otro fármaco (diroximima fumarato), porque no guarda relación con ozanimod.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 1201442002 | ZEPOSIA 0,92 MG CÁPSULAS DURAS | Cápsula dura |
| 1201442001 | ZEPOSIA 0,23 MG/0,46 MG CÁPSULAS DURAS | Cápsula dura |

Titular: Bristol-Myers Squibb Pharma EEIG. Los registros no incluyen el texto de la indicación aprobada.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El fármaco ya está comercializado en España y su mecanismo es plausible para el componente inflamatorio de la EM. Sin embargo, no hay evidencia directa en el fenotipo predicho: el único ensayo aleatorizado es en EM recurrente y no hay literatura. La prediccion de TxGNN por sí sola no basta.

**Para avanzar se necesita:**
- Obtener del prospecto de la AEMPS las advertencias y contraindicaciones (vacío bloqueante para el cribado de seguridad).
- Completar el mecanismo de acción desde DrugBank.
- Confirmar si NCT02576717 incluyó pacientes con EM recurrente progresiva y revisar sus resultados publicados.
- Hacer una búsqueda de literatura específica sobre ozanimod en EM progresiva con brotes.
- Definir criterios de selección de pacientes limitados a enfermedad con actividad inflamatoria (brotes).

*Este informe es solo de referencia para investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

