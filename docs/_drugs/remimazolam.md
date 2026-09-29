---
layout: default
title: Remimazolam
parent: Solo predicción del modelo (L5)
nav_order: 463
evidence_level: L5
indication_count: 2
---

# Remimazolam
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Remimazolam: De Sedación Procedimental a Insomnio

## Resumen en Una Frase

Remimazolam es una benzodiazepina de acción ultracorta administrada por vía intravenosa. Según información general, se usa para la sedación procedimental, aunque el registro de AEMPS de este paquete no incluye el texto de la indicación.
El modelo TxGNN predice que podría ser efectivo para **insomnio**, pero ninguno de los **8 ensayos clínicos** relacionados evalúa insomnio crónico y no hay **ninguna publicación** que lo respalde.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sedación procedimental (información general; el texto de indicación no figura en el registro de AEMPS del paquete) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L5 (solo predicción del modelo; sin estudios clínicos directos ni estudios preclínicos o de mecanismo en los datos) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Remimazolam es un modulador alostérico positivo de los receptores GABA-A, el mismo mecanismo de los hipnóticos establecidos. Por eso es biológicamente plausible que tenga un efecto sedante-hipnótico. No se dispone de datos detallados de mecanismo de acción en el paquete; esta descripción procede de la justificación mecanística de la predicción.

La relación con el insomnio es indirecta. Los ensayos disponibles estudian sedación perioperatoria o en UCI, y solo dos observan trastornos del sueño postoperatorios. En ambos, remimazolam forma parte del régimen anestésico y no es la intervención evaluada.

Hay además limitaciones prácticas. Remimazolam solo se administra por vía intravenosa y tiene una semivida muy corta, lo que dificulta trasladarlo al tratamiento del insomnio. El puntaje TxGNN de 0.999 es una predicción, no evidencia clínica.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06284668](https://clinicaltrials.gov/study/NCT06284668) | N/A | Completado | 315 | Esketamina vs remimazolam sobre trastorno del sueño y ansiedad postoperatorios en extracción de ovocitos. Es el más cercano a insomnio, pero en contexto perioperatorio y sin resultados publicados. |
| [NCT06108830](https://clinicaltrials.gov/study/NCT06108830) | N/A | Reclutando | 400 | Esketamina combinada con remimazolam sobre trastorno del sueño y ansiedad postoperatorios en gastroenteroscopia. No permite separar el efecto de remimazolam del de esketamina. |
| [NCT05606315](https://clinicaltrials.gov/study/NCT05606315) | Fase 4 | Desconocido | 285 | Sedación en UCI con remimazolam besilato en pacientes ventilados tras cirugía oral y maxilofacial. Relación solo indirecta con el sueño. |
| [NCT06575530](https://clinicaltrials.gov/study/NCT06575530) | Fase 4 | Reclutando | 306 | Remimazolam vs dexmedetomidina en sedación de pacientes ventilados en UCI tras cirugía no cardíaca. Sin criterio de valoración de insomnio. |
| [NCT07046364](https://clinicaltrials.gov/study/NCT07046364) | Fase 4 | Reclutando | 248 | Remimazolam sobre el delirio de emergencia en neurocirugía pediátrica con sevoflurano. La indicación es delirio, no insomnio. |
| [NCT04532606](https://clinicaltrials.gov/study/NCT04532606) | Fase 4 | Reclutando | 1128 | Anestesia general con remimazolam y pronóstico tras cirugía de cáncer de vejiga. Los desenlaces son oncológicos y quirúrgicos. |
| [NCT05466279](https://clinicaltrials.gov/study/NCT05466279) | N/A | Completado | 131 | Remimazolam vs propofol + midazolam en anestesia general. Estudio de anestesia sin relación demostrable con insomnio. |
| [NCT05375747](https://clinicaltrials.gov/study/NCT05375747) | N/A | Retirado | 0 | Remimazolam vs propofol en anestesia intravenosa total para cirugía de mama. Retirado sin datos y sin relación con insomnio. |

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1201505001 | BYFAVO 20 MG POLVO PARA SOLUCION INYECTABLE (Paion Pharma GmbH) | Polvo para solución inyectable | No especificada en el registro |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo y en la plausibilidad del mecanismo GABA-A. Ningún ensayo evalúa insomnio crónico, no hay publicaciones y la vía exclusivamente intravenosa con semivida ultracorta limita su uso en esta indicación.

**Para avanzar se necesita:**
- Resultados de NCT06284668 y NCT06108830, que evalúan el sueño en contexto perioperatorio.
- Ficha técnica de AEMPS con advertencias, contraindicaciones e indicación autorizada, para el análisis de seguridad.
- Datos de mecanismo de acción desde DrugBank.
- Evaluación de compatibilidad de vía y formulación, dado que solo existe la presentación intravenosa.
- Estudios preclínicos o exploratorios de sueño que aíslen el efecto de remimazolam.

**Nota:** la segunda predicción del modelo, delirium por abstinencia alcohólica (puntaje 99.30%), no tiene ensayos ni publicaciones (nivel L5, Hold). Sería necesario evaluarla aparte.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

