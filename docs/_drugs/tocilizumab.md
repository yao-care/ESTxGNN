---
layout: default
title: Tocilizumab
parent: Solo predicción del modelo (L5)
nav_order: 533
evidence_level: L5
indication_count: 10
---

# Tocilizumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Tocilizumab: Nueva Indicación Predicha en Espondilitis Anquilosante

## Resumen en Una Frase

Tocilizumab es un anticuerpo monoclonal humanizado contra el receptor de interleucina-6 (IL-6R). Según la literatura, se usa sobre todo en artritis reumatoide y artritis idiopática juvenil. El modelo TxGNN predice que podría ser efectivo para **espondilitis anquilosante**, pero la evidencia directa es débil: **2 ensayos de Fase 3 terminados anticipadamente** (sin resultados positivos confirmados en los datos aportados) y **19 publicaciones**, en su mayoría revisiones generales y casos aislados.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Espondilitis anquilosante |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L3 (ver nota) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 11 |
| Decisión Recomendada | Hold |

**Nota sobre el nivel de evidencia:** el Evidence Pack asigna L1. Sin embargo, los dos ECAs de Fase 3 (NCT01209702 y NCT01209689) figuran como **terminados**, no completados, y L1 exige ≥2 ECAs de Fase 3 completados. Por eso se asigna L3, apoyado en una revisión sistemática con metaanálisis en red y en metaanálisis de seguridad.

Los registros de AEMPS no incluyen texto de indicación aprobada, por lo que no se puede indicar la indicación original.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la literatura aportada, tocilizumab es un anticuerpo monoclonal humanizado que bloquea el receptor de IL-6, tanto el de membrana como el soluble. Su eficacia está comprobada en artritis reumatoide, artritis idiopática juvenil y arteritis de células gigantes.

La IL-6 se ha implicado, junto con el TNF-α y la IL-10, en la patogenia de la espondilitis anquilosante (revisión PMID 22452603). Por eso el bloqueo de IL-6 es biológicamente plausible en la inflamación axial. Esto explica en parte la alta puntuación del modelo.

Sin embargo, la evidencia clínica no acompaña esa plausibilidad. La literatura señala que la artritis reumatoide y la espondilitis anquilosante difieren claramente en su patogenia (PMID 19822066). Los dos ensayos de Fase 3 en espondilitis anquilosante se terminaron anticipadamente. Según el análisis del Evidence Pack, el programa BUILDER publicado no mostró una señal clara de eficacia, pero los datos aportados no lo confirman.

---

## Evidencia de Ensayos Clínicos

Solo dos de los ocho ensayos evalúan directamente tocilizumab en espondilitis anquilosante. El resto son estudios observacionales, registros o estudios de contexto.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01209702](https://clinicaltrials.gov/study/NCT01209702) | Fase 3 (2/3) | Terminado | 306 | ECA doble ciego frente a placebo de tocilizumab 8 mg/kg IV en EA sin respuesta a AINE y sin exposición previa a anti-TNF. Terminado anticipadamente |
| [NCT01209689](https://clinicaltrials.gov/study/NCT01209689) | Fase 3 | Terminado | 113 | ECA doble ciego frente a placebo (8 mg/kg o 4 mg/kg IV) en EA con respuesta inadecuada a anti-TNF. Terminado anticipadamente |
| [NCT07477795](https://clinicaltrials.gov/study/NCT07477795) | Fase 2 | Aún sin reclutar | 52 | ECA bayesiano de secukinumab en arteritis de Takayasu activa grave. Relación indirecta |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Fase 2 | Aún sin reclutar | 80 | Manejo perioperatorio de inmunosupresores en pacientes reumatológicos con artroplastia de hombro. No evalúa eficacia en EA |
| [NCT02925338](https://clinicaltrials.gov/study/NCT02925338) | N/A | Completado | 1431 | Observatorio de uso real de infliximab biosimilar (Inflectra). No aporta evidencia sobre tocilizumab |
| [NCT05670301](https://clinicaltrials.gov/study/NCT05670301) | N/A | Reclutando | 2500 | Registro de biomarcadores y perfiles de citocinas en enfermedades inflamatorias sistémicas |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Desconocido | 750000 | Estudio poblacional del riesgo de nuevas enfermedades inmunomediadas con biológicos |
| [NCT01965132](https://clinicaltrials.gov/study/NCT01965132) | N/A | Reclutando | 10000 | Registro coreano de biológicos en AR, EA y artritis psoriásica, centrado en seguridad |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [23765873](https://pubmed.ncbi.nlm.nih.gov/23765873/) | 2014 | ECAs (BUILDER-1 y -2) | Ann Rheum Dis | Evalúa la eficacia sintomática a corto plazo de tocilizumab en EA. El resumen disponible solo indica el objetivo, sin resultados |
| [26986130](https://pubmed.ncbi.nlm.nih.gov/26986130/) | 2016 | Revisión sistemática y metaanálisis en red | Medicine | Compara la eficacia de los biológicos disponibles para EA a partir de ECAs |
| [29290076](https://pubmed.ncbi.nlm.nih.gov/29290076/) | 2018 | Metaanálisis (seguridad) | Clin Rheumatol | Riesgo de infecciones graves con biológicos en EA y espondiloartritis axial no radiográfica |
| [22452603](https://pubmed.ncbi.nlm.nih.gov/22452603/) | 2012 | Revisión | Inflamm Allergy Drug Targets | Papel de la IL-6 en la EA y del bloqueo de IL-6 como opción terapéutica |
| [22450391](https://pubmed.ncbi.nlm.nih.gov/22450391/) | 2012 | Revisión | Curr Opin Rheumatol | Alternativas terapéuticas en EA refractaria a anti-TNF |
| [21803631](https://pubmed.ncbi.nlm.nih.gov/21803631/) | 2011 | Revisión | Joint Bone Spine | Biológicos para EA más allá de los antagonistas del TNFα |
| [28413099](https://pubmed.ncbi.nlm.nih.gov/28413099/) | 2017 | Observacional/revisión | Semin Arthritis Rheum | Optimización de la segunda línea de biológicos en AR, artritis psoriásica y EA |
| [33981717](https://pubmed.ncbi.nlm.nih.gov/33981717/) | 2021 | Reporte de casos | Front Med | Dos casos de amiloidosis AA en EA tratados con tocilizumab, con evolución favorable |
| [31852268](https://pubmed.ncbi.nlm.nih.gov/31852268/) | 2020 | Revisión | Expert Rev Clin Immunol | Riesgo de infección con fármacos no biológicos frente a biológicos en artritis inflamatoria |
| [39963138](https://pubmed.ncbi.nlm.nih.gov/39963138/) | 2025 | Revisión | Front Immunol | Manejo del riesgo, cribado y prevención de tuberculosis con inmunosupresores en artritis autoinmune |

---

## Información de Mercado en España

Se muestran 5 de las 11 autorizaciones registradas.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 08492001 | ROACTEMRA 20 mg/ml, concentrado para solución para perfusión | Solución inyectable |
| 08492003 | ROACTEMRA 20 mg/ml, concentrado para solución para perfusión | Solución inyectable |
| 1241825001 | Tocilizumab Stada 20 mg/ml, concentrado para solución para perfusión | Concentrado para solución para perfusión |
| 1241896010 | Avtozma 162 mg, solución inyectable en pluma precargada | Solución inyectable en pluma precargada |
| 1231754007 | Tyenne 162 mg, solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada |

El texto de indicación aprobada no figura en el registro; debe consultarse la ficha técnica en AEMPS.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- La puntuación de TxGNN es muy alta (99.99%) y el bloqueo de IL-6 es biológicamente plausible. Sin embargo, los dos ECAs de Fase 3 en espondilitis anquilosante se terminaron anticipadamente y no hay resultados positivos confirmados en los datos aportados.
- La literatura específica en EA se limita a revisiones generales y a casos aislados.

**Para avanzar se necesita:**
- Obtener y revisar los resultados completos de los ensayos NCT01209702 y NCT01209689 (programa BUILDER) y confirmar el motivo de la terminación anticipada.
- Descargar y analizar la ficha técnica de AEMPS para completar advertencias, contraindicaciones e indicaciones autorizadas (bloqueante para el cribado de seguridad).
- Completar los datos de mecanismo de acción desde DrugBank.
- Comparar con las alternativas ya establecidas en EA (anti-TNF e inhibidores de IL-17) antes de reconsiderar la indicación.

**Nota adicional:** entre las demás predicciones, la artritis idiopática juvenil poliarticular tiene respaldo de Fase 3 completado (NCT00988221). Tocilizumab ya es un tratamiento establecido en esa indicación, por lo que no constituye un reposicionamiento genuino.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

