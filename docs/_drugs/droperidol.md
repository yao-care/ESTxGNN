---
layout: default
title: Droperidol
parent: 僅模型預測 (L5)
nav_order: 96
evidence_level: L5
indication_count: 10
---

# Droperidol
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

# Droperidol: De Sedación en Agitación Aguda a Cefalea/Migraña Aguda

## Resumen en Una Frase

Droperidol es una butirofenona que, según la propia literatura recogida en este Evidence Pack, se ha empleado clásicamente como tranquilizante/sedante en cuadros de agitación aguda (no hay ficha técnica ni indicación original confirmada en este pack). Entre las **10 indicaciones** predichas por TxGNN para este fármaco, la que cuenta con mayor respaldo real es **Cefalea/Migraña Aguda**, con **1 ensayo clínico** y **20 publicaciones** —incluyendo varios ensayos aleatorizados doble ciego— que respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en el Evidence Pack (sin licencias en España; MOA marcado como dato pendiente — ver DG002) |
| Nueva Indicación Predicha | Cefalea/Migraña Aguda (seleccionada entre 10 candidatos TxGNN por ser la de mayor nivel de evidencia) |
| Puntaje de Predicción TxGNN | 99.47% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción confirmados por DrugBank (gap DG002, severidad alta). Según la información disponible en la propia literatura del pack, droperidol es una **butirofenona** con antagonismo D2/5-HT2, clase farmacológica que en varias publicaciones (Cochrane 2016, 2004, 2001) se describe como utilizada para tranquilización/sedación en cuadros de agitación aguda en varios países.

Ese mismo mecanismo de antagonismo D2/5-HT2 —junto con su efecto antiemético ya reconocido— es coherente con la fisiopatología de la migraña aguda, donde las vías dopaminérgicas participan tanto en las náuseas/vómitos asociados como en la sensibilización central. Esto explica por qué droperidol lleva décadas usándose off-label en servicios de urgencias para migraña y status migrainosus, y por qué ha sido incorporado en las revisiones de evidencia de la American Headache Society y la Canadian Headache Society.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01406860](https://clinicaltrials.gov/study/NCT01406860) | N/A | Terminado | 19 | Comparó droperidol vs. metoclopramida+difenhidramina para cefalea primaria en urgencias; finalizado anticipadamente por reclutamiento lento, por lo que la potencia estadística es insuficiente (evidencia solo de apoyo, grado B). |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [12552051](https://pubmed.ncbi.nlm.nih.gov/12552051/) | 2003 | ECA doble ciego, controlado con placebo | Neurology | Evalúa droperidol como terapia de "rescate" parenteral en migraña cuando fallan los fármacos de primera línea. |
| [11781912](https://pubmed.ncbi.nlm.nih.gov/11781912/) | 2002 | ECA | Am J Emerg Med | Confirma eficacia de droperidol IM para migraña aguda en urgencias, replicando hallazgos de una serie de casos previa. |
| [10452443](https://pubmed.ncbi.nlm.nih.gov/10452443/) | 1999 | Serie de casos retrospectiva | Am J Emerg Med | Revisión piloto de pacientes tratados con droperidol IM para migraña aguda; lo describe como terapia prometedora. |
| [9237411](https://pubmed.ncbi.nlm.nih.gov/9237411/) | 1997 | Cohorte/Serie de casos | Headache | Estudio piloto en 35 pacientes con status migrainosus/migraña refractaria tratados con droperidol IV 2.5 mg cada 30 min. |
| [21435315](https://pubmed.ncbi.nlm.nih.gov/21435315/) | 2011 | Revisión sistemática | CJEM | Evalúa si las butirofenonas (incluye droperidol) son eficaces para cefalea primaria en urgencias. |
| [25416184](https://pubmed.ncbi.nlm.nih.gov/25416184/) | 2015 | Revisión | Ann Pharmacother | Evalúa seguridad y eficacia de droperidol para el alivio de la migraña aguda. |
| [12890142](https://pubmed.ncbi.nlm.nih.gov/12890142/) | 2003 | Revisión | Headache | Droperidol y otros neurolépticos/antieméticos en el manejo de la migraña. |
| [32839811](https://pubmed.ncbi.nlm.nih.gov/32839811/) | 2020 | Revisión | AJHP | Revisión integral sobre la reintegración de droperidol a la práctica de urgencias (seguridad, indicaciones, eficacia, dosificación). |
| [24875925](https://pubmed.ncbi.nlm.nih.gov/24875925/) | 2015 | Revisión/Guía (Cochrane-tier) | Cephalalgia | Recomendaciones de la Sociedad Canadiense de Cefalea sobre tratamiento del dolor migrañoso en urgencias. |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Revisión/Guía | Headache | Evaluación de evidencia de la Sociedad Americana de Cefalea sobre farmacoterapias para migraña aguda. |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No hay advertencias, contraindicaciones ni interacciones farmacológicas registradas en este Evidence Pack (DG001, gap bloqueante: falta el prospecto/ficha técnica de TFDA, necesario antes de la evaluación de seguridad S1).

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen múltiples ensayos aleatorizados (incluyendo uno doble ciego controlado con placebo) y revisiones de sociedades científicas de cefalea que respaldan el uso de droperidol en migraña aguda, pero el único ensayo indexado en ClinicalTrials.gov se terminó anticipadamente por bajo reclutamiento (n=19), y falta por completo la información de seguridad/ficha técnica (gap bloqueante DG001) necesaria para una evaluación S1 completa.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha técnica de TFDA con advertencias y contraindicaciones (DG001, bloqueante — especialmente relevante dado el riesgo conocido de prolongación del QT asociado a butirofenonas)
- Confirmar el mecanismo de acción vía API de DrugBank (DG002)
- Aclarar el estatus regulatorio real en España, dado que actualmente figura como no comercializado (0 autorizaciones)
- Considerar un ensayo adecuadamente potenciado que replique NCT01406860, dado que este se terminó con muestra insuficiente
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

