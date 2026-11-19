---
layout: default
title: Isotretinoin
parent: Solo predicción del modelo (L5)
nav_order: 435
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
monitor_inn: "Isotretinoin"
predicted_indications: ["malignant hypertensive renal disease"]
description: "Isotretinoin: nueva indicación predicha, Malignant hypertensive renal disease (nivel de evidencia L5). En España, autorizaciones de la AEMPS: al menos 20"
---

# Isotretinoin
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

## Isotretinoin: Malignant hypertensive renal disease
{: .text-alpha }

## Resumen en Una Frase

Según el grafo de conocimiento utilizado por el modelo, la isotretinoína figura con indicaciones originales de hipertensión y trastorno hipertensivo; sin embargo, en la práctica clínica es un retinoide empleado en dermatología (acné), por lo que esa indicación original debe tomarse con cautela.
El modelo TxGNN predice que podría ser efectiva para la **hipertensión renovascular maligna**, con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.
La única base es el puntaje del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Malignant hypertensive renal disease |
| Puntaje de Predicción TxGNN | 0.9901 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 16; autorizadas no comercializadas: 3; revocadas o suspendidas: 1) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Isotretinoin (traducción no oficial): «Se desconoce el mecanismo de acción exacto de Zenatane en el tratamiento del acné nodular grave y resistente en pacientes no embarazadas de 12 años de edad o más con múltiples nódulos inflamatorios de un diámetro de 5 mm o más que no responden al tratamiento convencional, incluidos los antibióticos sistémicos. La isotretinoína, un retinoide, inhibe la función de las glándulas sebáceas y la queratinización.» Texto original en inglés: "The exact mechanism of action of Zenatane in the treatment of severe recalcitrant nodular acne in nonpregnant patients 12 years of age and older with multiple inflammatory nodules with a diameter of 5 mm or greater who are unresponsive to conventional therapy, including systemic antibiotics is unknown. Isotretinoin, a retinoid, inhibits sebaceous gland function and keratinization." ([DailyMed: Zenatane (isotretinoin) prescribing information, Dr. Reddy's Laboratories Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=27b3cf26-f22e-5b70-1c24-009933b7c6ee), versión del 2026-09-20; consultado el 2026-11-19). La isotretinoína es un retinoide cuya farmacología conocida (supresión de las glándulas sebáceas, efectos sobre la diferenciación y proliferación celular) no guarda relación con el control de la presión arterial.

Las indicaciones originales de hipertensión que figuran en los datos son incoherentes con el uso clínico conocido de la isotretinoína y podrían ser un artefacto del modelo TxGNN (aprendizaje profundo). Por ello, la relación entre la indicación original y la nueva indicación no puede considerarse mecanísticamente sólida.

La señalización de retinoides se ha explorado en modelos preclínicos de lesión y fibrosis renal, pero esto es especulativo y no está respaldado por evidencia en los datos compilados. La predicción debe tratarse con cautela.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

<!-- review:begin es-lic-20261105-isotretinoin-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Se muestran 5 de las 20 autorizaciones vigentes (todas son monofármaco, en cápsula blanda)." Eliminado: el número o el estado de comercialización de las autorizaciones no coincidía con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-isotretinoin-1 -->

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 67570 | ISOACNE 10 mg cápsulas blandas | Cápsula blanda | No disponible en los datos |
| 67878 | DERCUTANE 40 mg cápsulas blandas | Cápsula blanda | No disponible en los datos |
| 86649 | ISOTIORGA 40 mg cápsulas blandas | Cápsula blanda | No disponible en los datos |
| 78326 | DERCUTANE 30 mg cápsulas blandas | Cápsula blanda | No disponible en los datos |
| 82566 | ACNEMIN 10 mg cápsulas blandas EFG | Cápsula blanda | No disponible en los datos |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): trastornos de ansiedad, trastornos neuróticos y distímicos, trastornos psicóticos y mentales, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, pancreatitis, angioedema (incluido el hereditario), enfermedad inflamatoria intestinal, osteoporosis, lupus eritematoso sistémico, diabetes mellitus y cetoacidosis diabética, neutropenia y agranulocitosis, deficiencia de potasio y trastorno hipotensivo. Es relevante que figuren enfermedad renal y trastorno hipotensivo en relación con las indicaciones predichas.
- **Interacciones farmacológicas**: se registran 98 interacciones. Entre las de nivel **mayor** se encuentran doxiciclina, minociclina, tetraciclina y vitamina A. Entre las de nivel moderado se incluyen corticoides (betametasona, budesonida, dexametasona, hidrocortisona, prednisolona, prednisona, triamcinolona), warfarina, dicumarol, etanol, naltrexona, nitisinona, fostamatinib, ivacaftor, lumacaftor y abametapir tópico.
- **Otras consideraciones**: de forma general, la isotretinoína se asocia a teratogenicidad, elevación de lípidos y efectos hepáticos, que habría que ponderar cuidadosamente en pacientes con hipertensión grave o insuficiencia renal que reciben varios antihipertensivos.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única base es un puntaje alto del modelo (0,9901), sin ensayos clínicos ni literatura, sin mecanismo de acción disponible y con una indicación original incoherente con el uso clínico conocido. Además, el perfil de seguridad de la isotretinoína plantea dudas importantes en pacientes con hipertensión maligna y afectación renal.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), un vacío de datos bloqueante para el cribado de seguridad.
- Obtener los datos del mecanismo de acción (por ejemplo, desde DrugBank) para analizar un posible vínculo mecanístico.
- Realizar una búsqueda sistemática de literatura y ensayos, incluidos estudios preclínicos de retinoides en daño renal e hipertensión.
- Evaluar la relación beneficio-riesgo en población con hipertensión maligna y enfermedad renal, considerando las interacciones y contraindicaciones señaladas.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Se muestran 5 de las 20 autorizaciones vigentes (todas son monofármaco, en cápsula blanda)" | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Zenatane (isotretinoin) prescribing information, Dr. Reddy's Laboratories Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=27b3cf26-f22e-5b70-1c24-009933b7c6ee) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

