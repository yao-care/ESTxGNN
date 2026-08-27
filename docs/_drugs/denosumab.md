---
layout: default
title: Denosumab
parent: 僅模型預測 (L5)
nav_order: 88
evidence_level: L5
indication_count: 2
---

# Denosumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Denosumab: De Osteoporosis a Retinopatía Diabética No Proliferativa Severa

## Resumen en Una Frase

Denosumab es un anticuerpo monoclonal anti-RANKL, utilizado originalmente en el manejo de la pérdida ósea (osteoporosis y complicaciones esqueléticas asociadas). El modelo TxGNN predice que podría ser efectivo para **Retinopatía Diabética No Proliferativa Severa**, pero actualmente **no existen ensayos clínicos ni publicaciones registradas** que respalden directamente esta indicación específica — la predicción se apoya únicamente en el puntaje del modelo (99.63%).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Osteoporosis y pérdida ósea (uso general conocido del fármaco; no hay licencia registrada en el mercado evaluado) |
| Nueva Indicación Predicha | Retinopatía Diabética No Proliferativa Severa |
| Puntaje de Predicción TxGNN | 99.63% |
| Nivel de Evidencia | L5 |
| Estado de Mercado | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de denosumab en este paquete de evidencia. Según la información conocida, denosumab es un anticuerpo monoclonal que inhibe RANKL (clase: inhibidor de RANKL/RANK/OPG), y su eficacia en la inhibición de la resorción ósea ha sido ampliamente comprobada. Mecanísticamente, el eje RANKL/RANK/OPG también participa en procesos de inflamación vascular y angiogénesis, lo que constituye la base teórica —aunque no confirmada experimentalmente— de su posible aplicabilidad a la retinopatía diabética.

Para la indicación específica de **retinopatía diabética no proliferativa severa** (rank 1), no hay ningún ensayo clínico ni publicación que sustente esta hipótesis: la predicción es puramente algorítmica.

**Nota sobre evidencia relacionada:** el modelo también identificó una indicación más amplia y estrechamente relacionada, "retinopatía diabética" (general, rank 2, puntaje 99.23%), para la cual sí existe evidencia indirecta:
- Un ensayo Fase 3 completado (NCT00925600, n=769) evaluó opacificación del cristalino en pacientes con cáncer de próstata bajo denosumab; la retinopatía diabética no fue su objetivo principal, por lo que su relevancia se calificó como baja (Grado C).
- Un estudio de cohorte de 2024 (PMID 38899553) encontró que denosumab, en pacientes tratados por osteoporosis, se asoció con menor incidencia de diabetes tipo 2 y de complicaciones microvasculares (incluyendo retinopatía) frente a bisfosfonatos.

Esta evidencia es epidemiológica e indirecta, no mecanística ni específica de la retinopatía severa, por lo que no cambia la recomendación para la indicación de rank 1, pero sugiere una dirección de investigación relacionada que podría explorarse en paralelo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para "retinopatía diabética no proliferativa severa".

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para "retinopatía diabética no proliferativa severa".

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se sustenta únicamente en el puntaje del modelo TxGNN (nivel de evidencia L5), sin ningún ensayo clínico ni publicación que la respalde directamente. Aunque existe evidencia epidemiológica indirecta para la categoría más amplia de "retinopatía diabética" (rank 2, nivel L4), esta no es suficiente para justificar avanzar con la indicación específica de rank 1.

**Para avanzar se necesita:**
- Datos de advertencias/contraindicaciones del prospecto (actualmente bloqueante — sin esto no puede iniciarse la evaluación de seguridad S1)
- Datos detallados del mecanismo de acción (MOA) de denosumab
- Estudios preclínicos o mecanísticos que evalúen específicamente el eje RANKL/RANK/OPG en tejido retiniano
- Evaluar si la señal epidemiológica de rank 2 (reducción de complicaciones microvasculares) justifica un estudio dirigido a la retinopatía no proliferativa severa
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

