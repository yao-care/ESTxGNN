---
layout: default
title: Azathioprine
parent: Solo predicción del modelo (L5)
nav_order: 59
evidence_level: L5
indication_count: 10
---

# Azathioprine
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

# Azatioprina: De Inmunosupresor Tiopurínico a Síndrome de Microftalmia Colobomatosa con Displasia Rizomélica

## Resumen en Una Frase

La azatioprina es un inmunosupresor, profármaco de la 6-mercaptopurina, comercializado en España. El modelo TxGNN predice como primera indicación el **síndrome de microftalmia colobomatosa con displasia rizomélica** (puntaje 99.9994%), pero **no hay ningún ensayo clínico ni publicación** que respalde esa predicción y no se identificó una base mecanística. Las predicciones con evidencia real son la **enfermedad inflamatoria intestinal** y la **colitis ulcerosa**, donde el uso ya está establecido y no supone un reposicionamiento novedoso.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Síndrome de microftalmia colobomatosa con displasia rizomélica |
| Puntaje de Predicción TxGNN | 99.9994% (posición 61 en el ranking del modelo) |
| Nivel de Evidencia | L5 (solo predicción del modelo) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

Los textos de indicación aprobada de las 4 autorizaciones vienen vacíos en el registro recibido, por lo que no se puede citar la indicación original oficial.

## ¿Por qué es Razonable esta Predicción?

**Para esta primera predicción no lo es.** La azatioprina es un profármaco de la 6-mercaptopurina. Sus nucleótidos de tioguanina inhiben la síntesis de purinas y, mediante la inhibición de Rac1, inducen apoptosis de linfocitos T activados. Es decir, actúa suprimiendo la respuesta inmune.

El síndrome de microftalmia colobomatosa con displasia rizomélica es una malformación del desarrollo ocular y esquelético, sin componente inmunomediado conocido. Por eso no se espera que responda a una inmunosupresión antimetabolito de purinas. El puntaje del modelo (0.99999) refleja una relación en el grafo de conocimiento, no una razón biológica. Lo mismo ocurre con otras predicciones de alto puntaje pero sin base clínica, como el síndrome de braquidactilia-sindactilia y la displasia acromesomélica tipo Hunter-Thompson.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

## Otras Indicaciones Predichas con Evidencia

Estas predicciones no son la primera del ranking, pero concentran toda la evidencia disponible en el paquete.

| Indicación predicha | Puntaje TxGNN | Nivel de evidencia | Recomendación |
|------|------|------|------|
| Enfermedad inflamatoria intestinal | 99.52% | L1 | Proceed with Guardrails |
| Colitis ulcerosa | 99.33% | L1 | Proceed with Guardrails |
| Osteoartritis | 99.40% | L4 | Hold |

**Interpretación.** En enfermedad inflamatoria intestinal (EII) y colitis ulcerosa, la azatioprina es un tratamiento establecido y respaldado por guías, incluidas las recomendaciones españolas del GETECCU (2018). Su valor aquí es confirmatorio, no un hallazgo nuevo. En la colitis ulcerosa la evidencia es más sólida para mantenimiento de la remisión que para inducción.

**Matiz sobre el nivel L1.** El nivel L1 se apoya en síntesis de ECA a nivel de literatura (revisiones Cochrane y metaanálisis). Entre los ensayos aportados, el único de Fase 3 completado con azatioprina como intervención central es NCT00946946 (n=78). El resto son estudios de Fase 4 o en los que la azatioprina es el brazo comparador.

### Ensayos clínicos seleccionados (EII y colitis ulcerosa)

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT07235904](https://clinicaltrials.gov/study/NCT07235904) | Fase 4 | Reclutando | 300 | Mirikizumab de inicio precoz frente al estándar con azatioprina en colitis ulcerosa moderada-grave de diagnóstico reciente |
| [NCT00946946](https://clinicaltrials.gov/study/NCT00946946) | Fase 3 | Completado | 78 | Azatioprina frente a mesalazina para prevenir recaídas clínicas en Crohn con recurrencia endoscópica posoperatoria |
| [NCT05040464](https://clinicaltrials.gov/study/NCT05040464) | Fase 3 | Reclutando | 166 | Azatioprina frente a metotrexato en combinación con adalimumab en enfermedad de Crohn |
| [NCT03101800](https://clinicaltrials.gov/study/NCT03101800) | Fase 3 | Desconocido | 84 | Azatioprina a dosis baja con alopurinol frente a azatioprina en monoterapia en colitis ulcerosa |
| [NCT02425852](https://clinicaltrials.gov/study/NCT02425852) | Fase 4 | Completado | 65 | Azatioprina más infliximab frente a corticoides más azatioprina en colitis aguda grave |
| [NCT03151525](https://clinicaltrials.gov/study/NCT03151525) | Fase 4 | Desconocido | 100 | En colitis ulcerosa en remisión profunda con infliximab: continuar o suspender y pasar a azatioprina |
| [NCT07248644](https://clinicaltrials.gov/study/NCT07248644) | Fase 4 | Aún sin reclutar | 304 | Mesalazina en monoterapia frente a continuar tiopurinas en pacientes ≥60 años con colitis ulcerosa en remisión sostenida |
| [NCT03393247](https://clinicaltrials.gov/study/NCT03393247) | N/A | Desconocido | 160 | Azatioprina desde el inicio o a las 14 semanas junto con infliximab en Crohn |
| [NCT02453607](https://clinicaltrials.gov/study/NCT02453607) | N/A | Desconocido | 225 | Relación entre niveles de metabolitos de 6-MP y farmacocinética de infliximab en Crohn (observacional) |
| [NCT01536535](https://clinicaltrials.gov/study/NCT01536535) | Fase 4 | Completado | 431 | Terapia inicial estandarizada en colitis ulcerosa pediátrica; la participación de tiopurinas no está verificada |

### Literatura seleccionada (EII y colitis ulcerosa)

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39586616](https://pubmed.ncbi.nlm.nih.gov/39586616/) | 2025 | ECA | Gut | Ensayo ACTIVE: infliximab de inicio precoz más azatioprina frente a azatioprina sola en colitis aguda grave respondedora a corticoides |
| [40013523](https://pubmed.ncbi.nlm.nih.gov/40013523/) | 2025 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Actualización sobre azatioprina y 6-mercaptopurina para mantener la remisión en colitis ulcerosa |
| [19392869](https://pubmed.ncbi.nlm.nih.gov/19392869/) | 2009 | Metaanálisis | Aliment Pharmacol Ther | Eficacia de azatioprina y mercaptopurina en colitis ulcerosa |
| [24117596](https://pubmed.ncbi.nlm.nih.gov/24117596/) | 2013 | Metaanálisis | Aliment Pharmacol Ther | Probar mercaptopurina es una estrategia segura en pacientes con EII intolerantes a azatioprina |
| [40538240](https://pubmed.ncbi.nlm.nih.gov/40538240/) | 2025 | Estudio comparativo (sin clasificar) | Aliment Pharmacol Ther | Azatioprina o tofacitinib como mantenimiento en colitis ulcerosa aguda grave respondedora a corticoides |
| [29357999](https://pubmed.ncbi.nlm.nih.gov/29357999/) | 2018 | Guía | Gastroenterol Hepatol | Recomendaciones del GETECCU sobre el uso de tiopurinas en EII |
| [29293971](https://pubmed.ncbi.nlm.nih.gov/29293971/) | 2018 | Revisión | J Crohns Colitis | Panorama actualizado del tratamiento con tiopurinas en EII |
| [16048561](https://pubmed.ncbi.nlm.nih.gov/16048561/) | 2005 | Revisión | J Gastroenterol Hepatol | Farmacogenética y monitorización de metabolitos de azatioprina y 6-MP en EII |
| [37586320](https://pubmed.ncbi.nlm.nih.gov/37586320/) | 2023 | Cohorte | Cell Rep Med | Blautia wexlerae intestinal favorece el fracaso de la azatioprina al reducir la biodisponibilidad de 6-MP |
| [30889246](https://pubmed.ncbi.nlm.nih.gov/30889246/) | 2019 | Estudio mecanístico | Inflamm Bowel Dis | La azatioprina induce autofagia mediante mTORC1 y PERK |

**Guardarraíles propuestos para EII y colitis ulcerosa:**
- Genotipado de TPMT y NUDT15.
- Monitorización de metabolitos.
- Vigilancia de mielosupresión y hepatotoxicidad.
- Asesoramiento sobre riesgo de linfoma y cáncer de piel.
- Revisión de interacciones (alopurinol, ribavirina, inhibidores de la ECA).

**Osteoartritis (L4, Hold).** No hay ensayos ni literatura que evalúen la azatioprina en esta enfermedad. Los resultados devueltos corresponden a artritis reumatoide, otras artritis inflamatorias o temas no relacionados. Además, el riesgo de mielosupresión y neoplasias es desfavorable para una enfermedad degenerativa no mortal.

**Predicciones biológicamente desaconsejables.** En el síndrome WHIM, la enfermedad granulomatosa crónica y la enfermedad granulomatosa con defecto de quimiotaxis neutrofílica, la azatioprina podría empeorar citopenias e infecciones.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 51003 | IMUREL 50 mg polvo para solución inyectable (Teofarma S.R.L.) | Polvo para solución inyectable | — |
| 50043 | IMUREL 50 mg comprimidos recubiertos con película (Teofarma S.R.L.) | Comprimido | — |
| 78164 | IMMUFALK 100 mg comprimidos recubiertos con película (Dr. Falk Pharma GmbH) | Comprimido recubierto con película | — |
| 78165 | IMMUFALK 75 mg comprimidos recubiertos con película (Dr. Falk Pharma GmbH) | Comprimido recubierto con película | — |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. La ficha técnica de la AEMPS aún no se ha incorporado a este análisis y no se encontraron interacciones registradas.

Como precaución general para la azatioprina, el análisis de predicciones señala riesgo de mielosupresión, hepatotoxicidad, infecciones y neoplasias (linfoma y cáncer de piel). Esto refuerza que no debe considerarse en enfermedades con inmunodeficiencia o citopenias previas.

## Conclusión y Próximos Pasos

**Decisión: Hold** (para la indicación de primera posición del ranking)

**Justificación:**
- La predicción principal no tiene ensayos, literatura ni mecanismo plausible. Es probablemente un artefacto del grafo, con nivel de evidencia L5.
- Las únicas señales sólidas son EII y colitis ulcerosa (L1, Proceed with Guardrails), pero corresponden a uso ya establecido, no a reposicionamiento nuevo.

**Para avanzar se necesita:**
- Descartar la indicación de rango 1 salvo que aparezca evidencia preclínica o mecanística independiente.
- Incorporar la ficha técnica de la AEMPS (advertencias y contraindicaciones), que actualmente es un vacío bloqueante para el cribado de seguridad.
- Obtener el texto de indicación aprobada de las 4 autorizaciones españolas.
- Completar los datos de mecanismo de acción en DrugBank.
- Si se prioriza EII o colitis ulcerosa, definir un plan de guardarraíles (TPMT/NUDT15, hemograma, enzimas hepáticas, metabolitos) y verificar los ensayos con título truncado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

