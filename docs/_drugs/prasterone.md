---
layout: default
title: Prasterone
parent: Solo predicción del modelo (L5)
nav_order: 654
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "prasterone"
predicted_indications: ["heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "thrombophilia", "severe nonproliferative diabetic retinopathy", "thrombophilia due to protein S deficiency, autosomal recessive", "scleroderma (disease)", "complement component 4a deficiency", "pseudo-von Willebrand disease", "primary release disorder of platelets"]
description: "Prasterone: nueva indicación predicha, Deficiencia del cofactor 2 de la heparina (heparin cofactor 2 deficiency) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Prasterone
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

## Prasterone: Deficiencia del cofactor 2 de la heparina (heparin cofactor 2 deficiency)
{: .text-alpha }

## Resumen en Una Frase

Prasterona (DHEA) es un precursor de andrógenos y estrógenos, utilizado originalmente en dispareunia (dolor durante las relaciones sexuales).
El modelo TxGNN predice que podría ser efectivo para **deficiencia del cofactor 2 de la heparina**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata de una predicción puramente basada en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Deficiencia del cofactor 2 de la heparina (heparin cofactor 2 deficiency) |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 1 de 1) |
| Número de Autorizaciones | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la prasterona es un precursor hormonal (DHEA) que se convierte localmente en andrógenos y estrógenos. Su eficacia se ha establecido en la atrofia vulvovaginal con dispareunia, y se ha estudiado por sus propiedades inmunomoduladoras en el lupus.

Para la deficiencia del cofactor 2 de la heparina (SERPIND1), **no se ha identificado un vínculo mecanístico establecido**. La puntuación del modelo es muy alta (0,9999), pero proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. Cualquier relación sería especulativa, por ejemplo, mediante una modulación hormonal de la síntesis hepática de proteínas de coagulación.

Conviene señalar que el resto de las predicciones principales corresponden también a trastornos de la coagulación (factor V, antitrombina, trombofilia, deficiencia de proteína S, etc.) y carecen igualmente de respaldo clínico. La única predicción con una justificación biológica algo más plausible es la **esclerodermia** (posición 7, puntuación 0,9911), por su cercanía con el lupus y las propiedades inmunomoduladoras de la DHEA; requeriría una búsqueda bibliográfica específica antes de avanzar.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1171255001 | INTRAROSA 6,5 MG ÓVULOS | Óvulo | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas / Farmacología**: se registró una interacción de tipo farmacológico con el receptor de glicina (todos los subtipos), en la que la deshidroepiandrosterona actúa como ligando (metabolito). No se dispone de un nivel de gravedad clínica asociado.
- **Consideración teórica**: en las predicciones de trastornos protrombóticos (p. ej., exceso de factor V con trombosis espontánea, trombofilia), los precursores de esteroides sexuales exógenos podrían afectar teóricamente al equilibrio de la coagulación. Esto constituye una preocupación potencial de seguridad, no una justificación terapéutica.

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y sin un mecanismo plausible; además, el efecto de los esteroides sexuales sobre la coagulación podría ser incluso adverso.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), actualmente un vacío bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción (p. ej., consultando DrugBank).
- Realizar una búsqueda bibliográfica dirigida, priorizando la esclerodermia como hipótesis más plausible desde el punto de vista biológico.
- Evaluar la compatibilidad de la vía de administración (actualmente solo óvulo vaginal) con la nueva indicación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

