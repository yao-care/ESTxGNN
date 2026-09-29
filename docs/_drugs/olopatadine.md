---
layout: default
title: Olopatadine
parent: Solo predicción del modelo (L5)
nav_order: 394
evidence_level: L5
indication_count: 1
---

# Olopatadine
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

# Olopatadina: De Conjuntivitis Alérgica a Conjuntivitis Rosácea

## Resumen en Una Frase

Olopatadina es un antihistamínico H1 con acción estabilizadora de mastocitos, usado por vía tópica ocular (colirio) para la conjuntivitis alérgica. Este uso procede de conocimiento farmacológico general, porque las autorizaciones del Evidence Pack no incluyen el texto de indicación.
El modelo TxGNN predice que podría ser efectivo para la **conjuntivitis rosácea**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es una predicción basada solo en el modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos de AEMPS (texto de indicación vacío en todas las autorizaciones). Uso conocido: conjuntivitis alérgica (conocimiento general, no verificado) |
| Nueva Indicación Predicha | Conjuntivitis rosácea |
| Puntaje de Predicción TxGNN | 99.41% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 9 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según el conocimiento farmacológico general (no verificado con los datos suministrados), la olopatadina es un antagonista H1 con actividad estabilizadora de mastocitos. Se usa por vía tópica en conjuntivitis alérgica, y mecanísticamente podría ser aplicable a la conjuntivitis asociada a rosácea (rosácea ocular).

La relación sería solo indirecta: la histamina y los mastocitos podrían contribuir a la inflamación de la superficie ocular. Sin embargo, la rosácea ocular se explica sobre todo por disfunción de las glándulas de Meibomio, inestabilidad de la película lagrimal y factores inmunes innatos y microbianos. Un mecanismo antihistamínico abordaría, como mucho, una parte menor del cuadro.

El puntaje alto (0.994) no es evidencia clínica. Podría reflejar en parte la asociación conocida del fármaco con conjuntivitis en el grafo de conocimiento, lo que lo convertiría en una señal de indicación cercana y no específica de rosácea. Como no hay indicaciones originales registradas, no fue posible confirmar si el grafo ya cubre la conjuntivitis alérgica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Se muestran 5 de las 9 autorizaciones. Todas corresponden a colirio en solución.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 02217001IP3 | OPATANOL 1 mg/ml colirio en solución | Colirio en solución | No consignada en los datos |
| 02217001IP | OPATANOL 1 mg/ml colirio en solución | Colirio en solución | No consignada en los datos |
| 02217001IP1 | OPATANOL 1 mg/ml colirio en solución | Colirio en solución | No consignada en los datos |
| 02217001 | OPATANOL 1 mg/ml colirio en solución | Colirio en solución | No consignada en los datos |
| 02217001IP2 | OPATANOL 1 mg/ml colirio en solución | Colirio en solución | No consignada en los datos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5), sin ensayos ni publicaciones. El vínculo mecanístico con la rosácea ocular es débil e indirecto, y faltan datos de seguridad y de mecanismo de acción.

**Para avanzar se necesita:**
- Obtener el prospecto de AEMPS y extraer advertencias, contraindicaciones e indicación aprobada (este dato bloquea el cribado de seguridad).
- Completar el mecanismo de acción (MOA) desde DrugBank.
- Revisar la literatura y los registros de ensayos por si existe evidencia en conjuntivitis rosácea o rosácea ocular.
- Confirmar si el grafo ya cubre la conjuntivitis alérgica, para saber si la señal es específica o de una indicación cercana.
- Evaluar la compatibilidad de vía. El colirio es de uso ocular tópico, pero el estado está pendiente.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

