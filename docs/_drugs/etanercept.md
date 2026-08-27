---
layout: default
title: Etanercept
parent: 僅模型預測 (L5)
nav_order: 112
evidence_level: L5
indication_count: 6
---

# Etanercept
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

Ya reviso el Evidence Pack (candidato multi-indicación TW-DB00005-multi, Etanercept). Nota importante antes del informe: este Evidence Pack contiene **6 indicaciones predichas por TxGNN**, no solo una, con niveles de evidencia muy dispares (desde L1 con ensayos Fase 3 completados, hasta L5 sin ningún estudio real). Aplicar el formato de una sola indicación de forma literal ocultaría información crítica (dos candidatos con evidencia sólida y dos con "ruido" de modelo sin ninguna base clínica), así que adapto la estructura para cubrir el conjunto de forma honesta, manteniendo el orden de secciones solicitado.

---

# Etanercept: Evaluación de Múltiples Indicaciones Predichas por TxGNN

## Resumen en Una Frase

Etanercept es una proteína de fusión inhibidora del TNF-alfa, ampliamente utilizada en otros mercados para artritis reumatoide y enfermedades inflamatorias relacionadas, aunque actualmente **no está comercializada en España** según los registros consultados.
El modelo TxGNN predijo **6 posibles nuevas indicaciones**, pero la calidad de la evidencia varía radicalmente: dos candidatos (**espondilopatía inflamatoria** y **artritis reumatoide juvenil poliarticular**) cuentan con **evidencia de Nivel 1** (múltiples ensayos Fase 3 completados) y en realidad corresponden a usos ya aprobados en otros países, mientras que otros dos (hipermovilidad del cóccix, enfermedad de Kummell) carecen por completo de base clínica o mecanística.
En conjunto, la puntuación TxGNN por sí sola **no es un indicador fiable de plausibilidad clínica** en este candidato — se requiere revisar caso por caso.

---

## Resumen Rápido

**Información General del Fármaco**

| Ítem | Contenido |
|------|------|
| Indicación Original (conocida) | Enfermedades inflamatorias mediadas por TNF-alfa (artritis reumatoide y afines); no hay indicación aprobada registrada en España en este Evidence Pack |
| Mecanismo de Acción | No disponible en detalle en esta ficha (ver sección siguiente) |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |

**Ranking de Indicaciones Predichas por TxGNN**

| Rango | Indicación Predicha | Puntaje TxGNN | Nivel de Evidencia | Etapa de Decisión | Recomendación |
|------|------|------|------|------|------|
| 1 | Vasculitis reumatoide | 99.71% | L4 | S1 | **Hold** |
| 2 | Hipermovilidad del cóccix | 99.63% | L5 | S0 | **Hold** |
| 3 | Espondilopatía inflamatoria | 99.57% | L1 | S3 | **Proceed with Guardrails** |
| 4 | Enfermedad de Kummell | 99.55% | L5 | S0 | **Hold** |
| 5 | Artritis reumatoide juvenil poliarticular | 99.50% | L1 | S3 | **Proceed with Guardrails** |
| 6 | Enfermedad vertebral | 99.16% | L2 | S2 | **Research Question** |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en esta ficha de evidencia. Según la información conocida de forma general, Etanercept es una proteína de fusión del receptor soluble de TNF (TNFR:Fc), que se une al TNF-alfa circulante y bloquea su actividad biológica; es una de las moléculas fundadoras de la clase de "inhibidores de TNF", con uso extendido en otros mercados para artritis reumatoide, artritis idiopática juvenil, espondilitis anquilosante, artritis psoriásica y psoriasis en placas.

Con esa base mecanística, los 6 candidatos se dividen en tres grupos claramente diferenciados:

**Grupo A — Redescubrimiento de indicaciones ya establecidas (evidencia fuerte):** *Espondilopatía inflamatoria* y *Artritis reumatoide juvenil poliarticular* son, en la práctica, variantes de indicaciones para las que Etanercept ya tiene aprobación regulatoria en otros países (espondilitis anquilosante/espondiloartritis axial, y JIA poliarticular desde 1999). El TNF-alfa es el motor patogénico central en ambas enfermedades (entesitis/sacroileítis en la primera, sinovitis poliarticular en la segunda), por lo que el bloqueo de TNF tiene justificación mecanística directa y ya validada clínicamente. No se trata de una hipótesis nueva, sino de una confirmación del modelo.

**Grupo B — Señal contradictoria/paradójica (evidencia débil o negativa):** Para *vasculitis reumatoide*, la literatura muestra una relación **paradójica**: en vez de tratar la vasculitis, los anti-TNF (incluido etanercept) se han asociado a la **inducción** de vasculitis cutánea, nefropatía y fenómenos autoinmunes por depósito de inmunocomplejos o desregulación de interferón-alfa. El ensayo clave en la indicación más cercana (granulomatosis de Wegener/vasculitis asociada a ANCA, NCT00001901) fue negativo y mostró señales de seguridad desfavorables. Es decir, el mecanismo teórico (TNF participa en la inflamación vascular) apunta en una dirección, pero la evidencia clínica observada apunta en la contraria.

**Grupo C — Ruido de embedding, sin base clínica:** *Hipermovilidad del cóccix* y *Enfermedad de Kummell* son patologías mecánicas/estructurales (trauma, necrosis avascular postfractura vertebral) sin componente inflamatorio mediado por TNF. No existe ningún estudio clínico ni justificación mecanística; se consideran artefactos del espacio de embeddings del grafo de conocimiento, no candidatos reales.

*Enfermedad vertebral* (Grupo intermedio) es un término demasiado amplio: si se refiere a afectación vertebral de origen inflamatorio (solapando con espondilopatía inflamatoria) el mecanismo es válido; si incluye patología vertebral no inflamatoria, no lo es. Requiere aclarar la definición antes de avanzar.

---

## Evidencia de Ensayos Clínicos

### Espondilopatía inflamatoria (Grupo A — evidencia más sólida)

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00434044](https://clinicaltrials.gov/study/NCT00434044) | Fase 3 | Completado | 150 | RCT doble ciego controlado con placebo, primer estudio de etanercept en espondilitis anquilosante (EA) en pacientes chinos |
| [NCT00420238](https://clinicaltrials.gov/study/NCT00420238) | Fase 4 | Completado | 82 | RCT multicéntrico doble ciego, etanercept en EA axial activa, severa y avanzada |
| [NCT02364479](https://clinicaltrials.gov/study/NCT02364479) | Fase 4 | Completado | 150 | RCT doble ciego de proteína de fusión TNFR-II:Fc (misma familia molecular) en espondiloartritis axial activa |
| [NCT01258738](https://clinicaltrials.gov/study/NCT01258738) | Fase 3 | Completado | 225 | RCT doble ciego de etanercept vs. placebo en espondiloartritis axial no radiográfica, con extensión abierta de 92 semanas |
| [NCT00418548](https://clinicaltrials.gov/study/NCT00418548) | Fase 3 | Completado | 350 | RCT comparando etanercept 50mg semanal vs. 25mg dos veces por semana en EA |
| [NCT00844142](https://clinicaltrials.gov/study/NCT00844142) | Fase 2 | Desconocido | 80 | RCT etanercept vs. sulfasalazina en espondiloartritis axial temprana, evaluación por RM |
| [NCT00247962](https://clinicaltrials.gov/study/NCT00247962) | Fase 4 | Completado | 566 | RCT doble ciego comparando etanercept y sulfasalazina en EA |
| [NCT00317499](https://clinicaltrials.gov/study/NCT00317499) | Fase 3 | Completado | 205 | RCT doble ciego controlado con placebo en artritis psoriásica y psoriasis (familia de espondiloartropatías) |
| [NCT01610947](https://clinicaltrials.gov/study/NCT01610947) | N/A | Completado | 398 | RCT sobre espaciado de dosis de anti-TNF en espondiloartritis con baja actividad estable |
| [NCT02456363](https://clinicaltrials.gov/study/NCT02456363) | Fase 2 | Desconocido | 300 | Registro de terapia anti-TNF (incluye adalimumab) en EA, seguridad y eficacia |

### Artritis reumatoide juvenil poliarticular (Grupo A)

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03780959](https://clinicaltrials.gov/study/NCT03780959) | Fase 2/3 | Completado | 69 | Estudio pivotal original: seguridad, farmacocinética poblacional y eficacia de etanercept en JRA poliarticular |
| [NCT03781375](https://clinicaltrials.gov/study/NCT03781375) | Fase 3 | Terminado | 25 | RCT doble ciego comparando etanercept+metotrexato vs. metotrexato solo |
| [NCT02840175](https://clinicaltrials.gov/study/NCT02840175) | Fase 3 | Completado | 62 | RCT de reducción de tratamiento en JIA oligoarticular/poliarticular FR-negativa con enfermedad inactiva |
| [NCT07386587](https://clinicaltrials.gov/study/NCT07386587) | Fase 3 | Reclutamiento por invitación | 60 | RCT abierto comparando metotrexato solo vs. metotrexato+etanercept para actividad mínima/baja de enfermedad |
| [NCT00078793](https://clinicaltrials.gov/study/NCT00078793) | Fase 4 | Completado | 600 | Registro de seguridad a largo plazo de etanercept en JRA poliarticular/sistémica |
| [NCT06654882](https://clinicaltrials.gov/study/NCT06654882) | Fase 3 | Reclutando | 400 | Ensayo multibrazo de medicamentos secuenciales tras fallo de TNFi en JIA |
| [NCT01145352](https://clinicaltrials.gov/study/NCT01145352) | N/A | Completado | 113 | Vigilancia post-comercialización de Enbrel en JIA activa poliarticular |
| [NCT06413563](https://clinicaltrials.gov/study/NCT06413563) | N/A | Aún no reclutando | 75 | Análisis de biomarcadores linfocitarios por subtipo de JIA y terapia (estudio mecanístico) |

### Enfermedad vertebral (Grupo intermedio — definición ambigua)

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01258738](https://clinicaltrials.gov/study/NCT01258738) | Fase 3 | Completado | 225 | RCT etanercept vs. placebo en espondiloartritis axial no radiográfica |
| [NCT01188655](https://clinicaltrials.gov/study/NCT01188655) | N/A | Completado | 89 | Estudio observacional de Enbrel en EA en vida real |
| [NCT05115903](https://clinicaltrials.gov/study/NCT05115903) | Fase 4 | Desconocido | 15 | RCT de reducción escalonada de TNFi en espondiloartritis axial |
| [NCT02809781](https://clinicaltrials.gov/study/NCT02809781) | Fase 2/3 | Desconocido | 250 | Comparación de células madre mesenquimales vs. etanercept en EA (intervención distinta) |
| [NCT01400516](https://clinicaltrials.gov/study/NCT01400516) | Fase 4 | Completado | 26 | Teriparatide (no etanercept) para erosiones articulares en artritis reumatoide — baja relevancia directa |
| [NCT00413400](https://clinicaltrials.gov/study/NCT00413400) | N/A | Completado | 40 | Etanercept en síndrome metabólico — sin relación con enfermedad vertebral |

### Vasculitis reumatoide (Grupo B — señal contradictoria)

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00001901](https://clinicaltrials.gov/study/NCT00001901) | Fase 1/2 | Completado | 60 | Ensayo WGET: etanercept en granulomatosis de Wegener (vasculitis ANCA); **resultado negativo**, no mejoró mantenimiento de remisión y aumentó señal de neoplasia |
| [NCT01557322](https://clinicaltrials.gov/study/NCT01557322) | N/A | Completado | 1754 | Estudio observacional de vías de tratamiento en AR moderada (no específico de vasculitis) |
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | Completado | 808 | Estudio transversal de patrones de tratamiento en AR con DMARDs biológicos |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completado | 184 | Estudio no intervencionista de tocilizumab en AR (no etanercept) |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Desconocido | 750000 | Estudio observacional de riesgo de enfermedades inflamatorias inmunomediadas concurrentes con biológicos |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Fase 2 | Aún no reclutando | 80 | Manejo perioperatorio de inmunosupresores en artroplastia de hombro (indirecto) |

### Hipermovilidad del cóccix y Enfermedad de Kummell (Grupo C)

Actualmente no hay ensayos clínicos relacionados registrados para ninguna de las dos indicaciones — consistente con la ausencia de base mecanística.

---

## Evidencia de Literatura

### Espondilopatía inflamatoria

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28837372](https://pubmed.ncbi.nlm.nih.gov/28837372/) | 2018 | Revisión | Modern Rheumatology | Actualización de eficacia y seguridad de etanercept en espondiloartritis y JIA |
| [28682112](https://pubmed.ncbi.nlm.nih.gov/28682112/) | 2017 | Revisión | Expert Opin Biol Ther | Revisión sistemática de eficacia y tolerancia de etanercept en espondiloartritis axial |
| [28434410](https://pubmed.ncbi.nlm.nih.gov/28434410/) | 2017 | Meta-análisis | Int J Technol Assess Health Care | Meta-análisis de dosis y duración óptima de etanercept en EA |
| [17072572](https://pubmed.ncbi.nlm.nih.gov/17072572/) | 2006 | Revisión | Z Rheumatol | Revisión general de espondiloartritis, incluida EA |
| [18208819](https://pubmed.ncbi.nlm.nih.gov/18208819/) | 2008 | Coste-efectividad | Rheumatology (Oxford) | Análisis coste-efectividad de infliximab, etanercept y adalimumab en EA (guía NICE) |
| [36752358](https://pubmed.ncbi.nlm.nih.gov/36752358/) | 2023 | Cohorte | Arthritis Care Res | Impacto de políticas de biosimilares sobre uso de etanercept e infliximab |
| [24980068](https://pubmed.ncbi.nlm.nih.gov/24980068/) | 2015 | Revisión | Rheumatol Int | Revisión de biosimilares de etanercept |
| [39734351](https://pubmed.ncbi.nlm.nih.gov/39734351/) | 2024 | Revisión | Turk J Med Sci | Inmunogenicidad y reacciones de hipersensibilidad a anti-TNF (incl. etanercept) |
| [28940172](https://pubmed.ncbi.nlm.nih.gov/28940172/) | 2017 | Revisión | BioDrugs | GP2015, biosimilar de etanercept, aprobado para las mismas indicaciones |
| [25438042](https://pubmed.ncbi.nlm.nih.gov/25438042/) | 2015 | Revisión | Curr Med Res Opin | Etanercept y uveítis: relación ambivalente |

### Artritis reumatoide juvenil poliarticular

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10717011](https://pubmed.ncbi.nlm.nih.gov/10717011/) | 2000 | ECA | N Engl J Med | **Ensayo pivotal** (Lovell et al.) que estableció la eficacia y seguridad de etanercept en JRA poliarticular refractaria a metotrexato |
| [11246677](https://pubmed.ncbi.nlm.nih.gov/11246677/) | 2001 | Cohorte | J Rheumatol | Respuesta clínica a etanercept en JRA de curso poliarticular |
| [40148850](https://pubmed.ncbi.nlm.nih.gov/40148850/) | 2025 | Estudio comparativo | BMC Pediatrics | Comparación de eficacia y seguridad entre etanercept y adalimumab en pJIA |
| [28418334](https://pubmed.ncbi.nlm.nih.gov/28418334/) | 2017 | Revisión | Balkan Med J | Revisión general de artritis idiopática juvenil y subtipos |
| [12641492](https://pubmed.ncbi.nlm.nih.gov/12641492/) | 2003 | Revisión | BioDrugs | Uso de etanercept en AR, artritis psoriásica y JRA |
| [12421111](https://pubmed.ncbi.nlm.nih.gov/12421111/) | 2002 | Revisión | Drugs | Revisión actualizada de etanercept en AR/PsA/JRA |
| [29781829](https://pubmed.ncbi.nlm.nih.gov/29781829/) | 2019 | Cohorte | J Clin Rheumatol | Comparación de adultos con pJIA vs. AR: características clínicas y uso de medicación |
| [38204313](https://pubmed.ncbi.nlm.nih.gov/38204313/) | 2023 | Revisión | Turk J Pediatr | Elección y cambio de biológicos en JIA según subtipo |
| [26233720](https://pubmed.ncbi.nlm.nih.gov/26233720/) | 2015 | Revisión | Clin Rheumatol | Artritis relacionada con entesitis, subtipo de JIA |
| [20444859](https://pubmed.ncbi.nlm.nih.gov/20444859/) | 2010 | Estudio prospectivo | Rheumatology (Oxford) | Etanercept mejora crecimiento lineal y masa ósea en pJIA resistente a MTX |

### Enfermedad vertebral

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31969328](https://pubmed.ncbi.nlm.nih.gov/31969328/) | 2020 | Guía | Ann Rheum Dis | Recomendaciones EULAR 2019 para el manejo de AR con DMARDs biológicos |
| [41826212](https://pubmed.ncbi.nlm.nih.gov/41826212/) | 2026 | Guía | Ann Rheum Dis | Actualización 2025 de recomendaciones EULAR para AR |
| [38503473](https://pubmed.ncbi.nlm.nih.gov/38503473/) | 2024 | Revisión Sistemática | Ann Rheum Dis | Revisión sistemática que informa las recomendaciones EULAR 2023 para artritis psoriásica |
| [28682112](https://pubmed.ncbi.nlm.nih.gov/28682112/) | 2017 | Revisión | Expert Opin Biol Ther | Etanercept en espondiloartritis axial (relevante por solapamiento) |
| [35543102](https://pubmed.ncbi.nlm.nih.gov/35543102/) | 2023 | Cohorte | Scand J Rheumatol | Seguimiento a 3 años de curso corto de etanercept en espondiloartritis axial no radiográfica sospechada |
| [24101863](https://pubmed.ncbi.nlm.nih.gov/24101863/) | 2013 | Cohorte | Patient Prefer Adherence | Seguridad y eficacia a largo plazo de etanercept en EA |
| [40015358](https://pubmed.ncbi.nlm.nih.gov/40015358/) | 2025 | Cohorte | Joint Bone Spine | Predictores clínicos/ecográficos de actividad tras espaciado de anti-TNF en artritis psoriásica |
| [29624303](https://pubmed.ncbi.nlm.nih.gov/29624303/) | 2016 | Revisión | Reumatizam | Espondiloartritis juvenil |
| [17072572](https://pubmed.ncbi.nlm.nih.gov/17072572/) | 2006 | Revisión | Z Rheumatol | Espondiloartritis, incluida afectación vertebral inflamatoria |
| [20554241](https://pubmed.ncbi.nlm.nih.gov/20554241/) | 2010 | Revisión | Joint Bone Spine | Artritis reumatoide de inicio tardío |

### Vasculitis reumatoide (evidencia predominantemente de alerta de seguridad)

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Revisión Sistemática | Clin Rheumatol | Revisión sistemática de terapia biológica en vasculitis reumatoide |
| [28391344](https://pubmed.ncbi.nlm.nih.gov/28391344/) | 2017 | Revisión | Nephrol Dial Transplant | Papel del bloqueo de TNF-alfa en vasculitis asociada a ANCA y glomerulonefritis |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Cohorte | RMD Open | Riesgo específico por fármaco de eventos tipo lupus/vasculitis con TNFi en AR (BSRBR-RA) |
| [15468348](https://pubmed.ncbi.nlm.nih.gov/15468348/) | 2004 | Revisión | J Rheumatol | Bloqueo de TNF-alfa y riesgo de vasculitis |
| [31668853](https://pubmed.ncbi.nlm.nih.gov/31668853/) | 2019 | ECA | Biologicals | Comparación de eficacia/seguridad entre etanercept original y biosimilar en AR |
| [38931826](https://pubmed.ncbi.nlm.nih.gov/38931826/) | 2024 | Simulación PK | Pharmaceutics | Simulación farmacocinética poblacional de biosimilares de etanercept/adalimumab |
| [31632872](https://pubmed.ncbi.nlm.nih.gov/31632872/) | 2019 | Caso clínico | Cureus | Nefropatía asociada a etanercept |
| [15853915](https://pubmed.ncbi.nlm.nih.gov/15853915/) | 2005 | Caso clínico | Scand J Immunol | Vasculitis cutánea asociada a etanercept e infliximab |
| [12209493](https://pubmed.ncbi.nlm.nih.gov/12209493/) | 2002 | Caso clínico | Arthritis Rheum | Nodulosis y vasculitis acelerada tras terapia con etanercept |
| [41327089](https://pubmed.ncbi.nlm.nih.gov/41327089/) | 2025 | Caso clínico | BMC Nephrol | Paciente con AR que desarrolló nefropatía membranosa y vasculitis ANCA sucesivamente |

### Hipermovilidad del cóccix y Enfermedad de Kummell

Actualmente no hay literatura relacionada disponible para ninguna de las dos indicaciones.

---

## Información de Mercado en España

Etanercept **no se encuentra actualmente comercializado en España** según los registros consultados (0 autorizaciones registradas). No hay información de licencias, nombres de producto ni formas farmacéuticas disponibles en esta ficha de evidencia.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad — no hay advertencias, contraindicaciones ni interacciones farmacológicas registradas en esta ficha de evidencia.

**Nota relevante extraída de la propia evidencia clínica (no de la ficha de seguridad):** en el candidato "vasculitis reumatoide", múltiples reportes de caso y un estudio de cohorte (BSRBR-RA) documentan que los anti-TNF, incluido etanercept, pueden **inducir** vasculitis cutánea, nefropatía y fenómenos tipo lupus. Esto debería considerarse una señal de seguridad relevante independientemente del vacío de datos del prospecto.

---

## Conclusión y Próximos Pasos

Dado que este candidato agrupa 6 indicaciones con perfiles de evidencia muy distintos, la decisión se presenta por indicación:

**1. Espondilopatía inflamatoria — Decisión: Proceed with Guardrails**
**Justificación:** Evidencia de Nivel 1 con múltiples ECA Fase 3 completados; corresponde a un uso ya validado del TNF-alfa en espondiloartritis/EA en otros mercados. El principal guardrail es diferenciar la subpoblación radiográfica (EA) de la no radiográfica (nr-axSpA).

**2. Artritis reumatoide juvenil poliarticular — Decisión: Proceed with Guardrails**
**Justificación:** Evidencia de Nivel 1, incluyendo el ensayo pivotal original (Lovell et al., NEJM 2000) que sustentó la aprobación histórica de etanercept en JIA. Guardrail: ajuste de dosis pediátrica y monitorización de infecciones/neoplasias a largo plazo.

**3. Vasculitis reumatoide — Decisión: Hold**
**Justificación:** La evidencia disponible es contradictoria y mayoritariamente de seguridad negativa (inducción de vasculitis/nefropatía, ensayo clave WGET negativo). No se recomienda avanzar sin una revisión de farmacovigilancia dedicada.

**4. Enfermedad vertebral — Decisión: Research Question**
**Justificación:** Evidencia de Nivel 2 pero definición de la indicación ambigua y con solapamiento sustancial con "espondilopatía inflamatoria". No se puede tomar una decisión de avance hasta aclarar el fenotipo objetivo.

**5. Hipermovilidad del cóccix — Decisión: Hold**
**Justificación:** Sin ningún ensayo clínico, literatura ni justificación mecanística. Se interpreta como ruido del espacio de embeddings de TxGNN.

**6. Enfermedad de Kummell — Decisión: Hold**
**Justificación:** Patología de origen vascular/mecánico postraumático, sin componente inflamatorio mediado por TNF. Sin ningún soporte clínico. Se recomienda descartar.

**Para avanzar se necesita (aplica a todos los candidatos):**
- Confirmación del estado regulatorio real en España/AEMPS (esta ficha indica 0 autorizaciones, lo cual debería verificarse dado que Etanercept es un biológico ampliamente comercializado en otros mercados europeos bajo otras marcas)
- Datos del prospecto TFDA/AEMPS (advertencias, contraindicaciones, interacciones) — actualmente ausentes
- Datos detallados de mecanismo de acción (MOA) desde DrugBank
- Para los candidatos "Proceed with Guardrails": definición precisa de la subpoblación diana y plan de farmacovigilancia específico
- Para "Enfermedad vertebral": aclarar la definición clínica exacta antes de continuar la evaluación
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

