---
layout: default
title: Salbutamol
parent: 僅模型預測 (L5)
nav_order: 251
evidence_level: L5
indication_count: 10
---

# Salbutamol
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

# Salbutamol: De Broncoespasmo/Asma-EPOC a Conjuntivitis Papilar

## Resumen en Una Frase

Salbutamol es un agonista beta2-adrenérgico de acción corta, conocido clínicamente como broncodilatador de referencia en asma y enfermedad pulmonar obstructiva crónica (EPOC), aunque el texto oficial de indicación aprobada no está disponible en este paquete de evidencia (brecha de datos).
El modelo TxGNN predice que podría ser efectivo para **Conjuntivitis Papilar**, pero actualmente **0 ensayos clínicos** y **0 publicaciones** respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dato no disponible en el paquete de evidencia (brecha de datos); salbutamol es clínicamente conocido como broncodilatador para asma/EPOC |
| Nueva Indicación Predicha | Conjuntivitis Papilar (papillary conjunctivitis) |
| Puntaje de Predicción TxGNN | 99.9964% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, salbutamol es un agonista beta2-adrenérgico de acción corta, cuya eficacia como broncodilatador en asma y EPOC está ampliamente comprobada; mecanísticamente actúa sobre el músculo liso bronquial y, de forma sistémica, sobre la vía aérea.

La conjuntivitis papilar es, en la mayoría de los casos, una reacción mecánica o alérgica de contacto (asociada típicamente al uso de lentes de contacto o exposición a alérgenos), un mecanismo fisiopatológico distinto al de la broncoconstricción. El propio análisis de la evidencia señala que, aunque la puntuación de TxGNN es extremadamente alta, no existe evidencia mecanicista directa que respalde una acción antiinflamatoria local de salbutamol sobre la conjuntiva capaz de tratar este cuadro.

En consecuencia, esta predicción se interpreta como una señal algorítmica de alta confianza sin correlato clínico o preclínico verificable hasta el momento.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La puntuación de TxGNN es muy alta, pero no existe ningún ensayo clínico ni publicación que respalde la Conjuntivitis Papilar como indicación, y el mecanismo propuesto no es consistente con la fisiopatología conocida de esta condición. No se recomienda avanzar sin evidencia adicional.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) de salbutamol — actualmente marcado como brecha de datos de severidad Alta (DG002), pendiente de consulta en DrugBank
- Advertencias/contraindicaciones del prospecto TFDA — brecha de datos de severidad **Bloqueante** (DG001), impide la evaluación de seguridad S1
- Confirmación del texto de indicación original aprobada (no disponible en licencias/registro), dado que el campo `original_indications` está vacío
- Búsqueda dirigida de estudios preclínicos o series de casos que evalúen agonistas beta2 tópicos/oftálmicos en conjuntivitis alérgica o papilar, antes de reconsiderar esta candidatura
- Nota: el mismo paquete de evidencia contiene otros candidatos de salbutamol con evidencia sustancialmente más fuerte (p. ej. "obstructive lung disease" con nivel L1 y "bronchitis" con nivel L2), que en realidad corresponden a indicaciones ya establecidas del fármaco y no a reposicionamientos nuevos; se recomienda corregir `original_indications` en la base de datos en lugar de tratarlos como hallazgos de repurposing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

