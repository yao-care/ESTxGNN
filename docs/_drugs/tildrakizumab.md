---
layout: default
title: Tildrakizumab
parent: 僅模型預測 (L5)
nav_order: 276
evidence_level: L5
indication_count: 4
---

# Tildrakizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Tildrakizumab: De Psoriasis en Placas a Retinopatia Diabetica No Proliferativa Severa

## Resumen en Una Frase

Tildrakizumab es un anticuerpo monoclonal anti-IL-23p19, utilizado originalmente para el tratamiento de la psoriasis en placas.
El modelo TxGNN predice que podria ser efectivo para **Retinopatia Diabetica No Proliferativa Severa**,
pero actualmente **no existe ningun ensayo clinico ni publicacion** que respalde esta direccion; la prediccion se basa unicamente en la conectividad del grafo de conocimiento.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Psoriasis en placas (segun informacion conocida del farmaco; no confirmado por licencias regulatorias en Espana, ya que no esta comercializado) |
| Nueva Indicacion Predicha | Retinopatia Diabetica No Proliferativa Severa |
| Puntaje de Prediccion TxGNN | 99.63% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Espana | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion (MOA) de tildrakizumab en esta base de evidencia. Segun la informacion conocida del farmaco, tildrakizumab es un anticuerpo monoclonal que bloquea especificamente la subunidad p19 de la interleucina-23 (IL-23), interrumpiendo el eje inflamatorio IL-23/Th17. Su eficacia en psoriasis en placas moderada a grave esta bien establecida.

La retinopatia diabetica no proliferativa severa es una complicacion microvascular cuya patologia se relaciona principalmente con hiperglucemia cronica, estres oxidativo y vias de VEGF. Existe literatura que sugiere una posible participacion del eje IL-23/Th17 en procesos inflamatorios retinianos, pero esta relacion es indirecta y no constituye un mecanismo farmacologico validado.

Por lo tanto, la puntuacion elevada de TxGNN (99.63%) refleja unicamente la fuerza de conexion dentro del grafo de conocimiento, no evidencia biologica o clinica confirmada. La ausencia total de ensayos clinicos y publicaciones, junto con la falta de datos de MOA propios del farmaco, limita considerablemente la solidez de esta hipotesis de reposicionamiento.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad. (Tildrakizumab no esta comercializado en Espana, por lo que no existe ficha tecnica local disponible; se recomienda consultar la informacion del fabricante o la EMA cuando este disponible.)

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La evidencia disponible corresponde unicamente al nivel L5 (prediccion del modelo sin ningun estudio real que la respalde). No existen ensayos clinicos ni literatura para esta indicacion, el farmaco no esta comercializado en Espana, y faltan datos criticos de seguridad (advertencias, contraindicaciones) y de mecanismo de accion.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha tecnica oficial (TFDA/EMA) con advertencias y contraindicaciones (brecha bloqueante DG001)
- Completar los datos de mecanismo de accion mediante consulta a DrugBank (brecha DG002)
- Identificar estudios preclinicos o de mecanismo que vinculen la via IL-23/Th17 con la patologia retiniana diabetica antes de considerar cualquier avance
- Monitorear registros de ensayos clinicos (ClinicalTrials.gov, ICTRP) y PubMed para deteccion temprana de nueva evidencia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

