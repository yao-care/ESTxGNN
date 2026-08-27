---
layout: default
title: Alectinib
parent: 僅模型預測 (L5)
nav_order: 16
evidence_level: L5
indication_count: 10
---

# Alectinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Alectinib: De Cáncer de Pulmón No Microcítico ALK-Positivo a Fibromatosis Gingival

## Resumen en Una Frase

Alectinib es un inhibidor de la tirosina quinasa ALK utilizado originalmente para el tratamiento del cáncer de pulmón no microcítico (CPNM) ALK-positivo. El modelo TxGNN predice que podría ser efectivo para **Fibromatosis Gingival**, pero actualmente **no existe ningún ensayo clínico ni publicación** que respalde esta dirección, por lo que la señal debe considerarse de muy baja confianza.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de pulmón no microcítico (CPNM) ALK-positivo *(no hay registro de licencia en España; inferido del contexto de la literatura incluida en este paquete de evidencia)* |
| Nueva Indicación Predicha | Fibromatosis Gingival |
| Puntaje de Predicción TxGNN | 99.97% (rango del modelo: 1129) |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción (MOA) de alectinib en la ficha de este candidato. Según la información conocida a través de la literatura incluida en este mismo paquete de evidencia, alectinib es un inhibidor selectivo, competitivo con ATP, de segunda generación de la anaplastic lymphoma kinase (ALK); su eficacia en el CPNM ALK-positivo ha sido ampliamente comprobada en múltiples ensayos de Fase 3 (ALEX, J-ALEX, ALESIA, ALINA).

Sin embargo, en el caso concreto de la Fibromatosis Gingival, la relación mecanística con la indicación original **no es sostenible**. La fibromatosis gingival es una enfermedad benigna de hiperplasia fibrosa asociada principalmente a mutaciones constitucionales en genes como SOS1, sin que exista evidencia de que la vía de señalización ALK participe en su fisiopatología. El puntaje elevado de TxGNN (99.97%) no está acompañado de ningún ensayo clínico ni publicación, lo que es coherente con la propia valoración del modelo: se trata de una señal probablemente ruidosa de la "cola larga" del modelo (rango 1129 de la red), no de una hipótesis mecanísticamente fundamentada.

**Conclusión de esta sección:** no se identifica una base biológica razonable para esta predicción específica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Citotoxicidad

Alectinib pertenece a la clase de inhibidores de tirosina quinasa dirigidos contra ALK, utilizada en el tratamiento de neoplasias malignas (CPNM ALK-positivo), por lo que se documenta la siguiente información orientativa:

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa ALK) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Función hepática, electrocardiograma (prolongación de QTc), hemograma (se han descrito casos de anemia hemolítica), peso corporal (se ha descrito aumento de peso en tratamiento prolongado) |
| Protección en Manejo | Al tratarse de un antineoplásico oral, debe manipularse conforme a la normativa institucional de fármacos peligrosos (hazardous drugs) |

*Nota: los ítems de monitoreo anteriores se basan en notificaciones de casos y subestudios encontrados en la literatura de este mismo paquete de evidencia (p. ej., prolongación de QTc, anemia hemolítica, aumento de peso), no en una ficha técnica formal, ya que la ficha técnica de TFDA/AEMPS para este fármaco constituye actualmente un vacío de datos de carácter bloqueante (ver Conclusión).*

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Otras Indicaciones Candidatas Evaluadas en este Paquete de Evidencia

Este Evidence Pack (versión multi-candidato) evaluó 10 indicaciones predichas para alectinib. Ninguna alcanza el nivel de evidencia necesario para una recomendación de "Go", pero dos candidatos presentan señales de investigación que merecen seguimiento, y dos presentan una alerta relevante de calidad de datos:

| Rango | Indicación | Puntaje TxGNN | Nivel de Evidencia | Recomendación | Observación Clave |
|------|------|------|------|------|------|
| 1 | Fibromatosis Gingival | 99.97% | L5 | Hold | Sin mecanismo ni evidencia; ruido de cola larga |
| 2 | Fibroma Pulmonar | 99.96% | L5 | Hold | Sin mecanismo ALK conocido; sin evidencia |
| 3 | Hamartoma Pulmonar | 99.96% | L5 | Hold | Impulsado por HMGA2, no por ALK; sin evidencia |
| 4 | Carcinoma del Hilio Pulmonar | 99.96% | L3 | Research Question | Subtipo anatómico de CPNM ALK+; única literatura hallada es un caso de toxicidad, no de eficacia específica |
| 5 | Neoplasia Pulmonar Benigna | 99.95% | L4 | Hold | **Alerta de calidad de datos**: los 20 artículos hallados corresponden en realidad a ensayos pivotales (ALEX, J-ALEX, ALINA) de CPNM **maligno** ALK+, probable error de indexación por sinónimos; no debe usarse como evidencia de neoplasia benigna |
| 6 | Tumor de Células Germinales Pulmonar | 99.95% | L3 | Research Question | Existe ensayo basket activo (NCT05770037, DETERMINE) para tumores ALK-positivos raros; literatura específica limitada a neuroendocrinos/carcinoides atípicos, no a tumores de células germinales |
| 7 | Neoplasia del Surco Pulmonar (Pancoast) | 99.95% | L4 | Research Question | Subtipo anatómico de CPNM; sin evidencia directa, solo extrapolación de clase |
| 8 | Síndrome de Leucomelanodermia-Infantilismo-Discapacidad Intelectual-Hipodoncia-Hipotricosis | 99.95% | L5 | Hold | **Alerta de calidad de datos**: literatura hallada no guarda relación con el síndrome; error de indexación |
| 9 | IBMPFD/Demencia Frontotemporal | 99.95% | L5 | Hold | **Alerta de calidad de datos**: mecanismo real es la vía VCP, sin relación con ALK; literatura hallada trata de FTD en general, sin mención de alectinib |
| 10 | Epidermólisis Ampollosa Juntural | 99.95% | L5 | Hold | Enfermedad estructural (LAMA3/LAMB3/LAMC2, COL17A1); sin mecanismo ni evidencia |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- La indicación de rango 1 (Fibromatosis Gingival) carece de fundamento mecanístico y de cualquier evidencia clínica o de literatura; el propio análisis de razonamiento del paquete de evidencia la califica como probable ruido del modelo.
- A nivel de fármaco existen dos vacíos de datos críticos: (1) advertencias/contraindicaciones oficiales de ficha técnica (TFDA/AEMPS) — **bloqueante** para cualquier evaluación de seguridad (S1); y (2) mecanismo de acción detallado — de alta prioridad para el análisis de plausibilidad mecanística.
- Alectinib no está actualmente comercializado en España (0 autorizaciones), lo que también limita el contexto regulatorio disponible.

**Para avanzar se necesita:**
- Obtener la ficha técnica oficial (TFDA/AEMPS) con advertencias, contraindicaciones e interacciones farmacológicas (Data Gap bloqueante DG001).
- Completar los datos de mecanismo de acción (MOA) desde DrugBank (Data Gap DG002).
- Corregir el posible error de indexación/mapeo de enfermedad-literatura observado en los candidatos "Neoplasia Pulmonar Benigna", "Síndrome de Leucomelanodermia..." e "IBMPFD/Demencia Frontotemporal" antes de reutilizar esa evidencia.
- Si se desea continuar la línea de investigación, priorizar el candidato "Tumor de Células Germinales Pulmonar" (rango 6), dado el ensayo activo tipo basket (NCT05770037) que incluye cánceres ALK-positivos raros, mediante confirmación del estado de fusión ALK en la población objetivo.
- Descartar o reformular la hipótesis de "Fibromatosis Gingival" salvo que aparezca nueva evidencia mecanística o clínica.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

