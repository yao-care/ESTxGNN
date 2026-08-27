---
layout: default
title: Conestat Alfa
parent: 僅模型預測 (L5)
nav_order: 79
evidence_level: L5
indication_count: 10
---

# Conestat Alfa
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

# Conestat Alfa: De Angioedema Hereditario (indicación no confirmada en datos regulatorios) a Deficiencia del Inhibidor de C1

## Resumen en Una Frase

Los datos regulatorios de este paquete no confirman la indicación original de conestat alfa (campo marcado como vacío/Data Gap), aunque la evidencia clínica incluida en el propio paquete (decenas de ensayos sobre angioedema hereditario) indica que se trata de un inhibidor recombinante de la esterasa C1 humana usado en crisis de angioedema hereditario (HAE) por déficit de C1-INH.
El modelo TxGNN predice con **99.99%** de score que sería efectivo para **Deficiencia del Inhibidor de C1 (C1-INH)**, respaldado por **41 ensayos clínicos** (varios de Fase 3 completados) y **20 publicaciones**.
Sin embargo, esta "nueva" indicación coincide en gran medida con el uso ya establecido del fármaco — no representa, en sentido estricto, un reposicionamiento genuino.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | No registrada en los datos regulatorios de este paquete (Data Gap); la evidencia clínica incluida apunta a angioedema hereditario (HAE) por déficit de C1-INH |
| Nueva Indicacion Predicha | Deficiencia del Inhibidor de C1 (C1-INH) |
| Puntaje de Prediccion TxGNN | 99.99% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Proceed with Guardrails |

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción (campo `original_moa` marcado como Data Gap). Según la evidencia clínica incluida en este mismo paquete, conestat alfa es un inhibidor recombinante de la esterasa C1 humana (rhC1-INH, comercializado internacionalmente como Ruconest), cuya eficacia en el tratamiento de crisis agudas de angioedema hereditario (HAE) por déficit de C1-INH ha sido ampliamente demostrada en múltiples ensayos Fase 3.

La "nueva indicación" que predice TxGNN — deficiencia del inhibidor de C1 — es, desde el punto de vista fisiopatológico, esencialmente la misma entidad que el uso ya validado del fármaco: el HAE es la manifestación clínica de la deficiencia funcional o cuantitativa de C1-INH. Por tanto, la altísima puntuación del modelo (99.99%) probablemente refleja que esta asociación ya está presente en los datos de entrenamiento, más que un verdadero descubrimiento de reposicionamiento.

Como contraste, cabe destacar que otras indicaciones del listado (p. ej. "serpinopatía con polimerización tóxica de serpinas") obtuvieron puntuaciones igualmente altas pero sin ningún ensayo ni literatura de respaldo. El razonamiento del propio análisis indica que esa similitud probablemente proviene de que C1-INH pertenece a la superfamilia de serpinas a nivel de secuencia/estructura, no de un mecanismo terapéutico compartido — una limitación conocida de las predicciones basadas en grafos de conocimiento.

---

## Evidencia de Ensayos Clinicos

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00289211](https://clinicaltrials.gov/study/NCT00289211) | Fase 3 | Completado | 83 | Ensayo pivotal doble ciego controlado con placebo de C1INH-nf (conestat alfa) para crisis agudas de HAE |
| [NCT00438815](https://clinicaltrials.gov/study/NCT00438815) | Fase 3 | Completado | 113 | Estudio abierto de exposición repetida de C1INH-nf en crisis agudas de HAE (CHANGE 2) |
| [NCT06679426](https://clinicaltrials.gov/study/NCT06679426) | Fase 3 | Aún sin reclutar | 24 | Conestat alfa vs. placebo para angioedema inducido por IECA |
| [NCT02584959](https://clinicaltrials.gov/study/NCT02584959) | Fase 3 | Completado | 75 | C1 esterasa inhibidor subcutáneo (2000 UI) para prevención de crisis de angioedema |
| [NCT01188564](https://clinicaltrials.gov/study/NCT01188564) | Fase 3 | Completado | 75 | Confirmación de eficacia, seguridad e inmunogenicidad de rhC1INH (50 U/kg) en crisis agudas de HAE |
| [NCT00262301](https://clinicaltrials.gov/study/NCT00262301) | Fase 3 | Completado | 75 | RCT controlado con placebo de rhC1INH para crisis agudas de HAE |
| [NCT02316353](https://clinicaltrials.gov/study/NCT02316353) | Fase 3 | Completado | 126 | Seguridad y eficacia a largo plazo de C1-INH subcutáneo en profilaxis de HAE |
| [NCT00168103](https://clinicaltrials.gov/study/NCT00168103) | Fase 2/3 | Completado | 126 | C1 esterasa inhibidor pasteurizado en crisis abdominales/faciales de HAE congénita |
| [NCT05121376](https://clinicaltrials.gov/study/NCT05121376) | Fase 1/2 | Activo, sin reclutar | 44 | Terapia génica AAV5-SERPING1 (BMN 331) para HAE por déficit de C1-INH — mismo objetivo terapéutico, distinto fármaco |
| [NCT00914966](https://clinicaltrials.gov/study/NCT00914966) | Fase 4 | Completado | 20 | Escalada de dosis de C1-INH (CINRYZE) como profilaxis en HAE mal controlado |

---

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28754491](https://pubmed.ncbi.nlm.nih.gov/28754491/) | 2017 | ECA | Lancet | Ensayo cruzado Fase 2 controlado con placebo: eficacia de rhC1 esterasa inhibidor en profilaxis de HAE |
| [30021471](https://pubmed.ncbi.nlm.nih.gov/30021471/) | 2018 | Revisión | Expert Rev Clin Immunol | Revisión de conestat alfa como profilaxis para prevenir crisis en HAE |
| [22946752](https://pubmed.ncbi.nlm.nih.gov/22946752/) | 2012 | Revisión | BioDrugs | Síntesis de los dos ensayos pivotales aleatorizados de conestat alfa en crisis de HAE |
| [23420425](https://pubmed.ncbi.nlm.nih.gov/23420425/) | 2013 | Revisión sistemática | Pneumonol Alergol Pol | Comparación de eficacia clínica entre conestat alfa, C1INH humano e icatibant |
| [26106828](https://pubmed.ncbi.nlm.nih.gov/26106828/) | 2015 | Revisión/Guía | Curr Opin Allergy Clin Immunol | Manejo diagnóstico y terapéutico de HAE por déficit de C1-INH, experiencia italiana |
| [26250409](https://pubmed.ncbi.nlm.nih.gov/26250409/) | 2015 | Revisión | Immunotherapy | Terapia de reemplazo recombinante para HAE por déficit de C1-INH |
| [28687108](https://pubmed.ncbi.nlm.nih.gov/28687108/) | 2017 | Revisión/Guía | Immunol Allergy Clin North Am | Manejo agudo de crisis de angioedema hereditario |
| [29357215](https://pubmed.ncbi.nlm.nih.gov/29357215/) | 2018 | Revisión | Skin Therapy Lett | Nuevos tratamientos para angioedema hereditario |
| [24801469](https://pubmed.ncbi.nlm.nih.gov/24801469/) | 2014 | Serie de casos | Allergy Asthma Proc | Tratamiento domiciliario con conestat alfa en HAE por déficit de C1-INH, condiciones reales |
| [27940765](https://pubmed.ncbi.nlm.nih.gov/27940765/) | 2016 | Revisión | Pediatrics | Manejo de niños con HAE por déficit de inhibidor de C1 |

---

## Informacion de Mercado en España

Actualmente conestat alfa no tiene autorizaciones registradas en España (estado: no comercializado, 0 autorizaciones en los datos regulatorios de este paquete).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusion y Proximos Pasos

**Decision: Proceed with Guardrails**

**Justificacion:**
La evidencia clínica es sólida (nivel L1, múltiples ensayos Fase 3 completados) pero corresponde en gran medida al uso ya establecido del fármaco en HAE por déficit de C1-INH, no a un reposicionamiento nuevo. Además, faltan datos regulatorios críticos (advertencias, contraindicaciones e interacciones están marcadas como brecha de datos "Blocking"), lo que impide completar la evaluación inicial de seguridad (S1).

**Para avanzar se necesita:**
- Confirmar la indicación original real mediante el prospecto/ficha técnica oficial (AEMPS o equivalente), ya que el campo regulatorio está vacío
- Obtener advertencias, contraindicaciones e interacciones farmacológicas (actualmente sin datos)
- Obtener datos del mecanismo de acción (MOA) para fundamentar mejor el análisis de relación mecanística
- Clarificar si "Deficiencia del Inhibidor de C1" debe tratarse como reposicionamiento genuino o como confirmación del uso ya conocido, antes de avanzar en el pipeline de evaluación
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

