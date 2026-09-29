---
layout: default
title: Docetaxel
parent: Evidencia alta (L1-L2)
nav_order: 179
evidence_level: L1
indication_count: 10
---

# Docetaxel
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

# Docetaxel: De Indicación Original No Especificada a Carcinoma de Mama Femenino

## Resumen en Una Frase

Docetaxel es un citostático del grupo de los taxanos, comercializado en España como concentrado para perfusión. Los datos de autorización de la AEMPS recibidos no detallan su indicación original.
El modelo TxGNN predice que podría ser efectivo para **carcinoma de mama femenino**, con **50 ensayos clínicos** y **20 publicaciones** recuperados que respaldan esta dirección.
Esto es más una confirmación de un uso conocido que un reposicionamiento en sentido estricto.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de autorización recibidos |
| Nueva Indicación Predicha | Carcinoma de mama femenino |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, docetaxel estabiliza los microtúbulos, lo que bloquea su desensamblaje durante la mitosis. Esto provoca una detención del ciclo celular en G2/M y apoptosis en las células tumorales que se dividen rápidamente.

El cáncer de mama es un tumor bien establecido como sensible a los taxanes. Por eso el mecanismo citotóxico de docetaxel es directamente aplicable a esta enfermedad.

Como no hay indicaciones originales registradas en los datos, esta predicción se interpreta como confirmación de un uso ya conocido. El respaldo es amplio: hay ensayos de fase 3 con regímenes que incluyen docetaxel (por ejemplo, adriamicina/docetaxel frente a adriamicina/ciclofosfamida como adyuvancia) y numerosos ensayos de fase 2 neoadyuvantes y en enfermedad metastásica.

---

## Evidencia de Ensayos Clínicos

Se muestran 10 de los 50 ensayos recuperados, priorizando los de fase 3 y los de relevancia directa.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00003519](https://clinicaltrials.gov/study/NCT00003519) | Fase 3 | Completado | 2778 | Adriamicina/docetaxel frente a adriamicina/ciclofosfamida como tratamiento adyuvante en cáncer de mama con ganglios positivos o de alto riesgo |
| [NCT00017095](https://clinicaltrials.gov/study/NCT00017095) | Fase 3 | Completado | 1856 | Régimen con taxano frente a régimen sin taxano en cáncer de mama localmente avanzado o inflamatorio. Evalúa el valor predictivo de p53 |
| [NCT00408408](https://clinicaltrials.gov/study/NCT00408408) | Fase 3 | Desconocido | 1206 | Neoadyuvancia: efecto de añadir capecitabina o gemcitabina a docetaxel antes de AC, con o sin bevacizumab, sobre la respuesta patológica completa |
| [NCT00629278](https://clinicaltrials.gov/study/NCT00629278) | Fase 3 | Desconocido | 2500 | SHORT-HER: dos regímenes de quimioterapia adyuvante con 3 frente a 12 meses de trastuzumab en cáncer de mama HER2 positivo |
| [NCT00545688](https://clinicaltrials.gov/study/NCT00545688) | Fase 2 | Completado | 417 | Cuatro combinaciones de trastuzumab, docetaxel y pertuzumab en cáncer de mama HER2 positivo, con respuesta patológica completa como criterio principal |
| [NCT00841828](https://clinicaltrials.gov/study/NCT00841828) | Fase 2 | Completado | 102 | Epirrubicina/ciclofosfamida seguidas de docetaxel con trastuzumab frente a lapatinib en cáncer de mama HER2 positivo |
| [NCT02413320](https://clinicaltrials.gov/study/NCT02413320) | Fase 2 | Completado | 101 | Neoadyuvancia con carboplatino más docetaxel o paclitaxel, seguida de AC, en cáncer de mama triple negativo estadios I-III |
| [NCT00941330](https://clinicaltrials.gov/study/NCT00941330) | Fase 2 | Completado | 31 | Docetaxel-ciclofosfamida preoperatorio frente a exemestano en cáncer de mama con receptores hormonales positivos. Estudio directo pero pequeño |
| [NCT05189067](https://clinicaltrials.gov/study/NCT05189067) | Fase 2/3 | Desconocido | 190 | Paclitaxel más trastuzumab frente a docetaxel más trastuzumab adyuvantes en cáncer de mama HER2 positivo estadio I |
| [NCT00543829](https://clinicaltrials.gov/study/NCT00543829) | Fase 2 | Completado | 250 | Doxorrubicina intensificada más docetaxel, con o sin tamoxifeno, como terapia preoperatoria en carcinoma de mama operable |

---

## Evidencia de Literatura

Se muestran 10 de las 20 publicaciones recuperadas.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | ECA | J Clin Oncol | Ensayos ABC: docetaxel-ciclofosfamida (TC) frente a regímenes estándar con antraciclina y taxano en cáncer de mama precoz |
| [15161988](https://pubmed.ncbi.nlm.nih.gov/15161988/) | 2004 | Revisión | The Oncologist | Los taxanos, incluido docetaxel, son fármacos fundamentales en cáncer de mama metastásico, adyuvante y neoadyuvante |
| [7595719](https://pubmed.ncbi.nlm.nih.gov/7595719/) | 1995 | Revisión | J Clin Oncol | Revisión de los perfiles preclínico y clínico del taxoide docetaxel |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Revisión | Drug Ther Bull | Paclitaxel y docetaxel en cáncer de mama y de ovario |
| [11481357](https://pubmed.ncbi.nlm.nih.gov/11481357/) | 2001 | ECA fase IIb | J Clin Oncol | Doxorrubicina y docetaxel de dosis densa con G-CSF, con o sin tamoxifeno, como terapia preoperatoria en carcinoma de mama operable |
| [12599222](https://pubmed.ncbi.nlm.nih.gov/12599222/) | 2003 | Fase 2 | Cancer | Capecitabina con docetaxel y epirrubicina como primera línea en carcinoma de mama avanzado |
| [19856651](https://pubmed.ncbi.nlm.nih.gov/19856651/) | 2009 | Fase 1/2 | Tumori | Estudio de búsqueda de dosis de docetaxel y gemcitabina en carcinoma de mama metastásico |
| [15585076](https://pubmed.ncbi.nlm.nih.gov/15585076/) | 2004 | Fase 2 | Clin Breast Cancer | Docetaxel y cisplatino como quimioterapia primaria en cáncer de mama localmente avanzado |
| [26874836](https://pubmed.ncbi.nlm.nih.gov/26874836/) | 2017 | Estudio clínico | Breast Cancer | Docetaxel, ciclofosfamida y trastuzumab como quimioterapia neoadyuvante en cáncer de mama primario HER2 positivo |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | Cohorte retrospectiva | Anti-Cancer Drugs | Asociación entre quimioterapia adyuvante basada en docetaxel y linfedema relacionado con el cáncer de mama |

---

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones. Los datos recibidos no incluyen el texto de la indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 89109 | Docetaxel Tillomed 20 mg/ml concentrado para solución para perfusión EFG | Concentrado para solución para perfusión | Laboratorios Tillomed Spain S.L.U. |
| 112770005 | Docetaxel Kabi 20 mg/ml concentrado para solución para perfusión EFG | Concentrado para solución para perfusión | Fresenius Kabi Deutschland GmbH |
| 12770001 | Docetaxel Kabi 80 mg/4 ml concentrado para solución para perfusión EFG | Concentrado para solución para perfusión | Fresenius Kabi Deutschland GmbH |
| 89958 | Docetaxel Hikma 80 mg/4 ml concentrado para solución para perfusión EFG | Concentrado para solución para perfusión | Hikma Farmacêutica (Portugal) S.A. |
| 12769001 | Docetaxel Accord 20 mg/1 ml concentrado para solución para perfusión EFG | Concentrado para solución para perfusión | Accord Healthcare S.L.U. |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (clase taxano, estabilizador de microtúbulos) |
| Riesgo de Mielosupresión | Alto (la neutropenia es la toxicidad hematológica esperable en esta clase). Confirmar en el prospecto |
| Clasificación de Emetogenicidad | Baja a moderada, según la categoría del fármaco |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

Estos datos se basan en la clase del fármaco. El Evidence Pack no incluye datos de toxicidad, por lo que se debe consultar las advertencias y precauciones del prospecto.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay ensayos de fase 3 completados con regímenes que incluyen docetaxel en cáncer de mama, además de un ECA publicado y numerosos estudios de fase 2, por lo que la evidencia de eficacia es sólida (nivel L1). Sin embargo, faltan datos de seguridad y de la indicación aprobada, así que se recomienda avanzar con salvaguardas.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS para obtener advertencias, contraindicaciones e indicaciones aprobadas
- Completar los datos de mecanismo de acción e indicaciones originales desde DrugBank
- Confirmar la indicación de cáncer de mama en las fichas técnicas españolas
- Revisar los ensayos pendientes de clasificar, ya que la mayoría no tiene grado de relevancia asignado

**Nota sobre otras predicciones:** las demás indicaciones predichas tienen menos respaldo. Sarcoma de Ewing y rabdomiosarcoma llegan a L2 (fase 2 con gemcitabina-docetaxel). Los casos de carcinoma pulmonar de células pequeñas y de linfoma pulmonar primario parecen mezclados con cáncer de pulmón no microcítico. Las demás, sin ensayos ni literatura, quedan en espera (Hold).

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

