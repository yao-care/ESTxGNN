---
layout: default
title: Acarbose
parent: Solo predicción del modelo (L5)
nav_order: 13
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Acarbose: nueva indicación predicha, Síndrome de la extremidad rígida focal (nivel de evidencia L5). Indicación original: Diabetes mellitus tipo 2 (según el grafo de conocimiento"
---

# Acarbose
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

# Acarbosa: De Diabetes Mellitus Tipo 2 a Síndrome de la Extremidad Rígida Focal

## Resumen en Una Frase

Acarbosa es un inhibidor de la alfa-glucosidasa intestinal, utilizado originalmente para el tratamiento de la diabetes mellitus tipo 2.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de la extremidad rígida focal**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Diabetes mellitus tipo 2 (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Síndrome de la extremidad rígida focal |
| Puntaje de Predicción TxGNN | 99.65% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 12 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, acarbosa inhibe las alfa-glucosidasas intestinales, retrasando la digestión de carbohidratos y reduciendo la absorción de glucosa posprandial. Su eficacia en la diabetes tipo 2 está bien establecida.

Sin embargo, **no se identifica un vínculo mecanístico claro** con el síndrome de la extremidad rígida focal. Esta enfermedad es un trastorno neuroinmunológico del espectro de la persona rígida (patología GABAérgica/anti-GAD). La puntuación elevada de TxGNN probablemente refleja nodos compartidos en el grafo relacionados con la diabetes (por ejemplo, la autoinmunidad anti-GAD), y no una relación farmacológica demostrada.

Es importante señalar que esta predicción no es un caso aislado: otras indicaciones predichas (síndrome de la persona rígida clásico, síndrome de disfunción sensible a tiamina, opsismodisplasia, diversas lipodistrofias localizadas y agenesia pancreática) comparten el mismo patrón de puntuaciones altas sin evidencia clínica ni mecanismo plausible.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se listan las 5 primeras de las 12 autorizaciones vigentes (todas de principio activo único):

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 76586 | ACARBOSA FARMALIDER 50 MG COMPRIMIDOS | Comprimido | Farmalider S.A. |
| 70451 | ACARBOSA TECNIGEN 50 mg COMPRIMIDOS | Comprimido | Tecnimede España Industria Farmacéutica S.A. |
| 71442 | ACARBOSA VIATRIS 50 MG COMPRIMIDOS | Comprimido | Viatris Limited |
| 59419 | GLUCOBAY 50 mg COMPRIMIDOS | Comprimido | Bayer Hispania S.L. |
| 71443 | ACARBOSA VIATRIS 100 MG COMPRIMIDOS | Comprimido | Viatris Limited |

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no el prospecto)**: enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, cirrosis hepática, enfermedad inflamatoria intestinal, hipoglucemia y lesiones.
- **Interacciones Farmacológicas**: se identificaron 371 interacciones en total. Entre las revisadas figuran interacciones de nivel moderado con acetazolamida, salbutamol, aloe vera (hoja), alpelisib, amprenavir, aripiprazol, asenapina, asparaginasa, atazanavir, bedaquilina, bendroflumetiazida, benzfetamina, benzotiazida y betametasona; y de nivel menor con albiglutida, alclometasona (tópica), ácido lipoico, amcinonida y anisindiona.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible entre la inhibición de la alfa-glucosidasa y la fisiopatología neuroinmunológica del síndrome de la extremidad rígida focal.

**Para avanzar se necesita:**
- Evidencia preclínica o clínica que sustente la relación entre acarbosa y esta enfermedad
- Datos del mecanismo de acción para analizar vínculos mecanísticos
- Revisión de las advertencias y contraindicaciones del prospecto de la AEMPS
- Una revisión de las demás indicaciones predichas, que presentan el mismo nivel de evidencia (L5) y el mismo patrón de ausencia de respaldo
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

