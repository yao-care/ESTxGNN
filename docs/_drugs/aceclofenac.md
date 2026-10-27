---
layout: default
title: Aceclofenac
parent: Solo predicción del modelo (L5)
nav_order: 14
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Aceclofenac: nueva indicación predicha, Síndrome de braquiolmia-amelogénesis imperfecta (nivel de evidencia L5). Indicación original: Artritis reumatoide, espondilitis anquilosante…"
monitor_inn: "Aceclofenac"
predicted_indications: ["brachyolmia-amelogenesis imperfecta syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "hypermobility of coccyx", "inflammatory spondylopathy", "Kummell disease"]
---

# Aceclofenac
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

## Aceclofenaco: De Artritis Reumatoide a Síndrome de Braquiolmia-Amelogénesis Imperfecta
{: .text-alpha }

## Resumen en Una Frase

Aceclofenaco es un antiinflamatorio no esteroideo (AINE) oral, utilizado originalmente para el tratamiento del dolor y la inflamación en enfermedades reumáticas como la artritis reumatoide, la espondilitis anquilosante y la artrosis.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de braquiolmia-amelogénesis imperfecta**, pero **no existen ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Artritis reumatoide, espondilitis anquilosante, artrosis y otras enfermedades reumáticas (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Síndrome de braquiolmia-amelogénesis imperfecta |
| Puntaje de Predicción TxGNN | 99,89% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 16 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Según la información conocida, aceclofenaco es un AINE derivado del ácido fenilacético, con propiedades antiinflamatorias y analgésicas similares a las del diclofenaco, que actúa mediante la inhibición de la síntesis de prostaglandinas (entre ellas la PGE2). Su eficacia en enfermedades reumáticas inflamatorias y degenerativas está bien establecida.

Sin embargo, **la razonabilidad biológica de esta predicción es muy baja**. El síndrome de braquiolmia-amelogénesis imperfecta es un trastorno genético raro que afecta al esqueleto (platispondilia) y al esmalte dental. Un inhibidor de la COX no tiene una relación clara con su patología subyacente. La puntuación alta de TxGNN probablemente refleja anotaciones musculoesqueléticas compartidas en el grafo de conocimiento y no un vínculo mecanístico real.

Las demás predicciones de mayor rango (displasia acromesomélica tipo Hunter-Thompson, miosclerosis, braquiolmia, pseudoacondroplasia) presentan el mismo problema: son trastornos genéticos o fibróticos raros en los que, como máximo, cabría un alivio sintomático del dolor, sin efecto modificador de la enfermedad. La única predicción con cierta base de evidencia es la espondilopatía inflamatoria (rango 8), pero corresponde en gran medida a una reclasificación de la espondilitis anquilosante, que ya es una indicación existente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para el síndrome de braquiolmia-amelogénesis imperfecta.

*Nota:* para la predicción de rango 8 (espondilopatía inflamatoria) sí se recuperó literatura, que apoya de forma indirecta el uso de aceclofenaco en enfermedades inflamatorias axiales. No constituye evidencia para la indicación principal evaluada aquí.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 70982 | Aceclofenaco Aurovitas Spain 100 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos compilados |
| 69551 | Aracenac 100 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos compilados |
| 79696 | Aceclofenaco Stada 100 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos compilados |
| 59024 | Airtal 100 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |
| 60695 | Airtal 100 mg polvo para suspensión oral | Polvo para suspensión oral | No disponible en los datos compilados |

Hay 16 autorizaciones vigentes en total, todas de medicamentos de un solo principio activo. Además de los comprimidos y el polvo para suspensión oral, existe una presentación en crema (Airtal Difucrem 15 mg/g).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa exclusivamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible entre la inhibición de la COX y un trastorno genético esquelético-dental raro. Aunque el puntaje TxGNN es alto, no es suficiente por sí solo para justificar avanzar.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA) del fármaco
- Advertencias y contraindicaciones del prospecto de la AEMPS (actualmente no disponibles, lo que impide el cribado de seguridad)
- Una hipótesis fisiopatológica que justifique el uso de un AINE en esta enfermedad, con respaldo preclínico
- Evaluar con prioridad otras predicciones con mayor plausibilidad biológica (p. ej., espondilopatía inflamatoria), teniendo en cuenta que se solapa con indicaciones ya existentes
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

