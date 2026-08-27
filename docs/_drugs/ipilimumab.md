---
layout: default
title: Ipilimumab
parent: 僅模型預測 (L5)
nav_order: 153
evidence_level: L5
indication_count: 2
---

# Ipilimumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Ipilimumab: De Melanoma Cutáneo a Melanoma No Cutáneo

## Resumen en Una Frase

Ipilimumab es un anticuerpo monoclonal anti-CTLA-4 cuyo uso establecido, según el contexto de la literatura recopilada, es el melanoma cutáneo avanzado. El modelo TxGNN predice que podría ser efectivo también para **Melanoma No Cutáneo** (subtipos mucoso y uveal), con **50 ensayos clínicos** y **5 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en fichas de licencia (fármaco no comercializado en España); el contexto de la literatura señala melanoma cutáneo avanzado como uso establecido |
| Nueva Indicación Predicha | Melanoma No Cutáneo (mucoso/uveal) |
| Puntaje de Predicción TxGNN | 99.02% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

No se dispone de una ficha detallada de mecanismo de acción en este paquete de evidencia (dato pendiente de DrugBank). Sin embargo, la evidencia recopilada en ensayos y literatura confirma que ipilimumab es un anticuerpo monoclonal anti-CTLA-4: bloquea una señal inhibidora de los linfocitos T, liberando así una respuesta inmunitaria capaz de atacar el tumor (inhibidor de punto de control inmunitario).

Este mecanismo de acción no está restringido a un tejido de origen específico dentro del linaje melanocítico, por lo que es mecanísticamente plausible extender su uso del melanoma cutáneo a otros subtipos de melanoma (mucoso, uveal), que comparten el origen en melanocitos aunque difieran en localización anatómica y comportamiento biológico.

Existe, no obstante, una salvedad importante documentada en la propia evidencia: el melanoma uveal es conocido por presentar tasas de respuesta significativamente más bajas a los inhibidores de puntos de control inmunitario que el melanoma cutáneo, probablemente por el entorno inmunoprivilegiado del ojo y una menor carga mutacional tumoral. Esto matiza la fuerza de la predicción para ese subtipo en particular.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02506153](https://clinicaltrials.gov/study/NCT02506153) | Fase 3 | Activo, no reclutando | 1301 | Ensayo pivotal E1609: comparación de interferón en alta dosis o ipilimumab frente a pembrolizumab en melanoma resecado de alto riesgo (adyuvante) |
| [NCT02115139](https://clinicaltrials.gov/study/NCT02115139) | Fase 2 | Completado | 58 | Ipilimumab combinado con radioterapia aporta beneficio clínico en melanoma con metástasis cerebrales |
| [NCT03165422](https://clinicaltrials.gov/study/NCT03165422) | N/A | Completado | 68 | Estudio real-world en Japón: uso de ipilimumab tras nivolumab en melanoma, refleja práctica clínica habitual |
| [NCT06240143](https://clinicaltrials.gov/study/NCT06240143) | Fase 1b/2 | Reclutando | 96 | Ipilimumab + nivolumab neoadyuvante intradérmico en melanoma estadio II de alto riesgo; sin resultados aún |
| [NCT01689974](https://clinicaltrials.gov/study/NCT01689974) | Fase 2 | Terminado | 10 | ECA de ipilimumab ± radioterapia en melanoma metastásico; muestra pequeña, terminado prematuramente |
| [NCT03369223](https://clinicaltrials.gov/study/NCT03369223) | Fase 1/2 | Completado | 356 | BMS-986249 solo o con nivolumab en tumores sólidos avanzados; no específico de melanoma |
| [NCT04021420](https://clinicaltrials.gov/study/NCT04021420) | Fase 1/2 | Desconocido | 21 | Apertura de barrera hematoencefálica (dispositivo SonoCloud) con nivolumab ± ipilimumab en metástasis cerebrales de melanoma |
| [NCT06880198](https://clinicaltrials.gov/study/NCT06880198) | N/A | Reclutando | 20 | Estudio de soporte nutricional junto a terapia anti-PD1 ± ipilimumab; no evalúa eficacia directa del fármaco |
| [NCT02210104](https://clinicaltrials.gov/study/NCT02210104) | Fase 1 | Retirado | 0 | Terapia celular adoptiva con células T CD4+ anti-CTLA4; sin datos disponibles (retirado, inscripción 0) |
| [NCT00324155](https://clinicaltrials.gov/study/NCT00324155) | Fase 3 | Completado | 681 | Ensayo histórico dacarbazina + ipilimumab vs. dacarbazina + placebo en melanoma avanzado; base de la aprobación original del fármaco |

*Nota: la gran mayoría de los 50 ensayos identificados corresponden a melanoma en general (no específicamente subtipos no cutáneos); pocos abordan directamente melanoma mucoso o uveal.*

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [24999899](https://pubmed.ncbi.nlm.nih.gov/24999899/) | 2014 | Cohorte/Acceso ampliado | Med J Aust | Eficacia y tolerabilidad de ipilimumab en pacientes pretratados con melanoma cutáneo, uveal y mucoso; evalúa respuesta por subtipo |
| [28183255](https://pubmed.ncbi.nlm.nih.gov/28183255/) | 2018 | Revisión | Curr Cancer Drug Targets | Revisión del tratamiento adyuvante del melanoma; señala que solo el 5% son melanomas no cutáneos |
| [29466692](https://pubmed.ncbi.nlm.nih.gov/29466692/) | 2018 | Revisión | Discov Med | Actualización clínica de anticuerpos anti-PD-1 solos o combinados con ipilimumab en melanoma avanzado |
| [37887546](https://pubmed.ncbi.nlm.nih.gov/37887546/) | 2023 | Cohorte | Curr Oncol | Comparación de eficacia de anti-PD-1 ± ipilimumab entre pacientes jóvenes y mayores con melanoma avanzado |
| [40236344](https://pubmed.ncbi.nlm.nih.gov/40236344/) | 2025 | Reporte de caso | Cureus | Caso de metástasis de melanoma en colon transverso; describe riesgo de eventos adversos gastrointestinales graves con inmunoterapia |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (inhibidor de punto de control inmunitario anti-CTLA-4) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

**Nota crítica:** este paquete de evidencia marca la obtención del prospecto/advertencias de TFDA como un vacío de datos de severidad **Bloqueante (DG001)** — impide actualmente completar la evaluación preliminar de seguridad (S1). No se dispone tampoco de datos de interacciones farmacológicas (DDI: no encontrado).

---

## Nota: Otra Indicación Predicha de Baja Confianza

El mismo modelo también asignó una puntuación alta (99.06%) a **Choroideremia**, una enfermedad retiniana hereditaria sin relación mecanística conocida con el bloqueo de CTLA-4. Sin ensayos ni literatura de respaldo (L5, etapa S0), la propia evidencia recomienda **Hold** para esta señal — se incluye aquí solo para transparencia, no requiere acción.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El mecanismo de acción (bloqueo de CTLA-4) es plausible para extender el uso más allá del melanoma cutáneo, y existe un volumen considerable de ensayos (incluyendo un Fase 3 pivotal, n=1301) y literatura que aborda directamente subtipos mucoso y uveal. Sin embargo, la mayoría de los ensayos no son específicos del subtipo no cutáneo, y el melanoma uveal tiene una respuesta históricamente menor a esta clase de fármacos.

**Para avanzar se necesita:**
- Obtener el prospecto/advertencias de TFDA (DG001, bloqueante) antes de cualquier evaluación de seguridad
- Completar los datos de mecanismo de acción vía DrugBank (DG002)
- Priorizar ensayos y literatura específicos de melanoma mucoso/uveal (no solo melanoma general)
- Confirmar compatibilidad de vías de administración (actualmente marcada como pendiente)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

