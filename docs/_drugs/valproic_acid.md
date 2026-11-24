---
layout: default
title: Valproic Acid
parent: Solo predicción del modelo (L5)
nav_order: 837
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "Valproic acid"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia"]
description: "Valproic Acid: nueva indicación predicha, Neoplasia del nervio trigémino (trigeminal nerve neoplasm) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 14 (comercializadas: 11)"
---

# Valproic Acid
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Valproic Acid: Neoplasia del nervio trigémino (trigeminal nerve neoplasm)
{: .text-alpha }

## Resumen en Una Frase

El ácido valproico es un fármaco antiepiléptico de amplio espectro, utilizado originalmente para el tratamiento de la epilepsia, la epilepsia de ausencia y los episodios maníacos del trastorno bipolar.
El modelo TxGNN predice que podría ser efectivo para **neoplasia del nervio trigémino**, pero actualmente **no hay ensayos clínicos** y solo **1 publicación** (una serie de casos sobre el síndrome de Sturge-Weber, que no trata de esta indicación) está vinculada a la predicción. La evidencia es, en la práctica, solo la predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Neoplasia del nervio trigémino (trigeminal nerve neoplasm) |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 11 de 14; revocadas o suspendidas: 3) |
| Número de Autorizaciones | 14 (comercializadas: 11) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Valproic Acid (traducción no oficial): «El ácido valproico se disocia en el ion valproato en el tubo digestivo. No se han establecido los mecanismos por los que el valproato ejerce sus efectos antiepilépticos. Se ha sugerido que su actividad en la epilepsia está relacionada con el aumento de las concentraciones cerebrales de ácido gamma-aminobutírico (GABA).» Texto original en inglés: "Valproic acid dissociates to the valproate ion in the gastrointestinal tract. The mechanisms by which valproate exerts its antiepileptic effects have not been established. It has been suggested that its activity in epilepsy is related to increased brain concentrations of gamma-aminobutyric acid (GABA)." ([DailyMed: Valproic (valproic acid) prescribing information, Aphena Pharma Solutions - Tennessee, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=34a0d45a-4388-7d8b-e063-6394a90a6c3f), versión del 2025-05-23; consultado el 2026-11-19). Según la información conocida, el ácido valproico es un antiepiléptico de amplio espectro cuya eficacia en epilepsia está bien establecida. Su acción antiepiléptica se atribuye al refuerzo de la transmisión GABAérgica, al bloqueo de canales de sodio y a la modulación de canales de calcio tipo T. Además, es un inhibidor de la histona desacetilasa (HDAC1 figura como diana en los datos farmacológicos), y esta propiedad se investiga como estrategia en diversos cánceres e infección por VIH.

La relación entre la indicación original y la nueva es débil. La epilepsia es un trastorno neurológico funcional, mientras que la neoplasia del nervio trigémino es un tumor. El único vínculo mecanístico plausible es el efecto antitumoral preclínico de los inhibidores de HDAC, que es teórico y para el cual no se aporta evidencia específica en tumores del trigémino.

La única publicación vinculada (PMID 9157801) es una serie de 14 casos de síndrome de Sturge-Weber de 1997, un trastorno neurocutáneo vascular en el que el valproato se usa solo para controlar las convulsiones. No respalda la predicción. El puntaje alto proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

<!-- review:begin es-lic-20261105-valproic_acid-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Se muestran 5 de las 14 autorizaciones vigentes (todas de principio activo único, ninguna cancelada)." Eliminado: afirmaba que el medicamento no está autorizado o comercializado en España, o que sus autorizaciones están revocadas o suspendidas, lo que no coincide con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en España. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-valproic_acid-1 -->

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Serie de casos | Anales Españoles de Pediatría | Revisión de 14 casos de síndrome de Sturge-Weber en 25 años (características clínicas, evolución y respuesta terapéutica). No aborda tumores del nervio trigémino. |

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 60350 | DEPAKINE CRONO 500 mg COMPRIMIDOS DE LIBERACION PROLONGADA | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Sanofi Aventis S.A. | Comercializada |
| 60352 | DEPAKINE 100 mg/ml POLVO Y DISOLVENTE PARA SOLUCION INYECTABLE | POLVO Y DISOLVENTE PARA SOLUCIÓN INYECTABLE | Sanofi Aventis S.A. | Comercializada |
| 48828 | DEPAKINE 200 mg/ml SOLUCION ORAL | SOLUCIÓN ORAL | Sanofi Aventis S.A. | Comercializada |
| 68033 | ACIDO VALPROICO ALTAN 400 mg POLVO PARA SOLUCION INYECTABLE EFG | POLVO PARA SOLUCIÓN INYECTABLE | Altan Pharmaceuticals Sa | Comercializada |
| 84517 | ACIDO VALPROICO AUROVITAS 300 MG COMPRIMIDOS DE LIBERACION PROLONGADA EFG | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Aurovitas Spain, S.A.U. | Comercializada |
| 54470 | DEPAKINE 500 mg COMPRIMIDOS GASTRORRESISTENTES | COMPRIMIDO GASTRORRESISTENTE | Sanofi Aventis S.A. | Comercializada |
| 419721021-06-2011 | DEPAKINE CRONO 500 mg COMPRIMIDOS DE LIBERACION PROLONGADA | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Sanofi Aventis | Comercializada |
| 90007 | ACIDO VALPROICO SEACROSS 100 MG/ML SOLUCION INYECTABLE Y PARA PERFUSION | SOLUCIÓN INYECTABLE Y PARA PERFUSIÓN | Seacross Pharma (Europe) Limited | Comercializada |
| 60351 | DEPAKINE CRONO 300 mg COMPRIMIDOS DE LIBERACION PROLONGADA | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Sanofi Aventis S.A. | Comercializada |
| 84516 | ACIDO VALPROICO AUROVITAS 500 MG COMPRIMIDOS DE LIBERACION PROLONGADA EFG | COMPRIMIDO DE LIBERACIÓN PROLONGADA | Aurovitas Spain, S.A.U. | Comercializada |

Se muestran 10 de 14 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): trastornos de ansiedad, trastornos neuróticos, trastorno distímico, deficiencia de carbamoil fosfato sintetasa I, porfiria hereditaria y trastornos del metabolismo de porfirinas, enfermedad renal, piouréter, hiperargininemia, enfermedades hematológicas, pancreatitis, citrulinemia, trastorno cognitivo, enfermedad hepática, enfermedad de la vesícula biliar y trombocitopenia.
- **Interacciones farmacológicas**: la consulta se completó con un único registro, que corresponde a la interacción farmacológica con su diana HDAC1 (inhibición de histona desacetilasa 1), no a una interacción con otro medicamento.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5): no hay ensayos clínicos y la única publicación vinculada no trata de tumores del trigémino. Además, el perfil de contraindicaciones (hepáticas, hematológicas, pancreáticas) exige cautela en un contexto oncológico.

**Para avanzar se necesita:**
- Evidencia preclínica específica del efecto de inhibidores de HDAC/ácido valproico en tumores del nervio trigémino o tumores relacionados.
- Datos del mecanismo de acción y de advertencias y contraindicaciones del prospecto de la AEMPS.
- Una revisión de la literatura más específica sobre tumores del trigémino, ya que la publicación actual no es pertinente.
- Evaluación de seguridad para poblaciones con enfermedad hepática, trombocitopenia o riesgo de pancreatitis.

> Nota: entre las demás predicciones, la **neuralgia del trigémino** (puntaje 0,9983, nivel L4) cuenta con más respaldo bibliográfico.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | Eliminado: "Se muestran 5 de las 14 autorizaciones vigentes (todas de principio activo único, ninguna cancelada)" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Valproic (valproic acid) prescribing information, Aphena Pharma Solutions - Tennessee, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=34a0d45a-4388-7d8b-e063-6394a90a6c3f) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

