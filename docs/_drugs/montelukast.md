---
layout: default
title: Montelukast
parent: 僅模型預測 (L5)
nav_order: 187
evidence_level: L5
indication_count: 5
---

# Montelukast
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

# Montelukast: De Asma a Bronquitis

## Resumen en Una Frase

Montelukast es un antagonista selectivo del receptor de leucotrieno cisteinílico (CysLT1), utilizado originalmente en el tratamiento y prevención del asma y en el alivio de la rinitis alérgica. El modelo TxGNN predice que podría ser efectivo para **Bronquitis**, con **23 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección, aunque gran parte de esta evidencia corresponde a subtipos específicos (bronquiolitis obliterante post-trasplante, bronquitis eosinofílica no asmática) más que a la bronquitis en sentido amplio.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Asma (uso de referencia establecido); sin registro de indicación en las licencias españolas incluidas en este dataset |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 99.95% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en este Evidence Pack (data gap DG002). Según la información conocida, Montelukast es un antagonista del receptor de leucotrieno cisteinílico 1 (CysLT1), que bloquea la acción del leucotrieno D4 sobre el músculo liso bronquial y el endotelio de la vía aérea, inhibiendo la broncoconstricción, la inflamación y la infiltración eosinofílica. Su eficacia en asma ha sido ampliamente comprobada, y este mismo mecanismo mediado por leucotrienos participa en otras condiciones inflamatorias de la vía aérea.

El asma y la bronquitis comparten mecanismos fisiopatológicos: inflamación de la vía aérea, broncoconstricción y participación de leucotrienos cisteinílicos. Esto hace mecanísticamente razonable extender el uso de Montelukast a ciertos subtipos de bronquitis, particularmente la bronquitis eosinofílica no asmática y la bronquiolitis obliterante (BO) tras trasplante de células madre hematopoyéticas o de pulmón, donde varios ensayos han evaluado directamente su uso.

**Nota importante sobre la calidad del dato:** en este mismo Evidence Pack, "asma" aparece listada como la indicación predicha rank 3 (score TxGNN 99.54%, evidencia L1, "Proceed with Guardrails"), con una advertencia explícita del propio dataset de que se trata de una indicación **ya establecida** de Montelukast y no de un candidato genuino de reposicionamiento. Esto sugiere una posible confusión en el pipeline de datos entre "indicación original" e "indicación predicha" que debería revisarse antes de tomar decisiones basadas en este Evidence Pack.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01211509](https://clinicaltrials.gov/study/NCT01211509) | Fase 4 | Completado | 30 | RCT doble ciego con placebo: Montelukast para enlentecer la progresión del síndrome de bronquiolitis obliterante (BOS) tras trasplante de pulmón |
| [NCT01307462](https://clinicaltrials.gov/study/NCT01307462) | Fase 2 | Completado | 36 | Combinación FAM (fluticasona + azitromicina + montelukast) en bronquiolitis obliterante tras trasplante de células madre |
| [NCT00863317](https://clinicaltrials.gov/study/NCT00863317) | N/A | Completado | 141 | RCT doble ciego con placebo: Montelukast diario para bronquiolitis viral en lactantes |
| [NCT00656058](https://clinicaltrials.gov/study/NCT00656058) | Fase 2 | Completado | 25 | Estudio multiinstitucional de Montelukast para bronquiolitis obliterante tras trasplante alogénico/autólogo de células madre |
| [NCT04613180](https://clinicaltrials.gov/study/NCT04613180) | Fase 4 | Desconocido | 100 | Efectividad de montelukast sódico en tratamiento y prevención de bronquitis obstructiva recurrente en niños 1-7 años |
| [NCT01121016](https://clinicaltrials.gov/study/NCT01121016) | Fase 4 | Desconocido | 63 | Montelukast como terapia añadida a budesonida inhalada en bronquitis eosinofílica no asmática |
| [NCT03072849](https://clinicaltrials.gov/study/NCT03072849) | N/A | Completado | 23 | Detección y manejo temprano de BOS post-trasplante pediátrico con terapia combinada fluticasona/azitromicina/montelukast |
| [NCT00524693](https://clinicaltrials.gov/study/NCT00524693) | N/A | Completado | 51 | RCT doble ciego con placebo: efecto de montelukast en bronquiolitis aguda por VRS |
| [NCT01370187](https://clinicaltrials.gov/study/NCT01370187) | N/A | Completado | 146 | Montelukast para bronquiolitis aguda y sibilancias post-bronquiolitis en lactantes de 3-12 meses |
| [NCT00394069](https://clinicaltrials.gov/study/NCT00394069) | Fase 2 | Completado | 14 | Perfil de seguridad, tolerabilidad y concentración plasmática de gránulos orales de montelukast en niños de 3-6 meses con bronquiolitis |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38485149](https://pubmed.ncbi.nlm.nih.gov/38485149/) | 2024 | Guía de Práctica Clínica | Eur Respir J | Guía conjunta ERS/EBMT sobre tratamiento de la enfermedad pulmonar crónica de injerto contra huésped (incluye antileucotrienos) |
| [25563311](https://pubmed.ncbi.nlm.nih.gov/25563311/) | 2015 | ECA | Chinese Medical Journal | Montelukast añadido a budesonida mejora inflamación eosinofílica, tos y calidad de vida en bronquitis eosinofílica no asmática |
| [20976161](https://pubmed.ncbi.nlm.nih.gov/20976161/) | 2010 | ECA | PLoS ONE | Comparación de aceite de pescado y montelukast sobre inflamación de vía aérea y broncoconstricción inducida por hiperpnea |
| [38504551](https://pubmed.ncbi.nlm.nih.gov/38504551/) | 2024 | Revisión | Ther Adv Respir Dis | Potencial terapéutico de montelukast en síndrome de bronquiolitis obliterante tras trasplante pulmonar y de células madre |
| [30038355](https://pubmed.ncbi.nlm.nih.gov/30038355/) | 2019 | Revisión | Bone Marrow Transplant | Diagnóstico y tratamiento del síndrome de bronquiolitis obliterante |
| [21486501](https://pubmed.ncbi.nlm.nih.gov/21486501/) | 2011 | Revisión | BMJ Clinical Evidence | Revisión general de bronquiolitis en lactantes |
| [19450362](https://pubmed.ncbi.nlm.nih.gov/19450362/) | 2007 | Revisión | BMJ Clinical Evidence | Revisión general de bronquiolitis en lactantes |
| [29308548](https://pubmed.ncbi.nlm.nih.gov/29308548/) | 2018 | Revisión/Guía | Indian J Pediatr | Manejo de sibilancias recurrentes preescolares, diferenciación entre asma y bronquiolitis/bronquitis |
| [28545478](https://pubmed.ncbi.nlm.nih.gov/28545478/) | 2017 | Estudio Animal | J Cardiothorac Surg | Rol de LTB4 y montelukast en bronquiolitis obliterante relacionada con trasplante, en modelo de rata |
| [24345788](https://pubmed.ncbi.nlm.nih.gov/24345788/) | 2014 | Revisión (mecanismo) | Curr Opin Allergy Clin Immunol | Mecanismos de la tos crónica |

---

## Información de Mercado en España

Montelukast no está actualmente comercializado en España según los datos de este Evidence Pack (`market_status: 未上市`, 0 autorizaciones registradas). No hay licencias disponibles para tabular información de producto, forma farmacéutica o indicación aprobada localmente.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia clínica para "bronquitis" en sentido amplio es heterogénea: la mayoría de los ensayos y publicaciones de mayor calidad se concentran en subpoblaciones específicas (bronquiolitis obliterante post-trasplante, bronquitis eosinofílica no asmática, bronquiolitis viral infantil) más que en un ensayo confirmatorio dirigido a "bronquitis" como entidad única. Además, el fármaco no está comercializado en España y persisten brechas de datos bloqueantes (DG001: advertencias/contraindicaciones de la AEMPS).

**Para avanzar se necesita:**
- Obtener el prospecto/ficha técnica de la AEMPS (DG001, bloqueante) antes de cualquier evaluación de seguridad
- Completar datos de mecanismo de acción (MOA) vía DrugBank (DG002)
- Redefinir la indicación diana a un subgrupo específico y bien delimitado (p. ej. bronquiolitis obliterante post-trasplante o bronquitis eosinofílica no asmática) en lugar de "bronquitis" genérica
- Revisar la calidad del pipeline de datos: la aparición de "asma" como indicación predicha (rank 3, L1) cuando en realidad es la indicación ya establecida de Montelukast sugiere una posible confusión entre indicación original e indicación candidata que debe corregirse antes de futuras evaluaciones
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

