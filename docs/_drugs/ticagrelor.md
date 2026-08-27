---
layout: default
title: Ticagrelor
parent: 僅模型預測 (L5)
nav_order: 275
evidence_level: L5
indication_count: 10
---

# Ticagrelor
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

# Ticagrelor: De Enfermedad Isquémica Cardiovascular a Arteriosclerosis Intracraneal

## Resumen en Una Frase

Ticagrelor es un antiagregante plaquetario cuyo uso establecido corresponde al síndrome coronario agudo (SCA) y a pacientes sometidos a intervención coronaria percutánea (ICP), dentro del espectro de enfermedades isquémicas cardiovasculares. El modelo TxGNN predice que podría ser efectivo para **Arteriosclerosis Intracraneal**, con **11 ensayos clínicos** y **3 publicaciones** que actualmente respaldan esta dirección, aunque la evidencia todavía se considera preliminar.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | No disponible en este evidence pack (sin licencias TFDA/DrugBank registradas); el contexto de la evidencia recopilada apunta a uso establecido en enfermedad isquémica cardiovascular (SCA/ICP) |
| Nueva Indicacion Predicha | Arteriosclerosis Intracraneal |
| Puntaje de Prediccion TxGNN | 99.97% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Espana | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold (Research Question) |

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone del dato oficial de mecanismo de acción (`original_moa` marcado como vacío en DrugBank). Sin embargo, la propia evidencia recopilada en este paquete señala que ticagrelor es un **antagonista reversible del receptor plaquetario P2Y12**, que inhibe la activación y agregación plaquetaria inducida por ADP — mecanismo central de su uso ya consolidado en enfermedades isquémicas vasculares como el síndrome coronario agudo, tras ICP, y en enfermedad arterial periférica (respaldado por ensayos de gran tamaño como GLOBAL LEADERS y EUCLID, dentro del propio evidence pack).

La arteriosclerosis intracraneal comparte con la enfermedad coronaria un mismo sustrato fisiopatológico: formación de placa aterosclerótica con estenosis luminal y trombosis dependiente de la activación plaquetaria. Por ello, la inhibición de P2Y12 podría reducir eventos isquémicos originados en la placa intracraneal de forma análoga a como lo hace en la circulación coronaria.

No obstante, la circulación intracraneal difiere de la coronaria en un aspecto crítico: el riesgo de hemorragia intracraneal es distinto y potencialmente mayor, por lo que la extrapolación de seguridad desde el contexto cardiovascular debe hacerse con cautela, tal como señala explícitamente el análisis de racionalidad del propio candidato ("mecanismo similar a la arteriosclerosis coronaria, pero el riesgo hemorrágico de la circulación intracraneal difiere del coronario").

---

## Evidencia de Ensayos Clinicos

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT05047172](https://clinicaltrials.gov/study/NCT05047172) | Fase 3 | Activo, no reclutando | 1683 | CAPTIVA: compara rivaroxabán, ticagrelor o ambos frente a clopidogrel para reducir ictus isquémico, hemorragia intracerebral o muerte vascular a 1 año en estenosis arterial intracraneal; aún sin resultados |
| [NCT04948749](https://clinicaltrials.gov/study/NCT04948749) | N/A | Reclutando | 792 | DREAM-PRIDE: evalúa si stent liberador de fármaco + tratamiento médico agresivo reduce recurrencia de ictus a 1 año en enfermedad arterial intracraneal sintomática |
| [NCT06714526](https://clinicaltrials.gov/study/NCT06714526) | N/A | Reclutando | 100 | Estudio piloto que compara selección de inhibidor P2Y12 guiada por genotipo frente a clopidogrel convencional en enfermedad arterial intracraneal sintomática (ICAD) |
| [NCT06058130](https://clinicaltrials.gov/study/NCT06058130) | N/A | Desconocido | 2171 | Compara anticoagulación sola vs. combinada con antiagregante en ictus isquémico agudo con fibrilación auricular no valvular y estenosis arterial extra/intracraneal |
| [NCT01732822](https://clinicaltrials.gov/study/NCT01732822) | Fase 3 | Completado | 13885 | EUCLID: compara ticagrelor con clopidogrel sobre muerte cardiovascular, IM e ictus isquémico en enfermedad arterial periférica |
| [NCT06857045](https://clinicaltrials.gov/study/NCT06857045) | N/A | Retirado | 0 | Comparaba 3 vs. 6 meses de doble antiagregación tras implante de stent intracraneal liberador de sirolimus (NOVA); estudio retirado sin datos |
| [NCT01813435](https://clinicaltrials.gov/study/NCT01813435) | Fase 3 | Completado | 15991 | GLOBAL LEADERS: ticagrelor monoterapia tras 1 mes de doble antiagregación vs. terapia estándar tras implante de stent coronario |
| [NCT07164859](https://clinicaltrials.gov/study/NCT07164859) | Fase 3 | Aún no reclutando | 1700 | SOLOPCI: doble antiagregación muy corta seguida de monoterapia con inhibidor P2Y12 en pacientes mayores tras ICP |
| [NCT02605447](https://clinicaltrials.gov/study/NCT02605447) | Fase 4 | Completado | 2009 | EVOLVE Short DAPT: seguridad de 3 meses de doble antiagregación en pacientes de alto riesgo hemorrágico tras ICP con stent SYNERGY |
| [NCT03620760](https://clinicaltrials.gov/study/NCT03620760) | Fase 4 | Desconocido | 2036 | Compara ticagrelor en dosis baja (45 mg) vs. estándar (90 mg) en angina inestable tras implante de stent liberador de fármaco |

---

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39862061](https://pubmed.ncbi.nlm.nih.gov/39862061/) | 2025 | ECA | Int J Stroke | Diseño del ensayo CAPTIVA, que compara anticoagulación vs. antiagregación dual en estenosis arterial intracraneal sintomática, buscando alternativas superiores a clopidogrel+aspirina |
| [38252758](https://pubmed.ncbi.nlm.nih.gov/38252758/) | 2024 | Revisión | Stroke | Actualización enfocada en arteriosclerosis intracraneal: introducción, aspectos destacados y vacíos de conocimiento |
| [39658130](https://pubmed.ncbi.nlm.nih.gov/39658130/) | 2025 | Cohorte | J Neurointerv Surg | Experiencia con ticagrelor 60 mg dos veces al día + aspirina 81 mg frente al régimen estándar aspirina+clopidogrel en stenting intracraneal |

---

## Informacion de Mercado en Espana

No hay autorizaciones registradas actualmente: el medicamento figura como **no comercializado** en España (0 autorizaciones), por lo que no existen productos ni indicaciones aprobadas que listar en esta sección.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad (no hay datos disponibles de advertencias, contraindicaciones ni interacciones farmacológicas en este evidence pack).

---

## Conclusion y Proximos Pasos

**Decision: Hold (Research Question)**

**Justificacion:**
La evidencia actual (nivel L2) se apoya principalmente en un ensayo Fase 3 pivotal aún en curso y sin resultados (CAPTIVA, NCT05047172) junto con estudios de contexto general (DAPT, SCA) no específicos de arteriosclerosis intracraneal. Es una hipótesis mecanísticamente razonable pero todavía no respaldada por resultados confirmatorios ni por datos de seguridad propios del fármaco.

**Para avanzar se necesita:**
- Resultados del ensayo CAPTIVA (finalización estimada 2027) y de DREAM-PRIDE (finalización estimada 2026)
- Ficha técnica TFDA/EMA con advertencias y contraindicaciones — actualmente vacío y marcado como **bloqueante** (DG001) para la evaluación de seguridad inicial
- Mecanismo de acción detallado desde DrugBank — actualmente vacío (DG002)
- Evaluación específica del riesgo de hemorragia intracraneal en esta población, dado que difiere del perfil de sangrado coronario ya conocido
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

