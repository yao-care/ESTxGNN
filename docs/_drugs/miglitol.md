---
layout: default
title: Miglitol
parent: Solo predicción del modelo (L5)
nav_order: 528
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Miglitol: nueva indicación predicha, Síndrome de extremidad rígida focal (nivel de evidencia L5). Indicación original: Diabetes mellitus tipo 2 (según el grafo de conocimiento"
monitor_inn: "MIGLITOL"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pancreatic agenesis", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy"]
---

# Miglitol
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

# Miglitol: De Diabetes Mellitus Tipo 2 a Síndrome de Extremidad Rígida Focal

## Resumen en Una Frase

Miglitol es un fármaco antidiabético oral, originalmente utilizado para el tratamiento de la diabetes mellitus tipo 2.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de extremidad rígida focal**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es solo una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Diabetes mellitus tipo 2 (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Síndrome de extremidad rígida focal |
| Puntaje de Predicción TxGNN | 99.87% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información farmacológica conocida, miglitol es un inhibidor de las alfa-glucosidasas intestinales. Retrasa la digestión y absorción de los carbohidratos y reduce los picos de glucosa posprandial. Su eficacia en la diabetes tipo 2 es conocida.

El síndrome de extremidad rígida focal es un trastorno neurológico de origen probablemente autoinmune, perteneciente al espectro del síndrome de la persona rígida. Se relaciona con una disfunción GABAérgica y con anticuerpos anti-GAD. **No se ha identificado un vínculo mecanístico plausible** entre la inhibición de las alfa-glucosidasas intestinales y esta enfermedad.

La puntuación alta del modelo parece reflejar una asociación basada en el grafo, probablemente por vecinos compartidos de diabetes y autoinmunidad, y no una justificación farmacológica. En otras palabras, la predicción debe considerarse un artefacto computacional hasta que haya evidencia independiente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 62701 | PLUMAROL 50 mg COMPRIMIDOS | Comprimido | No especificada en los datos compilados |
| 62702 | PLUMAROL 100 mg COMPRIMIDOS | Comprimido | No especificada en los datos compilados |

Ambas autorizaciones son de monofármaco, están vigentes y pertenecen a Lacer S.A.

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no según el prospecto)**: enfermedad renal, piouréter, enfermedad inflamatoria intestinal, colitis ulcerosa, enfermedades infecciosas, hipoglucemia y lesiones.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones. Entre las 20 revisadas, la mayoría son de nivel moderado:
  - Simpaticomiméticos y broncodilatadores: fenilefrina, pseudoefedrina, epinefrina, formoterol, salbutamol.
  - Corticosteroides: hidrocortisona, triamcinolona.
  - Estrógenos: etinilestradiol, estradiol.
  - Otros: acetazolamida, hidroclorotiazida, etanol, alpelisib, aripiprazol, asenapina, asparaginasa.
  - De nivel menor: ranitidina y corticosteroides tópicos (hidrocortisona, alclometasona).
- Como contexto general de la clase, los inhibidores de alfa-glucosidasas pueden causar efectos adversos gastrointestinales. Si hay hipoglucemia durante el tratamiento, debe usarse glucosa oral y no sacarosa.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para el síndrome de extremidad rígida focal no cuenta con ensayos clínicos ni literatura (nivel L5), y no existe un vínculo mecanístico plausible con la acción de miglitol sobre las alfa-glucosidasas intestinales. La puntuación alta del modelo parece deberse a la proximidad en el grafo (diabetes y autoinmunidad), no a evidencia farmacológica.

**Para avanzar se necesita:**
- Una hipótesis mecanística plausible, respaldada por estudios preclínicos o de mecanismo, que conecte miglitol con la fisiopatología del síndrome de extremidad rígida focal.
- Datos oficiales de advertencias y contraindicaciones del prospecto de la AEMPS, y datos detallados del mecanismo de acción.
- Revisión de otras indicaciones predichas con mayor respaldo. Por ejemplo, la **diabetes mellitus tipo 1** (puntaje TxGNN 99.60%) cuenta con un ensayo de Fase 3 completado (NCT00213109, diseño abierto y sin inscripción reportada) y varios estudios clínicos publicados entre 1987 y 2011. Estos indican un beneficio adjunto a la insulina, aunque modesto, y no un mecanismo nuevo. Esa indicación podría evaluarse por separado, verificando antes los resultados del ensayo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

