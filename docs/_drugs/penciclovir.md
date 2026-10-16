---
layout: default
title: Penciclovir
parent: Solo predicción del modelo (L5)
nav_order: 621
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Penciclovir: nueva indicación predicha, Fascioliasis (nivel de evidencia L5). Indicación original: Herpes labial (según el grafo de conocimiento"
monitor_inn: "PENCICLOVIR"
predicted_indications: ["fascioliasis"]
---

# Penciclovir
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

# Penciclovir: De Herpes Labial a Fascioliasis

## Resumen en Una Frase

Penciclovir es un análogo nucleósido de la guanosina, utilizado originalmente en crema para el tratamiento del herpes labial.
El modelo TxGNN predice que podría ser efectivo para **fascioliasis**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Herpes labial (según el grafo de conocimiento; el texto de indicación de la autorización no está disponible) |
| Nueva Indicación Predicha | Fascioliasis |
| Puntaje de Predicción TxGNN | 99,06% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Según la información conocida, penciclovir es un análogo nucleósido de la guanosina que es fosforilado por la timidina cinasa viral y, después, inhibe la ADN polimerasa viral. Por ello, su actividad es específica frente a herpesvirus, y su eficacia en el herpes labial es la base de su uso clínico.

La relación con la fascioliasis es débil. *Fasciola hepatica* y *Fasciola gigantica* son trematodos y no se conoce en ellos una vía de activación dependiente de timidina cinasa viral. Tampoco se ha descrito un mecanismo antiparasitario plausible para penciclovir.

El puntaje alto de TxGNN (0,991) probablemente refleja proximidad en el grafo de conocimiento (por ejemplo, nodos compartidos con fármacos antiparasitarios o análogos de nucleósidos) y no una justificación biológica. La predicción debe considerarse una hipótesis computacional sin respaldo mecanístico demostrado.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 61462 | FENIVIR 10 mg/g CREMA (Perrigo España S.A.) | Crema | No disponible en los datos compilados |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo computacional (nivel L5), sin ensayos clínicos ni literatura, y no existe un mecanismo biológico plausible que vincule un antiviral específico de herpesvirus con un trematodo. Con la información actual no se justifica avanzar.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) del fármaco para evaluar cualquier vínculo mecanístico.
- Evidencia preclínica *in vitro* o *in vivo* de actividad frente a *Fasciola* spp.
- Revisión del prospecto de la AEMPS (advertencias y contraindicaciones) para completar el cribado de seguridad.
- Evaluación de la compatibilidad de la vía de administración: el producto autorizado es una crema de uso tópico, poco adecuada para una infección hepatobiliar sistémica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

