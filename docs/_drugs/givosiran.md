---
layout: default
title: Givosiran
parent: Solo predicción del modelo (L5)
nav_order: 258
evidence_level: L5
indication_count: 10
---

# Givosiran
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

# Givosirán: De Porfiria Hepática Aguda a Síndrome Hepatopulmonar

## Resumen en Una Frase

Givosirán es un ARN interferente pequeño (siRNA) que se utiliza en la porfiria hepática aguda, una indicación que se deduce de la literatura y del mecanismo del Evidence Pack, porque el registro español no incluye el texto de indicación.
El modelo TxGNN predice que podría ser efectivo para **síndrome hepatopulmonar**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.
Es una predicción puramente computacional, sin base mecanística plausible.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Porfiria hepática aguda (deducida de la literatura del Evidence Pack; el registro no incluye texto de indicación) |
| Nueva Indicación Predicha | Síndrome hepatopulmonar |
| Puntaje de Predicción TxGNN | 99.9986% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según el Evidence Pack, la respuesta es que **no es razonable con los datos actuales**. Givosirán es un siRNA conjugado con GalNAc que se dirige al hígado y silencia la enzima ALAS1. Con ello reduce los intermediarios de la vía del hemo, el ácido aminolevulínico (ALA) y el porfobilinógeno (PBG), responsables de los ataques neuroviscerales de la porfiria hepática aguda.

El síndrome hepatopulmonar, en cambio, se debe a una vasodilatación intrapulmonar en el contexto de una enfermedad hepática. No existe un vínculo conocido entre la supresión de ALAS1 y este proceso vascular pulmonar. Que ambas enfermedades tengan un componente hepático no basta para sostener una hipótesis mecanística.

Además, el mismo puntaje (99.9986%) aparece en otras cuatro enfermedades hepatovasculares o hepáticas no relacionadas: hipertensión portal familiar no cirrótica de inicio temprano, esclerosis hepatoportal, trombosis portal primitiva y cirrosis idiopática asociada al cobre. Esto sugiere un artefacto de vecindad en el grafo del modelo, más que una señal específica de la enfermedad.

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
| 1201428001 | GIVLAARI 189 MG/ML SOLUCIÓN INYECTABLE | Solución inyectable | Alnylam Netherlands B.V. |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Solo se dispone de la consulta de interacciones farmacológicas, que no arrojó resultados (0 interacciones registradas).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5), sin ensayos ni literatura, y carece de vínculo mecanístico con el síndrome hepatopulmonar. El puntaje idéntico en varias enfermedades hepáticas apunta a un artefacto del grafo.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS con advertencias y contraindicaciones (dato bloqueante para el cribado de seguridad).
- Completar los datos del mecanismo de acción desde DrugBank.
- Aportar una hipótesis mecanística que conecte la supresión de ALAS1 con la vasodilatación intrapulmonar, o evidencia preclínica.

**Observación adicional:** entre las 10 predicciones del paquete, la única con literatura es la porfiria por deficiencia de ALA deshidratasa (nivel L4, "Research Question"). Tiene una base mecanística sólida, pero la evidencia específica se limita a un reporte de caso sin respuesta a givosirán (PMID 35991568). Podría ser una línea de investigación más prometedora que el síndrome hepatopulmonar.

*Este informe es solo para referencia de investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

