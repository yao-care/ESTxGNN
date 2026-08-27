---
layout: default
title: Prasugrel
parent: 僅模型預測 (L5)
nav_order: 228
evidence_level: L5
indication_count: 10
---

# Prasugrel
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

# Prasugrel: De Sindrome Coronario Agudo a Hipertension Pulmonar

## Resumen en Una Frase

Prasugrel es un inhibidor del receptor P2Y12 (clase thienopiridina) utilizado como antiagregante plaquetario tras intervencion coronaria percutanea en pacientes con sindrome coronario agudo. El modelo TxGNN predice que podria ser efectivo para **Hipertension Pulmonar**, pero solo **2 ensayos clinicos** y **2 publicaciones** aparecen asociados a esta busqueda, y ninguno estudia realmente prasugrel en esta indicacion.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Sindrome coronario agudo (tras ICP), como antiagregante plaquetario (fuente: literatura de la evidencia recopilada; no hay datos regulatorios propios en la Evidence Pack) |
| Nueva Indicacion Predicha | Hipertension Pulmonar |
| Puntaje de Prediccion TxGNN | 99.88% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Espana | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion en la ficha del farmaco. Segun la evidencia recopilada, prasugrel es una thienopiridina que actua como antagonista irreversible del receptor P2Y12 plaquetario, mecanismo bien establecido en el tratamiento antiagregante del sindrome coronario agudo tras colocacion de stent.

La hipotesis mecanistica detras de esta prediccion es que la actividad antiplaquetaria podria tener un papel auxiliar en formas de hipertension pulmonar de origen tromboembolico cronico (CTEPH), donde la carga trombotica contribuye a la fisiopatologia de la enfermedad.

Sin embargo, es importante senalar que los ensayos clinicos y la literatura recuperados para esta busqueda **no estudian realmente prasugrel en hipertension pulmonar**: los dos ensayos tratan sobre elegibilidad de pacientes en un estudio de trombosis asociada a cancer y sobre manejo observacional de anticoagulantes orales no antagonistas de vitamina K (NOAC, no antiagregantes) en fibrilacion auricular. Se trata de una discrepancia entre la puntuacion del modelo TxGNN y la evidencia real disponible, lo que limita significativamente la confianza en esta prediccion en su estado actual.

## Evidencia de Ensayos Clinicos

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04846556](https://clinicaltrials.gov/study/NCT04846556) | N/A | Completado | 300 | Estudio retrospectivo multicentrico sobre la proporcion de pacientes con trombosis asociada a cancer no elegibles para el estudio CARAVAGGIO; no evalua prasugrel ni hipertension pulmonar directamente |
| [NCT03993119](https://clinicaltrials.gov/study/NCT03993119) | N/A | Completado | 500 | Estudio observacional transversal sobre el manejo de anticoagulantes NOAC en pacientes ancianos con fibrilacion auricular no valvular en Espana; no evalua antiagregantes ni hipertension pulmonar |

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Cohorte | Curr Med Res Opin | Factores asociados al uso, adherencia y persistencia de clopidogrel (y prasugrel) en pacientes con sindrome coronario agudo tras ICP; confirma el uso original de prasugrel pero no aborda hipertension pulmonar |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Cohorte/observacional | Kardiologiia | Analisis del efecto de terapias cronicas previas a la infeccion por COVID-19 sobre la mortalidad, en el registro ACTIV; no relacionado con prasugrel ni hipertension pulmonar de forma especifica |

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
Aunque la puntuacion de prediccion de TxGNN es muy alta (99.88%), la evidencia clinica y bibliografica recuperada no respalda especificamente el uso de prasugrel en hipertension pulmonar — los estudios encontrados tratan temas distintos (trombosis asociada a cancer, manejo de NOAC). El nivel de evidencia es L5 (solo prediccion del modelo, sin estudios reales que la sustenten), por lo que no se recomienda avanzar en este momento.

**Para avanzar se necesita:**
- Ficha tecnica/prospecto de la AEMPS con advertencias y contraindicaciones (actualmente bloqueante para la evaluacion de seguridad S1)
- Datos detallados del mecanismo de accion (MOA) de prasugrel
- Busqueda dirigida de estudios preclinicos o clinicos que evaluen antiagregantes P2Y12 especificamente en hipertension pulmonar tromboembolica cronica (CTEPH)
- Confirmacion formal de la indicacion original de prasugrel mediante fuente regulatoria (no disponible en este Evidence Pack)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

