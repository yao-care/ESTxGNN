---
layout: default
title: Atenolol
parent: Solo predicción del modelo (L5)
nav_order: 73
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Atenolol: nueva indicación predicha, Infarto de miocardio posterolateral (nivel de evidencia L5). Indicación original: Hipertensión arterial / infarto de miocardio (según el grafo de conoc…"
monitor_inn: "ATENOLOL"
predicted_indications: ["posterolateral myocardial infarction", "posteroinferior myocardial infarction", "malignant renovascular hypertension", "malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "septal myocardial infarction", "Braddock syndrome", "chronic pulmonary heart disease"]
---

# Atenolol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

# Atenolol: De Hipertensión Arterial a Infarto de Miocardio Posterolateral

## Resumen en Una Frase

Atenolol es un betabloqueante cardioselectivo (beta-1), utilizado originalmente para el tratamiento de la hipertensión arterial y el infarto de miocardio.
El modelo TxGNN predice que podría ser efectivo para **infarto de miocardio posterolateral**, aunque se trata de un subtipo anatómico de una indicación ya aprobada, por lo que no constituye un reposicionamiento en sentido estricto.
Para esta predicción concreta hay **0 ensayos clínicos** y **0 publicaciones** específicas; la evidencia es únicamente la predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial / infarto de miocardio (según el grafo de conocimiento; el texto de indicación de las autorizaciones españolas no está disponible) |
| Nueva Indicación Predicha | Infarto de miocardio posterolateral |
| Puntaje de Predicción TxGNN | 99.87% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, atenolol es un betabloqueante selectivo del receptor beta-1 adrenérgico. Su eficacia en hipertensión e infarto de miocardio está establecida, y mecanísticamente la reducción de la frecuencia cardíaca y de la demanda miocárdica de oxígeno resulta plausible en cualquier subtipo de infarto.

El infarto posterolateral es una variante anatómica del infarto de miocardio, una indicación original del fármaco. El alto puntaje del modelo refleja sobre todo la proximidad en la ontología de enfermedades con la indicación ya aprobada, y no una señal nueva de reposicionamiento.

Otras predicciones del mismo análisis (p. ej., hipertensión renovascular maligna, infarto posteroinferior y septal) siguen la misma lógica de subtipos de indicaciones existentes. Las predicciones de hipertensión pulmonar y síndrome de Braddock carecen de respaldo mecanístico claro.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

A modo de contexto, para el subtipo vecino (infarto posteroinferior) existe un estudio cruzado, simple ciego y aleatorizado de 1985 ([PMID 3901170](https://pubmed.ncbi.nlm.nih.gov/3901170/)) que comparó la actividad antiisquémica de atenolol y diltiazem en 23 pacientes tras un infarto; su relevancia para el subtipo posterolateral es limitada.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 58255 | ATENOLOL RATIOPHARM 100 mg comprimidos recubiertos EFG | Comprimido | No disponible |
| 56967 | TENORMIN 50 mg comprimidos | Comprimido | No disponible |
| 56777 | TENORMIN 0,5 mg/ml solución inyectable | Solución inyectable | No disponible |
| 62926 | ATENOLOL ARISTO 50 mg EFG | Comprimido | No disponible |
| 56695 | BLOKIUM 50 mg comprimidos | Comprimido | No disponible |

Se muestran 5 de las 20 autorizaciones vigentes (todas de principio activo único, ninguna cancelada).

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no proceden del texto del prospecto): bloqueo auriculoventricular, asma (incluidas las formas alérgica e intrínseca), diabetes mellitus (tipos 1 y 2) y cetoacidosis diabética, enfermedad de Raynaud, anafilaxia, insuficiencia hepática, anuria, pancreatitis, lupus eritematoso sistémico, psoriasis, gota e hiperuricemia, hipercalcemia, trastornos del metabolismo del fósforo y déficit de potasio, y trastornos de ansiedad y distimia.
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Entre las listadas, de gravedad moderada: epinefrina, hidrocortisona, hiosciamina, bupropión, triamcinolona, morfina, acetohexamida, atropina, betametasona, budesonida y sales de calcio (acetato, carbonato, citrato, gluconato, lactato, fosfato, entre otras). De gravedad menor: ácido acetilsalicílico, hidróxido de aluminio y attapulgita.
- Atenolol se elimina por vía renal, por lo que en insuficiencia renal sería necesario ajustar la dosis.

Para las advertencias del prospecto, consultar la ficha técnica de la AEMPS.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción corresponde a un subtipo anatómico de una indicación ya aprobada (infarto de miocardio), sin ensayos ni literatura específicos (nivel L5). No aporta una oportunidad nueva de reposicionamiento; el uso clínico ya está cubierto por la indicación existente.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), actualmente no disponible.
- Datos del mecanismo de acción desde DrugBank.
- Confirmar si el uso en subtipos de infarto ya está cubierto por la indicación autorizada, para decidir si la evaluación tiene sentido.
- Si se busca un reposicionamiento genuino, priorizar otras predicciones con señal distinta a la de las indicaciones existentes y revisión experta de las de bajo respaldo (p. ej., síndrome de Braddock).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

