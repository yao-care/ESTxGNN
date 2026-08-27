---
layout: default
title: Bimatoprost
parent: 僅模型預測 (L5)
nav_order: 42
evidence_level: L5
indication_count: 10
---

# Bimatoprost
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

# Bimatoprost: De Glaucoma/Hipotricosis de Pestañas a Alopecia

## Resumen en Una Frase

Bimatoprost es un análogo de prostamida/PGF2α, aprobado originalmente para el glaucoma de ángulo abierto y la hipertensión ocular, y posteriormente extendido a la hipotricosis de pestañas (Latisse, aprobación FDA). El modelo TxGNN predice que también podría ser efectivo para la **Alopecia**, respaldado por **10 ensayos clínicos** (incluyendo tres ECA de Fase 2 con más de 240 pacientes cada uno) y **10 publicaciones** relevantes. Sin embargo, la falta de datos de seguridad de TFDA/AEMPS es una brecha bloqueante que impide por ahora avanzar a la evaluación formal de seguridad.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Glaucoma de ángulo abierto / hipertensión ocular; hipotricosis de pestañas (uso internacional, no comercializado en España) |
| Nueva Indicación Predicha | Alopecia |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos estructurados sobre el mecanismo de acción (MOA) en la ficha del fármaco, pero la evidencia de literatura incluida en este paquete permite reconstruirlo: bimatoprost es un análogo sintético de prostamida/PGF2α que activa receptores FP en la vecindad del folículo piloso, prolongando la fase anágena (de crecimiento) del ciclo capilar y aumentando el diámetro y la pigmentación del pelo.

Este mecanismo ya está clínicamente validado para la hipotricosis de pestañas (Latisse, aprobación FDA), lo que constituye un precedente directo de traducción del efecto "colateral" (crecimiento piloso) en una indicación aprobada. La extensión hacia la alopecia del cuero cabelludo —tanto androgenética (AGA/FPHL) como areata— es mecanísticamente coherente, ya que se trata del mismo receptor y la misma vía de señalización, solo que aplicada a un folículo piloso distinto.

La solidez de esta hipótesis se refleja en que, a diferencia de la mayoría de las demás indicaciones predichas por TxGNN para este fármaco (ver sección de indicaciones descartadas), la alopecia cuenta con múltiples ensayos clínicos de Fase 2 aleatorizados y controlados, journals de dermatología revisados por pares, y un ensayo de Fase 4 ya aprobado comercialmente para una indicación folicular relacionada (hipotricosis de pestañas pediátrica).

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01325350](https://clinicaltrials.gov/study/NCT01325350) | Fase 2 | Completado | 306 | ECA en mujeres con alopecia de patrón femenino (FPHL): 3 dosis de bimatoprost vs. vehículo vs. minoxidil 2% OTC |
| [NCT01904721](https://clinicaltrials.gov/study/NCT01904721) | Fase 2 | Completado | 244 | ECA de seguridad y eficacia en hombres con alopecia androgenética (AGA) |
| [NCT01325337](https://clinicaltrials.gov/study/NCT01325337) | Fase 2 | Completado | 307 | ECA en hombres con AGA: 3 dosis de bimatoprost vs. vehículo vs. minoxidil 5% OTC |
| [NCT02170662](https://clinicaltrials.gov/study/NCT02170662) | Fase 2 | Completado | 33 | Efecto de bimatoprost tópico sobre folículos capilares andrógeno-dependientes |
| [NCT01023841](https://clinicaltrials.gov/study/NCT01023841) | Fase 4 | Completado | 71 | Seguridad y eficacia en pérdida de pestañas/hipotricosis en niños (indicación ya aprobada) |
| [NCT05600673](https://clinicaltrials.gov/study/NCT05600673) | Fase 1/2 | Completado | 30 | Bimatoprost 0.03% combinado con láser CO2 fraccionado en alopecia areata |
| [NCT01189279](https://clinicaltrials.gov/study/NCT01189279) | Fase 1 | Completado | 42 | Seguridad, tolerabilidad y farmacocinética de nuevas formulaciones tópicas en alopecia |
| [NCT02676310](https://clinicaltrials.gov/study/NCT02676310) | Fase 1 | Terminado | 53 | Escalada de dosis en AGA masculina (ensayo terminado antes de completarse) |
| [NCT02848300](https://clinicaltrials.gov/study/NCT02848300) | Fase 1 | Completado | 11 | Farmacocinética local y tolerabilidad cutánea en cuero cabelludo con AGA |
| [NCT00187577](https://clinicaltrials.gov/study/NCT00187577) | N/A | Completado | 14 | Comparación latanoprost vs. bimatoprost oftálmico para crecimiento de pestañas en alopecia areata |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32250713](https://pubmed.ncbi.nlm.nih.gov/32250713/) | 2022 | Revisión Sistemática | J Dermatolog Treat | Meta-análisis en red de tratamientos no quirúrgicos para AGA en hombres y mujeres |
| [29863806](https://pubmed.ncbi.nlm.nih.gov/29863806/) | 2018 | Guía Clínica | J Dermatol | Guía japonesa de diagnóstico y tratamiento de alopecia de patrón masculino/femenino |
| [28264599](https://pubmed.ncbi.nlm.nih.gov/28264599/) | 2017 | Revisión | Expert Opin Investig Drugs | Bimatoprost para alopecia de pestañas, cejas y cuero cabelludo |
| [40252129](https://pubmed.ncbi.nlm.nih.gov/40252129/) | 2025 | Estudio Clínico | Arch Dermatol Res | Combinación de láser CO2 fraccionado con bimatoprost mejora el recrecimiento en alopecia areata |
| [35278027](https://pubmed.ncbi.nlm.nih.gov/35278027/) | 2022 | Cohorte Prospectivo | Dermatol Ther | Estudio abierto prospectivo de bimatoprost tópico en pérdida de pestañas por alopecia totalis/universalis |
| [37089845](https://pubmed.ncbi.nlm.nih.gov/37089845/) | 2023 | Ensayo Clínico Abierto | Indian Dermatol Online J | Bimatoprost vs. propionato de clobetasol en alopecia areata del cuero cabelludo |
| [29854658](https://pubmed.ncbi.nlm.nih.gov/29854658/) | 2018 | Revisión | Indian Dermatol Online J | Revisión del uso de bimatoprost en dermatología, incluyendo alopecia |
| [33631058](https://pubmed.ncbi.nlm.nih.gov/33631058/) | 2021 | Revisión Sistemática | Dermatol Ther | Meta-análisis en red de tratamientos para alopecia areata |
| [35040730](https://pubmed.ncbi.nlm.nih.gov/35040730/) | 2022 | Preclínico/Formulación | Drug Deliv | Formulación tópica de bimatoprost con mayor penetración cutánea y eficacia de recrecimiento en AGA |
| [38577618](https://pubmed.ncbi.nlm.nih.gov/38577618/) | 2024 | Preclínico/Formulación | Int J Pharm X | Nanogel spanlastic para mejorar la administración dérmica de bimatoprost en AGA |

---

## Información de Mercado en España

Actualmente el bimatoprost no está comercializado en España (0 autorizaciones registradas en el paquete de evidencia), por lo que no hay información de productos disponibles.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Los datos de advertencias, contraindicaciones e interacciones farmacológicas (DDI) no están disponibles en las fuentes consultadas (TFDA/AEMPS). La obtención del prospecto oficial (TFDA) está identificada como una brecha de datos **bloqueante** para el avance a la evaluación de seguridad (S1).

---

## Otras Indicaciones Evaluadas (Descartadas por Baja Confianza)

El paquete de evidencia incluyó 10 indicaciones predichas por TxGNN. Salvo alopecia (y, en menor medida, "genetic alopecia" — L4, evidencia de reportes de caso), el resto obtuvo puntajes TxGNN altos pero **sin respaldo clínico ni literario**, y fueron señaladas por el propio análisis como probable ruido del grafo (relación mecanística nula o contradictoria):

| Indicación | Puntaje TxGNN | Nivel de Evidencia | Decisión |
|------|------|------|------|
| Malformación con componente odontal/periodontal | 99.99% | L5 | Hold |
| Síndrome con malformación de Dandy-Walker | 99.99% | L5 | Hold |
| Anomalía genética aislada del tallo piloso | 99.99% | L5 | Hold |
| Hipertricosis universal congénita tipo Ambras | 99.99% | L5 | Hold |
| Hipotricosis simple del cuero cabelludo | 99.99% | L5 | Hold |
| Hipotricosis congénita con milia | 99.99% | L5 | Hold |
| Alopecia areata difusa | 99.99% | L5 | Hold |
| Alopecia genética | 99.97% | L4 | Research Question |
| Malformación arteriovenosa pulmonar | 99.95% | L5 | Hold |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación de alopecia cuenta con evidencia mecanística sólida y múltiples ensayos de Fase 2 aleatorizados (L2) que respaldan la plausibilidad biológica, incluyendo un precedente de aprobación comercial en una indicación folicular relacionada (pestañas). Sin embargo, la ausencia del prospecto/ficha técnica de TFDA (DG001, severidad bloqueante) impide completar la evaluación de seguridad inicial (S1), y el fármaco no está actualmente comercializado en España, lo que añade incertidumbre regulatoria.

**Para avanzar se necesita:**
- Obtener el prospecto oficial de TFDA/AEMPS con advertencias y contraindicaciones (DG001, bloqueante)
- Completar los datos de mecanismo de acción (MOA) desde DrugBank (DG002)
- Confirmar la vía regulatoria en España dado que el fármaco no tiene autorización de comercialización actual
- Evaluar si existen datos de Fase 3 más recientes en AGA/FPHL que consoliden el nivel de evidencia de L2 a L1
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

