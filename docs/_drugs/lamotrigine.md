---
layout: default
title: Lamotrigine
parent: Solo predicción del modelo (L5)
nav_order: 447
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-31
monitor_inn: "Lamotrigine"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia"]
description: "Lamotrigine: nueva indicación predicha, Neoplasia del nervio trigémino (trigeminal nerve neoplasm) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Lamotrigine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Lamotrigine: Neoplasia del nervio trigémino (trigeminal nerve neoplasm)
{: .text-alpha }

## Resumen en Una Frase

La lamotrigina es un antiepiléptico de uso establecido, indicado originalmente en epilepsia (parcial, síndrome de Lennox-Gastaut y otras formas).
El modelo TxGNN predice que podría ser efectiva para **neoplasia del nervio trigémino**, pero no hay **ningún ensayo clínico** y solo **2 publicaciones**, ambas sobre neuralgia del trigémino y no sobre tumores. La predicción carece por ahora de respaldo directo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Neoplasia del nervio trigémino (trigeminal nerve neoplasm) |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 19) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos estructurados detallados sobre el mecanismo de acción. Según la información conocida, la lamotrigina bloquea los canales de sodio dependientes de voltaje y reduce la liberación de glutamato. Este mecanismo estabiliza las membranas neuronales hiperexcitables y explica su eficacia en epilepsia.

La puntuación tan alta (0.9997) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica; probablemente se debe a su parecido con la **neuralgia del trigémino**, una enfermedad distinta de un tumor. Los dos artículos recuperados tratan sobre neuralgia del trigémino (una revisión general de tratamientos y un caso de radiocirugía Gamma Knife por malformación cavernosa), no sobre una neoplasia.

Mecanísticamente, el bloqueo de canales de sodio podría aliviar el dolor facial neuropático asociado a un tumor del trigémino. Eso no equivale a un efecto antitumoral, y la evidencia recuperada no lo respalda.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Revisión | Expert Review of Neurotherapeutics | Revisión de los múltiples tratamientos médicos y quirúrgicos de la neuralgia del trigémino. No aborda neoplasias |
| [30650431](https://pubmed.ncbi.nlm.nih.gov/30650431/) | 2018 | Reporte de caso | Stereotactic and Functional Neurosurgery | Radiocirugía Gamma Knife en neuralgia del trigémino causada por una malformación cavernosa. No es un tumor ni un estudio con lamotrigina |

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones vigentes (todas de principio activo único). Los datos de autorización no incluyen texto de indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 67151 | Lamotrigina Sandoz 100 mg EFG | Comprimido masticable y dispersable |
| 67318 | Lamotrigina Normon 25 mg EFG | Comprimido masticable y dispersable |
| 64391 | Lamictal 2 mg | Comprimido masticable y dispersable |
| 67320 | Lamotrigina Normon 100 mg EFG | Comprimido masticable y dispersable |
| 68645 | Lamotrigina Combix 200 mg EFG | Comprimido masticable y dispersable |

## Consideraciones de Seguridad

- **Contraindicaciones o alertas del grafo de conocimiento** (no proceden del texto del prospecto): trastorno de ansiedad, trastorno neurótico, trastorno distímico, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, neutropenia, agranulocitosis, anemia (incluida la macrocítica), pancitopenia, anemia aplásica (incluida la idiopática) y meningitis no infecciosa.

Consultar el prospecto para las advertencias y contraindicaciones oficiales.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo computacional (L5): no hay ensayos clínicos y la literatura recuperada trata sobre neuralgia del trigémino, no sobre neoplasia. Además, el efecto plausible (alivio del dolor neuropático) no es antitumoral.

**Para avanzar se necesita:**
- Evidencia preclínica o clínica de actividad antitumoral de la lamotrigina en tumores del nervio trigémino.
- Datos detallados del mecanismo de acción y del texto oficial de seguridad (prospecto de la AEMPS).
- Aclarar si el objetivo real es el control del dolor neuropático asociado a tumores y no el tratamiento del tumor.

**Nota para reorientar la hipótesis:** la segunda predicción del modelo, la **neuralgia del trigémino** (puntaje 0,9989), tiene un respaldo bastante mayor (nivel L2). Incluye dos ensayos pequeños completados: [NCT00913107](https://clinicaltrials.gov/study/NCT00913107) (Fase 2/3, n=21, frente a carbamazepina) y [NCT00203229](https://clinicaltrials.gov/study/NCT00203229) (controlado con placebo, n=20), además de guías y revisiones que citan la lamotrigina como opción adicional o alternativa. Esta indicación merece una evaluación independiente.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

