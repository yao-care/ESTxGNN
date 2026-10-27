---
layout: default
title: Turoctocog Alfa Pegol
parent: Solo predicción del modelo (L5)
nav_order: 833
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Turoctocog Alfa Pegol: nueva indicación predicha, Trastorno de liberación plaquetaria primario (nivel de evidencia L5). Indicación original: Hemofilia (según el grafo de conocimiento"
monitor_inn: "TUROCTOCOG ALFA PEGOL"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "acquired coagulation factor deficiency", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "flood factor deficiency", "hereditary thrombocytosis with transverse limb defect", "fetal and neonatal alloimmune thrombocytopenia"]
---

# Turoctocog Alfa Pegol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Turoctocog alfa pegol: De Hemofilia a Trastorno de Liberación Plaquetaria Primario
{: .text-alpha }

## Resumen en Una Frase

Turoctocog alfa pegol es un factor VIII de coagulación recombinante, truncado en el dominio B y glicoPEGilado, utilizado originalmente para el tratamiento de la hemofilia.
El modelo TxGNN predice que podría ser efectivo para el **trastorno de liberación plaquetaria primario**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hemofilia (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Trastorno de liberación plaquetaria primario |
| Puntaje de Predicción TxGNN | 99,997% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, turoctocog alfa pegol es un factor VIII recombinante, truncado en el dominio B y glicoPEGilado, que repone el factor VIII deficiente en la hemofilia, y su uso en esa indicación está respaldado por su autorización de comercialización en España.

Sin embargo, la nueva indicación predicha es un defecto primario de la función plaquetaria, con niveles normales de factor VIII. La reposición de este factor no tiene una justificación mecanística clara en ese contexto. El puntaje elevado del modelo parece reflejar la proximidad dentro de la red de conocimiento entre trastornos hemorrágicos, y no un vínculo farmacológico validado.

Por tanto, esta predicción debe considerarse una hipótesis sin respaldo mecanístico ni clínico. Otras predicciones de la lista (por ejemplo, la deficiencia adquirida de factores de coagulación) son mecanísticamente más cercanas, pero tampoco cuentan con evidencia aportada y presentan limitaciones importantes, como la presencia de inhibidores autoinmunes.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1191374001 | ESPEROCT 500 UI | Polvo y disolvente para solución inyectable | No disponible en los datos compilados |
| 1191374002 | ESPEROCT 1000 UI | Polvo y disolvente para solución inyectable | No disponible en los datos compilados |
| 1191374003 | ESPEROCT 1500 UI | Polvo y disolvente para solución inyectable | No disponible en los datos compilados |
| 1191374004 | ESPEROCT 2000 UI | Polvo y disolvente para solución inyectable | No disponible en los datos compilados |
| 1191374005 | ESPEROCT 3000 UI | Polvo y disolvente para solución inyectable | No disponible en los datos compilados |

Todas las autorizaciones corresponden a Novo Nordisk A/S, son de principio activo único y se encuentran vigentes.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es de nivel L5 (solo modelo), sin ensayos clínicos ni literatura, y carece de lógica mecanística: el factor VIII no corrige un defecto plaquetario con niveles normales de FVIII. El puntaje alto de TxGNN parece un artefacto de proximidad en el grafo.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA).
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), actualmente no disponible, lo que impide el cribado de seguridad.
- Revisión de la literatura y de registros de ensayos para el trastorno de liberación plaquetaria primario.
- Evaluar si otras indicaciones predichas con mayor plausibilidad (p. ej., deficiencia adquirida de factores de coagulación) merecen priorizarse, teniendo en cuenta el papel de los inhibidores.
- Depurar las etiquetas de enfermedad ambiguas de las predicciones (p. ej., «flood factor deficiency») antes de nuevas evaluaciones.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

