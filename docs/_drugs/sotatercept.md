---
layout: default
title: Sotatercept
parent: 僅模型預測 (L5)
nav_order: 265
evidence_level: L5
indication_count: 10
---

# Sotatercept
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

# Sotatercept: Hacia Leucemia Linfoblástica Aguda (Indicación Original No Documentada)

## Resumen en Una Frase

El Evidence Pack no contiene datos verificados sobre la indicación original ni el mecanismo de acción de sotatercept (ambos marcados como brecha de datos). El modelo TxGNN predice que podría ser efectivo para **Leucemia Linfoblástica Aguda**, con un puntaje de **99.78%**, pero **0 ensayos clínicos** y **0 publicaciones** respaldan actualmente esta dirección — es una predicción puramente algorítmica, y el propio análisis mecanístico del pack la señala como posible ruido de baja relevancia.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible — sin licencias registradas en Taiwán ni indicación original documentada en este Evidence Pack |
| Nueva Indicación Predicha | Leucemia Linfoblástica Aguda |
| Puntaje de Predicción TxGNN | 99.78% (rank global #4300) |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Taiwán | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción original de sotatercept ni sobre su indicación aprobada (brecha de datos de alta prioridad, pendiente de resolver vía DrugBank API). Esto impide comparar formalmente la indicación original con la nueva indicación predicha.

No obstante, el análisis mecanístico incluido en las fichas de predicción del propio pack indica que sotatercept es una proteína de fusión del receptor de activina tipo IIA (ActRIIA-Fc), que inhibe señales de ligandos de la familia activina/GDF/BMP — el mismo mecanismo de moléculas relacionadas como luspatercept.

Para Leucemia Linfoblástica Aguda específicamente, la justificación mecanística incluida en el pack es débil: se reconoce que la vía de activina se relaciona con el microambiente medular de algunas neoplasias hematológicas, pero **no existe una cadena de evidencia directa**, y el propio análisis califica esta predicción como "ruido de baja relevancia". En contraste, otras indicaciones predichas en el mismo lote (p. ej., osteoporosis inducida por fármacos, rank 4) muestran una relación mecanística teóricamente más sólida con la vía activina/BMP en metabolismo óseo, aunque tampoco cuentan con evidencia clínica o de literatura que las respalde.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Taiwán

Sotatercept no cuenta actualmente con ninguna autorización de comercialización registrada en Taiwán (0 licencias). El estado de mercado reportado es **"No comercializado"**.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación predicha de mayor puntaje (Leucemia Linfoblástica Aguda) carece por completo de respaldo clínico o bibliográfico, y el propio análisis mecanístico del pack la clasifica como probable ruido de predicción sin cadena causal directa. Adicionalmente, existe una brecha de datos de severidad **Bloqueante** (DG001: advertencias/contraindicaciones TFDA) que impide formalmente que el candidato avance a la etapa S1 de evaluación de seguridad.

**Para avanzar se necesita:**
- Resolver DG001 (Bloqueante): obtener advertencias, contraindicaciones y prospecto oficial de TFDA — requisito previo para cualquier evaluación de seguridad (S1)
- Resolver DG002 (Alta): datos de mecanismo de acción vía API de DrugBank, para poder evaluar formalmente la plausibilidad mecanística
- Generar o localizar evidencia clínica/preclínica real (ensayos o literatura) para al menos una de las 10 indicaciones predichas; actualmente todas están en nivel L5
- Si se prioriza una indicación alternativa, considerar rank 4 (osteoporosis inducida por fármacos), cuya relación mecanística con la vía activina/BMP es teóricamente más consistente que la de leucemia linfoblástica aguda
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

