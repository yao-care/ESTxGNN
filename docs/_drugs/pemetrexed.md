---
layout: default
title: Pemetrexed
parent: Solo predicción del modelo (L5)
nav_order: 413
evidence_level: L5
indication_count: 10
---

# Pemetrexed
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Pemetrexed: Hacia Mesotelioma Peritoneal Maligno

## Resumen en Una Frase

Pemetrexed es un antifolato citotóxico comercializado en España en varias presentaciones para perfusión. Los registros de AEMPS del paquete de evidencia no incluyen el texto de su indicación original.
El modelo TxGNN predice que podría ser efectivo para **mesotelioma peritoneal maligno**, con **10 ensayos clínicos** y **20 publicaciones** que respaldan esta dirección. La evidencia es mayoritariamente observacional y de fases tempranas.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los registros de AEMPS recibidos (los textos de indicación vienen vacíos) |
| Nueva Indicación Predicha | Mesotelioma peritoneal maligno |
| Puntaje de Predicción TxGNN | 99,99 % |
| Nivel de Evidencia | L3 (ver nota) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Proceed with Guardrails |

> **Nota sobre el nivel de evidencia:** el paquete asigna L2, pero no hay ningún ECA de Fase 2/3 completado en el contexto peritoneal. El único ensayo completado es un Fase 2 de un solo brazo (NCT00061477). El resto son estudios retrospectivos, series de casos y revisiones, por lo que aplicando estrictamente los criterios corresponde L3.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la literatura y los ensayos incluidos, pemetrexed es un antifolato multidiana. Inhibe la timidilato sintasa, la dihidrofolato reductasa y la GARFT, enzimas clave en la síntesis de nucleótidos, y por tanto frena la división de células tumorales de proliferación rápida.

El mesotelioma pleural y el peritoneal comparten histología y dependencia de la vía del folato. Pemetrexed con platino es el tratamiento estándar de primera línea en el mesotelioma pleural. En el peritoneal se usa por extrapolación, ya que no existe un estándar sistémico establecido. Los estudios retrospectivos de pemetrexed más cisplatino como primera línea en mesotelioma peritoneal (Nagata 2019, Fujimoto 2017) apoyan esta práctica.

Como contexto, el mesotelioma pleural, otra indicación predicha, cuenta con ensayos de Fase 3 completados. Entre ellos están MAPS (NCT00651456) y CheckMate 743 (NCT02899299), donde pemetrexed-platino es la base o el comparador. Ese respaldo refuerza la plausibilidad biológica, pero no equivale a evidencia directa en localización peritoneal.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00061477](https://clinicaltrials.gov/study/NCT00061477) | Fase 2 | Completado | 48 | Pemetrexed + gemcitabina como primera línea en mesotelioma pleural o peritoneal; evalúa seguridad, supervivencia y respuesta tumoral |
| [NCT05001880](https://clinicaltrials.gov/study/NCT05001880) | Fase 2 | Reclutando | 66 | Aleatorizado: carboplatino, pemetrexed y bevacizumab con o sin atezolizumab en mesotelioma peritoneal; sin resultados |
| [NCT06543069](https://clinicaltrials.gov/study/NCT06543069) | Fase 2 | Reclutando | 28 | Brazo único: sintilimab y bevacizumab con pemetrexed y cisplatino en mesotelioma peritoneal irresecable |
| [NCT06057935](https://clinicaltrials.gov/study/NCT06057935) | Fase 2 | Reclutando | 64 | Quimioterapia intraperitoneal normotérmica vs. intravenosa tras citorreducción y HIPEC; el papel de pemetrexed no está claro |
| [NCT03875144](https://clinicaltrials.gov/study/NCT03875144) | Fase 2 | Suspendido | 66 | PIPAC (cisplatino + doxorrubicina) con quimioterapia sistémica (cisplatino + pemetrexed) vs. quimioterapia sola en primera línea |
| [NCT04462809](https://clinicaltrials.gov/study/NCT04462809) | Fase 2 | Desconocido | 40 | Mantenimiento con talazoparib tras platino-pemetrexed en mesotelioma pleural o peritoneal |
| [NCT02535312](https://clinicaltrials.gov/study/NCT02535312) | Fase 1/2 | Activo, no reclutando | 30 | TRC102 con cisplatino y pemetrexed en tumores sólidos y mesotelioma; el peritoneal es como mucho un subgrupo pequeño |
| [NCT02029690](https://clinicaltrials.gov/study/NCT02029690) | Fase 1 | Terminado | 85 | ADI-PEG 20 con pemetrexed y cisplatino en tumores mixtos; peritoneal solo en la cohorte de escalado de dosis |
| [NCT00402766](https://clinicaltrials.gov/study/NCT00402766) | Fase 1 | Completado | 19 | Cisplatino, pemetrexed e imatinib en mesotelioma maligno; dosis máxima tolerada, ensayo pequeño |
| [NCT01353482](https://clinicaltrials.gov/study/NCT01353482) | Fase 1/2 | Retirado | 0 | Vorinostat con pemetrexed-cisplatino; no reclutó pacientes, sin evidencia |

---

## Evidencia de Literatura

No se identificaron ECA específicos para localización peritoneal. Se priorizan los estudios clínicos sobre pemetrexed, seguidos de revisiones y casos.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31287877](https://pubmed.ncbi.nlm.nih.gov/31287877/) | 2019 | Estudio clínico | Jpn J Clin Oncol | Eficacia y seguridad de pemetrexed + cisplatino en primera línea en mesotelioma peritoneal avanzado |
| [28594258](https://pubmed.ncbi.nlm.nih.gov/28594258/) | 2017 | Retrospectivo | Expert Rev Anticancer Ther | Eficacia de pemetrexed + cisplatino en primera línea en mesotelioma peritoneal |
| [41133016](https://pubmed.ncbi.nlm.nih.gov/41133016/) | 2025 | Comparativo | Clin Med Insights Oncol | Compara pemetrexed-platino con gemcitabina-platino en primera línea; pemetrexed-platino es el régimen de referencia |
| [33743636](https://pubmed.ncbi.nlm.nih.gov/33743636/) | 2021 | Retrospectivo | BMC Cancer | Eficacia de la segunda línea y factores pronósticos en mesotelioma peritoneal avanzado |
| [38806763](https://pubmed.ncbi.nlm.nih.gov/38806763/) | 2024 | Cohorte multicéntrica | Ann Surg Oncol | Estrategias de tratamiento y resultados en una población heterogénea de mesotelioma peritoneal |
| [36765620](https://pubmed.ncbi.nlm.nih.gov/36765620/) | 2023 | Revisión | Cancers | Ruta diagnóstica y terapéutica; la citorreducción con HIPEC ofrece la mejor supervivencia en pacientes seleccionados |
| [35407498](https://pubmed.ncbi.nlm.nih.gov/35407498/) | 2022 | Revisión | J Clin Med | Tratamiento del mesotelioma peritoneal; cirugía citorreductora con HIPEC como opción inicial preferida |
| [30450291](https://pubmed.ncbi.nlm.nih.gov/30450291/) | 2018 | Revisión | Transl Lung Cancer Res | Revisión de una neoplasia muy rara con mal pronóstico y vínculo más débil con el asbesto que la pleural |
| [23291819](https://pubmed.ncbi.nlm.nih.gov/23291819/) | 2013 | Caso clínico | BMJ Case Rep | Respuesta a la reexposición a cisplatino + pemetrexed tras progresión, con revisión de literatura |
| [34723916](https://pubmed.ncbi.nlm.nih.gov/34723916/) | 2022 | Casos clínicos | J Immunother | Quimioinmunoterapia en dos pacientes con enfermedad no respondedora a platino |

---

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones. Los textos de indicación aprobada vienen vacíos en el registro recibido, por lo que se omite esa columna.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 86508 | Pemetrexed Sun 6 mg/ml solución para perfusión | Solución para perfusión | Sun Pharmaceutical Industries (Europe) B.V. |
| 80631 | Pemetrexed Tamarang 100 mg EFG | Polvo para concentrado para solución para perfusión | Tamarang S.A. |
| 87989 | Pemetrexed Aurovitas 500 mg EFG | Polvo para concentrado para solución para perfusión | Aurovitas Spain, S.A.U. |
| 80985 | Pemetrexed Tillomed 500 mg EFG | Polvo para concentrado para solución para perfusión | Laboratorios Tillomed Spain S.L. |
| 90206 | Pemetrexed Glenmark 500 mg EFG | Polvo para concentrado para solución para perfusión | Glenmark Arzneimittel GmbH |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antifolato multidiana) |
| Riesgo de Mielosupresión | Medio a alto (la neutropenia y otras citopenias son toxicidades limitantes habituales en esta clase); consultar el prospecto para el detalle |
| Clasificación de Emetogenicidad | Baja a moderada (según la clase del fármaco) |
| Ítems de Monitoreo | Hemograma con diferencial, función renal y hepática |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

Estos datos se basan en la clase farmacológica, no en datos de toxicidad del paquete de evidencia. Consultar las advertencias y precauciones del prospecto.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Pemetrexed más platino es una práctica establecida por extrapolación desde el mesotelioma pleural y cuenta con estudios clínicos y retrospectivos en enfermedad peritoneal. Sin embargo, no hay ECA específicos completados en localización peritoneal. Los ensayos aleatorizados actuales (NCT05001880, NCT06057935) siguen en curso y la evidencia directa es de nivel L3.

**Para avanzar se necesita:**
- Obtener la ficha técnica de AEMPS (advertencias, contraindicaciones y textos de indicación aprobada)
- Completar los datos del mecanismo de acción desde DrugBank
- Seguir los resultados de NCT05001880 y NCT06543069
- Definir la selección de pacientes: la citorreducción con HIPEC es preferente en quienes son candidatos quirúrgicos, y la quimioterapia sistémica se reserva para enfermedad avanzada
- Plan de monitoreo hematológico, renal y hepático

*Los resultados de este informe son solo para referencia de investigación y no constituyen consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

