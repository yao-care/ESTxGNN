---
layout: default
title: Elafibranor
parent: Solo predicción del modelo (L5)
nav_order: 280
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
description: "Elafibranor: nueva indicación predicha, Amenorrea (nivel de evidencia L5). Indicación original: Colangitis biliar primaria (según los datos farmacológicos compilados"
monitor_inn: "ELAFIBRANOR"
predicted_indications: ["amenorrhea (disease)"]
---

# Elafibranor
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

## Elafibranor: De Colangitis Biliar Primaria a Amenorrea
{: .text-alpha }

## Resumen en Una Frase

Elafibranor es un agonista dual de los receptores PPARα y PPARδ, desarrollado inicialmente para la esteatohepatitis no alcohólica (NASH) y reposicionado después para la colangitis biliar primaria, indicación autorizada por la FDA (junio de 2024) y la EMA (septiembre de 2024).
El modelo TxGNN predice que podría ser efectivo para **amenorrea**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Colangitis biliar primaria (según los datos farmacológicos compilados; el texto de indicación de la autorización española está vacío) |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 0.9986 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Elafibranor es un agonista dual de PPARα y PPARδ (genes *PPARA* y *PPARD*). Se convierte en el hígado en su principal metabolito activo, GFT-1007. En estudios preclínicos redujo la acumulación de grasa hepática, la inflamación y la fibrosis. Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Elafibranor (traducción no oficial): «El elafibranor y su principal metabolito activo, GFT1007, son agonistas de los receptores activados por proliferadores de peroxisomas (PPAR), y ambos activan PPAR-alfa, PPAR-gamma y PPAR-delta in vitro. Sin embargo, no se conoce bien el mecanismo por el cual el elafibranor ejerce sus efectos terapéuticos en pacientes con CBP.» Texto original en inglés: "Elafibranor and its main active metabolite GFT1007 are peroxisome proliferator-activated receptor (PPAR) agonists, both of which activate PPAR-alpha, PPAR-gamma, and PPAR-delta in vitro. However, the mechanism by which elafibranor exerts its therapeutic effects in patients with PBC is not well understood." ([DailyMed: Iqirvo (elafibranor) prescribing information, Ipsen Biopharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d78aa14f-6ec1-4b1d-a4ae-e48658137a25), versión del 2026-08-11; consultado el 2026-11-19).

La relación con la amenorrea es especulativa. La señalización PPAR influye en el metabolismo de lípidos y glucosa y en la inflamación, y posiblemente en la función ovárica e hipotálamo-hipofisaria. Esto podría ser relevante para causas metabólicas y endocrinas de amenorrea, como la disfunción ovulatoria asociada al síndrome de ovario poliquístico. Ningún dato compilado respalda este vínculo.

Además, el puntaje tan alto (0.9986) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. Debe interpretarse con cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1241855001 | IQIRVO 80 MG comprimidos recubiertos con película (Ipsen Pharma) | Comprimido recubierto con película | No disponible en el texto de la autorización |

## Consideraciones de Seguridad

- **Interacciones farmacológicas / farmacología**: la consulta se completó y devolvió 2 registros, ambos de naturaleza farmacológica (dianas) y no interacciones con otros fármacos con nivel de gravedad: PPARα (*PPARA*) y PPARβ/δ (*PPARD*). En los ensayos de fase 1/2 no se detectaron señales de seguridad específicas.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y con vínculo mecanístico especulativo. Además, faltan los datos de seguridad del prospecto, lo que impide avanzar al cribado de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), incluida la indicación aprobada
- Completar los datos del mecanismo de acción desde DrugBank
- Revisión de literatura y de registros de ensayos sobre PPAR y amenorrea/función ovárica (p. ej., síndrome de ovario poliquístico)
- Evaluar si el puntaje del modelo TxGNN (aprendizaje profundo) solo refleja similitudes aprendidas entre enfermedades relacionadas y no evidencia biológica
- Evaluar la seguridad en mujeres en edad fértil (embarazo y fertilidad) antes de cualquier estudio exploratorio
- Estudios preclínicos o de mecanismo que respalden el vínculo con el eje reproductivo

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Iqirvo (elafibranor) prescribing information, Ipsen Biopharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d78aa14f-6ec1-4b1d-a4ae-e48658137a25) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

