---
layout: default
title: Fluconazole
parent: Solo predicción del modelo (L5)
nav_order: 339
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-31
description: "Fluconazole: nueva indicación predicha, Queratoconjuntivitis epitelial punteada (nivel de evidencia L5). Indicación original: Candidiasis oral (y otras candidiasis, meningitis criptocócica)"
monitor_inn: "Fluconazole"
predicted_indications: ["punctate epithelial keratoconjunctivitis"]
---

# Fluconazole
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Fluconazol: De Candidiasis Oral a Queratoconjuntivitis Epitelial Punteada
{: .text-alpha }

## Resumen en Una Frase

Fluconazol es un antifúngico azólico utilizado originalmente para tratar candidiasis (oral, vulvovaginal, esofágica, diseminada y candidemia) y meningitis criptocócica.
El modelo TxGNN predice que podría ser efectivo para **queratoconjuntivitis epitelial punteada**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Candidiasis oral (y otras candidiasis, meningitis criptocócica) |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punteada |
| Puntaje de Predicción TxGNN | 0.9924 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 16) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, fluconazol es un antifúngico azólico que inhibe la enzima fúngica lanosterol 14-alfa-desmetilasa (CYP51), bloqueando la síntesis de ergosterol y comprometiendo la membrana de la célula fúngica. Su eficacia en candidiasis y criptococosis está comprobada.

La relación con la nueva indicación es débil. La queratoconjuntivitis epitelial punteada suele ser de origen viral (adenovirus), tóxico, o estar asociada a ojo seco y uso de lentes de contacto, causas que un antifúngico no aborda. Solo sería mecanísticamente aplicable si existiera un componente fúngico en algunos casos.

La puntuación proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. Debe tratarse únicamente como una hipótesis sin verificar.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

El medicamento está comercializado en este país, con 16 autorizaciones vigentes.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 58766 | DIFLUCAN 150 mg cápsulas duras | Cápsula dura | No disponible |
| 59672 | DIFLUCAN 10 mg/ml polvo para suspensión oral | Polvo para suspensión oral | No disponible |
| 68049 | FLUCONAZOL SALA 2 mg/ml solución para perfusión EFG | Solución para perfusión | No disponible |
| 69848 | CANDIFIX 150 mg cápsulas duras EFG | Cápsula dura | No disponible |
| 64619 | FLUCONAZOL NORMON 200 mg cápsulas duras EFG | Cápsula dura | No disponible |

---

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación o precaución (grafo de conocimiento, no texto del prospecto)**: síndrome de QT largo (incluido el familiar), enfermedad renal, piouréter, enfermedad hepática y enfermedad de la vesícula biliar.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones; entre las muestras revisadas:
  - **Mayor**: clorpropamida.
  - **Moderadas**: famotidina, rabeprazol, omeprazol, dexlansoprazol, hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida, loperamida, aprepitant, bisacodilo, ácido picosulfúrico, polietilenglicol con electrolitos y saxagliptina.
  - **Menores**: anfotericina B, clWarithromicina (claritromicina).

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única base es una puntuación alta del modelo (0.9924), sin ensayos clínicos ni literatura, y con una plausibilidad mecanística limitada, ya que las causas habituales de esta enfermedad no son fúngicas.

**Para avanzar se necesita:**
- Revisión sistemática de literatura sobre fluconazol en patología ocular (queratitis fúngica y uso oftálmico).
- Datos detallados del mecanismo de acción y análisis de su vínculo con la fisiopatología de la queratoconjuntivitis epitelial punteada.
- Textos de indicaciones, advertencias y contraindicaciones del prospecto de la AEMPS.
- Evaluación de la compatibilidad de vías de administración (oral/intravenosa frente a la vía tópica ocular).
- Evaluación de seguridad en población con prolongación del QT, enfermedad hepática o renal, y revisión de interacciones.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

