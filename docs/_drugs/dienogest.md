---
layout: default
title: Dienogest
parent: 僅模型預測 (L5)
nav_order: 91
evidence_level: L5
indication_count: 10
---

# Dienogest
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

# Dienogest: De Endometriosis a Amenorrea

## Resumen en Una Frase

Dienogest es una progestina de cuarta generacion, conocida comercialmente como VISANNE, utilizada para el tratamiento de la endometriosis. El modelo TxGNN predice que podria ser efectivo para inducir **Amenorrea**, con **4 ensayos clinicos** y **6 publicaciones** que actualmente respaldan esta direccion, aunque derivados principalmente de estudios sobre endometriosis en los que la amenorrea es el efecto terapeutico buscado.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Endometriosis (uso conocido por evidencia clinica — VISANNE; no confirmado en registro oficial de licencias, ver nota abajo) |
| Nueva Indicacion Predicha | Amenorrea |
| Puntaje de Prediccion TxGNN | 99.71% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Espana | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

> Nota: `taiwan_regulatory.licenses` esta vacio y `drug.original_indications` no contiene datos formales. La indicacion "Endometriosis" se infiere de la evidencia clinica adjunta (ensayos VISANNE) y no de un registro oficial de autorizacion en Espana.

## Por que es Razonable esta Prediccion?

No se dispone de datos oficiales sobre el mecanismo de accion (MOA) en la ficha del farmaco. Segun la informacion conocida a partir de la literatura incluida en este informe, dienogest es una progestina de cuarta generacion con actividad progestagenica altamente selectiva y actividad androgenica minima, aprobada en numerosos paises para el tratamiento de la endometriosis.

El vinculo mecanistico con la amenorrea es directo: el objetivo terapeutico del dienogest en endometriosis es precisamente inducir un estado hipoestrogenico y amenorrea, suprimiendo la proliferacion del tejido endometrial ectopico y reduciendo el dolor pelvico asociado. Es decir, la "nueva indicacion" predicha por TxGNN no representa un mecanismo distante, sino un efecto farmacologico ya documentado y buscado en el uso actual del farmaco.

Por ello, la plausibilidad mecanistica es alta: la evidencia disponible no proviene de ensayos disenados especificamente para amenorrea como enfermedad primaria, sino de ensayos de endometriosis donde la amenorrea inducida por dienogest es un resultado clinico relevante y consistentemente reportado.

## Evidencia de Ensayos Clinicos

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02425462](https://clinicaltrials.gov/study/NCT02425462) | N/A | Completado | 895 | Estudio de cohorte observacional en mujeres asiaticas con endometriosis; evalua efectividad de dienogest en calidad de vida y seguridad a largo plazo en practica clinica real. |
| [NCT07204093](https://clinicaltrials.gov/study/NCT07204093) | N/A | Activo, no reclutando | 138 | Compara estradiol transdermico combinado con dienogest versus drospirenona, evaluando satisfaccion del paciente en tratamiento de endometriosis. |
| [NCT04495855](https://clinicaltrials.gov/study/NCT04495855) | N/A | Completado | 968 | VISANNE en practica clinica real; evalua control de sintomas y recurrencia tras tratamiento con dienogest en endometriosis. |
| [NCT07164183](https://clinicaltrials.gov/study/NCT07164183) | Fase 3 | Reclutando | 290 | Estudio de no inferioridad comparando Indinol Forto vs Visanne (dienogest) en tratamiento de endometriosis. |

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41329046](https://pubmed.ncbi.nlm.nih.gov/41329046/) | 2026 | Revision | Eur J Contracept Reprod Health Care | Dienogest 2 mg (progestina de 4a generacion) muestra alto ratio de inhibicion y transformacion endometrial; respalda su uso para inducir amenorrea en endometriosis. |
| [39090694](https://pubmed.ncbi.nlm.nih.gov/39090694/) | 2024 | Revision sistematica | BMC Pharmacol Toxicol | Analisis Bayesiano de eventos adversos asociados a dienogest en endometriosis y adenomiosis. |
| [29161960](https://pubmed.ncbi.nlm.nih.gov/29161960/) | 2018 | Estudio observacional (cohorte retrospectiva) | Reproductive Sciences | Uso prolongado (>12 meses) de dienogest en 514 mujeres con endometrioma ovarico; eficacia y seguridad a largo plazo. |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Revision | Rev Endocr Metab Disord | Revision del trasfondo endocrino de los tratamientos hormonales para endometriosis, incluyendo induccion de amenorrea. |
| [34918698](https://pubmed.ncbi.nlm.nih.gov/34918698/) | 2021 | Reporte de caso | Medicine | Caso de tumor de celulas de la granulosa en paciente con sindrome de ovario poliquistico; relevancia indirecta al eje hormonal ovarico. |
| [40543564](https://pubmed.ncbi.nlm.nih.gov/40543564/) | 2025 | Otro | J Pediatr Adolesc Gynecol | Visualizacion avanzada para anomalias Mullerianas; relevancia limitada y probablemente marginal para esta indicacion. |

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad. Cabe destacar que existe un vacio de datos de severidad **Blocking** (DG001: advertencias/contraindicaciones oficiales del prospecto en Espana no disponibles), lo que impide actualmente completar la evaluacion de seguridad inicial (S1).

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
El puntaje TxGNN es alto y el vinculo mecanistico con la amenorrea es solido, ya que corresponde al efecto terapeutico ya buscado en el tratamiento de endometriosis con dienogest. Sin embargo, no existe ningun ensayo con amenorrea como indicacion primaria (evidencia nivel L3, solo estudios observacionales/revisiones derivados de endometriosis), el farmaco no esta comercializado en Espana (0 autorizaciones), y existe un vacio de datos **Blocking** que impide la evaluacion de seguridad inicial.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha tecnica oficial (advertencias, contraindicaciones) para completar la evaluacion S1 (DG001)
- Confirmar el mecanismo de accion detallado via DrugBank (DG002)
- Evaluar la viabilidad regulatoria de comercializacion en Espana
- Considerar un ensayo o analisis retrospectivo con amenorrea como criterio de valoracion primario, en lugar de un efecto secundario de tratamiento de endometriosis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

