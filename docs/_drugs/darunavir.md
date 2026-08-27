---
layout: default
title: Darunavir
parent: 僅模型預測 (L5)
nav_order: 82
evidence_level: L5
indication_count: 4
---

# Darunavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Darunavir: De Infección por VIH-1 a Síndrome de Inmunodeficiencia Felina (SIDA Felino)

## Resumen en Una Frase

Darunavir es un inhibidor de la proteasa del VIH-1, utilizado originalmente —en combinación con ritonavir o cobicistat— para el tratamiento de la infección por VIH-1.
El modelo TxGNN predice como candidato de mayor puntuación el **síndrome de inmunodeficiencia adquirida felina (SIDA felino)**,
pero la revisión de evidencia encontró que el único ensayo clínico indexado para esta indicación corresponde en realidad a pacientes humanos con VIH-1, no a felinos —es decir, **sin evidencia real de respaldo** tras verificación.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Infección por VIH-1 (uso clínico conocido; sin licencias registradas actualmente en España) |
| Nueva Indicacion Predicha | Síndrome de inmunodeficiencia adquirida felina (SIDA felino) |
| Puntaje de Prediccion TxGNN | 99.97% |
| Nivel de Evidencia | L5 (el único ensayo indexado resulta ser un error de mapeo de entidad — ver nota abajo) |
| Estado de Mercado en Espana | ❌ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

> **Nota sobre el nivel de evidencia:** el pipeline de origen clasificó esta indicación como L4, pero la verificación del ensayo NCT02770508 confirmó que se trata de un estudio en humanos con VIH-1, no de un modelo felino. Descontando ese ensayo, no queda ningún estudio real que respalde la indicación, por lo que el nivel de evidencia efectivo es L5 (solo predicción del modelo).

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción (MOA) en el Evidence Pack. Según la información farmacológica conocida, darunavir es un inhibidor de la proteasa del VIH-1 que bloquea la escisión de las poliproteínas gag-pol, impidiendo la maduración de partículas virales infecciosas; se administra siempre "potenciado" con ritonavir o cobicistat.

La hipótesis mecanística de TxGNN parte de la homología estructural entre proteasas de distintos lentivirus (VIH-1, virus de inmunodeficiencia felina, virus de inmunodeficiencia de simios). Sin embargo, la proteasa del virus de inmunodeficiencia felina (FIV) difiere sustancialmente de la del VIH-1 en su sitio activo, y no existe evidencia directa de actividad cruzada de darunavir frente a FIV. El único ensayo asociado a esta predicción (NCT02770508) fue verificado mediante búsqueda externa y corresponde a un estudio de fase 4 en **pacientes humanos VIH-1 positivos**, no a un modelo felino — lo que indica un probable error de mapeo de entidades en el grafo de conocimiento (coincidencia de la cadena "AIDS"/"immunodeficiency syndrome" entre especies).

En consecuencia, el vínculo mecanístico entre darunavir y el SIDA felino no puede considerarse respaldado por evidencia real en este momento; se trata de una señal a nivel de clase farmacológica (inhibidores de proteasa retroviral) sin confirmación específica para esta indicación.

---

## Evidencia de Ensayos Clinicos

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Fase 4 | Completado | 145 | Comparó darunavir/ritonavir + lamivudina vs. darunavir/ritonavir + emtricitabina/tenofovir en pacientes **humanos** VIH-1 sin tratamiento previo. **No es un estudio en felinos**; verificado como error de mapeo de entidad, no constituye evidencia para el SIDA felino. |

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal (síndrome de inmunodeficiencia felina).

---

## Otros Candidatos Evaluados en este Informe

Este Evidence Pack evaluó 4 posibles indicaciones nuevas para darunavir. Además de la indicación principal (arriba), se identificaron:

| Rank | Indicacion Predicha | Puntaje TxGNN | Nivel de Evidencia | Recomendacion | Nota |
|------|------|------|------|------|------|
| 2 | Infección por virus de inmunodeficiencia de simios (SIV) | 99.97% | L4 | Research Question | 4 publicaciones preclínicas en macacos con terapia antirretroviral combinada; ninguna evalúa darunavir específicamente como fármaco principal (evidencia de clase, no específica). |
| 3 | Trastorno del neurodesarrollo con marcha atáxica, ausencia de habla y sustancia blanca cortical disminuida | 99.66% | L5 | Hold | Sin ensayos ni literatura; sin vínculo mecanístico conocido. Probable falso positivo del modelo. |
| 4 | Hiperlipidemia combinada familiar (término obsoleto) | 99.19% | L5 | Hold | Sin ensayos ni literatura; dirección mecanística **opuesta** — los inhibidores de proteasa potenciados son conocidos por *inducir* dislipidemia, no tratarla. Probable ruido del grafo de conocimiento. |

**Literatura del candidato rank 2 (SIV):**

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Preclínico (macacos) | AIDS Res Hum Retroviruses | Evaluación comparativa de regímenes de terapia antirretroviral inyectable combinada en macacos rhesus infectados con SIV. |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Preclínico (macacos) | PLoS One | Terapia antirretroviral supresora + SAHA (inhibidor de histona deacetilasa) en macacos rhesus chinos infectados con SIV, enfocado en reservorios virales. |
| [21505294](https://pubmed.ncbi.nlm.nih.gov/21505294/) | 2011 | Preclínico (modelo mono SIDA) | AIDS (London) | El compuesto de oro auranofina restringe el reservorio viral en el modelo de SIDA en monos. |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Preclínico (modelo SIDA símico) | PLoS Pathogens | Régimen de ART altamente intensificado induce supresión viral a largo plazo y restricción del reservorio en modelo de SIDA símico. |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
Ninguno de los 4 candidatos de reposicionamiento cuenta con evidencia clínica o de literatura sólida y específica para darunavir. La indicación con mayor puntuación (SIDA felino) se basa en un único ensayo clínico que, tras verificación, resultó ser un error de mapeo de entidad (estudio en humanos con VIH-1, no en felinos). Además, existe una brecha de datos **bloqueante** sobre advertencias/contraindicaciones (TFDA/AEMPS), lo que impide por sí solo avanzar a la evaluación de seguridad S1 independientemente del mérito de la indicación.

**Para avanzar se necesita:**
- Obtener el prospecto oficial (TFDA/AEMPS) para completar la evaluación de seguridad S1 (gap bloqueante DG001)
- Obtener datos de mecanismo de acción (MOA) vía API de DrugBank (gap DG002)
- Corregir el mapeo de entidad "SIDA felino" en el grafo de conocimiento y, si corresponde, volver a ejecutar la predicción
- Para el candidato SIV: identificar si existe literatura donde darunavir sea el fármaco de estudio principal (no solo un componente de un régimen combinado)
- Descartar los candidatos 3 y 4 como señales de bajo valor salvo que aparezca evidencia mecanística nueva
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

