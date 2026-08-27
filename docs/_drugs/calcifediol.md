---
layout: default
title: Calcifediol
parent: 僅模型預測 (L5)
nav_order: 52
evidence_level: L5
indication_count: 4
---

# Calcifediol
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

# Calcifediol: De Deficiencia de Vitamina D a Raquitismo Vitamina D-Dependiente

## Resumen en Una Frase

Calcifediol (25-hidroxivitamina D3) es el precursor metabolico directo de la vitamina D activa, utilizado clinicamente para corregir la deficiencia de vitamina D.
El modelo TxGNN predice que podria ser especialmente relevante para el **raquitismo vitamina D-dependiente tipo 1B** (deficiencia de la enzima 25-hidroxilasa),
con **2 ensayos clinicos de relevancia limitada** y **17 publicaciones**, en su mayoria estudios preclinicos y series de casos, respaldando esta direccion.

> **Nota metodologica**: este paquete de evidencia contiene 4 indicaciones candidatas (`TW-DB00146-multi`). La de mayor puntaje TxGNN ("obsolete vitamin D deficiency") esta marcada como termino obsoleto en la ontologia y no tiene ninguna evidencia asociada — se trata probablemente de ruido de clasificacion que redescubre la indicacion original del farmaco, no una indicacion nueva. Por ello, este informe se centra en el candidato con mejor fundamento mecanistico y evidencia real (raquitismo vitamina D-dependiente), y resume los demas candidatos en la tabla siguiente.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Deficiencia de vitamina D (uso clinico establecido; sin licencia registrada en Espana en este paquete) |
| Nueva Indicacion Predicha | Raquitismo vitamina D-dependiente (tipo 1B / deficiencia de 25-hidroxilasa) |
| Puntaje de Prediccion TxGNN | 99.18% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Espana | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

## Otras Indicaciones Candidatas en este Paquete

| Rango | Indicacion | Score TxGNN | Nivel de Evidencia | Recomendacion | Nota |
|------|------|------|------|------|------|
| 1 | Deficiencia de vitamina D (termino obsoleto) | 99.99% | L5 | Hold | Termino obsoleto en la ontologia, sin ensayos ni literatura; posible redundancia con la indicacion original |
| 2 | Acidosis tubular renal | 99.86% | L4 | Research Question | Suele coexistir con osteomalacia por deficit de vitamina D, pero calcifediol no actua sobre el mecanismo acido-base en si |
| 3 | Raquitismo hipofosfatemico hereditario | 99.76% | L4 | Research Question | La forma ligada al X se trata tradicionalmente con calcitriol, no calcifediol; relacion mecanistica moderada |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion en el registro formal del farmaco (`original_moa` marcado como vacio). Segun la informacion recogida en el paquete de evidencia, calcifediol es la forma 25-hidroxilada de la vitamina D3, el paso metabolico intermedio que el higado produce a partir de la vitamina D3 antes de que el rinon la convierta, mediante la enzima 1α-hidroxilasa (CYP27B1), en la forma hormonal activa (calcitriol).

El raquitismo vitamina D-dependiente tipo 1B es causado especificamente por un deficit de la enzima hepatica 25-hidroxilasa (CYP2R1) — es decir, el mismo paso metabolico que calcifediol sustituye de forma directa al administrarse ya hidroxilado. Esto lo diferencia de otras variantes del mismo grupo de enfermedades: el tipo I (deficit de 1α-hidroxilasa) y el tipo II (defecto del receptor de vitamina D) afectan pasos posteriores en la via, donde calcifediol aporta poco beneficio adicional. Por tanto, la solidez mecanistica de esta prediccion depende del subtipo genetico exacto del paciente, y es mayor para el tipo 1B que para el resto del espectro clinico agrupado bajo "raquitismo vitamina D-dependiente".

## Evidencia de Ensayos Clinicos

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03265483](https://clinicaltrials.gov/study/NCT03265483) | N/A | Completado | 180 | Evalua suplementacion con magnesio para revertir la resistencia a la vitamina D; la intervencion no es calcifediol, relevancia indirecta (grado C) |
| [NCT05214040](https://clinicaltrials.gov/study/NCT05214040) | N/A | Aun no reclutando | 300,000 | Estudio observacional de insuficiencia de vitamina D en pacientes hospitalizados; no especifico para raquitismo vitamina D-dependiente (grado C) |

Ningun ensayo clinico registrado evalua directamente calcifediol en pacientes con raquitismo vitamina D-dependiente.

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28548312](https://pubmed.ncbi.nlm.nih.gov/28548312/) | 2017 | Revision/Reporte de caso | J Bone Miner Res | Describe 7 pacientes de 2 familias con raquitismo tipo 1B por mutaciones en CYP2R1 (25-hidroxilasa), el subtipo mas directamente corregible con calcifediol |
| [233695](https://pubmed.ncbi.nlm.nih.gov/233695/) | 1978 | Serie de casos | J Clin Endocrinol Metab | Hermanos con raquitismo hereditario y malabsorcion de calcio corregida con dosis altas de 25-hidroxivitamina D |
| [9316302](https://pubmed.ncbi.nlm.nih.gov/9316302/) | 1997 | Revision | Acta Paediatr Jpn | Revision comparativa de raquitismo vitamina D-dependiente tipo I y II y su respuesta a metabolitos activos de vitamina D |
| [22145480](https://pubmed.ncbi.nlm.nih.gov/22145480/) | 2011 | Reporte de caso | J Pediatr Endocrinol Metab | Dos casos pediatricos que ilustran la dificultad diagnostica entre tipo 1 (defecto enzimatico) y tipo 2 (defecto de receptor) |
| [2982764](https://pubmed.ncbi.nlm.nih.gov/2982764/) | 1985 | Serie de casos | Isr J Med Sci | Respuesta clinica diferencial a metabolitos de vitamina D segun el tipo de raquitismo vitamina D-dependiente |
| [11693961](https://pubmed.ncbi.nlm.nih.gov/11693961/) | 2001 | Estudio mecanistico | Crit Rev Eukaryot Gene Expr | Rol de la vitamina D en la funcion osteoblastica y mineralizacion osea, con referencia a los tipos I y II |
| [8914979](https://pubmed.ncbi.nlm.nih.gov/8914979/) | 1996 | Estudio in vitro | FEBS Lett | Respuesta de macrofagos de pacientes con tipo II a metabolitos de vitamina D3 |
| [26483391](https://pubmed.ncbi.nlm.nih.gov/26483391/) | 2015 | Serie de casos/Revision | BMJ Case Rep | Complicaciones respiratorias graves de raquitismo por deficit de vitamina D en un lactante |
| [3089562](https://pubmed.ncbi.nlm.nih.gov/3089562/) | 1986 | Estudio animal | Calcif Tissue Int | Modelo en tamarinos con resistencia a 1,25-dihidroxivitamina D similar al tipo II humano |
| [6285251](https://pubmed.ncbi.nlm.nih.gov/6285251/) | 1982 | Reporte de caso | Padiatrie und Padologie | Caso de raquitismo transitorio resistente a vitamina D en diagnostico diferencial |

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad. No se dispone de advertencias, contraindicaciones ni datos de interacciones farmacologicas en este paquete de evidencia (busqueda de DDI sin resultados).

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La evidencia disponible es exclusivamente preclinica, mecanistica y de series de casos (L4); ningun ensayo clinico evalua calcifediol directamente en raquitismo vitamina D-dependiente, y falta informacion de seguridad regulatoria basica (TFDA) necesaria incluso para una evaluacion inicial S1.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha tecnica de TFDA con advertencias y contraindicaciones (gap bloqueante DG001)
- Confirmar el mecanismo de accion detallado via DrugBank u otra fuente regulatoria (gap DG002)
- Aclarar si "obsolete vitamin D deficiency" (rango 1) es ruido de clasificacion o representa un gap de datos real
- Priorizar estratificacion genotipica (CYP2R1 vs CYP27B1 vs receptor VDR) antes de disenar cualquier estudio prospectivo, dado que solo el subtipo 1B tiene fundamento mecanistico solido para calcifediol
- Evaluar si existen series de casos adicionales o registros de enfermedades raras que aporten evidencia real mas alla de lo preclinico
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

