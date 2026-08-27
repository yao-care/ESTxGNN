---
layout: default
title: Alfacalcidol
parent: 僅模型預測 (L5)
nav_order: 17
evidence_level: L5
indication_count: 5
---

# Alfacalcidol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

Usando conocimiento de dominio farmacológico estándar (no una skill específica, ya que se trata de redacción directa de un informe siguiendo la plantilla v5 proporcionada), genero el informe a partir del Evidence Pack.

Nota metodológica antes del informe: el Evidence Pack es un paquete "multi-indicación" (5 candidatos); siguiendo la regla del prompt de usar `predicted_indications[0]`, el informe se centra en el candidato de mayor puntuación TxGNN (*familial isolated hypoparathyroidism due to impaired PTH secretion*), que también es el que trae una justificación mecanística completa en el propio pack. Las secciones "Información de Mercado en España" y "Citotoxicidad" se omiten porque no hay datos de licencias en España (`licenses: []`) y porque alfacalcidol no es un fármaco antineoplásico/citotóxico.

---

# Alfacalcidol: De Hipoparatiroidismo y Trastornos del Metabolismo Óseo-Mineral a Hipoparatiroidismo Aislado Familiar por Secreción Deficiente de PTH

## Resumen en Una Frase

Alfacalcidol es un análogo activado de la vitamina D (1α-hidroxivitamina D3) utilizado tradicionalmente en trastornos del metabolismo del calcio y fósforo, como el hipoparatiroidismo y la osteodistrofia renal. El modelo TxGNN predice que podría ser especialmente relevante para el **hipoparatiroidismo aislado familiar por secreción deficiente de PTH**, un subtipo genético específico de esta misma familia de trastornos, pero actualmente **no existen ensayos clínicos ni publicaciones** que evalúen directamente esta indicación concreta.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastornos del metabolismo del calcio y fósforo (hipoparatiroidismo, osteodistrofia renal) — texto específico de indicación no disponible en este Evidence Pack |
| Nueva Indicación Predicha | Hipoparatiroidismo Aislado Familiar por Secreción Deficiente de PTH |
| Puntaje de Predicción TxGNN | 99.61% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados del mecanismo de acción (MOA) en este Evidence Pack (marcado como vacío de datos de alta severidad). Según la información farmacológica conocida, alfacalcidol es un profármaco análogo de la vitamina D que solo requiere hidroxilación hepática (25-hidroxilación) para activarse a calcitriol, evitando así el paso de 1α-hidroxilación renal — un paso que fisiológicamente depende del estímulo de la hormona paratiroidea (PTH).

La relación entre la indicación original y la nueva indicación predicha es directa: en el hipoparatiroidismo aislado familiar por secreción deficiente de PTH, el defecto reside precisamente en la falta de estímulo hormonal sobre la 1α-hidroxilasa renal, lo que impide convertir la 25(OH)D en calcitriol activo y provoca hipocalcemia. Como alfacalcidol ya está "pre-activado" en el paso 1α, puede sortear directamente este bloqueo enzimático sin depender de la PTH, lo que constituye una justificación mecanística sólida y biológicamente plausible.

Pese a esta coherencia mecanística, la búsqueda no encontró ensayos clínicos ni literatura que aborden específicamente esta indicación. Esto podría deberse a que el uso de análogos de vitamina D activada en el hipoparatiroidismo hereditario ya es una práctica clínica estándar y consolidada (por lo que no genera nuevos registros de investigación), más que a una ausencia real de utilidad clínica. Aun así, se trata de una hipótesis mecanística no confirmada por evidencia directa en este pack.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El razonamiento mecanístico es sólido y biológicamente plausible, pero no existe ningún ensayo clínico ni publicación específica identificada que respalde el uso de alfacalcidol en el hipoparatiroidismo aislado familiar por secreción deficiente de PTH. Además, el propio Evidence Pack señala un vacío de datos bloqueante en el prospecto oficial (TFDA), lo que impide completar la evaluación de seguridad inicial (S1).

**Para avanzar se necesita:**
- Obtener el prospecto oficial (TFDA package insert) para completar la evaluación de seguridad S1
- Datos de mecanismo de acción (MOA) verificados desde DrugBank u otra fuente primaria
- Búsqueda dirigida de series de casos, guías clínicas o consensos de expertos sobre el uso de análogos de vitamina D activada específicamente en hipoparatiroidismo hereditario/familiar
- Confirmación de si las indicaciones ya aprobadas de alfacalcidol en otros mercados (fuera de España) incluyen formas hereditarias de hipoparatiroidismo, como respaldo indirecto adicional
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

