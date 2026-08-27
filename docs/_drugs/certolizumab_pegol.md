---
layout: default
title: Certolizumab Pegol
parent: 僅模型預測 (L5)
nav_order: 67
evidence_level: L5
indication_count: 6
---

# Certolizumab Pegol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Certolizumab Pegol: De Enfermedades Inflamatorias Autoinmunitarias a Vasculitis Reumatoide

## Resumen en Una Frase

Certolizumab pegol es un fragmento Fab' PEGilado anti-TNF-α, utilizado en la práctica clínica internacional para enfermedades inflamatorias autoinmunitarias como la artritis reumatoide, la artritis psoriásica, la espondiloartritis axial y la enfermedad de Crohn.
El modelo TxGNN predice que podría ser efectivo para **Vasculitis Reumatoide**, con un puntaje de **99.78%**,
pero la evidencia disponible (**3 ensayos clínicos indirectos** y **8 publicaciones**, mayoritariamente reportes de caso) apunta en sentido contrario: certolizumab aparece con más frecuencia como **causa** de vasculitis que como tratamiento de ella.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedades inflamatorias autoinmunitarias (artritis reumatoide, artritis psoriásica, espondiloartritis axial, enfermedad de Crohn), según literatura de la clase de inhibidores de TNF-α — sin autorización de comercialización registrada actualmente |
| Nueva Indicación Predicha | Vasculitis Reumatoide |
| Puntaje de Predicción TxGNN | 99.78% (rank 4233) |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

No se dispone de datos estructurados de mecanismo de acción (MOA) en la base de datos consultada (DrugBank). Según la literatura incluida en este informe, certolizumab pegol es un fragmento Fab' antigénico PEGilado que neutraliza selectivamente el TNF-α, sin la porción Fc del anticuerpo (PMID 27704400, PMID 18155297). Esta clase de fármacos ha demostrado eficacia bien establecida en enfermedades inflamatorias mediadas por TNF-α.

Desde el punto de vista mecanístico, la hipótesis de TxGNN es plausible en teoría: la vasculitis asociada a artritis reumatoide comparte vías inflamatorias mediadas por TNF-α con la enfermedad articular de base, por lo que un bloqueador de TNF-α podría, en principio, suprimir la inflamación vascular.

Sin embargo, la literatura real recuperada contradice mayoritariamente esta hipótesis: de las 8 publicaciones identificadas, solo 1 reporte de caso describe el uso de certolizumab como **tratamiento** de vasculitis (úlceras en piernas por vasculitis reumatoide), mientras que 4 reportes de caso documentan que certolizumab **indujo** distintos tipos de vasculitis (vasculitis leucocitoclástica, vasculitis urticarial hipocomplementémica, vasculitis de vaso mediano, glomerulonefritis rápidamente progresiva) como reacción adversa paradójica. Este es un patrón reconocido de los anti-TNF: la señal de seguridad es actualmente más fuerte que la señal de eficacia.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Fase 2 | Aún no reclutando | 80 | Manejo perioperatorio de inmunosupresores en artroplastia de hombro; sin relación directa con vasculitis |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Desconocido | 750,000 | Registro de riesgo de enfermedades inflamatorias inmunomediadas (IMID); no es un ensayo de eficacia |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completado | 184 | Estudio observacional de tocilizumab (no certolizumab) en artritis reumatoide |

**Ninguno de los ensayos identificados evalúa directamente certolizumab pegol en vasculitis reumatoide.**

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36418084](https://pubmed.ncbi.nlm.nih.gov/36418084/) | 2022 | Revisión | RMD open | Análisis comparativo del perfil de infecciones de fármacos inmunomoduladores según ficha técnica |
| [36597972](https://pubmed.ncbi.nlm.nih.gov/36597972/) | 2022 | Cohorte | RMD open | Seguimiento a largo plazo de certolizumab en uveítis por enfermedad inmunomediada (indicación distinta) |
| [29610119](https://pubmed.ncbi.nlm.nih.gov/29610119/) | 2018 | Cohorte | Clinical medicine & research | Eventos cutáneos adversos asociados a agentes biológicos, experiencia de un solo centro |
| [34786446](https://pubmed.ncbi.nlm.nih.gov/34786446/) | 2021 | Reporte de caso | JAAD case reports | Certolizumab como **tratamiento** de úlceras en piernas por vasculitis reumatoide (único caso favorable) |
| [31990069](https://pubmed.ncbi.nlm.nih.gov/31990069/) | 2020 | Reporte de caso | J Clin Pharm Ther | Vasculitis urticarial hipocomplementémica **inducida** por certolizumab durante tratamiento de AR |
| [28405087](https://pubmed.ncbi.nlm.nih.gov/28405087/) | 2017 | Reporte de caso | Proc (Bayl Univ Med Cent) | Vasculitis leucocitoclástica como reacción adversa a certolizumab |
| [41158918](https://pubmed.ncbi.nlm.nih.gov/41158918/) | 2025 | Reporte de caso | Cureus | Vasculitis de vaso mediano inducida por anti-TNF (certolizumab) en paciente con AR seronegativa |
| [32687015](https://pubmed.ncbi.nlm.nih.gov/32687015/) | 2021 | Reporte de caso | Mod Rheumatol Case Rep | Glomerulonefritis rápidamente progresiva tras inicio de certolizumab |

## Información de Mercado en España

Certolizumab pegol no cuenta actualmente con ninguna autorización de comercialización registrada en España (0 licencias).

## Consideraciones de Seguridad

No se dispone de información estructurada de advertencias, contraindicaciones ni interacciones farmacológicas para este fármaco en las fuentes consultadas. La obtención del prospecto oficial (TFDA/AEMPS) está identificada como una brecha de datos **bloqueante** para la evaluación de seguridad inicial (S1). Se recomienda consultar el prospecto oficial cuando esté disponible.

## Otros Candidatos Evaluados en este Informe

Este paquete de evidencia incluye 6 indicaciones predichas para certolizumab pegol. Por transparencia, se resumen aquí las otras 5, ya que dos de ellas presentan evidencia considerablemente más sólida que la vasculitis reumatoide:

| Indicación Predicha | Puntaje TxGNN | Nivel de Evidencia | Etapa | Decisión | Nota |
|------|------|------|------|------|------|
| Espondiloartropatía inflamatoria | 99.73% | L1 | S3 | **Proceed with Guardrails** | Múltiples ECA Fase 3 completados; mecanismo ya establecido y clínicamente maduro (no es una hipótesis novedosa) |
| Artritis reumatoide juvenil poliarticular | 99.69% | L2 | S2 | Research Question | 1 ensayo Fase 3 completado (NCT01550003, n=193) específico en pediatría; falta confirmar publicación de resultados |
| Enfermedad vertebral (vertebral disease) | 99.26% | L3 | S1 | Research Question | Etiqueta de enfermedad ambigua; evidencia recuperada corresponde mayormente a artritis reumatoide general, posible desajuste de ontología |
| Hipermovilidad del cóccix | 99.75% | L5 | S0 | Hold | Sin ensayos ni literatura; enfermedad mecánica/estructural sin relación plausible con inhibición de TNF-α |
| Enfermedad de Kümmell | 99.70% | L5 | S0 | Hold | Sin ensayos ni literatura; necrosis vertebral isquémica, sin relación mecanística con TNF-α |

## Conclusión y Próximos Pasos

**Decisión: Hold** (para la indicación de vasculitis reumatoide, foco de este informe)

**Justificación:**
La evidencia disponible es predominantemente de reportes de caso que documentan certolizumab pegol como **causa** de vasculitis (reacción adversa paradójica de anti-TNF), no como tratamiento de ella. Ningún ensayo clínico identificado evalúa directamente su eficacia en esta indicación. Además, la ausencia de datos de seguridad estructurados (advertencias/contraindicaciones, brecha bloqueante DG001) impide completar la evaluación inicial de seguridad (S1).

**Para avanzar se necesita:**
- Prospecto oficial (TFDA/AEMPS) con advertencias y contraindicaciones (brecha bloqueante DG001)
- Datos estructurados de mecanismo de acción vía DrugBank (DG002)
- Un estudio prospectivo controlado que evalúe específicamente eficacia (no solo seguridad) en vasculitis reumatoide
- Reconciliar la señal de seguridad paradójica antes de continuar el desarrollo en esta indicación

**Nota:** si el objetivo prioritario es identificar una vía de reposicionamiento viable para este fármaco, la **espondiloartropatía inflamatoria** (L1, Proceed with Guardrails) y la **artritis reumatoide juvenil poliarticular** (L2, Research Question) presentan una base de evidencia sustancialmente más sólida y merecen evaluación prioritaria sobre la vasculitis reumatoide.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

