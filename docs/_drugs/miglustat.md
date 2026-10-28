---
layout: default
title: Miglustat
parent: Solo predicción del modelo (L5)
nav_order: 529
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
monitor_inn: "MIGLUSTAT"
predicted_indications: ["autosomal ichthyosis syndrome with fatal disease course", "cholesteryl ester storage disease", "Krabbe disease", "metachromatic leukodystrophy", "Wolman disease with hypolipoproteinemia and acanthocytosis", "encephalopathy due to prosaposin deficiency", "Tay-Sachs disease", "benign neoplasm of adrenal gland", "recessive X-linked ichthyosis", "fatty acid hydroxylase-associated neurodegeneration"]
description: "Miglustat: nueva indicación predicha, Autosomal ichthyosis syndrome with fatal disease course (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Miglustat
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Miglustat: Autosomal ichthyosis syndrome with fatal disease course
{: .text-alpha }

## Resumen en Una Frase

Miglustat es un inhibidor oral de la glucosilceramida sintasa, utilizado originalmente para el tratamiento de la enfermedad de Gaucher y la enfermedad de Niemann-Pick.
El modelo TxGNN predice que podría ser efectivo para **la enfermedad de Tay-Sachs**,
con **4 ensayos clínicos** y **10 publicaciones** que actualmente respaldan esta dirección, aunque los resultados clínicos son mixtos.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Autosomal ichthyosis syndrome with fatal disease course |
| Puntaje de Predicción TxGNN | 0.9983 |
| Nivel de Evidencia | L5 (según la regla establecida: ≥2 ECAs de Fase 3 completados; ver nota abajo) |
| Estado de Mercado en España | Comercializado (registros vigentes: 6 de 7) |
| Número de Autorizaciones | 7 (vigentes: 6) |
| Decisión Recomendada | Proceed with Guardrails |

**Nota sobre el nivel de evidencia:** solo uno de los ensayos de Fase 3 figura como completado (NCT00672022); el otro (NCT03822013) fue terminado. Existe además un ECA publicado (PMID 19346952) y una revisión sistemática (2023). Los datos compilados asignan L1, pero una lectura estricta de la regla sugeriría un nivel inferior (L2–L3). Se recomienda verificarlo.

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según el conocimiento general, miglustat inhibe la glucosilceramida sintasa (UGCG), enzima clave en la síntesis de glicoesfingolípidos. Esto reduce la producción del sustrato que se acumula en los trastornos de depósito lisosomal (terapia de reducción de sustrato). Esta información proviene de conocimiento general y no de los datos aportados.

La enfermedad de Gaucher y la de Tay-Sachs son trastornos de depósito lisosomal de glicoesfingolípidos. En Tay-Sachs, la deficiencia de hexosaminidasa A provoca acumulación de gangliósido GM2, cuya síntesis depende de la vía que miglustat inhibe. Además, miglustat atraviesa la barrera hematoencefálica, lo cual es relevante en una enfermedad neurodegenerativa.

Sin embargo, la evidencia clínica es mixta. Un reporte de dos pacientes con Tay-Sachs infantil (PMID 16434676) indicó que el tratamiento no detuvo el deterioro neurológico, aunque se observó buena concentración en LCR y prevención de la macrocefalia. La eficacia debe confirmarse con los textos completos de los estudios.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00672022](https://clinicaltrials.gov/study/NCT00672022) | Fase 3 | Completado | 10 | Farmacocinética, seguridad y tolerabilidad de miglustat en gangliosidosis GM2 de inicio infantil; muestra pequeña, sin poder para eficacia |
| [NCT03822013](https://clinicaltrials.gov/study/NCT03822013) | Fase 3 | Terminado | 30 | Efectos de miglustat sobre síntomas neurológicos y sistémicos en Sandhoff y Tay-Sachs infantil; el más grande, pero terminado antes de tiempo |
| [NCT02030015](https://clinicaltrials.gov/study/NCT02030015) | Fase 4 | Terminado | 16 | Miglustat combinado con dieta cetogénica (Syner-G) en gangliosidosis; la combinación confunde el efecto del fármaco |
| [NCT00418847](https://clinicaltrials.gov/study/NCT00418847) | Fase 2 | Completado | 5 | Farmacocinética y tolerabilidad en gangliosidosis GM2 juvenil; solo 5 pacientes |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [19346952](https://pubmed.ncbi.nlm.nih.gov/19346952/) | 2009 | ECA | Genetics in Medicine | Estudio aleatorizado de 12 meses (con 24 meses de extensión) sobre seguridad y eficacia de miglustat en Tay-Sachs de inicio tardío |
| [37209042](https://pubmed.ncbi.nlm.nih.gov/37209042/) | 2023 | Revisión sistemática | European Journal of Neurology | Evalúa eficacia y seguridad de miglustat en gangliosidosis GM2 ante resultados previos inconsistentes |
| [42794762](https://pubmed.ncbi.nlm.nih.gov/42794762/) | 2026 | Revisión | Int J Mol Sci | Fundamento biológico, evidencia clínica y límites del reposicionamiento de miglustat en trastornos lisosomales neuronopáticos |
| [16434676](https://pubmed.ncbi.nlm.nih.gov/16434676/) | 2006 | Serie de casos | Neurology | Dos pacientes con Tay-Sachs infantil: sin detención del deterioro neurológico, pero con concentración significativa en LCR y prevención de macrocefalia |
| [30743792](https://pubmed.ncbi.nlm.nih.gov/30743792/) | 2009 | Revisión | Expert Rev Endocrinol Metab | Terapia de reducción de sustrato con miglustat en trastornos de glicoesfingolípidos con afectación cerebral |
| [16763917](https://pubmed.ncbi.nlm.nih.gov/16763917/) | 2006 | Revisión | J Inherit Metab Dis | Terapia de reducción de sustrato en trastornos de depósito de glicoesfingolípidos |
| [30524313](https://pubmed.ncbi.nlm.nih.gov/30524313/) | 2018 | Revisión | Front Physiol | Nuevos enfoques terapéuticos para la enfermedad de Tay-Sachs |
| [28476546](https://pubmed.ncbi.nlm.nih.gov/28476546/) | 2017 | Historia natural/cohorte | Mol Genet Metab | Cronología clínica de las gangliosidosis infantiles; la terapia con miglustat está limitada por efectos gastrointestinales |
| [18618288](https://pubmed.ncbi.nlm.nih.gov/18618288/) | 2008 | Estudio piloto | J Inherit Metab Dis | Evaluación neurocognitiva en Tay-Sachs de inicio tardío como posible medida de resultado |
| [12808890](https://pubmed.ncbi.nlm.nih.gov/12808890/) | 2003 | Perfil del fármaco | Curr Opin Investig Drugs | Desarrollo de miglustat en Gaucher tipo 1 y en otros trastornos de glicolípidos, incluido Tay-Sachs |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1171176001 | YARGESA 100 MG CÁPSULAS DURAS EFG | Cápsula dura | No disponible en los datos |
| 90992 | MIGLUSTAT WAYMADE 100 MG CÁPSULAS EFG | Cápsula dura | No disponible en los datos |
| 02238001 | ZAVESCA 100 MG CÁPSULAS DURAS | Cápsula dura | No disponible en los datos |
| 1231737001 | OPFOLDA 65 MG CÁPSULAS DURAS | Cápsula dura | No disponible en los datos |
| 78987 | MIGLUSTAT ACCORD 100 MG CÁPSULAS DURAS EFG | Cápsula dura | No disponible en los datos |

Hay 7 autorizaciones vigentes en total (todas de principio activo único); se muestran las 5 principales.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proviene del prospecto): enfermedad del sistema nervioso periférico, neuropatía periférica y enfermedad con función renal alterada.
- **Interacciones farmacológicas** (2 registros):
  - Imiglucerasa: interacción de nivel moderado.
  - Diana farmacológica: UDP-glucosa ceramida glucosiltransferasa (UGCG), mecanismo de acción esperado y no una interacción adversa.
- Consultar el prospecto para el resto de la información de seguridad, incluidas advertencias y contraindicaciones oficiales.
- La literatura señala efectos secundarios gastrointestinales que limitan el uso de miglustat en gangliosidosis infantiles.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe plausibilidad mecanística (reducción de la síntesis de GM2), ensayos de Fase 2–4 en la población diana, un ECA y una revisión sistemática. Sin embargo, los ensayos son pequeños, centrados en seguridad y farmacocinética, con dos terminados anticipadamente, y los resultados de eficacia son inconsistentes.

**Para avanzar se necesita:**
- Revisar los textos completos del ECA (PMID 19346952) y de la revisión sistemática (PMID 37209042) para verificar la eficacia real.
- Obtener los resultados de NCT03822013 y NCT02030015 y las causas de su terminación.
- Confirmar el nivel de evidencia (L1 frente a un nivel inferior).
- Obtener el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones autorizadas) y datos del mecanismo de acción desde DrugBank.
- Definir un plan de monitoreo de seguridad (neuropatía periférica, función renal y tolerabilidad gastrointestinal).

---

*Otras predicciones del modelo (autosómica ictiosis, enfermedad de Krabbe, leucodistrofia metacromática, entre otras) carecen de ensayos clínicos y literatura (nivel L5, decisión Hold), por lo que no se desarrollan en este informe.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

