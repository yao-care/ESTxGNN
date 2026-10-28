---
layout: default
title: Necitumumab
parent: Solo predicción del modelo (L5)
nav_order: 556
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Necitumumab: nueva indicación predicha, Fibromatosis gingival (nivel de evidencia L5). Indicación original: Cáncer de pulmón no microcítico (según la base de conocimiento"
monitor_inn: "NECITUMUMAB"
predicted_indications: ["fibromatosis, gingival", "hamartoma of lung", "fibroma of lung", "pulmonary sulcus neoplasm", "lung germ cell tumor", "lung benign neoplasm", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "junctional epidermolysis bullosa"]
---

# Necitumumab
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

## Necitumumab: De Cáncer de Pulmón No Microcítico a Fibromatosis Gingival
{: .text-alpha }

## Resumen en Una Frase

Necitumumab es un anticuerpo monoclonal dirigido contra el receptor del factor de crecimiento epidérmico (EGFR), utilizado originalmente para el tratamiento del cáncer de pulmón no microcítico (en particular el de tipo escamoso).
El modelo TxGNN predice que podría ser efectivo para **fibromatosis gingival**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de pulmón no microcítico (según la base de conocimiento; el texto de indicación de la autorización no está disponible) |
| Nueva Indicación Predicha | Fibromatosis gingival |
| Puntaje de Predicción TxGNN | 0,9992 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado (registros anulados: 1 de 1) |
| Número de Autorizaciones | 1 (vigentes: 0) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según la información conocida, necitumumab es un anticuerpo monoclonal IgG1 humano que bloquea el sitio de unión del ligando del EGFR, y su eficacia en cáncer de pulmón escamoso avanzado (en combinación con gemcitabina y cisplatino) fue demostrada en el ensayo de fase 3 SQUIRE.

La relación con la fibromatosis gingival es **especulativa**. La única conexión plausible es el papel de la señalización de EGFR en la proliferación de fibroblastos, pero ningún dato aportado respalda este vínculo. El puntaje alto proviene del modelo TxGNN (aprendizaje profundo) y probablemente refleje similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni una justificación mecanística específica.

Cabe señalar que la inhibición de EGFR produce con frecuencia toxicidad cutánea y de mucosas, lo que plantea dudas sobre su idoneidad en una enfermedad de tejidos blandos como esta.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1151084001 | PORTRAZZA 800 mg concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos compilados |

Titular: Eli Lilly Nederland B.V.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (anticuerpo monoclonal anti-EGFR) |
| Riesgo de Mielosupresión | Bajo como agente único; el riesgo aumenta al combinarse con quimioterapia citotóxica (p. ej., gemcitabina y cisplatino) |
| Clasificación de Emetogenicidad | Baja como agente único (la quimioterapia asociada puede elevarla) |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (5 registradas):
  - **Talidomida**: gravedad mayor
  - **Palifermina**: gravedad moderada
  - **Idelalisib**: gravedad moderada
  - **Gemcitabina**: gravedad menor
  - Además, se registra el EGFR como diana farmacológica de necitumumab (dato de farmacología, no una interacción clínica).

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para fibromatosis gingival se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura específica, y el vínculo mecanístico es especulativo. Además, la toxicidad cutánea y de mucosas propia de los inhibidores de EGFR plantea una preocupación de seguridad.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA)
- Estudios preclínicos que evalúen el papel de EGFR en la proliferación de fibroblastos gingivales
- Revisión del prospecto de la AEMPS (advertencias y contraindicaciones), actualmente pendiente
- Evaluación del balance beneficio-riesgo frente a alternativas terapéuticas existentes para la fibromatosis gingival
- Evidencia clínica o de literatura específica que respalde la indicación predicha
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

