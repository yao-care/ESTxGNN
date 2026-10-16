---
layout: default
title: Oxybutynin
parent: Solo predicción del modelo (L5)
nav_order: 597
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Oxybutynin: nueva indicación predicha, Síndrome de piernas inquietas (nivel de evidencia L5). Indicación original: Vejiga hiperactiva (según las indicaciones del grafo de conocimiento"
monitor_inn: "Oxybutynin"
predicted_indications: ["restless legs syndrome", "gastroduodenitis", "peptic ulcer disease"]
---

# Oxybutynin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Oxibutinina: De Vejiga Hiperactiva a Síndrome de Piernas Inquietas

## Resumen en Una Frase

Oxibutinina es un fármaco antimuscarínico, originalmente utilizado para el tratamiento de la vejiga hiperactiva y la vejiga neurógena.
El modelo TxGNN predice que podría ser efectivo para **Síndrome de Piernas Inquietas**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Vejiga hiperactiva (según las indicaciones del grafo de conocimiento; los textos de indicación autorizados no están disponibles) |
| Nueva Indicación Predicha | Síndrome de piernas inquietas |
| Puntaje de Predicción TxGNN | 99.74% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Según la información conocida, la oxibutinina es un antagonista de los receptores muscarínicos (los datos farmacológicos compilados la vinculan con los receptores M1 a M5) y su eficacia en la vejiga hiperactiva está establecida. Además, se le atribuye una acción antiespasmódica directa sobre el músculo liso.

Una posible relación es que el desequilibrio colinérgico/dopaminérgico se ha discutido en la fisiopatología del síndrome de piernas inquietas. Sin embargo, este vínculo es especulativo: los anticolinérgicos con actividad central suelen describirse como agravantes o sin beneficio claro en este síndrome. La relación con la indicación original (un trastorno urológico) es débil y no está establecida.

**Otras predicciones del modelo (todas con evidencia limitada):**

| Indicación Predicha | Puntaje TxGNN | Nivel de Evidencia | Comentario |
|------|------|------|------|
| Gastroduodenitis | 99.62% | L5 | Sin ensayos ni literatura; racional teórico antiespasmódico/antisecretor |
| Enfermedad ulcerosa péptica | 99.31% | L4 | Literatura antigua e indirecta, con una señal de seguridad contraria (esofagitis por reflujo) |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para el síndrome de piernas inquietas.

Para la indicación predicha de menor rango (enfermedad ulcerosa péptica), solo existe literatura indirecta y antigua:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [2360335](https://pubmed.ncbi.nlm.nih.gov/2360335/) | 1990 | Reporte de caso | DICP: Annals of Pharmacotherapy | Caso de esofagitis por reflujo inducida por oxibutinina, probablemente por reducción del tono del esfínter esofágico inferior |
| [4380481](https://pubmed.ncbi.nlm.nih.gov/4380481/) | 1965 | Revisión farmacológica/preclínica | Arch Int Pharmacodyn Ther | Caracterización de la oxibutinina como antiespasmódico musculotrópico con acción anticolinérgica moderada |
| [14173506](https://pubmed.ncbi.nlm.nih.gov/14173506/) | 1964 | Evaluación clínica (no controlada) | Curr Ther Res | Evaluación clínica histórica de la oxibutinina en enfermedad gastrointestinal |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 57185 | DITROPAN 5 mg COMPRIMIDOS | Comprimido | No disponible |
| 03270001 | KENTERA 3,9 mg/24 HORAS, PARCHE TRANSDÉRMICO | Parche transdérmico | No disponible |
| 85899 | VESOXX 1 MG/ML SOLUCIÓN INTRAVESICAL | Solución intravesical | No disponible |
| 62205 | DRESPLAN COMPRIMIDOS | Comprimido | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no el texto del prospecto)**: hipertensión, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, hiperplasia prostática benigna, enfermedad coronaria, paro cardíaco súbito, trastornos de la conducción cardíaca, glaucoma de ángulo cerrado, miastenia gravis y enfermedades de la unión neuromuscular, colitis ulcerosa y enfermedad inflamatoria intestinal, hipertiroidismo (enfermedad de Graves, tirotoxicosis), hernia de hiato, íleo paralítico, obstrucción intestinal, obstrucción del cuello vesical, megacolon tóxico, enfermedad por reflujo gastroesofágico y esofagitis.
- **Interacciones Farmacológicas**: la consulta no identificó interacciones con otros fármacos; únicamente se registró la afinidad farmacológica por los receptores muscarínicos M1 a M5.
- **Señal de seguridad relevante**: se ha descrito esofagitis por reflujo asociada a la oxibutinina (1990), lo que es desfavorable para las indicaciones gastrointestinales predichas.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (99.74%), pero no cuenta con ningún ensayo clínico ni publicación (nivel L5). Además, el vínculo mecanístico es especulativo y los anticolinérgicos de acción central no han mostrado beneficio claro en el síndrome de piernas inquietas.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA) y análisis del vínculo mecanístico con el síndrome de piernas inquietas
- Revisión de la literatura sobre anticolinérgicos en este síndrome, incluido el posible empeoramiento de los síntomas
- Obtención de los textos de indicación y del prospecto de la AEMPS (advertencias y contraindicaciones oficiales)
- Evaluación de la compatibilidad de las vías de administración (pendiente)
- Evidencia clínica o preclínica directa antes de reconsiderar la decisión
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

