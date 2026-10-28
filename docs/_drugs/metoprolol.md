---
layout: default
title: Metoprolol
parent: Solo predicción del modelo (L5)
nav_order: 518
evidence_level: L5
indication_count: 6
monitor_inn: "METOPROLOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease", "trichotillomania"]
last_modified_at: 2026-10-23
description: "Metoprolol: nueva indicación predicha, Malignant hypertensive renal disease (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Metoprolol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Metoprolol: Malignant hypertensive renal disease
{: .text-alpha }

## Resumen en Una Frase

Metoprolol es un betabloqueante cardioselectivo (beta-1) cuyas relaciones registradas en el grafo de conocimiento incluyen hipertensión, síndrome coronario agudo e infarto de miocardio.
El modelo TxGNN predice que podría ser efectivo para **enfermedad cardíaca pulmonar crónica**, con **5 ensayos clínicos** y **20 publicaciones** recuperadas, pero ninguno estudia directamente esta enfermedad, por lo que la evidencia se clasifica como nivel L5.

*Nota sobre la selección:* la predicción con mayor puntaje (enfermedad renal hipertensiva maligna, 0,9991) no tiene ensayos ni literatura, y es en esencia una manifestación de la hipertensión ya conocida. Se presenta la enfermedad cardíaca pulmonar crónica (5.ª en el ranking) como la única predicción con ensayos clínicos y literatura de apoyo indirecto. Para mantener coherencia con los datos de evidencia, el análisis siguiente se centra en ella.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Malignant hypertensive renal disease |
| Puntaje de Predicción TxGNN | 0.9991 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 3 de 6) |
| Número de Autorizaciones | 6 (vigentes: 3) |
| Decisión Recomendada | Hold |

Nota: la primera predicción de la lista (enfermedad renal hipertensiva maligna) también tiene nivel L5 y decisión Hold.

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento farmacológico general, metoprolol bloquea de forma selectiva los receptores beta-1, lo que reduce la frecuencia cardíaca, el gasto cardíaco y la demanda de oxígeno del miocardio.

La enfermedad cardíaca pulmonar crónica (cor pulmonale) suele derivar de enfermedades pulmonares como la EPOC. La conexión con metoprolol es indirecta: la evidencia recuperada trata sobre el uso de betabloqueantes en pacientes con enfermedad cardiovascular y EPOC, no sobre el cor pulmonale en sí. La cardioselectividad reduce teóricamente el riesgo de broncoespasmo.

Los datos aleatorizados son mixtos: el ensayo BLOCK-COPD (NCT02587351) se terminó antes de tiempo, y metoprolol no redujo las exacerbaciones de EPOC y se asoció con más exacerbaciones que requirieron hospitalización. Por tanto, la plausibilidad mecanística no equivale a eficacia demostrada.

## Evidencia de Ensayos Clínicos

Ninguno de los ensayos estudia directamente la enfermedad cardíaca pulmonar crónica.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06825728](https://clinicaltrials.gov/study/NCT06825728) | Fase 4 | Aún sin reclutar | 311 | Metoprolol en insuficiencia cardíaca con fracción de eyección reducida y EPOC; evalúa mortalidad y rehospitalizaciones. Sin resultados |
| [NCT00384566](https://clinicaltrials.gov/study/NCT00384566) | Fase 4 | Retirado | 0 | Carvedilol vs. metoprolol, evaluación respiratoria en insuficiencia cardíaca. Sin datos |
| [NCT02587351](https://clinicaltrials.gov/study/NCT02587351) | Fase 3 | Terminado | 532 | Betabloqueantes para prevenir exacerbaciones de EPOC (aleatorizado, doble ciego, con placebo). Terminado antes de tiempo; no mostró beneficio |
| [NCT05096884](https://clinicaltrials.gov/study/NCT05096884) | Fase 1 temprana | Terminado | 14 | Disnea y taquicardia tras COVID-19; relación solo tangencial |

## Evidencia de Literatura

Se listan las publicaciones más relevantes de las 20 recuperadas; todas abordan EPOC o insuficiencia cardíaca, no cor pulmonale.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38587241](https://pubmed.ncbi.nlm.nih.gov/38587241/) | 2024 | ECA | N Engl J Med | Betabloqueantes tras infarto con fracción de eyección conservada (contexto cardiovascular) |
| [38762800](https://pubmed.ncbi.nlm.nih.gov/38762800/) | 2024 | ECA | JAMA | Bisoprolol en EPOC con alto riesgo de exacerbación (otro fármaco; menciona que metoprolol no redujo exacerbaciones y aumentó las hospitalizaciones) |
| [33784233](https://pubmed.ncbi.nlm.nih.gov/33784233/) | 2021 | Análisis secundario de ECA | Ann Am Thorac Soc | Índice cronotrópico y exacerbaciones de EPOC en BLOCK-COPD |
| [32000982](https://pubmed.ncbi.nlm.nih.gov/32000982/) | 2020 | Cohorte | Am J Cardiol | Metoprolol vs. carvedilol en pacientes con insuficiencia cardíaca, EPOC, diabetes e insuficiencia renal |
| [26844454](https://pubmed.ncbi.nlm.nih.gov/26844454/) | 2016 | Cohorte | Medicine | Carvedilol, bisoprolol y metoprolol en insuficiencia cardíaca con EPOC (base de datos taiwanesa) |
| [32250198](https://pubmed.ncbi.nlm.nih.gov/32250198/) | 2020 | Revisión | Expert Rev Respir Med | Recomendaciones prácticas para betabloqueantes en EPOC |
| [14520486](https://pubmed.ncbi.nlm.nih.gov/14520486/) | 2003 | Estudio clínico | Heart Vessels | Metoprolol, usado con seguridad en enfermedad coronaria con EPOC (50 pacientes) |
| [6851273](https://pubmed.ncbi.nlm.nih.gov/6851273/) | 1983 | Estudio fisiológico | Clin Cardiol | Efecto de metoprolol sobre la función cardíaca y pulmonar en EPOC (6 pacientes) |

## Información de Mercado en España

Las 6 autorizaciones son de producto de un solo principio activo; los datos compilados no incluyen texto de indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Estado |
|---------|------|------|-----------|
| 82000 | Metoprolol Aurovitas 100 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Vigente |
| 54503 | Lopresor 100 mg comprimidos recubiertos con película | Comprimido recubierto con película | Vigente |
| 56989 | Beloken 1 mg/ml solución inyectable | Solución inyectable | Vigente |
| 61506 | Beloken Retard 95 mg comprimidos de liberación prolongada | Comprimido de liberación prolongada | Cancelada |
| 55748 | Beloken 100 mg comprimidos | Comprimido | Cancelada |

Hay una sexta autorización (81030, Metoprolol Krka Retard 95 mg, cancelada) no mostrada para respetar el límite de cinco filas.

## Consideraciones de Seguridad

- **Contraindicaciones registradas en el grafo de conocimiento** (no provienen del texto del prospecto): trastorno de ansiedad, pancreatitis, enfermedad hepática, lupus eritematoso sistémico, psoriasis, diabetes mellitus, cetoacidosis diabética, gota, hipotensión, miastenia gravis, feocromocitoma y encefalopatía hepática, entre otras.
- **Interacciones farmacológicas** (100 registradas; ejemplos): moderadas con epinefrina, corticoides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona), bupropión, morfina, atropina, cimetidina, canagliflozina, dapagliflozina y clorpropamida; menores con ácido acetilsalicílico y óxido de magnesio.
- **Señal de seguridad pulmonar:** en BLOCK-COPD, metoprolol se asoció con más exacerbaciones de EPOC que requirieron hospitalización. Esto es especialmente relevante para una población con enfermedad pulmonar crónica.

Consultar el prospecto para las advertencias y contraindicaciones oficiales, que no están disponibles en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ningún ensayo ni publicación estudia directamente la enfermedad cardíaca pulmonar crónica, por lo que el nivel de evidencia es L5. La evidencia indirecta en EPOC incluye una señal de seguridad desfavorable en el único ensayo de fase 3 con metoprolol.

**Para avanzar se necesita:**
- Estudios que evalúen directamente metoprolol en cor pulmonale o enfermedad cardíaca pulmonar crónica
- Seguimiento de los resultados del ensayo NCT06825728 (insuficiencia cardíaca con EPOC)
- Datos de mecanismo de acción y texto oficial de seguridad (prospecto de la AEMPS)
- Evaluación de riesgo-beneficio en pacientes con enfermedad pulmonar obstructiva
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

