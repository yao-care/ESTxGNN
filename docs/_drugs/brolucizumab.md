---
layout: default
title: Brolucizumab
parent: 僅模型預測 (L5)
nav_order: 47
evidence_level: L5
indication_count: 4
---

# Brolucizumab
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

# Brolucizumab: De Indicación Oftalmológica (Inhibidor de VEGF-A) a Trastorno Mitocondrial de la Fosforilación Oxidativa

## Resumen en Una Frase

Brolucizumab es un fragmento de anticuerpo anti-VEGF-A administrado por inyección intravítrea, utilizado originalmente en indicaciones oftalmológicas.
El modelo TxGNN predice que podría ser efectivo para **trastorno mitocondrial de la fosforilación oxidativa por anomalías del ADN nuclear**,
pero actualmente **no existe ningún ensayo clínico ni publicación** que respalde esta dirección, y el propio análisis de racionalidad mecanística del paquete de evidencia concluye que no hay conexión fisiopatológica plausible.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Indicación oftalmológica, inhibidor de VEGF-A administrado por inyección intravítrea (texto exacto de indicación no registrado en la fuente) |
| Nueva Indicación Predicha | Trastorno mitocondrial de la fosforilación oxidativa por anomalías del ADN nuclear |
| Puntaje de Predicción TxGNN | 99.67% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción específico en esta fuente (dato marcado como brecha de alta prioridad). Según la información disponible en el paquete de evidencia, brolucizumab es un fragmento de anticuerpo de cadena única que inhibe VEGF-A, aprobado exclusivamente para inyección intravítrea en indicaciones oftalmológicas.

Para la indicación de mayor puntaje predicho por TxGNN —trastorno mitocondrial de la fosforilación oxidativa por anomalías del ADN nuclear— el propio análisis de racionalidad mecanística incluido en el paquete de evidencia concluye que **no existe una conexión mecanística razonable**: la inhibición de VEGF-A y la angiogénesis no tiene un vínculo fisiopatológico conocido con los defectos de la cadena respiratoria mitocondrial derivados de mutaciones del ADN nuclear. Se trata de una predicción con puntaje alto del modelo pero sin respaldo mecanístico ni evidencia clínica o de literatura.

Cabe destacar que las indicaciones de rango 2 y 3 del mismo lote (varices esofágicas con y sin sangrado, puntaje ~99.12%) presentan al menos una hipótesis mecanística teórica —la angiogénesis esplácnica dependiente de VEGF en la hipertensión portal—, pero tampoco cuentan con ensayos clínicos, literatura, ni datos de seguridad en población con cirrosis/hipertensión portal que la respalden, y brolucizumab nunca ha sido evaluado por vía sistémica. La cuarta indicación (insuficiencia pancreática exocrina) también carece de vínculo mecanístico razonable según el mismo análisis.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Las cuatro indicaciones predichas se encuentran en Nivel de Evidencia L5 (solo predicción del modelo, sin ensayos clínicos ni literatura), y la indicación de mayor puntaje carece de plausibilidad mecanística según el propio análisis del paquete de evidencia. Además, el fármaco no está comercializado en España y falta información crítica de seguridad (advertencias/contraindicaciones de ficha técnica, marcada como brecha bloqueante).

**Para avanzar se necesita:**
- Ficha técnica/prospecto de la AEMPS con advertencias y contraindicaciones (brecha bloqueante DG001)
- Datos detallados del mecanismo de acción (DG002)
- Indicación(es) originales aprobadas documentadas formalmente (actualmente ausentes en la fuente)
- Evidencia clínica o preclínica real que sustente un vínculo fisiopatológico, especialmente para varices esofágicas (rango 2-3), antes de considerar cualquier avance
- Reevaluar si la indicación de rango 1 debe descartarse dado que el propio análisis mecanístico la contradice
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

