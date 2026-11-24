---
layout: default
title: Carvedilol
parent: Solo predicción del modelo (L5)
nav_order: 150
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "CARVEDILOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
description: "Carvedilol: nueva indicación predicha, Malignant hypertensive renal disease (nivel de evidencia L5). En España, autorizaciones de la AEMPS: al menos 20"
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
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 16; revocadas o suspendidas: 4) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Carvedilol (traducción no oficial): «COREG es una mezcla racémica en la que la actividad de bloqueo no selectivo de los receptores β-adrenérgicos está presente en el enantiómero S(-) y la actividad de bloqueo α1-adrenérgico está presente en ambos enantiómeros, R(+) y S(-), con igual potencia. COREG no tiene actividad simpaticomimética intrínseca.» Texto original en inglés: "COREG is a racemic mixture in which nonselective β-adrenoreceptor blocking activity is present in the S(-) enantiomer and α1-adrenergic blocking activity is present in both R(+) and S(-) enantiomers at equal potency. COREG has no intrinsic sympathomimetic activity." ([DailyMed: Coreg (carvedilol) prescribing information, Waylis Therapeutics LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=07c619c6-4a0c-445e-94fa-664a54f68a39), versión del 2026-07-31; consultado el 2026-11-19). Según la información conocida, carvedilol es un betabloqueante no selectivo con bloqueo alfa-1 adrenérgico y propiedades antioxidantes, y su eficacia en hipertensión está establecida. Mecanísticamente, la reducción de la presión arterial podría ser aplicable a formas graves de hipertensión.

La hipertensión renovascular maligna es una forma secundaria y grave de hipertensión. Sin embargo, en la enfermedad renovascular los principales motores son la activación del sistema renina-angiotensina y la estenosis de la arteria renal, por lo que el vínculo con el bloqueo beta/alfa-1 es solo una inferencia. Carvedilol no es un tratamiento de primera línea reconocido para la hipertensión maligna.

Otras predicciones del modelo con puntajes similares (ver nota al final de la sección de conclusión) comparten esta limitación: se apoyan en la etiqueta común de "hipertensión" más que en una fisiopatología compartida.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

## Información de Mercado en España

El texto de indicación aprobada no está disponible en los datos compilados.

<!-- review:begin es-lic-20261105-carvedilol-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Se listan 5 de las 20 autorizaciones vigentes (todas de medicamentos con carvedilol como único principio activo). El texto de indicación aprobada no está disponible en los datos compilados." Eliminado: el número o el estado de comercialización de las autorizaciones no coincidía con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-carvedilol-1 -->

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 59695 | COROPRES 25 mg COMPRIMIDOS | COMPRIMIDO | Cheplapharm Arzneimittel Gmbh | Comercializada |
| 65885 | CARVEDILOL CINFAMED 6,25 mg COMPRIMIDOS EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Laboratorios Cinfa S.A. | Comercializada |
| 61281 | COROPRES 6,25 mg COMPRIMIDOS | COMPRIMIDO | Cheplapharm Arzneimittel Gmbh | Comercializada |
| 70697 | CARVEDILOL TEVA-RATIOPHARM 25 mg COMPRIMIDOS EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Teva Pharma S.L.U. | Comercializada |
| 70293 | CARVEDILOL ALMUS 6,25 mg COMPRIMIDOS EFG | COMPRIMIDO | Almus Farmaceutica S.A.U. | Comercializada |
| 68471 | NORMOTRIDE 6,25 mg COMPRIMIDOS EFG | COMPRIMIDO | Arafarma Group S.A. | Comercializada |
| 68877 | CARVEDILOL NORMON 25 mg COMPRIMIDOS EFG | COMPRIMIDO | Laboratorios Normon S.A. | Comercializada |
| 66046 | CARVEDILOL SANDOZ 6,25 mg COMPRIMIDOS EFG | COMPRIMIDO | Sandoz Farmaceutica S.A. | Comercializada |
| 67966 | NORMOTRIDE 25 mg COMPRIMIDOS EFG | COMPRIMIDO | Arafarma Group S.A. | Comercializada |
| 65872 | CARVEDILOL KERN PHARMA 25 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Kern Pharma S.L. | Comercializada |

Se muestran 10 de al menos 20 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas. Los datos de este informe solo incluyen parte de las autorizaciones.

<!-- licenses:end -->

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

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Se listan 5 de las 20 autorizaciones vigentes (todas de medicamentos con carvedilol como único principio activo)" | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Coreg (carvedilol) prescribing information, Waylis Therapeutics LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=07c619c6-4a0c-445e-94fa-664a54f68a39) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

