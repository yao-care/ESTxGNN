---
layout: default
title: Etanercept
parent: Solo predicción del modelo (L5)
nav_order: 215
evidence_level: L5
indication_count: 6
---

# Etanercept
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

# Etanercept: De una Indicación Original no Registrada a Vasculitis Reumatoide

## Resumen en Una Frase

Etanercept es una proteína de fusión (receptor de TNF-Fc) que bloquea el factor de necrosis tumoral alfa. Los registros de autorización aportados no incluyen el texto de su indicación original, pero la literatura lo describe como fármaco aprobado para artritis reumatoide, artritis idiopática juvenil, artritis psoriásica, espondilitis anquilosante y psoriasis en placas.
El modelo TxGNN predice que podría ser efectivo para **vasculitis reumatoide**, con **6 ensayos clínicos** y **20 publicaciones** asociados. Casi ninguna de estas fuentes evalúa la eficacia en esta enfermedad, y buena parte de la literatura describe vasculitis como efecto adverso del propio fármaco.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los registros aportados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Vasculitis reumatoide |
| Puntaje de Predicción TxGNN | 99,71% |
| Nivel de Evidencia | L3 (una revisión sistemática sobre biológicos en vasculitis reumatoide, sin resultados de eficacia disponibles; el paquete de evidencia asigna L4) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 13 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información conocida, etanercept es una proteína de fusión del receptor p75 del TNF con la porción Fc de la IgG1. Se une al TNF-alfa y neutraliza su actividad. Su eficacia está bien establecida en enfermedades inflamatorias articulares, especialmente la artritis reumatoide.

La vasculitis reumatoide es una de las manifestaciones extraarticulares más graves de la artritis reumatoide. Como el TNF-alfa participa en la inflamación vascular de la enfermedad reumatoide, es plausible mecanísticamente que su bloqueo ayude. Esto explica en parte el puntaje tan alto del modelo (0,997).

Sin embargo, la evidencia clínica no confirma esa plausibilidad. Los inhibidores del TNF, incluido etanercept, se han asociado repetidamente con vasculitis paradójica, como muestran series y reportes de caso. La revisión sistemática sobre terapia biológica en vasculitis reumatoide existe, pero los datos aportados no incluyen sus resultados. El único ensayo intervencionista con etanercept en una vasculitis (fase 2) se hizo en granulomatosis de Wegener, una vasculitis distinta, y no se dispone de sus resultados. Por eso la prioridad es evaluar la seguridad antes de considerar eficacia.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00001901](https://clinicaltrials.gov/study/NCT00001901) | Fase 2 | Completado | 60 | Etanercept en granulomatosis de Wegener (vasculitis ANCA, no vasculitis reumatoide). Único ensayo intervencionista en vasculitis; evidencia solo indirecta y sin resultados disponibles |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Fase 2 | Aún no reclutando | 80 | Manejo perioperatorio de inmunosupresores en pacientes reumatológicos sometidos a artroplastia de hombro; no prueba etanercept en vasculitis |
| [NCT01557322](https://clinicaltrials.gov/study/NCT01557322) | N/A | Completado | 1754 | Estudio observacional de vías de tratamiento en artritis reumatoide moderada (etanercept frente a terapias no biológicas); sin pregunta de eficacia en vasculitis |
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | Completado | 808 | Estudio transversal de patrones de uso de FAME biológicos en artritis reumatoide en China; sin desenlace de vasculitis |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completado | 184 | Estudio no intervencionista con tocilizumab en artritis reumatoide; otro fármaco y sin desenlace de vasculitis |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Desconocido | 750000 | Registro muy grande sobre riesgo de nuevas enfermedades inflamatorias inmunomediadas tras biológicos; útil para señales de seguridad, no para eficacia |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Revisión sistemática | Clinical Rheumatology | Revisión (PRISMA) sobre fármacos biológicos en vasculitis reumatoide; el resumen disponible no incluye resultados |
| [28391344](https://pubmed.ncbi.nlm.nih.gov/28391344/) | 2017 | Revisión | Nephrology Dialysis Transplantation | Analiza si el bloqueo del TNF-alfa tiene papel en la vasculitis y glomerulonefritis asociadas a ANCA |
| [15468348](https://pubmed.ncbi.nlm.nih.gov/15468348/) | 2004 | Revisión (seguridad) | The Journal of Rheumatology | Bloqueo del TNF-alfa y riesgo de vasculitis |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Cohorte / farmacovigilancia | RMD Open | Compara el riesgo de eventos tipo lupus y tipo vasculitis en pacientes con artritis reumatoide tratados con anti-TNF frente a FAME no biológicos (registro BSRBR-RA) |
| [15853915](https://pubmed.ncbi.nlm.nih.gov/15853915/) | 2005 | Serie de casos | Scandinavian Journal of Immunology | Inmunología de la vasculitis cutánea asociada a etanercept e infliximab |
| [12209493](https://pubmed.ncbi.nlm.nih.gov/12209493/) | 2002 | Reporte de caso | Arthritis & Rheumatism | Nodulosis acelerada y vasculitis tras etanercept en artritis reumatoide |
| [11792895](https://pubmed.ncbi.nlm.nih.gov/11792895/) | 2002 | Reporte de caso | Rheumatology (Oxford) | Vasculitis cutánea asociada a etanercept e infliximab |
| [15801034](https://pubmed.ncbi.nlm.nih.gov/15801034/) | 2005 | Reporte de caso | The Journal of Rheumatology | Nefritis lúpica proliferativa y vasculitis leucocitoclástica durante el tratamiento con etanercept |
| [25544845](https://pubmed.ncbi.nlm.nih.gov/25544845/) | 2014 | Reporte de caso | Case Reports in Medicine | Vasculitis de grandes vasos en un paciente con artritis reumatoide bajo terapia anti-TNF |
| [24854356](https://pubmed.ncbi.nlm.nih.gov/24854356/) | 2014 | Cohorte unicéntrica | Annals of the Rheumatic Diseases | Utilidad de las pruebas ANA de rutina para predecir lupus y vasculitis inducidos por FAME biológicos |

---

## Información de Mercado en España

Los registros aportados no incluyen el texto de indicación aprobada, por lo que la tabla no lo muestra. Se listan 5 de las 13 autorizaciones.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 1171195010 | ERELZI 50 mg solución inyectable en pluma precargada | Solución inyectable en jeringa precargada |
| 199126023 | ENBREL 25 mg solución inyectable en pluma precargada | Solución inyectable en pluma precargada |
| 99126013 | ENBREL 25 mg solución inyectable en jeringas precargadas | Solución inyectable en jeringa precargada |
| 1171195003 | ERELZI 25 mg solución inyectable en jeringa precargada | Solución inyectable |
| 99126020 | ENBREL 50 mg solución inyectable en plumas precargadas | Solución inyectable en pluma precargada |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Aparte, la literatura recogida en este informe describe vasculitis paradójica, nefropatía y autoinmunidad (lupus y anticuerpos antinucleares) asociadas a etanercept y otros anti-TNF. Estos datos son relevantes porque la indicación predicha es precisamente una vasculitis.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje del modelo es muy alto (99,71%), pero no hay ningún ensayo que pruebe etanercept en vasculitis reumatoide. La única evidencia directa es una revisión sistemática sin resultados disponibles, mientras que el resto de la literatura describe vasculitis como efecto adverso de los anti-TNF. Con este balance no se puede recomendar avanzar.

**Para avanzar se necesita:**
- Leer completa la revisión sistemática (PMID 33058033) y extraer sus resultados de eficacia y seguridad con biológicos, incluido el bloqueo del TNF.
- Obtener los resultados del ensayo NCT00001901 (etanercept en granulomatosis de Wegener) y valorar si son extrapolables.
- Completar las advertencias y contraindicaciones del prospecto de la AEMPS, hoy sin datos.
- Completar los datos del mecanismo de acción y del texto de indicación aprobada en los registros.
- Realizar una evaluación de seguridad específica sobre vasculitis paradójica con anti-TNF.

**Nota:** en el mismo paquete, "espondilopatía inflamatoria" y "artritis reumatoide juvenil poliarticular" tienen evidencia L1. Corresponden a usos ya establecidos del fármaco, no a reposicionamiento nuevo. Las predicciones "hipermovilidad del coxis" y "enfermedad de Kümmell" no tienen ensayos ni literatura, y el paquete las considera probables artefactos del grafo de conocimiento.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

