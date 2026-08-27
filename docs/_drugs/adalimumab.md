---
layout: default
title: Adalimumab
parent: 僅模型預測 (L5)
nav_order: 13
evidence_level: L5
indication_count: 6
---

# Adalimumab
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

# Adalimumab: De Artritis Reumatoide a Vasculitis Reumatoide

## Resumen en Una Frase

Adalimumab es un anticuerpo monoclonal anti-TNF-α, ampliamente conocido por su uso original en el tratamiento de la artritis reumatoide y otras enfermedades inflamatorias autoinmunes.
El modelo TxGNN predice que podría ser relevante para **Vasculitis Reumatoide**,
con **5 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección — si bien la evidencia disponible es mixta e incluye señales de seguridad contradictorias (casos documentados de vasculitis inducida por el propio fármaco).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Artritis Reumatoide (información general conocida sobre el fármaco; no se dispone de datos formales de indicación aprobada en el mercado evaluado) |
| Nueva Indicación Predicha | Vasculitis Reumatoide |
| Puntaje de Predicción TxGNN | 99.80% |
| Nivel de Evidencia | L3 |
| Estado de Mercado | No Comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, adalimumab es un anticuerpo monoclonal completamente humano dirigido contra el TNF-α (factor de necrosis tumoral alfa), que bloquea esta citocina proinflamatoria clave. Su eficacia en artritis reumatoide y otras artropatías inflamatorias ha sido ampliamente comprobada, y mecanísticamente podría ser aplicable a la vasculitis reumatoide.

La vasculitis reumatoide es una de las manifestaciones extraarticulares más graves de la artritis reumatoide, mediada por complejos inmunes y asociada a las mismas vías inflamatorias impulsadas por TNF-α. En teoría, esto respalda la hipótesis de que un inhibidor de TNF-α podría ser beneficioso en esta indicación.

Sin embargo, la literatura disponible muestra señales contradictorias: varios reportes de caso documentan que adalimumab puede **inducir o coexistir con** vasculitis leucocitoclástica y eventos tipo lupus (la llamada "paradoja anti-TNF"), mientras que otro grupo de reportes describe una respuesta favorable de la vasculitis digital al tratamiento con adalimumab. No existe consenso mecanístico claro, por lo que esta predicción debe interpretarse como una **señal de seguridad a esclarecer**, más que como evidencia sólida de eficacia.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completado | 184 | Estudio observacional multinacional en pacientes con AR tratados con tocilizumab tras respuesta inadecuada a DMARDs; ofrece datos de seguridad de contexto en la misma población de biológicos, sin foco específico en vasculitis. |
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | Completado | 808 | Estudio transversal multicéntrico de patrones de tratamiento con DMARD biológicos en pacientes con AR en China; puede incluir comorbilidad de vasculitis, pero no fue diseñado para evaluar esta indicación. |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Desconocido | 750.000 | Estudio farmacoepidemiológico a gran escala sobre el riesgo de enfermedades inflamatorias inmunomediadas (IMID) incidentes en pacientes tratados con biológicos; podría capturar señales de vasculitis inducida, pero no es el criterio de valoración principal. |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Fase 2 | Aún no reclutando | 80 | Evalúa el manejo perioperatorio de inmunosupresores en pacientes reumatológicos sometidos a artroplastia de hombro; relación indirecta, sin foco en vasculitis. |
| [NCT05111743](https://clinicaltrials.gov/study/NCT05111743) | N/A | Completado | 9.261 | Estudio de vida real sobre brolucizumab en degeneración macular húmeda; no relacionado con adalimumab ni con vasculitis — probable error de indexación en la base de datos. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Revisión Sistemática | Clinical rheumatology | Revisión sistemática (PRISMA) sobre el uso de fármacos biológicos, incluyendo anti-TNF, en el tratamiento de la vasculitis reumatoide. |
| [18799049](https://pubmed.ncbi.nlm.nih.gov/18799049/) | 2008 | Revisión Sistemática | Clinical and experimental rheumatology | Comparación de características clínicas de vasculitis en 2707 pacientes con AR, 18 de ellos con vasculitis, tratados o no con anti-TNF. |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Cohorte | RMD open | Registro BSRBR-RA: compara el riesgo específico por fármaco de eventos tipo lupus y tipo vasculitis en pacientes con AR tratados con TNFi frente a DMARDs no biológicos. |
| [28719435](https://pubmed.ncbi.nlm.nih.gov/28719435/) | 2018 | Reporte de Caso | The American Journal of Dermatopathology | Primer caso reportado de vasculitis leucocitoclástica cutánea con hemofagocitosis perivascular asociada al tratamiento con adalimumab en AR. |
| [25133007](https://pubmed.ncbi.nlm.nih.gov/25133007/) | 2014 | Reporte de Caso | Case reports in rheumatology | Caso de vasculitis digital en paciente con AR que respondió favorablemente al tratamiento con adalimumab. |
| [30773522](https://pubmed.ncbi.nlm.nih.gov/30773522/) | 2019 | Reporte de Caso | Internal medicine (Tokyo, Japan) | Crisis aguda de hipertensión pulmonar en un paciente con vasculitis reumatoide, ocho meses después de reducir la dosis de adalimumab. |
| [19482531](https://pubmed.ncbi.nlm.nih.gov/19482531/) | 2009 | Reporte de Caso | Nephrologie & therapeutique | Glomerulonefritis necrotizante extracapilar asociada a anticuerpos anti-citoplasma de neutrófilos (ANCA) en paciente tratado con adalimumab por AR. |
| [23559388](https://pubmed.ncbi.nlm.nih.gov/23559388/) | 2013 | Reporte de Caso | Clinical rheumatology | Primer caso reportado de síndrome antifosfolípido asociado a adalimumab, con revisión de la literatura sobre vasculitis inducida por anti-TNF. |
| [36418100](https://pubmed.ncbi.nlm.nih.gov/36418100/) | 2023 | Reporte de Caso | Internal medicine (Tokyo, Japan) | Nefritis asociada a ANCA (MPO) durante tratamiento con abatacept y adalimumab por AR, atenuada posteriormente con tocilizumab. |
| [24558628](https://pubmed.ncbi.nlm.nih.gov/24558628/) | 2013 | Reporte de Caso | Case reports in nephrology | Adalimumab exacerba una lesión renal aguda por glomerulonefritis por IgA e induce autoanticuerpos tipo lupus en un paciente con psoriasis. |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- La evidencia actual para "Vasculitis Reumatoide" corresponde al nivel L3 (revisiones sistemáticas y estudios observacionales), sin ensayos clínicos controlados diseñados específicamente para esta indicación.
- Existe una señal de seguridad relevante y no resuelta: múltiples reportes de caso documentan que adalimumab puede **inducir** vasculitis (leucocitoclástica, asociada a ANCA, tipo lupus) además de tratarla — la conocida "paradoja anti-TNF" — lo que exige cautela antes de avanzar.
- Existe un vacío de datos de tipo *Blocking* (DG001: advertencias/contraindicaciones del prospecto no disponibles), que impide completar la evaluación de seguridad inicial (S1) requerida antes de cualquier decisión de avance.
- Como referencia de contexto: otras indicaciones predichas para adalimumab en este mismo candidato —espondilopatía inflamatoria y artritis reumatoide juvenil poliarticular— cuentan con evidencia de nivel L1 (múltiples ensayos Fase 3) y ya corresponden a usos clínicos establecidos del fármaco, a diferencia de la vasculitis reumatoide, que permanece como pregunta de investigación.

**Para avanzar se necesita:**
- Obtener las advertencias, contraindicaciones y datos de seguridad del prospecto oficial (resolver DG001, gap bloqueante).
- Obtener datos formales del mecanismo de acción desde DrugBank u otra fuente regulatoria (resolver DG002).
- Diseñar o identificar estudios prospectivos controlados enfocados específicamente en vasculitis reumatoide, no solo en AR general.
- Establecer un plan de monitoreo de seguridad específico para detectar vasculitis inducida por el propio fármaco (diagnóstico diferencial entre enfermedad de base y evento adverso).
- Confirmar la viabilidad regulatoria y de mercado, dado que el fármaco actualmente no está comercializado en el mercado evaluado.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

