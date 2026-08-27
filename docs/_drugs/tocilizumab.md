---
layout: default
title: Tocilizumab
parent: 僅模型預測 (L5)
nav_order: 279
evidence_level: L5
indication_count: 10
---

# Tocilizumab
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

# Tocilizumab: De Artritis Reumatoide a Espondilitis Anquilosante

## Resumen en Una Frase

Tocilizumab es un anticuerpo monoclonal antagonista del receptor de IL-6, cuyo uso establecido según la literatura del paquete de evidencia es la artritis reumatoide (y otras artritis inflamatorias como la artritis idiopática juvenil).
El modelo TxGNN predice, con la puntuación más alta de todo el candidato, que podría ser efectivo para **Espondilitis Anquilosante**,
pero **9 ensayos clínicos** y **20 publicaciones** revisados revelan que esta hipótesis ya fue probada y **no se confirmó**: los dos ensayos de Fase 3 diseñados específicamente para esta indicación fueron terminados por falta de eficacia.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Artritis Reumatoide (uso establecido según literatura del paquete de evidencia; sin autorización registrada en España en este dataset) |
| Nueva Indicacion Predicha | Espondilitis Anquilosante |
| Puntaje de Prediccion TxGNN | 99.99% |
| Nivel de Evidencia | L1 (evidencia clínica directa, pero de **resultado negativo**) |
| Estado de Mercado en España | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos estructurados de DrugBank sobre el mecanismo de acción (campo `original_moa` marcado como vacío). Sin embargo, la literatura incluida en el paquete de evidencia describe consistentemente a tocilizumab como un anticuerpo monoclonal humanizado que bloquea el receptor de interleucina-6 (IL-6R), tanto en su forma soluble como unida a membrana (PMID 28841363, 19368420, 31875623). Su uso clínico establecido es la artritis reumatoide y otras artritis inflamatorias mediadas por IL-6, como la artritis idiopática juvenil sistémica y poliarticular.

La espondilitis anquilosante (EA) comparte con la artritis reumatoide el carácter de enfermedad reumática inflamatoria crónica, lo que constituye la base teórica de la predicción del modelo: si el bloqueo de IL-6 controla la inflamación en artritis reumatoide, podría hipotéticamente hacerlo en EA. Esta lógica de similitud mecanística es plausible a nivel de grafo de conocimiento y explica la puntuación TxGNN extremadamente alta (99.99%).

No obstante, esta hipótesis ya fue puesta a prueba clínicamente. La literatura de mecanismo (PMID 22452603) señala que la patología de la EA está dominada por el eje IL-17/TNF-α, con un papel secundario de IL-6, a diferencia de la artritis reumatoide. Esto es consistente con el resultado observado: dos ensayos clínicos de Fase 3 diseñados específicamente para EA (NCT01209702 y NCT01209689) fueron **terminados** por no alcanzar los criterios de eficacia esperados. Es decir, la evidencia real contradice directamente la predicción computacional, un hallazgo importante para la evaluación de este candidato.

---

## Evidencia de Ensayos Clinicos

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01209702](https://clinicaltrials.gov/study/NCT01209702) | Fase 2/3 | Terminado | 306 | RCT específico de EA (tocilizumab 8 mg/kg IV vs. placebo); **terminado por eficacia insuficiente** — resultado negativo directo |
| [NCT01209689](https://clinicaltrials.gov/study/NCT01209689) | Fase 3 | Terminado | 113 | RCT específico de EA en pacientes con respuesta inadecuada a anti-TNF; **terminado por eficacia insuficiente** — resultado negativo directo |
| [NCT05670301](https://clinicaltrials.gov/study/NCT05670301) | N/A | Reclutando | 2500 | Registro observacional multicéntrico de biomarcadores de citocinas en enfermedades inflamatorias sistémicas; no es un ensayo de eficacia |
| [NCT02569736](https://clinicaltrials.gov/study/NCT02569736) | N/A | Completado | 60 | Estudio mecanístico in vivo/in vitro sobre células T foliculares en artritis reumatoide tratada con tocilizumab; no específico de EA |
| [NCT01965132](https://clinicaltrials.gov/study/NCT01965132) | N/A | Reclutando | 10000 | Registro coreano de terapias biológicas en AR, EA y artritis psoriásica; observacional, sin hipótesis de eficacia |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Desconocido | 750000 | Estudio de riesgo de enfermedades inflamatorias inmunomediadas concomitantes en pacientes con biológicos; no específico de EA ni de tocilizumab |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Fase 2 | Aún no reclutando | 80 | Manejo perioperatorio de inmunosupresores en artroplastia de hombro en pacientes reumatológicos; no evalúa eficacia en EA |
| [NCT02925338](https://clinicaltrials.gov/study/NCT02925338) | N/A | Completado | 1431 | Observatorio de uso real de Inflectra (infliximab, no tocilizumab); incluido por indexación de búsqueda, sin relevancia directa |
| [NCT07477795](https://clinicaltrials.gov/study/NCT07477795) | Fase 2 | Aún no reclutando | 52 | Ensayo de secukinumab (no tocilizumab) en arteritis de Takayasu; sin relevancia directa para EA |

**Conclusión de esta tabla:** la única evidencia intervencionista específica de EA (2 ensayos de Fase 2/3 y Fase 3) es **negativa**.

---

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [23765873](https://pubmed.ncbi.nlm.nih.gov/23765873/) | 2014 | ECA | Annals of the Rheumatic Diseases | Ensayos BUILDER-1/BUILDER-2: evaluación de eficacia sintomática a corto plazo de tocilizumab en EA (evidencia primaria directa sobre el fármaco en esta indicación) |
| [26986130](https://pubmed.ncbi.nlm.nih.gov/26986130/) | 2016 | Revisión sistemática / metaanálisis en red | Medicine | Comparación de eficacia de terapias biológicas disponibles para EA mediante metaanálisis bayesiano en red |
| [20959960](https://pubmed.ncbi.nlm.nih.gov/20959960/) | 2011 | Cohorte | Osteoporosis International | Efectos óseos sistémicos de terapias biológicas en artritis reumatoide y EA |
| [33981717](https://pubmed.ncbi.nlm.nih.gov/33981717/) | 2021 | Reporte de caso | Frontiers in Medicine | Tratamiento exitoso de amiloidosis AA secundaria a EA con tocilizumab (2 casos) |
| [22452603](https://pubmed.ncbi.nlm.nih.gov/22452603/) | 2012 | Revisión | Inflammation & Allergy Drug Targets | Revisión del papel de IL-6 en EA: mecanismo secundario frente al eje IL-17/TNF-α |
| [29290076](https://pubmed.ncbi.nlm.nih.gov/29290076/) | 2018 | Metaanálisis | Clinical Rheumatology | Riesgo de infecciones graves con biológicos en EA axial y espondiloartritis axial no radiográfica |
| [21803631](https://pubmed.ncbi.nlm.nih.gov/21803631/) | 2011 | Revisión | Joint Bone Spine | Agentes biológicos para EA más allá de los antagonistas de TNF-α |
| [19822066](https://pubmed.ncbi.nlm.nih.gov/19822066/) | 2009 | Revisión | Clinical and Experimental Rheumatology | Diferencias de patogénesis y respuesta a biológicos entre artritis reumatoide y EA |
| [22450391](https://pubmed.ncbi.nlm.nih.gov/22450391/) | 2012 | Revisión | Current Opinion in Rheumatology | Alternativas de tratamiento en EA refractaria a inhibición de TNF |
| [27789989](https://pubmed.ncbi.nlm.nih.gov/27789989/) | 2009 | Revisión | Open Access Rheumatology | Revisión integral de biológicos disponibles en AR, EA y artritis psoriásica |

**Conclusión de esta tabla:** el único estudio de nivel ECA sobre tocilizumab específicamente en EA (PMID 23765873) evalúa eficacia a corto plazo, en línea con los resultados negativos de los ensayos de Fase 3 terminados; el resto de la literatura de mayor calidad (revisiones sistemáticas, metaanálisis) sitúa a IL-6 como mecanismo secundario en esta enfermedad.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se dispone actualmente de advertencias, contraindicaciones ni datos de interacción farmacológica (DDI) estructurados para este fármaco en el paquete de evidencia. Cabe destacar que la obtención del prospecto/etiquetado regulatorio (TFDA/AEMPS) está identificada como una **brecha de datos bloqueante** (DG001) que impide completar la evaluación de seguridad inicial (etapa S1).

---

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
A pesar de la puntuación TxGNN más alta observada en este candidato (99.99%), los dos únicos ensayos clínicos diseñados específicamente para probar tocilizumab en espondilitis anquilosante (Fase 2/3 y Fase 3, combinados >400 pacientes) fueron **terminados por falta de eficacia**. La literatura mecanística confirma que la patogénesis de la EA está dominada por el eje IL-17/TNF-α, con un rol secundario de IL-6, lo que explica este resultado negativo. La evidencia clínica directa contradice la predicción del modelo.

**Para avanzar se necesita:**
- Resolver la brecha bloqueante DG001 (advertencias/contraindicaciones del prospecto TFDA) antes de cualquier evaluación de seguridad S1
- Obtener el mecanismo de acción estructurado desde DrugBank (DG002)
- Dado el resultado clínico negativo, no se recomienda continuar el desarrollo de esta indicación específica
- Nota: dentro del mismo lote de predicciones para este fármaco, la indicación de rango 7 (artritis reumatoide juvenil poliarticular) presenta evidencia de Fase 3 positiva y ya es una indicación aprobada por FDA/EMA — podría ser un candidato de seguimiento más productivo que la espondilitis anquilosante
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

