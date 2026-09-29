---
layout: default
title: Bezlotoxumab
parent: Solo predicción del modelo (L5)
nav_order: 74
evidence_level: L5
indication_count: 10
---

# Bezlotoxumab
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

# Bezlotoxumab: De Prevención de Recurrencia de Infección por C. difficile a Peritonitis Pélvica Aguda Femenina

## Resumen en Una Frase

Bezlotoxumab es un anticuerpo monoclonal humano que neutraliza la toxina B de *Clostridioides difficile*, utilizado para reducir la recurrencia de la infección por *C. difficile* (ICD).
El modelo TxGNN predice que podría ser efectivo para **peritonitis pélvica aguda femenina**,
pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Reducción de la recurrencia de la infección por *C. difficile* (según el mecanismo conocido del fármaco; el registro de AEMPS no incluye el texto de indicación) |
| Nueva Indicación Predicha | Peritonitis pélvica aguda femenina (acute female pelvic peritonitis) |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información conocida, bezlotoxumab es un anticuerpo monoclonal humano que se une a la toxina B de *C. difficile* y la neutraliza, y su uso se ha establecido para reducir la recurrencia de ICD.

La peritonitis pélvica aguda femenina suele ser polimicrobiana y no está mediada por la toxina B. No se identifica un vínculo mecanístico plausible entre el fármaco y esta enfermedad.

El puntaje alto de TxGNN (0.999) proviene solo de la proximidad en el grafo de conocimiento, sin respaldo de ensayos ni literatura. Debe interpretarse como una señal débil, probablemente un artefacto del modelo.

## Otras Predicciones del Modelo

Las otras nueve predicciones principales tampoco tienen evidencia (todas nivel L5, decisión Hold) ni un vínculo mecanístico plausible con la toxina B:

| Rango | Enfermedad Predicha | Puntaje TxGNN |
|------|------|------|
| 2 | Quiste embrionario de la trompa de Falopio | 99.89% |
| 3 | Embarazo tubárico | 99.89% |
| 4 | Salpingitis ístmica nodosa | 99.88% |
| 5 | Enfermedad del ligamento ancho uterino | 99.87% |
| 6 | Estenosis del canal lumbar | 99.87% |
| 7 | Linfangioma quístico abdominal | 99.87% |
| 8 | Síndrome de compresión del tronco celíaco | 99.87% |
| 9 | Embarazo ectópico abdominal | 99.87% |
| 10 | Varices pélvicas | 99.87% |

Varias comparten puntajes casi idénticos, lo que sugiere un artefacto de los embeddings del grafo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1161156001 | ZINPLAVA 25 MG/ML CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Concentrado para solución para perfusión | No disponible en el registro |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas. Además, la seguridad de un anticuerpo monoclonal en el embarazo no está establecida, lo que es relevante para varias de las indicaciones predichas (p. ej., embarazo tubárico y ectópico).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos, literatura ni mecanismo plausible. La toxina B de *C. difficile* no participa en la fisiopatología de la peritonitis pélvica aguda.

**Para avanzar se necesita:**
- Una hipótesis mecanística que justifique un papel de la toxina B en la enfermedad predicha
- Evidencia preclínica o clínica que respalde la indicación
- Datos de seguridad y contraindicaciones del prospecto de AEMPS
- Datos detallados del mecanismo de acción (MOA) desde DrugBank
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

