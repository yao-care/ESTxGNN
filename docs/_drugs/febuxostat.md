---
layout: default
title: Febuxostat
parent: 僅模型預測 (L5)
nav_order: 118
evidence_level: L5
indication_count: 3
---

# Febuxostat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Febuxostat: De Hiperuricemia/Gota a Hipouricemia Renal

## Resumen en Una Frase

Febuxostat es un inhibidor de la xantina oxidasa (XOR) utilizado habitualmente en el tratamiento de la hiperuricemia y la gota. El modelo TxGNN predice que podría ser efectivo para **Hipouricemia Renal**, pero esta dirección solo cuenta con **1 ensayo clínico** de relevancia cuestionable y **2 publicaciones** de tipo revisión, y existe una señal mecanística fuerte de que se trata de un falso positivo del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hiperuricemia / Gota (según información conocida de la clase farmacológica; sin ficha técnica TFDA verificada) |
| Nueva Indicación Predicha | Hipouricemia Renal |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha técnica (TFDA). Según la información conocida, febuxostat es un inhibidor de la xantina oxidasa (XOR) cuya acción farmacológica consiste en **reducir** la producción de ácido úrico, y su eficacia en hiperuricemia/gota está firmemente establecida.

Sin embargo, en este caso el análisis mecanístico apunta en contra de la predicción, no a favor. La hipouricemia renal es una alteración genética del transportador tubular de urato (p. ej. defectos de URAT1/GLUT9) en la que el paciente **ya excreta ácido úrico en exceso** y presenta niveles séricos bajos. Administrar un fármaco que reduce aún más la síntesis de ácido úrico no trataría esta condición, sino que teóricamente la agravaría.

Por esta razón, la asociación identificada por TxGNN se considera **altamente sospechosa de ser un artefacto lingüístico** entre los términos "hyperuricemia" (exceso de ácido úrico, indicación real de febuxostat) e "hypouricemia" (déficit de ácido úrico), más que una hipótesis de reposicionamiento genuina.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Fase 4 | Desconocido | 100 | Estudio prospectivo controlado sobre el efecto del control de ácido úrico en la recurrencia de cálculos y la función renal en pacientes con litiasis por hiperuricemia. El título no especifica intervención ni indicación, y la relevancia respecto a hipouricemia renal se calificó como baja (Grado C) — no puede considerarse evidencia de soporte. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Revisión | Clinical Rheumatology | Revisión narrativa sobre hipouricemia (urato sérico <2 mg/dL), su etiología y relevancia clínica para el reumatólogo; no evalúa febuxostat como tratamiento. |
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Revisión | Internal Medicine (Tokyo) | Reporte de un caso de lesión renal aguda inducida por ejercicio (EIAKI) asociada a hipouricemia renal familiar (mutación URAT1); menciona febuxostat como posible profilaxis de EIAKI en este contexto específico, no como tratamiento de la hipouricemia en sí. |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia es de nivel L5 (solo predicción del modelo), el único ensayo clínico disponible tiene relevancia baja y estado de reclutamiento desconocido, y la literatura no respalda directamente el uso de febuxostat para tratar la hipouricemia renal. Además, el análisis mecanístico sugiere que la dirección farmacológica es opuesta a la necesaria para esta indicación, por lo que se sospecha un falso positivo derivado de similitud terminológica (hiperuricemia vs. hipouricemia).

**Para avanzar se necesita:**
- Obtener los datos de advertencias/contraindicaciones de la TFDA (actualmente bloqueante para la evaluación de seguridad S1)
- Confirmar el mecanismo de acción (MOA) mediante DrugBank u otra fuente verificada
- Revisión mecanística independiente que descarte el falso positivo antes de invertir en investigación adicional sobre esta indicación específica
- Como alternativa, evaluar los candidatos secundarios del mismo evidence pack —deficiencia parcial de HPRT y síndrome de Lesch-Nyhan (ambos L4, etapa S1, "Research Question")— que presentan una lógica mecanística coherente con la acción real de febuxostat (reducción de producción de ácido úrico en estados de hiperuricemia por sobreproducción), aunque también carecen de ensayos clínicos directos
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

