---
layout: default
title: Minoxidil
parent: 僅模型預測 (L5)
nav_order: 184
evidence_level: L5
indication_count: 10
---

# Minoxidil
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

# Minoxidil: De Hipertensión Arterial a Hipotricosis Simple del Cuero Cabelludo

## Resumen en Una Frase

Minoxidil es un vasodilatador oral utilizado clásicamente para el tratamiento de la hipertensión arterial grave, actuando como abridor de canales de potasio (K+ ATP).
El modelo TxGNN predice que podría ser efectivo para la **Hipotricosis Simple del Cuero Cabelludo**, una enfermedad genética rara del folículo piloso,
con evidencia actual limitada a **3 publicaciones de casos clínicos** y **ningún ensayo clínico registrado**.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Hipertensión arterial grave (uso oral histórico) |
| Nueva Indicacion Predicha | Hipotricosis Simple del Cuero Cabelludo |
| Puntaje de Prediccion TxGNN | 99.9999% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de una ficha estructurada del mecanismo de acción (MOA) para minoxidil. Sin embargo, la literatura recogida en este informe describe a minoxidil como un abridor de canales de potasio (K+ ATP) con efecto vasodilatador que, a nivel folicular, prolonga la fase anágena e induce la vía de señalización Wnt/β-catenina — mecanismo ya reconocido y aprovechado en el uso tópico establecido de minoxidil para la alopecia androgenética (AGA).

La hipotricosis simple del cuero cabelludo es un trastorno monogénico autosómico dominante raro, asociado a variantes del gen *CDSN* (corneodesmosina), que al igual que la AGA cursa con alteración del ciclo de crecimiento del folículo piloso. Dado que el efecto de minoxidil actúa directamente sobre ese ciclo (fases anágena/telógena) con independencia de la causa subyacente de la miniaturización folicular, existe una lógica mecanística razonable para extender su uso a esta indicación.

No obstante, al tratarse de una enfermedad genética con muy pocos pacientes en el mundo, es intrínsecamente difícil generar evidencia de mayor nivel (ensayos aleatorizados), por lo que la evidencia disponible se limita a reportes de caso aislados, muchas veces en combinación con otras terapias (factores de crecimiento, extractos botánicos, PRP).

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39902296](https://pubmed.ncbi.nlm.nih.gov/39902296/) | 2024 | Reporte de caso | Frontiers in genetics | Caso familiar de HSS en un niño de 8 años por mutación en *CDSN*, tratado con combinación de extractos botánicos y minoxidil |
| [35761391](https://pubmed.ncbi.nlm.nih.gov/35761391/) | 2022 | Reporte de caso | Dermatologic therapy | Tratamiento de hipotricosis simple hereditaria del cuero cabelludo con minoxidil oral combinado con factores de crecimiento |
| [36651821](https://pubmed.ncbi.nlm.nih.gov/36651821/) | 2023 | Reporte de caso | The Journal of dermatological treatment | Tratamiento exitoso mediante inyección de plasma rico en plaquetas (PRP) combinada con minoxidil tópico al 2% |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusion y Proximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia disponible para esta indicación se limita a 3 reportes de caso (nivel L4), sin ningún ensayo clínico registrado, en una enfermedad genética de muy baja prevalencia. Esto corresponde a una etapa de "pregunta de investigación" (S2), insuficiente para avanzar incluso con medidas de mitigación (guardrails).

**Para avanzar se necesita:**
- Datos estructurados del mecanismo de acción (MOA) de minoxidil
- Advertencias y contraindicaciones del prospecto (TFDA/AEMPS), actualmente bloqueado como data gap crítico
- Series de casos más amplias o un registro de pacientes con hipotricosis simple, dado lo improbable de un ECA en esta población
- Evaluación de interacciones farmacológicas, ya que la base de datos DDI no arrojó resultados
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

