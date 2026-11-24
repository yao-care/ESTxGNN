---
layout: default
title: Fosfomycin
parent: Solo predicción del modelo (L5)
nav_order: 359
evidence_level: L5
indication_count: 8
monitor_inn: "fosfomycin"
predicted_indications: ["uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "epiglottitis", "urogenital tuberculosis", "laryngitis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "pyelitis"]
last_modified_at: 2026-11-24
description: "Fosfomycin: nueva indicación predicha, Uterine inflammatory disease (nivel de evidencia L5). En España, autorizaciones de la AEMPS: al menos 20"
---

# Fosfomycin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Fosfomycin: Uterine inflammatory disease
{: .text-alpha }

## Resumen en Una Frase

La fosfomicina es un antibiótico cuya relación principal registrada en el grafo de conocimiento es la infección del tracto urinario. El modelo TxGNN predice que podría ser efectiva para la **enfermedad inflamatoria uterina**. Esta predicción cuenta con **2 ensayos clínicos** y **1 publicación**, pero ninguno estudia directamente esa enfermedad, por lo que la evidencia real es muy limitada.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Uterine inflammatory disease |
| Puntaje de Predicción TxGNN | 0.9998 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 10; autorizadas no comercializadas: 2; revocadas o suspendidas: 8) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción. Según la información de la propia predicción, la fosfomicina inhibe la enzima MurA. Esta enzima participa en un paso temprano de la síntesis del peptidoglucano de la pared bacteriana. El fármaco tiene actividad amplia frente a patógenos urogenitales frecuentes.

La relación con la indicación original es plausible, porque las infecciones urinarias y las pélvicas o uterinas comparten parte de su flora bacteriana. Esa es la base de la predicción.

Sin embargo, la evidencia disponible es indirecta. Los dos ensayos son estudios farmacocinéticos pediátricos generales y no evalúan la enfermedad inflamatoria uterina. El único artículo trata sobre cistitis asociada a dienogest en mujeres con endometriosis, que es un problema urinario. Por tanto, la predicción es hoy solo una hipótesis mecanística.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | Completado | 3520 | Farmacocinética de fármacos poco estudiados administrados a niños según la práctica habitual. No tiene un objetivo sobre enfermedad inflamatoria uterina ni evalúa eficacia. |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Reclutando | 5000 | Plataforma general de farmacocinética y seguridad de fármacos poco estudiados en niños y jóvenes. No aborda esta indicación. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35653789](https://pubmed.ncbi.nlm.nih.gov/35653789/) | 2022 | Cohorte | J Obstet Gynaecol | Estudio prospectivo y controlado sobre la gravedad de la cistitis aguda y la bacteriuria en mujeres con endometriosis tras cirugía laparoscópica y tratamiento con dienogest o anticonceptivos orales combinados. Es un problema urinario y no estudia la enfermedad inflamatoria uterina. |

## Información de Mercado en España

Los textos de indicación aprobada no estaban disponibles en los datos compilados. Se muestran 5 autorizaciones vigentes:

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 84618 | FOSFOMICINA VIR 3 G GRANULADO PARA SOLUCION ORAL EN SOBRES EFG | GRANULADO PARA SOLUCIÓN ORAL EN SOBRE | Industria Quimica Y Farmaceutica Vir S.A. | Comercializada |
| 50880 | FOSFOCINA 250 MG/5 ML POLVO PARA SUSPENSION ORAL | POLVO PARA SUSPENSIÓN ORAL | Laboratorios Ern S.A. | Comercializada |
| 75651 | FOSFOMICINA KERN PHARMA 3 g GRANULADO PARA SOLUCION ORAL EFG | GRANULADO PARA SOLUCIÓN ORAL | Kern Pharma S.L. | Comercializada |
| 82353 | FOSFOMICINA CINFA 3 G GRANULADO PARA SOLUCION ORAL EN SOBRES EFG | GRANULADO PARA SOLUCIÓN ORAL | Laboratorios Cinfa S.A. | Comercializada |
| 77795 | FOSFOMICINA FARMALIDER 3 G GRANULADO PARA SOLUCION ORAL EFG | GRANULADO PARA SOLUCIÓN ORAL | Farmalider S.A. | Comercializada |

Se muestran 5 de al menos 20 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas. Los datos de este informe solo incluyen parte de las autorizaciones.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Contraindicaciones registradas en el grafo de conocimiento** (no proceden del texto del prospecto): enfermedad renal, piouréter, colitis por *Clostridium difficile* y enterocolitis necrotizante perinatal.
- **Interacciones farmacológicas** (3 detectadas):
  - Balsalazida: moderada.
  - Ácido picosulfúrico: moderada.
  - Metoclopramida: leve.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ningún estudio citado aborda directamente la enfermedad inflamatoria uterina. Los dos ensayos son farmacocinéticos generales y el artículo trata sobre cistitis. La predicción del modelo no basta por sí sola para avanzar, por lo que el nivel de evidencia es L5.

**Para avanzar se necesita:**
- Estudios clínicos o series de casos que evalúen la fosfomicina en infecciones uterinas o pélvicas.
- Datos de penetración tisular en útero y tejido pélvico.
- Datos detallados del mecanismo de acción y del espectro frente a los patógenos típicos de esta enfermedad.
- Las advertencias y contraindicaciones oficiales del prospecto de la AEMPS.
- Como alternativa, los datos del modelo señalan que la **pielitis**, otra indicación predicha, tiene una evidencia mucho más sólida (incluido un ensayo aleatorizado de fosfomicina intravenosa en infección urinaria complicada y pielonefritis aguda). Puede ser una candidata más prometedora para evaluar primero.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

