---
layout: default
title: Megestrol Acetate
parent: Evidencia alta (L1-L2)
nav_order: 340
evidence_level: L2
indication_count: 10
---

# Megestrol Acetate
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

# Acetato de megestrol: De Indicación Autorizada en España (sin detallar) a Carcinoma Endometrial del Cuerpo Uterino

## Resumen en Una Frase

El acetato de megestrol es un progestágeno sintético comercializado en España en suspensión oral, comprimidos y granulado, aunque los datos disponibles no detallan su indicación autorizada. El modelo TxGNN predice que podría ser efectivo para el **carcinoma endometrial del cuerpo uterino**, con **4 ensayos clínicos** registrados y **ninguna publicación** específica para esta indicación en el paquete de evidencia.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en los datos de autorización |
| Nueva Indicación Predicha | Carcinoma endometrial del cuerpo uterino |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

El acetato de megestrol es un progestágeno sintético. Actúa sobre los receptores de progesterona de los tumores endometriales sensibles a hormonas, favoreciendo la diferenciación celular y reduciendo la proliferación. Es un mecanismo hormonal bien establecido, no solo una predicción del grafo. Actualmente no se dispone de datos detallados de mecanismo de acción en DrugBank para este registro.

El estrógeno estimula el crecimiento de las células del cáncer de endometrio, y la terapia con progestágenos contrarresta ese efecto. Por eso los ensayos del paquete evalúan el megestrol o progestágenos afines en carcinoma endometrial, hiperplasia atípica y neoplasia intraepitelial endometrial. Varios de ellos se centran en la preservación de la fertilidad.

La relación con la indicación original no puede evaluarse con estos datos, porque los textos de indicación de las autorizaciones españolas están vacíos y el análisis de similitud está pendiente.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00729586](https://clinicaltrials.gov/study/NCT00729586) | Fase 2 | Completado | 73 | ECA aleatorizado de temsirolimus solo o con terapia hormonal (megestrol y tamoxifeno) en cáncer de endometrio avanzado, persistente o recurrente. Señal directa más relevante; falta confirmar el brazo de megestrol. |
| [NCT00503581](https://clinicaltrials.gov/study/NCT00503581) | Fase 2 | Terminado | 9 | Progestágeno continuo vs. secuencial (megestrol) en neoplasia intraepitelial endometrial con deseo de preservar el útero. Terminado con n=9, sin datos de eficacia utilizables. |
| [NCT04046185](https://clinicaltrials.gov/study/NCT04046185) | Fase 1 temprana | Desconocido | 60 | Inhibidor de PD-1 con progesterona vs. progesterona sola en cáncer de endometrio precoz con deseo de fertilidad. El efecto del megestrol no puede aislarse. |
| [NCT07462663](https://clinicaltrials.gov/study/NCT07462663) | Fase 4 | Aún sin reclutar | 80 | Piloto (SHAPE-ENDO, Barcelona) de estrategia hormonal más prehabilitación frente a cirugía inmediata en hiperplasia atípica o cáncer endometrioide de bajo riesgo con IMC ≥40. Sin resultados. |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 4376IP | MAYGACE ALTAS DOSIS 40 MG/ML | Suspensión oral | No especificada en los datos |
| 58775 | BOREA 160 mg | Comprimido | No especificada en los datos |
| 62012 | MEGEFREN SOBRES | Granulado | No especificada en los datos |
| 60783 | MAYGACE ALTAS DOSIS 40 mg/ml | Suspensión oral | No especificada en los datos |
| 58773 | MEGEFREN 160 mg | Comprimido | No especificada en los datos |

Se muestran 5 de las 6 autorizaciones registradas.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia hormonal (progestágeno); no es un citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto; la literatura del paquete describe efectos sobre la coagulación y supresión suprarrenal con dosis altas |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ECA de Fase 2 completado (n=73) que incluye terapia hormonal con megestrol en cáncer de endometrio avanzado, lo que sitúa la evidencia en L2, y el mecanismo progestágeno es plausible y conocido. Sin embargo, no hay literatura específica, el efecto del megestrol no está aislado en la mayoría de los ensayos y faltan los datos de seguridad de la ficha técnica.

**Para avanzar se necesita:**
- Confirmar que el megestrol figura en el brazo de tratamiento de NCT00729586 y obtener sus resultados.
- Descargar la ficha técnica de la AEMPS para obtener advertencias, contraindicaciones e indicaciones autorizadas.
- Completar el mecanismo de acción desde DrugBank.
- Buscar literatura específica de megestrol en carcinoma endometrial.
- Definir un plan de monitoreo de seguridad (eventos tromboembólicos, supresión suprarrenal) antes de cualquier uso en esta indicación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

