---
layout: default
title: Ascorbic Acid
parent: Solo predicción del modelo (L5)
nav_order: 68
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ascorbic Acid: nueva indicación predicha, Malformación esofágica no sindrómica (nivel de evidencia L5). Indicación original: Deficiencia de ácido ascórbico y escorbuto (según el grafo de conocim…"
monitor_inn: "Ascorbic acid"
predicted_indications: ["non-syndromic esophageal malformation", "esophageal disease", "congenital prothrombin deficiency", "injury", "biotin metabolic disease", "florid cemento-osseous dysplasia", "perinatal disease", "segmental odontomaxillary dysplasia", "disease by subcellular system affected"]
---

# Ascorbic Acid
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

# Ácido ascórbico: De deficiencia de ácido ascórbico y escorbuto a malformación esofágica no sindrómica

## Resumen en Una Frase

El ácido ascórbico (vitamina C) se utiliza para tratar y prevenir la deficiencia de vitamina C y el escorbuto.
El modelo TxGNN predice que podría ser efectivo para **malformación esofágica no sindrómica**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción basada en el grafo de conocimiento.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Deficiencia de ácido ascórbico y escorbuto (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas están vacíos) |
| Nueva Indicación Predicha | Malformación esofágica no sindrómica |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, el ácido ascórbico es una vitamina hidrosoluble con función antioxidante y de cofactor (por ejemplo, en la síntesis de colágeno). Su eficacia en la deficiencia de vitamina C y el escorbuto está plenamente establecida.

Sin embargo, no se identificó ningún vínculo mecanístico entre el fármaco y esta nueva indicación. Las malformaciones estructurales congénitas del esófago son defectos del desarrollo embrionario y es improbable que respondan a una vitamina con funciones antioxidantes y de cofactor. El puntaje alto de TxGNN refleja únicamente asociaciones dentro del grafo de conocimiento, sin respaldo en ensayos ni literatura.

Por tanto, la predicción debe considerarse una hipótesis sin fundamento clínico o mecanístico por ahora.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 90151 | VITAMINA C BASI 100 MG/ML SOLUCIÓN INYECTABLE | Solución inyectable | No especificada en los datos disponibles |
| 17536 | LAROSCORBINE 1000 mg/5 ml SOLUCIÓN INYECTABLE | Solución inyectable | No especificada en los datos disponibles |

Ambas autorizaciones son de monofármaco y están vigentes. Los titulares son Laboratorios Basi Industria Farmacéutica S.A. y Bayer Hispania S.L., respectivamente.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto, por lo que deben verificarse): hipertensión, epilepsia, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, úlcera péptica, artritis reumatoide, lupus eritematoso sistémico, esclerosis múltiple, rinitis alérgica, sarcoidosis, diabetes mellitus, cetoacidosis diabética, hiperparatiroidismo, anuria, hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo, trastornos de la coagulación, anemia falciforme, hiperoxaluria primaria y hemocromatosis hereditaria, entre otras.
- **Interacciones farmacológicas**: se identificaron 25 interacciones en total (se dispone del detalle de 20). Las de nivel **moderado** incluyen anfetamina, dextroanfetamina, lisdexanfetamina, metanfetamina, benzfetamina, hidróxido de aluminio, bortezomib y deferoxamina. Las de nivel leve incluyen paclitaxel, cisplatino, doxorrubicina (incluida la liposomal), etinilestradiol, pseudoefedrina, efedrina, flecainida, flufenazina, indinavir y mexiletina.

No se dispone de datos de advertencias principales ni de contraindicaciones extraídas del prospecto; consultar el prospecto para informacion de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto en TxGNN, pero carece de ensayos clínicos, de literatura y de un vínculo mecanístico plausible (nivel L5). No hay base para avanzar con esta indicación.

**Para avanzar se necesita:**
- Datos del mecanismo de acción del fármaco y una justificación biológica de su relación con el desarrollo esofágico.
- Evidencia preclínica o clínica específica en malformaciones esofágicas, hoy inexistente.
- Texto de indicaciones y advertencias del prospecto de la AEMPS, que no está disponible actualmente.
- Revisión de la compatibilidad de la vía de administración (solo existen formas inyectables comercializadas).

**Nota sobre otras predicciones para este fármaco:** los datos compilados muestran candidatos con más respaldo que el analizado aquí. "Deficiencia vitamínica" (nivel L3, Proceed with Guardrails) es en realidad una extensión de la indicación ya autorizada. "Lesión/injury" (nivel L1, Research Question) cuenta con varios ensayos de fase 2 a 4, pero pequeños o heterogéneos. "Enfermedad esofágica" (nivel L4, Hold) tiene literatura mixta, con una señal de seguridad en un modelo de reflujo en ratas. Se recomienda evaluarlos por separado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

