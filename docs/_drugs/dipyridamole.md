---
layout: default
title: Dipyridamole
parent: Solo predicción del modelo (L5)
nav_order: 256
evidence_level: L5
indication_count: 6
monitor_inn: "dipyridamole"
predicted_indications: ["sick sinus syndrome 2, autosomal dominant", "sarcoglycanopathy", "Wildervanck syndrome", "macrocephaly, dysmorphic facies, and psychomotor retardation", "lateral sinus thrombosis", "cavernous sinus thrombosis"]
last_modified_at: 2026-11-05
description: "Dipyridamole: nueva indicación predicha, Sick sinus syndrome 2, autosomal dominant (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 1 (comercializadas: 1)"
---

# Dipyridamole
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

## Dipyridamole: Sick sinus syndrome 2, autosomal dominant
{: .text-alpha }

## Resumen en Una Frase

Dipiridamol es un fármaco antiagregante plaquetario comercializado en España.
El modelo TxGNN predice que podría ser efectivo para **síndrome del seno enfermo 2, autosómico dominante (sick sinus syndrome 2, autosomal dominant)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; la predicción se basa solo en el puntaje del modelo y existe una posible preocupación de seguridad.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Sick sinus syndrome 2, autosomal dominant |
| Puntaje de Predicción TxGNN | 0.9989 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Dipyridamole (traducción no oficial): «El dipiridamol inhibe la captación de adenosina en las plaquetas, las células endoteliales y los eritrocitos in vitro e in vivo; la inhibición se produce de manera dependiente de la dosis a concentraciones terapéuticas (0.5 a 1.9 mcg/mL). Esta inhibición da lugar a un aumento de las concentraciones locales de adenosina, que actúa sobre el receptor A 2 plaquetario, estimulando así la adenilato ciclasa plaquetaria y aumentando las concentraciones plaquetarias de 3',5'-monofosfato cíclico de adenosina (cAMP).» Texto original en inglés: "Dipyridamole inhibits the uptake of adenosine into platelets, endothelial cells and erythrocytes in vitro and in vivo; the inhibition occurs in a dose-dependent manner at therapeutic concentrations (0.5 to 1.9 mcg/mL). This inhibition results in an increase in local concentrations of adenosine which acts on the platelet A 2 -receptor thereby stimulating platelet adenylate cyclase and increasing platelet cyclic-3',5'-adenosine monophosphate (cAMP) levels." ([DailyMed: dipyridamole prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=226099e2-70bb-4b9b-bb52-c20fbca2aec5), versión del 2026-04-29; consultado el 2026-11-19). Según la información farmacológica conocida, el dipiridamol aumenta la adenosina extracelular, lo que produce efecto antiagregante y vasodilatador.

Ese mismo mecanismo plantea dudas para esta predicción: la adenosina puede enlentecer la conducción en el nodo sinusal y en el nodo auriculoventricular. Por ello, el fármaco podría empeorar, en lugar de tratar, la disfunción del nodo sinusal.

No se ha establecido una justificación terapéutica. La predicción es puramente computacional, con un puntaje alto pero sin respaldo clínico, y conlleva una posible preocupación de seguridad.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 56981 | PERSANTIN 100 mg comprimidos recubiertos | Comprimido recubierto | Sin texto de indicación en los datos compilados |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 321 interacciones en total. Las de nivel moderado incluyen dexfenfluramina, sibutramina y fenfluramina. Otras interacciones registradas, sin nivel de gravedad definido, incluyen ácido acetilsalicílico, cimetidina, omeprazol, pantoprazol, lansoprazol, metformina, glimepirida, morfina y simvastatina.

Consultar el prospecto para el resto de la información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo (0,9989), sin ensayos clínicos ni literatura. Además, el efecto del dipiridamol sobre la adenosina podría ser perjudicial para la función del nodo sinusal.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y una justificación biológica plausible para esta enfermedad
- Evaluación del riesgo de bradicardia y de alteraciones de la conducción
- Revisión de las advertencias y contraindicaciones del prospecto
- Estudios preclínicos o clínicos que investiguen directamente esta indicación

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: dipyridamole prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=226099e2-70bb-4b9b-bb52-c20fbca2aec5) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

