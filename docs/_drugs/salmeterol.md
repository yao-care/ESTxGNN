---
layout: default
title: Salmeterol
parent: 僅模型預測 (L5)
nav_order: 252
evidence_level: L5
indication_count: 7
---

# Salmeterol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Salmeterol: De Asma/EPOC a Bronquitis

## Resumen en Una Frase

Salmeterol es un agonista β2-adrenérgico de acción prolongada (LABA), cuyo uso establecido es el tratamiento de mantenimiento del asma y la enfermedad pulmonar obstructiva crónica (EPOC).
El modelo TxGNN predice que también podría ser efectivo para **Bronquitis**, con **16 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección — si bien, como se detalla más abajo, esta señal representa en gran medida una extensión de un uso ya consolidado del fármaco más que una hipótesis de reposicionamiento verdaderamente nueva.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Asma y EPOC (uso farmacológico establecido; no hay indicación registrada en la base de datos de autorizaciones española) |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción (MOA) de salmeterol en este Evidence Pack. Según la información conocida en la literatura recogida (p. ej. PMID 26051688), salmeterol es un agonista selectivo del receptor β2-adrenérgico de acción prolongada (LABA), indicado para el tratamiento de mantenimiento del asma persistente grave y la EPOC, produciendo broncodilatación sostenida durante al menos 12 horas.

La bronquitis crónica es, clínicamente, un subtipo/componente de la EPOC. El efecto broncodilatador de salmeterol, junto con su papel coadyuvante antiinflamatorio cuando se combina con un corticosteroide inhalado (ICS, como fluticasona), ya ha sido validado directamente en múltiples ensayos de Fase 3 y Fase 4 en pacientes con EPOC asociada a bronquitis crónica (p. ej. combinaciones como Advair/Seretide, indicadas expresamente para "EPOC asociada a bronquitis crónica" en EE. UU.).

Por lo tanto, la predicción de TxGNN para bronquitis no constituye una hipótesis de reposicionamiento novedosa, sino el reconocimiento de una relación fármaco-indicación que ya forma parte del perfil terapéutico central de salmeterol. Esto explica el alto volumen de evidencia (16 ensayos, 20 publicaciones) y el nivel L1 alcanzado.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02173691](https://clinicaltrials.gov/study/NCT02173691) | Fase 3 | Completado | 584 | Comparación directa de tiotropio vs. salmeterol vs. placebo en broncodilatación a 6 meses en EPOC |
| [NCT01332409](https://clinicaltrials.gov/study/NCT01332409) | N/A | Completado | 2000 | Estudio poscomercialización a gran escala de ADOAIR (salmeterol/fluticasona) en EPOC (bronquitis crónica/enfisema), con foco en seguridad (neumonía) |
| [NCT01110200](https://clinicaltrials.gov/study/NCT01110200) | Fase 4 | Completado | 639 | FSC (fluticasona/salmeterol) vs. salmeterol solo en tasa de exacerbaciones de EPOC tras alta hospitalaria |
| [NCT00857766](https://clinicaltrials.gov/study/NCT00857766) | Fase 4 | Completado | 249 | FSC vs. placebo, efecto sobre rigidez arterial en pacientes con EPOC |
| [NCT00064402](https://clinicaltrials.gov/study/NCT00064402) | Fase 3 | Completado | 741 | Broncodilatador de acción prolongada (arformoterol) como tratamiento de mantenimiento en EPOC, comparador activo/placebo |
| [NCT00403286](https://clinicaltrials.gov/study/NCT00403286) | Fase 2 | Completado | 457 | Búsqueda de dosis de fluticasona/formoterol frente al perfil de referencia de Advair (fluticasona/salmeterol) en EPOC |
| [NCT04655508](https://clinicaltrials.gov/study/NCT04655508) | Fase 3 | Terminado | 35 | FSC vs. placebo para mejorar la función respiratoria en niños con síndrome de bronquiolitis obliterante post-TCMH |
| [NCT00268177](https://clinicaltrials.gov/study/NCT00268177) | Fase 3 | Completado | 130 | Salmeterol/fluticasona vs. placebo sobre actividad antiinflamatoria bronquial en EPOC |
| [NCT00633217](https://clinicaltrials.gov/study/NCT00633217) | Fase 4 | Completado | 247 | Comparación de FSC en MDI-HFA vs. FSC Diskus en EPOC asociada a bronquitis crónica |
| [NCT05748977](https://clinicaltrials.gov/study/NCT05748977) | Fase Temprana 1 | Desconocido | 80 | Comparación de broncodilatadores inhalados (incl. salmeterol/tiotropio/fluticasona) en pacientes con EPOC de exacerbación frecuente |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15970448](https://pubmed.ncbi.nlm.nih.gov/15970448/) | 2006 | ECA | Pulm Pharmacol Ther | Efecto agudo de salmeterol vs. placebo sobre el aclaramiento mucociliar y por tos en pacientes con bronquitis crónica leve-moderada |
| [12970006](https://pubmed.ncbi.nlm.nih.gov/12970006/) | 2003 | ECA | Chest | Eficacia y seguridad de fluticasona/salmeterol (Diskus) vs. placebo y monoterapias en EPOC |
| [9916607](https://pubmed.ncbi.nlm.nih.gov/9916607/) | 1998 | ECA | Clin Ther | Eficacia y tolerabilidad de salmeterol inhalado vs. teofilina oral en EPOC leve-moderada |
| [19124357](https://pubmed.ncbi.nlm.nih.gov/19124357/) | 2008 | Cohorte/ECA | Ther Adv Respir Dis | Seguridad y tolerancia a 1 año de arformoterol y salmeterol en EPOC |
| [19210134](https://pubmed.ncbi.nlm.nih.gov/19210134/) | 2009 | Cohorte | Curr Med Res Opin | Uso sanitario y costes en pacientes con bronquitis crónica que inician FSC vs. otras terapias inhaladas de mantenimiento |
| [16915216](https://pubmed.ncbi.nlm.nih.gov/16915216/) | 2006 | Estudio de experiencia | MedGenMed | Manejo de EPOC asociada a bronquitis crónica con fluticasona/salmeterol (Advair Diskus 250/50) |
| [21225021](https://pubmed.ncbi.nlm.nih.gov/21225021/) | 2010 | Revisión | Drugs of Today | Contexto de bronquitis crónica en EPOC; roflumilast como comparador terapéutico, discute el papel de broncodilatadores como salmeterol |
| [21316553](https://pubmed.ncbi.nlm.nih.gov/21316553/) | 2010 | Revisión | Arch Bronconeumol | Perfil clínico de roflumilast en EPOC con bronquitis asociada; contextualiza terapias broncodilatadoras existentes |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Guía/Revisión | Basic Clin Pharmacol Toxicol | Guía finlandesa de diagnóstico y farmacoterapia de la EPOC estable, incluye LABA como salmeterol |
| [31852314](https://pubmed.ncbi.nlm.nih.gov/31852314/) | 2020 | ECA (metaanálisis) | J Int Med Res | Comparación de fluticasona/formoterol vs. fluticasona/salmeterol en asma pediátrica |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La bronquitis crónica es, en esencia, una extensión clínica de las indicaciones ya establecidas de salmeterol (asma/EPOC), respaldada por evidencia de nivel L1 —múltiples ECAs de Fase 3/4 y un estudio poscomercialización a gran escala (N=2000)—. Sin embargo, el fármaco no está comercializado en España (0 autorizaciones) y falta un dato clasificado como **Bloqueante** (DG001: advertencias/contraindicaciones del prospecto de la AEMPS), lo que impide completar la evaluación inicial de seguridad (S1).

**Para avanzar se necesita:**
- Obtener el prospecto/ficha técnica de la AEMPS con advertencias y contraindicaciones (DG001, bloqueante)
- Confirmar el mecanismo de acción detallado del fármaco (DG002)
- Evaluar la viabilidad regulatoria/comercial en España, dado que actualmente no tiene autorización
- Consultar datos de interacciones farmacológicas (DDI), no localizados en la consulta actual
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

