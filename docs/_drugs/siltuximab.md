---
layout: default
title: Siltuximab
parent: 僅模型預測 (L5)
nav_order: 257
evidence_level: L5
indication_count: 8
---

# Siltuximab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Siltuximab: De Enfermedad de Castleman Multicentrica a Mastocitoma Extracutaneo

## Resumen en Una Frase

Siltuximab es un anticuerpo monoclonal quimerico anti-IL-6, utilizado originalmente para la enfermedad de Castleman multicentrica (MCD) HHV-8 negativa. El modelo TxGNN predice que podria ser efectivo para **Mastocitoma Extracutaneo**, con una puntuacion de prediccion de 99.64%, pero **sin ningun ensayo clinico ni publicacion** que respalde actualmente esta direccion — se trata unicamente de una prediccion del modelo.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Enfermedad de Castleman Multicentrica (MCD) HHV-8 negativa (no consta autorizacion en Espana) |
| Nueva Indicacion Predicha | Mastocitoma Extracutaneo |
| Puntaje de Prediccion TxGNN | 99.64% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Espana | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion de siltuximab en las fuentes consultadas (DrugBank/TFDA). Segun la informacion contextual disponible en este mismo paquete de evidencia, siltuximab es un anticuerpo monoclonal quimerico dirigido contra la interleucina-6 (IL-6), cuya eficacia en la enfermedad de Castleman multicentrica ha sido comprobada clinicamente.

Sin embargo, para la indicacion de mayor puntuacion en este analisis — el mastocitoma extracutaneo — el propio racional mecanistico generado indica que esta neoplasia esta impulsada principalmente por mutaciones en KIT, y que la via de IL-6 no constituye una ruta patogenica central. La relacion mecanistica se considera debil, y no existe respaldo de ensayos clinicos ni de literatura: la asociacion proviene exclusivamente de la puntuacion del modelo TxGNN.

En contraste, dentro del mismo conjunto de indicaciones predichas para siltuximab, candidatos como el sarcoma de Kaposi (rank 5, nivel de evidencia L4) presentan una justificacion mecanistica mas solida (ambas patologias asociadas al virus HHV-8/KSHV) y cuentan con literatura de respaldo, aunque no son el foco de este informe por no ocupar la primera posicion del ranking.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
Pese a la alta puntuacion de TxGNN (99.64%), el mastocitoma extracutaneo carece de cualquier evidencia clinica o de literatura, y el propio racional mecanistico interno califica la asociacion con IL-6 como debil frente al driver conocido (mutacion KIT). Ademas, siltuximab no esta comercializado en Espana y faltan datos criticos de seguridad (advertencias TFDA/AEMPS, contraindicaciones) y de mecanismo de accion.

**Para avanzar se necesita:**
- Advertencias y contraindicaciones oficiales del prospecto (TFDA/AEMPS) — actualmente bloqueante para cualquier evaluacion de seguridad (S1)
- Datos verificados del mecanismo de accion (MOA) desde DrugBank u otra fuente primaria
- Evidencia preclinica o clinica especifica que vincule la via IL-6 con el mastocitoma extracutaneo, dado que el driver dominante conocido es KIT
- Considerar priorizar, dentro del mismo pool de predicciones, indicaciones con mayor nivel de evidencia como el sarcoma de Kaposi (L4), que ya cuenta con literatura de respaldo por la relacion HHV-8/KSHV
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

