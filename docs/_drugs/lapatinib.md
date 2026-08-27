---
layout: default
title: Lapatinib
parent: 僅模型預測 (L5)
nav_order: 158
evidence_level: L5
indication_count: 1
---

# Lapatinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Lapatinib: De Cáncer de Mama HER2-positivo a Dermatofibrosarcoma Protuberans

## Resumen en Una Frase

Lapatinib es un inhibidor dual de tirosina cinasa (EGFR/HER2), utilizado internacionalmente en el tratamiento del cáncer de mama HER2-positivo.
El modelo TxGNN predice que podría ser efectivo para **Dermatofibrosarcoma Protuberans**,
pero actualmente **no existen ensayos clínicos ni publicaciones** que respalden esta dirección — la evidencia disponible es únicamente la predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de mama HER2-positivo (metastásico) — conocimiento general, no consta en el Evidence Pack |
| Nueva Indicación Predicha | Dermatofibrosarcoma Protuberans |
| Puntaje de Predicción TxGNN | 99.30% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción ni sobre la indicación original en este Evidence Pack (ambos marcados como brecha de datos, con la carencia de advertencias/contraindicaciones de ficha técnica clasificada como bloqueante). Según el conocimiento general disponible, Lapatinib es un inhibidor dual de tirosina cinasa que actúa sobre EGFR (ErbB1) y HER2 (ErbB2), y su eficacia en el cáncer de mama HER2-positivo está ampliamente establecida a nivel internacional.

No hay, sin embargo, ningún ensayo clínico ni publicación en el Evidence Pack que conecte mecanísticamente Lapatinib con el dermatofibrosarcoma protuberans (un sarcoma cutáneo asociado a menudo a la fusión COL1A1-PDGFB, con dependencia de la señalización del receptor PDGFR). La plausibilidad mecanística entre la inhibición de tirosina cinasas y esta vía de señalización no puede confirmarse ni descartarse con los datos actuales, por lo que la predicción debe considerarse exploratoria.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina cinasa EGFR/HER2) |
| Riesgo de Mielosupresión | Bajo (perfil típico de terapias dirigidas, menor que la quimioterapia citotóxica convencional) |
| Clasificación de Emetogenicidad | Baja |
| Items de Monitoreo | Función hepática, función cardíaca (FEVI), intervalo QT |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún ensayo clínico ni publicación que respalde la predicción, el fármaco no está comercializado en España, y faltan datos críticos de seguridad (ficha técnica TFDA, clasificada como brecha bloqueante) y de mecanismo de acción. La evidencia actual es exclusivamente la puntuación del modelo TxGNN (L5).

**Para avanzar se necesita:**
- Ficha técnica/prospecto de TFDA con advertencias y contraindicaciones (DG001, bloqueante)
- Datos de mecanismo de acción vía DrugBank API (DG002)
- Búsqueda ampliada de ensayos clínicos y literatura sobre Lapatinib en dermatofibrosarcoma protuberans (posiblemente en fuentes distintas a ClinicalTrials.gov/ICTRP/PubMed, o evaluando vías mecanísticas relacionadas como PDGFR)
- Evaluación de la disponibilidad/autorización de Lapatinib en España
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

