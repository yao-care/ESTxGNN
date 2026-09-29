---
layout: default
title: Fluvastatin
parent: Evidencia alta (L1-L2)
nav_order: 240
evidence_level: L2
indication_count: 10
---

# Fluvastatin
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **10** 
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

# Fluvastatina: De Hipercolesterolemia a Hiperlipoproteinemia

## Resumen en Una Frase

Fluvastatina es una estatina (inhibidor de la HMG-CoA reductasa) que se usa para tratar la hipercolesterolemia y reducir el riesgo cardiovascular.
El modelo TxGNN predice que podría ser efectiva para **hiperlipoproteinemia**, con **5 ensayos clínicos** registrados (ninguno evalúa fluvastatina directamente) y **20 publicaciones**, varias de ellas ensayos aleatorizados con fluvastatina.
Al tratarse de una estatina ya comercializada, esta predicción es en la práctica un uso dentro de indicación y no un reposicionamiento en sentido estricto.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipercolesterolemia y reducción del riesgo cardiovascular (según datos farmacológicos; los textos de autorización de AEMPS no incluyen indicación) |
| Nueva Indicación Predicha | Hiperlipoproteinemia |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Fluvastatina inhibe la enzima HMG-CoA reductasa (gen *HMGCR*), paso limitante de la síntesis hepática de colesterol. Al reducir esa síntesis, el hígado aumenta los receptores de LDL y baja el colesterol LDL circulante. Es una coincidencia directa con los trastornos de las lipoproteínas.

La hiperlipoproteinemia es precisamente el tipo de alteración que esta vía corrige. Por eso, más que un salto entre enfermedades distintas, la predicción refleja que la indicación original y la nueva pertenecen al mismo espacio clínico, el de los lípidos elevados. La literatura respalda esta relación con estudios de fluvastatina en hipercolesterolemia primaria, hiperlipidemia mixta e hipercolesterolemia familiar.

Un matiz importante: los ensayos registrados en el paquete de evidencia estudian otros fármacos (alirocumab, lapaquistat, evolocumab). La evidencia directa proviene de la literatura publicada sobre fluvastatina, evaluada solo a partir de títulos y resúmenes.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00726362](https://clinicaltrials.gov/study/NCT00726362) | No aplica | Completado | 3270 | Vigilancia de la eficacia de estatinas comercializadas (incluye posiblemente fluvastatina) en hiperlipidemia en práctica clínica real; no se puede confirmar la inclusión de fluvastatina |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Fase 3 | Completado | 18 | Alirocumab en niños y adolescentes con hipercolesterolemia familiar homocigota; enfermedad afín, pero otro fármaco |
| [NCT00532311](https://clinicaltrials.gov/study/NCT00532311) | Fase 3 | Terminado | 411 | Lapaquistat (inhibidor de escualeno sintasa) junto con estatinas en hipercolesterolemia; sin datos de fluvastatina |
| [NCT04608474](https://clinicaltrials.gov/study/NCT04608474) | Fase 4 | Completado | 81 | Piloto de evolocumab (inhibidor de PCSK9) en receptores de trasplante renal; otro fármaco y otra población |
| [NCT01634906](https://clinicaltrials.gov/study/NCT01634906) | No aplica | Completado | 55 | Estudio mecanístico de apoB unida a eritrocitos tras retirar estatinas; no especifica la estatina y no es de eficacia |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11219479](https://pubmed.ncbi.nlm.nih.gov/11219479/) | 2001 | ECA | Clin Ther | Comparación de eficacia y tolerabilidad de fluvastatina de liberación prolongada (80 mg) frente a liberación inmediata en hipercolesterolemia primaria |
| [15598476](https://pubmed.ncbi.nlm.nih.gov/15598476/) | 2004 | ECA | Clin Ther | Fluvastatina + fenofibrato frente a fluvastatina sola durante 12 meses en hiperlipidemia combinada, diabetes tipo 2 y cardiopatía coronaria |
| [10856536](https://pubmed.ncbi.nlm.nih.gov/10856536/) | 2000 | ECA | Atherosclerosis | Estudio FACT: 333 pacientes con hiperlipidemia mixta y enfermedad coronaria; fluvastatina sola, bezafibrato solo o su combinación |
| [8157036](https://pubmed.ncbi.nlm.nih.gov/8157036/) | 1993 | ECA (doble ciego) | Eur J Clin Pharmacol | Eficacia y seguridad de fluvastatina a dosis altas en 52 pacientes con hipercolesterolemia familiar |
| [7604789](https://pubmed.ncbi.nlm.nih.gov/7604789/) | 1995 | Estudio clínico | Am J Cardiol | Efecto de fluvastatina sobre el perfil lipídico y las apolipoproteínas en 31 pacientes chinos con hipercolesterolemia |
| [10067240](https://pubmed.ncbi.nlm.nih.gov/10067240/) | 1998 | Estudio clínico comparativo | Ter Arkh | Variabilidad del efecto hipolipemiante de simvastatina y fluvastatina en hiperlipoproteinemia primaria |
| [7604807](https://pubmed.ncbi.nlm.nih.gov/7604807/) | 1995 | Estudio abierto | Am J Cardiol | Terapia triple (fluvastatina, bezafibrato, colestiramina) durante 60 semanas en 22 pacientes con hipercolesterolemia familiar grave |
| [9271817](https://pubmed.ncbi.nlm.nih.gov/9271817/) | 1997 | Estudio abierto | Thromb Res | Fluvastatina 40 mg durante 8 semanas en 20 pacientes con hiperlipidemia tipo IIa y IIb; efecto sobre lípidos y el inhibidor de la vía del factor tisular (TFPI) |
| [24944371](https://pubmed.ncbi.nlm.nih.gov/24944371/) | 2003 | Estudio abierto | Curr Ther Res | 24 semanas con dosis crecientes; efecto sobre subfracciones de LDL, LDL oxidada y moléculas de adhesión |
| [11347136](https://pubmed.ncbi.nlm.nih.gov/11347136/) | 2001 | Revisión | Nihon Rinsho | Monografía sobre fluvastatina (sin resumen disponible) |

---

## Información de Mercado en España

Los textos de indicación aprobada están vacíos en los registros de AEMPS recibidos, por lo que se muestra el fabricante en su lugar.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 72243 | Fluvastatina Farmalider 40 mg cápsulas duras EFG | Cápsula dura | Farmalider S.A. |
| 64648 | Lescol Prolib 80 mg comprimidos de liberación prolongada | Comprimido de liberación prolongada | Ethyx Pharmaceuticals |
| 71207 | Fluvastatina Kern Pharma 80 mg comprimidos de liberación prolongada EFG | Comprimido de liberación prolongada | Kern Pharma S.L. |
| 75532 | Fluvastatina Aristo 40 mg cápsulas duras EFG | Cápsula dura | Aristo Pharma Iberia S.L. |
| 69981 | Fluvastatina Teva 20 mg cápsulas duras EFG | Cápsula dura | Teva Pharma S.L.U. |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Fluvastatina es una estatina comercializada en España (20 autorizaciones) y existen varios ensayos aleatorizados publicados en hipercolesterolemia e hiperlipidemia mixta. La evidencia directa proviene de la literatura y no de ensayos registrados, y se ha evaluado solo por título y resumen. Por eso el nivel es L2 y no L1.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de AEMPS (advertencias y contraindicaciones), un vacío de datos bloqueante para el cribado de seguridad.
- Confirmar el diseño y los resultados de los ECA clave (PMID 11219479, 15598476, 10856536) mediante lectura del texto completo.
- Confirmar si NCT00726362 incluye fluvastatina.
- Definir medidas de resguardo: monitorizar enzimas hepáticas y síntomas de miopatía, y revisar interacciones vía CYP2C9.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

