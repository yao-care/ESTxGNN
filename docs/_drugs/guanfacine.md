---
layout: default
title: Guanfacine
parent: Solo predicción del modelo (L5)
nav_order: 388
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-24
monitor_inn: "Guanfacine"
predicted_indications: ["faciodigitogenital syndrome", "specific developmental disorder", "chondromyxoid fibroma", "trichotillomania", "manic bipolar affective disorder", "restless legs syndrome", "Tourette syndrome"]
description: "Guanfacine: nueva indicación predicha, Faciodigitogenital syndrome (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 11 (comercializadas: 11)"
---

# Guanfacine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

## Guanfacine: Faciodigitogenital syndrome
{: .text-alpha }

## Resumen en Una Frase

Guanfacina es un agonista alfa-2A adrenérgico, utilizado originalmente para el tratamiento de la hipertensión y del trastorno por déficit de atención e hiperactividad (TDAH).
El modelo TxGNN predice que podría ser efectiva para el **Síndrome de Tourette**,
con **2 ensayos clínicos** (uno de Fase 3 completado y uno de Fase 4 completado) y **19 publicaciones** que actualmente respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Faciodigitogenital syndrome |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 (ver nota) |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 11 de 11) |
| Número de Autorizaciones | 11 (comercializadas: 11) |
| Decisión Recomendada | Proceed with Guardrails |

> **Nota sobre el nivel de evidencia:** Los datos compilados asignan L1, pero según los criterios de este informe L1 exige ≥2 ECA de Fase 3 completados. Aquí solo hay un ECA de Fase 3 (n=35) y un estudio de Fase 4 (n=34), por lo que el nivel que corresponde es **L2**. La evidencia es directa pero de tamaño reducido.

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Guanfacine (traducción no oficial): «La guanfacina es un agonista central de los receptores adrenérgicos alfa 2A. La guanfacina no es un estimulante del sistema nervioso central (SNC). Se desconoce el mecanismo de acción de la guanfacina en el TDAH.» Texto original en inglés: "Guanfacine is a central alpha 2A -adrenergic receptor agonist. Guanfacine is not a central nervous system (CNS) stimulant. The mechanism of action of guanfacine in ADHD is not known." ([DailyMed: Guanfacine Extended-Release (guanfacine) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3ec4fed6-cafc-49a0-9540-8d70ac435769), versión del 2026-10-15; consultado el 2026-11-19). Según la información conocida, la guanfacina es un agonista selectivo de los receptores adrenérgicos alfa-2A (también interactúa con los subtipos alfa-2B y alfa-2C), lo que fortalece la señalización de las redes de la corteza prefrontal y reduce el tono noradrenérgico.

La indicación original (TDAH) y el síndrome de Tourette están estrechamente relacionados: cerca de la mitad de los niños con Tourette presentan TDAH comórbido, y los estimulantes pueden empeorar los tics. Los agonistas alfa-2 (clonidina, guanfacina) se consideran opciones de primera línea en niños con tics y TDAH concurrente, según guías europeas y revisiones.

Mecanísticamente, la modulación de los circuitos cortico-estriato-tálamo-corticales y la reducción de la descarga noradrenérgica podrían disminuir la gravedad de los tics y mejorar los síntomas de atención. El efecto sobre los tics es modesto en comparación con los antipsicóticos.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00004376](https://clinicaltrials.gov/study/NCT00004376) | Fase 3 | Completado | 35 | ECA doble ciego controlado con placebo de guanfacina en niños y adolescentes con síndrome de Tourette/tics crónicos y TDAH; evalúa seguridad y eficacia |
| [NCT01547000](https://clinicaltrials.gov/study/NCT01547000) | Fase 4 | Completado | 34 | Estudio piloto multicéntrico de guanfacina de liberación prolongada (Intuniv) en niños con Tourette; evalúa tolerabilidad y eficacia preliminar |

## Evidencia de Literatura

Se muestran las publicaciones más relevantes (guías y revisiones sistemáticas primero, luego estudios clínicos y de seguridad).

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34757514](https://pubmed.ncbi.nlm.nih.gov/34757514/) | 2022 | Guía clínica | Eur Child Adolesc Psychiatry | Guías europeas (v2.0) sobre tratamiento farmacológico del síndrome de Tourette y otros trastornos de tics |
| [27132945](https://pubmed.ncbi.nlm.nih.gov/27132945/) | 2016 | Revisión sistemática | J Child Psychol Psychiatry | Revisión de intervenciones para Tourette en niños y jóvenes |
| [34286606](https://pubmed.ncbi.nlm.nih.gov/34286606/) | 2021 | Revisión sistemática | J Psychopharmacol | Calidad de la evidencia del tratamiento farmacológico del Tourette en niños y adultos |
| [31061209](https://pubmed.ncbi.nlm.nih.gov/31061209/) | 2019 | Revisión sistemática | Neurology | Eficacia y riesgos de los tratamientos de tics en Tourette y trastornos crónicos de tics |
| [19625978](https://pubmed.ncbi.nlm.nih.gov/19625978/) | 2009 | Metaanálisis | J Am Acad Child Adolesc Psychiatry | Eficacia de distintos fármacos para TDAH y tics en niños con ambos trastornos |
| [12469007](https://pubmed.ncbi.nlm.nih.gov/12469007/) | 2002 | Estudio piloto doble ciego | Clin Neuropharmacol | Efectos neuropsiquiátricos de guanfacina en 24 niños con Tourette leve, 4 semanas, controlado con placebo |
| [7559307](https://pubmed.ncbi.nlm.nih.gov/7559307/) | 1995 | Experiencia clínica preliminar | J Am Acad Child Adolesc Psychiatry | Guanfacina en TDAH comórbido con Tourette, sin los efectos hipotensores o sedantes de la clonidina |
| [23473832](https://pubmed.ncbi.nlm.nih.gov/23473832/) | 2013 | Revisión | Eur J Paediatr Neurol | Opciones farmacológicas en Tourette con TDAH comórbido |
| [37378108](https://pubmed.ncbi.nlm.nih.gov/37378108/) | 2023 | Serie de casos | Cureus | Mejoría significativa en tres pacientes con Tourette tratados con guanfacina y aripiprazol |
| [16229000](https://pubmed.ncbi.nlm.nih.gov/16229000/) | 2006 | Serie de casos (seguridad) | Mov Disord | Síncope en 4 niños con Tourette tratados con guanfacina, probablemente por hipotensión o bradicardia |

## Información de Mercado en España

La guanfacina está comercializada en España con 11 autorizaciones vigentes, todas de monofármaco y en forma de comprimido de liberación prolongada. Los textos de indicación aprobada no están disponibles en los datos compilados.

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 1151040002 | Intuniv 1mg comprimidos de liberacion prolongada | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Takeda Pharmaceuticals International Ag Ireland Branch | Comercializada |
| 1241908006 | PAXNEURY 6 MG COMPRIMIDOS DE LIBERACION PROLONGADA | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Neuraxpharm Pharmaceuticals S.L. | Comercializada |
| 1241908003 | PAXNEURY 3 MG COMPRIMIDOS DE LIBERACION PROLONGADA EFG | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Neuraxpharm Pharmaceuticals S.L. | Comercializada |
| 1241908001 | PAXNEURY 1 MG COMPRIMIDOS DE LIBERACION PROLONGADA EFG | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Neuraxpharm Pharmaceuticals S.L. | Comercializada |
| 1241908004 | PAXNEURY 4 MG COMPRIMIDOS DE LIBERACION PROLONGADA EFG | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Neuraxpharm Pharmaceuticals S.L. | Comercializada |
| 1151040004 | Intuniv 2mg comprimidos de liberacion prolongada | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Takeda Pharmaceuticals International Ag Ireland Branch | Comercializada |
| 1241908005 | PAXNEURY 5 MG COMPRIMIDOS DE LIBERACION PROLONGADA | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Neuraxpharm Pharmaceuticals S.L. | Comercializada |
| 1241908007 | PAXNEURY 7 MG COMPRIMIDOS DE LIBERACION PROLONGADA | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Neuraxpharm Pharmaceuticals S.L. | Comercializada |
| 1151040006 | Intuniv 3mg comprimidos de liberacion prolongada | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Takeda Pharmaceuticals International Ag Ireland Branch | Comercializada |
| 1241908002 | PAXNEURY 2 MG COMPRIMIDOS DE LIBERACION PROLONGADA EFG | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Neuraxpharm Pharmaceuticals S.L. | Comercializada |

Se muestran 10 de 11 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

Entre las autorizaciones figuran las de Paxneury (1, 2, 3, 4, 5, 6 y 7 mg), de Neuraxpharm; Intuniv es de Takeda.

<!-- review:begin es-lic-20261124b-guanfacine-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Las otras 6 autorizaciones corresponden a Paxneury (2, 3, 4, 5, 6 y 7 mg), de Neuraxpharm;" Corregido: la frase hablaba de autorizaciones que no figuraban en la tabla anterior; según CIMA (AEMPS), Paxneury tiene presentaciones de 1 a 7 mg (siete autorizaciones). La tabla de Información de Mercado en España se genera desde el 2026-11-24 por programa a partir de los datos de CIMA (AEMPS). Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261124b-guanfacine-1 -->

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): atrofia multisistémica, síndrome de taquicardia postural ortostática, hipotensión ortostática y otros trastornos hipotensores, infarto de miocardio y trombosis coronaria, enfermedad arterial coronaria, trastorno cerebrovascular, bloqueo auriculoventricular y disociación auriculoventricular, enfermedad hepática, enfermedad de la vesícula biliar, enfermedad renal crónica e insuficiencia renal terminal, hemoglobinopatía, estreñimiento, y trastornos de ansiedad, neuróticos y distímicos.
- **Interacciones farmacológicas / farmacología:** se identificaron 3 interacciones de tipo farmacológico, correspondientes a la unión con los receptores adrenérgicos alfa-2A, alfa-2B y alfa-2C. No se dispone de interacciones con otros fármacos con nivel de gravedad asignado.
- **Señales de seguridad en la literatura:** síncope (hipotensión o bradicardia) en niños con Tourette tratados con guanfacina; casos de reacción maníaca en niños; pausa sinusal en un caso de sobredosis combinada con olanzapina.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe evidencia directa de un ECA de Fase 3 y un estudio de Fase 4 completados, además de guías europeas que recogen los agonistas alfa-2 como opción en tics con TDAH comórbido, y el fármaco ya está comercializado en España. Sin embargo, los ensayos son pequeños (n=35 y n=34) y el efecto sobre los tics es modesto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones oficiales) y los textos de indicación aprobada.
- Completar los datos del mecanismo de acción.
- Resultados detallados de los dos ensayos y, de ser posible, un ECA de Fase 3 adicional con mayor tamaño muestral para confirmar eficacia sobre los tics.
- Plan de monitoreo: presión arterial, frecuencia cardíaca y sedación; evitar la suspensión brusca (riesgo de hipertensión de rebote); precaución con fármacos hipotensores o que prolonguen el QT.
- Vigilancia de síntomas maníacos en población pediátrica.

---

**Otras indicaciones predichas (para referencia):** Síndrome faciodigitogenital, fibroma condromixoide, tricotilomanía, síndrome de piernas inquietas y trastorno bipolar maníaco tienen evidencia nula o solo indirecta (L4–L5) y se recomienda mantenerlas en *Hold*. El "trastorno específico del desarrollo" queda como pregunta de investigación por solaparse con la indicación de TDAH. En el trastorno bipolar maníaco, además, hay informes de manía inducida por guanfacina en niños, lo que constituye una señal de seguridad y no un respaldo.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Guanfacine Extended-Release (guanfacine) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3ec4fed6-cafc-49a0-9540-8d70ac435769) |
| 2026-11-24 | «Las otras 6» → «Entre las autorizaciones figuran»; Paxneury también 1 mg | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

