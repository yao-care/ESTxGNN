---
layout: default
title: Glimepiride
parent: Solo predicción del modelo (L5)
nav_order: 379
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Glimepiride: nueva indicación predicha, Síndrome de la extremidad rígida focal (nivel de evidencia L5). Indicación original: Diabetes mellitus tipo 2 (según el grafo de conocimiento"
monitor_inn: "Glimepiride"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
---

# Glimepiride
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Glimepirida: De Diabetes Mellitus Tipo 2 a Síndrome de la Extremidad Rígida Focal
{: .text-alpha }

## Resumen en Una Frase

Glimepirida es una sulfonilurea utilizada originalmente para el tratamiento de la diabetes mellitus tipo 2.
El modelo TxGNN predice que podría ser efectiva para el **síndrome de la extremidad rígida focal**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Diabetes mellitus tipo 2 (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Síndrome de la extremidad rígida focal |
| Puntaje de Predicción TxGNN | 99,75% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, glimepirida es una sulfonilurea que estimula la secreción de insulina al actuar sobre los canales de potasio dependientes de ATP (K-ATP) de las células beta pancreáticas. Su eficacia en la diabetes tipo 2 está comprobada.

La posible conexión con el síndrome de la extremidad rígida focal es indirecta: este trastorno, del espectro del síndrome de la persona rígida, se asocia con autoinmunidad frente a GAD65 y con frecuencia coexiste con diabetes. Es probable que el modelo refleje esta co-ocurrencia de enfermedades en el grafo de conocimiento y no un efecto terapéutico real.

Glimepirida no tiene un mecanismo establecido sobre la rigidez muscular ni sobre la disfunción GABAérgica. Por ello, el vínculo mecanístico es especulativo y no está verificado.

Otras predicciones con puntajes similares (síndrome de la persona rígida clásico, opsismodisplasia, síndrome de disfunción sensible a tiamina, varias lipodistrofias localizadas y agenesia pancreática) tampoco cuentan con evidencia clínica. Todas se clasifican como L5 y "Hold". Cabe destacar que el síndrome de la persona rígida clásico obtuvo exactamente el mismo puntaje que la variante focal, lo que sugiere una asociación compartida del grafo y no evidencia independiente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal.

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones vigentes (todas de principio activo único, forma farmacéutica comprimido). El texto de la indicación aprobada no figura en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 61406 | AMARYL 2 mg comprimidos (Sanofi Aventis) | Comprimido | No disponible |
| 61409 | AMARYL 4 mg comprimidos (Sanofi Aventis) | Comprimido | No disponible |
| 62807 | RONAME 4 mg comprimidos (Lacer) | Comprimido | No disponible |
| 62808 | RONAME 2 mg comprimidos (Lacer) | Comprimido | No disponible |
| 67533 | Glimepirida Normon 2 mg comprimidos EFG | Comprimido | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, insuficiencia cardíaca congestiva, hipopituitarismo y déficits hormonales hipofisarios, hipogonadismo hipogonadotrópico (incluido el síndrome de Kallmann), síndrome de Sheehan, enfermedad del timo, osteoporosis (incluida la posmenopáusica) y enfermedades infecciosas.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones. Entre las listadas de nivel moderado figuran fenilefrina, acebutolol, acetazolamida, famotidina, ranitidina, acitretina, formoterol, pseudoefedrina, ketorolaco, epinefrina, ibuprofeno, etinilestradiol, hidrocortisona, albiglutida, salbutamol, etanol, nitazoxanida e hidroclorotiazida. La hidrocortisona tópica y la alclometasona tópica son de nivel leve.
- **Consideración específica**: en pacientes con síndrome de la persona rígida, la hipoglucemia inducida por sulfonilureas podría ser un problema de seguridad.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos ni literatura de apoyo, y el vínculo mecanístico probablemente refleja la co-ocurrencia de diabetes y autoinmunidad anti-GAD y no un efecto terapéutico.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) y análisis del vínculo mecanístico con la rigidez muscular y la disfunción GABAérgica
- Advertencias y contraindicaciones del prospecto de la AEMPS (dato bloqueante para el cribado de seguridad)
- Estudios preclínicos o series de casos que sustenten un posible beneficio
- Evaluación del riesgo de hipoglucemia en la población diana
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

