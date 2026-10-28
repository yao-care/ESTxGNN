---
layout: default
title: Bentazepam
parent: Solo predicción del modelo (L5)
nav_order: 96
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-28
description: "Bentazepam: nueva indicación predicha, Insomnio (nivel de evidencia L5). Indicación original: No disponible en la ficha de autorización (la literatura la describe…"
monitor_inn: "BENTAZEPAM"
predicted_indications: ["insomnia (disease)", "alcohol withdrawal delirium", "hallucinogen abuse", "barbiturate abuse", "antidepressant type abuse", "anxiety", "sleep disorder, initiating and maintaining sleep"]
---

# Bentazepam
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

## Bentazepam: De Trastornos de Ansiedad a Insomnio
{: .text-alpha }

## Resumen en Una Frase

Bentazepam es una benzodiazepina que actualmente no está comercializada en España (solo constan autorizaciones canceladas).
El modelo TxGNN predice que podría ser efectivo para **insomnio**, con un puntaje muy alto pero **sin ensayos clínicos ni publicaciones** específicas para esta indicación.
La única indicación predicha con algo de literatura es la **ansiedad** (3 publicaciones, ninguna es un ensayo de eficacia controlado).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en la ficha de autorización (la literatura la describe como trastornos de ansiedad) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 0,9995 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado (registros anulados: 1 de 1) |
| Número de Autorizaciones | 1 (vigentes: 0) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Bentazepam es una benzodiazepina. Actualmente no se dispone de datos detallados sobre su mecanismo de acción en los datos compilados para este informe. Según la información conocida, la clase benzodiazepínica actúa mediante modulación alostérica positiva del receptor GABA-A, un mecanismo reconocido para la sedación y la inducción del sueño.

La ansiedad y el insomnio son trastornos frecuentemente comórbidos, y las benzodiazepinas se utilizan en ambos. Por ello, el puntaje alto del modelo es coherente con el efecto de clase. Sin embargo, se trata únicamente de una predicción: no hay estudios específicos de bentazepam para insomnio.

**Otras indicaciones predichas (todas con nivel L5 y decisión Hold, salvo ansiedad):**

| Indicación Predicha | Puntaje TxGNN | Nivel | Comentario |
|------|------|------|------|
| Delirium por abstinencia de alcohol | 0,9969 | L5 | Racional de clase (GABA-A). Cuadro de alta gravedad; sin datos y con hepatotoxicidad descrita, no debería usarse sin evidencia. |
| Abuso de alucinógenos | 0,9948 | L5 | Vínculo indirecto (sedación de agitación/ansiedad); la puntuación proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. |
| Abuso de barbitúricos | 0,9948 | L5 | Racional de clase (sustitución supervisada); riesgo de dependencia. |
| Abuso de antidepresivos | 0,9948 | L5 | Sin racional farmacológico claro. |
| Ansiedad | 0,9937 | L4 | Única con literatura; pregunta de investigación. |
| Trastorno del sueño (inicio y mantenimiento) | 0,9907 | L5 | Muy relacionado con insomnio; solo predicción. |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para insomnio.

## Evidencia de Literatura

No hay literatura disponible para insomnio. Para la indicación de **ansiedad** (rango 6) existen las siguientes publicaciones sobre bentazepam:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [1983365](https://pubmed.ncbi.nlm.nih.gov/1983365/) | 1990 | Cohorte (farmacovigilancia) | Rev Med Univ Navarra | Estudio en 1046 pacientes psiquiátricos ambulatorios; detecta efectos adversos con incidencia >5% (sequedad de boca, somnolencia, astenia, molestias gástricas, estreñimiento, náuseas). La coprescripción más frecuente fue con antidepresivos. |
| [10961721](https://pubmed.ncbi.nlm.nih.gov/10961721/) | 2000 | Reporte de caso | Dig Dis Sci | Tres pacientes con aumento persistente de transaminasas tras semanas de tratamiento; se resolvió al retirar el fármaco. Señal de hepatotoxicidad. |
| [2893777](https://pubmed.ncbi.nlm.nih.gov/2893777/) | 1987 | Simulación farmacocinética | Int J Clin Pharmacol Ther Toxicol | Simulación de niveles plasmáticos con 25 mg cada 8, 12 y 24 h durante 5 días (modelo monocompartimental). |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 55464 | TIADIPONA (Mylan Ire Healthcare Limited) | Comprimido | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Hepatotoxicidad (literatura):** se han descrito casos de lesión hepática crónica con elevación persistente de transaminasas asociada a bentazepam, reversible tras la retirada.
- **Efectos adversos frecuentes (farmacovigilancia):** sequedad de boca, somnolencia, astenia, gastralgia/dispepsia, estreñimiento y náuseas.
- **Interacciones farmacológicas:** no se encontraron interacciones registradas en la consulta realizada.

No se dispone de advertencias ni contraindicaciones del prospecto; consultar el prospecto de AEMPS para la información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para insomnio se basa solo en el modelo (L5), sin ensayos ni literatura específica, y existe una señal de hepatotoxicidad documentada. La ansiedad, con evidencia L4, es la única indicación que podría plantearse como pregunta de investigación.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), necesario antes del cribado de seguridad.
- Obtener datos del mecanismo de acción desde DrugBank.
- Revisión de literatura y ensayos específicos de bentazepam en insomnio.
- Evaluar el riesgo hepático y de dependencia frente a otras benzodiazepinas ya establecidas para insomnio.
- Confirmar la indicación aprobada de la autorización 55464 y la compatibilidad de vía y forma farmacéutica (actualmente solo comprimido).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

