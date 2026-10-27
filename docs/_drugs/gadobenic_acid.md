---
layout: default
title: Gadobenic Acid
parent: Solo predicción del modelo (L5)
nav_order: 367
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Gadobenic Acid: nueva indicación predicha, Osteoartritis (nivel de evidencia L5). Indicación original: Agente de contraste para diagnóstico por RM (las autorizaciones no in…"
monitor_inn: "gadobenic acid"
predicted_indications: ["osteoarthritis", "osteoarthritis susceptibility"]
---

# Gadobenic Acid
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

## Ácido gadobénico: De Agente de Contraste para Resonancia Magnética a Osteoartritis
{: .text-alpha }

## Resumen en Una Frase

El ácido gadobénico (gadobenato de dimeglumina) es un agente de contraste a base de gadolinio utilizado en diagnóstico por resonancia magnética (RM), comercializado en España como MULTIHANCE.
El modelo TxGNN predice que podría ser efectivo para **osteoartritis**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Agente de contraste para diagnóstico por RM (las autorizaciones no incluyen texto de indicación en los datos compilados) |
| Nueva Indicación Predicha | Osteoartritis |
| Puntaje de Predicción TxGNN | 99.21% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, el ácido gadobénico es un agente de contraste paramagnético a base de gadolinio, empleado con fines diagnósticos y no terapéuticos. Su función es mejorar la señal en imágenes de RM, no modificar procesos patológicos.

Con los datos compilados, **no se identifica un vínculo mecanístico** que respalde su uso en osteoartritis. El puntaje alto de TxGNN (0.992) es una predicción computacional sin ensayos ni literatura que la corroboren. Su uso en imagen articular (p. ej., artrografía por RM) es diagnóstico y no debe confundirse con evidencia terapéutica.

La predicción podría reflejar artefactos del grafo de conocimiento, como asociaciones compartidas con imagen musculoesquelética o con la biología de iones metálicos relacionados con el gadolinio. Una segunda predicción, "susceptibilidad a la osteoartritis" (puntaje 99.16%), es un concepto de asociación genética o de riesgo y no una enfermedad tratable. Probablemente sea una señal redundante de la primera, no una evidencia independiente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 66373 | MULTIHANCE 529 mg/ml SOLUCIÓN INYECTABLE | Solución inyectable | No disponible en los datos compilados |
| 71048 | MULTIHANCE 529 mg/ml SOLUCIÓN INYECTABLE EN JERINGA PRECARGADA | Solución inyectable | No disponible en los datos compilados |

Ambas autorizaciones corresponden a Bracco Imaging S.P.A. y están vigentes.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 50 interacciones en total; las 20 detalladas son de nivel moderado. Las principales incluyen:
  - Antineoplásicos: paclitaxel, docetaxel, cisplatino, doxorrubicina, daunorubicina (también liposomal), metotrexato, tamoxifeno.
  - Betabloqueantes: acebutolol, atenolol, betaxolol (también oftálmico), bisoprolol, carteolol (oftálmico), carvedilol, nadolol, timolol (oftálmico).
  - Antirretrovirales: atazanavir, ritonavir, saquinavir.

Consultar el prospecto para el resto de la información de seguridad (advertencias y contraindicaciones).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y el ácido gadobénico es un agente de contraste diagnóstico sin farmacología conocida modificadora de la enfermedad en osteoartritis. No hay un vínculo mecanístico que la sustente.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consulta a DrugBank)
- Advertencias y contraindicaciones del prospecto de la AEMPS (necesarias para el cribado de seguridad)
- Texto de indicaciones aprobadas de las dos autorizaciones
- Estudios preclínicos o de mecanismo que justifiquen un efecto terapéutico en osteoartritis
- Revisión de la plausibilidad de la predicción, descartando artefactos del grafo de conocimiento
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

