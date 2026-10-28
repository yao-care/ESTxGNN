---
layout: default
title: Captopril
parent: Solo predicción del modelo (L5)
nav_order: 142
evidence_level: L5
indication_count: 3
monitor_inn: "CAPTOPRIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism"]
last_modified_at: 2026-10-28
description: "Captopril: nueva indicación predicha, hipertensión renal maligna (malignant hypertensive renal disease) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Captopril
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Captopril: inhibidor de la enzima convertidora de angiotensina (ECA) → hipertensión renal maligna (malignant hypertensive renal disease)
{: .text-alpha }

## Resumen en Una Frase

Captopril es un inhibidor de la enzima convertidora de angiotensina (ECA) utilizado en el tratamiento de la hipertensión.
El modelo TxGNN predice que podría ser efectivo para **hipertensión renal maligna (malignant hypertensive renal disease)**,
pero actualmente **no hay ensayos clínicos** y solo existe **1 publicación** (un reporte de caso diagnóstico) sin evidencia terapéutica directa.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | hipertensión renal maligna (malignant hypertensive renal disease) |
| Puntaje de Predicción TxGNN | 0,9928 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 6) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Por conocimiento general de la clase, captopril inhibe la ECA, reduce la formación de angiotensina II y, con ello, la vasoconstricción y la presión intraglomerular.

En la hipertensión maligna con afectación renal el sistema renina-angiotensina suele estar muy activado, por lo que mecanísticamente el bloqueo de este eje es biológicamente plausible. La indicación predicha se solapa conceptualmente con los usos cardiovasculares y renales habituales de la clase.

Conviene ser prudente: la única publicación recuperada describe una renografía con captopril en un paciente cuya hipertensión dependiente de renina se debía a un carcinoma renal de células cromófobas. Es un reporte diagnóstico, no terapéutico. Ninguna publicación estudia directamente el tratamiento de esta enfermedad con captopril, por lo que el puntaje alto refleja la proximidad con usos conocidos y no evidencia nueva.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28902735](https://pubmed.ncbi.nlm.nih.gov/28902735/) | 2017 | Reporte de caso | Clinical Nuclear Medicine | Renografía con captopril positiva sin estenosis de la arteria renal; la causa fue un carcinoma renal de células cromófobas y la hipertensión remitió tras la nefrectomía |

## Información de Mercado en España

Se registran 20 autorizaciones de medicamentos con captopril como único principio activo (la lista puede ser parcial); 6 figuran como vigentes y 14 como canceladas. Principales autorizaciones:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 61620 | CAPTOPRIL MYLAN 50 mg COMPRIMIDOS EFG | Comprimido | No registrada en los datos locales |
| 64762 | CAPTOPRIL MABO 50 mg COMPRIMIDOS EFG | Comprimido | No registrada en los datos locales |
| 55939 | CAPTOPRIL QUALIGEN 50 mg COMPRIMIDOS | Comprimido | No registrada en los datos locales |
| 64764 | CAPTOPRIL TARBIS 25 mg COMPRIMIDOS EFG | Comprimido | No registrada en los datos locales |
| 62424 | CAPTOPRIL SANDOZ 25 mg COMPRIMIDOS EFG | Comprimido | No registrada en los datos locales |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (nivel moderado, entre otras): hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida, metformina, alogliptina, canagliflozina, dapagliflozina, empagliflozina, ertugliflozina, exenatida, bupropión, morfina, ácido acetilsalicílico, dronabinol, clorpropamida y acetohexamida. Con nivel menor: hidróxido de aluminio y carbonato de calcio. Se identificaron 100 interacciones en total; aquí se muestran las primeras 20.
- **Condiciones de precaución** (relaciones de contraindicación recogidas en bases de datos, no texto de prospecto): angioedema (incluido el hereditario y el inducido por bloqueadores del sistema renina-angiotensina-aldosterona), enfermedad renal, enfermedad hepática y encefalopatía hepática, pancreatitis, enfermedad de la vesícula biliar, lupus eritematoso sistémico, diabetes y cetoacidosis diabética, deficiencia de potasio, neutropenia y agranulocitosis, estenosis aórtica, hipotensión, hiperparatiroidismo y enfermedades del tejido conectivo y óseas.

No se dispone de advertencias ni contraindicaciones del prospecto; consultar el prospecto para la información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos y la única publicación es un reporte de caso diagnóstico que no estudia el tratamiento de la hipertensión renal maligna con captopril. El puntaje del modelo (0,9928) no sustituye la evidencia clínica.

**Para avanzar se necesita:**
- Estudios clínicos u observacionales que evalúen captopril directamente en hipertensión renal maligna
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones) de la AEMPS
- Revisión de seguridad renal específica (función renal, potasio, riesgo de hipotensión) en esta población
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

