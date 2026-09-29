---
layout: default
title: Clonidine
parent: Solo predicción del modelo (L5)
nav_order: 139
evidence_level: L5
indication_count: 10
---

# Clonidine
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

# Clonidina: De Antihipertensivo (indicación no especificada en la ficha) a Síndrome Faciodigitogenital

## Resumen en Una Frase

La clonidina es un agonista alfa-2 adrenérgico de acción central, conocido como agente hipotensor y comercializado en España como Catapresan. El modelo TxGNN predice que podría ser efectiva para el **síndrome faciodigitogenital**, pero **no hay ningún ensayo clínico ni publicación** que respalde esta predicción, por lo que se trata solo de una señal del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en la ficha de AEMPS (texto de indicación vacío); farmacológicamente es un agente hipotensor |
| Nueva Indicación Predicha | Síndrome faciodigitogenital |
| Puntaje de Predicción TxGNN | 99.9993% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro del fármaco. Según la información farmacológica disponible, la clonidina actúa sobre los receptores alfa-2 adrenérgicos (subtipos A, B y C), y también se registra actividad sobre el receptor alfa-1D, los canales HCN y el transportador de cationes orgánicos 1 (OCT1). Su uso clínico conocido incluye hipertensión, profilaxis de migraña, dismenorrea grave, dolor oncológico intenso y TDAH.

**No se ha identificado un vínculo mecanístico entre la clonidina y el síndrome faciodigitogenital.** No hay ensayos, literatura ni relación evidente con la indicación original. El puntaje casi perfecto del modelo proviene solo de la estructura del grafo de conocimiento y no debe interpretarse como evidencia de eficacia.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 50669 | CATAPRESAN 0,150 mg COMPRIMIDOS | Comprimido | No especificada en los datos disponibles |

Titular: Glenwood GmbH Pharmazeutische Erzeugnisse.

## Otras Indicaciones Predichas con Más Respaldo

Para esta predicción no hay evidencia, pero el Evidence Pack incluye otras indicaciones con más respaldo. Como referencia para priorizar:

| Indicación Predicha | Nivel | Evidencia disponible | Recomendación |
|------|------|------|------|
| Síndrome de Tourette | L2 | 3 ensayos (Fase 4, n pequeños; uno comparativo clonidina vs. levetiracetam), guías europeas, metaanálisis en red y ensayo con parche de clonidina (2024) | Proceed with Guardrails |
| Trastorno bipolar maníaco | L3 | Revisión sistemática (2023), ECA adyuvante controlado con placebo (2022); único ensayo registrado terminado con n=5 | Research Question |
| Migraña | L3 | Estudios pequeños antiguos, comparación con propranolol, metaanálisis 2023 de antihipertensivos | Research Question |
| Trastorno específico del desarrollo | L4 | Evidencia indirecta (TDAH, autismo, aggressividad); ensayos en curso | Research Question |
| Tricotilomanía | L4 | Un caso clínico y datos animales | Research Question |
| Obesidad | L4 | Efecto sobre comorbilidades (hipertensión, resistencia a la insulina), no sobre el peso | Hold |
| Condroma mixoide, hipervitaminosis, microdeleción 16p11.2 | L5 | Solo predicción del modelo | Hold |

## Consideraciones de Seguridad

- **Interacciones farmacológicas:** la consulta se completó con 8 registros, pero corresponden a **dianas farmacológicas** de la clonidina y no a interacciones con otros medicamentos: receptores alfa-1D y alfa-2A/2B/2C, canales HCN1, HCN2 y HCN4 (datos de ratón) y OCT1. No se identificaron interacciones con fármacos concretos.

Consultar el prospecto para información sobre advertencias y contraindicaciones.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos clínicos, literatura ni mecanismo plausible, y el puntaje TxGNN es solo una señal basada en el grafo. Con nivel L5 no hay base para avanzar.

**Para avanzar se necesita:**
- Obtener el prospecto de AEMPS para completar la revisión de seguridad (advertencias y contraindicaciones), que actualmente bloquea el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Confirmar la indicación aprobada de Catapresan en AEMPS.
- Redirigir el esfuerzo a las indicaciones con más respaldo, en particular el **síndrome de Tourette** (L2). Ahí conviene verificar manualmente si los metaanálisis justifican L1, y aplicar como salvaguardas la monitorización de presión arterial y frecuencia cardíaca, la vigilancia de sedación y la retirada gradual para evitar hipertensión de rebote.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

