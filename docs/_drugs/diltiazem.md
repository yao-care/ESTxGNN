---
layout: default
title: Diltiazem
parent: Solo predicción del modelo (L5)
nav_order: 252
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Diltiazem: nueva indicación predicha, Susceptibilidad al ictus isquémico (término obsoleto) (nivel de evidencia L5). Indicación original: Trastorno hipertensivo / hipertensión"
monitor_inn: "DILTIAZEM"
predicted_indications: ["obsolete susceptibility to ischemic stroke"]
---

# Diltiazem
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Diltiazem: De Trastorno Hipertensivo a Susceptibilidad al Ictus Isquémico (término obsoleto)

## Resumen en Una Frase

Diltiazem es un bloqueador de los canales de calcio de tipo L, utilizado originalmente para el tratamiento de la hipertensión, la fibrilación auricular, la angina de Prinzmetal y la taquicardia ventricular.
El modelo TxGNN predice que podría ser efectivo para **susceptibilidad al ictus isquémico (término obsoleto)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastorno hipertensivo / hipertensión (las indicaciones proceden del grafo de conocimiento; los registros de la AEMPS no incluyen texto de indicación) |
| Nueva Indicación Predicha | Susceptibilidad al ictus isquémico (término obsoleto) |
| Puntaje de Predicción TxGNN | 99.08% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, diltiazem es un bloqueador de los canales de calcio no dihidropiridínico de tipo L, con eficacia comprobada en hipertensión, fibrilación auricular, angina de Prinzmetal y taquicardia ventricular.

Mecanísticamente, existen vínculos plausibles con la susceptibilidad al ictus: la reducción de la presión arterial, la vasodilatación cerebral con menor vasoespasmo y el control de la frecuencia en la fibrilación auricular, que es un factor de riesgo importante de ictus cardioembólico. Estos vínculos son hipotéticos y **no están respaldados por evidencia** en los datos disponibles.

Además, el nombre de la enfermedad está marcado como "obsoleto", lo que sugiere que el término de la ontología ha sido descontinuado o fusionado. Probablemente se trate de un concepto de riesgo o susceptibilidad y no de una condición clínica tratable, por lo que la predicción requiere un remapeo de la ontología antes de poder interpretarse.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones vigentes (todas de medicamentos con un único principio activo). Los registros no incluyen texto de indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 60006 | Lacerol Retard 120 mg | Cápsula dura de liberación prolongada | No disponible en el registro |
| 11456610496 | Tilker cápsulas | Cápsula dura de liberación prolongada | No disponible en el registro |
| 60089 | Doclis Retard 120 mg | Cápsula dura de liberación prolongada | No disponible en el registro |
| 59776 | Dinisor Retard 180 mg | Comprimido de liberación modificada | No disponible en el registro |
| 62328 | Diltiazem Sandoz 60 mg EFG | Comprimido | No disponible en el registro |

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no texto del prospecto)**: enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, angioedema (incluidas las formas adquirida, hereditaria y la inducida por bloqueadores del sistema renina-angiotensina-aldosterona), neutropenia, agranulocitosis, estenosis aórtica, trastornos hipotensivos, miocardiopatía hipertrófica, obstrucción de la arteria renal, taquicardia ventricular, bloqueo auriculoventricular, síndrome de Wolff-Parkinson-White, síndrome de Lown-Ganong-Levine y síndrome del seno enfermo, entre otras.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones; entre las mostradas, la de **mayor gravedad es con loperamida (Mayor)**. Las demás son de nivel moderado, entre ellas hidrocortisona, pioglitazona, bupropión, aprepitant, triamcinolona, morfina, ácido acetilsalicílico, dexametasona, betametasona, budesonida, canagliflozina y diversas sales de calcio.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación se sustenta únicamente en un puntaje alto del modelo (99.08%), sin ensayos clínicos ni literatura, y el término de la enfermedad es obsoleto, por lo que no está claro qué condición clínica se estaría tratando.

**Para avanzar se necesita:**
- Remapear el término obsoleto a una entidad vigente (por ejemplo, prevención primaria o secundaria del ictus isquémico)
- Revisar la literatura y los ensayos sobre bloqueadores de los canales de calcio y diltiazem en prevención del ictus
- Obtener los datos del mecanismo de acción desde DrugBank
- Descargar y analizar el prospecto de la AEMPS para obtener advertencias y contraindicaciones oficiales
- Evaluar el perfil de seguridad en la población de riesgo, en particular bradicardia, bloqueo AV e hipotensión
- Revisar la compatibilidad de vías de administración (pendiente)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

