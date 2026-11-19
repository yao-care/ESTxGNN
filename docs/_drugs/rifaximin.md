---
layout: default
title: Rifaximin
parent: Solo predicción del modelo (L5)
nav_order: 700
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-05
monitor_inn: "rifaximin"
predicted_indications: ["oral candidiasis", "commissural lip fistula", "osteoradionecrosis of the mandible", "oral leukoedema", "burning mouth syndrome", "candidiasis"]
description: "Rifaximin: nueva indicación predicha, Oral candidiasis (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 5 (comercializadas: 3; autorizadas no comercializadas: 2)"
---

# Rifaximin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Rifaximin: Oral candidiasis
{: .text-alpha }

## Resumen en Una Frase

Rifaximina es un antibiótico oral no absorbible, originalmente utilizado para el tratamiento de la encefalopatía hepática (y el coma hepático).
El modelo TxGNN predice que podría ser efectivo para **candidiasis oral**, pero **no hay ensayos clínicos** y solo **1 publicación** (un estudio de cohortes) relacionada, que además sugiere un posible riesgo en lugar de un beneficio.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Oral candidiasis |
| Puntaje de Predicción TxGNN | 0.9975 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 3 de 5; autorizadas no comercializadas: 2) |
| Número de Autorizaciones | 5 (comercializadas: 3) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Rifaximin (traducción no oficial): «La rifaximina es un fármaco antibacteriano. […] La rifaximina es un derivado semisintético de la rifampicina y actúa uniéndose a la subunidad beta de la ARN polimerasa dependiente de ADN bacteriana, bloqueando uno de los pasos de la transcripción. Esto da lugar a la inhibición de la síntesis de proteínas bacterianas y, en consecuencia, inhibe el crecimiento de las bacterias.» Texto original en inglés: "Rifaximin is an antibacterial drug. […] Rifaximin is a semi-synthetic derivative of rifampin and acts by binding to the beta-subunit of bacterial DNA-dependent RNA polymerase blocking one of the steps in transcription. This results in inhibition of bacterial protein synthesis and consequently inhibits the growth of bacteria." ([DailyMed: Xifaxan (rifaximin) prescribing information, Cardinal Health 107, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7afafa63-3236-4212-9589-045db6b01c0b), versión del 2025-08-27; consultado el 2026-11-19). Según la información conocida, rifaximina es un antibacteriano que apenas se absorbe y actúa en el intestino, modificando la microbiota intestinal. Su eficacia en la encefalopatía hepática está establecida, y se relaciona con la reducción de bacterias intestinales productoras de toxinas.

En este caso, la predicción **no resulta mecanísticamente convincente**. Rifaximina no tiene actividad antifúngica conocida, y la alteración de la microbiota intestinal podría incluso favorecer el sobrecrecimiento de hongos. El puntaje elevado (0,9975) probablemente refleja un artefacto del modelo TxGNN (aprendizaje profundo) y no una relación terapéutica real.

La única publicación disponible (PMID 34180023) asocia el uso de rifaximina con infecciones por *Candida* resistentes a micafungina en receptores de trasplante alogénico de progenitores hematopoyéticos. Es decir, constituye una señal de posible daño, no de beneficio terapéutico.

Otras indicaciones predichas (lesión fistulosa comisural del labio, osteorradionecrosis mandibular, leucoedema oral, síndrome de boca ardiente y candidiasis en general) tampoco cuentan con una justificación mecanística plausible, y sus niveles de evidencia son L5 (salvo candidiasis, L4), todas con recomendación Hold.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Cohorte | Annals of Hematology | En receptores de trasplante alogénico de progenitores hematopoyéticos, el uso de rifaximina (profilaxis para reducir infecciones intestinales y EICH aguda) se asoció con infecciones por *Candida* spp. resistentes a micafungina. Señal de riesgo, no de beneficio. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 62250 | SPIRAXIN 200 mg comprimidos recubiertos con película | Comprimido recubierto | No disponible en los datos |
| 12333201901 | SPIRAXIN 200 mg comprimidos recubiertos con película | Comprimido recubierto | No disponible en los datos |
| 77627 | TIXTAR 550 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos |
| 77626 | TIXTELLER 550 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos |
| 90543 | SPIRAXIN 400 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos |

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no proceden del prospecto): colitis por *Clostridium difficile* y enterocolitis necrosante perinatal.
- **Interacciones Farmacológicas**: se identificaron 69 interacciones. Entre las principales:
  - **Mayor**: vacuna viva de *Vibrio cholerae* (cepa CVD 103-HgR).
  - **Moderadas**: warfarina, ciclosporina, tolvaptán, cabozantinib, apalutamida, darolutamida, alpelisib, brigatinib, capmatinib, encorafenib, enasidenib, daclatasvir, ledipasvir, elagolix, elexacaftor, eliglustat, istradefilina, ácido bempedoico y ácido picosulfúrico.
- Además, la literatura disponible apunta a una posible señal de seguridad: mayor riesgo de infecciones por *Candida* resistentes a micafungina en pacientes trasplantados.

Para el resto de la información de seguridad (advertencias y contraindicaciones del prospecto), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de respaldo mecanístico y clínico: no hay ensayos, y la única publicación sugiere un posible perjuicio (infecciones por *Candida* resistentes) en lugar de beneficio. Rifaximina no tiene actividad antifúngica conocida; el puntaje alto proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones) de la AEMPS.
- Evidencia preclínica o clínica que demuestre un posible beneficio antifúngico o en candidiasis oral, descartando el sesgo de confusión por indicación.
- Evaluar con más detalle la señal de seguridad sobre infecciones fúngicas resistentes en poblaciones inmunodeprimidas.
- Considerar priorizar otras indicaciones con mayor plausibilidad biológica, dado que las demás predicciones actuales tampoco cuentan con evidencia.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Xifaxan (rifaximin) prescribing information, Cardinal Health 107, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7afafa63-3236-4212-9589-045db6b01c0b) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

