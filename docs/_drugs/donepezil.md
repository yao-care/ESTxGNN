---
layout: default
title: Donepezil
parent: Solo predicción del modelo (L5)
nav_order: 260
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-31
monitor_inn: "donepezil"
predicted_indications: ["psychogenic movement disorders", "chronic tic disorder", "primary orthostatic tremor", "extrapyramidal and movement disease", "benign shuddering attacks", "tremor-nystagmus-duodenal ulcer syndrome", "benign paroxysmal tonic upgaze of childhood with ataxia", "lingual-facial-buccal dyskinesia"]
description: "Donepezil: nueva indicación predicha, Psychogenic movement disorders (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Donepezil
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

## Donepezil: Psychogenic movement disorders
{: .text-alpha }

## Resumen en Una Frase

Donepezilo es un inhibidor de la colinesterasa, originalmente utilizado para el tratamiento de la enfermedad de Alzheimer.
El modelo TxGNN predice que podría ser efectivo para **Trastorno de Tics Crónicos** (segunda predicción de mayor puntaje, y la primera con respaldo bibliográfico), sin ensayos clínicos registrados y con **5 publicaciones** de alcance limitado (estudios pequeños, reportes de caso y trabajos preclínicos en ratón).

> Nota: la predicción con mayor puntaje (trastornos del movimiento psicógenos, 0,9923) no cuenta con ensayos clínicos ni literatura, por lo que este informe se centra en la primera indicación con evidencia disponible. En el anexo de la conclusión se resumen las demás predicciones.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Psychogenic movement disorders |
| Puntaje de Predicción TxGNN | 0.9923 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 15) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold (pregunta de investigación; no avanzar a uso clínico sin estudios controlados) |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, donepezilo pertenece a la clase de los inhibidores de la acetilcolinesterasa, su eficacia en la enfermedad de Alzheimer está establecida, y mecanísticamente podría ser aplicable a los tics por su efecto sobre la neurotransmisión colinérgica.

La disfunción colinérgica estriatal se ha propuesto como un factor en los tics y en el trastorno por déficit de atención e hiperactividad (TDAH). La modulación colinérgica de los circuitos del estriado, con interacción con los sistemas dopaminérgico y serotoninérgico, es plausible para los tics. En modelos de ratón, donepezilo redujo la respuesta de sacudida de cabeza inducida por DOI, un modelo propuesto de tics del síndrome de Tourette, y alteró la función serotoninérgica central.

Sin embargo, la evidencia humana se limita a estudios pequeños en su mayoría no controlados. No hay ensayos clínicos registrados ni ensayos aleatorizados confirmados entre los registros disponibles. El vínculo mecanístico es plausible, pero no está demostrado.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [18343255](https://pubmed.ncbi.nlm.nih.gov/18343255/) | 2008 | Estudio clínico abierto, prospectivo (según el título; diseño no verificable por título truncado) | Clinical Therapeutics | Donepezilo en niños y adolescentes con tics y TDAH, con escalada de dosis durante 18 semanas; se plantea que la disfunción colinérgica estriatal podría ser relevante |
| [10440471](https://pubmed.ncbi.nlm.nih.gov/10440471/) | 1999 | Reporte de caso / serie pequeña | Journal of Clinical Psychopharmacology | Uso de donepezilo en trastorno de Tourette y TDAH |
| [16986157](https://pubmed.ncbi.nlm.nih.gov/16986157/) | 2006 | Comentario / Revisión | Movement Disorders | Comentario sobre la posible eficacia de donepezilo en el síndrome de Tourette |
| [16045972](https://pubmed.ncbi.nlm.nih.gov/16045972/) | 2005 | Preclínico (ratón) | Pharmacology, Biochemistry, and Behavior | Efectos de donepezilo, nicotina y haloperidol sobre el sistema serotoninérgico central; relevancia para Tourette |
| [14643839](https://pubmed.ncbi.nlm.nih.gov/14643839/) | 2003 | Preclínico (ratón) | Pharmacology, Biochemistry, and Behavior | Donepezilo atenúa la respuesta de sacudida de cabeza inducida por DOI, modelo de tics |

## Información de Mercado en España

Las 20 autorizaciones son de medicamentos de un solo principio activo, vigentes, sin canceladas. No se dispone del texto de indicación aprobada en los datos compilados. Se listan las 5 principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 74861 | Donepezilo Flas Sandoz 5 mg comprimidos bucodispersables EFG | Comprimido bucodispersable | No disponible |
| 76026 | Donepezilo Kern Pharma 10 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 0612298C | Aricept 10 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 75251 | Donepezilo Ratio 5 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 76110-4-12-2006IP1 | Aricept Flas 10 mg comprimidos bucodispersables | Comprimido bucodispersable | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proviene del prospecto): epilepsia, asma (incluidas las formas intrínseca y alérgica), obstrucción del cuello vesical, enfermedad ulcerosa péptica activa, síndrome del seno enfermo (incluida la forma familiar) y bloqueo auriculoventricular.
- **Interacciones farmacológicas**: se registraron 257 interacciones. Entre las principales:
  - **Mayor**: bupropión.
  - **Moderada**: famotidina, ranitidina, cimetidina, hiosciamina, atropina (incluida la oftálmica), glicopirronio, clidinio, diciclomina, loperamida, dexametasona, metronidazol, dolasetrón, ácido picosulfúrico y polietilenglicol 3350 con electrolitos.
  - **Menor**: aprepitant, ácido acetilsalicílico, lorcaserina y claritromicina.
- **Señal de seguridad específica**: la literatura asociada a la predicción de trastornos del movimiento describe movimientos anormales inducidos por donepezilo (distonía cervical, corea, atetosis, temblor mandibular, síndrome de Pisa), lo que debe valorarse en un uso en trastornos del movimiento o tics.

Consultar el prospecto para el resto de advertencias y precauciones.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque el puntaje del modelo es alto y existe plausibilidad colinérgica, la evidencia humana se limita a un estudio abierto pequeño y reportes de caso, sin ensayos clínicos registrados. Corresponde a una pregunta de investigación, no a una base para uso clínico.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) del fármaco.
- Texto de indicaciones, advertencias y contraindicaciones del prospecto de la AEMPS.
- Un ensayo controlado y aleatorizado (Fase 2) en tics crónicos o síndrome de Tourette, con evaluación de seguridad pediátrica.
- Revisión completa de los estudios, ya que los títulos están truncados y el diseño no pudo verificarse.

**Resumen de las demás predicciones:**

| Indicación predicha | Puntaje TxGNN | Nivel | Observación |
|------|------|------|------|
| Trastornos del movimiento psicógenos | 0,9923 | L5 | Solo predicción; sin racional de inhibición colinesterásica claro. Hold |
| Temblor ortostático primario | 0,9917 | L5 | Solo predicción. Hold |
| Enfermedad extrapiramidal y de movimiento | 0,9916 | L3 | Evidencia mixta: un beneficio reportado en discinesias tardías, pero la revisión sistemática de 2025 señala trastornos del movimiento asociados a inhibidores de la colinesterasa. Pregunta de investigación |
| Ataques de escalofrío benignos | 0,9916 | L5 | Solo predicción; trastorno benigno y autolimitado. Hold |
| Síndrome de temblor-nistagmo-úlcera duodenal | 0,9915 | L5 | El único registro recuperado parece una coincidencia espuria. Hold |
| Mirada tónica hacia arriba paroxística benigna con ataxia | 0,9912 | L5 | Solo predicción; uso pediátrico requeriría amplia justificación. Hold |
| Discinesia linguo-facial-bucal | 0,9902 | L3 | Revisiones Cochrane sobre medicación colinérgica en discinesia tardía, sin establecer eficacia de donepezilo; hay reportes de movimientos anormales inducidos. Balance beneficio-riesgo incierto. Hold |
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

