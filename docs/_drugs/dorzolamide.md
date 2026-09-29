---
layout: default
title: Dorzolamide
parent: Evidencia alta (L1-L2)
nav_order: 182
evidence_level: L2
indication_count: 10
---

# Dorzolamide
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **10** 
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

# Dorzolamida: De Glaucoma de Ángulo Abierto a Glaucoma Hereditario Primario

## Resumen en Una Frase

Dorzolamida es un inhibidor de la anhidrasa carbónica en colirio, utilizado para reducir la presión intraocular en el glaucoma de ángulo abierto y la hipertensión ocular.
El modelo TxGNN predice que podría ser efectivo para el **glaucoma hereditario primario**, con **1 ensayo clínico** (Fase 2, pequeño) y **ninguna publicación** directamente relacionada.
Esta predicción es una extensión muy cercana a su uso ya autorizado, por lo que no constituye un reposicionamiento en sentido estricto.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Glaucoma de ángulo abierto e hipertensión ocular (según la descripción de uso clínico de la base farmacológica; los textos de indicación de las autorizaciones españolas vienen vacíos) |
| Nueva Indicación Predicha | Glaucoma hereditario primario |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

La base de datos no registra el mecanismo de acción original del fármaco. El análisis de reposicionamiento indica que la dorzolamida inhibe la anhidrasa carbónica II en el epitelio ciliar. Esto reduce la producción de bicarbonato y de humor acuoso y, con ello, la presión intraocular (PIO). Los datos farmacológicos confirman además su unión a las anhidrasas carbónicas 1, 7, 12 y 14.

Este mecanismo se aplica al glaucoma dependiente de la PIO en general. Por eso es coherente que el modelo lo asocie con una forma hereditaria o pediátrica: el objetivo terapéutico (bajar la PIO) es el mismo que en su indicación original.

La debilidad está en la evidencia específica. Solo hay un ensayo de Fase 2 con latanoprost y dorzolamida en glaucoma pediátrico primario. El título del registro está truncado, por lo que no se pudo confirmar la población exacta ni el papel de la dorzolamida en cada brazo.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Fase 2 | Completado | 37 | Evalúa el efecto hipotensor ocular y la seguridad de latanoprost y dorzolamida en glaucoma pediátrico primario refractario a cirugía (2009-2016). La muestra es pequeña y el protocolo se enmendó para reducir el número de ojos previstos. |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 75621 | Dorzolamida Farmalider 20 mg/ml colirio en solución | Colirio en solución | No disponible en los datos |
| 77776 | Arzolan 20 mg/ml colirio en solución | Colirio en solución | No disponible en los datos |
| 86764 | Dimaz 20 mg/ml colirio en solución | Colirio en solución | No disponible en los datos |
| 60651 | Trusopt 20 mg/ml colirio en solución | Colirio en solución | No disponible en los datos |
| 72752 | Dorzolamida Aristo 20 mg/ml colirio en solución | Colirio en solución | No disponible en los datos |

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: no se registraron interacciones con otros fármacos. Los datos disponibles describen solo la unión a las anhidrasas carbónicas 1, 7, 12 y 14.
- **Precauciones derivadas del análisis de reposicionamiento** (no verificadas con el prospecto de la AEMPS): alergia a sulfonamidas, compromiso del endotelio corneal y uso exclusivamente tópico.

Consultar el prospecto para el resto de la información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- El único respaldo específico para la forma hereditaria o pediátrica es un ensayo de Fase 2 pequeño (n=37) con población no confirmada, y no hay publicaciones asociadas.
- No se pudo revisar el prospecto de la AEMPS (advertencias y contraindicaciones), lo que bloquea el cribado de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS (advertencias, contraindicaciones y uso pediátrico).
- Confirmar la población y los brazos de NCT01527682, y buscar literatura sobre dorzolamida en glaucoma congénito o pediátrico.
- Obtener los datos del mecanismo de acción original desde DrugBank.

**Nota adicional:** el modelo también predijo *glaucoma 1, de ángulo abierto* y *glaucoma de ángulo abierto*. Ambos tienen evidencia L1 (múltiples ECA de Fase 3 y 4, revisiones sistemáticas y una revisión Cochrane), con la recomendación "Proceed with Guardrails". Son usos ya autorizados, y sirven como validación del modelo más que como oportunidad nueva. Las demás predicciones (alopecia, hipotricosis, insuficiencia cardíaca, enfermedades pulmonares y respiratorias) no tienen respaldo mecanístico ni clínico y deben mantenerse en Hold.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

