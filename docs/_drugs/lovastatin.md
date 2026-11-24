---
layout: default
title: Lovastatin
parent: Solo predicción del modelo (L5)
nav_order: 488
evidence_level: L5
indication_count: 1
monitor_inn: "Lovastatin"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-11-24
description: "Lovastatin: nueva indicación predicha, Deficiencia de la proteína de transferencia de ésteres de colesterol (nivel de evidencia L5). Indicación original: Hiperlipidemia y trastornos relacionados"
---

# Lovastatin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Lovastatina: De Hiperlipidemia a Deficiencia de la Proteína de Transferencia de Ésteres de Colesterol
{: .text-alpha }

## Resumen en Una Frase

Lovastatina es una estatina utilizada originalmente para tratar la hiperlipidemia y otras alteraciones lipídicas. El modelo TxGNN predice que podría ser efectiva para la **deficiencia de la proteína de transferencia de ésteres de colesterol (CETP)**, pero actualmente hay **0 ensayos clínicos** y **1 publicación** (un estudio preclínico en animales que no estudia directamente esta enfermedad). La predicción es, por ahora, solo una inferencia del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hiperlipidemia y trastornos relacionados (relación registrada en el grafo de conocimiento; los textos de indicación de las autorizaciones locales no están disponibles) |
| Nueva Indicación Predicha | Deficiencia de la proteína de transferencia de ésteres de colesterol |
| Puntaje de Predicción TxGNN | 0,9942 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 11; revocadas o suspendidas: 9) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Lovastatin (traducción no oficial): «El mecanismo del efecto reductor del LDL de la lovastatina puede implicar tanto la reducción de la concentración de VLDL-C como la inducción del receptor de LDL, lo que conduce a una menor producción y/o un mayor catabolismo del LDL-C. La apolipoproteína B también disminuye durante el tratamiento con lovastatina. La lovastatina es un inhibidor específico de la HMG-CoA reductasa, la enzima que cataliza la conversión de HMG-CoA en mevalonato.» Texto original en inglés: "The mechanism of the LDL-lowering effect of lovastatin may involve both reduction of VLDL-C concentration, and induction of the LDL receptor, leading to reduced production and/or increased catabolism of LDL-C. Apolipoprotein B also falls during treatment with lovastatin. Lovastatin is a specific inhibitor of HMG-CoA reductase, the enzyme which catalyzes the conversion of HMG-CoA to mevalonate." ([DailyMed: lovastatin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ac86821f-d741-4ab1-bd03-ce8797dd4f34), versión del 2026-11-13; consultado el 2026-11-19). Según la información conocida, lovastatina es una estatina que inhibe la HMG-CoA reductasa (HMGCR) y reduce el colesterol LDL. Los datos farmacológicos también registran una interacción con el receptor X de pregnano (NR1I2).

La deficiencia de CETP es un trastorno del metabolismo de las lipoproteínas caracterizado por HDL-C elevado. Las relaciones registradas en el grafo de conocimiento para lovastatina (hiperlipidemia, hipoalfalipoproteinemia, hiperlipidemia familiar) comparten este contexto de metabolismo lipídico, por lo que un vínculo a nivel de vía es plausible.

Sin embargo, no se ha demostrado ningún beneficio directo en la deficiencia de CETP. Esta condición es sobre todo un fenotipo bioquímico y no está claro que requiera tratamiento hipolipemiante. La puntuación alta del modelo es una inferencia, no evidencia clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [19965609](https://pubmed.ncbi.nlm.nih.gov/19965609/) | 2010 | Preclínico (modelo animal, knockout génico) | Journal of Lipid Research | La eliminación de StARD4, una proteína de transferencia de lípidos, produce una reducción modesta de peso y alteraciones menores del metabolismo lipídico. No estudia lovastatina ni la deficiencia de CETP. |

## Información de Mercado en España

Se listan las autorizaciones principales (la lista puede ser parcial; hay autorizaciones vigentes y otras canceladas). Los datos no incluyen el texto de indicación aprobada.

<!-- review:begin es-lic-20261124c-lovastatin-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Se listan las autorizaciones principales de las 20 registradas (la lista puede ser parcial; 11 vigentes y 9 canceladas entre las listadas)." Corregido: la cifra solo correspondía a las autorizaciones recogidas para este informe (una parte del total); según el listado completo de CIMA (AEMPS), datos del 2026-11-23, hay más autorizaciones con este principio activo. Las cifras recogidas están en el Resumen rápido y en la tabla de Información de Mercado en España. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261124c-lovastatin-1 -->

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 63359 | LOVASTATINA CINFA 40 mg COMPRIMIDOS EFG | COMPRIMIDO | Laboratorios Cinfa S.A. | Comercializada |
| 63361 | COLESVIR 20 mg COMPRIMIDOS | COMPRIMIDO | Industria Quimica Y Farmaceutica Vir S.A. | Comercializada |
| 63330 | LOVASTATINA VIR 20 mg COMPRIMIDOS EFG | COMPRIMIDO | Industria Quimica Y Farmaceutica Vir S.A. | Comercializada |
| 64438 | LOVASTATINA NORMON 40 mg COMPRIMIDOS EFG | COMPRIMIDO | Laboratorios Normon S.A. | Comercializada |
| 64034 | COLESVIR 40 mg COMPRIMIDOS | COMPRIMIDO | Industria Quimica Y Farmaceutica Vir S.A. | Comercializada |

Se muestran 5 de al menos 20 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas. Los datos de este informe solo incluyen parte de las autorizaciones.

<!-- licenses:end -->

## Consideraciones de Seguridad

No hay advertencias ni contraindicaciones de prospecto en los datos compilados. Consultar el prospecto para esa información.

- **Contraindicaciones registradas en el grafo de conocimiento** (no proceden de un prospecto): enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, hiperglucemia, úlcera péptica, miopatía y otras enfermedades musculares, rabdomiólisis, diabetes mellitus y cetoacidosis diabética, gota, trastornos de la coagulación, síndrome coronario agudo, infarto de miocardio, hipotensión, hipofosfatemia, entre otras.
- **Interacciones farmacológicas**: los datos disponibles son de farmacología de dianas (HMG-CoA reductasa y receptor X de pregnano), no interacciones clínicas con otros fármacos.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5): no hay ensayos clínicos ni estudios que analicen directamente la deficiencia de CETP con lovastatina, y no está claro que esta condición necesite tratamiento hipolipemiante.

**Para avanzar se necesita:**
- Confirmar la relevancia clínica de tratar la deficiencia de CETP y definir un resultado clínico objetivo
- Datos del mecanismo de acción y análisis de un vínculo mecanístico directo con la enfermedad
- Estudios preclínicos o clínicos que evalúen lovastatina en esta condición
- Obtener el prospecto de la AEMPS para analizar advertencias y contraindicaciones oficiales

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: lovastatin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ac86821f-d741-4ab1-bd03-ce8797dd4f34) |
| 2026-11-24 | «de las 20 registradas … 11 vigentes y 9 canceladas» → sin cifras | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

