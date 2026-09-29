---
layout: default
title: Erdafitinib
parent: Solo predicción del modelo (L5)
nav_order: 207
evidence_level: L5
indication_count: 6
---

# Erdafitinib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Erdafitinib: De Inhibidor de Quinasas FGFR a Hipertensión Pulmonar

## Resumen en Una Frase

Erdafitinib es un inhibidor de tirosina quinasas pan-FGFR (FGFR1-4) comercializado en España como Balversa. El modelo TxGNN predice que podría ser efectivo para **hipertensión pulmonar**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección. Se trata solo de una hipótesis basada en la predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Hipertensión pulmonar |
| Puntaje de Predicción TxGNN | 99,38 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Erdafitinib es un inhibidor pan-FGFR (FGFR1-4). No se dispone de datos detallados del mecanismo de acción en DrugBank para este registro, pero su clase farmacológica sí es conocida. La señalización FGF/FGFR, en particular FGF2/FGFR1, se ha relacionado con la proliferación del músculo liso de la arteria pulmonar y con el remodelado vascular. Esto es lo que da una base biológica plausible a la predicción.

Esta base es **solo una hipótesis preclínica**. El puntaje de 99,38 % es una predicción del modelo, no evidencia clínica. Tampoco hay datos sobre la indicación original del fármaco en los registros españoles del paquete de evidencia, por lo que no se puede analizar la similitud con la nueva indicación.

Toxicidades conocidas de la clase, como hiperfosfatemia y efectos oculares y ungueales, tendrían que sopesarse frente a cualquier beneficio potencial en una enfermedad vascular pulmonar.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 1241841009 | BALVERSA 4 MG comprimidos recubiertos con película | Comprimido recubierto con película | Janssen-Cilag International N.V. |
| 1241841004 | BALVERSA 3 MG comprimidos recubiertos con película | Comprimido recubierto con película | Janssen-Cilag International N.V. |
| 1241841011 | BALVERSA 5 MG comprimidos recubiertos con película | Comprimido recubierto con película | Janssen-Cilag International N.V. |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasas FGFR) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Fosfato sérico (hiperfosfatemia), examen ocular, vigilancia de alteraciones ungueales; el resto, según el prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5, etapa S0), sin ensayos ni literatura específica. Además, el perfil de toxicidad conocido exige una evaluación cuidadosa antes de plantear cualquier uso nuevo.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), ya que su ausencia bloquea el cribado de seguridad.
- Completar los datos del mecanismo de acción (consulta a la API de DrugBank).
- Realizar estudios preclínicos que evalúen la inhibición de FGFR en modelos de hipertensión pulmonar.
- Evaluar la relación beneficio-riesgo frente a las toxicidades de clase (hiperfosfatemia, efectos oculares y ungueales).

Otras indicaciones predichas (artritis reumatoide, esclerosis lateral amiotrófica, amenorrea, cardiopatía cifoescoliótica y síndrome de braquidactilia-sindactilia) tienen evidencia igualmente L5. Las que carecen de vínculo mecanístico plausible, o cuyo mecanismo sugiere posible perjuicio, deben mantenerse en espera.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

