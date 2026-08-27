---
layout: default
title: Niraparib
parent: 僅模型預測 (L5)
nav_order: 198
evidence_level: L5
indication_count: 10
---

# Niraparib
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

# Niraparib: De Cáncer de Ovario Seroso Recidivante a Neoplasia Quística (Carcinoma Seroso de Endometrio)

## Resumen en Una Frase

Niraparib es un inhibidor de PARP1/2 utilizado como terapia de mantenimiento en cáncer de ovario epitelial, trompa de Falopio o peritoneal primario recidivante sensible a platino. El modelo TxGNN predice que también podría ser efectivo para **Neoplasia Quística** (categoría que en la evidencia recuperada corresponde principalmente a carcinoma seroso de endometrio, biológicamente emparentado con el cáncer de ovario seroso de alto grado), con **3 ensayos clínicos** y **9 publicaciones** que actualmente respaldan esta dirección. Cabe advertir que, según el propio análisis mecanístico del pack, esta "nueva" indicación se solapa en gran medida con el área terapéutica ya aprobada del fármaco, más que representar una hipótesis de reposicionamiento verdaderamente novedosa.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de ovario epitelial, trompa de Falopio o peritoneal primario recidivante sensible a platino (terapia de mantenimiento) |
| Nueva Indicación Predicha | Neoplasia quística (carcinoma seroso de endometrio / ovario) |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L2 |
| Estado de Mercado | No comercializado (0 autorizaciones registradas) |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de una ficha formal de mecanismo de acción en la base de datos del fármaco (dato pendiente de captura desde DrugBank), pero la evidencia clínica y de literatura recopilada en este pack sí lo documenta: Niraparib es un inhibidor de PARP1/2 que induce letalidad sintética en células tumorales con deficiencia de recombinación homóloga (HRD), incluyendo mutaciones BRCA1/2. Este mecanismo es la base de su aprobación original en cáncer de ovario seroso de alto grado.

El carcinoma seroso de endometrio comparte características moleculares con el carcinoma seroso de ovario de alto grado (HGSOC) —inestabilidad cromosómica, perfiles similares de variación de número de copias somáticas y mutaciones somáticas—, por lo que su manejo clínico ya suele calcarse del modelo terapéutico del HGSOC. Esto hace mecanísticamente plausible que un inhibidor de PARP aprobado para cáncer de ovario seroso muestre actividad en tumores serosos de endometrio con deficiencia de HRD.

Dicho esto, el propio análisis de reposicionamiento incluido en el pack señala que la etiqueta "cystic neoplasm" es probablemente una clasificación ontológica gruesa que engloba estos tumores serosos ováricos/endometriales, es decir, la predicción del modelo estaría mayormente redescubriendo el área terapéutica ya establecida del fármaco (cáncer ginecológico seroso HRD-positivo) en lugar de señalar un uso genuinamente nuevo.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04716686](https://clinicaltrials.gov/study/NCT04716686) | Fase 2 | Reclutando | 83 | Niraparib en monoterapia como tratamiento de mantenimiento y de recidiva en carcinoma seroso de endometrio, basado en la similitud molecular con HGSOC. |
| [NCT05289648](https://clinicaltrials.gov/study/NCT05289648) | Fase 0 (Early Phase 1) | Retirado | 0 | Estudio exploratorio del efecto molecular/clínico de niraparib preoperatorio en cáncer de endometrio de alto grado; retirado sin datos disponibles. |
| [NCT04159155](https://clinicaltrials.gov/study/NCT04159155) | Fase 2/3 | Terminado | 11 | Ensayo canadiense multi-brazo (umbrella) sobre tratamiento de primera línea y mantenimiento en cáncer de endometrio seroso o p53 mutante; terminado con reclutamiento muy por debajo del objetivo. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40473279](https://pubmed.ncbi.nlm.nih.gov/40473279/) | 2025 | ECA/Cohorte | BMJ Open | Protocolo de ensayo Fase 2 de mantenimiento con niraparib en carcinoma seroso uterino estadio III/IV, recidivante quimio-naïve o sensible a platino. |
| [40702505](https://pubmed.ncbi.nlm.nih.gov/40702505/) | 2025 | Cohorte/Bioinformática | Journal of Ovarian Research | Identificación de subtipos de células madre tumorales y modelo pronóstico en HGSOC, con genes relacionados sobreexpresados en macrófagos (VSIG4, STAB1). |
| [31851805](https://pubmed.ncbi.nlm.nih.gov/31851805/) | 2019 | Revisión | New England Journal of Medicine | Medicina personalizada para el tratamiento primario del cáncer de ovario seroso. |
| [34321239](https://pubmed.ncbi.nlm.nih.gov/34321239/) | 2021 | Cohorte/Mecanístico | Cancer Research | Pérdida adquirida de metilación del promotor RAD51C como causa de resistencia a inhibidores de PARP en HGSOC. |
| [41323499](https://pubmed.ncbi.nlm.nih.gov/41323499/) | 2025 | Cohorte | Pathology Oncology Research | Perfilado genómico integral de HRD (FoundationOne CDx) para guiar recomendaciones de terapia con inhibidores de PARP en cáncer de ovario. |
| [41520277](https://pubmed.ncbi.nlm.nih.gov/41520277/) | 2026 | Preclínico | Cancer Biology & Therapy | Eficacia de la combinación carboplatino + inhibidor de PARP evaluada en esferoides y organoides de HGSOC. |
| [41214101](https://pubmed.ncbi.nlm.nih.gov/41214101/) | 2025 | Investigación básica | Scientific Reports | Claudin-4 como regulador dual de estabilidad genómica y evasión inmune en HGSOC, vinculado a resistencia terapéutica. |
| [31466953](https://pubmed.ncbi.nlm.nih.gov/31466953/) | 2019 | Reporte de caso | BMJ Case Reports | Uso de niraparib como terapia de mantenimiento en una paciente con cáncer de ovario y metástasis cerebrales. |
| [41465250](https://pubmed.ncbi.nlm.nih.gov/41465250/) | 2025 | Investigación básica | International Journal of Molecular Sciences | Determinación proteómica global de los efectos poli-farmacológicos de olaparib, niraparib y rucaparib en células de HGSOC. |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida — inhibidor de PARP1/2 (no es quimioterapia citotóxica convencional) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe evidencia de nivel L2 (ensayos de Fase 2/3, aunque ninguno completado con éxito estadístico claro) y 9 publicaciones que sustentan la extensión del mecanismo de niraparib a tumores serosos de endometrio con perfil molecular HRD-positivo. Sin embargo, esta "nueva" indicación se solapa conceptualmente con el área terapéutica ya aprobada del fármaco, por lo que debe tratarse como una extensión de indicación dentro de la misma familia biológica y no como un descubrimiento de reposicionamiento independiente.

De las otras 9 indicaciones predichas por TxGNN en este pack, 8 (epiglotis, hipofaringe benigno, lengua benigno, suelo de boca benigno, neuroblastoma cervical, tumor de testículo/paratestículo, oído interno, schwannoma del foramen yugular) carecen totalmente de ensayos o literatura de apoyo (L5/S0) y están correctamente marcadas como **Hold** — el propio análisis las atribuye a un posible sesgo de agrupamiento del modelo. La indicación "pre-malignant neoplasm" (rank 9) alcanza L4/S1 (**Research Question**), con 13 ensayos pero ninguno diseñado específicamente para lesiones premalignas.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha técnica de niraparib (TFDA/AEMPS) para completar la evaluación de seguridad S1, actualmente bloqueada por falta de datos de advertencias y contraindicaciones (gap bloqueante).
- Formalizar el dato de mecanismo de acción (MOA) directamente desde DrugBank en la ficha del fármaco.
- Confirmar el estatus real de comercialización en el mercado de destino, dado que actualmente figura sin licencias registradas.
- Resultados maduros de NCT04716686 (Fase 2, en curso) antes de considerar avanzar a diseño de estudio propio.
- Aclarar si "cystic neoplasm" debe tratarse como extensión de indicación (mismo mecanismo/población ya aprobada) o como candidato de reposicionamiento independiente, antes de asignar recursos de desarrollo.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

