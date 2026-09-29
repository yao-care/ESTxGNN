---
layout: default
title: Lorlatinib
parent: Solo predicción del modelo (L5)
nav_order: 331
evidence_level: L5
indication_count: 10
---

# Lorlatinib
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

# Lorlatinib: De Cáncer de Pulmón No Microcítico ALK-positivo a Fibromatosis Gingival

## Resumen en Una Frase

Lorlatinib es un inhibidor de tirosina quinasa de tercera generación, con buena penetración cerebral, que actúa sobre ALK y ROS1. Se usa para tratar el cáncer de pulmón no microcítico (CPNM) ALK-positivo.
El modelo TxGNN predice que podría ser efectivo para **fibromatosis gingival**, pero **no hay ningún ensayo clínico ni publicación** que respalde esta dirección. Es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CPNM ALK-positivo (el texto de indicación de las autorizaciones españolas no está disponible; se toma de la literatura y de la clasificación del farmaco) |
| Nueva Indicación Predicha | Fibromatosis gingival |
| Puntaje de Predicción TxGNN | 99.81% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Lorlatinib bloquea las quinasas ALK y ROS1, dos proteínas que impulsan el crecimiento de ciertos tumores cuando presentan reordenamientos genéticos. Por eso funciona en el CPNM con alteraciones de ALK o ROS1. No se dispone de datos detallados de mecanismo de acción en DrugBank para este informe.

En este caso **no se ha establecido un vínculo mecanístico**. La fibromatosis gingival es un crecimiento fibroso benigno de las encías, y no hay documentación de que ALK o ROS1 participen en su origen. La indicación original es un cáncer maligno dependiente de un oncogén concreto, mientras que la nueva indicación es un trastorno benigno sin esa dependencia.

El puntaje alto (99.81%) refleja patrones del grafo de conocimiento del modelo, no evidencia biológica ni clínica. Por sí solo no justifica avanzar.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 1191355001 | LORVIQUA 25 MG comprimidos recubiertos con película | Comprimido recubierto con película |
| 1191355002 | LORVIQUA 100 MG comprimidos recubiertos con película | Comprimido recubierto con película |

Titular: Pfizer Europe MA EEIG.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa ALK/ROS1) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5), sin ensayos ni publicaciones, y no hay un vínculo mecanístico plausible entre la inhibición de ALK/ROS1 y la fibromatosis gingival. Además, se trata de una enfermedad benigna, por lo que el balance riesgo-beneficio de un antineoplásico sería desfavorable sin evidencia previa.

**Para avanzar se necesita:**
- Evidencia biológica de que ALK/ROS1 u otra diana de lorlatinib participa en la fibromatosis gingival (estudios preclínicos o de tejido)
- Datos de mecanismo de acción desde DrugBank
- Advertencias y contraindicaciones del prospecto de la AEMPS, un requisito previo para cualquier evaluación de seguridad
- Texto de las indicaciones aprobadas en las autorizaciones españolas

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

