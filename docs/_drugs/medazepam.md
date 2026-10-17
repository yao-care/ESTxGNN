---
layout: default
title: Medazepam
parent: Solo predicción del modelo (L5)
nav_order: 498
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Medazepam: nueva indicación predicha, Insomnio (nivel de evidencia L5). Indicación original: No disponible en los datos de la autorización (el texto de indicación…"
monitor_inn: "medazepam"
predicted_indications: ["insomnia (disease)", "alcohol withdrawal delirium", "hallucinogen abuse", "antidepressant type abuse", "barbiturate abuse", "anxiety"]
---

# Medazepam
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

# Medazepam: De Indicación No Registrada en la Ficha a Insomnio

## Resumen en Una Frase

Medazepam es una benzodiazepina (profármaco de diazepam y N-desmetildiazepam) comercializada en España en cápsulas duras, aunque los datos compilados no recogen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **insomnio**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta indicación concreta; se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de la autorización (el texto de indicación está vacío) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Medazepam es una benzodiazepina que se metaboliza a diazepam y N-desmetildiazepam. Como otras de su clase, actúa como modulador alostérico positivo del receptor GABA-A, potenciando la inhibición del sistema nervioso central. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente del fármaco, por lo que esta descripción se basa en el conocimiento general de la clase.

Los efectos sedantes-hipnóticos de las benzodiazepinas hacen mecanísticamente plausible un papel en el insomnio. Sin embargo, no hay ensayos ni literatura específicos de medazepam para esta indicación, y el puntaje del modelo es solo una predicción computacional.

Es importante señalar que otras indicaciones predichas con puntajes similares (por ejemplo, delirium por abstinencia alcohólica, abuso de alucinógenos, de antidepresivos y de barbitúricos) también carecen de evidencia clínica. Varias de ellas parecen reflejar similitud en la estructura de la red más que una señal biológica específica. La ansiedad, por su parte, es más bien un uso consistente con la clase del fármaco que un reposicionamiento genuino.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para insomnio.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para insomnio.

*Nota:* para otras indicaciones predichas sí se recuperó literatura, pero no para la indicación principal. La más relevante es ansiedad (rango 6), con estudios como un ensayo doble ciego cruzado de medazepam frente a amobarbital ([PMID 4923930](https://pubmed.ncbi.nlm.nih.gov/4923930/), 1971, superior en aliviar síntomas de ansiedad neurótica) y un estudio comparativo en niños y adolescentes ([PMID 4592708](https://pubmed.ncbi.nlm.nih.gov/4592708/), 1973). Para barbitúricos (rango 5) solo existen estudios animales de los años 70-80 sobre potencial de abuso. Ninguno corresponde a insomnio.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 48887 | NOBRITOL 12,5 MG/5 MG CÁPSULAS DURAS | Cápsula dura | No disponible |
| 48888 | NOBRITOL FORTE 25 MG/10 MG CÁPSULAS DURAS | Cápsula dura | No disponible |

Ambas autorizaciones están vigentes y pertenecen a Kern Pharma S.L.

---

## Consideraciones de Seguridad

No hay advertencias, contraindicaciones ni interacciones farmacológicas disponibles en los datos compilados. Consultar el prospecto para información de seguridad.

Como referencia, la literatura recuperada para otras indicaciones menciona señales que conviene revisar: lesión renal aguda con la combinación medazepam-butilbromuro de hioscina (caso clínico, [PMID 24664310](https://pubmed.ncbi.nlm.nih.gov/24664310/)), autointoxicación en embarazo ([PMID 18818182](https://pubmed.ncbi.nlm.nih.gov/18818182/)), efectos sobre la capacidad de conducción ([PMID 9967](https://pubmed.ncbi.nlm.nih.gov/9967/)) y potencial de abuso de benzodiazepinas en modelos animales ([PMID 6119723](https://pubmed.ncbi.nlm.nih.gov/6119723/)). Además, sus metabolitos activos de eliminación lenta lo hacen potencialmente de acción prolongada ([PMID 6144464](https://pubmed.ncbi.nlm.nih.gov/6144464/)).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para insomnio se apoya únicamente en el modelo (L5), sin ensayos ni literatura específicos. Además, faltan datos de indicación aprobada y de seguridad de la ficha técnica, lo que impide avanzar en el cribado de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto/ficha técnica de la AEMPS (indicaciones, advertencias y contraindicaciones)
- Obtener datos del mecanismo de acción desde DrugBank
- Revisar la literatura específica de medazepam en insomnio (ensayos clínicos y estudios observacionales)
- Evaluar el riesgo de dependencia, sedación residual y metabolitos de acción prolongada frente a las alternativas hipnóticas disponibles
- Conciliar la indicación original con el etiquetado vigente en España
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

