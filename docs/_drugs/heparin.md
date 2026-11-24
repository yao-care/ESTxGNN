---
layout: default
title: Heparin
parent: Solo predicción del modelo (L5)
nav_order: 392
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "Heparin"
predicted_indications: ["thrombophilia due to protein C deficiency, autosomal recessive", "primary release disorder of platelets"]
description: "Heparin: nueva indicación predicha, Trombofilia por deficiencia de proteína C, autosómica recesiva (thrombophilia due to protein C deficiency… (nivel de evidencia L5). Indicación original: No consta …"
---

# Heparin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Heparin: Trombofilia por deficiencia de proteína C, autosómica recesiva (thrombophilia due to protein C deficiency, autosomal recessive)
{: .text-alpha }

## Resumen en Una Frase

La heparina es un anticoagulante utilizado originalmente en indicaciones como la embolia pulmonar, la coagulación intravascular diseminada y la púrpura fulminante.
El modelo TxGNN predice que podría ser efectiva para la **trombofilia por deficiencia de proteína C (autosómica recesiva)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden específicamente esta dirección; se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Trombofilia por deficiencia de proteína C, autosómica recesiva (thrombophilia due to protein C deficiency, autosomal recessive) |
| Puntaje de Predicción TxGNN | 0.9929 |
| Nivel de Evidencia | L5 (solo predicción del modelo, sin estudios reales; el análisis preliminar lo clasificaba como L4) |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 5 de 6; revocadas o suspendidas: 1) |
| Número de Autorizaciones | 6 (comercializadas: 5) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Heparin (traducción no oficial): «La heparina interactúa con la proteína plasmática de origen natural antitrombina III e induce un cambio conformacional que potencia notablemente la actividad inhibidora de serina proteasas de la antitrombina III, con lo que inhibe los factores de coagulación activados que participan en la secuencia final, en particular Xa y IIa. Pequeñas cantidades de heparina inhiben el factor Xa, y cantidades mayores inhiben la trombina (factor IIa).» Texto original en inglés: "Heparin interacts with the naturally occurring plasma protein, antithrombin III, to induce a conformational change, which markedly enhances the serine protease activity of antithrombin III, thereby inhibiting the activated coagulation factors involved in the closing sequence, particularly Xa and IIa. Small amounts of heparin inhibit Factor Xa, and larger amounts inhibit thrombin (Factor IIa)." ([DailyMed: Heparin Sodium And Dextrose (heparin sodium) prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=eede8a0c-5ae6-4166-84b3-12081405f08e), versión del 2026-05-25; consultado el 2026-11-19). Según la información conocida, la heparina potencia la actividad de la antitrombina (SERPINC1, con la que interactúa según los datos farmacológicos) e inhibe la trombina y el factor Xa. Esto reduce la formación de coágulos.

La deficiencia de proteína C genera un estado de hipercoagulabilidad, por lo que la anticoagulación con heparina podría contrarrestarlo de forma biológicamente plausible. Además, existe solapamiento con una de las indicaciones originales, la púrpura fulminante, que a menudo se asocia con deficiencia grave de proteína C.

Conviene matizar que el uso de la heparina como puente o tratamiento adyuvante en esta condición se apoya aquí solo en conocimiento general, no en la evidencia aportada. El tratamiento de reemplazo estándar es el concentrado de proteína C, y el inicio de warfarina conlleva un riesgo conocido de necrosis cutánea en estos pacientes, lo que hace relevante el solapamiento con heparina.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal predicha.

Nota: para la segunda predicción (trastorno primario de liberación plaquetaria, puntaje 0.9906) se recuperaron 20 publicaciones, pero ninguna evalúa la heparina como tratamiento de ese trastorno (tratan cirrosis, trombocitopenia inducida por heparina, tromboembolia asociada al cáncer, COVID-19, entre otros temas). Esa predicción tiene un nivel de evidencia L5, un mecanismo cuestionable (la anticoagulación podría agravar el sangrado) y también se recomienda Hold.

---

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 58691 | HEPARINA SODICA ROVI 1000 UI/ml SOLUCIÓN INYECTABLE | SOLUCIÓN INYECTABLE | Laboratorios Farmaceuticos Rovi S.A. | Comercializada |
| 56465 | HEPARINA SODICA SALA 1.000 UI/ml | SOLUCIÓN INYECTABLE | Laboratorio Reig Jofre, S.A. | Comercializada |
| 58678 | MENAVEN 1000 UI/G GEL | GEL | Laboratorios Menarini S.A. | Comercializada |
| 58693 | HEPARINA SODICA ROVI 5000 UI/ml SOLUCION INYECTABLE | SOLUCIÓN INYECTABLE | Laboratorios Farmaceuticos Rovi S.A. | Comercializada |
| 56029 | HEPARINA SODICA SALA 5000 UI/ml | SOLUCIÓN INYECTABLE | Laboratorio Reig Jofre, S.A. | Comercializada |
| 58679 | MENAVEN 1000 UI/G CREMA | POMADA | Laboratorios Menarini S.A. | Revocada |

Se muestran las 6 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

Hay presentaciones inyectables y tópicas (gel y crema). Las inyectables son las relevantes para una indicación sistémica como la predicha.

---

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no texto del prospecto)**:
  - Hemorrágicas y de coagulación: trombocitopenia, trombocitopenia inducida por heparina, hemofilia, trastornos de la coagulación, déficit de antitrombina III, defectos plaquetarios cualitativos, trombastenia de Glanzmann, hemorragia intracraneal e intracerebral, desprendimiento de placenta.
  - Hepáticas y digestivas: insuficiencia hepática, úlcera péptica activa, colitis ulcerosa y enfermedad inflamatoria intestinal, enfermedad de las vías biliares, ictericia obstructiva.
  - Vasculares y oculares: endocarditis infecciosa y subaguda bacteriana, retinopatía diabética e hipertensiva, enfermedades de la retina, arteriosclerosis obliterante, catarata diabética.
  - Otras: osteoporosis y osteoporosis posmenopáusica.
- **Interacciones farmacológicas**: los datos disponibles describen interacciones farmacológicas con la serpina C1 (antitrombina, SERPINC1) y con la glicoproteína Spike del coronavirus (SARS-CoV-2); no hay interacciones con otros fármacos.

Consultar el prospecto para las advertencias principales, que no están disponibles en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (0.9929) y un vínculo mecanístico plausible, pero no existe ningún ensayo clínico ni publicación que la respalde, por lo que es solo una predicción computacional. Además, el estándar de tratamiento es el concentrado de proteína C, y faltan los datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), un faltante bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Revisión sistemática de la literatura sobre el uso de heparina como puente o adyuvante en la deficiencia de proteína C y la púrpura fulminante neonatal.
- Evaluar la compatibilidad de vías de administración y la comparación con el concentrado de proteína C.
- Definir un plan de monitoreo de seguridad (plaquetas, riesgo de sangrado) para esta población.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Heparin Sodium And Dextrose (heparin sodium) prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=eede8a0c-5ae6-4166-84b3-12081405f08e) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

