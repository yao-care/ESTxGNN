---
layout: default
title: Gefitinib
parent: Solo predicción del modelo (L5)
nav_order: 371
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Gefitinib: nueva indicación predicha, Fibromatosis gingival (nivel de evidencia L5). Indicación original: Cáncer de pulmón no microcítico (según el grafo de conocimiento"
---

# Gefitinib
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

# Gefitinib: De Cáncer de Pulmón No Microcítico a Fibromatosis Gingival

## Resumen en Una Frase

Gefitinib es un inhibidor de la tirosina quinasa del receptor del factor de crecimiento epidérmico (EGFR), utilizado originalmente para el tratamiento del cáncer de pulmón no microcítico.
El modelo TxGNN predice que podría ser efectivo para **fibromatosis gingival**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de pulmón no microcítico (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Fibromatosis gingival |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 11 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, gefitinib inhibe la tirosina quinasa del EGFR, y su eficacia en el cáncer de pulmón no microcítico con mutaciones de EGFR está comprobada.

Mecanísticamente, la señalización de EGFR participa en la proliferación y el crecimiento celular, por lo que podría influir en procesos fibroproliferativos como la fibromatosis gingival. Sin embargo, esta relación es especulativa: no existe ningún estudio, ensayo ni publicación en los datos compilados que la respalde. El puntaje de 99.89% (posición 2513 del ranking del modelo) es el único sustento de esta predicción.

Además, la indicación original (un cáncer maligno) y la nueva (un crecimiento gingival fibroso, generalmente benigno) son muy distintas. Esto eleva el listón de la relación beneficio-riesgo, ya que se trataría de usar un fármaco oncológico en una condición no maligna.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Se muestran 5 de las 11 autorizaciones vigentes (todas de medicamentos con un único principio activo; no hay autorizaciones canceladas). Los textos de indicación aprobada no figuran en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 09526001 | IRESSA 250 mg comprimidos recubiertos con película | Comprimido recubierto con película | AstraZeneca AB |
| 83606 | Gefitinib Aristo 250 mg EFG | Comprimido recubierto con película | Aristo Pharma Iberia S.L. |
| 83716 | Gefitinib Sandoz 250 mg EFG | Comprimido recubierto con película | Sandoz Farmacéutica S.A. |
| 83851 | Gefitinib Teva 250 mg EFG | Comprimido recubierto con película | Teva B.V. |
| 84785 | Gefitinib Cipla 250 mg EFG | Comprimido recubierto con película | Cipla Europe |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa de EGFR), no citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Función hepática, función respiratoria (síntomas de enfermedad pulmonar intersticial) y vigilancia de toxicidad cutánea |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proviene del texto del prospecto): enfermedad hepática, enfermedad de la vesícula biliar, enfermedad pulmonar intersticial, fibrosis pulmonar y fibrosis pulmonar postinflamatoria.
- **Interacciones farmacológicas**: se identificaron 100 interacciones en total; las principales, de nivel moderado, son:
  - Antiácidos y antisecretores gástricos: famotidina, ranitidina, cimetidina, nizatidina y los inhibidores de la bomba de protones (omeprazol, esomeprazol, lansoprazol, dexlansoprazol, pantoprazol, rabeprazol).
  - Otros: aprepitant, claritromicina, dexametasona, naltrexona, miconazol, clotrimazol y troglitazona.
  - Con nivel desconocido: calcitriol y glimepirida.
- **Consideración específica**: la literatura recuperada para otras predicciones del mismo fármaco señala toxicidad cutánea, neumonitis/enfermedad pulmonar intersticial y prolongación del QT, aspectos a valorar en cualquier uso nuevo.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo (nivel L5), sin ensayos clínicos, literatura ni vínculo mecanístico demostrado, y la relación beneficio-riesgo de un inhibidor de EGFR oncológico en una condición generalmente benigna es desfavorable sin datos adicionales.

**Para avanzar se necesita:**
- Revisión bibliográfica dirigida sobre EGFR y fibromatosis gingival (modelos preclínicos).
- Datos detallados del mecanismo de acción y análisis del vínculo mecanístico con la nueva indicación.
- Información de seguridad del prospecto de la AEMPS (advertencias y contraindicaciones), actualmente no disponible.
- Evaluación de la compatibilidad de la vía de administración y de la viabilidad de una formulación o dosis adecuada para una condición no maligna.
- Comparación con alternativas terapéuticas ya establecidas para la fibromatosis gingival.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

