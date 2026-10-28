---
layout: default
title: Vilanterol
parent: Solo predicción del modelo (L5)
nav_order: 846
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
monitor_inn: "vilanterol"
predicted_indications: ["hyperlucent lung", "tracheal stenosis", "bronchial neoplasm (disease)", "respiratory malformation", "tracheal calcification", "laryngotracheitis"]
description: "Vilanterol: nueva indicación predicha, Hyperlucent lung (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Vilanterol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Vilanterol: Hyperlucent lung
{: .text-alpha }

## Resumen en Una Frase

Vilanterol es un agonista beta2 de acción prolongada (LABA) que se utiliza en inhaladores combinados para la enfermedad pulmonar obstructiva crónica (EPOC) y el asma.
Cabe señalar que esta predicción es en realidad una categoría paraguas que engloba las indicaciones ya conocidas del fármaco, por lo que no constituye un reposicionamiento en sentido estricto.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Hyperlucent lung |
| Puntaje de Predicción TxGNN | 0.9972 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 15 de 20) |
| Número de Autorizaciones | 20 (vigentes: 15) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, vilanterol es un agonista beta2-adrenérgico de acción prolongada que relaja el músculo liso de las vías respiratorias y produce broncodilatación sostenida (compatible con la administración una vez al día). Se utiliza siempre en combinación: con furoato de fluticasona (Relvar/Revinty), con umeclidinio (Anoro/Laventair) o en triple terapia con ambos (Trelegy/Elebrato/Temybric).

La "enfermedad pulmonar obstructiva" es la categoría general que abarca las indicaciones ya establecidas de vilanterol (EPOC, asma, bronquitis, enfisema). Por tanto, se trata de una indicación ya cubierta y no de un reposicionamiento genuino. La plausibilidad mecanística es alta: la broncodilatación mediada por beta2 actúa directamente sobre la obstrucción del flujo aéreo.

La evidencia es directa y abundante: ensayos de Fase 3 de gran tamaño (como IMPACT y FULFIL) con resultados de exacerbaciones y mortalidad.

---

## Evidencia de Ensayos Clínicos

Se muestran los 10 ensayos más relevantes de los 29 identificados.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT05062304](https://clinicaltrials.gov/study/NCT05062304) | N/A | Completado | 17281 | Registro del ensayo IMPACT: triple terapia en un solo inhalador (furoato de fluticasona/umeclidinio/vilanterol) frente a terapia dual en EPOC |
| [NCT03162055](https://clinicaltrials.gov/study/NCT03162055) | Fase 3 | Completado | 1119 | Glicopirronio/formoterol frente a umeclidinio/vilanterol durante 24 semanas en EPOC de moderada a muy grave (AERISTO) |
| [NCT02301975](https://clinicaltrials.gov/study/NCT02301975) | Fase 3 | Completado | 1526 | FF/VI una vez al día frente a FP/salmeterol y FP en asma persistente ya controlada con ICS+LABA (no inferioridad) |
| [NCT01686633](https://clinicaltrials.gov/study/NCT01686633) | Fase 3 | Completado | 1040 | FF/VI 200/25 y 100/25 frente a FF 100 en asma persistente de moderada a grave |
| [NCT01134042](https://clinicaltrials.gov/study/NCT01134042) | Fase 3 | Completado | 587 | FF/VI frente a FF sola y FP sola en asma persistente durante 24 semanas |
| [NCT02094937](https://clinicaltrials.gov/study/NCT02094937) | Fase 3 | Completado | 430 | Reducción escalonada desde FF/VI 100/25 en asma bien controlada en sujetos japoneses |
| [NCT01777334](https://clinicaltrials.gov/study/NCT01777334) | Fase 3 | Completado | 905 | Umeclidinio/vilanterol frente a tiotropio durante 24 semanas en EPOC (FEV1 valle) |
| [NCT01342913](https://clinicaltrials.gov/study/NCT01342913) | Fase 3 | Completado | 528 | Función pulmonar de 24 h de FF/VI una vez al día frente a salmeterol/FP dos veces al día en EPOC |
| [NCT01323621](https://clinicaltrials.gov/study/NCT01323621) | Fase 3 | Completado | 512 | Perfil de función pulmonar de 24 h de FF/VI 100/25 frente a FP/salmeterol 250/50 en EPOC |
| [NCT02487446](https://clinicaltrials.gov/study/NCT02487446) | Fase 3 | Completado | 357 | Indacaterol/glicopirronio frente a umeclidinio/vilanterol en EPOC de moderada a grave |

---

## Evidencia de Literatura

Se muestran las 10 publicaciones más relevantes, priorizando ECA y revisiones sistemáticas.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29668352](https://pubmed.ncbi.nlm.nih.gov/29668352/) | 2018 | ECA | N Engl J Med | Ensayo IMPACT: triple terapia una vez al día en un solo inhalador frente a terapia dual en EPOC |
| [28375647](https://pubmed.ncbi.nlm.nih.gov/28375647/) | 2017 | ECA | Am J Respir Crit Care Med | Ensayo FULFIL: triple terapia una vez al día frente a terapia dual ICS/LABA en EPOC |
| [32162970](https://pubmed.ncbi.nlm.nih.gov/32162970/) | 2020 | ECA (análisis de IMPACT) | Am J Respir Crit Care Med | Reducción de la mortalidad por todas las causas con FF/UMEC/VI en EPOC |
| [32918892](https://pubmed.ncbi.nlm.nih.gov/32918892/) | 2021 | ECA Fase 3A | Lancet Respir Med | CAPTAIN: triple terapia FF/UMEC/VI frente a FF/VI en asma mal controlada |
| [39797646](https://pubmed.ncbi.nlm.nih.gov/39797646/) | 2024 | Metaanálisis / cohorte | BMJ | Eficacia y seguridad comparadas de triples terapias en un solo inhalador en EPOC |
| [39696097](https://pubmed.ncbi.nlm.nih.gov/39696097/) | 2024 | Revisión sistemática y metaanálisis | BMC Pulm Med | Umeclidinio/vilanterol frente a otros broncodilatadores en EPOC |
| [35849317](https://pubmed.ncbi.nlm.nih.gov/35849317/) | 2022 | Metaanálisis en red | Adv Ther | FF/UMEC/VI frente a otras triples y duales en EPOC |
| [42281286](https://pubmed.ncbi.nlm.nih.gov/42281286/) | 2026 | Análisis post hoc de Fase 3 | Am J Respir Crit Care Med | Definición de estabilidad de la enfermedad en EPOC |
| [39731707](https://pubmed.ncbi.nlm.nih.gov/39731707/) | 2025 | Cohorte | Adv Ther | Efectividad comparada de FF/UMEC/VI y BUD/GLY/FORM en pacientes estadounidenses con EPOC |
| [28956463](https://pubmed.ncbi.nlm.nih.gov/28956463/) | 2017 | Revisión | Expert Rev Respir Med | Papel de FF/VI una vez al día en EPOC estable |

---

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones vigentes (todas de tipo monofármaco según el registro; los textos de indicación aprobada no figuran en los datos compilados).

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 114898002IP4 | Anoro Ellipta 55 mcg/22 mcg | Polvo para inhalación (unidosis) | No disponible en los datos |
| 13886002IP | Relvar Ellipta 92/22 mcg | Polvo para inhalación (unidosis) | No disponible en los datos |
| 114929002IP | Revinty Ellipta 92/22 mcg | Polvo para inhalación (unidosis) | No disponible en los datos |
| 114899002 | Laventair Ellipta 55/22 mcg | Polvo para inhalación (unidosis) | No disponible en los datos |
| 117123602 | Trelegy Ellipta 92/55/22 mcg | Polvo para inhalación (unidosis) | No disponible en los datos |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 388 interacciones en total. Entre las principales mostradas:
  - *Moderadas*: antidiabéticos (acarbosa, albiglutida, alogliptina, canagliflozina, clorpropamida, dapagliflozina, dulaglutida, empagliflozina); macrólidos (claritromicina); fármacos que prolongan el QT o procinéticos (cisaprida, dolasetrón); simpaticomiméticos (efedrina, epinefrina, dietilpropión).
  - *Leves*: corticoides (beclometasona, betametasona, budesonida, dexametasona).

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
No obstante, no es un reposicionamiento real, y la información de seguridad de la ficha técnica no está disponible.

**Para avanzar se necesita:**
- Obtener advertencias y contraindicaciones del prospecto de la AEMPS (bloqueante para el cribado de seguridad).
- Obtener los datos del mecanismo de acción desde DrugBank.
- Revisar los textos de indicación aprobada de las autorizaciones españolas.
- Revisar las interacciones moderadas (antidiabéticos, macrólidos, simpaticomiméticos, fármacos que prolongan el QT).

**Otras predicciones (no recomendadas por ahora):** el resto de indicaciones predichas (enfisema intersticial, enfisema compensatorio, pulmón hiperlúcido, estenosis traqueal, neoplasia bronquial, enfisema lobar congénito, malformación respiratoria, calcificación traqueal y laringotraqueítis) se clasifican como **Hold**, con evidencia L4-L5 y sin fundamento mecanístico claro. En la neoplasia bronquial, la evidencia solo se refiere al tratamiento de la EPOC concomitante en el perioperatorio, no al tumor.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

