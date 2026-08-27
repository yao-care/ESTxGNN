---
layout: default
title: Penciclovir
parent: 僅模型預測 (L5)
nav_order: 218
evidence_level: L5
indication_count: 1
---

# Penciclovir
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

# Penciclovir: De Infección por Herpesvirus (HSV/VZV) a Fascioliasis

## Resumen en Una Frase

Penciclovir es un análogo de guanosina utilizado como antiviral, cuyo mecanismo depende de la fosforilación por la timidina cinasa viral (HSV/VZV) para inhibir la ADN polimerasa viral.
El modelo TxGNN predice que podría ser efectivo para **Fascioliasis**,
pero actualmente **no existe ningún ensayo clínico ni publicación** que respalde esta dirección — se trata de una señal puramente predictiva.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | No especificada en el Evidence Pack (mecanismo descrito: antiviral frente a HSV/VZV) |
| Nueva Indicacion Predicha | Fascioliasis |
| Puntaje de Prediccion TxGNN | 99.06% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Espana | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Penciclovir actúa como análogo de nucleósido: tras ser fosforilado por la timidina cinasa de virus herpéticos (HSV/VZV), inhibe la ADN polimerasa viral y bloquea la replicación del virus. Este mecanismo es específico de la maquinaria de replicación viral.

La fascioliasis, en cambio, es una infección parasitaria causada por trematodos (*Fasciola hepatica/gigantica*), organismos multicelulares sin homología con la timidina cinasa ni la ADN polimerasa viral que constituyen el blanco de penciclovir. No existe una ruta metabólica conocida de estos parásitos que se solape con el mecanismo de acción del fármaco.

En consecuencia, la puntuación elevada de TxGNN (99.06%) refleja únicamente similitud de embeddings dentro del grafo de conocimiento, y no aporta plausibilidad biológica. Esta predicción debe interpretarse como una señal exploratoria de baja confianza, no como una hipótesis mecanísticamente fundamentada.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Informacion de Mercado en Espana

Penciclovir no cuenta actualmente con autorizaciones de comercialización registradas en los datos disponibles (0 licencias, estado "no comercializado").

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
No existe ningún ensayo clínico ni publicación que respalde la asociación penciclovir–fascioliasis, y el mecanismo de acción conocido del fármaco (inhibición de la replicación viral herpética) no tiene relación biológica plausible con una infección parasitaria por trematodos. La puntuación de TxGNN por sí sola es insuficiente para avanzar.

**Para avanzar se necesita:**
- Advertencias y contraindicaciones del prospecto de TFDA (brecha bloqueante identificada en el Evidence Pack — impide la evaluación inicial de seguridad S1)
- Confirmación del mecanismo de acción (MOA) vía DrugBank (brecha de alta prioridad)
- Evidencia preclínica que establezca un vínculo mecanístico real entre la vía antiviral y la biología del trematodo, de existir
- Cualquier estudio observacional o reporte de caso que surja en futuras búsquedas en ClinicalTrials.gov, ICTRP o PubMed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

