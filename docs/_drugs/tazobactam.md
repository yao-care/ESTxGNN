---
layout: default
title: Tazobactam
parent: Evidencia alta (L1-L2)
nav_order: 767
evidence_level: L1
indication_count: 2
---

# Tazobactam
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **2** 
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

# Tazobactam: De Neumonía Bacteriana a Neumonía (Nosocomial y Asociada a Ventilación)

## Resumen en Una Frase

Tazobactam es un inhibidor de betalactamasas que se administra siempre en combinación con un betalactámico (piperacilina o ceftolozano), y se utilizaba originalmente para tratar neumonía bacteriana, peritonitis, apendicitis e infecciones por estafilococos.
El modelo TxGNN predice que podría ser efectivo para **neumonía**, con **20 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.
Cabe señalar que esta predicción es en gran medida un uso ya existente o muy cercano a las indicaciones originales, y que la evidencia se refiere a combinaciones fijas, no a tazobactam en solitario.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Neumonía bacteriana (según las indicaciones originales del grafo de conocimiento; los textos de indicación de las autorizaciones españolas están vacíos) |
| Nueva Indicación Predicha | Neumonía |
| Puntaje de Predicción TxGNN | 99.46% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, tazobactam es un inhibidor de betalactamasas que forma parte de combinaciones con piperacilina y ceftolozano. Su eficacia en infecciones como la neumonía bacteriana, la peritonitis y las infecciones estafilocócicas está establecida, y mecanísticamente es aplicable a la neumonía.

Tazobactam restaura la actividad de los betalactámicos asociados frente a bacilos gramnegativos productores de betalactamasas, que son causas frecuentes de neumonía nosocomial y de neumonía asociada a ventilación mecánica. Por sí solo, tazobactam no tiene actividad antibacteriana relevante.

La neumonía predicha coincide con la indicación original de neumonía bacteriana, por lo que se trata más de un uso ya existente o muy próximo que de un reposicionamiento genuino. Muchos de los ensayos usan piperacilina/tazobactam como comparador, de modo que respaldan la eficacia de los regímenes con tazobactam, pero no un nuevo uso de tazobactam como agente independiente.

## Evidencia de Ensayos Clínicos

Se muestran los 10 ensayos más relevantes de los 20 registrados.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02070757](https://clinicaltrials.gov/study/NCT02070757) | Fase 3 | Completado | 726 | Ceftolozano/tazobactam frente a meropenem en neumonía nosocomial ventilada (ASPECT-NP); objetivo principal de no inferioridad en mortalidad por todas las causas a día 28 |
| [NCT02493764](https://clinicaltrials.gov/study/NCT02493764) | Fase 3 | Completado | 537 | Imipenem/relebactam frente a piperacilina/tazobactam en neumonía nosocomial o asociada a ventilación; ECA doble ciego |
| [NCT00253955](https://clinicaltrials.gov/study/NCT00253955) | Fase 3 | Completado | 460 | Levofloxacino 750 mg frente a piperacilina/tazobactam 4 g/500 mg en neumonía nosocomial leve a moderada; no inferioridad |
| [NCT00438269](https://clinicaltrials.gov/study/NCT00438269) | Fase 2 | Completado | 80 | Piloto aleatorizado sobre tratamiento antimicrobiano apropiado en cuidados críticos |
| [NCT04223752](https://clinicaltrials.gov/study/NCT04223752) | Fase 1 | Completado | 41 | Seguridad, tolerabilidad y farmacocinética de ceftolozano/tazobactam en niños con neumonía nosocomial |
| [NCT02387372](https://clinicaltrials.gov/study/NCT02387372) | Fase 1 | Completado | 37 | Farmacocinética y penetración pulmonar de ceftolozano/tazobactam en pacientes críticos |
| [NCT06972537](https://clinicaltrials.gov/study/NCT06972537) | N/A | En reclutamiento | 42 | Dosificación guiada por modelo frente a empírica de piperacilina/tazobactam en neumonía de ancianos; sin resultados aún |
| [NCT06977347](https://clinicaltrials.gov/study/NCT06977347) | N/A | Aún sin reclutar | 100 | Piperacilina/tazobactam en monoterapia frente a combinación con fluoroquinolona en neumonía comunitaria grave |
| [NCT07004049](https://clinicaltrials.gov/study/NCT07004049) | Fase 4 | En reclutamiento | 600 | Plataforma adaptativa (TREAT-GNB) para infecciones graves por gramnegativos multirresistentes |
| [NCT01853982](https://clinicaltrials.gov/study/NCT01853982) | Fase 3 | Terminado | 4 | Ceftolozano/tazobactam frente a piperacilina/tazobactam en neumonía asociada a ventilador; terminado con solo 4 participantes, sin datos útiles |

## Evidencia de Literatura

Se muestran las 10 publicaciones más relevantes de las 20 disponibles.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31563344](https://pubmed.ncbi.nlm.nih.gov/31563344/) | 2019 | ECA | Lancet Infect Dis | ASPECT-NP: ceftolozano/tazobactam frente a meropenem en neumonía nosocomial por gramnegativos, ensayo de no inferioridad de fase 3 |
| [32785589](https://pubmed.ncbi.nlm.nih.gov/32785589/) | 2021 | ECA | Clin Infect Dis | RESTORE-IMI 2: imipenem/cilastatina/relebactam frente a piperacilina/tazobactam en neumonía nosocomial o asociada a ventilación |
| [39674398](https://pubmed.ncbi.nlm.nih.gov/39674398/) | 2025 | ECA | Int J Infect Dis | Ensayo de fase III de no inferioridad de imipenem/relebactam frente a piperacilina/tazobactam en neumonía nosocomial o asociada a ventilación |
| [38971203](https://pubmed.ncbi.nlm.nih.gov/38971203/) | 2024 | Revisión sistemática | Int J Antimicrob Agents | Farmacocinética y farmacodinamia de nuevos betalactámicos en neumonía por gramnegativos resistentes a carbapenémicos |
| [38823453](https://pubmed.ncbi.nlm.nih.gov/38823453/) | 2024 | Revisión sistemática y metaanálisis en red | Clin Microbiol Infect | Pautas antibióticas empíricas en neumonía nosocomial no asociada a ventilador |
| [36543346](https://pubmed.ncbi.nlm.nih.gov/36543346/) | 2022 | Revisión | Eur Respir Rev | Nuevos antibióticos para la neumonía por gramnegativos |
| [35088403](https://pubmed.ncbi.nlm.nih.gov/35088403/) | 2022 | Revisión | Semin Respir Crit Care Med | Nuevos antibióticos para neumonía nosocomial y asociada a ventilador |
| [32600375](https://pubmed.ncbi.nlm.nih.gov/32600375/) | 2020 | Revisión | Crit Care | Actualización del tratamiento de la neumonía nosocomial en UCI |
| [38902935](https://pubmed.ncbi.nlm.nih.gov/38902935/) | 2025 | Cohorte | Clin Infect Dis | Resistencia a ceftazidima-avibactam y ceftolozano-tazobactam en bacteriemia o neumonía por *P. aeruginosa* multirresistente (40% vs 10%) |
| [35699444](https://pubmed.ncbi.nlm.nih.gov/35699444/) | 2022 | Estudio observacional | Antimicrob Agents Chemother | Relación entre exposición a betalactámicos (incluida piperacilina-tazobactam) y resultados en neumonía nosocomial en UCI |

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones vigentes (todas de medicamentos con un solo principio activo; ninguna cancelada). El texto de indicación aprobada no figura en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 67902 | Piperacilina/Tazobactam Accord 2/0,25 g | Polvo y disolvente para solución para perfusión | No disponible |
| 67903 | Piperacilina/Tazobactam Accord 4/0,5 g | Polvo para solución para perfusión | No disponible |
| 71824 | Piperacilina/Tazobactam Aurovitas 4 g/0,5 g | Polvo para solución para perfusión | No disponible |
| 86582 | Piperacilina/Tazobactam Stada 4 g/0,5 g | Polvo para solución para perfusión | No disponible |
| 78656 | Piperacilina/Tazobactam Normon 2 g/0,25 g | Polvo para solución inyectable y para perfusión | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones y enfermedades de riesgo según el grafo de conocimiento (no proceden del prospecto):** enfermedad renal, piouréter, neutropenia, agranulocitosis, trastornos de la coagulación, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal, mononucleosis infecciosa y síndrome de infección crónica por virus de Epstein-Barr.

No se encontraron interacciones farmacológicas en la consulta realizada. Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen varios ECA de fase 3 completados en neumonía nosocomial y asociada a ventilador con regímenes que contienen tazobactam o con piperacilina/tazobactam como comparador, y el fármaco ya está ampliamente comercializado en España. Sin embargo, la predicción coincide en gran medida con la indicación original y la evidencia corresponde a combinaciones fijas, por lo que no constituye un reposicionamiento propiamente dicho.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS para obtener advertencias y contraindicaciones oficiales, así como las indicaciones aprobadas de cada autorización
- Completar los datos del mecanismo de acción (MOA) desde DrugBank
- Aclarar qué parte de la evidencia corresponde a piperacilina/tazobactam como tratamiento y qué parte como comparador
- Plan de seguridad para poblaciones de riesgo (insuficiencia renal, neutropenia, trastornos de coagulación, antecedentes de colitis por *C. difficile*)
- Verificar con el contexto de resistencias local la idoneidad del régimen, ya que los estudios en infecciones por BLEE muestran resultados mixtos

---

### Segunda indicación predicha (referencia): infección del tracto urinario

El modelo también predice **infección del tracto urinario** (puntaje 99.12%, nivel de evidencia L1, decisión Proceed with Guardrails), respaldada por 5 ensayos clínicos y 20 publicaciones. Entre ellos destacan el ensayo de fase 3 [NCT03687255](https://clinicaltrials.gov/study/NCT03687255) (n=1043, cefepima-enmetazobactam frente a piperacilina/tazobactam) y el estudio de fase 3 japonés [NCT02728089](https://clinicaltrials.gov/study/NCT02728089) (n=115, ceftolozano/tazobactam). El ensayo [NCT03891433](https://clinicaltrials.gov/study/NCT03891433) (piperacilina/tazobactam frente a carbapenémicos en ITU por BLEE) está suspendido. En ITU por BLEE la evidencia es mixta y los carbapenémicos suelen preferirse en enfermedad grave.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

