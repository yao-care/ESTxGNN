---
layout: default
title: Metoprolol
parent: Solo predicción del modelo (L5)
nav_order: 518
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Metoprolol: nueva indicación predicha, Enfermedad renal hipertensiva maligna (nivel de evidencia L5). Indicación original: Hipertensión arterial (según el grafo de conocimiento"
monitor_inn: "METOPROLOL"
predicted_indications: ["malignant hypertensive renal disease", "malignant renovascular hypertension", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "posteroinferior myocardial infarction", "posterolateral myocardial infarction", "septal myocardial infarction", "chronic pulmonary heart disease", "trichotillomania"]
---

# Metoprolol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Metoprolol: De Hipertensión Arterial a Enfermedad Renal Hipertensiva Maligna

## Resumen en Una Frase

Metoprolol es un betabloqueante cardioselectivo (beta-1), utilizado originalmente para el tratamiento de la hipertensión arterial, el síndrome coronario agudo y el infarto de miocardio.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción concreta; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna |
| Puntaje de Predicción TxGNN | 99,91% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, metoprolol es un bloqueante selectivo de los receptores beta-1 adrenérgicos, cuya eficacia en la hipertensión arterial está comprobada. Al reducir la frecuencia cardíaca, el gasto cardíaco y la liberación de renina, disminuye la presión arterial.

La enfermedad renal hipertensiva maligna es una manifestación grave de daño en órgano diana de la hipertensión, por lo que el vínculo con la indicación original es plausible a través de la reducción de la presión arterial y de la renina. El puntaje elevado del modelo probablemente refleja esta cercanía con las indicaciones hipertensivas originales.

Conviene ser prudentes: el manejo de la hipertensión maligna aguda suele basarse en fármacos intravenosos, y el metoprolol oral no es una terapia estándar en este contexto. Además, no se aportó ningún ensayo ni publicación que sustente la predicción.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

### Otras predicciones evaluadas (contexto)

| Indicación predicha | Puntaje TxGNN | Nivel | Observación |
|------|------|------|------|
| Hipertensión renovascular maligna | 99,91% | L5 | La única publicación recuperada (PMID 1988765) trata sobre cromogranina A en feocromocitoma; es una coincidencia espuria |
| Hipertensión pulmonar de mecanismo multifactorial poco claro | 99,91% | L5 | Los betabloqueantes se evitan o se usan con cautela por el riesgo de disfunción ventricular derecha |
| Hipertensión pulmonar por enfermedad pulmonar o hipoxia | 99,91% | L4 | Solo evidencia indirecta (arritmias en enfermedad pulmonar, estudios animales) |
| Síndrome de Braddock | 99,89% | L5 | Solo predicción |
| Infarto de miocardio posteroinferior, posterolateral y septal | 99,84%–99,80% | L5/L4 | Subtipos del infarto ya cubierto por la indicación original; no son reposicionamiento real |
| Cor pulmonale crónico | 99,40% | L3 | Evidencia más sólida, pero principalmente sobre seguridad en EPOC con enfermedad cardíaca (ver abajo) |
| Tricotilomanía | 99,05% | L5 | Solo predicción, sin vínculo mecanístico claro |

### Candidata con mayor evidencia: cor pulmonale crónico

Ensayos clínicos relevantes:

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06825728](https://clinicaltrials.gov/study/NCT06825728) | Fase 4 | No reclutando aún | 311 | Metoprolol en insuficiencia cardíaca con fracción de eyección reducida y EPOC; compara dosis, evalúa mortalidad y rehospitalizaciones |
| [NCT02587351](https://clinicaltrials.gov/study/NCT02587351) | Fase 3 | Terminado | 532 | Betabloqueante (metoprolol) para prevenir exacerbaciones de EPOC; terminado antes de tiempo, evidencia no concluyente |
| [NCT00384566](https://clinicaltrials.gov/study/NCT00384566) | Fase 4 | Retirado | 0 | Carvedilol vs. metoprolol, efectos respiratorios; sin participantes, sin datos |
| [NCT05096884](https://clinicaltrials.gov/study/NCT05096884) | Fase 1 temprana | Terminado | 14 | Disnea y taquicardia tras COVID-19; relación solo tangencial |

Literatura seleccionada:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38587241](https://pubmed.ncbi.nlm.nih.gov/38587241/) | 2024 | ECA | N Engl J Med | Betabloqueantes tras infarto de miocardio con fracción de eyección preservada |
| [38762800](https://pubmed.ncbi.nlm.nih.gov/38762800/) | 2024 | ECA | JAMA | Bisoprolol en EPOC con alto riesgo de exacerbación (ensayo BICS); menciona que metoprolol no redujo las exacerbaciones y aumentó las que requerían hospitalización |
| [32000982](https://pubmed.ncbi.nlm.nih.gov/32000982/) | 2020 | Cohorte | Am J Cardiol | Metoprolol vs. carvedilol en pacientes geriátricos con insuficiencia cardíaca, EPOC, diabetes e insuficiencia renal |
| [26844454](https://pubmed.ncbi.nlm.nih.gov/26844454/) | 2016 | Cohorte | Medicine | Supervivencia con carvedilol, bisoprolol y metoprolol en insuficiencia cardíaca y EPOC coexistentes (Taiwán) |
| [29159953](https://pubmed.ncbi.nlm.nih.gov/29159953/) | 2018 | Cohorte | Eur J Heart Fail | Uso de betabloqueantes en insuficiencia cardíaca con EPOC (Dinamarca) |
| [33784233](https://pubmed.ncbi.nlm.nih.gov/33784233/) | 2021 | Análisis secundario de ECA | Ann Am Thorac Soc | Índice cronotrópico y exacerbaciones de EPOC en BLOCK COPD |
| [14520486](https://pubmed.ncbi.nlm.nih.gov/14520486/) | 2003 | Estudio clínico | Heart Vessels | Metoprolol, bloqueante beta-1 selectivo, usado con seguridad en enfermedad coronaria con EPOC |
| [32250198](https://pubmed.ncbi.nlm.nih.gov/32250198/) | 2020 | Revisión | Expert Rev Respir Med | Recomendaciones prácticas sobre betabloqueantes en EPOC |
| [15358010](https://pubmed.ncbi.nlm.nih.gov/15358010/) | 2004 | Revisión | J Am Coll Cardiol | Bloqueo adrenérgico en EPOC e insuficiencia cardíaca crónica coexistentes |
| [6851273](https://pubmed.ncbi.nlm.nih.gov/6851273/) | 1983 | Estudio de fisiología clínica | Clin Cardiol | Efecto de metoprolol sobre la función cardíaca y pulmonar en EPOC |

Esta evidencia se refiere sobre todo a la seguridad respiratoria de los betabloqueantes cardioselectivos en EPOC con enfermedad cardiovascular, y no demuestra eficacia frente al cor pulmonale en sí.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 82000 | Metoprolol Aurovitas 100 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos |
| 61506 | Beloken Retard 95 mg comprimidos de liberación prolongada | Comprimido de liberación prolongada | No disponible en los datos |
| 54503 | Lopresor 100 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos |
| 56989 | Beloken 1 mg/ml solución inyectable | Solución inyectable | No disponible en los datos |
| 55748 | Beloken 100 mg comprimidos | Comprimido | No disponible en los datos |

Existe además una sexta autorización vigente: 81030, Metoprolol Krka Retard 95 mg comprimidos de liberación prolongada EFG.

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no el prospecto)**: trastornos de ansiedad, enfermedad hepática, pancreatitis, enfermedad de la vesícula biliar, lupus eritematoso sistémico, psoriasis, diabetes mellitus y cetoacidosis diabética, gota, hipotensión, miastenia gravis y enfermedades de la unión neuromuscular, feocromocitoma, hiperparatiroidismo, hipercalcemia, anuria, encefalopatía hepática, entre otras.
- **Interacciones farmacológicas**: se identificaron 100 interacciones; las muestran principalmente nivel moderado, por ejemplo con epinefrina, corticoides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona), anticolinérgicos (atropina, hiosciamina, glicopirronio), bupropión, morfina, cimetidina, lorcaserina, canagliflozina, dapagliflozina, clorpropamida y sales de calcio. El ácido acetilsalicílico y el óxido de magnesio presentan interacciones de nivel menor.
- **Señal en cor pulmonale/EPOC**: la literatura señala que metoprolol aumentó las exacerbaciones de EPOC con hospitalización en el ensayo BLOCK-COPD, y que los betabloqueantes pueden empeorar la función del ventrículo derecho en hipertensión pulmonar.

Consultar el prospecto para las advertencias y contraindicaciones oficiales.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal (enfermedad renal hipertensiva maligna) no cuenta con ensayos ni literatura, por lo que solo alcanza el nivel L5. Las demás predicciones tienen evidencia indirecta, son subtipos de indicaciones ya aprobadas o presentan señales de seguridad desfavorables; la más desarrollada (cor pulmonale, L3) es una pregunta de investigación sobre seguridad en EPOC más que una prueba de eficacia.

**Para avanzar se necesita:**
- Obtener y revisar los prospectos de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), actualmente ausentes.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una búsqueda dirigida de literatura y ensayos sobre metoprolol en hipertensión maligna con afectación renal.
- Si se prioriza el cor pulmonale/EPOC, esperar los resultados de NCT06825728 y analizar el riesgo de exacerbaciones observado en BLOCK-COPD.
- Definir un plan de monitoreo de seguridad para poblaciones específicas (EPOC, diabetes, enfermedad hepática).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

