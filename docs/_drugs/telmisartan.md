---
layout: default
title: Telmisartan
parent: Solo predicción del modelo (L5)
nav_order: 770
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-31
monitor_inn: "telmisartan"
predicted_indications: ["Prinzmetal angina", "brain stem infarction", "ABri amyloidosis", "cerebral artery occlusion", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "intracerebral hemorrhage", "Braddock syndrome"]
description: "Telmisartan: nueva indicación predicha, Angina de Prinzmetal (Prinzmetal angina) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Telmisartan
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Telmisartan: Angina de Prinzmetal (Prinzmetal angina)
{: .text-alpha }

## Resumen en Una Frase

Telmisartán es un antagonista del receptor de angiotensina II (ARA-II) utilizado originalmente para tratar la hipertensión arterial y para la prevención de eventos cerebrovasculares.
El modelo TxGNN predice que podría ser efectivo para la **angina de Prinzmetal** (angina vasoespástica).
Actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, por lo que se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Angina de Prinzmetal (Prinzmetal angina) |
| Puntaje de Predicción TxGNN | 0.9998 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 14) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, telmisartán bloquea el receptor AT1 de la angiotensina II y actúa además como agonista parcial de PPARγ. Su eficacia en la hipertensión está comprobada, y mecanísticamente podría ser aplicable a la angina de Prinzmetal.

La angina de Prinzmetal está causada por el vasoespasmo de las arterias coronarias. El bloqueo del receptor AT1 y la activación parcial de PPARγ podrían influir en el tono vascular y en la función endotelial, que son procesos relevantes en este vasoespasmo. La hipertensión y la angina vasoespástica comparten, por tanto, un componente de regulación del tono vascular.

Esta relación es **hipotética**. No se recuperó ningún ensayo ni publicación que la respalde, y la similitud con la indicación original no ha sido evaluada formalmente.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Telmisartán está comercializado en España con 20 autorizaciones vigentes, todas de medicamento único (sin combinaciones) y ninguna cancelada. Los datos compilados no incluyen el texto de la indicación aprobada de cada autorización. A continuación se muestran 5 de ellas:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 98089007IP3 | PRITOR 80 mg comprimidos (Bayer AG) | Comprimido |
| 98090002 | MICARDIS 40 mg comprimidos (Boehringer Ingelheim) | Comprimido |
| 98090022 | MICARDIS 80 mg comprimidos (Boehringer Ingelheim) | Comprimido |
| 98089002 | PRITOR 40 mg comprimidos (Bayer AG) | Comprimido |
| 110632009 | Tolura 40 mg comprimidos EFG (Krka) | Comprimido |

El resto son genéricos (EFG) de 20, 40 y 80 mg, en comprimido o comprimido recubierto con película.

---

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no según el prospecto)**: se asocian al fármaco las siguientes condiciones:
  - Hepáticas y biliares: insuficiencia hepática, enfermedad hepática, coma hepático, encefalopatía hepática, colestasis (incluida la colestasis intrahepática recurrente benigna y la familiar), enfermedad de la vesícula biliar, ictericia neonatal y pancreatitis.
  - Renales y urinarias: enfermedad renal, anuria, piouréter, obstrucción de la arteria renal y nefrocalcinosis.
  - Metabólicas y endocrinas: diabetes mellitus, cetoacidosis diabética, hiperuricemia, gota, hipercalcemia, trastornos del metabolismo del fósforo, deficiencia de potasio, hiperparatiroidismo y osteítis fibrosa.
  - Otras: hipotensión, lupus eritematoso sistémico (incluido el pediátrico).
- **Interacciones Farmacológicas**: se identificaron 185 interacciones.
  - **Mayores**: citrato de potasio y bicarbonato de potasio, por riesgo de hiperpotasemia.
  - **Moderadas (ejemplos)**: hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida, ácido acetilsalicílico, morfina, bupropión, dronabinol, canagliflozina, dapagliflozina, empagliflozina, exenatida, insulinas, ácido picosulfúrico, sulfato de sodio y polietilenglicol con electrolitos.

No se dispone de las advertencias ni de las contraindicaciones del prospecto de la AEMPS. Consultar el prospecto para la información de seguridad oficial.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La angina de Prinzmetal tiene un puntaje alto en el modelo (0.9998), pero no hay ningún ensayo clínico ni publicación que la respalde (nivel L5). El vínculo mecanístico es solo plausible, y la seguridad no puede evaluarse sin el prospecto.

**Para avanzar se necesita:**
- Revisión de la literatura y de registros de ensayos específicos sobre telmisartán o ARA-II en vasoespasmo coronario.
- Datos del mecanismo de acción y estudios preclínicos o de mecanismo que conecten el bloqueo AT1/PPARγ con el vasoespasmo coronario.
- Obtención y análisis del prospecto de la AEMPS (advertencias y contraindicaciones), un paso bloqueante para el cribado de seguridad.
- Evaluación del riesgo en pacientes con angina vasoespástica que presenten tendencia a hipotensión, compromiso renal o hiperpotasemia.

**Nota:** entre las demás predicciones del modelo para este fármaco, la hemorragia intracerebral (nivel L2, "Proceed with Guardrails") y la oclusión de arteria cerebral (nivel L3) cuentan con más respaldo. La evidencia de la primera proviene de la estrategia de triple píldora del ensayo TRIDENT, no de telmisartán por separado. Podrían priorizarse frente a la angina de Prinzmetal.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

