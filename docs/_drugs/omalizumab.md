---
layout: default
title: Omalizumab
parent: 僅模型預測 (L5)
nav_order: 204
evidence_level: L5
indication_count: 10
---

# Omalizumab
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

# Omalizumab: De Asma Alérgica Grave a Bronquitis

## Resumen en Una Frase

Omalizumab es un anticuerpo monoclonal humanizado anti-IgE, utilizado originalmente en el tratamiento del asma alérgica grave persistente y la urticaria espontánea crónica (según se describe en la literatura recogida en este expediente).
El modelo TxGNN predice que podría ser efectivo para **Bronquitis**, con una puntuación de predicción del **99.99%**.
Sin embargo, solo **2 ensayos clínicos** y **8 publicaciones** respaldan actualmente esta dirección, y gran parte de esa evidencia corresponde en realidad a estudios de asma, no de bronquitis propiamente dicha.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Asma alérgica grave persistente y urticaria espontánea crónica (según literatura del expediente; no hay registro formal de indicaciones en este Evidence Pack) |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción (MOA) en la ficha estructurada de DrugBank (Data Gap). Según la literatura incluida en este expediente, omalizumab es un anticuerpo monoclonal humanizado que se une específicamente a la región constante (dominio Cε3) de la cadena pesada de la IgE, bloqueando su interacción con el receptor de alta afinidad FcεRI en mastocitos y basófilos, y reduciendo así la inflamación de tipo 2 mediada por IgE (PMID 16222080, PMID 11270941).

El asma alérgica y la bronquitis comparten vía aérea como órgano diana, lo que en principio sustenta una hipótesis mecanística: si la inflamación bronquial tiene un componente eosinofílico/alérgico mediado por IgE, bloquear la IgE podría, en teoría, ser beneficioso. De hecho, el único ensayo con enfoque más específico (NCT02049294) se centró en "bronquitis eosinofílica persistente".

No obstante, es necesario matizar la solidez de esta predicción. Según el análisis de relevancia incluido en el propio expediente, ambos ensayos identificados corresponden en realidad a poblaciones de **asma** (uno evalúa el efecto ahorrador de esteroides en pacientes con asma y bronquitis eosinofílica, con solo 11 sujetos; el otro es un estudio de búsqueda de dosis de **QGE031/ligelizumab** —un anticuerpo anti-IgE distinto de omalizumab— en urticaria espontánea crónica, sin descripción específica de bronquitis). La "bronquitis crónica" en sentido amplio (p. ej., asociada al tabaquismo) no es una enfermedad mediada por IgE, por lo que el vínculo mecanístico es débil fuera del subtipo eosinofílico/alérgico. Es probable que TxGNN haya agrupado el asma alérgica bajo el término genérico "bronquitis", generando una señal más amplia de lo que la evidencia real sustenta.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Fase 2/3 | Completado | 11 | Ensayo doble ciego controlado con placebo del efecto ahorrador de esteroides de Omalizumab en pacientes con asma y bronquitis eosinofílica persistente; población real predominantemente asmática, muestra muy pequeña. |
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Fase 2 | Completado | 382 | Estudio de búsqueda de dosis (add-on) de **QGE031 (ligelizumab)**, no de omalizumab, en urticaria espontánea crónica (CSU); sin descripción específica de bronquitis — relevancia limitada para esta indicación. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Revisión | Expert Opinion on Pharmacotherapy | Retos del tratamiento farmacológico del asma asociada a enfermedades de la vía aérea inducidas por tabaquismo, incluida la bronquitis crónica y el solapamiento asma-EPOC. |
| [35369622](https://pubmed.ncbi.nlm.nih.gov/35369622/) | 2022 | Cohorte | Postepy Dermatologii i Alergologii | Uso de omalizumab en pacientes de edad media/avanzada con asma alérgica grave y solapamiento con EPOC. |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Reporte de Caso | J Investig Allergol Clin Immunol | Caso raro de bronquitis plástica tras termoplastia bronquial (sin relación directa con eficacia de omalizumab). |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | Revisión | Masui (Jpn J Anesthesiology) | Manejo preoperatorio de pacientes con asma bronquial o bronquitis crónica; menciona omalizumab como opción en asma alérgica grave. |
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | No clasificado | Clinical Reviews in Allergy & Immunology | Revisión de la aprobación y experiencia postcomercialización de omalizumab; eficacia demostrada en asma persistente moderada-grave. |
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | No clasificado | Current Medical Research and Opinion | Análisis conjunto de seguridad y tolerabilidad de omalizumab en niños con asma alérgica. |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | No clasificado | Allergologia et Immunopathologia | Revisión general de anticuerpos monoclonales en pediatría, incluyendo enfermedades alérgicas. |
| [21163396](https://pubmed.ncbi.nlm.nih.gov/21163396/) | 2010 | No clasificado | Revue des Maladies Respiratoires | Revisión francesa sobre definición, fisiopatología y tratamiento de las exacerbaciones del asma del adulto. |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia disponible para "bronquitis" es de nivel L3 y, tras revisión de relevancia, los dos ensayos identificados corresponden en realidad a poblaciones de asma o a un fármaco distinto (ligelizumab), no a bronquitis propiamente dicha. Además, la ausencia de datos de advertencias/contraindicaciones de TFDA (Data Gap bloqueante) impide avanzar siquiera a la evaluación inicial de seguridad (S1).

**Para avanzar se necesita:**
- Obtener el prospecto/ficha técnica de TFDA con advertencias y contraindicaciones (bloqueante para evaluación S1).
- Confirmar el mecanismo de acción (MOA) formal en DrugBank para el análisis de relación mecanística.
- Redefinir la consulta de evidencia distinguiendo explícitamente "bronquitis eosinofílica/alérgica" de "bronquitis crónica no alérgica", dado que TxGNN parece haber sobregeneralizado el término.
- Excluir o marcar claramente los estudios que en realidad evalúan otros fármacos anti-IgE (p. ej., QGE031/ligelizumab) para evitar sobreestimar la evidencia.
- Nota: la indicación de rango 2 ("atopic eczema", L2, Proceed with Guardrails, con ensayo RCT directo NCT02300701) presenta evidencia considerablemente más sólida y podría priorizarse como candidato alternativo en un informe separado.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

