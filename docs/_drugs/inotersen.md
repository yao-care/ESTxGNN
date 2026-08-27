---
layout: default
title: Inotersen
parent: 僅模型預測 (L5)
nav_order: 146
evidence_level: L5
indication_count: 10
---

# Inotersen
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

# Inotersen: De Amiloidosis Hereditaria por Transtirretina (hATTR) a Porfiria Intermitente Aguda

## Resumen en Una Frase

Inotersen es un oligonucleotido antisentido (ASO) dirigido al ARNm de transtirretina (TTR), cuya indicacion conocida es la polineuropatia por amiloidosis hereditaria mediada por transtirretina (hATTR); esta informacion proviene del analisis mecanistico interno, ya que el campo de MOA formal del Evidence Pack esta vacio.
El modelo TxGNN predice que podria ser efectivo para **Porfiria Intermitente Aguda**,
pero actualmente **no hay ensayos clinicos** y solo **1 publicacion** (una revision general, no especifica de esta indicacion) respalda esta direccion.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Amiloidosis hereditaria por transtirretina (hATTR) con polineuropatia (informacion conocida del farmaco; no confirmada por licencias de AEMPS en este Evidence Pack) |
| Nueva Indicacion Predicha | Porfiria Intermitente Aguda |
| Puntaje de Prediccion TxGNN | 99.92% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Espana | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

El Evidence Pack no incluye datos formales de mecanismo de accion (campo marcado como vacio), pero el analisis mecanistico interno aporta contexto util: inotersen es un ASO de segunda generacion que se dirige al ARNm de TTR en el higado y lo degrada via RNase H1, reduciendo la produccion de transtirretina causante de la amiloidosis en hATTR.

La Porfiria Intermitente Aguda (PIA) es una enfermedad monogenica distinta, causada por deficiencia de HMBS (PBGD), que provoca acumulacion de ALA/PBG. Su diana terapeutica establecida es el ARNm de ALAS1 (abordado por siRNA como givosiran), sin ninguna via molecular compartida con TTR.

La puntuacion elevada de TxGNN probablemente refleja una similitud de categoria — ambos son farmacos de accion hepatica basados en oligonucleotidos para enfermedades metabolicas monogenicas del higado — mas que una superposicion real de mecanismo molecular. Esto se traduce en una hipotesis biologicamente debil que no deberia interpretarse como evidencia de eficacia real.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados.

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30847674](https://pubmed.ncbi.nlm.nih.gov/30847674/) | 2019 | Revision | Neurological Sciences | Revision general sobre avances terapeuticos en neuropatias perifericas hereditarias (incluyendo hATTR); menciona farmacos como inotersen dentro de la "revolucion terapeutica" en amiloidosis hATTR, pero no aborda especificamente la Porfiria Intermitente Aguda. Relevancia pendiente de confirmar. |

## Consideraciones de Seguridad

No hay datos formales de seguridad disponibles en este Evidence Pack (advertencias, contraindicaciones e interacciones farmacologicas figuran como vacios) — consultar el prospecto/ficha tecnica para informacion completa. El analisis mecanistico interno si menciona, como conocimiento de referencia, que inotersen tiene advertencias conocidas de trombocitopenia y glomerulonefritis, relevantes para cualquier evaluacion de seguridad posterior.

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La evidencia es insuficiente para avanzar: nivel L4 sin ningun ensayo clinico y una sola publicacion de relevancia no confirmada. Ademas, el vinculo mecanistico entre el objetivo de inotersen (TTR) y la fisiopatologia de la Porfiria Intermitente Aguda (via ALAS1) no esta establecido, lo que sugiere que la puntuacion de TxGNN refleja similitud de categoria de farmaco mas que una hipotesis biologica solida. El farmaco tampoco esta comercializado en Espana (0 autorizaciones).

**Para avanzar se necesita:**
- Ficha tecnica/prospecto oficial (AEMPS o fabricante) con advertencias y contraindicaciones — actualmente bloqueante (DG001)
- Datos formales de mecanismo de accion (DG002)
- Estudios preclinicos o de mecanismo que evaluen directamente TTR-ASO en el contexto de PIA
- Confirmacion de relevancia de la publicacion PMID 30847674 respecto a esta indicacion especifica

**Nota adicional:** El Evidence Pack incluye otros 9 candidatos de menor prioridad (apendicitis, meningitis infecciosa/no infecciosa, peritonitis y varias enfermedades del espectro IgG4-relacionado), todos con nivel de evidencia L5, sin ensayos clinicos ni literatura, y sin vinculo mecanistico identificable con el objetivo de TTR. Se recomienda **Hold** para todos ellos por tratarse de ruido de prediccion del modelo.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

