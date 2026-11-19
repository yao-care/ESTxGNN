---
layout: default
title: Bisoprolol
parent: Solo predicción del modelo (L5)
nav_order: 108
evidence_level: L5
indication_count: 4
monitor_inn: "BISOPROLOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
last_modified_at: 2026-11-05
description: "Bisoprolol: nueva indicación predicha, Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: al menos 20"
---

# Bisoprolol
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

## Bisoprolol: betabloqueante selectivo beta-1 → enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)
{: .text-alpha }

## Resumen en Una Frase

Bisoprolol es un betabloqueante selectivo del receptor beta-1 adrenérgico, utilizado como antihipertensivo.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) |
| Puntaje de Predicción TxGNN | 0,9994 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 12; autorizadas no comercializadas: 3; revocadas o suspendidas: 5) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Bisoprolol (traducción no oficial): «El FUMARATO DE BISOPROLOL es un bloqueante de los adrenorreceptores beta 1 -selectivo (cardioselectivo) sin actividad estabilizadora de membrana ni actividad simpaticomimética intrínseca significativas en su intervalo de dosis terapéuticas. Sin embargo, la cardioselectividad no es absoluta y, a dosis más altas (≥ 20 mg), el fumarato de bisoprolol también inhibe los adrenorreceptores beta 2 , localizados principalmente en la musculatura bronquial y vascular; por lo tanto, para conservar la selectividad es importante utilizar la dosis eficaz más baja.» Texto original en inglés: "BISOPROLOL FUMARATE is a beta 1 -selective (cardioselective) adrenoceptor blocking agent without significant membrane stabilizing activity or intrinsic sympathomimetic activity in its therapeutic dosage range. Cardioselectivity is not absolute, however, and at higher doses (≥ 20 mg) bisoprolol fumarate also inhibits beta 2 -adrenoceptors, chiefly located in the bronchial and vascular musculature; to retain selectivity it is therefore important to use the lowest effective dose." ([DailyMed: bisoprolol fumarate prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6517d564-ea55-4084-a8ab-34fea548c24e), versión del 2026-11-11; consultado el 2026-11-19). Por su clase, bisoprolol bloquea de forma selectiva los receptores beta-1 adrenérgicos, lo que reduce la frecuencia cardíaca, el gasto cardíaco y la presión arterial.

La enfermedad renal hipertensiva maligna es una complicación grave de órgano diana de la hipertensión severa, por lo que reducir la presión arterial es mecanísticamente plausible. Además, el bloqueo beta-1 disminuye la liberación de renina, algo potencialmente relevante en el daño renal mediado por el sistema renina-angiotensina.

Hay que ser cautos: el puntaje elevado parece reflejar la relación conocida del fármaco con la hipertensión y no una evidencia independiente. La hipertensión maligna se maneja habitualmente en contexto agudo con fármacos intravenosos, y no existen ensayos ni literatura sobre esta indicación específica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Los datos compilados indican que bisoprolol está comercializado en España, con autorizaciones válidas (la lista de registros puede ser parcial). Principales presentaciones:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 57543 | EURADAL 10 mg comprimidos recubiertos con película | Comprimido recubierto |
| 63048 | EMCONCOR COR 5 mg comprimidos recubiertos con película | Comprimido recubierto con película |
| 57654 | EMCONCOR 5 mg comprimidos recubiertos con película | Comprimido recubierto con película |
| 73633 | Bisoprolol Cor Viatris 5 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 85878 | Bisoprolol Zentiva 7,5 mg comprimidos EFG | Comprimido |

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: se identificaron interacciones de nivel moderado, entre otras, con epinefrina, hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona, bupropión, morfina, atropina, hiosciamina, metescopolamina, acetohexamida y sales de calcio (acetato, carbonato, citrato, gluconato). También hay interacciones leves con ácido acetilsalicílico, hidróxido de aluminio y attapulgita.
- **Enfermedades de precaución registradas en los datos compilados** (no proceden del texto del prospecto): asma, diabetes mellitus y cetoacidosis diabética, enfermedad renal, enfermedad hepática y encefalopatía hepática, miastenia gravis, psoriasis, lupus eritematoso sistémico, gota, pancreatitis, entre otras.

Consultar el prospecto para el resto de la información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ensayos clínicos ni literatura propios y el puntaje alto parece derivar de la relación ya conocida del fármaco con la hipertensión. Además, el manejo habitual de la hipertensión maligna es agudo e intravenoso.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción
- Revisión de la evidencia clínica específica sobre bisoprolol en nefropatía hipertensiva maligna
- Información de seguridad del prospecto de la AEMPS (advertencias y contraindicaciones)
- Evaluación de la viabilidad clínica frente a los tratamientos intravenosos estándar

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: bisoprolol fumarate prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6517d564-ea55-4084-a8ab-34fea548c24e) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

