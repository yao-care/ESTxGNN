---
layout: default
title: Fedratinib
parent: 僅模型預測 (L5)
nav_order: 119
evidence_level: L5
indication_count: 10
---

# Fedratinib
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

# Fedratinib: De Indicación Original No Especificada a PEComa Benigno

## Resumen en Una Frase

Los datos disponibles en este informe no incluyen la indicación original aprobada de fedratinib (brecha de datos pendiente). Según las justificaciones mecanísticas incluidas en este análisis, fedratinib actúa como inhibidor de JAK2/FLT3. El modelo TxGNN predice que podría ser efectivo para **PEComa Benigno**, con una puntuación del **99.84%**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, y el propio análisis mecanístico incluido en los datos no encuentra relación causal entre el mecanismo del fármaco y la enfermedad.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en este informe (brecha de datos, ver DG001/DG002) |
| Nueva Indicación Predicha | PEComa Benigno (benign PEComa) |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados sobre el mecanismo de acción original de fedratinib en este informe (brecha de datos de prioridad alta, DG002, pendiente de consulta directa en DrugBank). A partir de las justificaciones mecanísticas incluidas en el conjunto de datos, fedratinib se describe consistentemente como un inhibidor de **JAK2/FLT3**.

El PEComa Benigno, según el propio análisis incluido en los datos, está impulsado principalmente por mutaciones en **TSC1/TSC2** que activan de forma excesiva la vía **mTOR**, siendo los inhibidores de mTOR el abordaje terapéutico estándar. No existe intersección conocida entre esta vía y el mecanismo JAK2/FLT3 de fedratinib.

En consecuencia, el propio dato de origen (`repurposing_rationale.mechanistic_link`) concluye explícitamente que esta predicción **no tiene una base teórica sustancial**: se trata de una asociación estadística del modelo TxGNN sin respaldo mecanístico, clínico ni bibliográfico.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia es de nivel L5 (solo predicción del modelo, sin estudios reales), no existen ensayos clínicos ni literatura de respaldo, y el propio análisis mecanístico contenido en los datos indica que no hay relación plausible entre el mecanismo JAK2/FLT3 de fedratinib y la fisiopatología TSC1/TSC2-mTOR del PEComa Benigno. No hay base suficiente para avanzar esta indicación en este momento.

**Para avanzar se necesita:**
- Confirmar el mecanismo de acción original de fedratinib mediante consulta directa a DrugBank (DG002)
- Obtener la indicación original aprobada y el prospecto oficial (TFDA/AEMPS) para completar la evaluación de seguridad S1 (DG001, bloqueante)
- Generar evidencia preclínica específica que justifique una relación mecanística antes de reconsiderar esta candidatura

---

### Nota: Otros candidatos en este Evidence Pack

Este paquete de evidencia incluye 10 indicaciones predichas para fedratinib. La mayoría (rangos 1-7 y 10) presentan el mismo patrón: L5, sin ensayos ni literatura, y mecanismos explícitamente descritos como no relacionados (vías mTOR/TSC, PDGFRB, SMARCB1/EZH2, inflamasoma/IL-1β).

Los candidatos en rango 8 y 9 (linfohistiocitosis hemofagocítica asociada a enfermedad maligna / a infección) destacan por tener un nivel de evidencia superior (**L4, etapa S1, "Research Question"**), ya que la tormenta de citocinas de la HLH depende de la vía JAK-STAT, y el inhibidor de clase relacionada ruxolitinib ya cuenta con series de casos en HLH refractaria. No obstante, no existe evidencia directa de fedratinib en estas indicaciones — es una extrapolación de efecto de clase, no evidencia propia del fármaco. Si se desea profundizar en este programa de reposicionamiento, estos dos candidatos representan la dirección con mayor plausibilidad mecanística dentro de este conjunto.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

