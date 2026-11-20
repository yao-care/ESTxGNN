---
layout: default
title: Bendroflumethiazide
parent: Solo predicción del modelo (L5)
nav_order: 94
evidence_level: L5
indication_count: 4
monitor_inn: "bendroflumethiazide"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
last_modified_at: 2026-11-20
description: "Bendroflumethiazide: nueva indicación predicha, enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) (nivel de evidencia L5). Indicación original: No consta en los datos local…"
---

# Bendroflumethiazide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Bendroflumetiazida: diurético tiazídico → enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)
{: .text-alpha }

## Resumen en Una Frase

Bendroflumetiazida es un diurético de tipo tiazídico que se utiliza para tratar la hipertensión.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) |
| Puntaje de Predicción TxGNN | 0,9988 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado (registros anulados: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 0) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según ChEMBL (EMBL-EBI), el mecanismo de acción registrado para Bendroflumethiazide es (traducción no oficial): «Inhibidor del cotransportador de sodio-cloruro sensible a tiazidas». Texto original en inglés: "Thiazide-sensitive sodium-chloride cotransporter inhibitor" ([ChEMBL CHEMBL1684 (bendroflumethiazide): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1684), CC BY-SA 3.0; consultado el 2026-11-19). Según la información conocida, la bendroflumetiazida es un diurético tiazídico, clase que reduce la presión arterial al disminuir el volumen circulante y favorecer la eliminación de sodio y agua por el riñón.

Un vínculo con la enfermedad renal hipertensiva es plausible por la reducción de la presión arterial. Sin embargo, la hipertensión maligna con afectación renal es una emergencia hipertensiva que se trata con fármacos de acción rápida por vía parenteral. Las tiazidas no son un tratamiento estándar y su eficacia disminuye cuando la filtración glomerular está reducida.

El puntaje elevado (0,9988) probablemente refleja la cercanía con la indicación hipertensiva original, más que una evidencia clínica propia. No se aportaron ensayos ni literatura que lo sustenten.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 56535 | NEATENOL DIU 100mg/5mg COMPRIMIDOS | Comprimido | No registrada en los datos locales |

Este producto es una asociación a dosis fija (100 mg/5 mg), por lo que su autorización no describe la situación de la bendroflumetiazida como principio activo único.

## Consideraciones de Seguridad

- **Contraindicaciones y enfermedades con riesgo asociado** (no proceden del texto del prospecto; son relaciones de contraindicación recopiladas en los datos del informe): trastornos de ansiedad, enfermedad renal, anuria, pancreatitis, enfermedad hepática y encefalopatía hepática, enfermedad de la vesícula biliar, lupus eritematoso sistémico, deficiencia de potasio, diabetes mellitus y cetoacidosis diabética, hiperuricemia y gota, hiperparatiroidismo, hipercalcemia y nefrocalcinosis, miastenia gravis, bloqueo auriculoventricular, enfisema pulmonar y enfermedad bronquial.
- **Interacciones farmacológicas**: se identificaron 168 interacciones. Entre las principales (nivel moderado) figuran acarbosa, metformina, pioglitazona, alogliptina, albiglutida, hidrocortisona, dexametasona, betametasona, triamcinolona, beclometasona, anfotericina B, omeprazol, rabeprazol, bupropión, morfina y colecalciferol. De nivel menor: doxiciclina, hioscimina y atropina.

Se debe consultar el prospecto para conocer las advertencias oficiales.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ensayos clínicos ni literatura, y la plausibilidad mecanística es limitada: las tiazidas no son tratamiento de referencia en una emergencia hipertensiva con afectación renal. El perfil de seguridad en enfermedad renal también es desfavorable.

**Para avanzar se necesita:**
- Búsqueda de estudios clínicos o literatura que evalúen directamente la bendroflumetiazida en esta enfermedad
- Datos del mecanismo de acción
- Advertencias y contraindicaciones del prospecto de la AEMPS
- Evaluación de seguridad en pacientes con deterioro de la función renal

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente (revisado el 2026-11-20; la versión anterior se guarda en el registro) | [ChEMBL CHEMBL1684 (bendroflumethiazide): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1684) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

