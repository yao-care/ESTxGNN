---
layout: default
title: Fosinopril
parent: Evidencia moderada (L3-L4)
nav_order: 360
evidence_level: L4
indication_count: 5
last_modified_at: 2026-10-14
description: "Fosinopril: nueva indicación predicha, Enfermedad renal hipertensiva maligna (nivel de evidencia L4). Indicación original: Hipertensión arterial (trastorno hipertensivo)"
monitor_inn: "FOSINOPRIL"
predicted_indications: ["malignant hypertensive renal disease", "malignant renovascular hypertension", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
---

# Fosinopril
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **5** 
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

# Fosinopril: De Hipertensión a Enfermedad Renal Hipertensiva Maligna

## Resumen en Una Frase

Fosinopril es un inhibidor de la enzima convertidora de angiotensina (IECA), originalmente utilizado para el tratamiento de la hipertensión arterial.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden específicamente esta dirección: es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial (trastorno hipertensivo) |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna |
| Puntaje de Predicción TxGNN | 99,87% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, fosinopril es un profármaco que se convierte en fosinoprilato, un inhibidor de la ACE que reduce la angiotensina II y, con ello, la presión arterial. Su eficacia en la hipertensión está establecida.

La nefropatía hipertensiva maligna está impulsada por una hipertensión muy grave y por la activación del sistema renina-angiotensina-aldosterona (SRAA), por lo que el mecanismo es plausible. Sin embargo, se trata en esencia de una extensión de la indicación ya aprobada de hipertensión. El puntaje tan alto (99,87%) probablemente refleja la cercanía con la indicación original y no constituye evidencia clínica.

Otras predicciones del modelo tienen un respaldo aún más débil: la hipertensión renovascular maligna (puntaje 99,87%, L4) es coherente con el SRAA, pero los IECA conllevan riesgo en la estenosis bilateral de la arteria renal. Las predicciones de hipertensión pulmonar (99,87%) y el síndrome de Braddock (99,81%) carecen de un vínculo mecanístico claro y quedan en L5, con recomendación Hold.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Para la indicación principal (enfermedad renal hipertensiva maligna) actualmente no hay literatura relacionada disponible.

Para referencia, en la predicción de hipertensión pulmonar por enfermedad pulmonar o hipoxia se recuperaron dos publicaciones, ninguna de las cuales respalda la eficacia:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9923037](https://pubmed.ncbi.nlm.nih.gov/9923037/) | 1998 | Reporte de caso | Revue des maladies respiratoires | Neumonía eosinofílica hipóxica en dos pacientes tratados con IECA (enalapril y fosinopril); posible señal de seguridad, no de eficacia |
| [31105790](https://pubmed.ncbi.nlm.nih.gov/31105790/) | 2019 | Preclínico/Bioinformática | Experimental and Therapeutic Medicine | Genes diana en células mesangiales de ratón en nefropatía diabética; sin relación directa con el tema |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 59716 | FOSITENS 20 mg COMPRIMIDOS | Comprimido | No disponible en los datos |
| 83239 | FOSINOPRIL AUROVITAS 20 MG COMPRIMIDOS EFG | Comprimido | No disponible en los datos |
| 74975 | FOSINOPRIL AUROBINDO 20 mg COMPRIMIDOS EFG | Comprimido | No disponible en los datos |
| 66779 | FOSINOPRIL TEVA 20 mg COMPRIMIDOS EFG | Comprimido | No disponible en los datos |

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo asociadas (según el grafo de conocimiento, no el prospecto)**: enfermedad renal, hepatopatía, pancreatitis, enfermedad de la vesícula biliar, angioedema (incluido el hereditario, el adquirido y el inducido por bloqueadores del SRAA), lupus eritematoso sistémico, deficiencia de potasio, diabetes mellitus y cetoacidosis diabética, neutropenia y agranulocitosis, estenosis aórtica y otras valvulopatías aórticas, trastornos hipotensivos, hiperparatiroidismo, encefalopatía/coma hepático, enfermedades del tejido conectivo y enfermedades óseas.
- **Interacciones farmacológicas**: se identificaron 100 interacciones en total; las más relevantes son las de nivel **Mayor** con **bicarbonato de potasio** y **citrato de potasio** (riesgo de hiperpotasemia). Entre las de nivel moderado figuran corticosteroides (hidrocortisona, betametasona, budesonida, dexametasona, triamcinolona), antidiabéticos (alogliptina, canagliflozina, dapagliflozina, empagliflozina, saxagliptina, metformina, clorpropamida), ácido acetilsalicílico, bupropión, morfina y dronabinol, entre otros.
- **Consideración específica**: en la hipertensión renovascular maligna, los IECA pueden provocar deterioro agudo de la función renal en caso de estenosis bilateral de la arteria renal.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal se apoya únicamente en el puntaje del modelo y en la cercanía con la indicación de hipertensión ya aprobada, sin ensayos clínicos ni literatura específica (nivel L4). Además, falta la información del prospecto, lo que impide completar el cribado de seguridad.

**Para avanzar se necesita:**
- Obtener las advertencias y contraindicaciones del prospecto de la AEMPS (carencia bloqueante).
- Obtener datos del mecanismo de acción desde DrugBank.
- Realizar una revisión sistemática de la literatura sobre IECA en nefroesclerosis hipertensiva maligna y en hipertensión renovascular.
- Evaluar el perfil de seguridad renal (estenosis de la arteria renal, hiperpotasemia) en la población objetivo.
- Aclarar la indicación aprobada en cada autorización española, ya que no figura en los datos disponibles.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

