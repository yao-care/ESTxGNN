---
layout: default
title: Etanercept
parent: Solo predicción del modelo (L5)
nav_order: 311
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
monitor_inn: "ETANERCEPT"
predicted_indications: ["hypermobility of coccyx", "Kummell disease", "vertebral disease"]
description: "Etanercept: nueva indicación predicha, Hypermobility of coccyx (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 13 (comercializadas: 13)"
---

# Etanercept
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Etanercept: Hypermobility of coccyx
{: .text-alpha }

## Resumen en Una Frase

Etanercept es una proteína de fusión que bloquea el factor de necrosis tumoral (TNF) y se utiliza originalmente para la artritis psoriásica, la artritis reumatoide, la espondilitis anquilosante y la artritis idiopática juvenil.
El modelo TxGNN predice que podría ser efectivo para **vasculitis reumatoide**, pero la evidencia directa es muy limitada: **1 ensayo clínico** sin relación directa con la indicación y **20 publicaciones**, varias de las cuales describen vasculitis inducida por etanercept.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Hypermobility of coccyx |
| Puntaje de Predicción TxGNN | 0.9963 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 13 de 13) |
| Número de Autorizaciones | 13 (comercializadas: 13) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Etanercept (traducción no oficial): «El TNF es una citocina de origen natural que participa en las respuestas inflamatorias e inmunitarias normales. Desempeña un papel importante en los procesos inflamatorios de la AR, la AIJ poliarticular, la APs y la EA, y en la patología articular resultante. […] El etanercept es una forma soluble dimérica del receptor p75 del TNF que puede unirse a moléculas de TNF.» Texto original en inglés: "TNF is a naturally occurring cytokine that is involved in normal inflammatory and immune responses. It plays an important role in the inflammatory processes of RA, polyarticular JIA, PsA, and AS and the resulting joint pathology. […] Etanercept is a dimeric soluble form of the p75 TNF receptor that can bind TNF molecules." ([DailyMed: Enbrel (etanercept) prescribing information, Immunex Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a002b40c-097d-47a5-957f-7a7b1807af7f), versión del 2026-05-11; consultado el 2026-11-19). Según la información conocida, etanercept es una proteína de fusión del receptor soluble de TNF unida a la fracción Fc de la IgG1, que neutraliza el TNF-alfa. Su eficacia en artritis reumatoide y otras artritis inflamatorias está establecida.

La vasculitis reumatoide es una de las manifestaciones extraarticulares más graves de la artritis reumatoide, una indicación ya aprobada. Por ello, el bloqueo del TNF es biológicamente plausible. Una revisión sistemática de 2021 (PMID 33058033) evalúa el uso de fármacos biológicos en esta enfermedad.

Sin embargo, la literatura también muestra una señal contraria: se han descrito casos de vasculitis cutánea, nefropatía y otros eventos tipo vasculitis asociados a etanercept, lo que sugiere que los inhibidores del TNF pueden inducir vasculitis de forma paradójica. Además, el bloqueo del TNF no ha mostrado beneficio claro en la vasculitis asociada a ANCA. El único ensayo vinculado trata del manejo perioperatorio de inmunosupresores y no evalúa etanercept en vasculitis.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Fase 2 | Reclutando | 80 | Manejo perioperatorio de inmunosupresores en pacientes reumatológicos sometidos a artroplastia total de hombro; evalúa brotes, dolor y complicaciones. No evalúa etanercept en vasculitis (relación indirecta). |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Revisión sistemática | Clinical Rheumatology | Revisión del uso de fármacos biológicos en vasculitis reumatoide, una complicación grave de la artritis reumatoide. |
| [28391344](https://pubmed.ncbi.nlm.nih.gov/28391344/) | 2017 | Revisión | Nephrology Dialysis Transplantation | Discute si el bloqueo del TNF-alfa tiene papel en la vasculitis asociada a ANCA y la glomerulonefritis. |
| [16624928](https://pubmed.ncbi.nlm.nih.gov/16624928/) | 2006 | Revisión | J Am Soc Nephrol | Papel del TNF-alfa en la vasculitis asociada a ANCA, con lecciones de otras enfermedades inflamatorias crónicas. |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Estudio de cohortes | RMD Open | Riesgo de eventos tipo lupus y tipo vasculitis en pacientes con AR tratados con inhibidores del TNF (registro BSRBR-RA). |
| [31491879](https://pubmed.ncbi.nlm.nih.gov/31491879/) | 2019 | Metaanálisis en red | Int J Mol Sci | 36 ECA: los inhibidores del TNF, originales y biosimilares, reducen de forma similar la destrucción articular en AR. |
| [31632872](https://pubmed.ncbi.nlm.nih.gov/31632872/) | 2019 | Reporte de caso | Cureus | Nefropatía asociada a etanercept. |
| [10955351](https://pubmed.ncbi.nlm.nih.gov/10955351/) | 2000 | Reporte de caso | J Rheumatol | Primer caso de vasculitis leucocitoclástica por etanercept en AR grave. |
| [12209493](https://pubmed.ncbi.nlm.nih.gov/12209493/) | 2002 | Reporte de caso | Arthritis Rheum | Nodulosis acelerada y vasculitis tras etanercept en AR. |
| [25544845](https://pubmed.ncbi.nlm.nih.gov/25544845/) | 2014 | Reporte de caso | Case Rep Med | Vasculitis de grandes vasos en una paciente con AR bajo tratamiento anti-TNF. |
| [15853915](https://pubmed.ncbi.nlm.nih.gov/15853915/) | 2005 | Revisión | Scand J Immunol | Inmunología de la vasculitis cutánea asociada a etanercept e infliximab. |

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 1171195010 | ERELZI 50 MG SOLUCION INYECTABLE EN PLUMA PRECARGADA | SOLUCIÓN INYECTABLE EN JERINGA PRECARGADA | Sandoz Gmbh | Comercializada |
| 199126023 | ENBREL 25 MG SOLUCION INYECTABLE EN PLUMA PRECARGADA | SOLUCIÓN INYECTABLE EN PLUMA PRECARGADA | Pfizer Europe Ma Eeig | Comercializada |
| 99126013 | ENBREL 25 mg SOLUCION INYECTABLE EN JERINGAS PRECARGADAS | SOLUCIÓN INYECTABLE EN JERINGA PRECARGADA | Pfizer Europe Ma Eeig | Comercializada |
| 1171195003 | ERELZI 25 MG SOLUCION INYECTABLE EN JERINGA PRECARGADA | SOLUCIÓN INYECTABLE | Sandoz Gmbh | Comercializada |
| 99126020 | ENBREL 50 mg SOLUCION INYECTABLE EN PLUMAS PRECARGADAS | SOLUCIÓN INYECTABLE EN PLUMA PRECARGADA | Pfizer Europe Ma Eeig | Comercializada |
| 99126003 | ENBREL 25 mg POLVO Y DISOLVENTE PARA SOLUCION INYECTABLE | POLVO Y DISOLVENTE PARA SOLUCIÓN INYECTABLE | Pfizer Europe Ma Eeig | Comercializada |
| 1171195007 | ERELZI 50 MG SOLUCION INYECTABLE EN JERINGA PRECARGADA | SOLUCIÓN INYECTABLE EN JERINGA PRECARGADA | Sandoz Gmbh | Comercializada |
| 1151074002 | Benepali 50mg solucion inyectable en pluma precargada | SOLUCIÓN INYECTABLE EN PLUMA PRECARGADA | Samsung Bioepis Nl B.V. | Comercializada |
| 1201436005 | NEPEXTO 50 MG SOLUCION INYECTABLE EN PLUMA PRECARGADA | SOLUCIÓN INYECTABLE EN PLUMA PRECARGADA | Biosimilar Collaborations Ireland Limited | Comercializada |
| 1151074005 | BENEPALI 25 MG SOLUCION INYECTABLE EN JERINGA PRECARGADA | SOLUCIÓN INYECTABLE | Samsung Bioepis Nl B.V. | Comercializada |

Se muestran 10 de 13 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

Todas las autorizaciones son de monofármaco e incluyen Enbrel, Benepali, Erelzi y Nepexto.

<!-- review:begin es-lic-20261124b-etanercept-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Se muestran 5 de las 13 autorizaciones vigentes (todas monofármaco), que incluyen Enbrel, Benepali, Erelzi y Nepexto." Corregido: se elimina la descripción de las filas de la tabla anterior y el número de autorizaciones; se conserva el resto del contenido. La tabla de Información de Mercado en España se genera desde el 2026-11-24 por programa a partir de los datos de CIMA (AEMPS); las cifras actuales están en el Resumen rápido y bajo la tabla. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261124b-etanercept-1 -->

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (100 interacciones registradas; se listan las principales):
  - **Gravedad mayor:** corticoides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida, prednisona, prednisolona), deferiprona, iobenguano (I-131), ibritumomab tiuxetán y tositumomab (incluido el marcado con I-131).
  - **Gravedad moderada:** metronidazol, tinidazol, rosuvastatina y simvastatina.
  - **Gravedad menor:** sales de zinc (sulfato, acetato, gluconato).
- **Señales de la literatura:** se han descrito vasculitis cutánea, nefropatía y eventos tipo lupus asociados a inhibidores del TNF, además de infecciones (reactivación de tuberculosis, herpes zóster diseminado que simuló vasculitis).

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El mecanismo es plausible, pero no hay ensayos que evalúen etanercept en vasculitis reumatoide, y la literatura incluye reportes de vasculitis inducida por el propio fármaco. La evidencia se limita a revisiones y reportes de casos (L4).

**Para avanzar se necesita:**
- Evidencia clínica directa (ensayos o estudios observacionales controlados) de etanercept en vasculitis reumatoide
- Análisis comparativo del riesgo de vasculitis paradójica inducida por inhibidores del TNF
- Datos de advertencias y contraindicaciones del prospecto de la AEMPS
- Datos detallados del mecanismo de acción (MOA)
- Plan de monitoreo de seguridad (infecciones, cribado de tuberculosis, función renal)

**Nota sobre otras predicciones:** *inflamatoria espondilopatía* y *artritis reumatoide juvenil poliarticular* (L1, Proceed with Guardrails) corresponden a usos ya autorizados y no a un reposicionamiento real. *Hipermovilidad del coxis* y *enfermedad de Kümmell* carecen de evidencia (L5, Hold), y *enfermedad vertebral* es una categoría demasiado amplia que debe acotarse antes de evaluarse.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Enbrel (etanercept) prescribing information, Immunex Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a002b40c-097d-47a5-957f-7a7b1807af7f) |
| 2026-11-24 | Eliminado: descripción de la tabla anterior y número de autorizaciones; se conserva el resto | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

