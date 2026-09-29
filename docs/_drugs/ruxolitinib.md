---
layout: default
title: Ruxolitinib
parent: Solo predicción del modelo (L5)
nav_order: 480
evidence_level: L5
indication_count: 10
---

# Ruxolitinib
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

# Ruxolitinib: De Neoplasias Mieloproliferativas a Tumor de Células Epitelioides Perivasculares del Cuerpo Uterino

## Resumen en Una Frase

Ruxolitinib es un inhibidor de JAK1/2 comercializado en España como Jakavi. Los datos de AEMPS proporcionados no incluyen su indicación aprobada; según el conocimiento general de la ficha técnica europea, se usa en neoplasias mieloproliferativas como la mielofibrosis.
El modelo TxGNN predice que podría ser efectivo para **tumor de células epitelioides perivasculares del cuerpo uterino (PEComa uterino)**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción, que se apoya solo en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos de AEMPS proporcionados (ver nota abajo) |
| Nueva Indicación Predicha | Tumor de células epitelioides perivasculares del cuerpo uterino (PEComa uterino) |
| Puntaje de Predicción TxGNN | 99.73% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Hold |

> Nota: los textos de indicación aprobada de las autorizaciones están vacíos. La referencia a neoplasias mieloproliferativas procede del conocimiento general, no del Evidence Pack, y debe verificarse en la ficha técnica de AEMPS.

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, ruxolitinib es un inhibidor de las quinasas JAK1 y JAK2, y su eficacia en enfermedades mieloproliferativas está establecida. Mecanísticamente, su posible aplicación al PEComa uterino sería solo indirecta.

El PEComa se explica sobre todo por la desregulación de la vía mTOR (genes TSC1/TSC2), no por la vía JAK/STAT. La única conexión plausible sería una comunicación cruzada entre JAK/STAT y mTOR, y no se aportó ningún dato que la respalde.

Por eso la predicción debe considerarse una hipótesis del modelo. Se necesitarían estudios preclínicos que muestren actividad de la inhibición de JAK en este tumor antes de darle más peso.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 112773015 | JAKAVI 10 MG COMPRIMIDOS | Comprimido | Novartis Europharm Limited |
| 112773017 | JAKAVI 5 MG/ML SOLUCIÓN ORAL | Solución oral | Novartis Europharm Limited |
| 112773011 | JAKAVI 20 MG COMPRIMIDOS | Comprimido | Novartis Europharm Limited |
| 112773008 | JAKAVI 15 MG COMPRIMIDOS | Comprimido | Novartis Europharm Limited |
| 112773005 | JAKAVI 5 MG COMPRIMIDOS | Comprimido | Novartis Europharm Limited |

Se muestran 5 de las 6 autorizaciones registradas. Se sustituyó la columna de indicación aprobada por el titular porque el texto de indicación está vacío en todos los registros.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para el PEComa uterino tiene un puntaje alto (99.73%), pero es solo una predicción del modelo (L5), sin ensayos ni publicaciones. El mecanismo del tumor (mTOR) tampoco se relaciona directamente con la inhibición de JAK1/2.

**Para avanzar se necesita:**
- Datos preclínicos que respalden la actividad de la inhibición de JAK/STAT en PEComa
- Datos del mecanismo de acción (MOA) del fármaco
- Advertencias y contraindicaciones del prospecto de AEMPS, hoy no disponibles y bloqueantes para el cribado de seguridad
- Texto de la indicación aprobada de cada autorización

**Otras predicciones del mismo fármaco:** el modelo también predice **síndrome hemofagocítico asociado a infección** (puntaje 99.32%), con 2 ensayos clínicos y 20 publicaciones. Su nivel de evidencia es L3 y su recomendación, *Proceed with Guardrails*. Tiene mucho más respaldo que el PEComa y sería una mejor candidata para priorizar. Requeriría control del patógeno, vigilancia de citopenias y uso bajo supervisión especializada.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

