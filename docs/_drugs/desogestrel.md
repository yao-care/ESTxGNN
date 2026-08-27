---
layout: default
title: Desogestrel
parent: 僅模型預測 (L5)
nav_order: 89
evidence_level: L5
indication_count: 10
---

# Desogestrel
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

# Desogestrel: De Anticoncepción Hormonal a Amenorrea

## Resumen en Una Frase

Desogestrel es un progestágeno de tercera generación utilizado como componente de anticonceptivos hormonales (combinados o solo progestágeno). El modelo TxGNN predice que podría ser efectivo para **Amenorrea**, con **2 ensayos clínicos** y **16 publicaciones** identificadas, pero ninguno de estos estudios evalúa desogestrel como tratamiento de la amenorrea — de hecho, la amenorrea es un efecto adverso conocido de este fármaco, no un uso terapéutico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Anticoncepción hormonal (progestágeno, uso combinado u oral de progestágeno solo) |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción (MOA) en la ficha del fármaco. Según la evidencia recopilada, desogestrel es un progestágeno de baja actividad androgénica (tercera generación), utilizado ampliamente en combinación con etinilestradiol como anticonceptivo oral, y también en formulación de progestágeno solo (minipíldora).

**⚠️ Señal de alerta metodológica:** la relación entre desogestrel y amenorrea señalada por TxGNN es mecanísticamente inversa a lo esperado. Farmacológicamente, desogestrel es un inhibidor de la ovulación cuyo efecto adverso frecuente es *inducir* amenorrea (ausencia de sangrado por atrofia endometrial), no tratarla. El puntaje alto del modelo probablemente refleja la co-ocurrencia en registros clínicos entre usuarias de anticonceptivos y códigos diagnósticos de amenorrea (una reacción adversa reportada), en lugar de una relación causal terapéutica real. Ningún ensayo clínico identificado utiliza desogestrel como intervención para tratar la amenorrea.

Cabe destacar que, dentro del mismo Evidence Pack, la indicación predicha "acné" (rank 4) presenta un fundamento mecanístico mucho más sólido y consistente con el uso conocido de anticonceptivos combinados con desogestrel, respaldado por un ensayo Fase 4 completado (NCT01466673, grado de relevancia A) y evidencia de nivel L2. Se recomienda evaluar esa dirección como candidato prioritario en lugar de amenorrea.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01588873](https://clinicaltrials.gov/study/NCT01588873) | Fase 4 | Desconocido | 42 | Comparó anticonceptivo oral vs. anillo vaginal hormonal en parámetros hormonales/metabólicos en mujeres con SOP; no evalúa tratamiento de amenorrea (relevancia: grado C). |
| [NCT00946192](https://clinicaltrials.gov/study/NCT00946192) | Fase 3 | Completado | 121 | Estudió la función reproductiva/endocrina en atletas con amenorrea del ejercicio, comparando estrógeno transdérmico u oral frente a ausencia de tratamiento; no es un ensayo intervencional de desogestrel para amenorrea (relevancia: grado B). |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35261299](https://pubmed.ncbi.nlm.nih.gov/35261299/) | 2022 | Cohorte | Gynecol Endocrinol | Compara perfil de sangrado de drospirenona vs. desogestrel 0.075 mg; señala que la amenorrea es un patrón de sangrado asociado (no un objetivo terapéutico) de las píldoras de progestágeno solo. |
| [3161265](https://pubmed.ncbi.nlm.nih.gov/3161265/) | 1985 | Estudio farmacodinámico | Acta Obstet Gynecol Scand Suppl | Evalúa androgenicidad de progestágenos; menciona amenorrea como parte del cuadro clínico del SOP, no como indicación tratable por desogestrel. |
| [11725730](https://pubmed.ncbi.nlm.nih.gov/11725730/) | 2001 | Estudio observacional | J Reprod Med | Evalúa densidad mineral ósea en mujeres con oligoamenorrea hipotalámica tratadas con anticonceptivos orales de dosis decrecientes de estrógeno. |
| [8447356](https://pubmed.ncbi.nlm.nih.gov/8447356/) | 1993 | Revisión/Tolerabilidad | Am J Obstet Gynecol | Revisión general de tolerabilidad de desogestrel/etinilestradiol; beneficios no anticonceptivos reportados, sin evidencia específica sobre amenorrea. |
| [8218004](https://pubmed.ncbi.nlm.nih.gov/8218004/) | 1993 | Cohorte comparativa | Br J Obstet Gynaecol | Compara fiabilidad, control de ciclo y efectos secundarios de dos formulaciones con desogestrel (20 vs 30 mcg etinilestradiol). |
| [2956054](https://pubmed.ncbi.nlm.nih.gov/2956054/) | 1987 | Estudio observacional | Contraception | Evalúa el aplazamiento del sangrado por deprivación en usuarias de anticonceptivos orales combinados de baja dosis. |
| [23221134](https://pubmed.ncbi.nlm.nih.gov/23221134/) | 2012 | Estudio observacional | Georgian Med News | Estudia el manejo de oligomenorrea/amenorrea de origen central en mujeres infértiles; no involucra desogestrel como tratamiento directo. |
| [21249657](https://pubmed.ncbi.nlm.nih.gov/21249657/) | 2011 | Revisión (Cochrane) | Cochrane Database Syst Rev | Revisión sobre dosis de estrógeno en anticonceptivos orales combinados y su relación con patrones de sangrado. |
| [1436906](https://pubmed.ncbi.nlm.nih.gov/1436906/) | 1992 | Revisión | Obstet Gynecol Surv | Revisión de la nueva generación de progestágenos (desogestrel, norgestimato, gestodeno) en anticoncepción oral. |
| [8324604](https://pubmed.ncbi.nlm.nih.gov/8324604/) | 1993 | Revisión | Br Med Bull | Revisión sobre aceptabilidad y uso eficaz de anticonceptivos orales combinados. |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ningún ensayo clínico ni publicación identificados evalúan desogestrel como tratamiento de la amenorrea; toda la evidencia disponible corresponde a estudios de anticoncepción hormonal donde la amenorrea aparece como efecto adverso o patrón de sangrado, no como resultado terapéutico buscado. El alto puntaje de TxGNN probablemente refleja un artefacto de co-ocurrencia en datos clínicos (usuarias de anticonceptivos con diagnóstico de amenorrea) más que una señal de reposicionamiento válida.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) de desogestrel desde DrugBank
- Ficha técnica/prospecto de AEMPS con advertencias y contraindicaciones (actualmente sin datos)
- Evaluación separada de la indicación "acné" (rank 4), que presenta evidencia L2 y un ensayo Fase 4 completado directamente relevante — candidato con mucho mayor potencial que amenorrea
- Si se desea explorar amenorrea, sería necesario un ensayo dedicado que use desogestrel como intervención terapéutica, no solo como anticonceptivo de fondo
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

