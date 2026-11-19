---
layout: default
title: Siponimod
parent: Solo predicción del modelo (L5)
nav_order: 739
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-20
description: "Siponimod: nueva indicación predicha, Hipertensión pulmonar (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (el texto de indicación de las…"
monitor_inn: "SIPONIMOD"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "kyphoscoliotic heart disease", "migraine with brainstem aura", "Prinzmetal angina", "rheumatoid arthritis", "atrophoderma vermiculata"]
---

# Siponimod
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

## Siponimod: De Indicación Original No Especificada a Hipertensión Pulmonar
{: .text-alpha }

## Resumen en Una Frase

Siponimod es un modulador selectivo de los receptores S1P1/S1P5 que se comercializa en España con el nombre Mayzent. Los datos compilados para este informe no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **hipertensión pulmonar**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (el texto de indicación de las autorizaciones está vacío) |
| Nueva Indicación Predicha | Hipertensión pulmonar |
| Puntaje de Predicción TxGNN | 0,9968 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 3 de 3) |
| Número de Autorizaciones | 3 (comercializadas: 3) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Siponimod (traducción no oficial): «El siponimod es un modulador del receptor de S1P. El siponimod se une con alta afinidad a los receptores 1 y 5 de S1P. El siponimod bloquea la capacidad de los linfocitos de salir de los ganglios linfáticos, lo que reduce el número de linfocitos en la sangre periférica.» Texto original en inglés: "Siponimod is an S1P receptor modulator. Siponimod binds with high affinity to S1P receptors 1 and 5. Siponimod blocks the capacity of lymphocytes to egress from lymph nodes, reducing the number of lymphocytes in peripheral blood." ([DailyMed: Mayzent (siponimod) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=44492772-5aed-4627-bd85-e8e89f308bb3), versión del 2026-06-30; consultado el 2026-11-19). Según la información conocida, siponimod es un modulador selectivo de los receptores de esfingosina-1-fosfato (S1P1 y S1P5). Estos receptores intervienen en la migración de los linfocitos y en la función de barrera endotelial.

La señalización de S1P se ha relacionado con la remodelación vascular pulmonar y con la función de barrera del endotelio, lo que ofrece un posible vínculo teórico con la hipertensión pulmonar. Sin embargo, la modulación de S1P1 provoca bradicardia transitoria y podría tener efectos impredecibles sobre la vasculatura pulmonar.

Este vínculo es puramente computacional (puntaje alto de TxGNN) y no cuenta con ensayos ni literatura de apoyo. No se pudo establecer la relación con la indicación original, ya que esta no figura en los datos.

### Otras predicciones del modelo (para contexto)

| Posición | Indicación predicha | Puntaje TxGNN | Nivel | Comentario |
|------|------|------|------|------|
| 2 | Trastorno de migraña | 0,9966 | L4 | Solo un reporte de caso/comentario (2022) y una entrada genérica de «Neurología» |
| 3 | Cardiopatía cifoscoliótica | 0,9956 | L5 | Sin vínculo mecanístico plausible; la puntuación procede del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes aprendidas por el modelo entre enfermedades relacionadas, no evidencia biológica |
| 4 | Migraña con aura de tronco encefálico | 0,9956 | L4 | Misma publicación de 2022, no específica |
| 6 | Angina de Prinzmetal | 0,9934 | L5 | Sin evidencia; preocupación de seguridad cardíaca |
| 7 | Artritis reumatoide | 0,9916 | L4 | La más plausible biológicamente (secuestro linfocitario), aún en fase de hipótesis |
| 8 | Atrofodermia vermiculada | 0,9910 | L5 | Sin vínculo mecanístico; probable artefacto computacional |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para hipertensión pulmonar.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1191414003 | MAYZENT 2 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 1191414001 | MAYZENT 0,25 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 1191414007 | MAYZENT 1 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |

Titular de las tres autorizaciones: Novartis Europharm Limited.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las que se muestran, muchas son de nivel **Mayor**:
  - Antiácidos/antagonistas H2: famotidina, ranitidina, cimetidina.
  - Corticosteroides: hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida.
  - Antieméticos: aprepitant, dolasetrón, palonosetrón.
  - Antibióticos: claritromicina, levofloxacino.
  - Otros: oxandrolona.
  - De nivel **Moderado**: loperamida, bisacodilo, ácido picosulfúrico, polietilenglicol 3350 con electrolitos, sulfato de sodio, naltrexona.
- **Consideración cardíaca (según el análisis de la predicción)**: la modulación de S1P1 puede causar bradicardia y retraso de la conducción auriculoventricular. Esto es especialmente relevante en hipertensión pulmonar, cardiopatía cifoscoliótica y angina de Prinzmetal.

Para advertencias y contraindicaciones, consultar el prospecto, ya que no se dispone de esos datos.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para hipertensión pulmonar se basa únicamente en el modelo (L5), sin ensayos ni literatura, con un vínculo mecanístico débil y posibles riesgos cardiovasculares. Entre las demás predicciones, solo la artritis reumatoide muestra un fundamento de clase razonable, aunque sigue en fase de hipótesis.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias, contraindicaciones e indicación aprobada), un vacío crítico que impide el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Estudios preclínicos de siponimod en modelos de hipertensión pulmonar.
- Evaluación específica del riesgo cardiovascular (bradicardia, conducción AV) en pacientes con enfermedad cardiopulmonar.
- Priorizar, de forma exploratoria, la revisión de la hipótesis de artritis reumatoide como alternativa más plausible.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Mayzent (siponimod) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=44492772-5aed-4627-bd85-e8e89f308bb3) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

