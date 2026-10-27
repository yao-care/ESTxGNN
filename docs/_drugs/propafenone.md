---
layout: default
title: Propafenone
parent: Solo predicción del modelo (L5)
nav_order: 668
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Propafenone: nueva indicación predicha, Trastorno bipolar maníaco (nivel de evidencia L5). Indicación original: Fibrilación auricular y taquicardia ventricular (según las relaciones…"
monitor_inn: "Propafenone"
predicted_indications: ["manic bipolar affective disorder", "periodic paralysis with transient compartment-like syndrome", "Prinzmetal angina", "arrhythmogenic right ventricular cardiomyopathy", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania"]
---

# Propafenone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Propafenona: De Fibrilación Auricular y Taquicardia Ventricular a Trastorno Bipolar Maníaco
{: .text-alpha }

## Resumen en Una Frase

La propafenona es un antiarrítmico utilizado originalmente en el tratamiento de la fibrilación auricular y de la taquicardia ventricular.
El modelo TxGNN predice que podría ser efectiva para el **trastorno bipolar maníaco**, pero **no hay ensayos clínicos** y solo hay **3 publicaciones** (una revisión y dos reportes de caso), que describen **riesgos de seguridad** y no un beneficio terapéutico.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Fibrilación auricular y taquicardia ventricular (según las relaciones fármaco-enfermedad del grafo de conocimiento; los textos de indicación de las autorizaciones españolas no figuran) |
| Nueva Indicación Predicha | Trastorno bipolar maníaco |
| Puntaje de Predicción TxGNN | 99.80% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la propafenona es un antiarrítmico con eficacia comprobada en arritmias auriculares y ventriculares. Los datos compilados la vinculan farmacológicamente con los receptores β1 y β2 adrenérgicos y con el canal de potasio Kv1.5.

**En este caso, la predicción no es razonable desde el punto de vista mecanístico.** No se identifica ningún mecanismo terapéutico plausible que conecte un antiarrítmico cardíaco con el tratamiento de la manía. La literatura recuperada describe a la propafenona como una posible **causa** de manía (reporte de caso de 1985) y como fuente de interacciones medicamentosas (psicosis orgánica por interacción con venlafaxina en 2001; interacciones entre antipsicóticos y fármacos cardiovasculares en 2020).

El puntaje alto del modelo parece reflejar una asociación en la red con efectos adversos psiquiátricos y con la comorbilidad cardiovascular en pacientes bipolares, no una señal de eficacia. Debe interpretarse como una señal de seguridad y no como una oportunidad de reposicionamiento.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32124390](https://pubmed.ncbi.nlm.nih.gov/32124390/) | 2020 | Revisión | Pharmacological Reports | Evalúa interacciones perjudiciales entre antipsicóticos y fármacos cardiovasculares, dada la alta comorbilidad entre trastorno bipolar o esquizofrenia y enfermedad cardiovascular |
| [11949740](https://pubmed.ncbi.nlm.nih.gov/11949740/) | 2001 | Reporte de caso | International Journal of Psychiatry in Medicine | Psicosis orgánica por interacción venlafaxina-propafenona en un paciente con trastorno bipolar |
| [2579063](https://pubmed.ncbi.nlm.nih.gov/2579063/) | 1985 | Reporte de caso | Journal of Clinical Psychiatry | Caso de manía secundaria a propafenona; se plantea como complicación no reconocida previamente |

Ninguna de estas publicaciones demuestra un beneficio de la propafenona en la manía.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 55538 | Rytmonorm 150 mg comprimidos recubiertos | Comprimido recubierto |
| 55541 | Rytmonorm 300 mg comprimidos recubiertos | Comprimido recubierto |
| 58275 | Rytmonorm 3,5 mg/ml solución inyectable | Solución inyectable |
| 82298 | Propafenona hidrocloruro Accord 150 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 82299 | Propafenona hidrocloruro Accord 300 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |

Las 5 autorizaciones están vigentes y son de monofármaco. Los textos de indicación aprobada no figuran en los datos compilados.

## Consideraciones de Seguridad

- **Contraindicaciones o enfermedades de riesgo según el grafo de conocimiento** (no proceden del texto del prospecto):
  - Cardiovasculares: síndrome de QT largo (incluida la forma familiar), torsades de pointes, infarto de miocardio, enfermedad coronaria, aterosclerosis e hipotensión.
  - Metabólicas y orgánicas: hipopotasemia, hepatopatía, enfermedad de la vesícula biliar y nefropatía.
  - Neuromusculares: miastenia gravis.
  - Hematológicas: agranulocitosis y neutropenia, incluidas las formas congénitas.
- **Interacciones y señales de seguridad en este contexto**: la literatura recuperada documenta una posible inducción de manía y una interacción con venlafaxina que causó psicosis orgánica. Esto es especialmente relevante en pacientes con trastorno bipolar.

Para el resto de la información de seguridad, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (L5), sin ensayos clínicos, y la literatura disponible indica que la propafenona puede inducir manía o interactuar con psicofármacos. No hay base para avanzar en esta indicación.

**Para avanzar se necesita:**
- Datos del mecanismo de acción que justifiquen un efecto antimaníaco, algo que hoy no existe.
- Estudios preclínicos que demuestren un efecto terapéutico y no solo una asociación con efectos adversos psiquiátricos.
- Revisión de las advertencias y contraindicaciones del prospecto de la AEMPS.

**Nota para la priorización:** entre las demás indicaciones predichas, la **taquicardia ventricular polimórfica catecolaminérgica** tiene un respaldo claramente mayor. Cuenta con estudios preclínicos sobre el bloqueo del receptor de rianodina RyR2, cohortes observacionales y un reporte de 35 años de tratamiento eficaz con propafenona. Se sitúa en el nivel L3 y se recomienda como "Proceed with Guardrails". Las salvaguardas son descartar cardiopatía estructural, usar un betabloqueante como terapia base y vigilar de cerca el ECG y la anchura del QRS. Conviene evaluarla en un informe específico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

