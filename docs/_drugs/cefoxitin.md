---
layout: default
title: Cefoxitin
parent: Solo predicción del modelo (L5)
nav_order: 156
evidence_level: L5
indication_count: 9
monitor_inn: "cefoxitin"
predicted_indications: ["infectious otitis media", "urinary tract infection (disease)", "chronic otitis media", "suppurative otitis media", "middle ear disease", "Ureaplasma urethritis", "toxocariasis", "otosalpingitis", "non-suppurative otitis media"]
last_modified_at: 2026-10-27
description: "Cefoxitin: nueva indicación predicha, otitis media infecciosa (infectious otitis media) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Cefoxitin
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

## Cefoxitina: cefamicina de segunda generación (inhibidor de la síntesis de la pared celular bacteriana) → otitis media infecciosa (infectious otitis media)
{: .text-alpha }

## Resumen en Una Frase

Cefoxitina es un antibiótico cefamicina de uso intravenoso, comercializado en España.
El modelo TxGNN predice que podría ser efectivo para **otitis media infecciosa (infectious otitis media)**,
pero actualmente no hay ensayos clínicos y solo hay **1 publicación** general (una revisión sobre MRSA) vinculada a esta predicción, sin datos clínicos específicos de cefoxitina.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | otitis media infecciosa (infectious otitis media) |
| Puntaje de Predicción TxGNN | 0,9930 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 3 de 4) |
| Número de Autorizaciones | 4 (vigentes: 3) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Cefoxitina es una cefamicina de segunda generación que inhibe la síntesis de la pared celular bacteriana y es estable frente a muchas beta-lactamasas. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción, por lo que esta explicación se basa en el conocimiento general de la clase.

Mecanísticamente, su actividad sobre patógenos como *Staphylococcus aureus* y bacterias anaerobias hace plausible un efecto en la otitis media de origen bacteriano. Sin embargo, el único artículo recuperado es una revisión general sobre MRSA (perspectiva "One Health") que menciona la otitis media solo como una de las enfermedades que causa este patógeno; no estudia cefoxitina como tratamiento.

Además, cefoxitina se utiliza principalmente como marcador fenotípico para detectar MRSA, no como terapia en otitis media. Por ello, la razonabilidad de la predicción es solo teórica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33061472](https://pubmed.ncbi.nlm.nih.gov/33061472/) | 2020 | Revisión | Infection and Drug Resistance | Revisión general sobre epidemiología, factores de virulencia y resistencia de MRSA; cita la otitis media como una de las infecciones que produce, sin datos clínicos de cefoxitina |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 68149 | Cefoxitina IPS 1 g | Polvo y disolvente para solución inyectable | No registrada en los datos locales |
| 84251 | Cefoxitina LDP Laboratorios Torlan 1 g | Polvo para solución inyectable | No registrada en los datos locales |
| 84252 | Cefoxitina LDP Laboratorios Torlan 2 g | Polvo para solución inyectable | No registrada en los datos locales |
| 63814 | Cefoxitina Normon 1 g | Polvo y disolvente para solución inyectable | No registrada en los datos locales |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 35 interacciones en total. Las de nivel moderado incluyen kanamicina, neomicina, estreptomicina, ácido picosulfúrico y dicumarol. Heparina figura como interacción menor. Otras (p. ej., vancomicina, metronidazol, omeprazol, morfina) tienen nivel no clasificado.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos ni estudios que evalúen directamente cefoxitina en otitis media; la única publicación es una revisión general sobre MRSA. Por ello, el nivel de evidencia es L5 y la predicción se apoya únicamente en el modelo y en un razonamiento mecanístico general.

**Para avanzar se necesita:**
- Estudios clínicos o de eficacia que evalúen cefoxitina específicamente en otitis media
- Datos de sensibilidad de los patógenos habituales de la otitis media a cefoxitina
- Datos detallados del mecanismo de acción
- Advertencias y contraindicaciones del prospecto de las autorizaciones españolas
- Evaluación de la compatibilidad de la vía de administración (actualmente solo formas inyectables)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

