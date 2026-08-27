---
layout: default
title: Venetoclax
parent: 僅模型預測 (L5)
nav_order: 292
evidence_level: L5
indication_count: 10
---

# Venetoclax
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

# Venetoclax: De Leucemia Linfocítica Crónica a Leucemia Linfocítica Crónica/Linfoma Linfocítico de Células Pequeñas de Origen Pre-Centro Germinal

## Resumen en Una Frase

Venetoclax es un inhibidor selectivo de BCL-2 cuya eficacia ya está firmemente establecida en la leucemia linfocítica crónica/linfoma linfocítico de células pequeñas (LLC/LLP) y en la leucemia mieloide aguda (LMA), respaldada por ensayos pivotales como MURANO. El modelo TxGNN predice adicionalmente que podría ser eficaz en el subtipo de LLC/LLP de origen pre-centro germinal (IGHV no mutado, mal pronóstico), pero esta dirección específica cuenta actualmente solo con **1 publicación** (una revisión indirecta) y **ningún ensayo clínico** que la respalde de forma directa.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Leucemia linfocítica crónica/linfoma linfocítico de células pequeñas (LLC/LLP) y leucemia mieloide aguda (LMA) — según evidencia citada en el propio evidence pack (ensayo MURANO); no confirmado por ficha técnica AEMPS, ya que el producto no está comercializado en España |
| Nueva Indicación Predicha | LLC/LLP de origen pre-centro germinal (subtipo IGHV no mutado) |
| Puntaje de Predicción TxGNN | 99.55% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

No se dispone actualmente de datos detallados y verificados sobre el mecanismo de acción (MOA) de venetoclax procedentes de las fuentes consultadas (DrugBank/TFDA). Según la evidencia recopilada en este mismo informe, venetoclax es un inhibidor de BCL-2 —una proteína antiapoptótica que permite la supervivencia de células malignas dependientes de esta vía— y su eficacia en LLC/LLP en general ya ha sido demostrada de forma sólida (ensayo de fase 3 MURANO, entre otros).

La nueva indicación predicha no es una enfermedad distinta, sino un **subtipo molecular** de la propia LLC/LLP: el originado en células B pre-centro germinal, caracterizado por genes de la región variable de inmunoglobulina no mutados (U-IGHV) y peor pronóstico frente al subtipo post-centro germinal mutado (M-CLL). Mecanísticamente resulta razonable extrapolar la dependencia de BCL-2 —ya demostrada en la LLC en su conjunto— a este subgrupo de peor pronóstico. Sin embargo, la única publicación disponible se limita a caracterizar la estructura y función del receptor de células B (BCR) en este subtipo, sin evaluar directamente la respuesta a venetoclax, por lo que la evidencia es indirecta.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35158929](https://pubmed.ncbi.nlm.nih.gov/35158929/) | 2022 | Revisión | Cancers | Caracteriza el receptor de células B (BCR) tumoral en LLC, diferenciando el subtipo pre-centro germinal (U-IGHV, mal pronóstico) del post-centro germinal (M-IGHV, buen pronóstico); no evalúa directamente la eficacia de venetoclax en este subtipo |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor selectivo de BCL-2), no quimioterapia citotóxica convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación predicha en primer lugar por TxGNN es en realidad un subtipo molecular de la LLC/LLP, para el cual solo existe una publicación indirecta (sin ensayos clínicos ni evaluación directa de venetoclax). El nivel de evidencia (L4) no justifica avanzar más allá de la etapa de investigación exploratoria.

**Para avanzar se necesita:**
- Resolver el vacío de datos bloqueante sobre advertencias/contraindicaciones de la ficha técnica de la TFDA/AEMPS (DG001), imprescindible antes de cualquier evaluación de seguridad (S1)
- Obtener datos verificados del mecanismo de acción (MOA) directamente de DrugBank (DG002)
- Buscar estudios que evalúen venetoclax específicamente en pacientes con LLC/LLP de IGHV no mutado (pre-centro germinal), más allá de la evidencia general en LLC
- Confirmar el estatus regulatorio real en España, dado que el producto figura como no comercializado pese a ser un fármaco con aprobación conocida en otras indicaciones hematológicas
- Considerar en paralelo otros candidatos del mismo evidence pack con mayor nivel de evidencia (p. ej., leucemia mieloide crónica BCR-ABL1+ en fase S2/L2, o linfoma folicular en fase S2/L2), que podrían representar oportunidades de reposicionamiento más sólidas que la indicación de rango 1
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

