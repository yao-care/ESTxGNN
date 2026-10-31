---
layout: default
title: Lisinopril
parent: Solo predicción del modelo (L5)
nav_order: 476
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-31
monitor_inn: "LISINOPRIL"
predicted_indications: ["pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "Braddock syndrome", "chronic pulmonary heart disease", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome"]
description: "Lisinopril: nueva indicación predicha, Pulmonary hypertension with unclear multifactorial mechanism (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Lisinopril
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Lisinopril: Pulmonary hypertension with unclear multifactorial mechanism
{: .text-alpha }

## Resumen en Una Frase

Lisinopril es un inhibidor de la enzima convertidora de angiotensina (IECA), utilizado originalmente para el tratamiento de la hipertensión arterial y el infarto de miocardio.
El modelo TxGNN predice que podría ser efectivo para **infarto de miocardio posterolateral**, con una puntuación muy alta, pero **sin ensayos clínicos ni publicaciones** específicas que respalden esta predicción.
Se trata de un subtipo anatómico de una indicación ya conocida, por lo que no constituye un reposicionamiento genuino.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Pulmonary hypertension with unclear multifactorial mechanism |
| Puntaje de Predicción TxGNN | 0.9989 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 13) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, lisinopril pertenece a la clase de los IECA: bloquea la conversión de angiotensina I en angiotensina II, lo que reduce la vasoconstricción y la carga hemodinámica sobre el corazón.

El infarto de miocardio ya figura entre las indicaciones originales de lisinopril. El infarto posterolateral es un subtipo anatómico del infarto de miocardio, por lo que el beneficio de la inhibición de la ECA (menor remodelado ventricular y menor mortalidad tras el infarto) se extiende de forma plausible a esta localización.

La puntuación alta del modelo refleja sobre todo la relación ontológica con la enfermedad de origen y no aporta evidencia nueva.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Se identificaron 20 autorizaciones vigentes, todas de monofármaco, en forma de comprimido. Se listan las 5 principales (el texto de indicación aprobada no figura en los datos compilados):

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 64562 | LISINOPRIL CINFA 20 mg COMPRIMIDOS EFG | Comprimido | No disponible |
| 65530 | LISINOPRIL VIATRIS 5 MG COMPRIMIDOS EFG | Comprimido | No disponible |
| 88814 | LISINOPRIL GRINDEKS 20 MG COMPRIMIDOS EFG | Comprimido | No disponible |
| 59129 | PRINIVIL 20 mg COMPRIMIDOS | Comprimido | No disponible |
| 59127 | ZESTRIL 20 mg COMPRIMIDOS | Comprimido | No disponible |

---

## Consideraciones de Seguridad

- **Contraindicaciones y enfermedades de riesgo (según el grafo de conocimiento, no el prospecto)**: angioedema (adquirido, hereditario o inducido por bloqueadores del sistema renina-angiotensina-aldosterona), enfermedad renal, enfermedad hepática y encefalopatía hepática, pancreatitis, enfermedad de la vesícula biliar, lupus eritematoso sistémico y otras enfermedades del tejido conectivo, diabetes y cetoacidosis diabética, deficiencia de potasio, neutropenia y agranulocitosis, estenosis aórtica, hipotensión, hiperparatiroidismo y enfermedad ósea.
- **Interacciones Farmacológicas**: se registraron 100 interacciones. Entre las principales destacan las de nivel **mayor** con **citrato de potasio** y **bicarbonato de potasio** (riesgo de hiperpotasemia). Las de nivel moderado incluyen corticoides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona), antidiabéticos (metformina, alogliptina, saxagliptina, canagliflozina, dapagliflozina, empagliflozina, clorpropamida), ácido acetilsalicílico, morfina, bupropión, dronabinol, ácido picosulfúrico y polietilenglicol con electrolitos.

Para las advertencias del prospecto, consultar la ficha técnica oficial.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es de alta puntuación, pero corresponde a un subtipo anatómico de una indicación ya aprobada (infarto de miocardio) y no cuenta con ensayos ni literatura específicos; por tanto, no aporta una oportunidad real de reposicionamiento.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto oficial de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), ya que su ausencia impide completar el cribado de seguridad.
- Obtener los datos del mecanismo de acción desde DrugBank.
- Confirmar si el infarto posterolateral ya está cubierto por la indicación de infarto de miocardio en la ficha técnica, lo que haría innecesaria una nueva indicación.
- Priorizar, si se busca reposicionamiento real, candidatas mejor respaldadas del mismo conjunto, como la **cardiopatía pulmonar crónica** (nivel L3; dos estudios clínicos antiguos y pequeños con lisinopril, PMID 17047621 y 14524095, de diseño no verificado), que requeriría confirmación con ensayos controlados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

