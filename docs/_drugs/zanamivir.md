---
layout: default
title: Zanamivir
parent: Solo predicción del modelo (L5)
nav_order: 570
evidence_level: L5
indication_count: 2
---

# Zanamivir
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Zanamivir: De Influenza a Pielonefritis

## Resumen en Una Frase

Zanamivir es un inhibidor de la neuraminidasa viral, utilizado originalmente para tratar la gripe (influenza).
El modelo TxGNN predice que podría ser efectivo para **pielonefritis**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Influenza (el texto de indicación no figura en las autorizaciones registradas) |
| Nueva Indicación Predicha | Pielonefritis |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, zanamivir inhibe la neuraminidasa (sialidasa) del virus de la influenza, y su eficacia en esta infección viral está establecida.

Con la información disponible, **no se identifica un vínculo mecanístico plausible** con la pielonefritis. Esta es una infección principalmente bacteriana de las vías urinarias altas, y zanamivir no tiene actividad antibacteriana conocida de relevancia clínica. Existen sialidasas bacterianas, pero no hay evidencia de que zanamivir las inhiba ni de que eso sirva para el tratamiento.

El puntaje muy alto (99.84%) proviene de un grafo de conocimiento y no equivale a evidencia biológica o clínica. Debe interpretarse con cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 1181349001 | DECTOVA 10 mg/ml solución para perfusión | Solución para perfusión | Glaxosmithkline Trading Services Limited |
| 62712 | RELENZA 5 mg/dosis polvo para inhalación (unidosis) | Polvo para inhalación | Glaxosmithkline S.A. |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5), sin ensayos ni literatura para pielonefritis y sin un mecanismo plausible. No hay base para avanzar en esta indicación en este momento.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de la AEMPS (advertencias y contraindicaciones), una brecha bloqueante para el cribado de seguridad.
- Completar los datos de mecanismo de acción desde DrugBank.
- Buscar evidencia preclínica que demuestre actividad de zanamivir frente a patógenos de pielonefritis, o algún mecanismo que la explique.
- Evaluar la compatibilidad de vías de administración (hay presentaciones inhalada e intravenosa) si aparece evidencia de eficacia.

**Nota sobre la segunda predicción:** el modelo también predice "trastorno del metabolismo de la tirosina" (99.02%). Las 3 publicaciones asociadas tratan sobre resistencia de la neuraminidasa de la influenza y métodos de ensayo, no sobre metabolismo de la tirosina. No respaldan esa predicción, que también queda en **Hold** con nivel L5.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

