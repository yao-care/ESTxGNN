---
layout: default
title: Dextromethorphan
parent: Solo predicción del modelo (L5)
nav_order: 172
evidence_level: L5
indication_count: 6
---

# Dextromethorphan
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Dextrometorfano: De Tos (uso antitusivo) a Enfermedad de la Cavidad Nasal

## Resumen en Una Frase

El dextrometorfano es un antitusivo de acción central, comercializado en España en jarabes, soluciones orales, comprimidos y pastillas.
El modelo TxGNN predice que podría ser efectivo para **enfermedad de la cavidad nasal**, pero actualmente **no hay literatura** que lo respalde y el único ensayo clínico asociado (**1 ensayo**) estudia depresión mayor, no patología nasal.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tos (uso antitusivo según datos farmacológicos; los textos de indicación de AEMPS no están disponibles) |
| Nueva Indicación Predicha | Enfermedad de la cavidad nasal |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados de mecanismo de acción en el campo original del fármaco. Según la información complementaria, el dextrometorfano es un antagonista del receptor NMDA, agonista del receptor sigma-1 e inhibidor de la recaptación de serotonina, con actividad antitusiva central. Los datos farmacológicos también lo relacionan con GRIN2C (subunidad GluN2C del receptor NMDA), TAS2R1 (receptor del gusto amargo) y SIGMAR1.

La relación con la nueva indicación es débil. No hay un vínculo directo entre estos mecanismos y la patología de la cavidad nasal. Si existiera algún beneficio, probablemente sería sintomático (tos o hipersensibilidad de la vía aérea superior) y no modificador de la enfermedad.

Por ello, la puntuación tan alta del modelo debe leerse como una señal de hipótesis, no como evidencia de eficacia. Las otras indicaciones predichas tampoco tienen ensayos ni literatura: laringofaringitis aguda (99.98%), difteria faucial, cefalea trigémino-autonómica, trastorno degenerativo del disco cervical y urticaria alérgica. En varias de ellas el vínculo mecanístico es nulo o meramente especulativo.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06958692](https://clinicaltrials.gov/study/NCT06958692) | Fase 3 | Reclutando | 388 | Ensayo multicéntrico, aleatorizado, doble ciego y controlado con placebo de comprimidos de liberación sostenida de dextrometorfano y bupropión en adultos chinos con trastorno depresivo mayor. Sin resultados aún. Es una combinación a dosis fija y no está relacionado con patología nasal. |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones. Los textos de indicación aprobada no están disponibles en los datos recibidos.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 57623 | Cinfatos Antitusivo 2 mg/ml Solución Oral | Solución oral | No disponible |
| 83679 | Intertos 15 mg Comprimidos | Comprimido | No disponible |
| 67400 | Bicasan 2 mg/ml Jarabe | Jarabe | No disponible |
| 80342 | Tosystop 20 mg Solución Oral | Solución oral | No disponible |
| 24381 | Propalcof 15 mg Comprimidos | Comprimido | No disponible |

Otras formas farmacéuticas registradas: comprimido bucodispersable, pastilla para chupar y cápsula blanda.

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: la consulta se completó, pero los 3 registros son dianas farmacológicas, no interacciones clínicas con otros medicamentos: GluN2C (GRIN2C), TAS2R1 y receptor sigma no opioide intracelular 1 (SIGMAR1). No incluyen nivel de gravedad.

Consultar el prospecto para información de advertencias y contraindicaciones.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene respaldo clínico ni bibliográfico. El único ensayo asociado evalúa una combinación en depresión mayor, y el mecanismo del fármaco no se conecta con la patología nasal. Con las reglas de nivel de evidencia el resultado es L5. El nivel L3 asignado inicialmente al ensayo no se sostiene.

**Para avanzar se necesita:**
- Revisión bibliográfica dirigida (dextrometorfano en rinitis, rinosinusitis o hipersensibilidad de la vía aérea superior)
- Definir con precisión qué patología nasal concreta abarca el término predicho
- Obtener del prospecto de AEMPS las advertencias, contraindicaciones e indicaciones aprobadas, que actualmente faltan
- Datos de mecanismo de acción desde DrugBank para analizar el vínculo mecanístico
- Comprobar en el registro que el ensayo NCT06958692 no incluye ninguna rama nasal

*Estos resultados son solo para investigación y no constituyen consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

