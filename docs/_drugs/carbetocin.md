---
layout: default
title: Carbetocin
parent: Solo predicción del modelo (L5)
nav_order: 145
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Carbetocin: nueva indicación predicha, Síndrome similar a la isotretinoína (nivel de evidencia L5). Indicación original: Síndrome de Prader-Willi / síndrome de Noonan (según el grafo de cono…"
monitor_inn: "carbetocin"
predicted_indications: ["isotretinoin-like syndrome", "Goodman syndrome"]
---

# Carbetocin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Carbetocina: De Síndrome de Prader-Willi a Síndrome Similar a la Isotretinoína

## Resumen en Una Frase

Carbetocina es un agonista del receptor de oxitocina, originalmente asociado en el grafo de conocimiento a indicaciones como el síndrome de Prader-Willi y el síndrome de Noonan; en España está autorizada como inyectable.
El modelo TxGNN predice que podría ser efectiva para el **síndrome similar a la isotretinoína**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Síndrome de Prader-Willi / síndrome de Noonan (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Síndrome similar a la isotretinoína |
| Puntaje de Predicción TxGNN | 99.15% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la carbetocina es un agonista del receptor de oxitocina (OXTR), utilizado para prevenir la hemorragia posparto por atonía uterina. Además, una formulación intranasal (LV-101) ha sido desarrollada para el síndrome de Prader-Willi, con el fin de reducir el hambre extrema asociada a la hiperfagia.

Las indicaciones originales (Prader-Willi y Noonan) son síndromes del desarrollo de base genética. Es probable que el modelo esté relacionando el fármaco con el síndrome similar a la isotretinoína (un trastorno congénito raro con malformaciones) por proximidad en el grafo entre síndromes genéticos o congénitos, y no por una vía biológica demostrada.

Los datos aportados no respaldan ninguna vía biológica que conecte la agonización del receptor de oxitocina con esta enfermedad. El vínculo mecanístico, por tanto, **no está verificado**. Cabe señalar también que la segunda predicción del modelo (síndrome de Goodman, puntaje 99.06%) presenta las mismas limitaciones: sin ensayos, sin literatura y con un vínculo basado solo en cercanía en el grafo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 79228 | Carbetocina GP-Pharm 100 microgramos solución inyectable en jeringa precargada (Gp Pharm S.A.) | Solución inyectable en jeringa precargada | No disponible en los datos compilados |
| 68550 | Duratobal 100 microgramos/ml solución inyectable (Ferring S.A.U.) | Solución inyectable | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta se completó con un único registro de naturaleza farmacológica (no una interacción con otro fármaco): la carbetocina actúa sobre el receptor de oxitocina (OXTR) humano. No se identificaron interacciones con otros medicamentos.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto en TxGNN, pero es solo una predicción del modelo (nivel L5), sin ensayos clínicos ni literatura, y sin una vía biológica plausible que conecte el receptor de oxitocina con el síndrome similar a la isotretinoína.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de la AEMPS (advertencias y contraindicaciones), imprescindible antes de cualquier cribado de seguridad
- Datos detallados del mecanismo de acción (MOA) del fármaco
- Una hipótesis biológica que relacione la señalización de oxitocina con la fisiopatología de la enfermedad predicha
- Búsqueda de evidencia preclínica o de casos que respalde la asociación
- Evaluación de la compatibilidad de vías de administración (solo disponible por vía inyectable en España)
- Confirmar las indicaciones aprobadas en las autorizaciones españolas
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

