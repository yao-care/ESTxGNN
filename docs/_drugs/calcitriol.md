---
layout: default
title: Calcitriol
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L5
indication_count: 7
---

# Calcitriol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Calcitriol: De Trastornos del Metabolismo de Calcio y Fósforo a Raquitismo Hipofosfatémico Hereditario

*Nota metodológica: TxGNN generó 7 indicaciones predichas para calcitriol. La de mayor puntaje (rank 1, "obsolete vitamin D deficiency") está marcada por el propio pipeline como un artefacto de ontología de enfermedades obsoleta, no como candidato válido; los ranks 3–5 no tienen ningún ensayo ni literatura de respaldo. Este informe se centra en **raquitismo hipofosfatémico hereditario** (rank 7), la única indicación con evidencia clínica directa y de mayor calidad (L2).*

## Resumen en Una Frase

Calcitriol es la forma hormonalmente activa de la vitamina D (1,25-dihidroxivitamina D3), utilizada clínicamente en trastornos del metabolismo de calcio y fósforo. El modelo TxGNN predice que podría ser efectivo para **raquitismo hipofosfatémico hereditario**, con **7 ensayos clínicos** y **20 publicaciones** relacionadas, incluyendo un ensayo que evalúa calcitriol en monoterapia específicamente para esta indicación.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en este Evidence Pack (sin datos de indicaciones originales ni de ficha técnica de TFDA/AEMPS) |
| Nueva Indicación Predicha | Raquitismo hipofosfatémico hereditario |
| Puntaje de Predicción TxGNN | 99.28% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción (MOA) de calcitriol en este Evidence Pack. Según la información conocida, calcitriol es el metabolito activo final de la vitamina D3, responsable de la absorción intestinal de calcio y fósforo y de la regulación de la mineralización ósea.

El raquitismo hipofosfatémico hereditario (incluyendo la forma ligada al X, XLH) se debe a una pérdida renal crónica de fosfato mediada por exceso de FGF23, la cual también suprime la síntesis endógena de calcitriol. Esto genera un déficit funcional de calcitriol que agrava la mineralización ósea defectuosa, independientemente del aporte de fosfato. Por eso el vínculo mecanístico aquí es directo (no una inferencia lejana): calcitriol se ha usado durante décadas junto con suplementos de fosfato como pilar del tratamiento de esta enfermedad, y ensayos más recientes exploran si la monoterapia con calcitriol basta para mejorar los parámetros óseos sin las complicaciones renales asociadas a las altas dosis de fosfato.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03748966](https://clinicaltrials.gov/study/NCT03748966) | Fase Temprana 1 | Activo, no reclutando | 20 | Monoterapia con calcitriol (sin fosfato) en XLH; evalúa fosfato sérico, mineralización ósea y crecimiento sin aumentar calcificaciones renales. Relevancia A: título menciona calcitriol explícitamente |
| [NCT03820518](https://clinicaltrials.gov/study/NCT03820518) | Fase 4 | Estado desconocido | 100 | Compara dosis alta vs. baja de vitamina D activa + fosfato neutro en niños con XLH; probablemente calcitriol, no confirmado literalmente en el título |
| [NCT06046820](https://clinicaltrials.gov/study/NCT06046820) | Fase 3 | Activo, no reclutando | 27 | Eficacia y seguridad de INZ-701 en deficiencia de ENPP1; fármaco del estudio no confirmado como calcitriol |
| [NCT00844740](https://clinicaltrials.gov/study/NCT00844740) | N/A | Retirado | 0 | Evalúa cinacalcet (no calcitriol) como tratamiento a largo plazo del raquitismo hipofosfatémico familiar; ensayo retirado |
| [NCT06921720](https://clinicaltrials.gov/study/NCT06921720) | N/A | Aún no reclutando | 65 | Medición de ATP por espectroscopia de fósforo-31 en diabetes fosfática; estudio observacional, sin evaluación de calcitriol |
| [NCT01526304](https://clinicaltrials.gov/study/NCT01526304) | N/A | Estado desconocido | 150 | Estudio transversal de FGF23, Klotho y esclerostina en formadores de cálculos renales; no es intervención con calcitriol |
| [NCT04846647](https://clinicaltrials.gov/study/NCT04846647) | N/A | Completado | 260 | Estudio observacional de secreción inadecuada de FGF23 en pacientes con hipofosfatemia; no evalúa tratamiento con calcitriol |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [6252463](https://pubmed.ncbi.nlm.nih.gov/6252463/) | 1980 | Estudio clínico | The New England Journal of Medicine | Respuesta ósea a fosfato, ergocalciferol y calcitriol en 11 niños con raquitismo resistente a vitamina D; calcitriol aumentó la absorción intestinal de fosfato |
| [3839245](https://pubmed.ncbi.nlm.nih.gov/3839245/) | 1985 | Estudio clínico | The Journal of Clinical Investigation | Dosis altas de calcitriol curan la osteomalacia coexistente en XLH, a diferencia de la terapia convencional con fosfato y vitamina D |
| [2492895](https://pubmed.ncbi.nlm.nih.gov/2492895/) | 1989 | Estudio clínico | Calcified Tissue International | Medición de masa ósea en 17 niños con raquitismo hipofosfatémico familiar tras terapia con calcitriol y fosfato suplementario |
| [29292875](https://pubmed.ncbi.nlm.nih.gov/29292875/) | 2017 | Estudio de cohorte | Pediatric Endocrinology Reviews | Crecimiento espontáneo y efecto de terapia temprana con calcitriol y fosfato en 127 pacientes con XLH de 49 centros |
| [39181153](https://pubmed.ncbi.nlm.nih.gov/39181153/) | 2024 | Revisión | The Lancet | Revisión de XLH: exceso de FGF23 reduce la síntesis de calcitriol, causando pérdida renal de fosfato y raquitismo |
| [40295317](https://pubmed.ncbi.nlm.nih.gov/40295317/) | 2025 | Revisión | Calcified Tissue International | Diagnóstico y terapia de XLH, incluyendo el rol de calcitriol en el manejo estándar |
| [36446330](https://pubmed.ncbi.nlm.nih.gov/36446330/) | 2022 | Revisión | Hormone Research in Paediatrics | Revisión histórica y fisiológica del raquitismo, vitamina D y metabolismo de calcio/fósforo |
| [17117305](https://pubmed.ncbi.nlm.nih.gov/17117305/) | 2006 | Revisión | Arquivos Brasileiros de Endocrinologia e Metabologia | Raquitismo hipofosfatémico y osteomalacia: niveles inapropiadamente bajos de calcitriol como mecanismo común |
| [35226335](https://pubmed.ncbi.nlm.nih.gov/35226335/) | 2022 | Estudio de cohorte | Journal of Endocrinological Investigation | Crecimiento en altura y proporción corporal desde el nacimiento hasta la adultez en raquitismo hipofosfatémico hereditario |
| [3796683](https://pubmed.ncbi.nlm.nih.gov/3796683/) | 1987 | Estudio de cohorte | The New England Journal of Medicine | Hipercalciuria idiopática y raquitismo hipofosfatémico hereditario con hipercalciuria (HHRH) como expresiones de un defecto genético común |

## Información de Mercado en España

Calcitriol no está actualmente comercializado en España según este Evidence Pack (0 autorizaciones registradas), por lo que no hay información de producto, forma farmacéutica ni indicación aprobada disponible para tabular.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

⚠️ Este Evidence Pack marca como **brecha bloqueante** la ausencia de advertencias/contraindicaciones oficiales (ficha técnica de TFDA), lo que impide actualmente completar la evaluación de seguridad inicial (S1). No se debe avanzar a evaluación clínica sin resolver este punto.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La indicación de raquitismo hipofosfatémico hereditario cuenta con evidencia de nivel L2: un ensayo activo que evalúa calcitriol en monoterapia (NCT03748966) y décadas de literatura clínica que respaldan a calcitriol como componente histórico del tratamiento estándar (junto con fosfato) para esta enfermedad. Sin embargo, el fármaco no está comercializado en España y faltan datos regulatorios básicos de seguridad, por lo que no puede avanzar sin controles adicionales.

**Para avanzar se necesita:**
- Ficha técnica/prospecto de TFDA con advertencias y contraindicaciones oficiales (brecha bloqueante DG001)
- Datos del mecanismo de acción confirmados vía DrugBank (DG002)
- Resultados de NCT03748966 (monoterapia con calcitriol en XLH) y NCT06046820 al completarse
- Evaluación de vías de comercialización/formas farmacéuticas para entrada al mercado español, dado el estado actual "no comercializado"
- Confirmación de las indicaciones originales aprobadas de calcitriol, actualmente ausentes en este Evidence Pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

