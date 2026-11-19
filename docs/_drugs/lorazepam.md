---
layout: default
title: Lorazepam
parent: Solo predicción del modelo (L5)
nav_order: 483
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
monitor_inn: "LORAZEPAM"
predicted_indications: ["trigeminal nerve neoplasm"]
description: "Lorazepam: nueva indicación predicha, Neoplasia del nervio trigémino (trigeminal nerve neoplasm) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: al menos 20"
---

# Lorazepam
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

## Lorazepam: Neoplasia del nervio trigémino (trigeminal nerve neoplasm)
{: .text-alpha }

## Resumen en Una Frase

Lorazepam es una benzodiazepina utilizada originalmente para el tratamiento de la ansiedad y de diversos cuadros convulsivos (como el estado epiléptico).
El modelo TxGNN predice que podría ser efectivo para **neoplasia del nervio trigémino**, pero **no existen ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Neoplasia del nervio trigémino (trigeminal nerve neoplasm) |
| Puntaje de Predicción TxGNN | 0.9987 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 12; autorizadas no comercializadas: 4; revocadas o suspendidas: 4) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Lorazepam (traducción no oficial): «El lorazepam ejerce su efecto en el tratamiento de los trastornos de ansiedad mediante la unión al sitio de las benzodiazepinas de los receptores del ácido gamma-aminobutírico A (GABA A ) en el cerebro y potencia la inhibición sináptica mediada por el GABA.» Texto original en inglés: "Lorazepam exerts its effect for the treatment of anxiety disorders through binding to the benzodiazepine site of the gamma-aminobutyric acid-A (GABA A ) receptors in the brain and enhances GABA-mediated synaptic inhibition." ([DailyMed: Loreev Xr (lorazepam) prescribing information, Almatica Pharma LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=227734c1-bf01-9607-73ea-5a1f38a89bd9), versión del 2025-10-08; consultado el 2026-11-19). Según la información conocida, lorazepam es una benzodiazepina que potencia la inhibición mediada por el receptor GABA-A, con efectos ansiolíticos, sedantes y anticonvulsivos.

La relación entre la indicación original y la nueva es débil. La ansiedad y la epilepsia son trastornos de hiperexcitabilidad neuronal sobre los que actúa el fármaco, mientras que una neoplasia del nervio trigémino es un tumor. No se conoce un vínculo mecanístico claro: lorazepam no tiene actividad antineoplásica ni modificadora de la enfermedad en tumores nerviosos. A lo sumo podría aliviar síntomas acompañantes (ansiedad, convulsiones, malestar asociado al dolor).

Por tanto, el puntaje muy alto de TxGNN proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica; no cuenta con respaldo clínico ni bibliográfico que la sustente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

<!-- review:begin es-lic-20261105-lorazepam-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Se listan 5 de las 20 autorizaciones vigentes (todas de principio activo único):" Eliminado: el número o el estado de comercialización de las autorizaciones no coincidía con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-lorazepam-1 -->

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 90287 | Lorazepam Aurovitas 1 mg comprimidos EFG | Comprimido | No disponible |
| 83684 | Lorazepam Aristo 2,5 mg comprimidos bucodispersables EFG | Comprimido bucodispersable | No disponible |
| 88360 | Temelor 4 mg/ml solución inyectable EFG | Solución inyectable | No disponible |
| 49796 | Orfidal 1 mg comprimidos | Comprimido | No disponible |
| 68477 | Lorazepam Cinfa 1 mg comprimidos EFG | Comprimido | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): insuficiencia hepática, enfermedad hepática, encefalopatía hepática y coma hepático; enfermedad renal; porfiria; glaucoma de ángulo abierto y de ángulo cerrado; síndrome de apnea del sueño, síndrome de hipoventilación central congénita e insuficiencia respiratoria; trastornos relacionados con sustancias y abuso/dependencia de sustancias; enfermedad de la vesícula biliar.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones. Entre las principales destacan las de nivel **mayor** con morfina (incluida la morfina liposomal), por riesgo de depresión del sistema nervioso central y respiratoria. Hay interacciones **moderadas** con bupropión, dronabinol, nabilona, teduglutida, metoclopramida, opio y sibutramina. Los antiácidos (óxido de magnesio, hidróxido de aluminio, carbonato de calcio, entre otros) presentan interacciones menores.
- **Señal adicional**: la literatura recuperada para otras indicaciones señala riesgo de toxicidad por propilenglicol con infusiones parenterales de lorazepam a dosis altas, además de tolerancia, dependencia y deterioro al día siguiente en el uso hipnótico.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de ensayos clínicos, literatura y vínculo mecanístico plausible; el puntaje alto del modelo no basta por sí solo. Lorazepam solo podría tener un papel sintomático, no terapéutico sobre el tumor.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y una hipótesis biológica que conecte el fármaco con la neoplasia del nervio trigémino
- Revisión sistemática de la literatura y de registros de ensayos clínicos para esta indicación
- Obtención de las advertencias y contraindicaciones del prospecto de la AEMPS (actualmente sin datos, lo que bloquea el cribado de seguridad)

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Se listan 5 de las 20 autorizaciones vigentes (todas de principio activo único):" | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Loreev Xr (lorazepam) prescribing information, Almatica Pharma LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=227734c1-bf01-9607-73ea-5a1f38a89bd9) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

