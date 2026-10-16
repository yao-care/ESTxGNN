---
layout: default
title: Teprotumumab
parent: Solo predicción del modelo (L5)
nav_order: 778
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Teprotumumab: nueva indicación predicha, Monosomía X (nivel de evidencia L5). Indicación original: Exoftalmos endocrino (según el grafo de conocimiento"
monitor_inn: "TEPROTUMUMAB"
predicted_indications: ["monosomy X", "esophageal varices with bleeding", "esophageal varices without bleeding", "mixed gonadal dysgenesis", "mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "Turner syndrome due to structural X chromosome anomalies", "mosaic monosomy X", "sex chromosome disorder of sex development", "varicose disease", "X chromosome number anomaly"]
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

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Teprotumumab: De Exoftalmos Endocrino a Monosomía X

## Resumen en Una Frase

Teprotumumab es un anticuerpo monoclonal anti-IGF-1R, originalmente utilizado para el tratamiento del exoftalmos endocrino (oftalmopatía tiroidea).
El modelo TxGNN predice que podría ser efectivo para **Monosomía X (síndrome de Turner)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Exoftalmos endocrino (según el grafo de conocimiento; el texto de indicación de la autorización no está disponible) |
| Nueva Indicación Predicha | Monosomía X |
| Puntaje de Predicción TxGNN | 99.79% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, teprotumumab es un anticuerpo monoclonal que bloquea el receptor del factor de crecimiento similar a la insulina tipo 1 (IGF-1R), y su eficacia en el exoftalmos endocrino es la base de su uso clínico.

Sin embargo, el análisis disponible **no identifica un vínculo mecanístico plausible** con la monosomía X. Se trata de un trastorno cromosómico (síndrome de Turner) cuyo manejo del crecimiento se basa en hormona de crecimiento; bloquear IGF-1R podría incluso ser contraproducente para el crecimiento. El puntaje alto (0.998) refleja la proximidad en el grafo de conocimiento, no evidencia biológica o clínica.

Cabe señalar que las demás predicciones de mayor puntaje (otras variantes del síndrome de Turner, trastornos del desarrollo sexual de origen cromosómico, várices esofágicas, enfermedad varicosa y trastornos mitocondriales) tampoco cuentan con ensayos, literatura ni justificación mecanística. Muchas parecen agruparse en torno al mismo conjunto de enfermedades del síndrome de Turner, lo que sugiere redundancia en la predicción.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1251941001 | TEPEZZA 500 MG polvo para concentrado para solución para perfusión (Amgen Europe B.V.) | Polvo para concentrado para solución para perfusión | No disponible en los datos compilados |

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
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

