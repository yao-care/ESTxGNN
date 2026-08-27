---
layout: default
title: Flurazepam
parent: 僅模型預測 (L5)
nav_order: 121
evidence_level: L5
indication_count: 1
---

# Flurazepam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Flurazepam: De Insomnio (uso historico no confirmado en el Evidence Pack) a Trastorno del Sueño (Dificultad para Iniciar y Mantener el Sueño)

## Resumen en Una Frase

Flurazepam es una benzodiazepina cuyo mecanismo de accion y datos de indicacion original no estan disponibles en este Evidence Pack. El modelo TxGNN predice que podria ser efectivo para **Trastorno del Sueño (Inicio y Mantenimiento)**, con **0 ensayos clinicos estructurados** pero **20 publicaciones** que actualmente respaldan esta direccion — cabe destacar que la literatura recuperada describe a flurazepam como un hipnotico ya utilizado historicamente para el insomnio, por lo que esta prediccion podria reflejar un uso ya establecido mas que un reposicionamiento novedoso.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | No disponible en el Evidence Pack (sin licencias registradas; ver nota abajo) |
| Nueva Indicacion Predicha | Trastorno del sueño, inicio y mantenimiento (insomnio) |
| Puntaje de Prediccion TxGNN | 99.42% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion de flurazepam en este Evidence Pack (dato marcado como bloqueante/alto en la evaluacion de gaps). Sin embargo, la literatura recuperada permite contextualizar la prediccion: flurazepam es descrita repetidamente como una de las primeras benzodiazepinas hipnoticas, actuando sobre el receptor GABA-A (ver PMID 37730991, estructura cryo-EM de receptores GABAA), y multiples publicaciones (PMID 1319429, PMID 3332464, PMID 641469) documentan su uso clinico establecido desde la decada de 1970 para el tratamiento del insomnio, incluyendo eficacia tanto en induccion como en mantenimiento del sueño.

Esto significa que la indicacion predicha por TxGNN (trastorno del sueño, inicio y mantenimiento) coincide en gran medida con el uso farmacologico ya conocido de esta molecula como hipnotico benzodiacepinico, y no con una indicacion terapeutica novedosa en otra area clinica. Por tanto, el valor de este candidato como "reposicionamiento" es limitado: la señal del modelo parece confirmar conocimiento farmacologico preexistente mas que descubrir una aplicacion nueva.

Dado que faltan los datos estructurados de indicacion original (`original_indications` vacio) y de MOA, no es posible verificar formalmente esta hipotesis dentro del propio Evidence Pack; se recomienda complementar con datos de DrugBank/ficha tecnica antes de sacar conclusiones definitivas.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados (ni en ClinicalTrials.gov ni en ICTRP para esta combinacion farmaco-indicacion).

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38401406](https://pubmed.ncbi.nlm.nih.gov/38401406/) | 2024 | Revision sistematica / meta-analisis en red de ECAs | Eur Neuropsychopharmacol | Meta-analisis en red de ECAs sobre efectos residuales de hipnoticos (incl. flurazepam) en el rendimiento de conduccion |
| [2671059](https://pubmed.ncbi.nlm.nih.gov/2671059/) | 1989 | Estudio comparativo controlado | J Clin Psychopharmacol | Comparacion de brotizolam 0.25mg vs flurazepam 15mg vs placebo en 36 ancianos con insomnio cronico durante 2 semanas |
| [7792498](https://pubmed.ncbi.nlm.nih.gov/7792498/) | 1995 | Estudio clinico comparativo | Sleep | Flurazepam 30mg y zolpidem 10mg alteran la percepcion de sueño en insomnes vs placebo, en 10 pacientes |
| [7792497](https://pubmed.ncbi.nlm.nih.gov/7792497/) | 1995 | Estudio clinico comparativo | Sleep | Mismo diseño en 15 dormidores normales (no insomnes) |
| [6120270](https://pubmed.ncbi.nlm.nih.gov/6120270/) | 1981 | Estudio de laboratorio del sueño / clinico | Methods Find Exp Clin Pharmacol | Estudios polisomnograficos de triazolam, flunitrazepam y flurazepam en pacientes insomnes |
| [2567741](https://pubmed.ncbi.nlm.nih.gov/2567741/) | 1989 | Revision critica | J Clin Psychopharmacol | Revision de insomnio de rebote tras suspension de triazolam, temazepam y flurazepam |
| [1319429](https://pubmed.ncbi.nlm.nih.gov/1319429/) | 1992 | Revision | J Clin Psychiatry | Historia y farmacologia de las benzodiazepinas hipnoticas; flurazepam como primera de su clase (1970) |
| [3332464](https://pubmed.ncbi.nlm.nih.gov/3332464/) | 1987 | Revision | Semin Neurol | Neurofarmacologia clinica de trastornos del sueño; flurazepam eficaz en induccion y mantenimiento del sueño |
| [27751669](https://pubmed.ncbi.nlm.nih.gov/27751669/) | 2016 | Revision | Clin Ther | Seguridad y eficacia de medicamentos para el sueño en adultos mayores |
| [37730991](https://pubmed.ncbi.nlm.nih.gov/37730991/) | 2023 | Estudio mecanistico (cryo-EM) | Nature | Estructuras cryo-EM de ensamblajes nativos del receptor GABAA, diana de hipnoticos como las benzodiazepinas |

## España — Estado de Mercado

Segun este Evidence Pack, flurazepam **no esta comercializado** en España (0 autorizaciones registradas). No hay informacion de nombre comercial, forma farmaceutica ni indicacion aprobada disponible para listar.

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad. No hay datos de advertencias, contraindicaciones ni interacciones farmacologicas disponibles en este Evidence Pack (la busqueda de interacciones no arrojo resultados).

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
Existe un data gap bloqueante sobre advertencias/contraindicaciones (equivalente a ficha tecnica) que impide realizar la evaluacion de seguridad inicial (S1). Ademas, el farmaco no esta comercializado en España y la indicacion predicha coincide en gran medida con el uso historico ya conocido de flurazepam como hipnotico, lo que reduce su valor como candidato de reposicionamiento novedoso.

**Para avanzar se necesita:**
- Obtener la ficha tecnica/prospecto (AEMPS o equivalente) con advertencias y contraindicaciones — bloqueante para pasar a S1
- Confirmar el mecanismo de accion (MOA) mediante DrugBank u otra fuente farmacologica
- Verificar la indicacion original real de flurazepam (actualmente vacia en el registro) para determinar si la prediccion constituye un reposicionamiento genuino o una confirmacion de uso ya establecido
- Confirmar el estado real de comercializacion en España, dado que el registro actual muestra 0 licencias
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

