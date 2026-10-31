---
layout: default
title: Desmopressin
parent: Solo predicción del modelo (L5)
nav_order: 235
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-31
monitor_inn: "desmopressin"
predicted_indications: ["congenital prothrombin deficiency", "inherited thrombophilia", "Glanzmann thrombasthenia", "primary release disorder of platelets", "Scott syndrome", "flood factor deficiency"]
description: "Desmopressin: nueva indicación predicha, Deficiencia congénita de protrombina (congenital prothrombin deficiency) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Desmopressin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Desmopressin: Deficiencia congénita de protrombina (congenital prothrombin deficiency)
{: .text-alpha }

## Resumen en Una Frase

Desmopresina es un análogo sintético de la vasopresina, utilizado originalmente para la enfermedad de von Willebrand, la hemofilia A leve y la enuresis nocturna.
El modelo TxGNN predice que podría ser efectivo para **deficiencia congénita de protrombina**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Deficiencia congénita de protrombina (congenital prothrombin deficiency) |
| Puntaje de Predicción TxGNN | 0.9970 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 13) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, la desmopresina eleva los niveles plasmáticos del factor VIII y del factor de von Willebrand (VWF) mediante su liberación desde los depósitos endoteliales, a través de la activación de los receptores V2.

La protrombina (factor II) no se libera por esta vía, por lo que **no existe una base mecanística clara** para un beneficio en la deficiencia congénita de protrombina. Ambas son enfermedades hemorrágicas hereditarias, y es probable que el alto puntaje del modelo TxGNN (deep learning) refleje similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

En conclusión, esta predicción debe considerarse una hipótesis sin respaldo mecanístico ni clínico en este momento.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones vigentes (todas de monofármaco). El texto de la indicación aprobada no está disponible en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 89023 | Desmopresina Aristo 240 microgramos comprimidos sublinguales EFG | Comprimido sublingual | No disponible |
| 68268 | Minurin Flas 120 microgramos liofilizado oral | Liofilizado oral | No disponible |
| 61413 | Minurin 4 microgramos/ml solución inyectable | Solución inyectable | No disponible |
| 58566 | Minurin 0,1 mg/ml solución para pulverización nasal | Solución para pulverización nasal | No disponible |
| 78875 | Desmirin 360 microgramos/ml solución oral | Solución oral | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones o enfermedades de riesgo según el grafo de conocimiento** (no proviene del texto del prospecto): hipertensión, enfermedad coronaria, insuficiencia renal, fibrosis quística, polidipsia, polidipsia/diabetes insípida dipsogénica, intoxicación por agua, rinitis alérgica o vasomotora, faringitis, resfriado común e infecciones respiratorias.
- **Interacciones farmacológicas**: se identificaron 172 interacciones. Entre las principales:
  - **Mayor**: hidrocortisona, triamcinolona, dexametasona, beclometasona, betametasona, budesonida, prednisolona y prednisona.
  - **Moderada**: epinefrina, loperamida, morfina (incluida la liposomal), opio y clorpropamida.
  - **Menor**: ácido acetilsalicílico.
- Además, la literatura general señala que el uso de desmopresina puede complicarse con hiponatremia y, raramente, con eventos trombóticos arteriales.

Para el resto de la información de seguridad, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de ensayos clínicos y de literatura, y la desmopresina no actúa sobre la vía de la protrombina, por lo que el puntaje de 0.9970 parece un artefacto computacional y no una señal terapéutica.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) y del texto de indicaciones, advertencias y contraindicaciones del prospecto de la AEMPS.
- Una justificación mecanística plausible para la deficiencia de protrombina, o bien datos preclínicos.
- Priorizar otras predicciones con mayor respaldo (p. ej., trastorno de liberación plaquetaria, con nivel L3 y estudios observacionales).

**Nota sobre otras indicaciones predichas:**
- **Trastorno primario de liberación plaquetaria**: L3, la más prometedora; requiere confirmación.
- **Trombastenia de Glanzmann**: L4, evidencia indirecta; el estándar de tratamiento es la transfusión de plaquetas y FVIIa recombinante.
- **Trombofilia hereditaria** y **enfermedad de von Willebrand pseudo (tipo plaquetario)**: el mecanismo es contrario o desfavorable, y el uso podría ser inadecuado.
- **Síndrome de Scott**: L5, sin datos de eficacia.
- **"Flood factor deficiency"**: entidad que parece un artefacto de datos; debe verificarse antes de cualquier evaluación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

