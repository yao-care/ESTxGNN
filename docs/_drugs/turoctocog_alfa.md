---
layout: default
title: Turoctocog Alfa
parent: Solo predicción del modelo (L5)
nav_order: 832
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Turoctocog Alfa: nueva indicación predicha, Trastorno de liberación primaria de las plaquetas (nivel de evidencia L5). Indicación original: Hemofilia (según el grafo de conocimiento"
monitor_inn: "TUROCTOCOG ALFA"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "Scott syndrome", "acquired coagulation factor deficiency", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "flood factor deficiency", "thrombotic thrombocytopenic purpura", "hereditary thrombocytosis with transverse limb defect"]
---

# Turoctocog Alfa
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

## Turoctocog Alfa: De Hemofilia a Trastorno de Liberación Primaria de las Plaquetas
{: .text-alpha }

## Resumen en Una Frase

Turoctocog alfa es un factor VIII de coagulación humano recombinante (con dominio B truncado), utilizado originalmente para el tratamiento de la hemofilia.
El modelo TxGNN predice que podría ser efectivo para el **trastorno de liberación primaria de las plaquetas**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hemofilia (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Trastorno de liberación primaria de las plaquetas |
| Puntaje de Predicción TxGNN | 99,99 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Turoctocog alfa es un factor VIII recombinante con el dominio B truncado. Su función es reponer el factor VIII deficiente en la hemofilia. No se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe.

Los trastornos de liberación plaquetaria son defectos de la secreción de gránulos de las plaquetas, no una deficiencia de factor VIII. Un papel de apoyo del factor VIII solo es concebible en la amplificación secundaria de la coagulación, algo meramente especulativo. La relación entre la indicación original y la nueva se limita probablemente al fenotipo hemorrágico compartido.

La puntuación alta de TxGNN es solo una predicción del modelo, sin respaldo de ensayos ni literatura. La plausibilidad mecanística es débil y debe considerarse una hipótesis por verificar.

### Otras indicaciones predichas

| Rango | Indicación | Puntaje TxGNN | Comentario |
|------|------|------|------|
| 2 | Pseudo-enfermedad de von Willebrand | 99,99 % | Vínculo plausible pero indirecto (el VWF transporta y estabiliza al FVIII); no corrige el defecto del receptor GPIbα |
| 3 | Trombastenia de Glanzmann | 99,99 % | El FVIII no corrige el defecto de la integrina αIIbβ3; el manejo estándar es transfusión de plaquetas y FVIIa recombinante |
| 4 | Síndrome de Scott | 99,95 % | Conexión teórica vía complejo tenasa, pero el FVIII no restituye la superficie de membrana ausente |
| 5 | Déficit adquirido de factores de coagulación | 99,95 % | La más plausible mecanísticamente (p. ej., hemofilia A adquirida), pero los inhibidores autoinmunes neutralizan el FVIII; suelen preferirse agentes puenteantes. Clasificada como pregunta de investigación |
| 6 | Diátesis hemorrágica por defecto del receptor de colágeno | 99,91 % | Problema primario de función plaquetaria; sin respaldo |
| 7 | Trastorno hemorrágico por trombocitopenia constitucional | 99,91 % | El FVIII no trata la causa subyacente |
| 8 | "Flood factor deficiency" | 99,61 % | Nombre no identificable; posible artefacto de la ontología, debe verificarse |
| 9 | Púrpura trombótica trombocitopénica | 99,54 % | Preocupación de seguridad: un producto procoagulante podría agravar la trombosis |
| 10 | Trombocitosis hereditaria con defecto transverso de miembros | 99,52 % | Sin fundamento biológico identificado |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 113888001 | NOVOEIGHT 250 UI | Polvo y disolvente para solución inyectable | No disponible en los datos compilados |
| 113888002 | NOVOEIGHT 500 UI | Polvo y disolvente para solución inyectable | No disponible en los datos compilados |
| 113888003 | NOVOEIGHT 1000 UI | Polvo y disolvente para solución inyectable | No disponible en los datos compilados |
| 113888004 | NOVOEIGHT 1500 UI | Polvo y disolvente para solución inyectable | No disponible en los datos compilados |
| 113888005 | NOVOEIGHT 2000 UI | Polvo y disolvente para solución inyectable | No disponible en los datos compilados |

Existe además una sexta autorización (113888006, NOVOEIGHT 3000 UI). Las seis son monofármaco, vigentes y de Novo Nordisk A/S.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como observación derivada del análisis mecanístico: para la púrpura trombótica trombocitopénica (rango 9), un producto procoagulante podría agravar la trombosis, por lo que esa indicación no debería perseguirse sin evidencia sólida.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Todas las indicaciones predichas se sustentan únicamente en la puntuación del modelo (nivel L5), sin ensayos ni literatura, y la plausibilidad mecanística de la principal (trastorno de liberación plaquetaria) es débil, ya que el FVIII no corrige defectos primarios de función plaquetaria.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), actualmente sin datos
- Completar los datos del mecanismo de acción
- Realizar una búsqueda sistemática de literatura y ensayos para cada indicación predicha
- Priorizar la investigación del déficit adquirido de factores de coagulación (hemofilia A adquirida), la más plausible, considerando el problema de los inhibidores
- Verificar en la ontología la entrada "flood factor deficiency"
- Evaluar la compatibilidad de vía de administración y el riesgo trombótico antes de cualquier avance
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

