---
layout: default
title: Flurazepam
parent: Evidencia moderada (L3-L4)
nav_order: 238
evidence_level: L3
indication_count: 1
---

# Flurazepam
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **1** 
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

# Flurazepam: De Indicación Original No Registrada a Trastorno del Sueño (Inicio y Mantenimiento)

## Resumen en Una Frase

El registro de AEMPS no incluye el texto de la indicación original de flurazepam. La literatura lo describe como una benzodiazepina hipnótica establecida.
El modelo TxGNN predice que podría ser efectivo para el **trastorno del sueño (inicio y mantenimiento del sueño)**, es decir, el insomnio.
Hay **0 ensayos clínicos registrados** y **20 publicaciones**, en su mayoría revisiones y estudios clínicos antiguos, que respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en el registro (el texto de indicación de AEMPS está vacío) |
| Nueva Indicación Predicha | Trastorno del sueño (inicio y mantenimiento del sueño) |
| Puntaje de Predicción TxGNN | 99.42% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, flurazepam es una benzodiazepina que actúa como modulador alostérico positivo de los receptores GABA-A. Potencia la neurotransmisión inhibitoria GABAérgica y produce efectos sedantes e hipnóticos.

Este mecanismo coincide con la indicación predicha. Las revisiones identificadas describen a flurazepam como el primer hipnótico benzodiazepínico, disponible desde 1970. Una de ellas indica que es eficaz tanto para la inducción como para el mantenimiento del sueño (PMID 3332464). El estudio estructural por crio-EM de ensambles nativos de receptores GABA-A (PMID 37730991) respalda el mecanismo a nivel de receptor.

La ausencia de indicación original en el registro probablemente refleja una carencia de la base de datos y no una falta de uso. El puntaje TxGNN muy alto (0.994) es coherente con esta interpretación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38401406](https://pubmed.ncbi.nlm.nih.gov/38401406/) | 2024 | Revisión sistemática y metaanálisis en red de ECA | Eur Neuropsychopharmacol | Evalúa los efectos residuales de los hipnóticos sobre la conducción (desviación estándar de la posición lateral y tasas de deterioro al día siguiente) |
| [2671059](https://pubmed.ncbi.nlm.nih.gov/2671059/) | 1989 | Estudio comparativo con placebo | J Clin Psychopharmacol | Brotizolam 0.25 mg vs flurazepam 15 mg vs placebo durante 2 semanas en 36 ancianos con insomnio crónico; evalúa sueño y desempeño |
| [7792498](https://pubmed.ncbi.nlm.nih.gov/7792498/) | 1995 | Estudio clínico | Sleep | Flurazepam 30 mg y zolpidem 10 mg vs placebo en 10 insomnes; efecto sobre la percepción de estar dormido o despierto |
| [7792497](https://pubmed.ncbi.nlm.nih.gov/7792497/) | 1995 | Estudio clínico | Sleep | Mismo diseño de comparación en 15 voluntarios con sueño normal |
| [27751669](https://pubmed.ncbi.nlm.nih.gov/27751669/) | 2016 | Revisión | Clin Ther | Seguridad y eficacia de los medicamentos para el insomnio en adultos mayores |
| [3332464](https://pubmed.ncbi.nlm.nih.gov/3332464/) | 1987 | Revisión | Semin Neurol | Flurazepam es eficaz para la inducción y el mantenimiento del sueño y conserva gran parte de su eficacia tras 4 semanas de uso nocturno |
| [1319429](https://pubmed.ncbi.nlm.nih.gov/1319429/) | 1992 | Revisión | J Clin Psychiatry | Farmacología de los hipnóticos benzodiazepínicos; flurazepam fue el primero, disponible desde 1970 |
| [2567741](https://pubmed.ncbi.nlm.nih.gov/2567741/) | 1989 | Revisión crítica | J Clin Psychopharmacol | Revisa estudios de laboratorio del sueño sobre insomnio de rebote tras triazolam, temazepam y flurazepam |
| [6120270](https://pubmed.ncbi.nlm.nih.gov/6120270/) | 1981 | Estudio de laboratorio del sueño y clínico | Methods Find Exp Clin Pharmacol | Registros polisomnográficos con triazolam, flunitrazepam y flurazepam en pacientes con insomnio |
| [37730991](https://pubmed.ncbi.nlm.nih.gov/37730991/) | 2023 | Estudio estructural/mecanístico | Nature | Estructuras crio-EM de receptores GABA-A nativos, diana de sedantes e hipnóticos |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 50234 | DORMODOR 30 mg CÁPSULAS DURAS (Viatris Healthcare Limited) | Cápsula dura | No consignada en el registro |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El mecanismo GABAérgico es coherente con la indicación de insomnio y el puntaje TxGNN es muy alto. Sin embargo, la evidencia disponible es de nivel L3, formada por revisiones y estudios clínicos antiguos, sin ensayos clínicos registrados. No se dispone de la información de seguridad de AEMPS.

**Para avanzar se necesita:**
- Obtener y analizar la ficha técnica de AEMPS de DORMODOR (advertencias, contraindicaciones e indicación autorizada), un requisito bloqueante antes del cribado de seguridad
- Confirmar la indicación original y el mecanismo de acción en DrugBank
- Verificar en la ficha técnica la coincidencia entre la indicación autorizada en España y la indicación predicha
- Definir un plan de seguridad para poblaciones vulnerables, como adultos mayores, considerando los efectos residuales sobre la conducción y el insomnio de rebote descritos en la literatura
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

