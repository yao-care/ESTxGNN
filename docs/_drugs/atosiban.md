---
layout: default
title: Atosiban
parent: Solo predicción del modelo (L5)
nav_order: 77
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Atosiban: nueva indicación predicha, Glaucoma hereditario primario (nivel de evidencia L5). Indicación original: No disponible en los textos de autorización de la AEMPS (según otras…"
monitor_inn: "atosiban"
predicted_indications: ["primary hereditary glaucoma", "open-angle glaucoma", "congenital hypotrichosis milia", "alopecia", "hypotrichosis simplex of the scalp", "vascular disease", "diffuse alopecia areata", "arterial thoracic outlet syndrome", "venous thoracic outlet syndrome", "visceral calciphylaxis"]
---

# Atosiban
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

## Atosiban: De Indicación Original No Registrada a Glaucoma Hereditario Primario
{: .text-alpha }

## Resumen en Una Frase

Atosiban es un antagonista peptídico de los receptores de oxitocina y vasopresina, utilizado en Europa como tocolítico para retrasar el parto prematuro en mujeres adultas embarazadas de 24 a 33 semanas.
El modelo TxGNN predice que podría ser efectivo para **glaucoma hereditario primario**, con una puntuación muy alta (0,9992), pero **sin ensayos clínicos ni publicaciones** que respalden esta dirección; se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los textos de autorización de la AEMPS (según otras fuentes de datos, tocolítico en parto prematuro) |
| Nueva Indicación Predicha | Glaucoma hereditario primario |
| Puntaje de Predicción TxGNN | 0,9992 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 9 de 15) |
| Número de Autorizaciones | 15 (vigentes: 9) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco. Según la información farmacológica compilada, atosiban actúa como antagonista de los receptores de oxitocina (OXTR) y de los receptores de vasopresina V1A, V1B y V2. Su uso establecido es la inhibición de las contracciones uterinas en el parto prematuro.

La relación entre la indicación original (obstétrica) y el glaucoma hereditario primario es muy débil. Los datos no muestran ningún vínculo establecido con la fisiopatología del glaucoma hereditario (defectos de la malla trabecular o del drenaje del humor acuoso). La puntuación elevada de TxGNN refleja similitud en la red de conocimiento, no biología demostrada.

Cabe señalar que otras indicaciones predichas (por ejemplo, glaucoma de ángulo abierto, alopecia o enfermedad vascular) tampoco cuentan con evidencia clínica. Solo "enfermedad vascular" presenta literatura preclínica indirecta (nivel L4), centrada en oxitocina y no en atosiban como tratamiento.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para glaucoma hereditario primario.

---

## Información de Mercado en España

Se registran 15 autorizaciones vigentes, todas de fármaco único. Los textos de indicación aprobada no figuran en los datos compilados. Principales autorizaciones:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 79315 | Atosiban Altan 6,75 mg/0,9 ml solución inyectable EFG | Solución inyectable | No disponible |
| 81920 | Atosiban Ever Pharma 75 mg/10 ml concentrado para solución para perfusión | Solución inyectable | No disponible |
| 84868 | Atosiban Hybio 37,5 mg/5 ml concentrado para solución para perfusión EFG | Concentrado para solución para perfusión | No disponible |
| 99124001 | Tractocile 7,5 mg/ml, solución inyectable | Solución inyectable | No disponible |
| 99124002 | Tractocile 7,5 mg/ml, concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible |

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas / farmacología de dianas**: la consulta se completó con 4 registros, todos de interacción con dianas farmacológicas (no con otros fármacos): receptores V1A (AVPR1A), V1B (AVPR1B), V2 (AVPR2) y de oxitocina (OXTR). No se dispone de niveles de gravedad.
- **Señal de seguridad indirecta**: un estudio de cohorte neonatal (PMID 30646165, JAMA Network Open, 2018) examinó la asociación entre la exposición a tocolíticos y la hemorragia intraventricular en prematuros. Es una señal a vigilar, no evidencia terapéutica.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para glaucoma hereditario primario se basa solo en la puntuación del modelo (nivel L5), sin ensayos clínicos, literatura ni vínculo mecanístico plausible con el glaucoma.

**Para avanzar se necesita:**
- Revisión del prospecto de la AEMPS (indicaciones, advertencias y contraindicaciones), actualmente sin datos
- Datos detallados del mecanismo de acción (por ejemplo, desde DrugBank)
- Estudios preclínicos que evalúen la modulación de receptores de oxitocina/vasopresina en la presión intraocular o el drenaje del humor acuoso
- Análisis de compatibilidad de vía de administración (atosiban solo está disponible en formas parenterales; una indicación oftalmológica requeriría evaluar formulaciones alternativas)
- Considerar si otras indicaciones predichas, como enfermedad vascular (L4), merecen priorizarse como pregunta de investigación
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

