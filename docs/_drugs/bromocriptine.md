---
layout: default
title: Bromocriptine
parent: Solo predicción del modelo (L5)
nav_order: 84
evidence_level: L5
indication_count: 10
---

# Bromocriptine
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

# Bromocriptina: De Hiperprolactinemia y Enfermedad de Parkinson a Trastorno Congénito de la Glicosilación con Defecto de Fucosilación

## Resumen en Una Frase

Bromocriptina es un agonista dopaminérgico D2 que se usa en enfermedad de Parkinson, tumores hipofisarios, hiperprolactinemia y acromegalia. Los datos de la AEMPS recibidos no incluyen el texto de la indicación aprobada, así que esta información procede de los datos de farmacología.
El modelo TxGNN predice que podría ser efectivo para **trastorno congénito de la glicosilación con defecto de fucosilación**, pero **no hay ningún ensayo clínico ni publicación** que respalde esta predicción. Es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hiperprolactinemia, enfermedad de Parkinson, tumores hipofisarios y acromegalia (según datos de farmacología; la AEMPS no aporta texto de indicación) |
| Nueva Indicación Predicha | Trastorno congénito de la glicosilación con defecto de fucosilación |
| Puntaje de Predicción TxGNN | 99.83% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Los datos de farmacología muestran que bromocriptina actúa sobre receptores dopaminérgicos (D1 a D5), varios receptores serotoninérgicos (5-HT1A, 1B, 1D, 2A, 2B, 2C, 6, 7) y receptores adrenérgicos α2 (A, B y C). Su acción terapéutica principal es como agonista D2.

**No se identificó un vínculo mecanístico plausible.** Un agonista dopaminérgico D2 no tiene un papel conocido en la fucosilación ni en el metabolismo del GDP-fucosa, que es la vía afectada en este trastorno. Además, en los datos recibidos la indicación original no tiene una relación clara con esta enfermedad metabólica rara.

El puntaje alto (99.83%) proviene únicamente de la estructura del grafo de conocimiento del modelo. No debe interpretarse como evidencia de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 54633 | PARLODEL 2,5 mg COMPRIMIDOS | Comprimido | No disponible en los datos recibidos |
| 56200 | PARLODEL 5 mg CÁPSULAS | Cápsula dura | No disponible en los datos recibidos |

Ambos productos pertenecen al titular Exeltis Healthcare S.L.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Los 16 registros de "interacciones" recibidos corresponden a dianas farmacológicas (receptores 5-HT, α2-adrenérgicos y dopaminérgicos), no a interacciones con otros medicamentos.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5): no hay ensayos ni literatura, y no existe un vínculo mecanístico plausible entre un agonista D2 y el defecto de fucosilación.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicación aprobada), que está pendiente.
- Completar los datos del mecanismo de acción desde DrugBank.
- Proponer una hipótesis mecanística sobre la vía de fucosilación antes de plantear estudios preclínicos.
- Si se busca una línea con más soporte, evaluar otras predicciones del mismo fármaco. La de **esquizofrenia** (rango 9, nivel L4) tiene 3 ensayos registrados, pero orientados al manejo de comorbilidades (prediabetes e hiperprolactinemia inducida por antipsicóticos), no a tratar la psicosis. Además, un reporte de caso sugiere riesgo de exacerbación psicótica.
- Verificar si bromocriptina forma parte de la combinación del estudio preclínico PMID 39009597 (retinopatías), que hoy no está confirmado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

