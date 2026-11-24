---
layout: default
title: Isosorbide Dinitrate
parent: Solo predicción del modelo (L5)
nav_order: 434
evidence_level: L5
indication_count: 10
monitor_inn: "isosorbide dinitrate"
predicted_indications: ["alopecia", "congenital hypotrichosis milia", "hypotrichosis simplex of the scalp", "pulmonary hypertension", "diffuse alopecia areata", "vascular disease", "hypertrichosis (disease)", "kyphoscoliotic heart disease", "visceral calciphylaxis", "arterial thoracic outlet syndrome"]
last_modified_at: 2026-11-24
description: "Isosorbide Dinitrate: nueva indicación predicha, Alopecia (nivel de evidencia L5). Indicación original: No disponible (la autorización local no incluye texto de indicación)"
---

# Isosorbide Dinitrate
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

## Dinitrato de isosorbida: De Indicación Original No Registrada a Alopecia
{: .text-alpha }

## Resumen en Una Frase

El dinitrato de isosorbida es un donante de óxido nítrico con efecto vasodilatador. En los datos compilados para este informe, la autorización española del producto no incluye texto de indicación aprobada. El modelo TxGNN predice que podría ser efectivo para **alopecia**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, de modo que se trata solo de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (la autorización local no incluye texto de indicación) |
| Nueva Indicación Predicha | Alopecia |
| Puntaje de Predicción TxGNN | 0,9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado (registros anulados: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 0) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para hydralazine hydrochloride and isosorbide dinitrate (combinación que contiene Isosorbide Dinitrate) (traducción no oficial): «El dinitrato de isosorbida es un vasodilatador que actúa tanto sobre las arterias como sobre las venas.» Texto original en inglés: "Isosorbide dinitrate is a vasodilator affecting both arteries and veins." ([DailyMed: Bidil (hydralazine hydrochloride and isosorbide dinitrate) prescribing information, Azurity Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e1e63cd5-d1e4-4af5-bad5-1ad41ea46b00), versión del 2025-11-30; consultado el 2026-11-19). Según la información conocida, el dinitrato de isosorbida es un donante de óxido nítrico (NO) y un vasodilatador. Su eficacia en la indicación original no puede confirmarse con los datos locales disponibles, porque la autorización española no incluye texto de indicación.

La relación con la alopecia es solo **hipotética**. Se plantea que la vasodilatación podría mejorar la microcirculación del cuero cabelludo, de forma análoga a otros vasodilatadores como el minoxidil. No existe ningún estudio clínico ni publicación que respalde este vínculo, y el puntaje de 0,9999 es únicamente una predicción computacional de similitud en la red de conocimiento.

Este mecanismo debe tomarse con cautela. La alopecia tiene causas diversas (androgénica, autoinmune, genética) que la vasodilatación por sí sola no aborda. Por ello, la plausibilidad biológica es baja y especulativa.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 49679 | ISO-LACER 5 mg COMPRIMIDOS | COMPRIMIDO | Lacer S.A. | Revocada |

Se muestra la única autorización con este principio activo en los datos de CIMA (AEMPS).

<!-- licenses:end -->

La lista puede ser parcial respecto a otros productos, pero los datos compilados registran una única autorización, ya cancelada. Actualmente no hay presentaciones comercializadas de este principio activo en esta base.

---

## Consideraciones de Seguridad

- **Relaciones de contraindicación en el grafo de conocimiento** (no proceden del texto del prospecto): hipotensión, miocardiopatía hipertrófica, enfermedad coronaria, accidente cerebrovascular y trastornos cerebrovasculares, infarto cerebral, infarto de miocardio, trombosis coronaria, hemoglobinopatía, anemia (incluida la macrocítica), hipertiroidismo, enfermedad de Graves, tirotoxicosis, pseudotumor cerebral, hipertensión intracraneal, hemorragia intracerebral, acetilación lenta y síndrome de Rowell. Deben verificarse con la ficha técnica oficial.
- **Interacciones farmacológicas**: se registraron 141 interacciones. Entre las de nivel moderado figuran bupropión, morfina, opio, dronabinol, nabilona, sapropterina, rosiglitazona y los inhibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina, ertugliflozina). La interacción con omeprazol es de nivel menor.

No se dispone de las advertencias y contraindicaciones del prospecto oficial. Consultar el prospecto para la información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para alopecia se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni publicaciones sobre esta enfermedad. El vínculo mecanístico es especulativo y la única autorización local está cancelada.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) del fármaco.
- Estudios preclínicos que evalúen el efecto de los donantes de NO en el folículo piloso.
- Revisión del prospecto oficial (advertencias y contraindicaciones), requisito previo para cualquier evaluación de seguridad.
- Evaluación de la viabilidad de una vía de administración adecuada para el cuero cabelludo, hoy sin definir.
- Valorar por separado otras predicciones del modelo que cuentan con algo más de literatura (por ejemplo, hipertensión pulmonar), cuya evaluación es independiente de esta.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Bidil (hydralazine hydrochloride and isosorbide dinitrate) prescribing information, Azurity Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e1e63cd5-d1e4-4af5-bad5-1ad41ea46b00) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

