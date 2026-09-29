---
layout: default
title: Formoterol
parent: Solo predicción del modelo (L5)
nav_order: 243
evidence_level: L5
indication_count: 6
---

# Formoterol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Formoterol: De Broncodilatador Inhalado (Asma/EPOC) a Malformación Respiratoria

## Resumen en Una Frase

Formoterol es un agonista beta-2 de acción prolongada (LABA), comercializado en España en formas inhaladas. Los datos de autorización de AEMPS no incluyen el texto de la indicación, pero los ensayos asociados lo sitúan en asma y EPOC.
El modelo TxGNN predice que podría ser efectivo para **malformación respiratoria** con un puntaje muy alto (99.92 %).
Sin embargo, **ninguno de los 21 ensayos clínicos ni de las 10 publicaciones** recuperados estudia esta enfermedad: todos corresponden a asma, EPOC o enfermedad de vías aéreas pequeñas.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Malformación respiratoria |
| Puntaje de Predicción TxGNN | 99.92 % |
| Nivel de Evidencia | L5 (solo predicción del modelo; no hay estudios en esta indicación) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 7 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, formoterol es un agonista beta-2 de acción prolongada. Relaja el músculo liso de las vías aéreas y produce broncodilatación, y se usa habitualmente junto con corticoides inhalados o anticolinérgicos.

Este mecanismo podría aliviar síntomas de obstrucción del flujo aéreo en enfermedades estructurales de la vía aérea. Sin embargo, **no corrige una malformación**. El puntaje tan alto (0.999) refleja más probablemente la cercanía en el grafo de conocimiento con el asma y la EPOC que un vínculo biológico real con las malformaciones respiratorias.

La relación entre las indicaciones conocidas y la nueva es, por tanto, débil. Los ensayos y artículos encontrados tratan enfermedades adquiridas de la vía aérea (asma, EPOC, asma en fumadores), no anomalías congénitas. Esta predicción debe interpretarse como una asociación del modelo, sin respaldo mecanístico ni clínico demostrado.

## Evidencia de Ensayos Clínicos

Se recuperaron 21 ensayos. Ninguno estudia malformación respiratoria. Se muestran los 10 más informativos, todos en poblaciones con asma o EPOC:

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT05114434](https://clinicaltrials.gov/study/NCT05114434) | N/A | Desconocido | 40 | Terapia triple beclometasona/formoterol/glicopirronio y eficacia de la tos en EPOC moderada a grave |
| [NCT01620099](https://clinicaltrials.gov/study/NCT01620099) | Fase 4 | Completado | 60 | Piloto sobre afectación de vías aéreas pequeñas en asmáticos fumadores |
| [NCT00931385](https://clinicaltrials.gov/study/NCT00931385) | Fase 3 | Completado | 99 | Perfil de FEV1 a 24 horas de BI 1744 CL frente a Foradil (formoterol) en EPOC |
| [NCT05421598](https://clinicaltrials.gov/study/NCT05421598) | Fase 2 | Completado | 437 | Amlitelimab subcutáneo como terapia añadida en asma moderada a grave (ECA controlado con placebo) |
| [NCT03324607](https://clinicaltrials.gov/study/NCT03324607) | Fase 2/3 | Completado | 20 | Glicopirronio/formoterol (Bevespi) sobre ventilación e intercambio gaseoso en EPOC, con RM de 129Xe |
| [NCT01803555](https://clinicaltrials.gov/study/NCT01803555) | Fase 3 | Completado | 605 | Budesonida/formoterol Spiromax frente a Symbicort Turbohaler durante 12 semanas en asma persistente |
| [NCT02345161](https://clinicaltrials.gov/study/NCT02345161) | Fase 3 | Completado | 1811 | Triple combinación FF/UMEC/VI frente a budesonida/formoterol en EPOC durante 24 semanas |
| [NCT03888131](https://clinicaltrials.gov/study/NCT03888131) | Fase 3 | Completado | 750 | Beclometasona/formoterol (pMDI) frente a Symbicort en EPOC durante 24 semanas |
| [NCT01577082](https://clinicaltrials.gov/study/NCT01577082) | Fase 3 | Completado | 542 | CHF 1535 (beclometasona/formoterol) frente a beclometasona en asma no controlada |
| [NCT02127866](https://clinicaltrials.gov/study/NCT02127866) | Fase 2 | Completado | 211 | Glicopirronio (CHF 5259) añadido a Foster (beclometasona/formoterol) en asma no controlada |

## Evidencia de Literatura

Las 10 publicaciones recuperadas tratan asma, EPOC, enfermedad de vías aéreas pequeñas u otros temas. Ninguna trata malformación respiratoria:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [22541245](https://pubmed.ncbi.nlm.nih.gov/22541245/) | 2012 | ECA | J Allergy Clin Immunol | Seguridad a largo plazo y control del asma con budesonida/formoterol pMDI en pacientes afroamericanos |
| [35115339](https://pubmed.ncbi.nlm.nih.gov/35115339/) | 2022 | ECA cruzado | Eur Respir J | Comparación de efectos broncodilatadores, sistémicos y cardiovasculares entre dosis repetidas de budesonida/formoterol y salbutamol en asma estable |
| [40840693](https://pubmed.ncbi.nlm.nih.gov/40840693/) | 2026 | Revisión sistemática y metaanálisis | J Am Pharm Assoc | Seguridad y eficacia de budesonida/glicopirronio/formoterol frente a glicopirronio/formoterol en EPOC |
| [20528601](https://pubmed.ncbi.nlm.nih.gov/20528601/) | 2010 | Revisión | J Asthma | Revisión de eficacia y seguridad de budesonida/formoterol en aerosol para asma persistente |
| [24842803](https://pubmed.ncbi.nlm.nih.gov/24842803/) | 2014 | Revisión | Prog Neuropsychopharmacol Biol Psychiatry | Estrategias basadas en neurotransmisores para la disfunción cognitiva en síndrome de Down (relación indirecta con formoterol) |
| [30662579](https://pubmed.ncbi.nlm.nih.gov/30662579/) | 2018 | Cohorte | Can Respir J | Errores en el uso de inhaladores y resultados maternos y fetales en embarazadas asmáticas |
| [14738234](https://pubmed.ncbi.nlm.nih.gov/14738234/) | 2004 | Estudio experimental | Eur Respir J | Formoterol protege frente a los efectos inducidos por el factor activador de plaquetas en asma |
| [35034195](https://pubmed.ncbi.nlm.nih.gov/35034195/) | 2022 | Estudio fisiológico | Eur J Appl Physiol | Respuestas compensatorias ante el aumento de anomalías mecánicas en EPOC durante el sueño |
| [37691104](https://pubmed.ncbi.nlm.nih.gov/37691104/) | 2023 | Reporte de caso | J Med Case Rep | Enfermedad de vías aéreas pequeñas en síndrome post-COVID-19 agudo, seguimiento de tres años |
| [41686546](https://pubmed.ncbi.nlm.nih.gov/41686546/) | 2026 | Reporte de caso y revisión | Medicine | Micosis broncopulmonar alérgica por *Schizophyllum commune* en un paciente con cáncer de pulmón operado |

## Información de Mercado en España

Se muestran 5 de las 7 autorizaciones:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 61667 | OXIS TURBUHALER 9 microgramos/INHALACIÓN | Polvo para inhalación |
| 66573 | FORMOTEROL STADA 12 microgramos | Polvo para inhalación (cápsula dura) |
| 67037 | BRONCORAL NEO 12 microgramos/PULSACIÓN | Solución para inhalación en envase a presión |
| 62197 | FORADIL AEROLIZER 12 microgramos | Polvo para inhalación (cápsula dura) |
| 66558 | FORMOTEROL ALDO-UNION 12 microgramos | Polvo para inhalación (cápsulas duras) |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para malformación respiratoria descansa solo en el puntaje del modelo. No hay ensayos ni publicaciones que estudien esta enfermedad, y el mecanismo broncodilatador no explica un efecto sobre una anomalía estructural congénita.

**Para avanzar se necesita:**
- Definir si la malformación respiratoria es una condición tratable con un beneficio sintomático plausible, o solo un artefacto de cercanía en el grafo con asma y EPOC.
- Completar los datos de mecanismo de acción e indicaciones originales desde DrugBank.
- Obtener las advertencias y contraindicaciones del prospecto de AEMPS.
- Buscar estudios preclínicos o de casos específicos en malformaciones de la vía aérea que respalden la hipótesis.

**Nota sobre otras predicciones del mismo fármaco:** el modelo también predice enfermedad pulmonar obstructiva (nivel L1) y asma (nivel L1), con ensayos de Fase 3 y ECA grandes. Ambas son indicaciones ya establecidas, no reposicionamiento real. En asma, formoterol debe usarse siempre junto con un corticoide inhalado y no en monoterapia. Estas dos indicaciones son las mejor respaldadas del paquete de evidencia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

