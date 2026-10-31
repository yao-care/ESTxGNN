---
layout: default
title: Carvedilol
parent: Solo predicción del modelo (L5)
nav_order: 150
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-31
monitor_inn: "CARVEDILOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
description: "Carvedilol: nueva indicación predicha, Malignant hypertensive renal disease (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Carvedilol
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

## Carvedilol: Malignant hypertensive renal disease
{: .text-alpha }

## Resumen en Una Frase

Carvedilol es un betabloqueante no selectivo con actividad bloqueante alfa-1, utilizado originalmente para el tratamiento de la hipertensión.
El modelo TxGNN predice que podría ser efectivo para **hipertensión renovascular maligna**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden directamente esta predicción (solo predicción computacional).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Malignant hypertensive renal disease |
| Puntaje de Predicción TxGNN | 0.9955 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 16) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, carvedilol es un betabloqueante no selectivo con bloqueo alfa-1 adrenérgico y propiedades antioxidantes, y su eficacia en hipertensión está establecida. Mecanísticamente, la reducción de la presión arterial podría ser aplicable a formas graves de hipertensión.

La hipertensión renovascular maligna es una forma secundaria y grave de hipertensión. Sin embargo, en la enfermedad renovascular los principales motores son la activación del sistema renina-angiotensina y la estenosis de la arteria renal, por lo que el vínculo con el bloqueo beta/alfa-1 es solo una inferencia. Carvedilol no es un tratamiento de primera línea reconocido para la hipertensión maligna.

Otras predicciones del modelo con puntajes similares (ver nota al final de la sección de conclusión) comparten esta limitación: se apoyan en la etiqueta común de "hipertensión" más que en una fisiopatología compartida.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones vigentes (todas de medicamentos con carvedilol como único principio activo). El texto de indicación aprobada no está disponible en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 59695 | COROPRES 25 mg comprimidos | Comprimido | No disponible |
| 61281 | COROPRES 6,25 mg comprimidos | Comprimido | No disponible |
| 65885 | Carvedilol Cinfamed 6,25 mg comprimidos EFG | Comprimido recubierto con película | No disponible |
| 66921 | Carvedilol Teva 25 mg comprimidos EFG | Comprimido | No disponible |
| 68471 | Normotride 6,25 mg comprimidos EFG | Comprimido | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no texto del prospecto)**: insuficiencia hepática, asma (incluidos asma intrínseco y alérgico), bronquitis, enfisema pulmonar y otras enfermedades bronquiales, diabetes mellitus y cetoacidosis diabética, trastornos hipotensivos, enfermedad vascular periférica (claudicación intermitente, enfermedad arterial periférica), bloqueo auriculoventricular, síndrome del seno enfermo (incluida la forma familiar), angina de Prinzmetal, anafilaxia y síndrome del iris flácido intraoperatorio.
- **Interacciones Farmacológicas** (100 interacciones registradas; se muestran las principales):
  - **Mayor**: epinefrina.
  - **Moderada**: hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida, hiosciamina, atropina, bupropión, morfina, lorcaserina, canagliflozina, acetohexamida y sales de calcio (fosfato, acetato, carbonato, citrato).
  - **Menor**: ácido acetilsalicílico, hidróxido de aluminio, atapulgita.
- **Contexto pulmonar**: la literatura revisada señala que el bloqueo beta no selectivo requiere evaluación cuidadosa de seguridad en pacientes con enfermedad pulmonar, y los betabloqueantes se usan con cautela en hipertensión arterial pulmonar por el posible deterioro del ventrículo derecho.

Para información completa de advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción solo cuenta con respaldo computacional (nivel L5), sin ensayos clínicos ni literatura, y carvedilol no es un tratamiento reconocido para la hipertensión maligna de origen renovascular, donde predomina la activación del sistema renina-angiotensina.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y su relación con la fisiopatología renovascular.
- Revisión del prospecto de la AEMPS (advertencias y contraindicaciones) para completar el análisis de seguridad.
- Revisión sistemática de literatura y ensayos específicos en hipertensión renovascular/maligna.
- Comparación con los tratamientos estándar (bloqueo del sistema renina-angiotensina, otros antihipertensivos) para determinar un posible valor añadido.

**Nota sobre otras predicciones del modelo:**

| Indicación Predicha | Puntaje TxGNN | Nivel de Evidencia | Recomendación | Comentario |
|------|------|------|------|------|
| Enfermedad renal hipertensiva maligna | 0,9955 | L5 | Hold | Muy cercana a la indicación aprobada; sin ensayos ni literatura. Posible beneficio renal por propiedades antioxidantes, solo como hipótesis. |
| Hipertensión pulmonar de mecanismo multifactorial poco claro | 0,9954 | L5 | Hold | Probable coincidencia por la etiqueta "hipertensión"; fisiopatología distinta de la sistémica. |
| Hipertensión pulmonar por enfermedad pulmonar y/o hipoxia | 0,9954 | L5 | Pregunta de investigación | Evidencia preclínica indirecta (p. ej., carvedilol revirtió la hipertensión inducida por hipoxia intermitente en ratas, PMID 26291659, y modelos de hipertrofia ventricular derecha por hipoxia); gran parte de la literatura recuperada es ajena al tema y no hay ensayos clínicos. |
| Síndrome de Braddock | 0,9937 | L5 | Hold | Sin justificación mecanística evidente; probable artefacto del modelo TxGNN (aprendizaje profundo). |
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

