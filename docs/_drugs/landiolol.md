---
layout: default
title: Landiolol
parent: 僅模型預測 (L5)
nav_order: 157
evidence_level: L5
indication_count: 6
---

# Landiolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Landiolol: De Control Agudo de Arritmias Cardíacas a Discinesia Linguofacial-Bucal

## Resumen en Una Frase

Landiolol es un betabloqueante β1-selectivo de acción ultracorta (vida media ~4 minutos), administrado por vía intravenosa para el control agudo de la frecuencia cardíaca en entornos hospitalarios (UCI/quirófano).
El modelo TxGNN predice que podría ser efectivo para **Discinesia Linguofacial-Bucal**, con una puntuación de **99,11%**,
pero actualmente **no existen ensayos clínicos ni publicaciones** que respalden esta dirección — la evidencia es puramente computacional.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en el Evidence Pack actual (brecha de datos registrada, ver sección MOA) |
| Nueva Indicación Predicha | Discinesia Linguofacial-Bucal |
| Puntaje de Predicción TxGNN | 99,11% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de landiolol en el Evidence Pack (brecha de datos de alta severidad). Según la información disponible en las justificaciones mecanísticas asociadas a esta predicción, landiolol es un betabloqueante β1-selectivo de acción ultracorta, utilizado por vía intravenosa exclusivamente para el control agudo del ritmo/frecuencia cardíaca en contextos de cuidados intensivos o quirúrgicos.

La relación entre este uso original y la discinesia linguofacial-bucal es débil. La propia justificación mecanística generada para esta predicción indica que la fisiopatología de este tipo de discinesia (tardía u orofacial) se asocia principalmente con hipersensibilidad de receptores dopaminérgicos o con la vía GABA, sin una conexión directa conocida con el bloqueo adrenérgico β1-selectivo. Solo existe una inferencia indirecta muy débil: que los trastornos del movimiento a veces cursan con síntomas autonómicos concomitantes.

En consecuencia, esta predicción debe interpretarse como una señal exploratoria generada por similitud de red en TxGNN, sin respaldo mecanístico sólido ni evidencia clínica o preclínica que la sustente en este momento.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Informacion de Mercado en Espana

Landiolol no está comercializado actualmente en España (0 autorizaciones registradas), por lo que no se dispone de información de productos ni indicaciones aprobadas localmente.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. (No se encontraron datos de advertencias, contraindicaciones ni interacciones farmacológicas en las fuentes consultadas; la búsqueda de DDI no arrojó resultados.)

## Conclusion y Proximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en la puntuación del modelo TxGNN (L5), sin ningún ensayo clínico ni publicación de respaldo, y la propia justificación mecanística generada reconoce que la conexión farmacológica entre landiolol y la discinesia linguofacial-bucal es indirecta y débil. No existe base suficiente para avanzar a evaluación de seguridad.

**Para avanzar se necesita:**
- Datos del prospecto/ficha técnica de TFDA (advertencias y contraindicaciones) — brecha bloqueante (DG001)
- Datos del mecanismo de acción (MOA) desde DrugBank — brecha de alta severidad (DG002)
- Búsqueda ampliada de literatura preclínica o de mecanismo que conecte el bloqueo β1 con discinesias orofaciales
- Nota: entre los seis candidatos evaluados, "primary orthostatic tremor" (rank 6) presenta una justificación farmacológica algo más plausible (los betabloqueantes no selectivos son tratamiento estándar en temblores), aunque también carece de evidencia clínica directa para landiolol y mantiene recomendación Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

