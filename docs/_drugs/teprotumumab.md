---
layout: default
title: Teprotumumab
parent: Solo predicción del modelo (L5)
nav_order: 778
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "TEPROTUMUMAB"
predicted_indications: ["monosomy X", "esophageal varices with bleeding", "esophageal varices without bleeding", "mixed gonadal dysgenesis", "mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "Turner syndrome due to structural X chromosome anomalies", "mosaic monosomy X", "sex chromosome disorder of sex development", "varicose disease", "X chromosome number anomaly"]
description: "Teprotumumab: nueva indicación predicha, Monosomía X (monosomy X) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 1 (comercializadas: 1)"
---

# Teprotumumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Teprotumumab: Monosomía X (monosomy X)
{: .text-alpha }

## Resumen en Una Frase

Teprotumumab es un anticuerpo monoclonal anti-IGF-1R, originalmente utilizado para el tratamiento del exoftalmos endocrino (oftalmopatía tiroidea).
El modelo TxGNN predice que podría ser efectivo para **Monosomía X (síndrome de Turner)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Monosomía X (monosomy X) |
| Puntaje de Predicción TxGNN | 0.9979 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Teprotumumab (traducción no oficial): «El mecanismo de acción del teprotumumab-trbw en pacientes con enfermedad ocular tiroidea no se ha caracterizado completamente. El teprotumumab-trbw se une al IGF-1R y bloquea su activación y señalización.» Texto original en inglés: "Teprotumumab-trbw's mechanism of action in patients with Thyroid Eye Disease has not been fully characterized. Teprotumumab-trbw binds to IGF-1R and blocks its activation and signaling." ([DailyMed: Tepezza (teprotumumab) prescribing information, Horizon Therapeutics USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3e6c54a1-cefd-4a5b-a855-ab9f268b6cce), versión del 2026-09-28; consultado el 2026-11-19). Según la información conocida, teprotumumab es un anticuerpo monoclonal que bloquea el receptor del factor de crecimiento similar a la insulina tipo 1 (IGF-1R), y su eficacia en el exoftalmos endocrino es la base de su uso clínico.

Sin embargo, el análisis disponible **no identifica un vínculo mecanístico plausible** con la monosomía X. Se trata de un trastorno cromosómico (síndrome de Turner) cuyo manejo del crecimiento se basa en hormona de crecimiento; bloquear IGF-1R podría incluso ser contraproducente para el crecimiento. El puntaje alto (0.9979) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica o clínica.

Cabe señalar que las demás predicciones de mayor puntaje (otras variantes del síndrome de Turner, trastornos del desarrollo sexual de origen cromosómico, várices esofágicas, enfermedad varicosa y trastornos mitocondriales) tampoco cuentan con ensayos, literatura ni justificación mecanística. Muchas parecen agruparse en torno al mismo conjunto de enfermedades del síndrome de Turner, lo que sugiere redundancia en la predicción.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 1251941001 | TEPEZZA 500 MG POLVO PARA CONCENTRADO PARA SOLUCION PARA PERFUSION | POLVO PARA CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Amgen Europe B.V. | Comercializada |

Se muestra la única autorización con este principio activo en los datos de CIMA (AEMPS).

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 45 interacciones de nivel moderado (fuente: DDInter). Las principales corresponden a antidiabéticos, entre ellos:
  - Metformina, pioglitazona, glimepirida, glipizida, glibenclamida y clorpropamida
  - Inhibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina, ertugliflozina)
  - Inhibidores de DPP-4 (alogliptina, saxagliptina, linagliptina)
  - Agonistas de GLP-1 (albiglutida, dulaglutida, semaglutida, exenatida)
  - Acarbosa e insulina humana

  Esto es coherente con el efecto del fármaco sobre el control glucémico, por lo que se requeriría vigilancia de la glucemia en pacientes diabéticos.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L5), sin ensayos ni literatura, y la biología del bloqueo de IGF-1R no respalda su uso en la monosomía X; incluso podría ser perjudicial para el crecimiento.

**Para avanzar se necesita:**
- Datos de mecanismo de acción (MOA) desde DrugBank
- Advertencias y contraindicaciones del prospecto de AEMPS
- Texto de indicación aprobada de la autorización española
- Estudios preclínicos o de mecanismo que justifiquen un vínculo entre IGF-1R y la indicación predicha
- Evaluación de si alguna otra indicación predicha (por ejemplo, de menor puntaje) tiene un fundamento biológico más sólido

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Tepezza (teprotumumab) prescribing information, Horizon Therapeutics USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3e6c54a1-cefd-4a5b-a855-ab9f268b6cce) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

