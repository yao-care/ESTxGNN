---
layout: default
title: Trandolapril
parent: Solo predicción del modelo (L5)
nav_order: 812
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Trandolapril: nueva indicación predicha, Hipertensión renovascular maligna (nivel de evidencia L5). Indicación original: Hipertensión arterial (según el grafo de conocimiento"
monitor_inn: "TRANDOLAPRIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "chronic pulmonary heart disease"]
---

# Trandolapril
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Trandolapril: De Hipertensión Arterial a Hipertensión Renovascular Maligna

## Resumen en Una Frase

Trandolapril es un inhibidor de la enzima convertidora de angiotensina (IECA), utilizado originalmente para el tratamiento de la hipertensión arterial.
El modelo TxGNN predice que podría ser efectivo para **hipertensión renovascular maligna**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden directamente esta indicación; la predicción se apoya solo en el modelo y en un razonamiento mecanístico.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Hipertensión renovascular maligna |
| Puntaje de Predicción TxGNN | 99,92% |
| Nivel de Evidencia | L4 (según la clasificación de los datos compilados; sin ensayos ni literatura propios para esta indicación, lo que en rigor corresponde a L5) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, trandolapril pertenece a la clase de los inhibidores de la ECA: bloquea la conversión de angiotensina I en angiotensina II, reduciendo la vasoconstricción y la secreción de aldosterona. Su eficacia en hipertensión arterial está establecida.

La hipertensión renovascular está impulsada en gran medida por la activación del sistema renina-angiotensina, por lo que el bloqueo de este eje es mecanísticamente plausible. La predicción tiene, por tanto, una base biológica razonable.

Sin embargo, el puntaje elevado probablemente refleja la cercanía con la indicación ya aprobada (hipertensión) y no una evidencia independiente. Además, los IECA pueden precipitar insuficiencia renal aguda en la estenosis bilateral de la arteria renal, lo que exige especial cautela en este escenario.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal (hipertensión renovascular maligna).

Para otras indicaciones predichas (por ejemplo, hipertensión pulmonar asociada a enfermedad pulmonar o hipoxia) se identificaron publicaciones preclínicas o indirectas, ninguna en humanos con hipertensión pulmonar. No constituyen respaldo para la indicación principal y se mencionan solo como contexto.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 59984 | GOPTEN 0,5 mg CAPSULAS DURAS | Cápsula dura | No disponible en los datos compilados |
| 59985 | GOPTEN 2 mg CAPSULAS DURAS | Cápsula dura | No disponible en los datos compilados |

Ambas autorizaciones son de monofármaco, están vigentes y pertenecen a Viatris Healthcare Limited.

## Consideraciones de Seguridad

- **Contraindicaciones / condiciones de riesgo según el grafo de conocimiento** (no proceden del texto del prospecto): enfermedad renal, enfermedad hepática, angioedema (incluido el hereditario, el adquirido y el inducido por bloqueadores del sistema renina-angiotensina-aldosterona), neutropenia y agranulocitosis, estenosis aórtica, miocardiopatía hipertrófica, obstrucción de la arteria renal, trastornos hipotensivos, miastenia gravis, taquicardia ventricular, bloqueo auriculoventricular e insuficiencia cardíaca, entre otras.
- **Interacciones farmacológicas**: se registraron 100 interacciones en total. Entre las mostradas, las de nivel **mayor** son con **citrato de potasio** y **bicarbonato de potasio** (riesgo de hiperpotasemia). Hay numerosas interacciones de nivel **moderado**, por ejemplo con corticoides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona), antidiabéticos (metformina, alogliptina, canagliflozina, dapagliflozina, empagliflozina, glimepirida, clorpropamida), ácido acetilsalicílico, morfina, bupropión, dronabinol, ácido picosulfúrico y polietilenglicol con electrolitos.
- Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos ni literatura que respalden la hipertensión renovascular maligna; la predicción se basa solo en el modelo y en la plausibilidad mecanística, con un riesgo renal relevante en este contexto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto oficial de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas).
- Completar los datos del mecanismo de acción.
- Realizar una búsqueda sistemática de ensayos y literatura clínica sobre IECA en hipertensión renovascular maligna.
- Evaluar el riesgo de insuficiencia renal aguda (estenosis bilateral de arteria renal) e hiperpotasemia, con un plan de monitoreo de función renal y potasio.
- Confirmar la compatibilidad de vía y forma farmacéutica con la nueva indicación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

