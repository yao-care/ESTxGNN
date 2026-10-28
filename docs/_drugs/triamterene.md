---
layout: default
title: Triamterene
parent: Solo predicción del modelo (L5)
nav_order: 824
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
monitor_inn: "triamterene"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease"]
description: "Triamterene: nueva indicación predicha, Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Triamterene
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Triamterene: Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)
{: .text-alpha }

## Resumen en Una Frase

Triamtereno es un diurético ahorrador de potasio, utilizado originalmente para el tratamiento de la hipertensión y la insuficiencia cardíaca congestiva.
El modelo TxGNN predice que podría ser efectivo para la **enfermedad renal hipertensiva maligna**,
pero actualmente no hay **ensayos clínicos** ni **publicaciones** que respalden esta dirección: se trata solo de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) |
| Puntaje de Predicción TxGNN | 0.9989 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 1 de 1) |
| Número de Autorizaciones | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado en la base de datos. Según la información conocida, el triamtereno es un diurético ahorrador de potasio que bloquea el canal epitelial de sodio (ENaC) en la nefrona distal, lo que reduce el volumen y la presión arterial. Su eficacia en la hipertensión ha sido comprobada, por lo que un efecto antihipertensivo es plausible.

Sin embargo, la enfermedad renal hipertensiva maligna es una emergencia hipertensiva con daño renal que requiere tratamiento parenteral rápido; un diurético oral de efecto moderado no es un tratamiento primario adecuado.

Otras predicciones del modelo tienen una base igualmente débil: hipertensión renovascular maligna (99.89%), hipertensión pulmonar de mecanismo multifactorial incierto (99.88%), hipertensión pulmonar por enfermedad pulmonar o hipoxia (99.88%), síndrome de Braddock (99.84%) y cor pulmonale crónico (99.75%, nivel L4, con apoyo solo indirecto del manejo de la insuficiencia cardíaca). Ninguna cuenta con ensayos clínicos que evalúen el triamtereno en esas indicaciones.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal predicha. Para otras predicciones se recuperaron artículos, pero no aportan evidencia relevante sobre el triamtereno en esas indicaciones (por ejemplo, un reporte de edema pulmonar asociado a hidroclorotiazida y un estudio de fisiología de colon en ratas).

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 53542 | SALIDUR 77,6 MG / 25 MG COMPRIMIDOS (Laboratorios Almirall S.L.) | Comprimido | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no el texto del prospecto)**: enfermedad o insuficiencia hepática, encefalopatía/coma hepático, enfermedad renal, anuria, hipercalcemia, nefrolitiasis, nefrocalcinosis, nefropatía aguda por uratos, gota, diabetes mellitus (tipo 1 y 2), cetoacidosis diabética, acidosis (incluida la acidosis láctica adquirida), lupus eritematoso sistémico, pancreatitis, enfermedad de la vesícula biliar, hiperparatiroidismo, anemia por deficiencia de ácido fólico, ictericia neonatal, entre otras.
- **Interacciones Farmacológicas**: se identificaron 104 interacciones en total. La más relevante entre las mostradas es de nivel **mayor** con **citrato de potasio** (riesgo de hiperpotasemia). Hay varias de nivel moderado (por ejemplo, metformina, corticoides como hidrocortisona, dexametasona, betametasona, triamcinolona y budesonida, bupropión, morfina, canagliflozina, dapagliflozina, dronabinol, bisacodilo, ácido picosulfúrico y polietilenglicol con electrolitos) y otras de nivel menor (famotidina, ranitidina, cimetidina, doxiciclina y minociclina).
- Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos ni literatura, y es clínicamente poco plausible: una emergencia hipertensiva con daño renal no se trata con un diurético oral ahorrador de potasio. Además, el perfil de contraindicaciones renales y el riesgo de hiperpotasemia agravan la preocupación.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones oficiales), imprescindible para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión de la literatura específica sobre triamtereno en hipertensión maligna y nefropatía hipertensiva.
- Evaluar el riesgo de hiperpotasemia y deterioro renal en este contexto antes de cualquier estudio.
- Considerar priorizar otras predicciones con apoyo indirecto más sólido, como el cor pulmonale crónico (manejo sintomático de la congestión).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

