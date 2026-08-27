---
layout: default
title: Iloprost
parent: 僅模型預測 (L5)
nav_order: 140
evidence_level: L5
indication_count: 9
---

# Iloprost
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Iloprost: De Hipertensión Arterial Pulmonar a Hipotricosis Simple del Cuero Cabelludo

## Resumen en Una Frase

Iloprost es un análogo sintético de prostaciclina (PGI2), históricamente aprobado para el tratamiento de la hipertensión arterial pulmonar (HAP). El modelo TxGNN predice, con la puntuación más alta de este paquete de evidencia, que podría ser efectivo para **Hipotricosis Simple del Cuero Cabelludo**, pero actualmente **no existe ningún ensayo clínico ni publicación** que respalde esta dirección, y el propio análisis mecanístico la señala como probable falso positivo del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial pulmonar (HAP) — según se menciona en las justificaciones mecanísticas de este informe; sin ficha regulatoria propia disponible |
| Nueva Indicación Predicha | Hipotricosis simple del cuero cabelludo |
| Puntaje de Predicción TxGNN | 99.45% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de una ficha estructurada de mecanismo de acción (MOA) para iloprost en este informe. Según la información recogida en las justificaciones mecanísticas de las demás indicaciones de este mismo paquete de evidencia, iloprost es un análogo sintético de prostaciclina (PGI2) con efecto vasodilatador pulmonar y antiagregante plaquetario, ya aprobado para el tratamiento de la HAP.

Mecanísticamente no existe relación conocida entre este mecanismo (vasodilatación de músculo liso vascular y antiagregación plaquetaria) y las vías reguladoras del crecimiento folicular (p. ej. receptor de andrógenos, WNT/β-catenina). El propio informe señala explícitamente que la puntuación alta de TxGNN podría deberse a un falso positivo en el espacio de embeddings del grafo, posiblemente por proximidad con otros análogos de prostaglandina que sí tienen efecto documentado sobre el crecimiento capilar (como bimatoprost).

En consecuencia, esta predicción no cuenta con respaldo mecanístico sólido ni con ningún dato clínico o de literatura, lo que limita fuertemente su plausibilidad como candidato de reposicionamiento en esta etapa.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Pese a tener la puntuación TxGNN más alta del paquete, la indicación "hipotricosis simple del cuero cabelludo" no cuenta con ningún ensayo clínico ni publicación de respaldo, y el análisis mecanístico del propio informe la califica como probable falso positivo del modelo, sin conexión biológica plausible con el mecanismo conocido de iloprost.

**Para avanzar se necesita:**
- Ficha de mecanismo de acción (MOA) verificada de DrugBank
- Advertencias/contraindicaciones del prospecto (TFDA/AEMPS) — actualmente bloqueante para cualquier evaluación de seguridad
- Evidencia preclínica específica que vincule prostaciclinas con la vía de crecimiento folicular, si se desea sostener esta hipótesis

**Nota sobre otras indicaciones del mismo paquete de evidencia:**
Este paquete incluye otras indicaciones predichas para iloprost con evidencia sustancialmente más sólida, todas dentro del espectro de hipertensión arterial pulmonar (HAP), que es la indicación ya aprobada del fármaco:

- **HAP asociada a infección por VIH** (rank 6): Nivel L1, un ensayo Fase 3 completado, doblemente ciego y controlado con placebo (NCT00709956, n=64), más 4 publicaciones. Recomendación: **Proceed with Guardrails**.
- **HAP asociada a enfermedad del tejido conectivo** (rank 8): Nivel L3, 20 publicaciones incluyendo cohortes de uso de iloprost intravenoso domiciliario. Recomendación: **Research Question**.
- **HAP asociada a cardiopatía congénita** (rank 3): Nivel L3, un ensayo clínico y 20 publicaciones. Recomendación: **Research Question**.

Dado que estas indicaciones comparten el mecanismo ya aprobado de iloprost (vasodilatación pulmonar en HAP Grupo 1 de la OMS) y cuentan con evidencia real, se recomienda priorizar su evaluación sobre la indicación de rank 1 aquí reportada.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

