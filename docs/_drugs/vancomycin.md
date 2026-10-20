---
layout: default
title: Vancomycin
parent: Solo predicción del modelo (L5)
nav_order: 839
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Vancomycin: nueva indicación predicha, Esclerodermia difusa (nivel de evidencia L5). Indicación original: Colitis por Clostridium difficile (según el grafo de conocimiento"
monitor_inn: "Vancomycin"
predicted_indications: ["diffuse scleroderma", "paratyphoid fever", "salmonellosis", "congenital analbuminemia", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "typhoid fever", "blood group incompatibility", "streptococcal pneumonia", "premalignant hematological system disease"]
---

# Vancomycin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Vancomicina: De Colitis por Clostridium difficile a Esclerodermia Difusa

## Resumen en Una Frase

Vancomicina es un antibiótico glucopéptido, originalmente utilizado para tratar la colitis por *Clostridium difficile*, infecciones estafilocócicas, endocarditis y artritis bacteriana.
El modelo TxGNN predice que podría ser efectivo para **esclerodermia difusa**, pero **no hay ensayos clínicos** y solo **1 publicación** (un reporte de caso sin relación directa con el tratamiento de la esclerodermia) acompaña esta predicción.
La evidencia es únicamente computacional y la predicción carece de plausibilidad mecanística.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Colitis por *Clostridium difficile* (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Esclerodermia difusa |
| Puntaje de Predicción TxGNN | 99,92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 10 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la vancomicina es un antibiótico glucopéptido que inhibe la síntesis de la pared celular de bacterias grampositivas, y su eficacia en infecciones por grampositivos y colitis por *C. difficile* está bien establecida.

Sin embargo, **la predicción no resulta razonable desde el punto de vista biológico**. La esclerodermia difusa (esclerosis sistémica) es una enfermedad autoinmune y fibrótica, sin un componente bacteriano que la vancomicina pueda tratar. El análisis de los datos indica que no existe un vínculo mecanístico plausible y que el puntaje alto de TxGNN parece ser un artefacto del grafo de conocimiento.

La única publicación recuperada describe un caso de eritrodermia con sepsis y eosinofilia, que no aborda el tratamiento de la esclerodermia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Reporte de caso | The American Journal of Case Reports | Caso de erupción exfoliativa difusa con sepsis y eosinofilia en un varón de 56 años (posible eritrodermia); no trata la esclerodermia |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 73785 | Vancomicina Pfizer 1000 mg | Polvo para concentrado para solución para perfusión | No disponible |
| 90304 | Vangozyr 250 mg cápsulas duras | Cápsula dura | No disponible |
| 73784 | Vancomicina Pfizer 500 mg | Polvo para concentrado para solución para perfusión | No disponible |
| 85651 | Vancomicina Normon 1000 mg | Polvo para concentrado para solución para perfusión | No disponible |
| 67283 | Vancomicina Sala 1.000 mg | Polvo para solución inyectable | No disponible |

Se muestran 5 de las 10 autorizaciones vigentes, todas de principio activo único.

---

## Consideraciones de Seguridad

- **Contraindicaciones / condiciones de riesgo (según el grafo de conocimiento, no el prospecto)**: enfermedad renal, piouréter, neutropenia, agranulocitosis, trastornos de la audición y enfermedades del sistema auditivo.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones; entre las principales:
  - **Mayores**: inmunoglobulina G humana (intravenosa), inmunoglobulina humana antineurotoxina botulínica A/B y vacuna viva de *Vibrio cholerae* (cepa CVD 103-HgR).
  - **Moderadas**: AINE (ketorolaco, ibuprofeno, diclofenaco, celecoxib), anfotericina B (incluido el complejo lipídico), aminoglucósidos y polipéptidos (amikacina, capreomicina, bacitracina), carboplatino, metformina, estrógenos (etinilestradiol, estradiol), mesalazina, balsalazida, ibandronato y colestiramina.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura relevante, y no existe un mecanismo biológico plausible que vincule un antibiótico antibacteriano con la fibrosis autoinmune de la esclerodermia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y de advertencias y contraindicaciones del prospecto de la AEMPS.
- Evidencia preclínica o clínica que justifique un vínculo entre vancomicina y la esclerodermia (actualmente inexistente).
- Revisar otras indicaciones predichas con mayor plausibilidad biológica, como la **neumonía estreptocócica** (nivel L4, actividad frente a grampositivos). Aun así, podría tratarse más de una extensión de uso existente que de un reposicionamiento genuino. Las predicciones para salmonelosis, fiebre tifoidea y paratifoidea carecen de fundamento, ya que son bacterias gramnegativas intrínsecamente resistentes a la vancomicina.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

