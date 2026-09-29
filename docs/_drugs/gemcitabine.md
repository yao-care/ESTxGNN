---
layout: default
title: Gemcitabine
parent: Evidencia alta (L1-L2)
nav_order: 256
evidence_level: L1
indication_count: 10
---

# Gemcitabine
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **10** 
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

# Gemcitabina: De Cáncer de Páncreas a Carcinoma de Mama Femenino

## Resumen en Una Frase

La gemcitabina es un análogo de nucleósido que se usa como quimioterapia en adenocarcinoma de páncreas, cáncer de pulmón no microcítico y cáncer de ovario, y en combinación en cáncer de mama metastásico.
El modelo TxGNN predice que podría ser efectiva para el **carcinoma de mama femenino**, con **50 ensayos clínicos** recuperados (solo una parte evalúa gemcitabina en mama) y **20 publicaciones** que respaldan esta dirección.
Esta predicción no es un reposicionamiento en sentido estricto, porque la gemcitabina ya se usa en cáncer de mama metastásico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Adenocarcinoma de páncreas (monoterapia); cáncer de pulmón no microcítico, ovario y mama en combinación (fuente: datos farmacológicos, porque el texto de indicación de AEMPS está vacío) |
| Nueva Indicación Predicha | Carcinoma de mama femenino |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la farmacología general, la gemcitabina es un análogo de nucleósido que inhibe la síntesis de ADN en la fase S del ciclo celular. Los datos farmacológicos disponibles la asocian con las subunidades **RRM1** y **RRM2** de la ribonucleótido reductasa, una enzima necesaria para producir los nucleótidos que requiere la replicación del ADN.

Este mecanismo es citotóxico y no depende del órgano de origen, por lo que es aplicable a tumores sólidos muy distintos. La gemcitabina se usa en páncreas, pulmón y ovario, y en combinación con paclitaxel en cáncer de mama metastásico. La predicción hacia mama es coherente con un uso ya conocido, y por eso el puntaje del modelo es tan alto.

Los ensayos de fase 3 y fase 2 revisados evalúan la gemcitabina sobre todo en **combinaciones** (con paclitaxel, trastuzumab, docetaxel o capecitabina) y en **cáncer de mama metastásico o avanzado**.

---

## Evidencia de Ensayos Clínicos

Se listan los 10 ensayos más relevantes para gemcitabina en cáncer de mama. Los hallazgos se resumen a partir del diseño descrito en cada ensayo, porque el registro no incluye resultados.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00093795](https://clinicaltrials.gov/study/NCT00093795) | Fase 3 | Completado | 4894 | Tres regímenes adyuvantes en cáncer de mama con ganglios positivos; uno añade gemcitabina a paclitaxel tras AC de dosis densa |
| [NCT00006459](https://clinicaltrials.gov/study/NCT00006459) | Fase 3 | Completado | No disponible | Paclitaxel con o sin gemcitabina en cáncer de mama avanzado o metastásico |
| [NCT00561119](https://clinicaltrials.gov/study/NCT00561119) | Fase 3 | Completado | 326 | Mantenimiento frente a observación tras 6 ciclos de gemcitabina + paclitaxel en primera línea |
| [NCT00408408](https://clinicaltrials.gov/study/NCT00408408) | Fase 3 | Desconocido | 1206 | Terapia neoadyuvante: capecitabina o gemcitabina añadidas a docetaxel, con o sin bevacizumab; objetivo de respuesta patológica completa |
| [NCT00039546](https://clinicaltrials.gov/study/NCT00039546) | Fase 3 | Desconocido | No disponible | Estudio tAnGo: gemcitabina añadida a paclitaxel, epirrubicina y ciclofosfamida en adyuvancia |
| [NCT02252887](https://clinicaltrials.gov/study/NCT02252887) | Fase 2 | Completado | 45 | Gemcitabina + trastuzumab + pertuzumab en cáncer de mama metastásico HER2 positivo |
| [NCT01050322](https://clinicaltrials.gov/study/NCT01050322) | Fase 2 | Completado | 142 | Lapatinib con capecitabina, vinorelbina o gemcitabina en cáncer de mama HER2 amplificado tras taxanos |
| [NCT00006007](https://clinicaltrials.gov/study/NCT00006007) | Fase 2 | Completado | 59 | Pemetrexed + gemcitabina en cáncer de mama metastásico |
| [NCT00193063](https://clinicaltrials.gov/study/NCT00193063) | Fase 2 | Completado | 41 | Gemcitabina semanal + trastuzumab en cáncer de mama metastásico con sobreexpresión de HER2 |
| [NCT00110084](https://clinicaltrials.gov/study/NCT00110084) | Fase 2 | Completado | 50 | Nab-paclitaxel semanal + gemcitabina en cáncer de mama metastásico |

**Nota:** el ensayo NCT00942331 (fase 3, n=506) fue marcado con relevancia "A" en el registro, pero estudia carcinoma urotelial y no cáncer de mama. No se cuenta como evidencia para esta indicación.

---

## Evidencia de Literatura

No hay ECA entre las publicaciones recuperadas. Se listan revisiones y estudios clínicos.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [17462169](https://pubmed.ncbi.nlm.nih.gov/17462169/) | 2007 | Revisión sistemática | Health Technol Assess | Evalúa la efectividad clínica y el coste-efectividad de gemcitabina + paclitaxel en segunda línea tras antraciclinas |
| [15685819](https://pubmed.ncbi.nlm.nih.gov/15685819/) | 2004 | Revisión | Oncology (Williston Park) | Gemcitabina y paclitaxel son activos en cáncer de mama metastásico; en ensayos fase II respondieron 114 de 221 pacientes (52%) |
| [15685821](https://pubmed.ncbi.nlm.nih.gov/15685821/) | 2004 | Revisión | Oncology (Williston Park) | Gemcitabina con platinos en cáncer de mama metastásico, con beneficio clínico y tasas de respuesta |
| [15685820](https://pubmed.ncbi.nlm.nih.gov/15685820/) | 2004 | Revisión | Oncology (Williston Park) | Gemcitabina + docetaxel: mecanismos complementarios y toxicidades parcialmente no solapadas |
| [14768404](https://pubmed.ncbi.nlm.nih.gov/14768404/) | 2003 | Revisión | Oncology (Williston Park) | Combinaciones de gemcitabina, antraciclinas y taxanos en cáncer de mama avanzado |
| [14754469](https://pubmed.ncbi.nlm.nih.gov/14754469/) | 2004 | Revisión | Clin Breast Cancer | Fundamento y datos clínicos de gemcitabina + trastuzumab en HER2 positivo |
| [12722022](https://pubmed.ncbi.nlm.nih.gov/12722022/) | 2003 | Estudio fase II (presentación) | Semin Oncol | Gemcitabina + trastuzumab en cáncer de mama metastásico muy pretratado; efecto aditivo o sinérgico en líneas celulares |
| [41348333](https://pubmed.ncbi.nlm.nih.gov/41348333/) | 2025 | Estudio clínico | Breast Cancer Res Treat | Vinorelbina + gemcitabina cada dos semanas en cáncer de mama HR+/HER2- tras inhibidor de CDK4/6 |
| [40779028](https://pubmed.ncbi.nlm.nih.gov/40779028/) | 2025 | Ensayo fase I | Breast Cancer Res Treat | Carboplatino + gemcitabina + mifepristona en cáncer de mama avanzado y ovario recurrente |
| [12123338](https://pubmed.ncbi.nlm.nih.gov/12123338/) | 2002 | Farmacocinética | Ann Oncol | Interacciones farmacocinéticas y farmacodinámicas de gemcitabina, epirrubicina y paclitaxel en cáncer de mama avanzado |

---

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones. El registro no contiene texto de indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 73626 | Gemcitabina GP-Pharm 200 mg polvo para solución para perfusión EFG | Polvo para solución para perfusión | No disponible en el registro |
| 74479 | Gemcitabina Accord 2000 mg polvo para solución para perfusión | Polvo para solución para perfusión | No disponible en el registro |
| 71169 | Gemcitabina Accord 200 mg polvo para solución para perfusión EFG | Polvo para solución para perfusión | No disponible en el registro |
| 72981 | Gemcitabina Aurovitas 1000 mg concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en el registro |
| 76156 | Gemcitabina Accord 2000 mg concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en el registro |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antimetabolito, análogo de nucleósido) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal (recomendación general; confirmar en la ficha técnica) |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Señal en literatura:** existe un reporte de retinopatía inducida por gemcitabina (PMID 28961673, 2017). Se incluye solo como alerta y no está confirmado por el prospecto.

Consultar el prospecto para información de seguridad. El registro no incluye advertencias ni contraindicaciones de la ficha técnica de AEMPS. La consulta de interacciones solo devolvió dianas farmacológicas (RRM1 y RRM2), no interacciones con otros fármacos.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay varios ensayos de fase 3 completados que incluyen gemcitabina en cáncer de mama (NCT00093795, NCT00006459, NCT00561119), lo que sostiene el nivel L1. Sin embargo, el uso ya existe en mama metastásico y la evidencia se centra en combinaciones. Por eso el uso debe limitarse a los escenarios respaldados, por ejemplo cáncer de mama triple negativo (TNBC) y regímenes combinados.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), que es un vacío bloqueante para el cribado de seguridad.
- Confirmar el estado de la indicación en mama en las fichas técnicas españolas.
- Obtener datos del mecanismo de acción desde DrugBank.
- Verificar los resultados publicados de los ensayos de fase 3, porque el registro solo aporta su diseño.

**Otras predicciones del modelo:** el adenocarcinoma mixto endometrial, el adenocarcinoma mucinoso endometrial y el adenocarcinoma mucinoso cervical quedan como preguntas de investigación (L3). Las demás predicciones (recto, colon, vesícula, endometrio velloglandular, rete ovarii y endometrioide rico en mucina) quedan en espera (Hold), con evidencia L4-L5.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

