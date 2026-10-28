---
layout: default
title: Glucarpidase
parent: Solo predicción del modelo (L5)
nav_order: 381
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Glucarpidase: nueva indicación predicha, Catarata diabética (nivel de evidencia L5). Indicación original: No disponible en la autorización de AEMPS (el texto de indicación est…"
monitor_inn: "glucarpidase"
predicted_indications: ["diabetic cataract", "diabetic retinopathy", "tetanic cataract", "mature cataract", "craniostenosis cataract", "immature cataract", "diabetes mellitus type 2 associated cataract", "cortical cataract", "nuclear senile cataract", "senile cataract"]
---

# Glucarpidase
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

## Glucarpidasa: De Toxicidad por Metotrexato a Catarata Diabética
{: .text-alpha }

## Resumen en Una Frase

Glucarpidasa es una enzima recombinante (carboxipeptidasa G2) comercializada en España como Voraxaze, utilizada para degradar el metotrexato cuando sus concentraciones en plasma son tóxicas. El modelo TxGNN predice que podría ser efectivo para **catarata diabética**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en la autorización de AEMPS (el texto de indicación está vacío). Según el mecanismo conocido, se usa para eliminar metotrexato con concentraciones tóxicas por aclaramiento retardado |
| Nueva Indicación Predicha | Catarata diabética |
| Puntaje de Predicción TxGNN | 0,9985 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 1 de 1) |
| Número de Autorizaciones | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Glucarpidasa es una carboxipeptidasa G2 bacteriana recombinante que hidroliza el metotrexato y otros folatos en metabolitos inactivos. Su función es de rescate: reduce rápidamente el metotrexato circulante cuando el riñón no lo elimina adecuadamente. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción en DrugBank.

Con la información disponible, **la predicción no tiene un puente mecanístico plausible**. La catarata diabética se asocia con la vía de los polioles, la aldosa reductasa, la glicación y el estrés oxidativo del cristalino, y la glucarpidasa no actúa sobre ninguno de ellos. Además, es una enzima sistémica de gran tamaño, sin datos de administración ocular.

El puntaje (0,9985) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. Varios subtipos de catarata (tetánica, madura, inmadura, craneoestenosis, asociada a diabetes tipo 2) comparten exactamente el mismo puntaje (0,9983), lo que sugiere un efecto inespecífico de las similitudes aprendidas por el modelo y no una señal biológica específica. Lo mismo ocurre con la retinopatía diabética (rank 2, 0,9984), sin vínculo identificado con las vías VEGF, inflamatoria o microvascular, y con poca probabilidad de que una enzima grande cruce la barrera hematorretiniana.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1211586001 | VORAXAZE 1.000 UNIDADES POLVO PARA SOLUCION INYECTABLE (Serb) | Polvo para solución inyectable | No disponible en el registro |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 8 interacciones de nivel moderado (fuente: DDInter), todas con fármacos relacionados con el metabolismo de los folatos:
  - Leucovorina y levoleucovorina
  - Pemetrexed y pralatrexato
  - Trimetoprima y trimetrexato
  - Pirimetamina y proguanilo

  Es especialmente relevante la interacción con leucovorina/levoleucovorina, ya que estos rescatadores de folato son sustratos de la enzima.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo TxGNN (aprendizaje profundo) (L5), sin ensayos ni literatura, sin vínculo mecanístico plausible con la catarata diabética y con puntajes idénticos en múltiples subtipos que apuntan a un artefacto del modelo. Una enzima sistémica de gran tamaño tampoco tiene viabilidad ocular evidente.

**Para avanzar se necesita:**
- Datos del mecanismo de acción desde DrugBank
- Advertencias y contraindicaciones del prospecto de AEMPS (el prospecto aún no se ha analizado, lo que bloquea el cribado de seguridad)
- Texto de la indicación aprobada en la autorización española
- Evidencia preclínica que respalde algún vínculo con la vía de los polioles o el estrés oxidativo del cristalino
- Evaluación de la vía de administración y la penetración ocular, hoy sin datos de compatibilidad
- Revisión de la validez del puntaje TxGNN frente a posibles artefactos de embedding
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

