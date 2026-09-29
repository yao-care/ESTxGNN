---
layout: default
title: Travoprost
parent: Solo predicción del modelo (L5)
nav_order: 542
evidence_level: L5
indication_count: 10
---

# Travoprost
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

# Travoprost: De Glaucoma a Calcifilaxis Visceral

## Resumen en Una Frase

Travoprost es un análogo de prostaglandina de administración tópica ocular, utilizado en el tratamiento del glaucoma y la hipertensión ocular.
El modelo TxGNN predice que podría ser efectivo para **calcifilaxis visceral**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es una predicción basada solo en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Glaucoma e hipertensión ocular (deducido de los ensayos y la literatura recuperados; el texto de indicación de la AEMPS no está disponible) |
| Nueva Indicación Predicha | Calcifilaxis visceral |
| Puntaje de Predicción TxGNN | 99.9998% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 18 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, travoprost es un análogo de prostaglandina de uso oftálmico, con eficacia comprobada para reducir la presión intraocular en glaucoma. Sin datos de MOA no es posible verificar mecanísticamente su aplicabilidad a la calcifilaxis visceral.

Los datos aportados no documentan ningún vínculo mecanístico entre travoprost y la calcifilaxis visceral. El puntaje de TxGNN (0.9999984) proviene únicamente de la predicción del grafo de conocimiento. La calcifilaxis visceral es una enfermedad vascular sistémica, mientras que travoprost se administra como colirio, y no hay evidencia que respalde una justificación vascular sistémica.

Por ello, esta predicción debe considerarse una hipótesis generada por el modelo, sin respaldo clínico o preclínico en los datos recibidos. Además, la compatibilidad de vías de administración entre el uso actual (ocular) y la posible nueva indicación no ha sido evaluada.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Travoprost está comercializado en España con 18 autorizaciones. Se listan las 5 principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 79302 | Travoprost Abamed 40 microgramos/ml colirio en solución | Colirio en solución | Qualix Pharma S.L. |
| 79222 | Travoprost Rafarm 40 microgramos/ml colirio en solución | Colirio en solución | Rafarm S.A. |
| 01199002IP | Travatan 40 microgramos/ml colirio en solución | Colirio en solución | Novartis Europharm Limited |
| 81831 | Vizitrav 40 microgramos/ml colirio en solución | Colirio en solución | Bausch + Lomb Ireland Limited |
| 01199001 | Travatan 40 microgramos/ml colirio en solución | Colirio en solución | Novartis Europharm Limited |

El texto de indicación aprobada no figura en los datos recibidos para ninguna de estas autorizaciones.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para calcifilaxis visceral es solo del modelo (nivel L5), sin ensayos clínicos ni literatura, sin mecanismo documentado y con una vía de administración ocular poco compatible con una enfermedad sistémica. No hay base para avanzar.

**Para avanzar se necesita:**
- Datos de mecanismo de acción (MOA) desde DrugBank
- Advertencias y contraindicaciones del prospecto de la AEMPS
- Evidencia preclínica o clínica que vincule análogos de prostaglandina con la calcifilaxis
- Evaluación de compatibilidad de vía de administración (ocular vs. sistémica)

**Nota sobre otras predicciones:** las otras nueve indicaciones predichas también quedan en Hold. Ocho están en L5 sin evidencia. Hemangioendotelioma está en L4, pero solo con un caso clínico de efecto adverso (derrame uveal con travoprost en un paciente con síndrome de Sturge-Weber) y una revisión general. Ninguna de las dos publicaciones muestra beneficio terapéutico. Para "enfermedad vascular", los 15 ensayos y 20 publicaciones recuperados tratan solo glaucoma e hipertensión ocular, y no aportan evidencia para esa indicación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

