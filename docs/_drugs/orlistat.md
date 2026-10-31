---
layout: default
title: Orlistat
parent: Solo predicción del modelo (L5)
nav_order: 592
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-31
monitor_inn: "ORLISTAT"
predicted_indications: ["hypervitaminosis"]
description: "Orlistat: nueva indicación predicha, Hipervitaminosis (hypervitaminosis) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Orlistat
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

## Orlistat: Hipervitaminosis (hypervitaminosis)
{: .text-alpha }

## Resumen en Una Frase

Orlistat es un inhibidor de las lipasas gástrica y pancreática, utilizado originalmente para el tratamiento de la obesidad (incluida la obesidad monogénica).
El modelo TxGNN predice que podría ser efectivo para **hipervitaminosis**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Hipervitaminosis (hypervitaminosis) |
| Puntaje de Predicción TxGNN | 0.9942 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 15) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Orlistat inhibe las lipasas gástrica y pancreática y reduce la absorción de grasa de la dieta en aproximadamente un 30%. Los datos compilados para este informe no incluyen el campo formal de mecanismo de acción, por lo que esta descripción procede del análisis de reposicionamiento y no ha podido contrastarse con el registro original.

Las vitaminas liposolubles (A, D, E, K) se absorben junto con la grasa de la dieta, por lo que orlistat disminuye su absorción. Es un efecto adverso conocido y la razón por la que se recomienda suplementación vitamínica durante el tratamiento. De forma puramente teórica, este efecto podría reducir la carga vitamínica en una hipervitaminosis liposoluble (por ejemplo, exceso de vitamina A o D).

Sin embargo, la relación es débil. El puntaje alto de TxGNN (0.9942) es solo una predicción del modelo, sin respaldo de ensayos ni literatura. El efecto sobre los niveles de vitaminas es un efecto secundario nutricional, no una terapia establecida para la toxicidad vitamínica. El manejo estándar (suspender la fuente de la vitamina, cuidados de soporte y, en algunos casos, otros fármacos) ya existe, y usar orlistat con este fin conllevaría riesgo de déficit de otras vitaminas liposolubles.

## Información de Mercado en España

Se identificaron 20 autorizaciones vigentes, todas de monofármaco y ninguna cancelada. Las principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 07401009 | ALLI 60 mg cápsulas duras | Cápsula dura | No disponible |
| 78962 | Orlistat Sandoz 120 mg cápsulas duras | Cápsula dura | No disponible |
| 98071003IP9 | Xenical 120 mg cápsulas duras | Cápsula dura | No disponible |
| 81233 | Orlistat Teva 120 mg cápsulas duras | Cápsula dura | No disponible |
| 07401012 | ALLI 27 mg comprimidos masticables | Comprimido masticable | No disponible |

Entre las demás autorizaciones figuran Beacita, Orlidunn, Normostat, Linestat, Orliloss, Orlistat Stada, Orlistat Aurovitas y Orlistat Aristo.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): insuficiencia hepática, hiperoxaluria primaria, anorexia nerviosa, bulimia nerviosa, trastornos por déficit vitamínico, colestasis (incluidas la colestasis intrahepática recurrente benigna y la familiar) y lesión hepática inducida por fármacos.
- **Interacciones farmacológicas**: se registraron 100 interacciones. Las principales de nivel moderado incluyen abacavir, lamivudina, acarbosa, albiglutida, alogliptina, metformina, amiodarona, asparaginasa, atazanavir, emtricitabina, brentuximab vedotina, canagliflozina, cannabidiol, clorpropamida y clofarabina. Las de nivel leve incluyen colecalciferol, calcifediol y calcitriol.
- **Nota relevante para esta predicción**: la contraindicación en trastornos por déficit vitamínico y la interacción con vitaminas liposolubles refuerzan el riesgo de usar orlistat en un contexto de manejo de niveles vitamínicos.

Las advertencias y contraindicaciones del prospecto de la AEMPS no están disponibles; consultar el prospecto para la información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura. El mecanismo propuesto es un efecto secundario nutricional, no una terapia establecida, y existe riesgo de déficit de otras vitaminas liposolubles.

**Para avanzar se necesita:**
- Revisión de literatura que evalúe si orlistat modifica los niveles de vitaminas en hipervitaminosis (estudios preclínicos o series de casos)
- Datos del mecanismo de acción desde DrugBank para contrastar el vínculo mecanístico
- Advertencias y contraindicaciones del prospecto de la AEMPS (pendiente de descarga y análisis)
- Evaluación de la viabilidad frente al manejo estándar y del riesgo de déficit vitamínico
- Análisis de compatibilidad de vía y formulación para la nueva indicación
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

