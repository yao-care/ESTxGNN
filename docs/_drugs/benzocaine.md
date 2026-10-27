---
layout: default
title: Benzocaine
parent: Solo predicción del modelo (L5)
nav_order: 98
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Benzocaine: nueva indicación predicha, Conjuntivitis papilar (nivel de evidencia L5). Indicación original: Tiña del pie (según el grafo de conocimiento"
monitor_inn: "Benzocaine"
predicted_indications: ["papillary conjunctivitis"]
---

# Benzocaine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Benzocaína: De Tiña del Pie a Conjuntivitis Papilar
{: .text-alpha }

## Resumen en Una Frase

La benzocaína es un anestésico local tópico de tipo éster, utilizado originalmente en afecciones como la tiña del pie, la dermatitis y la faringitis (según el grafo de conocimiento de TxGNN), y comercializado en España en forma de gel y solución bucal.
El modelo TxGNN predice que podría ser efectiva para la **conjuntivitis papilar**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tiña del pie (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Conjuntivitis papilar |
| Puntaje de Predicción TxGNN | 99,38% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la benzocaína es un anestésico local tópico de tipo éster que bloquea los canales de sodio dependientes de voltaje, reduciendo la conducción nerviosa y la sensibilidad local. Su uso se ha asociado con el alivio sintomático de molestias en piel y mucosas.

Un vínculo mecanístico especulativo sería el alivio del picor o la molestia ocular. Sin embargo, la conjuntivitis papilar es principalmente una afección inflamatoria alérgica o mecánica (por ejemplo, asociada al uso de lentes de contacto), y un anestésico no actúa sobre su causa subyacente. La similitud con las indicaciones originales (afecciones cutáneas y de mucosas con síntomas locales) es solo parcial y está pendiente de evaluar.

El puntaje elevado de TxGNN (99,38%) es únicamente una predicción del modelo, sin respaldo de estudios reales. Además, el uso ocular de benzocaína plantea preocupaciones de seguridad: toxicidad corneal con exposición repetida a anestésicos y riesgo de sensibilización por contacto, que podría empeorar la inflamación conjuntival. La compatibilidad de vías de administración también está pendiente de evaluar: las presentaciones actuales son bucales, gingivales y dentales, no oftálmicas.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 65866 | TOPISPRAY 200 mg/ml solución para pulverización bucal | Solución dental | No disponible en los datos compilados |
| 69069 | TOPIGEL 200 mg/g gel bucal | Gel bucal | No disponible en los datos compilados |
| 58609 | DENTISPRAY 50 mg/ml solución dental | Solución dental | No disponible en los datos compilados |
| 59360 | HURRICAINE 200 mg/g gel bucal | Gel bucal | No disponible en los datos compilados |
| 59359 | HURRICAINE SPRAY 200 mg/ml solución para pulverización bucal | Solución dental | No disponible en los datos compilados |

Hay 8 autorizaciones vigentes en total (todas de principio activo único); se muestran las 5 principales.

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no proceden del texto del prospecto; requieren verificación): insuficiencia y enfermedad hepática, encefalopatía hepática, epilepsia, porfirias, enfermedad renal, trombocitopenia, neutropenia, agranulocitosis, trastornos de la coagulación, diabetes mellitus y cetoacidosis diabética, sarcoidosis, hiperparatiroidismo e hipercalcemia, herpes simple, gastritis, trastornos de ansiedad y neuróticos, y abuso/dependencia de sustancias, entre otras.
- **Consideración específica para el uso ocular propuesto**: riesgo de toxicidad corneal con uso repetido de anestésicos y de sensibilización por contacto.

No se dispone de datos de interacciones farmacológicas. Consultar el prospecto para información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura. Además, el mecanismo de un anestésico no aborda la causa de la conjuntivitis papilar y el uso ocular plantea riesgos de seguridad relevantes.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), un vacío de datos bloqueante para el cribado de seguridad
- Datos detallados del mecanismo de acción desde DrugBank
- Estudios preclínicos de tolerabilidad ocular (toxicidad corneal y sensibilización)
- Evaluación de la viabilidad de una formulación oftálmica, ya que las presentaciones actuales no son oftálmicas
- Revisión sistemática de literatura que justifique la hipótesis antes de plantear ensayos clínicos
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

