---
layout: default
title: Orlistat
parent: Solo predicción del modelo (L5)
nav_order: 397
evidence_level: L5
indication_count: 1
---

# Orlistat
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Orlistat: De Obesidad a Hipervitaminosis

## Resumen en Una Frase

Orlistat es un inhibidor de las lipasas gastrointestinales, comercializado en España en productos como Xenical y Alli, y conocido por su uso en el control del peso.
El modelo TxGNN predice que podría ser efectivo para **hipervitaminosis**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata solo de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Obesidad (según conocimiento general del fármaco; los textos de indicación de las autorizaciones AEMPS recibidas están vacíos) |
| Nueva Indicación Predicha | Hipervitaminosis |
| Puntaje de Predicción TxGNN | 99.42% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Por conocimiento farmacológico general, orlistat inhibe las lipasas gástrica y pancreática y reduce la absorción de grasa de la dieta en aproximadamente un 30%. Este razonamiento no proviene de los datos suministrados.

Esa menor absorción de grasa reduce también la absorción de las vitaminas liposolubles (A, D, E y K), un efecto adverso conocido del fármaco. De ahí surge una hipótesis biológicamente plausible pero puramente teórica: limitar la absorción de vitaminas liposolubles podría ser útil en el exceso de vitamina A o D. No aplicaría al exceso de vitaminas hidrosolubles.

Conviene interpretar el resultado con cautela. El puntaje alto (0.994) es solo una predicción del modelo y no constituye evidencia clínica. El término "hipervitaminosis" es poco específico, y el efecto sobre las vitaminas liposolubles se describe hoy como un riesgo del fármaco (déficit), no como un beneficio terapéutico.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 07401009 | ALLI 60 MG CAPSULAS DURAS | Cápsula dura | No disponible en los datos recibidos |
| 78962 | ORLISTAT SANDOZ 120 MG CAPSULAS DURAS | Cápsula dura | No disponible en los datos recibidos |
| 98071003IP9 | XENICAL 120 MG CAPSULAS DURAS | Cápsula dura | No disponible en los datos recibidos |
| 81233 | ORLISTAT TEVA 120 MG CAPSULAS DURAS | Cápsula dura | No disponible en los datos recibidos |
| 07401012 | ALLI 27 mg COMPRIMIDOS MASTICABLES | Comprimido masticable | No disponible en los datos recibidos |

Se muestran 5 de las 20 autorizaciones.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en los datos recibidos.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo TxGNN (nivel L5), sin ensayos clínicos ni literatura. Además, el mecanismo conocido (menor absorción de vitaminas liposolubles) es hoy un efecto adverso y no un beneficio terapéutico demostrado.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de AEMPS (advertencias y contraindicaciones), ya que sin ello no se puede iniciar el cribado de seguridad
- Obtener datos del mecanismo de acción desde DrugBank
- Precisar qué tipo de hipervitaminosis se plantea (A, D, otras)
- Hacer una búsqueda de literatura y ensayos clínicos específica para orlistat e hipervitaminosis
- Confirmar la indicación original en los textos de indicación de las autorizaciones AEMPS
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

