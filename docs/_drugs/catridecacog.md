---
layout: default
title: Catridecacog
parent: Solo predicción del modelo (L5)
nav_order: 152
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Catridecacog: nueva indicación predicha, Trastorno de liberación primaria de las plaquetas (nivel de evidencia L5). Indicación original: Deficiencia de factor XIII, subunidad A"
---

# Catridecacog
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Catridecacog: De Deficiencia de Factor XIII (subunidad A) a Trastorno de Liberación Primaria Plaquetaria

## Resumen en Una Frase

Catridecacog es el factor XIII de la coagulación recombinante (subunidad A), utilizado originalmente para la deficiencia congénita de la subunidad A del factor XIII.
El modelo TxGNN predice que podría ser efectivo para el **trastorno de liberación primaria de las plaquetas**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Deficiencia de factor XIII, subunidad A |
| Nueva Indicación Predicha | Trastorno de liberación primaria de las plaquetas |
| Puntaje de Predicción TxGNN | 99,29% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Catridecacog es el factor XIII A-subunidad recombinante, una transglutaminasa que entrecruza la fibrina y estabiliza el coágulo. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada; el análisis se basa en el conocimiento general del factor XIII.

Los trastornos de liberación plaquetaria (defectos de secreción de gránulos) alteran la hemostasia primaria. La suplementación con factor XIII actúa más adelante en la cascada, sobre la estabilidad del coágulo, por lo que no corregiría el defecto de secreción plaquetaria en sí. El vínculo es plausible solo como un efecto adyuvante indirecto sobre la firmeza del coágulo.

El puntaje elevado de TxGNN (99,29%) es únicamente una predicción computacional, probablemente reflejo de la cercanía en el grafo entre trastornos hemorrágicos, y no de una justificación mecanística sólida.

### Otras predicciones del modelo (para referencia)

| Posición | Nueva Indicación Predicha | Puntaje TxGNN | Nivel de Evidencia | Comentario |
|------|------|------|------|------|
| 2 | Enfermedad de pseudo-von Willebrand | 99,29% | L5 | El defecto está en la interacción plaqueta-VWF (GPIbα con ganancia de función); el factor XIII no lo corrige. Solo un beneficio teórico sobre la estabilidad de la fibrina. |
| 3 | Trombastenia de Glanzmann | 99,15% | L5 | El defecto es del receptor integrina αIIbβ3; los tratamientos establecidos (transfusión de plaquetas, factor VIIa recombinante) actúan sobre el defecto primario. |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 12775001 | NOVOTHIRTEEN 2500 UI polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable | Deficiencia congénita de factor XIII, subunidad A (según la indicación original del fármaco; el texto de la autorización no está disponible) |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (L5), sin ensayos ni literatura, y el mecanismo del factor XIII no aborda el defecto primario de estos trastornos plaquetarios; además, falta la información de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), requisito previo para cualquier evaluación de seguridad
- Completar los datos del mecanismo de acción (MOA) desde DrugBank
- Revisión sistemática de literatura y de registros de ensayos que respalden el uso en trastornos de función plaquetaria
- Datos preclínicos o de mecanismo que demuestren un beneficio sobre la estabilidad del coágulo en estos trastornos
- Evaluar la compatibilidad de vía de administración y la similitud con la indicación original
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

