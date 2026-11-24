---
layout: default
title: Digoxin
parent: Solo predicción del modelo (L5)
nav_order: 250
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-24
monitor_inn: "Digoxin"
predicted_indications: ["Prinzmetal angina", "duodenal obstruction", "duodenal ulcer (disease)", "duodenogastric reflux", "hypoalphalipoproteinemia"]
description: "Digoxin: nueva indicación predicha, Angina de Prinzmetal (Prinzmetal angina) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 4 (comercializadas: 4)"
---

# Digoxin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Digoxin: Angina de Prinzmetal (Prinzmetal angina)
{: .text-alpha }

## Resumen en Una Frase

Digoxina es un glucósido cardíaco utilizado originalmente para el tratamiento de la fibrilación auricular y la intoxicación digitálica.
El modelo TxGNN predice que podría ser efectiva para **Angina de Prinzmetal**, pero actualmente **no hay ensayos clínicos** y solo **1 publicación** (una revisión no específica de la digoxina) relacionada con esta dirección, por lo que la evidencia es únicamente predictiva.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Angina de Prinzmetal (Prinzmetal angina) |
| Puntaje de Predicción TxGNN | 0.9981 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 4 de 4) |
| Número de Autorizaciones | 4 (comercializadas: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Digoxin (traducción no oficial): «Todas las acciones de la digoxina están mediadas por sus efectos sobre la Na-K ATPasa. Esta enzima, la «bomba de sodio», se encarga de mantener el medio intracelular en todo el organismo, desplazando los iones sodio hacia el exterior de las células y los iones potasio hacia su interior.» Texto original en inglés: "All of digoxin’s actions are mediated through its effects on Na-K ATPase. This enzyme, the “sodium pump,” is responsible for maintaining the intracellular milieu throughout the body by moving sodium ions out of and potassium ions into cells." ([DailyMed: Lanoxin (digoxin) prescribing information, Covis Pharma US, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9ec84cac-6ecc-43dc-8006-6ccc029e2707), versión del 2025-10-17; consultado el 2026-11-19). Según la información conocida, la digoxina inhibe la bomba Na+/K+-ATPasa (subunidad α-1, gen ATP1A1), lo que aumenta el calcio intracelular y la contractilidad miocárdica. Su eficacia en la fibrilación auricular está comprobada, pero no hay una base mecanística clara para la angina de Prinzmetal.

La angina de Prinzmetal se debe a vasoespasmo coronario y se trata con antagonistas del calcio y nitratos. El aumento del calcio intracelular y el potencial de vasoconstricción hacen que la digoxina sea, en teoría, desfavorable para esta indicación.

Por tanto, el alto puntaje de TxGNN (0.9981) es solo una predicción basada en la red de conocimiento, sin vínculo mecanístico creíble. La única publicación asociada (PMID 10736610) es una revisión sobre cronofarmacología del tratamiento antihipertensivo, no específica de la digoxina ni de esta indicación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Revisión | Acta physiologica et pharmacologica Bulgarica | Revisión sobre ritmos circadianos y su impacto en el tratamiento antihipertensivo; no es específica de la digoxina ni de la angina de Prinzmetal |

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 23850 | DIGOXINA TEOFARMA 0,25 mg COMPRIMIDOS | COMPRIMIDO | Teofarma S.R.L. | Comercializada |
| 34566 | DIGOXINA KERN PHARMA 0,25 mg COMPRIMIDOS | COMPRIMIDO | Kern Pharma S.L. | Comercializada |
| 34753 | DIGOXINA KERN PHARMA 0,25 mg/ml SOLUCION INYECTABLE | SOLUCIÓN INYECTABLE | Kern Pharma S.L. | Comercializada |
| 34755 | LANACORDIN PEDIATRICO | SOLUCIÓN ORAL | Kern Pharma S.L. | Comercializada |

Se muestran las 4 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no del prospecto)**: enfermedad renal, deficiencia de potasio, hipercalcemia, nefrocalcinosis, alteraciones del metabolismo del fósforo, infarto de miocardio, trombosis coronaria, cor pulmonale, síndrome de Wolff-Parkinson-White, síndrome del seno enfermo (incluida la forma familiar), fibrilación ventricular, miocardiopatía hipertrófica (incluida la familiar), miocardiopatía restrictiva, bloqueo auriculoventricular, hipotiroidismo (incluido el congénito) y mixedema, miocarditis, pericarditis constrictiva, hemoglobinopatía y piuria ureteral.
- **Interacciones Farmacológicas**: la consulta se completó con 1 registro, correspondiente a la diana farmacológica de la digoxina (subunidad α-1 de la Na+/K+-ATPasa), no a una interacción con otro fármaco. Se debe consultar el prospecto para interacciones clínicas.

Las advertencias y contraindicaciones del prospecto de la AEMPS no están disponibles; consultar el prospecto para la información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5): no hay ensayos clínicos, la única publicación no es específica y el mecanismo de la digoxina es teóricamente desfavorable en el vasoespasmo coronario. Además, varias contraindicaciones cardiovasculares conocidas refuerzan la cautela.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA) y un análisis de su vínculo con el vasoespasmo coronario
- Estudios preclínicos o clínicos específicos de digoxina en angina de Prinzmetal
- Prospecto de la AEMPS con advertencias, contraindicaciones e indicaciones aprobadas, para completar el cribado de seguridad
- Evaluación de la relación riesgo-beneficio frente a los tratamientos estándar (antagonistas del calcio y nitratos)

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Lanoxin (digoxin) prescribing information, Covis Pharma US, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9ec84cac-6ecc-43dc-8006-6ccc029e2707) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

