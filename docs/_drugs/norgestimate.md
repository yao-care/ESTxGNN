---
layout: default
title: Norgestimate
parent: Solo predicción del modelo (L5)
nav_order: 576
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
monitor_inn: "norgestimate"
predicted_indications: ["zinc, elevated plasma"]
description: "Norgestimate: nueva indicación predicha, Zinc plasmático elevado (zinc, elevated plasma) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 3 (comercializadas: 1)"
---

# Norgestimate
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

## Norgestimate: Zinc plasmático elevado (zinc, elevated plasma)
{: .text-alpha }

## Resumen en Una Frase

Norgestimato es un progestágeno (profármaco cuyos metabolitos activos incluyen levonorgestrel y norelgestromina), habitualmente combinado con etinilestradiol, y su uso original está asociado al acné y a trastornos relacionados con la menopausia, como la osteoporosis posmenopáusica y la vaginitis atrófica.
El modelo TxGNN predice que podría ser efectivo para **zinc plasmático elevado**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Zinc plasmático elevado (zinc, elevated plasma) |
| Puntaje de Predicción TxGNN | 0.9906 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 3; revocadas o suspendidas: 2) |
| Número de Autorizaciones | 3 (comercializadas: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para norgestimate and ethinyl estradiol (combinación que contiene Norgestimate) (traducción no oficial): «Si bien la combinación de etinilestradiol y norgestimato aumenta la globulina fijadora de hormonas sexuales (SHBG) y disminuye la testosterona libre, no se ha establecido la relación entre estos cambios y una disminución de la gravedad del acné facial en mujeres por lo demás sanas con esta afección cutánea.» Texto original en inglés: "While the combination of ethinyl estradiol and norgestimate increases sex hormone-binding globulin (SHBG) and decreases free testosterone, the relationship between these changes and a decrease in the severity of facial acne in otherwise healthy women with this skin condition has not been established." ([DailyMed: Tri-Sprintec (norgestimate and ethinyl estradiol) prescribing information, Preferred Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1f8b9aad-f31f-4cda-861d-c08a977fc923), versión del 2026-10-12; consultado el 2026-11-19). Según la información conocida, norgestimato es un progestágeno que se combina con etinilestradiol en anticonceptivos orales. Su indicación original es el acné, y mecanísticamente se desconoce si podría ser aplicable a la nueva indicación.

Como conocimiento general (no respaldado por los datos compilados para este informe), los esteroides sexuales y los anticonceptivos orales pueden modificar los niveles circulantes de oligoelementos, como zinc, cobre y ceruloplasmina. Esto sugeriría una posible relación biológica, pero no constituye un vínculo mecanístico demostrado.

Además, el zinc plasmático elevado es un hallazgo de laboratorio y no una enfermedad con una diana terapéutica clara, por lo que el significado clínico de cualquier intervención es incierto. El puntaje de 0,9906 proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| BE141215 | EDELSIN comprimidos (Janssen-Cilag) | Comprimido | No disponible en los datos compilados |
| 83379 | EDELSINE 0,250/0,035 MG comprimidos (Laboratorios Effik) | Comprimido | No disponible en los datos compilados |
| 84027 | LIBERELLE 0,25 MG/0,035 MG comprimidos EFG (Exeltis Healthcare) | Comprimido | No disponible en los datos compilados |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): hipertensión, epilepsia, trastornos de ansiedad y neuróticos, distimia, porfiria, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, hiperglucemia, diabetes mellitus y cetoacidosis diabética, hipertrigliceridemia, hipercalcemia y nefrocalcinosis, hipotiroidismo, lupus eritematoso sistémico, asma, y carcinoma de mama femenino.
- **Interacciones farmacológicas**: se identificaron 38 interacciones. Entre las de nivel **mayor** figuran sugammadex, griseofulvina, bexaroteno, brigatinib, dabrafenib y encorafenib. Entre las de nivel moderado figuran metreleptina, miltefosina, adalimumab, anakinra, cladribina y enasidenib, entre otras (se muestra solo una parte de la lista).

No se dispone de advertencias ni contraindicaciones del prospecto; consultar el prospecto para la información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, sin mecanismo de acción documentado y con una indicación diana que es un hallazgo de laboratorio y no una enfermedad. Además, el perfil de contraindicaciones es amplio.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), requisito previo para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una búsqueda de literatura sobre anticonceptivos orales/progestágenos y zinc plasmático.
- Definir si el zinc plasmático elevado constituye una indicación clínica con relevancia terapéutica.
- Evaluar la compatibilidad de vía de administración y la similitud con las indicaciones originales (actualmente pendientes).

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Tri-Sprintec (norgestimate and ethinyl estradiol) prescribing information, Preferred Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1f8b9aad-f31f-4cda-861d-c08a977fc923) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

